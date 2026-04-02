# Async Redis Client Ecosystem

Covers Dimension 1: redis-py async, aioredis merger, connection pooling, pipeline batching, and alternatives (Valkey, caching libraries).

## aioredis Merger into redis-py

The standalone `aioredis` library was merged into `redis-py` starting with version 4.2.0rc1 [13]. The last standalone aioredis release was v2.0.1 in December 2021 [13]. The library is now abandoned and located at `github.com/aio-libs-abandoned/aioredis-py` [13].

**Current import paths:**
- `from redis import asyncio as aioredis` (compatibility alias)
- `import redis.asyncio as redis` (preferred)

Installation: `pip install redis>=4.2.0rc1` [13].

## redis-py Async API

redis-py is the canonical async Redis client for Python. Key characteristics:

| Feature | Detail | Source |
|---------|--------|--------|
| Async module | `redis.asyncio` | [13] |
| Pipeline API | Identical sync/async interface | [21] |
| Pipeline default | `transaction=True` (MULTI/EXEC wrapping) | [21] |
| Connection pools | `ConnectionPool`, `BlockingConnectionPool` | [21] |
| Pool ownership | `Redis.from_pool()` transfers ownership | [21] |
| Cleanup | `await redis.aclose()` recommended for async clients | [13][21] |

### Connection Pool Types

| Pool Type | Default max_connections | Exhaustion Behavior |
|-----------|----------------------|---------------------|
| `ConnectionPool` | 2^31 (2,147,483,648) — effectively unlimited | Raises `ConnectionError` |
| `BlockingConnectionPool` | 50 | Waits up to `timeout` seconds (default: 20s) |

Source: [21]

`BlockingConnectionPool` is recommended for async applications to avoid "Too many connections" errors under high concurrency [21].

### from_pool vs connection_pool

| Pattern | Pool Ownership | `aclose()` Behavior |
|---------|---------------|---------------------|
| `Redis.from_pool(pool)` | Redis instance owns pool | Closes pool |
| `Redis(connection_pool=pool)` | Caller owns pool | Leaves pool open |
| `Redis()` (no pool arg) | Internal pool created | Closes internal pool |

Source: [21]

## Pipeline Batching

Pipelining sends multiple commands in a single network round trip [5].

**Benchmark** (Ruby Redis client, 10,000 PINGs) [5]:
- Without pipelining: 1.185238 seconds
- With pipelining: 0.250783 seconds
- Speedup: **~4.7x**

Beyond RTT reduction, pipelining reduces syscall overhead (fewer `read()`/`write()` context switches). Throughput increases "almost linearly with longer pipelines, eventually reaching ~10x baseline throughput" [5].

**Batching recommendation:** Send in batches of ~10,000 commands to bound server-side memory usage [5].

**Pipeline vs Scripting:** Use pipelining for write-heavy or independent commands. Use Lua scripting (EVAL) for read-compute-write patterns where intermediate results are needed [5].

## Valkey Compatibility

Valkey is a Redis fork under Linux Foundation stewardship (BSD license). Two Python clients exist [20]:

| Client | Version | Release | License | Distinctive Features |
|--------|---------|---------|---------|---------------------|
| valkey-glide | v2.1.1 | 2025-10-08 | Apache-2.0 | PubSub State Restoration, Cluster Scan, AZ-Based Read |
| valkey-py | v6.1.0 | 2025-02-11 | MIT | Persistent Connection Pool |

Both support Redis OSS 7.2+ and Valkey 7.2+ [20]. Neither supports client-side caching [20]. Standard redis-py works with Valkey without modification due to protocol compatibility [20].

## FastAPI Caching Libraries

### fastapi-cache2

| Property | Value |
|----------|-------|
| Version | 0.2.2 (July 24, 2024) |
| Python | >=3.8, <4.0 |
| License | Apache-2.0 |
| Backends | Redis, Memcached, DynamoDB, in-memory |

Decorator-based: `@cache(expire=60)` on endpoints. Supports ETag and Cache-Control HTTP headers [18].

### cashews

Async-native caching library with richer strategy support than fastapi-cache2 [19]:

| Strategy | Description |
|----------|-------------|
| Simple cache | Basic TTL-based caching |
| Failover | Return cached value on exception |
| Early refresh | Proactive background refresh before expiration |
| Soft TTL | Graceful degradation allowing stale data |

Additional features: tag-based invalidation, Bloom filters, compression (gzip, zlib), TTL string syntax ("2h5m") [19].

The project claims client-side caching is "10x faster than simple cache with redis" — this is unsubstantiated with no benchmark methodology provided [19].

## Gaps and Limitations

- redis-py readthedocs returned 403 (AI crawler blocking) — detailed async API documentation not directly verified.
- Pipeline benchmark is Ruby-based; Python-specific async pipeline performance not measured in available sources.
- cashews adoption metrics and version history not captured.
- No coverage of alternative clients (coredis, aredis) or in-process caches (cachetools, aiocache) beyond brief discovery mentions.
