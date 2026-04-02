# Streams vs Pub/Sub

Covers Dimension 5: Redis Streams vs Redis Pub/Sub for real-time event delivery in async Python.

## Feature Comparison

| Feature | Streams | Pub/Sub |
|---------|---------|---------|
| Delivery guarantee | At-least-once (via PEL + XACK) [16] | At-most-once [6] |
| Persistence | Yes (stream is a data structure) [16] | None [6] |
| Consumer groups | Yes (load balancing, per-consumer tracking) [16] | No (broadcast to all subscribers) [6] |
| Crash recovery | Yes (PEL, XAUTOCLAIM) [16][17] | No [6] |
| Message replay | Yes (read from any position) [16] | No [6] |
| Buffering | Yes (stream stores all messages until trimmed) [16] | No (fire-and-forget) [6] |
| Acknowledgment | Yes (XACK) [16] | No [6] |
| Late subscriber | Can read historical messages [16] | Misses all prior messages [6] |
| Pattern matching | No | Yes (PSUBSCRIBE with glob patterns) [6] |
| Cluster scaling | Standard slot-based | Sharded Pub/Sub (Redis 7.0+) [6] |
| Storage overhead | Higher (data structure + PEL) | None |
| Latency | Slightly higher (persistence overhead) | Lower (no storage) |

## Pub/Sub Semantics

### At-Most-Once Delivery

"Messages delivered once if at all. No persistence, no retries. If subscriber disconnected, message permanently lost" [6].

### Message Ordering

"Subscribers receive messages in order published" [6].

### Subscribed Client Restrictions

A subscribed client can only issue: PING, (P|S)SUBSCRIBE, (P|S)UNSUBSCRIBE, QUIT, RESET [6].
Exception: RESP3 protocol allows any commands in subscribed state [6].

### Duplicate Message Risk

A client subscribed to both a specific channel AND a matching pattern receives duplicate messages — one `message` event and one `pmessage` event [6].

### No Database Isolation

"Publishing on db 10 is heard by subscribers on db 1" [6]. Best practice: prefix channels with environment names (`test:notifications`, `production:notifications`) [6].

## Streams Semantics

### Consumer Groups

Each message delivered to exactly one consumer in a group. Consumers auto-created on first use [16].

### Pending Entries List (PEL)

Tracks unacknowledged messages per consumer [16]:
- Created on message delivery
- Persists until `XACK`
- On redelivery: counter increments, last delivery time updates
- Enables crash recovery and message claiming

### Crash Recovery

Official recovery pattern [16]:
1. Read pending: `XREADGROUP ... STREAMS mystream 0`
2. Process and acknowledge: `XACK`
3. Resume new: `XREADGROUP ... STREAMS mystream >`

### XAUTOCLAIM (Redis 6.2+)

Simplifies retry handling by combining `XPENDING` + `XCLAIM` [17]:
- Scans PEL for entries idle > `min-idle-time` (milliseconds)
- Cursor-based iteration (returns `0-0` when scan complete)
- Internal scan limit: `COUNT × 10` entries
- Delivery counter incremented (tracks retry count)
- Automatic cleanup of deleted messages from PEL
- Redis 7.0+ adds deleted message IDs to return value

### NOACK Mode

Skip PEL tracking for fire-and-forget Streams consumption [16]. Trades reliability for performance — semantics become similar to Pub/Sub but with persistence.

## Sharded Pub/Sub (Redis 7.0+)

Traditional Pub/Sub in Redis Cluster broadcasts messages to all nodes. Sharded Pub/Sub addresses this by limiting propagation [6]:

- Commands: `SSUBSCRIBE`, `SUNSUBSCRIBE`, `SPUBLISH`
- Shard channels assigned to slots using the same hash algorithm as keys
- "Published messages only forwarded within shard (not cluster-wide)" [6]
- "Reduces cluster bus traffic significantly" [6]
- Enables horizontal scaling

From discovery findings: traditional Pub/Sub cluster throughput limited to `network_bandwidth / (nodes × message_size)`. Example: 10-node cluster, 1KB messages, 1Gbit/s → max ~12.5K RPS (unverified from full-page fetch).

## Use Case Decision Guide

| Use Case | Recommended | Rationale |
|----------|-------------|-----------|
| Cache invalidation across instances | Pub/Sub | Best-effort is sufficient; TTL provides safety net. Low overhead [6] |
| Real-time notifications (chat, dashboards) | Pub/Sub | Low latency, broadcast semantics, message loss acceptable [6] |
| Job/task queues | Streams | At-least-once delivery, consumer groups for load balancing [16] |
| Event sourcing / audit logs | Streams | Persistence, replay capability, ordered log [16] |
| Temporary result store | Streams or Key-per-result | Depends on whether consumer groups and ordering needed [16] |
| Microservice communication | Streams | Reliability and replay needed for cross-service events [16] |

## Gaps and Limitations

- No Python-specific performance benchmarks comparing Streams vs Pub/Sub throughput or latency.
- No data on how `XREADGROUP BLOCK` interacts with asyncio event loops (does it require dedicated connections?).
- Sharded Pub/Sub cluster throughput calculation from discovery phase only (unverified).
- No coverage of Redis Streams consumer group lag monitoring (`XINFO GROUPS` lag metric, Redis 7+).
- Missing: dead-letter queue patterns (what to do with messages exceeding retry threshold).
