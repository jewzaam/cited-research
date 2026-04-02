# Redis Caching Patterns for Async Python

A citation-backed analysis of Redis caching patterns, client libraries, and operational practices for async Python applications built on FastAPI + asyncpg.

## Methodology

This document was produced using the cited-research methodology: every factual claim traces to a web source visited in-session. Two independent review agents audited the output — one checking citations against source content, the other checking cross-file numerical and logical consistency. See [citations.md](citations.md) for all sources.

Seven research dimensions were investigated:
1. Async Redis Client Ecosystem
2. Caching Patterns & FastAPI Integration
3. Cache Invalidation Strategies
4. Temporary Result Store Pattern
5. Streams vs Pub/Sub
6. Operational Considerations
7. Connection Lifecycle & Error Handling

---

## 1. Async Redis Client Ecosystem

### The Canonical Client: redis-py

The standalone `aioredis` library was merged into redis-py starting with version 4.2.0rc1 [13]. The last standalone aioredis release was v2.0.1 in December 2021 [13]. All async Redis work in Python should use `redis.asyncio`:

```python
import redis.asyncio as redis
```

redis-py provides two connection pool types [21]:

| Pool Type | Default max_connections | Exhaustion Behavior |
|-----------|----------------------|---------------------|
| `ConnectionPool` | 2^31 (effectively unlimited) | Raises `ConnectionError` |
| `BlockingConnectionPool` | 50 | Waits up to 20 seconds |

`BlockingConnectionPool` is recommended for async applications to prevent connection exhaustion under high concurrency [21].

### Pool Lifecycle

The `Redis.from_pool(pool)` method gives the Redis instance ownership of the pool — calling `aclose()` closes both [21]. Without `from_pool`, the pool stays open after `aclose()` and must be manually closed [21]. Explicit cleanup via `await redis.aclose()` is recommended for async clients [13].

### Pipeline Batching

Pipelining sends multiple commands in a single round trip. Official benchmark (Ruby client, 10,000 PINGs): **~4.7x speedup** (1.185s → 0.251s) [5]. Throughput increases "almost linearly with longer pipelines, eventually reaching ~10x baseline throughput" [5]. Recommended batch size: ~10,000 commands to bound server memory [5].

By default, `pipeline(transaction=True)` wraps commands in `MULTI/EXEC` for atomic execution. Set `transaction=False` for pure batching [21].

### Valkey Compatibility

Valkey is a Redis fork under Linux Foundation stewardship (BSD license). Two Python clients exist [20]:

- **valkey-glide** v2.1.1 (Apache-2.0): Rust core, PubSub State Restoration, Cluster Scan
- **valkey-py** v6.1.0 (MIT): Fork of redis-py, Persistent Connection Pool

Both support Redis OSS 7.2+ and Valkey 7.2+ [20]. Standard redis-py works with Valkey without modification due to protocol compatibility [20].

### Caching Libraries

| Library | Version | Strategies | Tag Invalidation | Stampede Protection |
|---------|---------|------------|-------------------|---------------------|
| fastapi-cache2 | 0.2.2 (Jul 2024) | Simple TTL | Namespace only | No |
| cashews | — | Simple, failover, early refresh, soft TTL | Yes | Yes (early refresh) |

Sources: [18][19]

cashews provides richer caching strategies including failover (return cached value on exception) and early refresh (proactive background refresh before expiration) [19]. fastapi-cache2 is simpler — decorator-based with ETag/Cache-Control support [18].

---

## 2. Caching Patterns

### Cache-Aside (Lazy Loading)

The most common pattern. Application checks cache first; on miss, queries the database, populates cache, returns data [8][9].

- Advantage: "Cache contains only requested data (cost-effective)" [8]
- Disadvantage: "Initial response time overhead on miss (extra roundtrips)" [8]
- No consistency guarantee — external changes to the data store are invisible until TTL expires [9]

### Write-Through

Cache updated immediately when the primary database is updated. "Almost always implemented alongside lazy loading" [8].

- Advantage: "Cache stays up-to-date, greater likelihood of hits" [8]
- Disadvantage: "Infrequently-requested data also cached (larger cache)" [8]

**Best practice:** "Combine write-through and lazy loading with appropriate expiration" [8].

### Write-Side Ordering

"Update data store first, then invalidate cache (delete key). Order matters: update store BEFORE removing cache to avoid stale data window" [9]. Reversing this order allows a concurrent request to refill the cache with stale data.

### FastAPI Integration

**Decorator-based** (fastapi-cache2): `@cache(expire=60)` on endpoints. Initialize via lifespan: `FastAPICache.init(RedisBackend(redis))` [18].

**Strategy-based** (cashews): `@cache(ttl="3h", key="user:{request.user.uid}")` with failover, early refresh, and soft TTL strategies [19].

**Dependency injection:** Create a `CacheService` dependency wrapping Redis operations, inject via `Depends()`. Use FastAPI's lifespan context manager for connection lifecycle (replaces deprecated `@app.on_event`).

---

## 3. Cache Invalidation

### Invalidation Types

Redis documentation defines four approaches [10]:

| Type | Mechanism | Use Case |
|------|-----------|----------|
| Time-based | TTL expiration | Most common; safety net for all other strategies |
| Event-based | System event trigger | Data updates (e.g., blog post edited) |
| Command-based | Explicit action with dependency IDs | User-initiated operations |
| Group-based | Invalidate by category/tag | Related data (e.g., all "politics" articles) |

### TTL Strategy

| Data Type | Recommended TTL |
|-----------|----------------|
| Static content | 1 year minimum [10] |
| Frequently updated | Minutes to 1 hour [10] |
| Dynamic content | Shorter expiration [10] |

"Expiration policy must match access patterns. Not too short (constant reloads), not too long (stale data)" [9].

**TTL jitter:** Add random offset to prevent synchronized expiration (cache stampede).

### Pub/Sub for Multi-Instance Invalidation

Pub/Sub broadcasts invalidation signals across application instances [6]. Critical limitation: at-most-once delivery — "if subscriber disconnected, message permanently lost" [6]. Use Pub/Sub for best-effort invalidation with TTL as a safety net.

Sharded Pub/Sub (Redis 7.0+) restricts message propagation to the owning shard, reducing cluster bus traffic [6].

### Tag-Based Invalidation

cashews supports built-in tag-based invalidation [19], mapping to Redis's "dependency ID" concept [10]. fastapi-cache2 offers namespace-based organization but not true tag-based invalidation [18].

### Cache Stampede Prevention

| Strategy | Description | Library Support |
|----------|-------------|-----------------|
| TTL jitter | Random TTL offset | Manual |
| Distributed locking | SET NX — one rebuilds, others wait | Manual |
| Early refresh | Background refresh before expiration | cashews [19] |
| Stale-while-revalidate | Serve stale while refreshing | cashews (soft TTL) [19] |

---

## 4. Temporary Result Store Pattern

Redis can serve as an ephemeral result store for background jobs or long-running operations. Two approaches are viable:

### Key-per-Result (Simple)

```
SET job:result:{job_id} <payload> EX 300
GET job:result:{job_id}
```

Low complexity. TTL handles automatic cleanup. No ordering or consumer group semantics.

### Streams-Based (Advanced)

Redis Streams provide persistence, consumer groups, and crash recovery [16]:

- Each message delivered to exactly one consumer in a group [16]
- PEL (Pending Entries List) tracks unacknowledged messages [16]
- Crash recovery: read pending (ID `0`), process and `XACK`, then resume new (ID `>`) [16]
- XAUTOCLAIM (Redis 6.2+) simplifies retry by combining `XPENDING` + `XCLAIM` with cursor semantics [17]

**XAUTOCLAIM details:** Scans PEL for entries idle > `min-idle-time` (ms). Internal scan limit: `COUNT × 10` entries. Default COUNT: 100. Increments delivery counter for retry tracking [17].

### Pattern Comparison

| Approach | Persistence | Consumer Groups | Crash Recovery | Complexity |
|----------|------------|-----------------|----------------|------------|
| Key-per-result | TTL-based | N/A | No | Low |
| Streams | Until trimmed [16] | Yes [16] | Yes (PEL) [16][17] | Medium |

---

## 5. Streams vs Pub/Sub

| Feature | Streams | Pub/Sub |
|---------|---------|---------|
| Delivery | At-least-once (PEL + XACK) [16] | At-most-once [6] |
| Persistence | Yes [16] | None [6] |
| Consumer groups | Yes [16] | No (broadcast) [6] |
| Crash recovery | Yes (PEL, XAUTOCLAIM) [16][17] | No [6] |
| Message replay | Yes [16] | No [6] |
| Late subscriber | Reads history [16] | Misses everything [6] |
| Storage overhead | Higher | None |

### When to Use Each

- **Pub/Sub:** Cache invalidation, real-time notifications, chat — where message loss is acceptable and low latency matters [6]
- **Streams:** Job queues, event sourcing, result stores — where reliability, replay, and load balancing are needed [16]

### Sharded Pub/Sub (Redis 7.0+)

Traditional Pub/Sub broadcasts to all cluster nodes. Sharded Pub/Sub limits propagation to the owning shard [6]:
- Commands: `SSUBSCRIBE`, `SUNSUBSCRIBE`, `SPUBLISH`
- "Reduces cluster bus traffic significantly" [6]

---

## 6. Operational Considerations

### Eviction Policy Selection

For a cache-only deployment, `allkeys-lru` is the recommended default for most workloads (power-law/Pareto access patterns) [1]. If access is highly skewed with stable hot data, `allkeys-lfu` (Redis 4.0+) is better [14].

**Critical gotcha:** "volatile-* policies behave like noeviction if no keys have TTL set" [1].

Redis uses **approximated** LRU/LFU via sampling (`maxmemory-samples` default: 5). Value 10 is "very close to true LRU" [1].

### LFU Tuning

`lfu-log-factor` (default 10) controls how many hits saturate the counter [1]:

| factor | 100 hits | 1K hits | 100K hits | 1M hits |
|--------|----------|---------|-----------|---------|
| 0 | 104 | 255 | 255 | 255 |
| 1 | 18 | 49 | 255 | 255 |
| 10 | 10 | 18 | 142 | 255 |
| 100 | 8 | 11 | 49 | 143 |

`lfu-decay-time` (default 1 minute): counter decays by 1 every N minutes. Set to 0 to never decay [1].

### Persistence for Cache-Only

Disable both RDB and AOF: `save ""`, `appendonly no` [2]. This eliminates fork latency and I/O overhead. Data loss on restart is acceptable — the database is the source of truth.

| Configuration | Max Data Loss |
|---------------|---------------|
| Cache-only (no persistence) | All data |
| RDB only | 5+ minutes |
| AOF everysec | ~1 second |
| Hybrid (RDB + AOF) | ~1 second |

Source: [2]

### Memory Optimization

Compact encodings (listpack in Redis 7.0+) save "up to 10x less memory (average 5x)" [7]. Sharding objects into hashes (~100 fields each) reduced 100,000 objects from 11 MB to 1.7 MB — **6.5x savings** [7].

Plan for peak memory, not average. Memory is not returned to the OS when keys are deleted [7].

### Monitoring

**Key metrics** from `INFO` command [11]:
- Cache hit ratio: `keyspace_hits / (keyspace_hits + keyspace_misses) * 100` [1]
- `mem_fragmentation_ratio`: healthy 1.0-1.5, concerning >1.5 [11]
- `evicted_keys`: indicator of memory pressure [11]
- `rejected_connections`: `maxclients` exhausted [11]

**Prometheus:** `oliver006/redis_exporter` on port 9121. Supports Valkey 7.x-9.x and Redis. Exports INFO metrics plus per-database stats [12].

---

## 7. Connection Lifecycle & Error Handling

### Production Configuration

Official redis-py recommendations [4]:

| Parameter | Default | Recommended |
|-----------|---------|-------------|
| `socket_connect_timeout` | 10s | 15s |
| `socket_timeout` | 10s | 5s |
| `health_check_interval` | — | 3s |
| Retry attempts | 3 | 3 (default adequate) |

Default retry: 3 attempts with ExponentialBackoff and jitter, retrying on `ConnectionError` and `TimeoutError` [4].

### Pool Sizing

- `BlockingConnectionPool` with explicit `max_connections` is recommended for async [21]
- Sizing rule of thumb: 2-3x expected peak concurrent requests [15]
- Official guidance: "Start with a small pool; let it grow dynamically. Monitor actual connection usage" [3]

### Retry and Circuit Breaker

**Built-in retry** (redis-py): `Retry(ExponentialBackoff(), retries)` with configurable error types [4].

**External retry** (Tenacity): `AsyncRetrying` with `wait_exponential()` for more sophisticated backoff [15].

**Circuit breaker pattern:** Three states — closed (normal), open (rejecting), half-open (testing recovery). Prevents cascading failures when Redis is unavailable [15].

### Graceful Degradation Stack

1. **Retry** with exponential backoff masks transient failures [4]
2. **Circuit breaker** prevents thundering herd on sustained failures [15]
3. **Stale cache fallback** returns old data instead of errors
4. **Health checks** (`health_check_interval`) detect problems early [4]
5. **Monitoring** via OpenTelemetry for observability [4]

---

## Limitations and Caveats

### Source Accessibility

redis-py readthedocs returned 403 on all fetch attempts (AI crawler blocking). Connection pool details, retry API documentation, and async examples were sourced from WebSearch snippets and GitHub issues [21] rather than the canonical documentation pages.

### Unverified Claims

The following claims from the discovery phase were not verified against full-page fetches:
- MessagePack serialization performance (4x faster, 70% smaller than JSON)
- Pub/Sub cluster throughput formula (network_bandwidth / nodes × message_size)
- Per-key memory overhead (40-50 bytes — discovery sources varied from 40 to 90 bytes)

### Benchmark Limitations

The pipeline benchmark (~4.7x speedup) was conducted with the Ruby Redis client using PING commands [5]. Python-specific async pipeline performance may differ due to asyncio overhead. The "~10x" throughput ceiling is stated without specifying pipeline depth or conditions [5].

### Marketing Claims

- cashews "10x faster" client-side caching: no benchmark methodology, sample size, or conditions [19]
- Ulta Beauty "40% revenue increase" with Redis LFU: marketing case study, revenue not attributable to caching alone [14]

---

## Decision Framework

### Quick-Start Configuration for FastAPI + asyncpg

1. **Client:** `redis.asyncio` with `BlockingConnectionPool` (max_connections = 2-3x peak concurrent requests)
2. **Caching pattern:** Cache-aside with TTL. Consider cashews for stampede protection (early refresh)
3. **Invalidation:** TTL-based primary, Pub/Sub secondary for multi-instance coordination
4. **Eviction:** `allkeys-lru` for general caching, `allkeys-lfu` if access is highly skewed
5. **Persistence:** Disable (`save ""`, `appendonly no`) for pure cache use
6. **Monitoring:** `oliver006/redis_exporter` → Prometheus → alerts on fragmentation, eviction rate, hit ratio
7. **Resilience:** Built-in `Retry(ExponentialBackoff(), 3)` + circuit breaker for production

### Streams vs Pub/Sub Decision

- Need reliability, replay, or load balancing? → **Streams** [16]
- Need broadcast, low latency, fire-and-forget? → **Pub/Sub** [6]
- Cache invalidation across instances? → **Pub/Sub** + TTL safety net [6]
- Temporary result store with recovery? → **Streams** with consumer groups [16]
