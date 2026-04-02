# Citations

All sources visited in-session via WebSearch or WebFetch on 2026-04-02.

**[1]** "Using Redis key eviction." *Redis Documentation*.
<https://redis.io/docs/latest/develop/reference/eviction/>
**Tier:** 2
Data extracted: Complete list of 10 eviction policies, maxmemory configuration defaults (64-bit: 0/unlimited, 32-bit: 3GB), maxmemory-samples default (5), LFU lfu-log-factor table, lfu-decay-time default (1 minute), LRM policy (Redis 8.6+), policy selection guidance, monitoring metrics and cache hit ratio formula.

**[2]** "Persistence." *Redis Documentation*.
<https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/>
**Tier:** 2
Data extracted: RDB and AOF configuration, appendfsync options (always/everysec/no), data loss characteristics by configuration (RDB: 5+ min, AOF everysec: ~1s, AOF always: none, cache-only: all), hybrid persistence recommendation, Redis 7.0+ multi-part AOF, cache-only config (save "", appendonly no).

**[3]** "Connection pools and multiplexing." *Redis Documentation*.
<https://redis.io/docs/latest/develop/clients/pools-and-muxing/>
**Tier:** 2
Data extracted: Connection pooling workflow (borrow/return), multiplexing concepts, pool sizing guidance (start small, grow dynamically), redis-py supports pooling (not multiplexing).

**[4]** "Production usage." *Redis Documentation (redis-py)*.
<https://redis.io/docs/latest/develop/clients/redis-py/produsage/>
**Tier:** 2
Data extracted: socket_connect_timeout default (10s, recommended 15), socket_timeout default (10s, recommended 5), health_check_interval (recommended 3), default retry (3 attempts with ExponentialBackoff and jitter), supported errors (ConnectionError, TimeoutError), production checklist.

**[5]** "Pipelining." *Redis Documentation*.
<https://redis.io/docs/latest/develop/using-commands/pipelining/>
**Tier:** 2
Data extracted: Pipeline benchmark (Ruby, 10k PINGs: 1.185s without vs 0.251s with, ~4.7x speedup), syscall optimization explanation, ~10x throughput ceiling with longer pipelines, 10k command batch size recommendation, pipelining vs scripting trade-offs.

**[6]** "Pub/Sub." *Redis Documentation*.
<https://redis.io/docs/latest/develop/pubsub/>
**Tier:** 2
Data extracted: At-most-once delivery semantics, message ordering, subscribed client command restrictions, pattern matching (PSUBSCRIBE), duplicate risk with channel + pattern subscriptions, no key space relation, Sharded Pub/Sub (Redis 7.0+) with SSUBSCRIBE/SPUBLISH, explicit limitations list (no persistence, no acknowledgment, no buffering).

**[7]** "Memory optimization." *Redis Documentation*.
<https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/memory-optimization/>
**Tier:** 2
Data extracted: Compact encoding savings (up to 10x, average 5x), hash-max-listpack-entries/value thresholds by version, memory savings example (100k objects: 1.7 MB with hashes vs 11 MB direct keys = 6.5x), bitmap efficiency (100M users = 12 MB), memory not freed to OS on key deletion.

**[8]** "Database Caching Strategies Using Redis — Caching Patterns." *AWS Whitepapers*.
<https://docs.aws.amazon.com/whitepapers/latest/database-caching-strategies-using-redis/caching-patterns.html>
**Tier:** 1
Data extracted: Cache-aside definition (reactive, on-demand), write-through definition (proactive, immediate update), best practice to combine both with expiration, advantages/disadvantages of each.

**[9]** "Cache-Aside pattern." *Azure Architecture Center, Microsoft*.
<https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside>
**Tier:** 2
Data extracted: Write-side ordering (update store BEFORE invalidating cache), TTL matching access patterns, cache priming at startup, consistency limitations, when to use/not use cache-aside.

**[10]** "Cache invalidation." *Redis Glossary*.
<https://redis.io/glossary/cache-invalidation/>
**Tier:** 2
Data extracted: Four invalidation types (time-based, event-based, command-based, group-based), dependency ID concept, TTL recommendations by data type (static: 1 year per Google, frequently updated: minutes to 1 hour, dynamic: shorter).

**[11]** "INFO." *Redis Command Reference*.
<https://redis.io/docs/latest/commands/info/>
**Tier:** 2
Data extracted: Complete section list, memory metrics (used_memory, used_memory_rss, mem_fragmentation_ratio, allocator_frag_ratio), stats metrics (keyspace_hits/misses, evicted_keys, expired_keys, instantaneous_ops_per_sec, rejected_connections), fragmentation threshold (>1.5).

**[12]** "redis_exporter." oliver006. *GitHub*.
<https://github.com/oliver006/redis_exporter>
**Tier:** 2
Data extracted: Supports Valkey 7.x-9.x and Redis, default port 9121, exports INFO metrics plus per-database keys/expiring/avg_ttl, --check-keys flag, Lua script custom metrics, multi-target scraping, TLS support.

**[13]** "What is the difference between aioredis v2.0 and redis-py asyncio?" *Redis FAQ*.
<https://redis.io/faq/doc/26366kjrif/what-is-the-difference-between-aioredis-v2-0-and-redis-py-asyncio>
**Tier:** 2
Data extracted: aioredis v2.0.1 last release December 2021, abandoned. Merged into redis-py 4.2.0rc1+. Import: `from redis import asyncio as aioredis`.

**[14]** "LFU vs LRU: How to Choose the Right Cache Eviction Policy." *Redis Blog*.
<https://redis.io/blog/lfu-vs-lru-how-to-choose-the-right-cache-eviction-policy/>
**Tier:** 2
Data extracted: LFU vs LRU comparison (frequency vs recency), use case guidance (LFU: skewed/predictable workloads; LRU: dynamic/bursty), Morris counter with decay, per-database eviction in Redis Enterprise.
Note: Ulta Beauty case study (2s→1ms, "40% revenue increase") is a marketing claim without independent verification. Revenue figure not attributable to caching alone.

**[15]** Akarshan. "Building a Robust Redis Client with Retry Logic in Python." *Dev.to*.
<https://dev.to/akarshan/building-a-robust-redis-client-with-retry-logic-in-python-jeg>
**Tier:** 3
Data extracted: Tenacity AsyncRetrying with wait_exponential, circuit breaker pattern (closed/open/half-open), pool sizing guidance (2-3x concurrent requests), health_check_interval=30, graceful degradation stack (retry → circuit breaker → backoff → health checks), asyncio.Lock singleton pattern.
Note: health_check_interval=30 contradicts official recommendation of 3 [4]. Blog post, not peer-reviewed.

**[16]** "XREADGROUP." *Redis Command Reference*.
<https://redis.io/docs/latest/commands/xreadgroup/>
**Tier:** 2
Data extracted: Consumer group semantics (one message per consumer), PEL (Pending Entries List) lifecycle, special ID ">" for new messages, NOACK option, CLAIM option (Redis 8.4+), crash recovery pattern (read pending with 0, then resume with >), deleted entry behavior (PEL persists, payload nil).

**[17]** "XAUTOCLAIM." *Redis Command Reference*.
<https://redis.io/docs/latest/commands/xautoclaim/>
**Tier:** 2
Data extracted: Available since Redis 6.2.0, combines XPENDING+XCLAIM, SCAN-like cursor semantics, min-idle-time in milliseconds, internal scan limit (COUNT × 10), delivery counter increment, automatic PEL cleanup of deleted messages, default COUNT 100, deleted_message_ids in return (Redis 7.0+).

**[18]** "fastapi-cache2." long2ice. *PyPI*.
<https://pypi.org/project/fastapi-cache2/>
**Tier:** 2
Data extracted: Version 0.2.2 (July 24, 2024), Python >=3.8 <4.0, Apache-2.0 license, backends (Redis, Memcached, DynamoDB, in-memory), @cache(expire=60) decorator, ETag/Cache-Control support.

**[19]** Krukov. "cashews." *GitHub*.
<https://github.com/Krukov/cashews>
**Tier:** 3
Data extracted: Async caching library, backends (in-memory LRU, Redis, DiskCache), TTL string format ("2h5m"), strategies (simple, failover, early refresh, soft TTL), tag-based invalidation, Bloom filters, compression (gzip, zlib).
Note: "10x faster" client-side caching claim is unsubstantiated — no benchmark methodology provided.

**[20]** "Clients." *Valkey Documentation*.
<https://valkey.io/clients/>
**Tier:** 2
Data extracted: valkey-glide v2.1.1 (2025-10-08, Apache-2.0), valkey-py v6.1.0 (2025-02-11, MIT), feature comparison matrix, both support Redis OSS 7.2+ / Valkey 7.2+, neither has client-side caching.

**[21]** redis-py connection pool details. *WebSearch compilation from GitHub issues and documentation*.
<https://github.com/redis/redis-py/issues/2517>, <https://github.com/redis/redis-py/issues/2220>, <https://github.com/redis/redis-py/issues/341>
**Tier:** 4
Data extracted: ConnectionPool default max_connections = 2^31 (effectively unlimited), BlockingConnectionPool default max_connections = 50 with timeout = 20s, from_pool() ownership semantics, pipeline transaction=True default (MULTI/EXEC wrapping), WATCH optimistic locking.
