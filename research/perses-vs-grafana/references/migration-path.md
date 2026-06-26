# Migration Path

Dimension 7 of the Perses vs Grafana comparison. Source details in [citations.md](../citations.md).

---

## Grafana-to-Perses Migration

### Methods

| Method | Command/Process | Source |
|--------|----------------|--------|
| UI | Navigate to home page → "import dashboard" → paste/upload Grafana JSON → import | [4] |
| CLI | `percli migrate -f grafana-dashboard.json --online -o json > perses-dashboard.json` | [4] |
| API | Dedicated `/api/migrate` endpoint | [4] |
| Go SDK | Define dashboards as Go code, utilizing community mixins | [10] |

Apply result: `percli apply -f perses-dashboard.json --project my-project` [4]

Kubernetes CR output: `--format cr` flag [4]

### How It Works

1. Grafana dashboard JSON imported into Go structure, mapped to Perses Go structure [4]
2. For each variable, panel, and query, a CUE script from the corresponding plugin generates the Perses data model [4]
3. Only works if the plugin is supported [4]

### Limitations

| Limitation | Detail | Source |
|-----------|--------|--------|
| Scope | **Only dashboards** — cannot migrate alerts, users, or other resources | [4] |
| Quality | **Best-effort** basis — not all Grafana plugins have Perses equivalents | [4] |
| Unsupported plugins | Variables become static list with placeholder values `["grafana", "migration", "not", "supported"]` | [4] |
| Best support | Prometheus queries have best support | [10] |
| Non-Prometheus | Dashboards using other data sources or custom panel plugins "may require manual adjustment post-migration" | [10] |

### Version Compatibility

- Development started when Grafana 9.0.0 was latest [4]
- Backward compatible since; "high chance you can migrate your dashboard from an older version" [4]
- Team always targets latest Grafana version [4]

### Post-Migration Tips

- Remove `"name"` field from datasource objects to use default datasource [4]
- Review `StaticListVariable` entries with placeholder values for manual attention [4]

---

## Coexistence Strategies

- Both tools can connect to same data sources (Prometheus, Tempo, Loki) [10]
- Red Hat approach: migration from Grafana to Perses for multicluster observability [10]
- No documented long-term coexistence patterns found — approach is migration, not dual-running

### Community Mixins

Prebuilt dashboards for K8s, Node, Thanos available via `perses/community-mixins` [10]. Can combine community panels with migrated Grafana dashboards to "reduce migration time and complexity" [10].

---

## Grafana's Own Migration Challenges

Grafana itself has version upgrade migration issues documented in GitHub:
- Database migration failures in 11.3.0, 12.1, 12.4, and 13.0 releases (from counter-discovery research)
- Unified storage migration causes rollbacks and service unavailability
- Large annotation tables cause indefinite migration hangs

Grafana's JSON schema compatibility across versions is also a challenge: "can very easily break your configuration" [9], and upgrading Grafana frequently broke dashboards at Amadeus due to schema changes [8].

---

## Comparison

| Dimension | Perses | Grafana |
|-----------|--------|---------|
| Migration tooling | Official (UI, CLI, API, Go SDK) | N/A (migration is TO Perses FROM Grafana) |
| Migration scope | Dashboards only | — |
| Migration quality | Best-effort; Prometheus queries best supported | — |
| Version compatibility | Grafana 9.0.0+ | — |
| Coexistence | Both connect to same backends; no dual-run patterns documented | — |
| Schema stability | Open specification, designed for stability | schemaVersion changes across releases |

## Gaps and Limitations

- Migration is one-way (Grafana → Perses) with no reverse path.
- Only dashboards migrate — teams must separately handle alerts, users, teams, folders, and other Grafana resources.
- Plugin coverage is incomplete and expanding — no published success rate data.
- Table column settings above 16 require manual entry (from counter-discovery GitHub issues).
- Dashboard name regeneration issues reported post-migration (from counter-discovery GitHub issues).
- No documented runbook for parallel operation during transition period.
