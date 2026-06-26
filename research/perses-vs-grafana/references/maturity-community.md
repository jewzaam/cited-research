# Maturity & Community

Dimension 6 of the Perses vs Grafana comparison. Source details in [citations.md](../citations.md).

---

## Perses Maturity

### Project Timeline

| Date | Event | Source |
|------|-------|--------|
| January 26, 2021 | First commit | [7] |
| 2022 | Open-sourced by Amadeus | [11] |
| September 2023 | PromCon presentation | [8] |
| August 29, 2024 | CNCF Sandbox acceptance | [7] |
| May 2025 | SAP maintainer joins | [11] |
| April 29, 2026 | Operator v0.4.0 release | [6] |

### Community Metrics (from CNCF)

| Metric | Value | YoY Change | Source |
|--------|-------|------------|--------|
| Total contributors | 1,235 | +138% | [7] |
| Contributing organizations | 470 | +119% | [7] |
| GitHub stars | 975 | +131% | [7] |
| GitHub forks | 229 | +332% | [7] |
| Software value | $18.5M | — | [7] |
| Health Score | 82 (Excellent) | — | [7] |

Note: YoY growth percentages are high but absolute numbers remain small relative to mature projects. Contributor counts may include automated/bot contributions.

### Maturity Assessments

- "Very young project, still far from providing functionality and maturity equivalent to popular Grafana" [8]
- "Formative stages" [22]
- Plugin system "undergoing redesign" [9]
- Operator API v1alpha2: "unstable CRDs and API" [6]
- Red Hat COO integration is "technology preview" [10]

### Production Adopters

| Organization | Usage | Source |
|-------------|-------|--------|
| Amadeus | Originator; 5,000+ internal dashboards | [8] |
| Red Hat | OpenShift traces UI, COO 1.4 tech preview | [10] |
| SAP | Cloud Infrastructure monitoring, sovereign cloud (ApeiroRA) | [11] |
| Chronosphere | Platform embedding, code contributions | [8], [9] |
| Dash0 | Full dashboard compatibility, operator syncs | [9] |

### Release Cadence

No formal release cadence policy found for core Perses. Operator has 18 releases through v0.4.0 [6].

---

## Grafana Maturity

### Key Metrics (FY ending January 31, 2026)

| Metric | Value | Source |
|--------|-------|--------|
| ARR | >$400M | [18] |
| Customers | 7,000+ | [18] |
| Fortune 50 penetration | 70% | [18] |
| Employees | 1,400+ (40+ countries) | [18] |
| Users worldwide | 35M+ | [18] |
| Data source plugins | 160+ | [18] |
| Project age | 10+ years | [21] |

Note: Self-reported financials, not independently audited (private company) [18].

### Industry Recognition

| Award | Result | Source |
|-------|--------|--------|
| Gartner MQ for Observability Platforms (2025) | Leader, furthest for Completeness of Vision | [18] |
| Forbes Cloud 100 | #13 (5th consecutive year) | [18] |
| DevOps Dozen Awards 2025 | Best Observability Solution | [18] |

### Named Enterprise Customers

Anthropic, Bloomberg, NVIDIA, Microsoft, Salesforce, SpotOn, LexisNexis Risk Solutions, MasterControl [18].

### CNCF Relationship

- Silver member since 2017, Platinum since July 2021 [19]
- Governing Board seat (Tom Wilkie) [19]
- Contributed to: Prometheus, Cortex, Thanos, Jaeger, OpenTelemetry [19]
- Top contributor to OpenTelemetry and Prometheus [18]
- CNCF Technology Radar (2020): 2/3 paired Prometheus with Grafana [19]

### Release Cadence

Feature maturity stages: Experimental → Private Preview → Public Preview → GA [25]. Grafana 12 released in FY 2026 [18].

---

## Licensing

| Aspect | Perses | Grafana |
|--------|--------|---------|
| License | Apache 2.0 | AGPLv3 (core: Grafana, Loki, Tempo) |
| Relicensing | N/A | From Apache 2.0, April 21, 2021 |
| Plugins/agents | Apache 2.0 | Apache 2.0 |
| Network service requirement | None | Must share source if modified and served over network |
| OSI approved | Yes | Yes |
| Rationale | Vendor-neutral CNCF project | "Balance open source value with commercial sustainability" (Raj Dutt) |

The AGPLv3 relicensing "spurred CoreDash working group" which contributed to Perses's formation trajectory [8]. Grafana Labs chose AGPLv3 over SSPL/source-available to remain genuinely open source [17].

---

## Scale Comparison

| Metric | Perses | Grafana |
|--------|--------|---------|
| Age | ~5 years (first commit 2021) | 10+ years |
| GitHub stars | 975 | Not enumerated; 35M+ users |
| Contributors | 1,235 total | Not enumerated; 1,400+ employees |
| Production adopters (named) | 5 | 7,000+ customers |
| Revenue | N/A (CNCF project) | >$400M ARR |
| CNCF status | Sandbox (hosted project) | Platinum member (company) |

## Gaps and Limitations

- CNCF Sandbox status carries risk: 15-20% of sandbox projects are archived within three years.
- Perses contributor concentration: three primary companies (Amadeus, Red Hat, SAP/Chronosphere) — bus factor risk at organizational level.
- Grafana maturity metrics are self-reported from a private company.
- Perses release cadence is undocumented.
- No direct GitHub contributor count comparison available (Grafana's contributor page not fetched).
