# Redis Caching Patterns for Async Python

Citation-backed analysis of Redis integration patterns for FastAPI + asyncpg applications.

## TL;DR

Use `redis.asyncio` (redis-py 4.2+) with `BlockingConnectionPool` for async Redis. Cache-aside with TTL is the primary pattern; combine with Pub/Sub for multi-instance invalidation. For cache-only deployments, use `allkeys-lru` eviction with persistence disabled. Monitor via `oliver006/redis_exporter` + Prometheus.

## Key Findings

| Question | Answer |
|----------|--------|
| Which async client? | `redis.asyncio` (aioredis merged into redis-py 4.2.0rc1+) |
| Which pool type? | `BlockingConnectionPool` (prevents connection exhaustion under concurrency) |
| Pipeline benefit? | ~4.7x speedup (10k commands), up to ~10x with longer pipelines |
| Caching pattern? | Cache-aside + write-through. Update DB first, then delete cache key |
| Invalidation? | TTL primary + Pub/Sub for multi-instance coordination (at-most-once) |
| Stampede protection? | cashews (early refresh) or manual distributed locking |
| Streams vs Pub/Sub? | Streams for reliability/replay; Pub/Sub for broadcast/low-latency |
| Eviction policy? | `allkeys-lru` (general) or `allkeys-lfu` (skewed access) |
| Persistence? | Disable for pure cache (`save ""`, `appendonly no`) |
| Monitoring? | redis_exporter → Prometheus. Alert on fragmentation >1.5, eviction rate |
| Valkey compatible? | Yes — redis-py works with Valkey without modification |

## Quick Decision Framework

1. **Is message loss acceptable?** → Pub/Sub. Otherwise → Streams
2. **Is access pattern skewed (80/20)?** → `allkeys-lfu`. Otherwise → `allkeys-lru`
3. **Need stampede protection?** → cashews (early refresh). Otherwise → fastapi-cache2
4. **Is Redis the source of truth?** → Enable persistence (AOF). Otherwise → cache-only (disable)
5. **Need temporary result store?** → Key-per-result (simple) or Streams (with recovery)

## Files

| File | Contents |
|------|----------|
| [redis-async-python.md](redis-async-python.md) | Full analysis with methodology |
| [citations.md](citations.md) | All 21 sources, numbered and tiered |
| [references/async-client-ecosystem.md](references/async-client-ecosystem.md) | redis-py, aioredis merger, Valkey, caching libraries |
| [references/caching-patterns-fastapi.md](references/caching-patterns-fastapi.md) | Cache-aside, write-through, FastAPI integration |
| [references/cache-invalidation.md](references/cache-invalidation.md) | TTL, Pub/Sub, tag-based, stampede prevention |
| [references/temporary-result-store.md](references/temporary-result-store.md) | Polling pattern, Streams, key design |
| [references/streams-vs-pubsub.md](references/streams-vs-pubsub.md) | Feature comparison, use case guide |
| [references/operational-considerations.md](references/operational-considerations.md) | Eviction, persistence, memory, monitoring |
| [references/connection-lifecycle.md](references/connection-lifecycle.md) | Pool sizing, retry, circuit breaker, degradation |
| [audit/citation-audit.md](audit/citation-audit.md) | Independent citation verification |
| [audit/consistency-review.md](audit/consistency-review.md) | Cross-file consistency check |
