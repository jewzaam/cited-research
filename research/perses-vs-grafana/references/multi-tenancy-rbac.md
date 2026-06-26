# Multi-tenancy & RBAC

Dimension 8 of the Perses vs Grafana comparison. Source details in [citations.md](../citations.md).

---

## Perses Multi-tenancy Model

### Project-Based Isolation

Projects serve as the fundamental isolation boundary [3]:
- Every dashboard must belong to a project [3]
- Projects can be personal or collaborative [3]
- Server-level permissions govern project creation [3]
- Creator auto-gets Owner role with full control (edit, rename, delete) [3]

### Resource Scoping

| Scope | Resources | Source |
|-------|-----------|--------|
| Project-scoped | Dashboards, Datasources, Variables, Secrets, Roles, RoleBindings, Ephemeral Dashboards | [3] |
| Global | GlobalDatasources, GlobalRoles, GlobalRoleBindings | [3], [6] |

Dual-scope model: datasources and variables can exist at global or project level. Lower scopes override higher scopes [3].

### RBAC Model

Kubernetes-inspired with four resource types [3], [10]:
- **Role** — scoped to project
- **GlobalRole** — spans all projects
- **RoleBinding** — binds role to user within project
- **GlobalRoleBinding** — binds role across all projects

Permission actions: create, read, update, delete — purely additive, no deny rules [3].

### Kubernetes RBAC Integration

Red Hat COO auto-deploys six ClusterRoles [10]:

| ClusterRole | Access |
|-------------|--------|
| `persesdashboard-editor-role` | CRUD on dashboards |
| `persesdashboard-viewer-role` | Read-only on dashboards |
| `persesdatasource-editor-role` | CRUD on datasources |
| `persesdatasource-viewer-role` | Read-only on datasources |
| `persesglobaldatasource-editor-role` | CRUD on global datasources |
| `persesglobaldatasource-viewer-role` | Read-only on global datasources |

- ClusterRoleBinding: access across all namespaces/projects [10]
- RoleBinding: restricted to specific namespace/project [10]
- Dashboard list auto-filters by user authorization [10]

### Auth Providers

Native (username/password), OIDC, OAuth, Kubernetes (TokenReview/SubjectAccessReview) [1]. Kubernetes auth supports configurable QPS (default 500) and burst (default 1000) [1].

---

## Grafana Multi-tenancy Model

### Organization-Based Isolation

Two architectural approaches [20]:

**Single-Stack** (recommended for most customers):
- RBAC for role-based access control [20]
- LBAC (Label-Based Access Control): Prometheus label selectors restrict data queries [20]
- Risk: misconfigured LBAC = data leaks [20]

**Multi-Stack** (for complete isolation needs):
- Each tenant gets distinct UI frontend and backend [20]
- Cross-stack correlation doesn't work [20]
- Recommended for: resellers/MSPs, highly regulated environments [20]

### RBAC Model

**OSS** (5 basic roles) [13]:
1. Grafana administrator
2. Organization administrator
3. Editor
4. Viewer
5. None

**Enterprise/Cloud** (full RBAC) [13]:
- Fixed roles: immutable, assignable to users/teams/service accounts
- Custom roles: action + scope pairs (e.g., `teams.roles:read` + `teams:id:1`)
- Basic role modification (new permissions auto-added to modified basic roles)
- 20+ resource categories covered by fixed roles

### Folder Permissions

- Folders serve as permission boundaries [13]
- Permissions cascade to subfolders and dashboards [13]
- Permission levels: View, Edit, Admin [13]
- Assignable to users, teams, service accounts, roles [13]
- Limitation: folder named "General" or "general" cannot have RBAC permissions managed [13]

### Backend Multi-tenancy

- X-Scope-OrgID header for tenant isolation in Loki and Tempo (self-hosted) [20]
- Grafana Cloud: LBAC with Prometheus label selectors [20]

---

## Comparison

| Dimension | Perses | Grafana OSS | Grafana Enterprise/Cloud |
|-----------|--------|------------|-------------------------|
| Isolation model | Project-based | Organization-based | Organization + LBAC/multi-stack |
| RBAC availability | Built-in (all editions) | 5 basic roles only | Full RBAC (fixed + custom roles) |
| Custom roles | N/A (4 role types, additive) | No | Yes (action + scope pairs) |
| Datasource isolation | PersesDatasource (project) vs PersesGlobalDatasource (cluster) | Per-organization | Per-organization + LBAC |
| K8s RBAC integration | Native (ClusterRoles, TokenReview) | Via proxy | Via proxy |
| Auth providers | Native, OIDC, OAuth, K8s | Native, LDAP, OAuth | + SAML, SCIM |
| Deny rules | No (purely additive) | No | No |

## Gaps and Limitations

- Perses RBAC is simpler than Grafana Enterprise — no custom role definitions beyond the 4 role types, no LBAC equivalent.
- Grafana Enterprise RBAC (custom roles, LBAC) is behind a commercial paywall.
- Grafana OSS is limited to 5 basic roles — less granular than Perses's project-scoped roles.
- Perses has no "team" concept equivalent to Grafana teams.
- Grafana folder named "General" cannot have RBAC managed — a known limitation [13].
- No published data on Perses concurrent user handling or RBAC performance at scale.
