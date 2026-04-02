# Temporary Result Store Pattern

Covers Dimension 4: Redis as a polling/streaming result store, TTL lifecycle, key design.

## Pattern Overview

The temporary result store pattern uses Redis to hold ephemeral results from background jobs or long-running operations. A client submits work, receives a job ID, and polls until the result is ready.

**Typical flow:**
1. Client sends request → FastAPI handler dispatches background work
2. Handler returns `job_id` immediately
3. Worker processes the job, stores result in Redis with TTL
4. Client polls a status endpoint using `job_id`
5. When status is "done", client retrieves the result
6. TTL automatically cleans up the result after a configured period

## Redis Streams for Result Storage

Redis Streams provide a persistent, append-only log that supports consumer groups [16].

### Consumer Group Semantics

- Each message is delivered to exactly one consumer in a group [16]
- Consumers are auto-created on first use [16]
- The special ID `>` receives only new messages never delivered to any consumer [16]
- Using ID `0` returns pending entries for the requesting consumer (crash recovery) [16]

### Pending Entries List (PEL)

The PEL tracks unacknowledged messages per consumer [16]:
- Created on message delivery
- Persists until `XACK` acknowledgment
- On redelivery: delivery counter increments, last delivery time updates
- Deleted stream entries: PEL entry persists but payload becomes `nil`

### Crash Recovery Pattern

From official Redis documentation [16]:
1. `XREADGROUP ... STREAMS mystream 0` — recover pending messages
2. Process and `XACK` each message
3. `XREADGROUP ... STREAMS mystream >` — resume consuming new messages

### XAUTOCLAIM for Stale Message Recovery

XAUTOCLAIM (Redis 6.2+) combines `XPENDING` and `XCLAIM` with SCAN-like cursor semantics [17]:

- Transfers ownership of pending entries idle longer than `min-idle-time` (milliseconds)
- Returns `[cursor_id, [claimed_messages], [deleted_message_ids]]`
- Deleted message IDs in return value added in Redis 7.0+ [17]
- Internal scan limit: `COUNT × 10` entries per call [17]
- Default COUNT: 100 [17]
- Claiming resets idle time, preventing duplicate processing [17]
- Increments delivery counter (unless `JUSTID` flag used) [17]

### NOACK Option

Skip PEL tracking entirely with `NOACK` flag [16]. Trades reliability for performance — acceptable when message loss is tolerable for the use case.

## Key-Value Approach (Alternative to Streams)

For simpler polling scenarios, individual keys with TTL work:

```
SET job:result:{job_id} <serialized_result> EX 300
GET job:result:{job_id}
```

### Key Naming Conventions

From discovery-phase findings (not verified from full-page fetch):
- Standard format: `{object-type}:{identifier}:{sub-object}` with colon separators
- Job queue patterns: `queue:{type}:pending`, `job:{job_id}:result`, `job:{job_id}:status`
- Environment prefixing: `dev:job:123`, `prod:job:123`

## Serialization

Pipelining multiple result storage commands yields significant throughput gains [5]:
- ~4.7x speedup for batched operations (Ruby benchmark, 10k PINGs) [5]
- Up to ~10x throughput ceiling with longer pipelines [5]
- Recommended batch size: ~10,000 commands [5]

From discovery findings (unverified from full pages): MessagePack provides ~4x faster serialization than JSON with ~70% size reduction. Combining MessagePack with zlib compression can reduce fetch/deserialize time by 70% over JSON.

## TTL Lifecycle

**Setting TTL:** Every temporary result key must have a TTL to prevent memory leaks. Redis supports:
- `SET key value EX seconds` — set with TTL at creation
- `EXPIRE key seconds` — set TTL on existing key
- `PEXPIRE key milliseconds` — millisecond precision

**Sliding TTL:** Extend expiration on each access to keep active data alive while inactive data expires.

**Stream trimming:** For Streams-based result stores, use `MAXLEN` or `MINID` with `XADD` or `XTRIM` to bound memory [17]. Approximate trimming (`~` flag) is more performant than exact trimming.

## Pattern Comparison

| Approach | Persistence | Ordering | Consumer Groups | Complexity |
|----------|------------|----------|-----------------|------------|
| Key-per-result (SET/GET) | TTL-based | None | N/A | Low |
| Redis Streams | Until trimmed | Guaranteed | Yes | Medium |
| Redis List (LPUSH/BRPOP) | Until consumed | FIFO | Manual | Low |

## Gaps and Limitations

- No application-level patterns showing FastAPI polling endpoint wiring — sources cover Redis mechanics but not the HTTP layer.
- No memory overhead comparison between Streams-based and key-per-result approaches.
- Serialization performance claims (MessagePack 4x faster) from discovery snippets, not verified from full-page fetches.
- No coverage of WebSocket or SSE alternatives to HTTP polling.
- Stream MAXLEN/MINID trimming details sourced from XAUTOCLAIM docs [17], not from dedicated XADD/XTRIM documentation.
