# Connection Lifecycle & Error Handling

Covers Dimension 7: async connection pool sizing, health checks, retry patterns, graceful degradation.

## Production Configuration

Official redis-py production parameters [4]:

| Parameter | Default | Recommended | Purpose |
|-----------|---------|-------------|---------|
| `socket_connect_timeout` | 10s | 15s | Connection establishment timeout |
| `socket_timeout` | 10s | 5s | Command response timeout |
| `health_check_interval` | — | 3s | PING when connection idle > N seconds |
| Retry attempts | 3 | 3 (or custom) | Default with ExponentialBackoff + jitter |
| Retry errors | `ConnectionError`, `TimeoutError` | Same + custom | Errors that trigger retry |

### Retry Configuration

Built-in retry support [4]:
```python
from redis.backoff import ExponentialBackoff
from redis.retry import Retry

retry = Retry(ExponentialBackoff(), 8)  # 8 retries
r = Redis(retry=retry, retry_on_error=[BusyLoadingError])
```

To narrow retry scope: `Retry(ExponentialBackoff(), 3, supported_errors=(TimeoutError,))` [4].

## Connection Pool Sizing

### Pool Types and Defaults

| Pool Type | Default max_connections | Exhaustion Behavior |
|-----------|----------------------|---------------------|
| `ConnectionPool` | 2^31 (~2.1 billion) | Raises `ConnectionError` |
| `BlockingConnectionPool` | 50 | Waits up to 20s (default timeout) |

Source: [21]

`BlockingConnectionPool` is recommended for async Python to prevent "Too many connections" errors under concurrency [21].

### Sizing Guidance

- Official Redis docs: "Start with a small pool; let it grow dynamically as needed. Monitor actual connection usage to find optimal size" [3].
- Community guidance: Set `max_connections` to 2-3x expected peak concurrent requests [15].
- Redis server default `maxclients`: 10,000 [15] (from discovery findings).

**Contradicting guidance on health_check_interval:** Official Redis docs recommend 3 seconds [4]. A community blog post recommends 30 seconds [15]. The official value should be treated as authoritative.

## Connection Lifecycle

### from_pool Ownership Model

| Pattern | Pool Ownership | `aclose()` Behavior |
|---------|---------------|---------------------|
| `Redis.from_pool(pool)` | Redis instance owns pool | Closes pool |
| `Redis(connection_pool=pool)` | Caller owns pool | Leaves pool open — manual close required |
| `Redis()` (default) | Internal pool created | Closes internal pool |

Source: [21]

### Async Cleanup

`await redis.aclose()` is required for async clients — there is no asyncio destructor [13]. Without explicit cleanup, connections leak.

For shared pools across multiple Redis instances, use `connection_pool=` and manually close the pool after all instances are done [21].

## Retry Patterns

### redis-py Built-in Retry

Default: 3 attempts with ExponentialBackoff and jitter [4]. Retries on `ConnectionError` and `TimeoutError` by default.

### Tenacity Library (External)

For more sophisticated retry logic [15]:
- `AsyncRetrying` for coroutine-based retry
- `wait_exponential()` with configurable multiplier, maximum delay, base
- `retry_if_exception_type()` for selective exception handling

### Circuit Breaker Pattern

Three states for preventing cascading failures [15]:

| State | Behavior | Transition |
|-------|----------|------------|
| Closed (normal) | Requests pass through | → Open after N failures |
| Open (failing) | Requests immediately rejected | → Half-Open after timeout |
| Half-Open (testing) | Selective test requests | → Closed on success, Open on failure |

Libraries: `pybreaker`, `circuit-breaker-python` (from discovery findings).

## Graceful Degradation

When Redis is unavailable, the application should degrade rather than fail [15]:

| Strategy | Description |
|----------|-------------|
| Transparent retry | Automatic retry masks transient failures |
| Fast failure | Circuit breaker prevents thundering herd |
| Adaptive waiting | Exponential backoff with jitter reduces retry storms |
| Stale cache fallback | Return old cached data instead of errors |
| Health monitoring | Health checks enable external systems to detect degradation |

### Singleton Pattern for Async

Use `asyncio.Lock()` in a `RedisClientManager` class to ensure a single client instance across concurrent operations [15].

## Pipeline Performance

Pipelining batches multiple commands into a single network round trip [5]:

| Metric | Value | Conditions |
|--------|-------|------------|
| Speedup | ~4.7x | Ruby client, 10k PINGs |
| Max throughput gain | ~10x | With sufficiently long pipelines |
| Recommended batch size | ~10,000 commands | Bounds server-side memory |

Source: [5]

**Default pipeline behavior:** `transaction=True` wraps commands in `MULTI/EXEC` for atomic execution [21]. Set `transaction=False` for pure batching without atomicity.

**Optimistic locking:** `WATCH` monitors keys; `WatchError` raised if watched key changes before `EXEC` [21].

## Production Checklist

From official redis-py documentation [4]:
1. Client-side caching
2. Retries (ExponentialBackoff)
3. Health checks (health_check_interval)
4. Exception handling
5. Timeouts (socket_connect_timeout, socket_timeout)
6. Server-assisted client-side caching hints (SCH)
7. OpenTelemetry monitoring

## Gaps and Limitations

- redis-py readthedocs returned 403 — detailed Retry class API documentation not available.
- Pipeline benchmark is Ruby-based [5]; Python async pipeline performance may differ due to asyncio overhead.
- No empirical data on health_check_interval impact on connection stability or latency.
- No data on `BlockingConnectionPool` vs `ConnectionPool` async performance comparison.
- No coverage of how `aclose()` interacts with in-flight commands (graceful drain behavior).
- TLS/SSL configuration covered only in discovery phase, not in fetched sources.
