# Perses vs Grafana

A citation-backed technical comparison of Perses (CNCF Sandbox dashboarding project) and Grafana (established observability platform) across nine dimensions. All claims sourced from 25 web sources visited on 2026-06-26.

Last revised: 2026-06-26

---

## Key Comparison Table

| Dimension | Perses | Grafana |
|-----------|--------|---------|
| **Architecture** | File-based or MySQL; K8s operator (v1alpha2, unstable) | SQLite/MySQL/Postgres; documented active-active HA |
| **Data sources** | 6 native + Thanos/Jaeger via compatible APIs | 160+ plugins |
| **Dashboard authoring** | Code-first (CUE/Go SDKs), 16 panel types | UI-first (drag-and-drop), 6 as-code tools |
| **CNCF status** | Sandbox project (Aug 2024), Apache 2.0 | Platinum member company (Jul 2021), AGPLv3 |
| **Alerting** | **None** — delegates to Prometheus/Alertmanager | Unified alerting (Grafana 8+), 13+ notification channels |
| **Maturity** | ~5 years, 975 stars, 5 named adopters | 10+ years, 35M+ users, 7,000+ customers, $400M+ ARR |
| **Migration** | Official tools (UI/CLI/API), dashboards only, best-effort | N/A (migration is FROM Grafana) |
| **RBAC** | Built-in all editions (project-based, 4 role types) | OSS: 5 basic roles; Enterprise: full RBAC + LBAC |
| **Performance** | No published benchmarks | Proven at scale (adoption), no published benchmarks |

## Decision Framework

**Choose Perses when:**

1. **Apache 2.0 licensing is required** — AGPLv3 is a legal blocker for your organization (embedding, redistribution, network service modifications)
2. **Kubernetes-native CRDs are essential** — you want dashboards deployed as Custom Resources alongside applications, with namespace-to-project mapping
3. **Dashboard-as-code is the primary workflow** — your team writes CUE/Go, validates in CI/CD, and deploys via GitOps pipelines
4. **Prometheus-ecosystem focus** — your observability stack is primarily Prometheus/Thanos/Loki/Tempo with no need for 150+ other data sources
5. **You accept early-stage risk** — operator is v1alpha2, plugin system under redesign, no HA documentation, no published performance data

**Choose Grafana when:**

1. **Broad data source coverage needed** — your stack includes CloudWatch, Elasticsearch, InfluxDB, MySQL, or other non-Prometheus sources
2. **Built-in alerting required** — you want alerting and visualization in a single tool
3. **Production-proven maturity matters** — you need documented HA, battle-tested at scale (35M+ users), with enterprise support options
4. **UI-first dashboard building** — your team prefers drag-and-drop visual authoring over code compilation
5. **Comprehensive RBAC needed** — Enterprise/Cloud RBAC with custom roles, LBAC, and team-based permissions (requires commercial license)

**Neither is a drop-in replacement for the other.** Perses is a dashboard layer; Grafana is a full observability platform. A team choosing Perses must separately solve for alerting, data storage, and heterogeneous data source integration.

## Full Analysis

- [perses-vs-grafana.md](perses-vs-grafana.md) — complete comparison with methodology
- [citations.md](citations.md) — all 25 sources with tier ratings
- [references/](references/) — one file per dimension with detailed tables and quotes
- [audit/](audit/) — citation audit and consistency review reports
