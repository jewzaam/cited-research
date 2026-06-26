# Data Source Support

Dimension 2 of the Perses vs Grafana comparison. Source details in [citations.md](../citations.md).

---

## Perses Data Sources

### Native Backends (from API specification)

| Backend | Type | Source |
|---------|------|--------|
| Prometheus | Metrics | [2] |
| Loki | Logs | [2] |
| Tempo | Traces | [2] |
| Pyroscope | Profiling | [2] |
| ClickHouse | Analytics | [2] |
| VictoriaLogs | Logs | [2] |

**Total: 6 named backends in the dashboard API specification** [2].

### Additional Sources via Compatible APIs

| Source | Interface | Evidence |
|--------|-----------|----------|
| Thanos | Prometheus-compatible API | [7], [9] |
| Jaeger | Native support | [7], [9] |

### Plugin Extensibility

- Plugin system exists: `percli plugin generate --plugin.type=Panel --plugin.name=ClickHousePanel` [21]
- Plugin types: datasource, query, variable, panel, explorer [2]
- Plugin system described as "undergoing a redesign" [9]
- SAP blog mentions Splunk support via plugin architecture [11]

### Datasource Discovery

- HTTP Service Discovery: fetches datasource lists from HTTP endpoints with OAuth, Basic Auth support [1]
- Kubernetes Service Discovery: discovers services and pods filtered by labels, namespace, port, service type [1]

### Datasource Access Modes

- Direct URL (pointing straight at backend) [21]
- Proxy (routing through Perses backend) [21]

---

## Grafana Data Sources

### Scale

| Metric | Value | Source |
|--------|-------|--------|
| Total plugins | 160+ | [18] |
| New plugins added (FY ending Jan 2026) | 15 | [18] |
| "100+ sources" (feature matrix comparisons) | Earlier figure, superseded by 160+ | [21] |

### Named Core Sources

Prometheus, Loki, Tempo, Mimir, InfluxDB, OpenSearch, Elasticsearch, MySQL, PostgreSQL, and many more [21], [23].

### Plugin Ecosystem

- Mature (10+ years of development) [21]
- Third-party plugin marketplace launched April 2026 [18]
- Panel, data source, and app plugin types [14]
- Community and commercial plugins available [18]

---

## Comparison

| Dimension | Perses | Grafana |
|-----------|--------|---------|
| Native backends | 6 (+ Thanos, Jaeger via compatible APIs) | 160+ plugins |
| Plugin ecosystem maturity | "Undergoing redesign" [9] | 10+ years, marketplace |
| Observability coverage | Metrics, logs, traces, profiling | Metrics, logs, traces, profiling + 150+ other sources |
| Discovery | HTTP SD + K8s SD [1] | Plugin-based configuration |
| Access modes | Direct URL or proxy [21] | Direct, proxy, or server (data source-specific) |

## Gaps and Limitations

- Perses data source count (6-8) is an order of magnitude smaller than Grafana's (160+).
- Teams with heterogeneous stacks (CloudWatch, Elasticsearch, InfluxDB, etc.) face significant integration work or are blocked with Perses.
- Perses plugin system redesign means current extensibility mechanisms may change.
- SquaredUp evaluation (written at an earlier date) found "only Prometheus datasource" — subsequent additions of Loki, Tempo, ClickHouse, Pyroscope, VictoriaLogs show active expansion [22] vs [2].
- Grafana's exact current plugin count ("160+" from Feb 2026 press release) may differ from catalog count.
