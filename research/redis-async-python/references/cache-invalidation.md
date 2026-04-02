# Cache Invalidation Strategies

Covers Dimension 3: TTL strategies, event-driven invalidation, pub/sub cache busting, tag-based invalidation, and stampede prevention.

## Invalidation Types

Redis documentation defines four cache invalidation approaches [10]:

| Type | Mechanism | Example |
|------|-----------|---------|
| Time-based | Predetermined TTL interval | News: hourly, stocks: every few minutes |
| Event-based | Triggered by system event | Blog post updated → invalidate cached version |
| Command-based | Explicit user/system action with dependency IDs | File deleted → invalidate file's cache via matching ID |
| Group-based | Invalidate by category/tag | "Politics" section update → invalidate all politics articles |

### Dependency ID Concept

A dependency ID is a "label identifying which cache entries to invalidate. Same label on multiple entries creates a group" [10]. This is the conceptual foundation for tag-based invalidation libraries like cashews [19].

## TTL Strategies

### Recommended TTL Ranges

| Data Type | TTL Range | Source |
|-----------|-----------|--------|
| Static content (CSS, images) | 1 year minimum | [10] (attributed to Google) |
| Frequently updated (stocks, news) | Few minutes to 1 hour | [10] |
| Dynamic content (eCommerce) | Shorter expiration | [10] |

**TTL guidance from Azure:** "Expiration policy must match access patterns. Not too short (constant reloads), not too long (stale data)" [9].

### TTL Jitter

From discovery-phase findings (not directly from fetched full pages): Add random offset to TTL values to prevent synchronized expiration across keys, which causes cache stampedes. Typical jitter: 30 seconds to 1 minute of randomness.

## Event-Driven Invalidation via Pub/Sub

Redis Pub/Sub can broadcast invalidation signals across application instances [6].

**Mechanics:**
1. Instance modifies data → publishes invalidation message to channel
2. All subscribed instances receive message → delete local/shared cache entry
3. Next request triggers cache-aside reload

**Critical limitation:** Pub/Sub has at-most-once delivery. "If subscriber disconnected, message permanently lost" [6]. Missed invalidation messages result in stale caches until TTL expires.

**Best practice:** Use Pub/Sub for best-effort invalidation combined with TTL as a safety net.

### Sharded Pub/Sub (Redis 7.0+)

For Redis Cluster deployments, traditional Pub/Sub broadcasts to all nodes. Sharded Pub/Sub restricts message propagation to the owning shard, reducing cluster bus traffic [6]:

- Commands: `SSUBSCRIBE`, `SUNSUBSCRIBE`, `SPUBLISH`
- Shard channels assigned to slots using the same algorithm as keys
- Enables horizontal scaling of invalidation signals

## Tag-Based Invalidation

Tag-based invalidation maps to Redis's "group-based" invalidation concept [10]. Libraries supporting this pattern:

| Library | Tag Support | Mechanism |
|---------|------------|-----------|
| cashews | Yes — tag-based and time-based invalidation built in | [19] |
| fastapi-cache2 | Namespace-based only (not true tag-based) | [18] |

cashews stores tag-to-key mappings enabling O(1) group invalidation [19].

## Cache Stampede Prevention

When a popular key expires, many concurrent requests simultaneously miss the cache and hit the database ("thundering herd" problem).

**Prevention strategies** (from discovery findings):

| Strategy | Description |
|----------|-------------|
| TTL jitter | Add random offset to TTL to prevent synchronized expiration |
| Distributed locking | `SET NX` with short TTL — one request rebuilds, others wait |
| Early refresh | Proactively refresh before expiration (cashews supports this [19]) |
| Stale-while-revalidate | Serve stale data while one request refreshes in background |

cashews implements "early refresh" — proactive background refresh before expiration — as a built-in strategy [19]. fastapi-cache2 does not mention stampede protection in its documentation [18].

## Eviction as Passive Invalidation

When `maxmemory` is reached, Redis evicts keys according to the configured policy [1]:

- **allkeys-lru**: Evicts least recently used keys. Recommended for power-law access patterns [1].
- **allkeys-lfu**: Evicts least frequently used keys (Redis 4.0+). Better for skewed workloads [14].
- **volatile-ttl**: Evicts keys with shortest remaining TTL [1].
- **noeviction**: Returns error — no automatic invalidation [1].

**Critical gotcha:** "volatile-* policies behave like noeviction if no keys have TTL set" [1]. Forgetting to set TTLs with volatile policies leads to OOM errors.

## Write-Side Invalidation Ordering

"Update data store first, then invalidate cache (delete key). Order matters: update store BEFORE removing cache to avoid stale data window" [9].

If the cache key is deleted first, a concurrent request can refill the cache with old data before the database write completes. The correct sequence:

1. Write to database
2. Delete from cache
3. Next read triggers cache-aside reload with fresh data

## Gaps and Limitations

- Redis Keyspace Notifications (alternative to Pub/Sub for event-driven invalidation) not covered in fetched sources.
- No quantitative data on invalidation latency (how long stale data persists with different strategies).
- Stampede prevention strategies sourced primarily from discovery-phase snippets, not verified from full-page fetches.
- No coverage of database-trigger-based invalidation (PostgreSQL LISTEN/NOTIFY → Redis).
