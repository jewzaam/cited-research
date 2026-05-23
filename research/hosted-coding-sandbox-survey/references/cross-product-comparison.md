# Cross-product comparison

Side-by-side on the four recurring problems. Cells summarise design choice; numbers in brackets cite [citations.md](../citations.md).

| Product | Session persistence | Browser surface | Isolation boundary | Credential injection |
|---|---|---|---|---|
| **GitHub Codespaces** | Per-codespace VM + dev container. `/workspaces` persists across stop/start AND rebuild; rest of FS persists across stop/start only. Idle 30 min default, 5–240 min range, "activity" includes terminal I/O. Pool-based prebuilds for fast cold-create. [1][2][5][7][8] | Hosted VS Code over TLS tunnel; auto-port-forward on terminal `http://localhost:PORT` printing; wildcard subdomain `*.app.github.dev`; private (default) / org / public visibility. [3][6] | Per-codespace VM ("Two codespaces are never co-located on the same VM"). Per-codespace isolated virtual network with firewalls blocking inter-codespace traffic. [3] | Fresh `GITHUB_TOKEN` minted on every create/restart, scoped to user's repo perms. Secrets exported as env vars; 100/scope, 48 KB each; three-tier user/repo/org hierarchy with repo overriding org. [3][4] |
| **Gitpod Classic** (sunsetting) | K8s pod + PV. Idle 30 min default; max lifetime 8 h free / 36 h paid. Soft-delete 14 d / full-delete +21 d / record-delete +365 d after last active. [9] | Workspace URL `<id>.ws-<region>.gitpod.io`; port subdomain `<port>-<id>.ws-<region>.gitpod.io`; private (default) / public; OpenVSCode-based browser editor. [11] | K8s pod-per-workspace + user-namespace UID/GID mapping; namespace per workspace; NetworkPolicies restrict east-west. Cross-workspace escape disclosed historically (drove Flex pivot). [12] | Env vars scoped Repository / User (repo precedence). Org access boundary. `GITPOD_IMAGE_AUTH` default-not-mounted. OAuth integrations for GH/GL/BB. [10] |
| **Gitpod Flex / Ona** (current) | Runners in customer cloud (AWS first); environments = EC2-class VMs, not pods. Persistence detail mid-migration in docs. [12][13] | Same OpenVSCode-based editor (continuity claim from discovery; not re-verified at primary source). Routing through customer runner. | Per-environment VM; deployment is single-tenant in customer cloud account. "control plane heavily inspired by Kubernetes" without being k8s. [12][13] | Secrets distinct from env vars; AES256-GCM at rest (per discovery / changelog); env or file delivery; "secret updates apply to new environments only". Source-control "All source control interactions occur only through the runner on your infrastructure". |
| **Coder** | Resources classified persistent vs ephemeral (ephemeral destroyed on stop). On K8s: pod (ephemeral) + PVC at `$HOME` (persistent). Prebuilt pool via `coder_workspace_preset.prebuilds {instances, expiration_policy.ttl}`; on claim, ownership transfers and `terraform apply` re-runs. Five states inc. distinct Unhealthy. [14][15][19] | code-server primary (VS Code Web/JupyterLab/RStudio/Airflow/File Browser also supported). JetBrains via Gateway (desktop, SSH-over-tunnel). Apps exposed via `coder_app` Terraform resource through agent. [21] | Pod-per-workspace; reference design = namespace per developer with ServiceAccount + RoleBinding scoped to namespace; "full kubectl access" within boundary. Tailscale WireGuard agent-to-client tunnels with NAT-traversal + DERP relay fallback (embedded DERP in coderd by default). [16][20] | SSH keys in-memory only, never written to workspace disk. Git HTTPS via `GIT_ASKPASS` per workspace. External auth env-var matrix `CODER_EXTERNAL_AUTH_<N>_ID/TYPE/CLIENT_ID/CLIENT_SECRET`. Vault integration supported. Template parameters are NOT secrets. [17][18] |
| **Replit** | Snapshot Engine: manifest-based block storage (NBD-backed virtual block devices on GCS, 16 MiB chunks). Fork = manifest copy (constant-time). Always On removed Jan 1, 2024; Deployments only. Autoscale scales to zero on idle. [22][23][26][28] | Server-rendered IDE w/ ~3000 LOC plugin core (discovery). Preview/Webview pane w/ Eruda devtools. | Today: "Linux containers hardened with seccomp-bpf"; microVM rollout in progress (hypervisor not named). Production: per-customer GCP Project (even free tier), apps on Cloud Run + Cloud Armor + WAF. [22] | Secrets AES-256 at rest, env-var injection at runtime; remix shows names not values to non-owners. Repl Identity = PASETO token in `REPL_IDENTITY` env var, verifiable with ED25519 public keys in `REPL_PUBKEYS`. [24][25] |
| **StackBlitz / WebContainers** | In-memory virtual filesystem; runtime persists nothing; embedder uses IndexedDB or Git for persistence. One `WebContainer.boot()` per page; `teardown()` required to re-boot. [31][32] | Browser tab IS the workspace — no IDE-over-tunnel; StackBlitz Codeflow IDE in the same page. URL-as-entry-point pattern: `pr.new` swap for `github.com`. [34] | Browser tab — user-agent process isolation. Requires `Cross-Origin-Embedder-Policy: require-corp` + `Cross-Origin-Opener-Policy: same-origin` on hosting page; SharedArrayBuffer dependency makes COI non-bypassable. [30] | No first-class secrets primitive. Env vars passed per-spawned-process via `spawn(opts.env)`. Secrets traverse the browser. [31] |
| **Daytona** (current AI-sandbox product) | States Creating / Started / Stopped / Archived (Paused experimental). Ephemeral mode auto-deletes on stop AND revokes session credentials. Snapshots from Docker/OCI images. Volumes S3-backed with per-sandbox subpath isolation. [36][37][41][42] | Wildcard subdomain proxy: standard `https://{port}-{sandboxId}.{proxyDomain}` with `x-daytona-preview-token` header; signed `https://{port}-{token}.{proxyDomain}` with TTL 1–86400 s. `public=true` bypasses auth. Web terminal = preview port 22222 (discovery). SSH Gateway on TCP 2222 bypasses Caddy. Port range 3000–9999. [38][39] | Sysbox runtime = VM-level isolation w/o hypervisor; user-NS maps in-container root to unprivileged on host; exclusive UID/GID per sandbox. `INTER_SANDBOX_NETWORK_ENABLED=false` default. Organization as tenancy boundary with assignment-based RBAC. [37][38][40] | Auth via Auth0/OIDC at platform level (Auth0 attribution from discovery, uncited); OSS bundles Dex. Sandbox env vars at creation (k/v or `.env`). Registry creds via short-lived federated tokens (ECR cross-account IAM-role assumption: "Daytona assumes it on every pull to fetch a short-lived ECR token"). API keys per-user/per-org with granular scopes. [38][42] |
| **Eclipse Che / Dev Spaces** | DevWorkspace CR per workspace, reconciled by DevWorkspace Operator. PVC strategy: per-user (default), per-workspace, ephemeral. Idle defaults `secondsOfInactivityBeforeIdling` / `secondsOfRunBeforeIdling` not on the running-at-scale page (unverified at primary source). [43][46][50] | Single Traefik gateway (`che-gateway` Deployment) does Routing + OAuth2-Proxy OIDC + kube-rbac-proxy RBAC enforcement. code-server / VS Code Web for browser editor. [45] | Namespace per user (auto-provisioned, template-named). Bidirectional sync from `eclipse-che` namespace → user namespaces, with revert-on-tamper. Three NetworkPolicies close K8s east-west default-open. RBAC-driven workspace access via kube-rbac-proxy. [44][45][48] | Git PAT via dashboard or manual K8s Secret with specific labels/annotations. Generic secret/configmap automount via labels `controller.devfile.io/mount-to-devworkspace=true` + `watch-secret=true` and annotations `mount-as: file\|subpath\|env`. OIDC (Keycloak on plain K8s). [47][49] |
| **Devpod** (Loft Labs) | Container providers: kill PID 1 on inactivity. Machine providers: in-VM daemon shuts down/deletes. State preserved on stop; restart resumes. K8s provider uses PV sized by `persistentVolumeSize` (discovery). [54] | Browser IDE = OpenVSCode Server installed in workspace, reached via local-client localhost tunnel — no public URL. JetBrains via Gateway. SSH via auto-modified `~/.ssh/config` entry `WORKSPACE_NAME.devpod`. [55] | OSS: no native multi-tenancy — each developer's local client uses own kubeconfig/IAM; isolation is provider-level (K8s RBAC + namespace). K8s tunnel via control plane, no node-side agent required. Pro adds central control plane. [52][57] | Forward-from-client, never broker centrally. Git HTTPS via credential helper; SSH via agent-forwarding; Docker via credential helper; GPG opt-in via SSH tunnel. Opt-outs `SSH_INJECT_GIT_CREDENTIALS=false` / `SSH_INJECT_DOCKER_CREDENTIALS=false`. Provider-level toggles `injectGitCredentials`/`injectDockerCredentials` in `provider.yaml`. [53][56] |

## Pattern groupings — design-axis observations

**Workspace abstraction:**
- Custom Resource: Eclipse Che (DevWorkspace), arguably Coder (Terraform-defined).
- API object: Codespaces, Daytona, Gitpod, Replit.
- Local CLI object: Devpod.
- Browser-tab object: StackBlitz.

**Tenancy unit:**
- VM-per-tenant: Codespaces, Gitpod Flex, Replit (post-microVM).
- Pod + UID-NS + NetworkPolicy: Gitpod Classic, Coder, Eclipse Che.
- Sysbox container: Daytona.
- GCP-project-per-tenant: Replit (production deployments).
- User-agent process: StackBlitz.
- Whatever the underlying provider gives: Devpod (OSS).

**Persistence layer:**
- Pod + PVC: Gitpod Classic, Coder (K8s), Eclipse Che.
- VM + EBS-class disk: Codespaces, Gitpod Flex.
- Manifest-based COW block storage: Replit (Snapshot Engine).
- Container + S3-subpath-isolated volume: Daytona.
- In-memory only: StackBlitz.
- Provider-dependent: Devpod.

**Browser-access surface:**
- Hosted IDE-in-browser + per-port wildcard subdomain proxy: Codespaces, Gitpod, Coder, Eclipse Che, Daytona.
- IDE-and-runtime same browser tab: StackBlitz.
- IDE-in-browser via local-client tunnel only: Devpod.
- IDE bespoke (not VS Code derivative): Replit.

**Credential injection canonical pattern:**
- Env-var at runtime: Codespaces, Replit, Daytona, Gitpod Classic.
- Helper-on-demand (never persist on disk): Coder SSH keys, Devpod git/docker/GPG helpers.
- Secret-mount via labels/annotations: Eclipse Che.
- File-or-env via secret primitive: Gitpod Flex.
- No first-class primitive (spawn-time env only): StackBlitz.

**Auth at session boundary:**
- OIDC (OAuth2-Proxy or similar): Eclipse Che, Daytona.
- Platform-owned token (GITHUB_TOKEN / coder agent token / REPL_IDENTITY): Codespaces, Coder, Replit.
- User's local creds passed through: Devpod.
- Per-port token (header or signed-URL): Daytona.
- Org membership: Gitpod private ports.
