# Caching Patterns & FastAPI Integration

Covers Dimension 2: cache-aside, write-through, write-behind patterns and their mapping to FastAPI.

## Cache-Aside (Lazy Loading)

The most common caching pattern. The application manages the cache explicitly [8][9].

**Flow:**
1. Application checks cache
2. On hit: return cached data
3. On miss: query database, populate cache with TTL, return data

**Advantages:**
- "Cache contains only requested data (cost-effective)" [8]
- Straightforward to implement
- Works well with dependency injection

**Disadvantages:**
- "Initial response time overhead on miss (extra roundtrips)" [8]
- No consistency guarantee — external processes can change the data store without the cache knowing [9]

**Write-side ordering:** "Update data store first, then invalidate cache (delete key). Order matters: update store BEFORE removing cache to avoid stale data window" [9].

## Write-Through

Cache updated immediately when the primary database is updated [8].

**Advantages:**
- "Cache stays up-to-date, greater likelihood of hits" [8]
- Optimal database read performance

**Disadvantages:**
- "Infrequently-requested data also cached (larger cache)" [8]

**Implementation note:** "Almost always implemented alongside lazy loading" [8]. The combination covers both read (cache-aside) and write (write-through) paths.

**Best practice:** "Combine write-through and lazy loading with appropriate expiration" [8].

## Write-Behind (Write-Back)

Not directly documented in the fetched AWS whitepaper content [8]. From discovery-phase findings (unverified from full-page fetch): the write-behind pattern defers database writes by first writing to cache, then asynchronously flushing to the database via a background worker or message queue.

## FastAPI Integration Patterns

### Decorator-Based (fastapi-cache2)

```python
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

@app.get("/")
@cache(expire=60)
async def index():
    return dict(hello="world")
```

Initialize during lifespan: `FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")` [18].

Supports: ETag, Cache-Control headers, custom namespace, custom key building [18].

### Decorator-Based (cashews)

```python
from cashews import cache
cache.setup("redis://localhost")

@cache(ttl="3h", key="user:{request.user.uid}")
async def get_user(request):
    ...
```

Richer strategy support including failover (return cached on exception) and early refresh (proactive background refresh before expiration) [19].

### Dependency Injection (Manual)

FastAPI's dependency injection can yield a Redis connection per request. The lifespan context manager (`@asynccontextmanager`) handles startup (initialize pool) and shutdown (close pool). Replaces deprecated `@app.on_event("startup/shutdown")` (from discovery findings).

### Cache-Aside in FastAPI

The cache-aside pattern maps naturally to FastAPI dependencies:

1. Create a `CacheService` dependency that wraps Redis operations
2. Inject it into route handlers via `Depends()`
3. Route handler checks cache, falls through to database on miss
4. Service layer handles cache population

**Cache priming:** "Prepopulate cache with likely-needed data at startup" via lifespan events [9].

## Pattern Selection Guide

| Pattern | When to Use | Trade-off |
|---------|-------------|-----------|
| Cache-aside | General-purpose API caching, read-heavy workloads | Miss penalty on first access |
| Write-through + cache-aside | Frequently read data that changes via known write paths | Larger cache, more write overhead |
| Write-behind | Write-heavy workloads tolerating eventual consistency | Complexity, data loss risk |

## Gaps and Limitations

- No quantitative performance comparisons between fastapi-cache2 and cashews.
- Write-behind pattern not covered by primary fetched sources — claims from discovery phase only.
- No coverage of read-through pattern specifics for Redis.
- asyncpg-specific integration (three-way FastAPI + asyncpg + Redis) not addressed in any fetched source.
- fastapi-cache2 at version 0.2.2 — pre-1.0 maturity [18].
