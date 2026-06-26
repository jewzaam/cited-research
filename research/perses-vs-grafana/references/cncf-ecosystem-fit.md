# CNCF Ecosystem Fit

Dimension 4 of the Perses vs Grafana comparison. Source details in [citations.md](../citations.md).

---

## Perses CNCF Status

| Metric | Value | Source |
|--------|-------|--------|
| CNCF level | Sandbox | [7] |
| Acceptance date | August 29, 2024 | [7] |
| Health Score | 82 (Excellent) | [7] |
| Total contributors | 1,235 (+138% YoY) | [7] |
| Contributing organizations | 470 (+119% YoY) | [7] |
| GitHub stars | 975 (+131% YoY) | [7] |
| GitHub forks | 229 (+332% YoY) | [7] |
| Software value | $18.5M | [7] |
| First commit | January 26, 2021 | [7] |
| License | Apache 2.0 | [6], [8] |
| Governance | CNCF TOC oversight, Linux Foundation | [7], [8] |

### Kubernetes-Native Features

- Official Perses Operator with 4 CRDs [6]
- Helm charts via `perses/helm-charts` repository [6]
- Namespace-to-project mapping [6]
- PersesDashboard and PersesDatasource CRDs for declarative management [6]
- FluxCD integration documented in Helm docs [6]
- Community mixins (alertRules and dashboards) for K8s, Node, Thanos [10]

### Contributing Companies

| Company | Role | Source |
|---------|------|--------|
| Amadeus | Originator, end-user (5,000+ dashboards) | [8] |
| Red Hat | OpenShift integration (COO 1.4 tech preview) | [10] |
| SAP | Maintainer since May 2025, sovereign cloud initiative | [11] |
| Chronosphere | Platform embedding, code contributions | [8], [9] |
| Dash0 | Platform embedding | [9] |

### Origin Context

The CNCF CoreDash working group, formed partly in response to Grafana's AGPLv3 relicensing, contributed to Perses's trajectory toward CNCF membership [8]. Creator Augustin Husson is also a Prometheus maintainer [8].

---

## Grafana CNCF Status

| Metric | Value | Source |
|--------|-------|--------|
| CNCF membership level | Platinum (not a hosted project) | [19] |
| Silver membership | 2017 | [19] |
| Platinum upgrade | July 28, 2021 | [19] |
| Governing Board seat | Tom Wilkie (VP Product) | [19] |
| Contributed CNCF projects | Prometheus, Cortex, Thanos, Jaeger, OpenTelemetry | [19] |
| License | AGPLv3 (core); plugins/agents remain Apache 2.0 | [17] |

### Kubernetes Integration

- Community K8s Operator (CRDs, OSS only, no official Helm chart) [14]
- Crossplane Provider (K8s CRDs, alpha stage, ArgoCD compatible) [14]
- File-based provisioning via ConfigMaps [12]
- Grafana Operator manages dashboards as CRDs with ArgoCD [14]

### Ecosystem Presence

- CNCF End User Technology Radar (Sept 2020): 2/3 of respondents paired Prometheus with Grafana [19]
- "Prolific contributor" to CNCF projects [19]
- Top contributor to OpenTelemetry and Prometheus (as of FY 2026) [18]
- Beyla (eBPF auto-instrumentation) donated to OpenTelemetry community [18]

---

## Comparison

| Dimension | Perses | Grafana |
|-----------|--------|---------|
| CNCF relationship | Hosted project (Sandbox) | Company membership (Platinum) |
| Governance | CNCF TOC, vendor-neutral | Corporate (Grafana Labs) |
| License | Apache 2.0 | AGPLv3 (core) |
| K8s CRDs | Official operator, 4 CRDs | Community operator; Crossplane (alpha) |
| Helm chart | Official | Community |
| K8s auth | Native (TokenReview/SubjectAccessReview) [1] | Via operator or proxy |

## Gaps and Limitations

- Perses is CNCF Sandbox (lowest maturity tier) — 15-20% of sandbox projects are archived within three years.
- Grafana is NOT a CNCF hosted project — it is a CNCF Platinum member company. This distinction matters: CNCF does not govern Grafana's codebase.
- Perses operator at v1alpha2 with production-use caution warning [6].
- Grafana's community K8s Operator has no official Helm chart [14].
- Perses contributor metrics (1,235 total) may include automated/bot contributions at the CNCF tracking level.
