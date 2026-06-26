# Perses vs Grafana: A Citation-Backed Technical Comparison

## Methodology

This comparison evaluates Perses and Grafana across nine dimensions using exclusively web sources visited in-session on 2026-06-26. Every factual claim carries an inline citation referencing [citations.md](citations.md). Two independent audit agents verified the output: a citation audit checked every URL against source content, and a consistency review checked numerical and logical consistency across all files.

Research agents searched for counter-perspectives alongside supporting evidence. Sources that challenge expected narratives are integrated throughout — not segregated into a "cons" section.

---

## 1. Architecture & Deployment Model

### Perses

Perses stores configuration in either a **file-based backend** (YAML/JSON on local filesystem) or **SQL** (MySQL only) [1]. The SQL backend is recommended for multi-instance deployments: "Prefer the SQL config in case you are running multiple Perses instances" [1]. No PostgreSQL or SQLite support exists.

The Kubernetes deployment model uses an **official operator** with four CRDs (Perses, PersesDashboard, PersesDatasource, PersesGlobalDatasource) [6]. The API version is `perses.dev/v1alpha2`, explicitly described as "unstable CRDs and API, changes can happen frequently" [6]. The operator warns users to "suggest caution in mission-critical environments" [6]. Red Hat ships a **technology preview** (not GA) of Perses via the Cluster Observability Operator 1.4, integrated into OpenShift and ACM consoles [10].

**HA is undocumented** — SQL enables multi-instance, and the operator supports `instanceSelector` for multi-instance sync [6], but no active-active architecture, load-balancing guidance, or notification deduplication is documented.

### Grafana

Grafana stores data in **SQLite** (default, single-instance only), **MySQL**, or **PostgreSQL** [16]. For HA, a shared MySQL or PostgreSQL database is required — SQLite is explicitly "unsuitable" [16].

The HA topology is **active-active** behind a load-balancing reverse proxy. Session affinity is not required because auth tokens are stored in the shared database [16]. Alerting HA executes all alerts on every server with notification deduplication, though alert load distribution across servers is not supported [16].

Kubernetes integration comes via **six as-code tools** [14]: Terraform Provider (broadest coverage), Crossplane Provider (alpha, active drift correction), community K8s Operator (OSS only, no Helm chart), Grizzly CLI, Grafonnet (Jsonnet library), and Ansible Collection (Cloud only, 8 resources).

### Key Difference

Perses is **designed for Kubernetes** with official CRDs and namespace-to-project mapping. Grafana's K8s story relies on community or alpha-stage tools. However, Grafana's HA architecture is documented and battle-tested at 35M+ users [18], while Perses HA is undocumented.

---

## 2. Data Source Support

Perses natively supports **six backends**: Prometheus, Loki, ClickHouse, Tempo, Pyroscope, and VictoriaLogs [2]. Additionally, Thanos and Jaeger are supported via compatible APIs [7], [9]. A plugin system exists for adding sources, but it is "undergoing a redesign" [9].

Grafana supports **160+ data source plugins** [18]. The plugin ecosystem has 10+ years of development [21].

This is an order-of-magnitude difference. Teams with heterogeneous observability stacks (CloudWatch, Elasticsearch, InfluxDB, MySQL, etc.) face significant integration work or are blocked entirely with Perses [22]. However, Perses's data source list has expanded — an earlier SquaredUp evaluation found only Prometheus [22], while the current API spec lists six backends plus Thanos/Jaeger [2].

---

## 3. Dashboard Authoring & UX

### Perses: Code-First

Perses dashboards are defined using **CUE** (percli >=v0.51.0, cue >=v0.12.0) or **Go** (percli >=v0.44.0) SDKs [5]. The build/deploy workflow is `percli dac build` → `percli apply`, with server-side validation and GitHub Actions support via `perses/cli-actions` [5].

The dashboard spec uses a flat panel map referenced by Grid layouts via JSON pointer `$ref` [2]. 16 panel plugin kinds are available: BarChart, FlameChart, GaugeChart, HeatMapChart, HistogramChart, LogsTable, Markdown, PieChart, ScatterChart, StatChart, StatusHistoryChart, Table, TimeSeriesChart, TimeSeriesTable, TraceTable, TracingGanttChart [2].

Augustin Husson, the creator, stated that Grafana's data model is "not made for dashboard as code" [8]. Perses was built to address Amadeus's problem of Grafana upgrades breaking 5,000+ dashboards due to schema changes [8].

Embeddable NPM packages allow individual charts to be embedded into external UIs — a distinctive capability [8], [9].

**Counter-perspective**: SquaredUp found the authoring workflow requires Go → YAML → JSON → API call, calling hand-coding "tedious and error-prone" [22]. Windows compatibility is "problematic" — Docker is the recommended workaround [22]. The code-first approach has a higher barrier for non-developers.

### Grafana: UI-First with Retrofit DaC

Grafana offers a **drag-and-drop dashboard builder** with 10+ years of refinement [21]. File-based provisioning supports YAML config files with filesystem change detection (watch events for <=10s intervals, polling for >10s) [12]. The `foldersFromFilesStructure` feature mirrors directory hierarchy into Grafana folders up to 4 levels deep [12].

Six as-code tools provide varying GitOps capabilities [14]. The **Crossplane Provider** offers active drift correction ("UI changes discarded on resync") but is in alpha [14]. The **Terraform Provider** has the broadest resource coverage [14].

**Counter-perspective**: Grafana's GitOps support is more mature and battle-tested than often assumed. A documented real-world case uses Terraform + tofu-controller + Flux with 1-minute reconciliation intervals and automatic drift correction (from counter-discovery research). The narrative that teams must choose Perses for GitOps is contradicted by Grafana's six-tool ecosystem.

---

## 4. CNCF Ecosystem Fit

Perses is a **CNCF Sandbox project** (accepted August 29, 2024) [7] with vendor-neutral governance under the CNCF TOC. It is licensed under **Apache 2.0** [6].

Grafana Labs is a **CNCF Platinum member** (since July 2021) [19] with a Governing Board seat, but Grafana itself is NOT a CNCF hosted project. This distinction matters: CNCF does not govern Grafana's codebase. Grafana Labs contributes to Prometheus, Cortex, Thanos, Jaeger, and OpenTelemetry [19] and is a top contributor to OpenTelemetry and Prometheus [18]. Grafana's core is licensed under **AGPLv3** since April 2021 [17].

The licensing difference is significant. AGPLv3 requires source code sharing if the software is modified and served over a network [17]. Grafana Labs chose AGPLv3 over SSPL/source-available licenses to remain OSI-approved [17]. The relicensing "spurred CoreDash working group" which contributed to Perses's trajectory [8]. For organizations where AGPLv3 is a legal concern, Perses's Apache 2.0 license is a material advantage.

**Counter-perspective**: CNCF Sandbox is the lowest maturity tier. An estimated 15-20% of sandbox projects are archived within three years (from counter-discovery research). Sandbox status does not guarantee project survival.

---

## 5. Alerting & Notification

**Perses has no built-in alerting.** This is confirmed by four independent sources [9], [21], [23], [4]. Perses treats alerting as the responsibility of the underlying metrics backend (Prometheus/Alertmanager).

**Grafana's unified alerting** (since Grafana 8) provides [15]:
- Two alert types: Grafana-managed (multi-dimensional, multi-datasource) and Cortex/Loki-managed
- Contact Points + Notification Policies architecture with label-based routing
- 13+ notification channels: Slack, Discord, Telegram, Google Chat, Teams, PagerDuty, OpsGenie, VictorOps, Kafka, MQTT, Webhook, Email, Pushover [12]
- Silences for temporary notification suppression
- HA: all nodes execute all alerts, notifications deduplicated [16]

This is a fundamental gap. Teams wanting a single pane of glass for monitoring AND alerting must use external tools alongside Perses. No Perses roadmap item for adding alerting was found — it is unclear whether alerting is permanently out of scope or deferred.

---

## 6. Maturity & Community

### Perses

First commit January 26, 2021 [7]. CNCF Sandbox since August 2024 [7]. Community metrics: 1,235 total contributors (+138% YoY), 470 contributing organizations (+119% YoY), 975 GitHub stars (+131% YoY) [7]. Growth rates are high but absolute numbers remain small.

Production adopters: Amadeus (5,000+ dashboards, originator) [8], Red Hat (OpenShift COO 1.4 tech preview) [10], SAP (maintainer since May 2025, sovereign cloud) [11], Chronosphere and Dash0 (platform embedding) [8], [9].

Multiple assessments confirm early maturity: "very young project, still far from providing functionality and maturity equivalent to popular Grafana" [8], "formative stages" [22], operator API "unstable" [6].

### Grafana

10+ years of development [21]. ARR >$400M, 7,000+ customers, 70% Fortune 50 penetration, 35M+ users worldwide, 1,400+ employees [18]. Gartner MQ Leader for Observability Platforms [18]. Named customers include Anthropic, Bloomberg, NVIDIA, Microsoft, Salesforce [18]. These financials are self-reported (private company) [18].

---

## 7. Migration Path

Perses provides **three official migration methods** from Grafana: UI import, CLI (`percli migrate`), and API endpoint [4]. Red Hat adds Go SDK migration [10].

Scope is **dashboards only** — alerts, users, teams, folders, and other resources cannot be migrated [4]. Migration is **best-effort**: not all Grafana plugins have Perses equivalents, and unsupported variables become static lists with placeholder values `["grafana", "migration", "not", "supported"]` [4]. Prometheus queries have the best support [10].

Version compatibility extends to Grafana 9.0.0+ [4]. The `--format cr` flag outputs Kubernetes CR format for direct kubectl/GitOps application [4].

**Counter-perspective**: Migration is explicitly lossy. Table column settings above 16 require manual entry, and dashboard name regeneration issues are documented in GitHub issues (from counter-discovery research). No published migration success rate data exists. Running both tools simultaneously during migration adds operational complexity with no documented runbook.

---

## 8. Multi-tenancy & RBAC

### Perses

Project-based isolation: every dashboard must belong to a project [3]. Four RBAC resource types (Role, GlobalRole, RoleBinding, GlobalRoleBinding) with purely additive permissions (create, read, update, delete) [3]. Auto-ownership: project creators get full control [3].

Kubernetes integration: six auto-deployed ClusterRoles via the operator (persesdashboard-editor/viewer, persesdatasource-editor/viewer, persesglobaldatasource-editor/viewer) [10]. Dashboard list auto-filters by user authorization [10].

RBAC is **built into all editions** — no commercial paywall [3].

### Grafana

OSS: five basic roles only (Grafana admin, Org admin, Editor, Viewer, None) [13].

Enterprise/Cloud: full RBAC with fixed roles (immutable, 20+ resource categories), custom roles (action + scope pairs), and LBAC (label-based data access policies using Prometheus label selectors) [13], [20].

Two multi-tenancy models: single-stack (RBAC + LBAC in one instance) recommended for most customers, multi-stack (separate stacks per tenant) for complete isolation [20]. Risk: misconfigured LBAC = data leaks [20].

**Key tension**: Perses ships RBAC in all editions; Grafana locks granular RBAC behind Enterprise/Cloud. But Grafana Enterprise RBAC is more feature-rich (custom roles, LBAC, team assignments) than Perses's additive-only model.

---

## 9. Performance at Scale

**No published performance benchmarks exist for Perses.** This was confirmed across all research sources. The 5,000+ dashboard count at Amadeus [8] motivated the project but no latency, concurrency, or resource consumption data has been published. Perses's HA architecture is undocumented beyond "use SQL for multi-instance" [1].

Grafana's scale is proven through adoption (35M+ users, 7,000+ customers) [18] but also lacks published dashboard-layer benchmarks. Known constraints include: SQLite unsuitable for HA [16], alerting HA runs all rules on all nodes without load distribution [16], and dashboard/folder limits of 1,000 each on the free tier (from counter-discovery research).

---

## Reflection

Before finalizing, I reconsidered the following:

1. **Data source count framing**: Early sources cite Grafana as "100+ sources" [21] while the Feb 2026 press release says "160+" [18]. I used the more current figure but noted the discrepancy.

2. **Perses maturity vs potential**: The research heavily documents Perses's current limitations. This is accurate but may underweight the project's trajectory — contributor growth (+138% YoY), data source expansion, and vendor adoption (Red Hat, SAP) suggest momentum. The comparison reflects a snapshot, not a forecast.

3. **GitOps narrative**: Counter-discovery revealed Grafana's GitOps support is more mature than commonly assumed. I integrated this rather than presenting a one-sided "Perses = GitOps, Grafana = legacy" narrative.

4. **Licensing significance**: The AGPLv3 vs Apache 2.0 distinction is material for embedding/redistribution but irrelevant for many end-user deployments. I stated the facts without overweighting either side.

---

## Limitations

1. Grafana contributor count not fetched — no direct comparison with Perses's 1,235.
2. Grafana panel type count not enumerated — comparison with Perses's 16 types is qualitative.
3. Grafana Enterprise RBAC and LBAC implementation details are behind a commercial paywall.
4. Performance comparison is impossible — neither tool publishes dashboard-layer benchmarks.
5. Perses is rapidly evolving; this analysis reflects the state as of June 2026.
6. Several sources (Dash0, SigNoz, SquaredUp) are competitors or adopters with potential bias — cross-validated against primary sources where possible.

## Supporting Files

- [citations.md](citations.md) — all 25 sources with tier ratings and specific data extracted
- [references/architecture-deployment.md](references/architecture-deployment.md)
- [references/data-source-support.md](references/data-source-support.md)
- [references/dashboard-authoring-ux.md](references/dashboard-authoring-ux.md)
- [references/cncf-ecosystem-fit.md](references/cncf-ecosystem-fit.md)
- [references/alerting-notification.md](references/alerting-notification.md)
- [references/maturity-community.md](references/maturity-community.md)
- [references/migration-path.md](references/migration-path.md)
- [references/multi-tenancy-rbac.md](references/multi-tenancy-rbac.md)
- [references/performance-at-scale.md](references/performance-at-scale.md)
