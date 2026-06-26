# Architecture & Deployment Model

Dimension 1 of the Perses vs Grafana comparison. Source details in [citations.md](../citations.md).

---

## Perses Architecture

| Aspect | Detail | Source |
|--------|--------|--------|
| Storage backends | File-based (YAML/JSON on local filesystem) or SQL (MySQL only) | [1] |
| Multi-instance | SQL recommended: "Prefer the SQL config in case you are running multiple Perses instances" | [1] |
| Default listen | `:8080`, metrics at `/metrics` | [1] |
| Encryption | AES-256 for sensitive data; key must be exactly 32 bytes | [1] |
| Auth providers | Native (username/password), OIDC, OAuth, Kubernetes (TokenReview/SubjectAccessReview) | [1] |
| Token TTLs | Access: 15 min default, Refresh: 24h default | [1] |
| Read-only mode | Disables POST, PUT, DELETE endpoints | [1] |
| Provisioning | Auto-populates DB from filesystem folders at configurable interval (default 1h); "data from provisioning folder will totally override what exists in database" | [1] |
| Plugin loading | Configurable path, supports archived plugins extracted at startup, dev mode available | [1] |
| Datasource discovery | HTTP Service Discovery and Kubernetes Service Discovery | [1] |
| Build requirements | Go v1.23+, Node v22+, NPM v10+ | [21] |

### Kubernetes Deployment

| CRD | Scope | Purpose |
|-----|-------|---------|
| `Perses` | Namespaced | Deploys server (Deployment for SQL, StatefulSet for file-based/PVC) |
| `PersesDashboard` | Namespaced | Dashboard synced to Perses instances |
| `PersesDatasource` | Namespaced | Project-scoped datasource |
| `PersesGlobalDatasource` | Cluster-scoped | Datasource shared across all projects |

- API version: `perses.dev/v1alpha2` — "unstable CRDs and API, changes can happen frequently" [6]
- Production: "encourage usage for testing and development, but suggest caution in mission-critical environments" [6]
- Cert-manager required for webhook certificates [6]
- Helm chart "newly released" [6]
- Latest release: v0.4.0 (April 29, 2026), 18 total releases [6]
- Red Hat COO 1.4: technology preview of Red Hat build of Perses in OpenShift/ACM (April 2, 2026) [10]

### HA Support

No explicit HA documentation found. SQL backend enables multi-instance but no load-balancing guidance, notification deduplication, or active-active architecture is documented. Operator supports multi-instance sync via `instanceSelector` [6].

---

## Grafana Architecture

| Aspect | Detail | Source |
|--------|--------|--------|
| Storage backends | SQLite3 (default, NOT suitable for HA), MySQL, PostgreSQL | [16] |
| Deployment | Active-active behind load-balancing reverse proxy | [16] |
| Session management | Auth token strategy with database; sticky sessions NOT required | [16] |
| SSL | Termination at load balancer recommended | [16] |
| License | AGPLv3 (core: Grafana, Loki, Tempo); plugins/agents/libraries remain Apache 2.0 | [17] |

### High Availability

| Aspect | Detail | Source |
|--------|--------|--------|
| Database | Shared MySQL or PostgreSQL required | [16] |
| Topology | Active-active, multiple servers behind load balancer | [16] |
| Alerting HA | All alerts execute on every server; notifications deduplicated | [16] |
| Alert load distribution | NOT supported — every node evaluates every alert rule | [16] |
| Grafana Live | "Works with limitations in highly available setup" | [16] |
| Enterprise licensing | Requires shared hostname for license token | [16] |

### Kubernetes Deployment

Six as-code tools provide varying levels of K8s integration [14]:

| Tool | K8s Native | Platform | Notes |
|------|-----------|----------|-------|
| Crossplane Provider | Yes (CRDs) | Cloud + OSS | Alpha stage, active drift correction |
| K8s Operator | Yes (CRDs) | OSS only | Community-built, no Helm chart |
| Terraform Provider | No | Cloud + OSS | Broadest resource coverage |
| Grizzly | No (K8s-inspired YAML) | Cloud + OSS | CLI tool |
| Grafonnet | No | N/A | Jsonnet library (generator) |
| Ansible Collection | No | Cloud only | 8 resources |

---

## Architecture Comparison

| Dimension | Perses | Grafana |
|-----------|--------|---------|
| Storage | File-based (YAML/JSON) or MySQL | SQLite, MySQL, PostgreSQL |
| K8s-native CRDs | Official operator, 4 CRDs | Community operator; Crossplane (alpha) |
| HA | SQL for multi-instance; no formal HA docs | Documented active-active with shared DB |
| GitOps design | Purpose-built; percli CLI, CUE/Go SDKs | Retrofit; 6 third-party tools |
| Config model | Provisioning overrides DB ("totally override") | Provisioning can coexist with UI edits (allowUiUpdates) |
| Auth | Native, OIDC, OAuth, K8s | Native, LDAP, OIDC, OAuth, SAML (Enterprise) |
| License | Apache 2.0 | AGPLv3 (core) |

## Gaps and Limitations

- Perses HA architecture is undocumented beyond "use SQL for multi-instance." No load-balancing, failover, or notification deduplication guidance found.
- Perses supports MySQL only for SQL backend; no PostgreSQL or SQLite.
- Grafana K8s Operator is community-built with no official Helm chart.
- Grafana Crossplane Provider is alpha stage.
- Perses operator explicitly warns against production use.
