# Citations

All sources visited in-session. Tier 1 = peer-reviewed/government; Tier 2 = vendor primary docs / established reference; Tier 3 = industry blog / engineering post / conference talk / well-known practitioner; Tier 4 = forum / community wiki / personal blog.

Publication dates noted where visible; dev sandbox tooling is fast-moving so currency matters.

---

## GitHub Codespaces

[1] **GitHub Docs — Codespaces deep dive.** Tier 2. <https://docs.github.com/en/codespaces/about-codespaces/deep-dive>. Architecture: per-codespace VM + Docker container; shallow clone into `/workspaces` mounted into container; `/workspaces` persists across stop/start AND container rebuild; outside `/workspaces` persists across stop/start but not rebuild.

[2] **GitHub Docs — Understanding the codespace lifecycle.** Tier 2. <https://docs.github.com/en/codespaces/about-codespaces/understanding-the-codespace-lifecycle>. Default 30-min idle timeout; default 30-day retention of stopped codespaces; saved changes preserved across stop/start.

[3] **GitHub Docs — Security in GitHub Codespaces.** Tier 2. <https://docs.github.com/en/codespaces/reference/security-in-github-codespaces>. "Each codespace is hosted on its own newly-built virtual machine (VM). Two codespaces are never co-located on the same VM." Isolated virtual network; firewalls block inter-codespace traffic; GITHUB_TOKEN scoped to repo perms with automatic expiry; new token on every create/restart; only creator can connect.

[4] **GitHub Docs — Managing account-specific secrets for Codespaces.** Tier 2. <https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces>. Secrets exported as env vars; 100 secrets max per scope; 48 KB per secret; repo-level precedence over org-level.

[5] **GitHub Docs — About Codespaces prebuilds.** Tier 2. <https://docs.github.com/en/codespaces/prebuilding-your-codespaces/about-github-codespaces-prebuilds>. Two-phase: prebuild workflow runs `onCreateCommand`+`updateContentCommand` then snapshots; user-create downloads snapshot onto fresh VM and runs `postCreateCommand`; concurrency limit of one workflow run per config.

[6] **GitHub Docs — Forwarding ports.** Tier 2. <https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace>. Auto-detection on terminal `http://localhost:PORT` output; subdomain format `https://CODESPACENAME-PORT.app.github.dev`; HTTP default; visibility Private/Org/Public.

[7] **GitHub Docs — Setting timeout period for Codespaces.** Tier 2. <https://docs.github.com/en/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces>. Default 30 min; range 5–240 min; activity = typing/mouse OR terminal I/O (input or output); org policy caps user setting.

[8] **GitHub Blog — How GitHub's engineering team moved Codespaces to Codespaces.** Tier 3. <https://github.blog/engineering/infrastructure/githubs-engineering-team-moved-codespaces/>. Published Aug 11, 2021 (updated Dec 19, 2022). GitHub.com repo "almost 13 GB on disk"; cloning takes 20 min; cold create progressed from 45 min → 5 min → 10 sec with prebuilds; "pools of codespaces, fully cloned and bootstrapped, waiting to be connected".

---

## Gitpod (Classic + Flex / Ona)

[9] **Ona / Gitpod Docs — Workspace lifecycle (Classic).** Tier 2. <https://ona.com/docs/configure/workspaces/workspace-lifecycle>. States: Starting / Running / Stopping / Stopped. "workspaces stop following 30 minutes without user input". Max lifetime: 8 h free / 36 h paid. Soft delete 14 d after last active (28 d w/ uncommitted changes); full delete 21 d after soft; DB record deleted 365 d after full. `gp timeout set` extends inactivity timeout.

[10] **Ona / Gitpod Docs — Environment variables (Classic).** Tier 2. <https://ona.com/docs/configure/repositories/environment-variables>. Repository-level and User-level scopes; "Repository-specific Environment Variables will take precedence over User-specific Environment Variables." Org access boundary; `GITPOD_IMAGE_AUTH` "not mounted into workspaces for security reasons" by default.

[11] **Ona / Gitpod Docs — Ports (Classic).** Tier 2. <https://ona.com/docs/configure/workspaces/ports>. Subdomain pattern `3000-yourworkspace.ws-eu45.gitpod.io`. Visibility: `private` (default) / `public`. Authenticated URL for private; needs `credentials: "include"` + `Access-Control-Allow-Credentials` for cross-origin.

[12] **Ona — We are leaving Kubernetes.** Tier 3. <https://ona.com/stories/we-are-leaving-kubernetes>. Published Oct 31, 2024. "Kubernetes is built to run well controlled application workloads, not unruly development environments." Tried Firecracker, Cloud Hypervisor, QEMU (mid-2023); Firecracker had "Lack of GPU support" and "No virtiofs support at the time of our experiments" (two separate bullets); Cloud Hypervisor had "slower snapshot and restore processes due to the lack of userfaultfd support". Replaced k8s with Gitpod Flex — "control plane heavily inspired by Kubernetes" plus dev-env-specific abstractions.

[13] **InfoQ — Gitpod Flex: Cloud Development After Kubernetes.** Tier 3. <https://www.infoq.com/news/2024/12/gitpod-kubernetes-flex/>. Published Dec 29, 2024. Independent confirmation that Flex "carries over important aspects of Kubernetes, such as control theory and declarative APIs" while simplifying the architecture; specific substrate not disclosed. (Verbatim phrase "inspired by k8s" comes from [12], not InfoQ.)

---

## Coder

[14] **Coder Docs — Architecture.** Tier 2. <https://coder.com/docs/admin/infrastructure/architecture>. `coderd` "a thin API that connects workspaces, provisioners and users" — sole Postgres talker. `provisionerd` runs Terraform (sole provider). Resources classified computational vs peripheral, persistent vs ephemeral (ephemeral destroyed on workspace stop). Agent runs in workspace, provides SSH/port-forward/liveness/startup scripts.

[15] **Coder Docs — Workspace lifecycle.** Tier 2. <https://coder.com/docs/user-guides/workspace-lifecycle>. States: Running, Stopped, Deleted, Failed, Unhealthy. "Stopped: Ephemeral resources destroyed, persistent resources idle". Stop triggered manually or by template-update/inactivity scheduling; Unhealthy = "Resources have been provisioned, but the agent can't facilitate connections".

[16] **Coder Docs — Networking.** Tier 2. <https://coder.com/docs/admin/networking>. "Tailscale's open source backs our websocket/HTTPS networking logic." WireGuard tunnels over ephemeral UDP; STUN-based NAT traversal; DERP relay fallback. Embedded DERP relay by default; can use Tailscale's public DERP via `--derp-config-url` or custom via `--derp-config-path`.

[17] **Coder Docs — External authentication.** Tier 2. <https://coder.com/docs/admin/external-auth>. OAuth2.0 to GitHub/GitLab/BitBucket/Azure DevOps. Env vars: `CODER_EXTERNAL_AUTH_<N>_ID|TYPE|CLIENT_ID|CLIENT_SECRET`. Callback URL: `https://example.com/external-auth/{ID}/callback`. Git HTTPS auth via `GIT_ASKPASS` mechanism configured per workspace.

[18] **Coder Docs — Secrets.** Tier 2. <https://coder.com/docs/admin/security/secrets>. "SSH keys are never stored in Coder workspaces, and are fetched only when SSH is invoked. The keys are held in-memory and never written to disk." Uses `$GIT_SSH_COMMAND` for git SSH. "Coder is open-minded about how you get your secrets into your workspaces." Vault integration supported. Template parameters NOT for secrets (workspace-visible).

[19] **Coder Docs — Prebuilt workspaces.** Tier 2. <https://coder.com/docs/admin/templates/extending-templates/prebuilt-workspaces>. Pool model; `prebuilds {}` block inside `coder_workspace_preset` with `instances` and `expiration_policy { ttl }`. On claim: ownership transferred from `prebuilds` user to requesting user, name changed, `terraform apply` re-run with new ownership — "transparent to the developer".

[20] **Coder Blog — Kubernetes namespaces as dev environments.** Tier 3. <https://coder.com/blog/kubernetes-namespaces-as-dev-environments>. Published Mar 6, 2023. Per-developer namespace pattern + ServiceAccount + RoleBinding scoped to namespace; full `kubectl` within boundary.

[21] **Coder Docs — Web IDEs.** Tier 2. <https://coder.com/docs/ides/web-ides>. Primary: code-server ("our supported method of running VS Code in the web browser"). Others: VS Code Web, JupyterLab, RStudio, Airflow, File Browser.

---

## Replit

[22] **Replit Blog — Defense in Depth.** Tier 3. <https://replit.com/blog/defense-in-depth-how-replit-secures-every-layer-of-the-vibe-coding-stack>. Published Apr 20, 2026 (updated Apr 21). "Linux containers hardened with seccomp-bpf and several additional layers of system hardening"; "currently rolling out a replacement of our entire container-based infrastructure with microVMs"; "every single customer gets their own GCP Project, even free-tier users"; apps on Cloud Run + Cloud Armor + WAF.

[23] **Replit Blog — Inside Replit's Snapshot Engine.** Tier 3. <https://replit.com/blog/inside-replits-snapshot-engine>. Published Dec 17, 2025 (updated Dec 18). "checkpoint copies the current manifest under a new name, and restore replaces the current manifest with a different version." "copying a disk is a matter of copying the manifest, making it both cheap and constant-time." Virtual block devices via NBD backed by Google Cloud Storage; 16 MiB immutable chunks.

[24] **Replit Blog — Repl Identity (Zero-Click Auth).** Tier 3. <https://replit.com/blog/repl-identity>. Published Aug 2, 2022 (updated Oct 5, 2023). `REPL_IDENTITY` env var is "a PASETO token, signed by our infrastructure". Verification via `REPL_PUBKEYS` ED25519 public keys "injected into each repl". Go package `go-replidentity`.

[25] **Replit Docs — Secrets.** Tier 2. <https://docs.replit.com/replit-workspace/workspace-features/secrets>. "AES-256 encryption at rest and TLS encryption in transit"; runtime env-var access; App Secrets vs Account Secrets; on remix, non-owners see names only, not values; secrets unavailable in Static Deployments.

[26] **Replit Docs — Autoscale Deployments.** Tier 2. <https://docs.replit.com/cloud-services/deployments/autoscale-deployments>. Scale-to-zero: "When your app is idle, it reduces the number to as low as zero to save you money." Configurable max-instance cap. (Exact idle threshold + cold-start times not stated on this page.)

[27] **Replit Blog — Nix.** Tier 3. <https://replit.com/blog/nix>. Published May 24, 2021 (updated Oct 6, 2023). `replit.nix` config; "over 30,000 OS packages instantly"; "a huge 1 terabyte shared disk image we mount into every repl right under /nix"; Nix's content-addressable store enables conflict-free shared image.

[28] **Replit Blog — Changes to Hosting on Replit.** Tier 3. <https://replit.com/blog/hosting-changes>. Published Sep 28, 2023 (updated Nov 29, 2023). "Always On will be fully removed from the product on January 1st, 2024." "After January 1st, Deployments will be the only way to host applications on Replit."

---

## StackBlitz / WebContainers

[29] **WebContainers Docs — Introduction.** Tier 2. <https://webcontainers.io/guides/introduction>. "WebContainers are a browser-based runtime for executing Node.js applications and operating system commands, entirely inside your browser tab." Isolation: "everything is contained in a browser tab". "spinning up the entire dev environment in milliseconds".

[30] **WebContainers Docs — Configuring headers.** Tier 2. <https://webcontainers.io/guides/configuring-headers>. Requires `Cross-Origin-Embedder-Policy: require-corp` and `Cross-Origin-Opener-Policy: same-origin`. "WebContainer requires SharedArrayBuffer, which, in turn, requires your website to be cross-origin isolated."

[31] **WebContainers Docs — API reference.** Tier 2. <https://webcontainers.io/api>. "Only a single instance of WebContainer can be booted concurrently". `spawn()` takes optional `env: Record<string, string|number|boolean>`. `fs` modeled after `fs.promises`.

[32] **WebContainers Docs — Working with the file system.** Tier 2. <https://webcontainers.io/guides/working-with-the-file-system>. "WebContainer API gives you access to work with a virtual file system, right in memory." Mount via nested-object format or `@webcontainer/snapshot` binary.

[33] **StackBlitz Blog — Introducing WebContainers.** Tier 3. <https://blog.stackblitz.com/posts/introducing-webcontainers/>. Published May 20, 2021. "a WebAssembly-based operating system powerful enough to run Node.js"; "a virtualized TCP network stack that's mapped to your browser's ServiceWorker API"; "100% of code execution occurs in the browser security sandbox".

[34] **StackBlitz Developer Docs — Codeflow IDE.** Tier 2. <https://developer.stackblitz.com/codeflow/working-in-codeflow-ide>. URL pattern: "swap 'github.com' with 'pr.new' in the repository URL." Codeflow IDE handles both PR creation and PR review (auto-spins in 'PR Review mode' when opened on a PR URL).

---

## Daytona

[35] **Daytona Docs — Architecture.** Tier 2. <https://www.daytona.io/docs/en/architecture/>. Three planes: Interface (SDKs, CLI, Dashboard, MCP, SSH), Control (API, Proxy, Snapshot builder, Sandbox manager), Compute (runners + daemon + snapshot store + volumes). Runners are pull-based: "Each runner polls the control plane API for jobs".

[36] **Daytona Docs — Sandboxes.** Tier 2. <https://www.daytona.io/docs/en/sandboxes/>. States: Creating, Started, Stopped, Archived (Paused experimental — "stop behaves as pause and preserves memory state"). Ephemeral: "Ephemeral sandboxes are automatically deleted once they are stopped." Triggered by setting `ephemeral=True` or `autoDeleteInterval: 0`. "Each sandbox runs in isolation, giving it a dedicated kernel, filesystem, network stack, and allocated vCPU, RAM, and disk."

[37] **Daytona Docs — Security Exhibit.** Tier 2. <https://www.daytona.io/docs/en/security-exhibit/>. "Daytona uses Sysbox as its container runtime to provide VM-level isolation without hardware virtualization overhead." Linux user-namespaces map root inside to unprivileged on host; "exclusive user-ID and group-ID mappings". Ephemeral mode revokes "any session-scoped credentials or tokens" on termination.

[38] **Daytona Docs — OSS deployment.** Tier 2. <https://www.daytona.io/docs/en/oss-deployment/>. Docker Compose stack: API, Proxy, Runner, SSH Gateway (port 2222 TCP, bypasses Caddy), PostgreSQL, Redis, Dex (OIDC), Registry, MinIO, Jaeger, MailDev, PgAdmin. Caddy = HTTPS terminator. DNS: base + proxy + wildcard `*.proxy.daytona.example.com`. `INTER_SANDBOX_NETWORK_ENABLED` default = inter-container communication disabled.

[39] **Daytona Docs — Preview and authentication.** Tier 2. <https://www.daytona.io/docs/en/preview-and-authentication/>. Standard URL `https://{port}-{sandboxId}.{proxyDomain}` with header `x-daytona-preview-token`. Signed URL `https://{port}-{token}.{proxyDomain}` with TTL 1 s – 86 400 s (default 60 s, recommended ≥ 3600). `public=true` bypasses auth. Port range 3000–9999.

[40] **Daytona Docs — Organizations.** Tier 2. <https://www.daytona.io/docs/en/organizations/>. "Each organization has its own sandboxes, API keys, and resource quotas." Roles Owner / Member; Member permissions via Assignments (Viewer/Developer/Sandboxes-Admin/Snapshots-Admin/Registries-Admin/Volumes-Admin/Super Admin/Auditor/Infrastructure Admin).

[41] **Daytona Docs — Volumes.** Tier 2. <https://www.daytona.io/docs/en/volumes/>. "Volume data is stored in an S3-compatible object store." Subpath isolation: "Each sandbox sees only files under its assigned subpath at mount_path and cannot read or write sibling subpaths within the same volume." Single volume mountable to multiple sandboxes; FUSE-backed.

[42] **Daytona Docs — Snapshots.** Tier 2. <https://www.daytona.io/docs/en/snapshots/>. From Docker/OCI images, public or private (Docker Hub / GAR / GHCR / ECR). ECR: "cross-account IAM role assumption"; "Daytona assumes it on every pull to fetch a short-lived ECR token. No long-lived AWS credentials are shared." Default entrypoint `sleep infinity` if none.

---

## Eclipse Che

[43] **Eclipse Che Docs — Architecture overview.** Tier 2. <https://eclipse.dev/che/docs/stable/administration-guide/architecture-overview/>. Three groups: Che server, DevWorkspace operator (creates K8s objects for user workspaces), user workspaces (container-based dev env, IDE included). DevWorkspace CRs = central abstraction. User dashboard = main control surface.

[44] **Eclipse Che Docs — Configuring a user namespace.** Tier 2. <https://eclipse.dev/che/docs/stable/administration-guide/configuring-a-user-namespace/>. Bidirectional sync: changes in `eclipse-che` namespace propagate to all user namespaces; changes in user namespace are reverted. Sync source labeled `app.kubernetes.io/part-of: che.eclipse.org` + `app.kubernetes.io/component: workspaces-config`. Annotation `che.eclipse.org/sync-retain-on-delete: "true"` preserves on source deletion.

[45] **Eclipse Che Docs — Gateway.** Tier 2. <https://eclipse.dev/che/docs/stable/administration-guide/gateway/>. Three responsibilities: routing (Traefik), authentication (OAuth2 Proxy + OIDC), access control (kube-rbac-proxy enforces K8s RBAC). Managed by Che operator as `che-gateway` Deployment.

[46] **Eclipse Che Docs — Storage strategy.** Tier 2. <https://eclipse.dev/che/docs/stable/administration-guide/configuring-the-storage-strategy/>. `pvcStrategy` field on `CheCluster` CR. Options: per-user (default — "single PVC for all workspaces"), per-workspace ("Each workspace is given its own PVC"), ephemeral (lost on stop). Per-workspace override via devfile or URL.

[47] **Eclipse Che Docs — Mounting secrets.** Tier 2. <https://eclipse.dev/che/docs/stable/end-user-guide/mounting-secrets/>. Required labels: `controller.devfile.io/mount-to-devworkspace: 'true'` + `controller.devfile.io/watch-secret: 'true'`. Annotations: `mount-path` (default `/etc/secret/<Secret_name>`), `mount-as: file|subpath|env` (default `file`).

[48] **Eclipse Che Docs — NetworkPolicies.** Tier 2. <https://eclipse.dev/che/docs/stable/administration-guide/configuring-network-policies/>. "By default, all Pods in a Kubernetes cluster can communicate with each other even if they are in different namespaces". Three policies: `allow-from-eclipse-che` (Che → user namespace), `allow-from-openshift-apiserver` (apiserver → devworkspace-webhook-server), `allow-from-workspaces-namespaces` (user → che-gateway).

[49] **Eclipse Che Docs — Using a git provider access token.** Tier 2. <https://eclipse.dev/che/docs/stable/end-user-guide/using-a-git-provider-access-token/>. Dashboard config at `/dashboard/#/user-preferences?tab=personal-access-tokens`. Manual Secret: labels `app.kubernetes.io/component: scm-personal-access-token` + `app.kubernetes.io/part-of: che.eclipse.org`; annotations `che.eclipse.org/che-userid`, `scm-personal-access-token-name`, `scm-url`, `scm-organization`; `stringData: token: <Content>`.

[50] **Eclipse Che Docs — Running at scale.** Tier 2 (partial). <https://eclipse.dev/che/docs/stable/administration-guide/running-at-scale/>. Fetched but page focuses on resources/etcd/autoscaling/multi-cluster — idle-timeout defaults (`secondsOfInactivityBeforeIdling`, `secondsOfRunBeforeIdling`) NOT on this page. Defaults unverified at primary source level; discovery agent cited them from secondary sources.

---

## Devpod (Loft Labs)

[51] **Devpod Docs — How it works overview.** Tier 2. <https://devpod.sh/docs/how-it-works/overview>. Client-agent architecture. Tunnel = vendor-specific (kubectl for K8s, instance connect for AWS, SSH for VMs). "Devpod establishes a connection to the workspace using a vendor specific API." Agent "starts a SSH server using the STDIO of the secure tunnel".

[52] **Devpod Docs — Deploy K8s.** Tier 2. <https://devpod.sh/docs/how-it-works/deploy-k8s>. "the secure tunnel is set up using the kubernetes control plane (e.g. kubectl ...) so an agent is not necessary to be run on the kubernetes node".

[53] **Devpod Docs — Credentials.** Tier 2. <https://devpod.sh/docs/developing-in-workspaces/credentials>. Git HTTPS via "git credentials helper". SSH via "agent-forwarding that will be configured automatically on the ssh configuration for the workspace." Docker via "docker credentials helper". GPG via SSH tunnel (opt-in: `GPG_AGENT_FORWARDING=true`). Opt-outs: `SSH_INJECT_GIT_CREDENTIALS=false`, `SSH_INJECT_DOCKER_CREDENTIALS=false`.

[54] **Devpod Docs — Inactivity timeout.** Tier 2. <https://devpod.sh/docs/developing-in-workspaces/inactivity-timeout>. Container providers (docker/k8s/ssh): "DevPod can automatically kill the container its running in by terminating the process with pid 1." Machine providers: "DevPod will install itself as a Daemon into the remote VM and track the activity from there." Machine daemon may "automatically shutdown the machine or even delete it, based on what's cheaper for the given cloud provider."

[55] **Devpod Docs — Connect to a workspace.** Tier 2. <https://devpod.sh/docs/developing-in-workspaces/connect-to-a-workspace>. Browser IDE = OpenVSCode Server (`--ide openvscode`). JetBrains via Gateway. SSH via auto-modified `~/.ssh/config` entry `WORKSPACE_NAME.devpod`. `devpod ssh my-workspace` as CLI fallback.

[56] **Devpod Docs — Agent (provider development).** Tier 2. <https://devpod.sh/docs/developing-providers/agent>. Agent injection: "inject itself into the environment to handle the following tasks: deploying the container, forward credentials, ssh server, auto-shutdown after a period of inactivity." Provider-level options `injectGitCredentials`, `injectDockerCredentials` configurable in `provider.yaml` `agent` section.

[57] **Devpod Docs — What is Devpod.** Tier 2. <https://devpod.sh/docs/what-is-devpod>. "No need to install a server backend, DevPod runs solely on your computer." Contrast w/ Codespaces/JetBrains Spaces/Google Cloud Workstations: cost ("usually around 5-10 times cheaper"), cloud-provider flexibility, local execution option.

---

## Cross-cutting / source-quality notes

- Gitpod docs are mid-migration from `gitpod.io` to `ona.com` (post-rebrand). Many old Flex doc URLs return 404; Classic-era URLs redirect to `ona.com/docs/...`. Several Flex-specific pages (introduction, secrets, runners/aws) currently 404 — Flex architecture detail in this research draws on Tier-3 independent coverage (InfoQ, [12]) and the leaving-k8s story.
- Replit blog URLs `blog.replit.com/...` redirect to `replit.com/blog/...`; the latter is canonical.
- Daytona pivoted Feb 2025 from devcontainer CDE to AI agent sandbox runtime; pre-pivot devcontainer/git-OAuth flows are not prominent in current docs and are excluded from this research.
- Eclipse Che `running-at-scale` page did not contain expected idle-timeout defaults; those defaults remain unverified at primary-source level.
- All vendor docs are Tier 2 by classification but should be read as marketing-influenced where they describe security guarantees (per user instruction to expand Tier-3/-4 third-party coverage, blog posts from independent practitioners were sought where available).
