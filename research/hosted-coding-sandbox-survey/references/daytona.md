# Daytona

Dimension: how Daytona solves the four recurring problems. Scope: current AI-sandbox product (post-Feb-2025 pivot); the pre-pivot devcontainer CDE is out of scope. Sources in [citations.md](../citations.md).

## Architecture orientation

Three planes [35]:
- **Interface plane**: SDKs (Python/TypeScript/Ruby/Go/Java), CLI, Dashboard, MCP, SSH.
- **Control plane** ("the central coordination layer"): API, Proxy, Snapshot builder, Sandbox manager. NestJS REST API as the primary entry point.
- **Compute plane** ("the infrastructure layer where sandboxes run"): runners, sandbox daemon, snapshot store, volumes.

Runners are **pull-based**: "They poll the control plane API for jobs and execute sandbox operations" [35]. This is the most homelab-portable architectural fact in the survey — runners need no inbound exposure (no Ingress, no port-forward, no NodePort). For a k3s build behind NAT or with limited Ingress capacity, a polling-runner pattern lets compute nodes live anywhere reachable to the control plane.

## Session persistence

States: Creating / Started / Stopped / Archived [36], with Paused as an experimental state where "stop behaves as pause and preserves memory state" [36]. Archived is a cheaper-storage variant for cold sandboxes. Ephemeral mode is opt-in: "Ephemeral sandboxes are automatically deleted once they are stopped" [36]; setting `ephemeral=True` or `autoDeleteInterval: 0` triggers it [36]. Critically, ephemeral mode "any session-scoped credentials or tokens are revoked" on termination [37] — credential lifecycle is bound to sandbox lifecycle.

Snapshots are templates, not user-data backups: built from "Docker or OCI compatible images" [42] — public registries, local Dockerfiles via `--dockerfile`, or private registries (Docker Hub, GAR, GHCR, ECR). On boot, the snapshot becomes the base image; default entrypoint is `sleep infinity` if none is specified [42] — a clean way to keep the container alive for interactive use without requiring a contrived process tree.

Volumes are S3-backed and shareable: "Volume data is stored in an S3-compatible object store" [41]. The standout design is **subpath isolation**: "Each sandbox sees only files under its assigned subpath at mount_path and cannot read or write sibling subpaths within the same volume" [41]. One shared volume → per-sandbox subpaths → cross-tenant read denied. This is the cleanest "shared but isolated" storage pattern in the survey and translates directly to k8s (CSI volume subpath or projected volume with restricted ServiceAccount).

## Browser access UX

A wildcard subdomain preview proxy. Standard URL: `https://{port}-{sandboxId}.{daytonaProxyDomain}` with header `x-daytona-preview-token` [39]. Signed URL: `https://{port}-{token}.{daytonaProxyDomain}` with the token embedded in subdomain, configurable TTL 1–86,400 s (default 60 s, recommended ≥ 3600) [39]. `public=true` flag on a sandbox bypasses auth entirely [39]. Port range 3000–9999 [39]. "Standard and signed preview tokens are not interchangeable" [39] — distinct mechanisms for programmatic vs URL-share use.

Web terminal is exposed as just another preview on **port 22222** (discovery agent finding) — no special protocol, same proxy fabric. SSH Gateway is on port 2222 TCP and "bypasses Caddy — it is exposed directly through the firewall" [38].

The pattern worth importing for a homelab: one wildcard subdomain proxy serves all per-sandbox HTTP previews, with two auth modes (header for programmatic, subdomain-embedded token for share-as-URL) and a public escape hatch. The web terminal as a preview port is a particularly clean collapse — no separate browser-terminal protocol to maintain.

## Multi-tenant isolation

**Organization as tenancy boundary**. "Each organization has its own sandboxes, API keys, and resource quotas" [40]. Roles: Owner and Member; Members get permissions through Assignments — Viewer (required), Developer, Sandboxes Admin, Snapshots Admin, Registries Admin, Volumes Admin, Super Admin, Auditor, Infrastructure Admin [40]. Granular without enterprise IAM heaviness.

**Container-level isolation**: Sysbox runtime. "Daytona uses Sysbox as its container runtime to provide VM-level isolation without hardware virtualization overhead" [37]. "Sysbox enforces Linux user-namespaces on all sandboxes, ensuring that the root user inside a sandbox maps to a fully unprivileged user on the host" [37]. Each sandbox gets "exclusive user-ID and group-ID mappings, so a process escaping one sandbox has no permissions to access other sandboxes or host resources" [37].

**Network segmentation**: the runner env var `INTER_SANDBOX_NETWORK_ENABLED` default is "inter-container communication disabled" [38]. Plus "network segmentation between sandbox traffic, control plane, and management interfaces" and "configurable allow-lists and network block policies" [37].

For k3s specifically: Sysbox is usable via a `RuntimeClass`; the `INTER_SANDBOX_NETWORK_ENABLED=false` invariant maps to default-deny NetworkPolicies; per-sandbox UID mapping maps to PodSecurity restricted profile + runAsUser/Group.

## Credential injection

**User auth**: Auth0/OIDC at the platform layer (Auth0 attribution from discovery; not in primary-source pages fetched in this pass). OSS bundles **Dex** as a self-hostable OIDC provider [38], mounted at `/dex/*` on the main Caddy domain.

**Sandbox secrets**: env vars at creation, k/v pairs or `.env` file (discovery agent finding on `/docs/en/sandboxes/`; not separately highlighted on the security-exhibit page [37]). No first-class secrets store distinct from env vars surfaced in the docs pulled here.

**Registry creds (worth importing)**: short-lived federated tokens for image pulls. For ECR specifically: "cross-account IAM role assumption" — "Daytona assumes it on every pull to fetch a short-lived ECR token. No long-lived AWS credentials are shared" [42]. This pattern (broker on every pull, never persist the long-lived cred) generalises beyond ECR.

**API key model**: per-user, per-org, granular permission scopes, optional expiration, revocable, masked-after-creation (per discovery agent).

## Self-hosted topology (most homelab-relevant)

OSS deployment is **Docker Compose only**; Helm charts exist but aren't documented as the OSS path [38]. Stack: API + Proxy + Runner + SSH Gateway (port 2222 TCP) + Postgres + Redis + Dex + Registry + MinIO + Jaeger + MailDev + PgAdmin. Caddy terminates HTTPS with Let's Encrypt DNS-01 (Cloudflare/DO/Route53/Hetzner). DNS records needed: base + `proxy.<domain>` + wildcard `*.proxy.<domain>` [38].

Implication for the homelab: porting Daytona's OSS pattern to k3s means adapting the Compose topology, not just deploying their Helm charts. The Sysbox-runtime + wildcard-preview-proxy + pull-based-runner triple is what to mine, not the deployment artifacts.

## Gaps

- OSS runner-to-sandbox containerization story (does OSS install Sysbox automatically or is OSS plain-Docker isolation?) not confirmed in [37][38].
- Signing scheme for signed preview URLs (HMAC vs asymmetric, key rotation) not documented [39].
- Helm chart support level for OSS not stated [38].
- DinD resource-limit-disabled posture noted in discovery; security implications for nested-container homelab workloads not analysed here.
- Git provider OAuth presence in current product (vs the pre-pivot devcontainer flow) not verified.
