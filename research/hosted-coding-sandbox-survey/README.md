# Hosted coding sandbox products — design-inspiration survey

Eight hosted coding sandbox products surveyed for **design choices** on four recurring problems — session persistence, browser access UX, multi-tenant isolation, credential injection. The asker is building a self-hosted 3-node k3s homelab sandbox; this research mines each product's architecture for ideas worth importing. Adoption of any surveyed product is out of scope; no pricing data.

Products: GitHub Codespaces · Gitpod (Classic + Flex/Ona) · Coder · Replit · StackBlitz/WebContainers · Daytona · Eclipse Che · Devpod.

Last revised: 2026-05-23. Counter-perspective handling: skipped (design-pattern mining, not buy-vs-build).

## Headline summary table

| Product | Persistence | Browser surface | Isolation | Credential injection |
|---|---|---|---|---|
| **Codespaces** | `/workspaces` survives rebuild; rest survives stop only. 30-min idle default, 5–240 range. Prebuild pools. | Hosted VS Code; auto-forward on `localhost:PORT` terminal print; wildcard `*.app.github.dev`. | Per-codespace VM ("never co-located"); per-codespace isolated VNET; firewall blocks inter-codespace. | Fresh `GITHUB_TOKEN` per restart, scoped to repo perms. Secrets env-var; 100/scope, 48 KB. |
| **Gitpod Classic** | K8s pod + PV. 30 min idle. 8 h/36 h max lifetime. Soft/full/record-delete staircase 14/+21/+365 d. | OpenVSCode; `<port>-<id>.ws-<region>.gitpod.io`; private/public. | Pod + UID-NS + NetworkPolicies. (Historical escape drove Flex.) | Repo/User env-var scopes; repo precedence; `GITPOD_IMAGE_AUTH` default-not-mounted. |
| **Gitpod Flex** | Runners in customer cloud; per-env VMs (not pods). Single-tenant deployment. | Continuity OpenVSCode + routing via customer runner. | Per-environment VM in customer cloud account. | Secrets primitive distinct from env; AES256-GCM at rest; env-or-file delivery; updates only apply to new envs. |
| **Coder** | Resources classified persistent/ephemeral. K8s = pod + PVC at $HOME. Prebuild pool via `coder_workspace_preset.prebuilds`. | code-server primary; JetBrains via Gateway over SSH-over-tunnel. Apps via `coder_app`. | Pod-per-workspace + namespace-per-developer + ServiceAccount/RoleBinding. Tailscale WireGuard tunnels + embedded DERP fallback. | SSH keys in-memory only. `GIT_ASKPASS` per workspace. `CODER_EXTERNAL_AUTH_<N>_*` matrix. Vault supported. |
| **Replit** | Snapshot Engine = manifest-based COW block storage on NBD + GCS; fork = manifest copy. Always On removed 2024-01-01; Deployments only. | ~3000 LOC plugin-core IDE; Preview pane w/ Eruda. | Linux containers + seccomp-bpf today; microVM rollout in progress. Per-customer GCP Project (even free). Cloud Run + Cloud Armor + WAF. | Secrets AES-256 + TLS; env-var runtime. Repl Identity = PASETO + `REPL_PUBKEYS` ED25519 verifier injection. |
| **StackBlitz** | In-memory virtual FS; runtime persists nothing. Git or IndexedDB as truth. One boot per page. | Browser tab IS the workspace (WASM-Node + ServiceWorker TCP). `pr.new` URL swap onboarding. | Browser-tab process isolation. Non-bypassable COOP/COEP requirement on hosting page. | No first-class secrets. Env per `spawn()`. |
| **Daytona** | States Created/Started/Stopped/Archived (+exp Paused). Ephemeral mode revokes session creds on stop. Snapshots from OCI. Volumes S3-backed with subpath isolation. | Wildcard subdomain proxy: header `x-daytona-preview-token` OR signed-subdomain; TTL 1–86400 s; `public=true` bypass. Web terminal = preview port 22222 (discovery). | Sysbox runtime = VM-level isolation no hypervisor. User-NS + exclusive UID/GID. `INTER_SANDBOX_NETWORK_ENABLED=false` default. Org as tenancy unit + assignment RBAC. | Dex OIDC (Auth0 at platform layer per discovery, uncited). Env-var on create. ECR via cross-account IAM-role assumption — "Daytona assumes it on every pull to fetch a short-lived ECR token." |
| **Eclipse Che** | DevWorkspace CR + DWO. `pvcStrategy`: per-user (default) / per-workspace / ephemeral. (Idle defaults unverified at primary source.) | Single Traefik gateway = Routing + OAuth2-Proxy OIDC + kube-rbac-proxy. code-server. | Namespace per user (auto-provisioned). Bidirectional sync from `eclipse-che` w/ revert-on-tamper. Three explicit NetworkPolicies close K8s east-west. | Git PAT via K8s Secret w/ labels/annotations. Label-driven secret automount: `mount-to-devworkspace=true` + `watch-secret=true` + `mount-as: file\|subpath\|env`. |
| **Devpod** | Container providers: kill PID 1 on idle. Machine providers: in-VM shutdown daemon. K8s PV via `persistentVolumeSize`. | Browser IDE = OpenVSCode in workspace via **localhost tunnel from local client** — no public URL. JetBrains via Gateway. SSH via auto-modified `~/.ssh/config`. | OSS = no native multi-tenancy; isolation is whatever the underlying provider gives (kubeconfig RBAC + namespace for K8s). K8s tunnel via control plane, no node-side agent. | Forward-from-client — never broker centrally. Git/Docker via credential helpers. SSH agent-forwarding. GPG opt-in. `SSH_INJECT_GIT_CREDENTIALS=false` opt-out. |

## Quick decision framework

For each of the four recurring problems, the survey suggests one or two patterns worth defaulting to in a k3s homelab:

1. **Persistence** — start with persistent-vs-ephemeral classification at the template layer (Coder), PVC `per-user` default with override (Eclipse Che). Add snapshot-then-mutate for AI-agent safety later (Replit Snapshot Engine pattern).
2. **Browser UX** — wildcard subdomain preview proxy (convergent across the survey). Default header-token auth + opt-in signed-subdomain for sharing (Daytona). Web terminal as another preview port (Daytona).
3. **Isolation** — pod + UID-NS + three NetworkPolicies as baseline (Eclipse Che). Consider Sysbox RuntimeClass for VM-grade-without-hypervisor (Daytona). Defense-in-depth invariant: "Every layer assumes the one above it might fail" (Replit).
4. **Credentials** — in-memory-only SSH keys (Coder), `GIT_ASKPASS` for HTTPS (Coder), label-driven K8s secret automount (Eclipse Che), short-lived federated tokens for registries (Daytona). Avoid env-var-only as the only path.

## Full document layout

- [`hosted-coding-sandbox-survey.md`](hosted-coding-sandbox-survey.md) — full survey deliverable with headline observations and reflection.
- [`references/`](references/) — one file per product + cross-product comparison + synthesis.
- [`citations.md`](citations.md) — every source URL with publication date and quoted material (57 sources).
- [`audit/`](audit/) — citation audit and consistency review (next step).
