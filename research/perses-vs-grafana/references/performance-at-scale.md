# Performance at Scale

Dimension 9 of the Perses vs Grafana comparison. Source details in [citations.md](../citations.md).

---

## Perses Performance Evidence

### Published Data

**No published performance benchmarks found for Perses.** This was confirmed across all research sources — no latency numbers, concurrency metrics, load test results, or resource consumption data exist publicly.

### Indirect Evidence

| Data Point | Detail | Source |
|-----------|--------|--------|
| Amadeus scale | 5,000+ dashboards motivated Perses creation | [8] |
| Architecture | Lightweight — dashboard layer only, no data storage, no alerting | [23] |
| Storage backends | File-based (single-instance) or MySQL (multi-instance) | [1] |
| SQL recommendation | "Prefer the SQL config in case you are running multiple Perses instances" | [1] |
| Operator maturity | v1alpha2 — "suggest caution in mission-critical environments" | [6] |

### HA Architecture

No formal HA documentation. SQL backend enables multi-instance deployment but no load-balancing guidance, failover procedures, or notification deduplication details exist [1], [6].

---

## Grafana Performance at Scale

### HA Architecture

| Aspect | Detail | Source |
|--------|--------|--------|
| Topology | Active-active behind load-balancing reverse proxy | [16] |
| Database | Shared MySQL or PostgreSQL required; SQLite "unsuitable" for HA | [16] |
| Session management | Auth tokens in shared DB; sticky sessions not required | [16] |
| Alerting HA | All nodes execute all alerts; notifications deduplicated | [16] |
| Alert load distribution | NOT supported — every node runs every alert rule | [16] |
| Grafana Live | "Works with limitations in highly available setup" | [16] |

### Known Scale Constraints

| Constraint | Detail | Source |
|-----------|--------|--------|
| SQLite limitation | Single-writer database with file-level locking; prevents true HA | Counter-discovery |
| Dashboard/folder limits | 1,000 dashboards and 1,000 folders (free tier, introduced April 2026) | Counter-discovery |
| Alert evaluation | Every node evaluates every alert — no sharding or distribution | [16] |

### Scale Indicators

| Metric | Value | Source |
|--------|-------|--------|
| Users worldwide | 35M+ | [18] |
| Customers | 7,000+ | [18] |
| Fortune 50 penetration | 70% | [18] |
| Data source plugins | 160+ | [18] |
| FedRAMP High + DoD IL5 | Federal Cloud compliance achieved | [18] |

---

## Comparison

| Dimension | Perses | Grafana |
|-----------|--------|---------|
| Published benchmarks | **None** | None (but proven at scale via adoption) |
| HA documentation | Not available | Documented active-active pattern |
| Max known deployment | 5,000+ dashboards (Amadeus, pre-Perses) | 35M+ users across 7,000+ customers |
| Multi-instance | SQL backend; operator multi-instance sync | Shared DB with load balancer |
| Alert scaling | N/A (no alerting) | All-node execution, no sharding |
| Database options | File-based or MySQL | SQLite, MySQL, PostgreSQL |

## Gaps and Limitations

- **Perses has no published performance data** — the absence is not evidence of poor performance, but it means adoption requires trust without verification.
- Grafana's scale story is proven through adoption (35M+ users) but lacks published latency/throughput benchmarks at the dashboard layer.
- Grafana alerting HA does not distribute load — every node runs every alert, which may not scale efficiently for large rule sets.
- Grafana's SQLite limitation is a known anti-pattern in K8s deployments where multiple replicas cannot share a file-level lock.
- Perses's MySQL-only SQL support limits database choice compared to Grafana's MySQL + PostgreSQL.
