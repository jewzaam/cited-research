# Citations — Perses vs Grafana

All sources visited in-session via WebSearch or WebFetch on 2026-06-26.

---

**[1]** "Configuration." *Perses Documentation*, n.d.
<https://perses.dev/perses/docs/configuration/configuration/>
**Tier:** 2
Data extracted: Storage backends (file-based YAML/JSON, SQL/MySQL), auth methods (native, OIDC, OAuth, Kubernetes), AES-256 encryption, provisioning behavior, datasource discovery (HTTP SD, K8s SD), server configuration.

**[2]** "Dashboard." *Perses API Documentation*, n.d.
<https://perses.dev/perses/docs/api/dashboard/>
**Tier:** 2
Data extracted: Dashboard data model specification — 16 panel plugin kinds, Grid layout system, $ref panel referencing, datasource backends (Prometheus, Loki, ClickHouse, Tempo, Pyroscope, VictoriaLogs), REST API endpoints.

**[3]** "Project." *Perses Concepts Documentation*, n.d.
<https://perses.dev/perses/docs/concepts/project/>
**Tier:** 2
Data extracted: Project-based multi-tenancy model, resource scoping (7 project-scoped resource types), auto-ownership, dual-scope model for datasources/variables.

**[4]** "Migrate from Grafana." *Perses Documentation*, n.d.
<https://perses.dev/perses/docs/migration/>
**Tier:** 2
Data extracted: Three migration methods (UI, CLI, API), best-effort semantics, dashboards-only scope, unsupported plugin placeholder values, Grafana 9.0.0 baseline compatibility.

**[5]** "Getting Started with Dashboard-as-Code." *Perses Documentation*, n.d.
<https://perses.dev/perses/docs/dac/getting-started/>
**Tier:** 2
Data extracted: CUE SDK (percli >=v0.51.0, cue >=v0.12.0) and Go SDK (percli >=v0.44.0) workflows, percli dac build/apply commands, GitHub Actions support via perses/cli-actions, offline vs online validation.

**[6]** "Perses Operator." *GitHub — perses/perses-operator*, n.d.
<https://github.com/perses/perses-operator>
**Tier:** 2
Data extracted: 4 CRDs (Perses, PersesDashboard, PersesDatasource, PersesGlobalDatasource), API version v1alpha2 ("unstable"), production caution warning, cert-manager requirement, v0.4.0 latest (April 29, 2026), 18 total releases.

**[7]** "Perses." *CNCF Projects*, n.d.
<https://www.cncf.io/projects/perses/>
**Tier:** 1
Data extracted: CNCF Sandbox accepted August 29, 2024. Health Score 82. Contributors: 1,235 (+138% YoY). Orgs: 470 (+119% YoY). Stars: 975 (+131% YoY). Forks: 229 (+332% YoY). Software value: $18.5M. First commit: January 26, 2021.

**[8]** "PromCon Recap: Unveiling Perses." *Logz.io Blog*, 2023.
<https://logz.io/blog/promcon-recap-perses-project/>
**Tier:** 3
Data extracted: Amadeus origin (5,000+ dashboards), Augustin Husson (creator, Prometheus maintainer), PromCon Sept 2023 presentation, three contributing companies (Amadeus, Red Hat, Chronosphere), maturity assessment ("very young project, still far from Grafana"), CoreDash working group, embeddable NPM packages.

**[9]** "What is Perses?" *Dash0 Knowledge Base*, n.d.
<https://www.dash0.com/knowledge/what-is-perses>
**Tier:** 3
Data extracted: Data sources (Prometheus, Thanos, Jaeger native), plugin system "undergoing redesign," K8s operator on roadmap, no built-in alerting, adopters (Red Hat, SAP, Chronosphere, Dash0), code-first vs UI comparison.
Note: Dash0 is a Perses adopter; potential bias.

**[10]** "Red Hat build of Perses with the cluster observability operator." *Red Hat Developer*, April 2, 2026.
<https://developers.redhat.com/articles/2026/04/02/red-hat-build-perses-cluster-observability-operator>
**Tier:** 2
Data extracted: COO 1.4 technology preview, OpenShift/ACM integration, 6 auto-deployed ClusterRoles, PersesDatasource vs PersesGlobalDatasource scoping, dashboard management UI, Grafana import, datasource support (Prometheus/Thanos, Loki, Tempo), migration methods.

**[11]** "Moving ahead in Dashboard Visualization with Perses." *SAP Community Blog*, 2025.
<https://community.sap.com/t5/technology-blog-posts-by-sap/moving-ahead-in-dashboard-visualization-with-perses/ba-p/14420905>
**Tier:** 3
Data extracted: SAP adoption via ApeiroRA (IPCEI-CIS EU initiative), Akshay Iyyadurai Balasundaram became maintainer May 2025, ~100 merged PRs, contributions (MCP Server, Helm chart ownership), sovereign cloud motivation.

**[12]** "Provision Grafana." *Grafana Documentation*, n.d.
<https://grafana.com/docs/grafana/latest/administration/provisioning/>
**Tier:** 2
Data extracted: File-based provisioning via YAML, dashboard providers (filesystem paths, foldersFromFilesStructure up to 4 levels), allowUiUpdates behavior, env var interpolation, filesystem watch (<= 10s) vs polling (>10s), alerting provisioning (13+ notification channels: Slack, Discord, Telegram, Google Chat, Teams, PagerDuty, OpsGenie, VictorOps, Kafka, MQTT, Webhook, Email, Pushover).

**[13]** "Role-based access control." *Grafana Documentation*, n.d.
<https://grafana.com/docs/grafana/latest/administration/roles-and-permissions/access-control/>
**Tier:** 2
Data extracted: OSS = 5 basic roles only, Enterprise/Cloud = fixed roles + custom roles (action + scope pairs), automatic permission drift, folder "General" RBAC limitation, 20+ resource categories for fixed roles.

**[14]** "A complete guide to managing Grafana as code." *Grafana Labs Blog*, n.d.
<https://grafana.com/blog/a-complete-guide-to-managing-grafana-as-code-tools-tips-and-tricks/>
**Tier:** 2
Data extracted: Six as-code tools (Terraform Provider, Crossplane Provider alpha, K8s Operator community-built/OSS-only, Grizzly CLI, Grafonnet Jsonnet library, Ansible Collection Cloud-only/8 resources), Crossplane active drift correction, platform support matrix.

**[15]** "The new unified alerting system for Grafana." *Grafana Labs Blog*, n.d.
<https://grafana.com/blog/the-new-unified-alerting-system-for-grafana-everything-you-need-to-know/>
**Tier:** 2
Data extracted: Unified alerting in Grafana 8, common API, two alert types (Grafana-managed multi-dimensional + Cortex/Loki-managed), Contact Points + Notification Policies architecture, label-based routing, Silences, multi-panel support (Time series, Table, Heatmap).

**[16]** "Set up Grafana for high availability." *Grafana Documentation*, n.d.
<https://grafana.com/docs/grafana/latest/setup-grafana/set-up-for-high-availability/>
**Tier:** 2
Data extracted: Active-active behind load balancer, shared MySQL/Postgres required (SQLite unsuitable), session affinity not required, alerting HA (all nodes execute all alerts, deduplicate notifications), alert load distribution NOT supported, Grafana Live limitations.

**[17]** "Grafana, Loki, and Tempo will be relicensed to AGPLv3." Dutt, Raj. *Grafana Labs Blog*, April 21, 2021.
<https://grafana.com/blog/2021/04/20/grafana-loki-tempo-relicensing-to-agplv3/>
**Tier:** 2
Data extracted: Apache 2.0 to AGPLv3 relicensing (Grafana, Loki, Tempo), plugins/agents/libraries remain Apache 2.0, OSI-approved, rationale (commercial sustainability, reciprocal contribution), source code sharing requirement for network services.

**[18]** "Grafana Labs caps a breakout year of growth and product innovation." *Grafana Labs Press Release*, February 3, 2026.
<https://grafana.com/press/2026/02/03/grafana-labs-caps-a-breakout-year-of-growth-and-product-innovation/>
**Tier:** 2
Data extracted: ARR >$400M, 7,000+ customers, 70% Fortune 50, 1,400+ employees, 35M+ users, 160+ data source plugins, Gartner MQ Leader (Observability), Forbes Cloud 100 #13, Grafana 12 released.
Note: Self-reported financials, not independently audited (private company).

**[19]** "CNCF Announces Grafana Labs Upgrades Membership to Platinum." *CNCF Announcements*, July 28, 2021.
<https://www.cncf.io/announcements/2021/07/28/cloud-native-computing-foundation-announces-grafana-labs-upgrades-membership-to-platinum/>
**Tier:** 1
Data extracted: Silver member since 2017, Platinum upgrade July 2021, Governing Board seat (Tom Wilkie), contributed to Prometheus/Cortex/Thanos/Jaeger/OpenTelemetry, CNCF Technology Radar 2/3 pair Prometheus with Grafana.

**[20]** "Single-tenant vs. multi-tenant architecture with Grafana Cloud." *Grafana Labs Blog*, n.d.
<https://grafana.com/blog/single-tenant-vs-multi-tenant-architecture-with-grafana-cloud-how-to-choose-the-right-approach/>
**Tier:** 2
Data extracted: Single-stack (RBAC + LBAC) vs multi-stack models, LBAC with Prometheus label selectors, misconfigured LBAC = data leak risk, multi-stack for complete isolation/resellers/regulated environments, cross-stack correlation doesn't work.

**[21]** "Getting Started with Perses: The Free, Open Source Grafana Alternative." *AppsCode Blog*, n.d.
<https://appscode.com/blog/post/getting-started-with-perses-the-free-open-source-grafana-alternative/>
**Tier:** 3
Data extracted: Feature matrix (code-first vs UI-first, 100+ vs 2 data sources, DB vs CRDs/Git storage, third-party vs native GitOps, external vs native K8s, manual vs CI/CD validation), licensing comparison, build requirements (Go v1.23+, Node v22+, NPM v10+).

**[22]** "Perses — A new language for dashboards?" *SquaredUp Blog*, n.d.
<https://squaredup.com/blog/perses-a-new-language-for-dashboards/>
**Tier:** 3
Data extracted: Windows compatibility "problematic," Prometheus-only datasource at time of review, Go SDK workflow (Go -> YAML -> JSON -> curl POST), multiple intermediate steps, "formative stages" assessment.
Note: SquaredUp is a competing dashboard vendor; review may predate recent Perses data source additions.

**[23]** "7 Grafana Alternatives in 2026." *SigNoz Blog*, n.d.
<https://signoz.io/blog/grafana-alternatives/>
**Tier:** 3
Data extracted: Perses = "CNCF Sandbox dashboarding tool targeting visualization layer," no alerting, no data storage, dashboard layer only, fewer panel types and community plugins, best dashboard-only alternative, Apache 2.0 vs AGPLv3.
Note: SigNoz is a Grafana competitor; potential bias.

**[24]** "Grafana Alerting." *Grafana Documentation*, n.d.
<https://grafana.com/docs/grafana/latest/alerting/>
**Tier:** 2
Data extracted: Multi-datasource alert queries, metrics and log alerting, consolidated management view, notification configuration.
Note: Landing page — limited depth; detailed specs in sub-pages.

**[25]** "Release life cycle for Grafana Labs." *Grafana Documentation*, n.d.
<https://grafana.com/docs/release-life-cycle/>
**Tier:** 2
Data extracted: Four maturity stages (Experimental, Private Preview, Public Preview, GA), support levels by stage, GA = fully supported with SLA.
Note: Does not contain version release cadence; only feature maturity stages.
