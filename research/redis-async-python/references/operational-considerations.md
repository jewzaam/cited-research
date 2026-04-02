# Operational Considerations

Covers Dimension 6: memory limits, eviction policies, persistence, and monitoring for cache-only Redis deployments.

## Memory Configuration

### maxmemory

| Platform | Default | Notes |
|----------|---------|-------|
| 64-bit | 0 (unlimited) | Must be explicitly set for caching |
| 32-bit | 3GB (implicit) | Hard limit |

Configure at startup via `redis.conf` or at runtime: `CONFIG SET maxmemory 100mb` [1].

### Memory Planning

- Plan for **peak** memory usage, not average [7]
- Memory is NOT automatically freed to OS when keys are deleted (allocator retains pages) [7]
- Fragmentation ratio can be unreliable when usage drops significantly from peak [7]
- Reserve memory for replication buffers if using replicas (not counted toward `maxmemory`) [1]
- Check buffer usage: `INFO memory` → `mem_not_counted_for_evict` [1]

## Eviction Policies

Redis provides 10 eviction policies [1]:

### All-Keys Policies

| Policy | Mechanism | Best For |
|--------|-----------|----------|
| `allkeys-lru` | Evict least recently used | Power-law access (Pareto distribution) — **recommended default** |
| `allkeys-lfu` | Evict least frequently used (Redis 4.0+) | Highly skewed, stable access patterns |
| `allkeys-lrm` | Evict least recently modified (Redis 8.6+) | Read-heavy, preserve recently written data |
| `allkeys-random` | Random eviction | Equal access frequency |

### Volatile Policies (TTL keys only)

| Policy | Mechanism |
|--------|-----------|
| `volatile-lru` | LRU among keys with TTL |
| `volatile-lfu` | LFU among keys with TTL |
| `volatile-lrm` | LRM among keys with TTL (Redis 8.6+) |
| `volatile-random` | Random among keys with TTL |
| `volatile-ttl` | Shortest remaining TTL |

### noeviction

Returns error on writes when `maxmemory` reached. No keys removed. Reads continue normally [1].

**Critical operational gotcha:** "volatile-* policies behave like noeviction if no keys have TTL set" [1].

### Approximation Algorithm

Redis uses **approximated** LRU/LFU (not true implementations) to save memory [1]:
- `maxmemory-samples`: Default 5. Samples N random keys and evicts the best candidate.
- Value 5: "good approximation" [1]
- Value 10: "very close to true LRU" with slight CPU overhead [1]
- Redis 3.0+ maintains a pool of good eviction candidates [1]

### LFU Configuration

LFU (Redis 4.0+) uses a probabilistic Morris counter [1][14]:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `lfu-log-factor` | 10 | Controls counter saturation speed |
| `lfu-decay-time` | 1 minute | Counter decays by 1 every N minutes; 0 = never |

`lfu-log-factor` saturation table [1]:

| factor | 100 hits | 1K hits | 100K hits | 1M hits |
|--------|----------|---------|-----------|---------|
| 0 | 104 | 255 | 255 | 255 |
| 1 | 18 | 49 | 255 | 255 |
| 10 | 10 | 18 | 142 | 255 |
| 100 | 8 | 11 | 49 | 143 |

### LFU vs LRU Selection

| Choose LFU when... | Choose LRU when... |
|--------------------|-------------------|
| Skewed access (80/20 rule) [14] | Rapidly changing patterns [14] |
| Static hot data [14] | Temporal locality (user sessions) [14] |
| Popularity rankings [14] | Burst patterns (flash sales) [14] |

## Persistence (Cache-Only Deployment)

For a pure caching use case (database is source of truth):

**Recommended configuration:**
```
save ""
appendonly no
```

This disables both RDB and AOF, eliminating fork latency and I/O overhead [2].

### Data Loss by Configuration

| Configuration | Max Data Loss |
|---------------|---------------|
| No persistence (cache-only) | All data on restart |
| RDB only | 5+ minutes |
| AOF everysec | ~1 second |
| AOF always | None (very slow) |
| RDB + AOF (hybrid) | ~1 second |

Source: [2]

### If Persistence is Needed

For non-cache Redis uses (e.g., session storage):
- `appendfsync everysec`: Default AOF mode. Max 1 second data loss. Background thread fsync [2].
- Hybrid (RDB + AOF): Recommended for production — AOF for durability, RDB for faster restarts [2].
- On restart, AOF takes precedence over RDB [2].

## Monitoring

### INFO Command Metrics

Critical sections for cache monitoring [11]:

**Memory:**
- `used_memory` / `used_memory_rss` — actual vs OS-reported memory
- `mem_fragmentation_ratio` = `used_memory_rss / used_memory` — healthy: 1.0-1.5, concerning: >1.5 [11]
- `allocator_frag_ratio` — true external fragmentation (more reliable than `mem_fragmentation_ratio`) [11]
- `maxmemory` / `maxmemory_policy` — configured limits

**Stats:**
- `keyspace_hits` / `keyspace_misses` — for hit ratio: `hits / (hits + misses) * 100` [1]
- `evicted_keys` — keys evicted due to memory pressure [11]
- `expired_keys` — keys expired by TTL [11]
- `instantaneous_ops_per_sec` — current throughput [11]
- `rejected_connections` — `maxclients` exhausted [11]

### Prometheus Exporter

The `oliver006/redis_exporter` is the de facto standard [12]:
- Supports Valkey 7.x-9.x and Redis
- Default: port 9121, metrics at `/metrics`
- Exports most `INFO` metrics plus per-database keys/expiring/avg_ttl
- Key features: multi-target scraping, TLS/SSL, Redis Cluster discovery, Lua script custom metrics
- Pattern-based key monitoring via `--check-keys` flag

### Recommended Alerts

| Metric | Threshold | Meaning |
|--------|-----------|---------|
| `mem_fragmentation_ratio` | >1.5 for 15 minutes | Excessive fragmentation |
| `mem_fragmentation_ratio` | <1.0 for 1 minute | Redis using swap — critical latency impact |
| `evicted_keys` rate | Increasing | Memory pressure, possible wrong eviction policy |
| `rejected_connections` | >0 | maxclients exhausted |
| Cache hit ratio | <50-80% (workload dependent) | Inefficient caching or wrong eviction policy |

## Memory Optimization

### Compact Encodings

Redis uses special memory-efficient encodings for small data structures [7]:
- Savings: "up to 10x less memory (average 5x)" [7]
- Redis >= 7.0: `hash-max-listpack-entries 512`, `hash-max-listpack-value 64` [7]
- Redis >= 7.2: Adds set and sorted set listpack thresholds [7]

### Hash Sharding Example

100,000 objects stored as sharded hashes (~100 fields each) vs direct keys [7]:
- With hash sharding: **1.7 MB**
- Direct keys: **11 MB**
- Savings: **~6.5x reduction**

Strategy: split key `object:1234` into hash key `object:12`, field `34` [7].

### Bitmap Efficiency

100 million users representable as bitmap in **12 MB** of RAM [7].

## Gaps and Limitations

- Active defragmentation (`activedefrag`) configuration not covered in fetched sources.
- redis-py built-in retry documentation fetch failed (readthedocs 403).
- No data on Prometheus exporter resource overhead (CPU/memory cost).
- Memory overhead per individual key (in bytes) not precisely quantified in fetched sources — only aggregate comparisons available.
- No coverage of SLOWLOG configuration or latency monitoring subsystem.
