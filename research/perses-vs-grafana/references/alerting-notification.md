# Alerting & Notification

Dimension 5 of the Perses vs Grafana comparison. Source details in [citations.md](../citations.md).

---

## Perses: No Built-in Alerting

Perses deliberately excludes alerting from its scope. This is confirmed by four independent sources:

| Source | Statement | Citation |
|--------|-----------|----------|
| Dash0 | "No built-in alerting" | [9] |
| SigNoz | "Does not include alerting or data storage" | [23] |
| AppsCode | Alerting absent from feature matrix entirely | [21] |
| Perses Migration docs | "Only dashboards migrate — can't migrate alerts, users, etc." (alerting is not a Perses concept) | [4] |

### Design Rationale

Perses treats alerting as the responsibility of the underlying metrics backend (Prometheus/Alertmanager). The Perses Operator supports Prometheus alerting rules managed via CRDs [6], but this is Prometheus-native alerting, not Perses-native alerting.

Community mixins can include `alertRules`, but these are managed externally [10].

---

## Grafana: Unified Alerting

### Architecture

Unified alerting introduced in Grafana 8 with a common API backing the engine [15]:

| Feature | Detail | Source |
|---------|--------|--------|
| Alert types | Grafana-managed (multi-dimensional, multi-datasource) + Cortex/Loki-managed | [15] |
| Multi-dimensional | Single rule generates multiple alert instances | [15] |
| Expressions | Math and reduce expressions across data sources | [15] |
| Panel support | Time series, Table, Heatmap (decoupled from Graph panels) | [15] |

### Notification Architecture

| Component | Purpose | Source |
|-----------|---------|--------|
| Contact Points | Define receivers (e.g., email, Slack) | [15] |
| Notification Policies | Define routing logic (label-based matching) | [15] |
| Silences | Temporary notification suppression, dedicated section | [15] |

Notification channels (13+ supported via provisioning) [12]:

| Category | Channels |
|----------|----------|
| Chat/messaging | Slack, Discord, Telegram, Google Chat, Microsoft Teams |
| Incident management | PagerDuty, OpsGenie, VictorOps |
| Infrastructure | Kafka, MQTT, Prometheus Alertmanager |
| General | Webhook (TLS + HMAC), Email, Pushover |

### High Availability

- All alerts execute on every server; notifications deduplicated [16]
- Alert load distribution between servers NOT supported [16]
- Without additional setup steps, duplicate notifications may occur [16]

### Provisioning

Full alerting provisioning via YAML files: alert rules, contact points, notification policies [12]. Ansible Collection also manages alert contact points and notification policies [14].

---

## Comparison

| Dimension | Perses | Grafana |
|-----------|--------|---------|
| Built-in alerting | **No** | Yes (unified since Grafana 8) |
| Alert types | N/A | Grafana-managed + Cortex/Loki-managed |
| Multi-datasource alerts | N/A | Yes |
| Notification channels | N/A | 13+ (Slack, PagerDuty, etc.) |
| Notification routing | N/A | Label-based via Notification Policies |
| Silences | N/A | Yes, dedicated section |
| HA alerting | N/A | All-node execution + dedup |
| Alerting provisioning | N/A | Full YAML-based provisioning |
| External alerting | Delegates to Prometheus/Alertmanager | Built-in + external |

## Gaps and Limitations

- Perses's lack of alerting is a fundamental architectural gap for teams wanting a single pane of glass for monitoring and alerting.
- No Perses roadmap item found for adding alerting — unclear if permanently out of scope or deferred.
- Grafana alerting HA does not distribute alert evaluation load — all nodes run all rules, which may not scale efficiently.
- Grafana unified alerting UI for Prometheus-style alerts was initially "heavily skewed towards YAML-like textbox editors" but has since improved [15].
