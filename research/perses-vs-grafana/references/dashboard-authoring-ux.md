# Dashboard Authoring & UX

Dimension 3 of the Perses vs Grafana comparison. Source details in [citations.md](../citations.md).

---

## Perses Dashboard Authoring

### Data Model

Dashboard spec fields [2]:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `display` | Display spec | No | Rich name and description |
| `datasources` | map[string → Datasource] | No | Referenced by panels/variables |
| `variables` | list | No | Dashboard-level variables |
| `panels` | map[string → Panel spec] | No | Panel definitions keyed by reference ID |
| `layouts` | list of Grid specs | **Yes** | Positioning/display of panels |
| `duration` | duration | No | Default time range |
| `refreshInterval` | duration | No | Default refresh interval |

Minimum viable dashboard: one panel + one layout [2].

Panels defined in a flat map, referenced by layouts via JSON pointer `$ref` (e.g., `"$ref": "#/spec/panels/statRAM"`) [2].

### Panel Plugin Kinds (16 total)

BarChart, FlameChart, GaugeChart, HeatMapChart, HistogramChart, LogsTable, Markdown, PieChart, ScatterChart, StatChart, StatusHistoryChart, Table, TimeSeriesChart, TimeSeriesTable, TraceTable, TracingGanttChart [2].

### Dashboard-as-Code SDKs

| SDK | Prerequisites | Workflow |
|-----|--------------|----------|
| CUE | percli >=v0.51.0, cue >=v0.12.0 | `cue mod init` → `percli dac setup` → write CUE → `percli dac build` |
| Go | percli >=v0.44.0, Go installed | `go mod init` → `percli dac setup --language go` → write Go → `percli dac build` |

Both produce JSON/YAML, deployed via `percli apply` [5].

### CI/CD Integration

- Build → validate → deploy pipeline [5]
- GitHub Actions: `perses/cli-actions` with reusable workflow and independent actions [5]
- Server-side validation: `server-validation: true` [5]
- Offline mode: CUE SDK provides local schema validation without running server [5]

### UI Authoring

- Red Hat COO 1.4: dashboard list page (filter, sort, create, delete, rename, duplicate), direct editing of panels/PanelGroups/variables, Grafana JSON import [10]
- SquaredUp evaluation: UI creation possible but workflow requires Go → YAML → JSON → API call — "tedious and error-prone" for hand-coding [22]

### Embeddable Components

Granular NPM packages for embedding individual charts into external UIs via plugin architecture — cited as a distinctive capability [8], [9].

---

## Grafana Dashboard Authoring

### UI-First Approach

- Drag-and-drop dashboard builder, 10+ years of development [21]
- Panel editor sidebar/toolbar, content outline (tree view), template variables, time picker [12]

### File-Based Provisioning

| Feature | Detail | Source |
|---------|--------|--------|
| Config format | YAML in `provisioning/dashboards` | [12] |
| Dashboard formats | Classic JSON and Kubernetes resource format (`kind: Dashboard`) | [12] |
| Env var interpolation | `$ENV_VAR` or `${ENV_VAR}` syntax | [12] |
| Filesystem detection | <=10s = filesystem watch events; >10s = polling | [12] |
| Folder mirroring | `foldersFromFilesStructure` — directory hierarchy up to 4 levels deep | [12] |
| UI updates | `allowUiUpdates: true` saves to DB but provisioning overwrites on next sync | [12] |
| Alerting provisioning | Full support: alert rules, contact points, notification policies | [12] |

### Six As-Code Tools

| Tool | Platform | Drift Correction | K8s Native | Scope |
|------|----------|-------------------|-----------|-------|
| Terraform Provider | Cloud + OSS | Plan/apply | No | Broadest resource coverage |
| Crossplane Provider | Cloud + OSS | Active resync (UI changes discarded) | Yes (CRDs) | Matches Terraform; **alpha stage** |
| K8s Operator | OSS only | Operator reconciliation | Yes (CRDs) | Moderate; **no Helm chart** |
| Grizzly | Cloud + OSS | No (CLI push) | No (YAML-inspired) | Dashboards, folders, datasources, Prometheus rules |
| Grafonnet | N/A (generator) | N/A | No | Dashboards only (Jsonnet library) |
| Ansible Collection | Cloud only | Idempotent runs | No | 8 resources |

Source: [14]

---

## Version Control Friendliness

| Aspect | Perses | Grafana |
|--------|--------|---------|
| Native format | Typed spec compiled from CUE/Go [5] | JSON (manually authored or generated) [12] |
| Diff quality | Clean YAML/JSON diffs from code compilation [8] | JSON diffs noisy — schema changes across versions [8] |
| Validation | Static validation in CI/CD via percli [5] | Manual or via Terraform plan [14] |
| Data model | "made for dashboard as code" [8] | "not made for dashboard as code" (Augustin Husson) [8] |
| Schema stability | Open specification [9] | schemaVersion increments with releases [21] |

## Gaps and Limitations

- Perses has 16 panel plugin kinds vs an uncounted (but significantly larger) Grafana panel library.
- Perses UI authoring is less mature than Grafana's drag-and-drop builder.
- Perses CUE/Go SDK requires programming knowledge — higher barrier for non-developers [22].
- Grafana JSON schema has version compatibility issues across releases — "can very easily break your configuration" [9].
- Grafana Crossplane Provider is alpha; K8s Operator is community-built without Helm chart [14].
- Windows compatibility for Perses is "problematic" — Docker recommended [22].
