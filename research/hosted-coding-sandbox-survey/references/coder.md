# Coder (orchestration platform)

Dimension: how Coder solves the four recurring problems. Scope is the open-core orchestration platform (`coder/coder`), not the standalone `code-server` binary. Sources in [citations.md](../citations.md).

## Architecture orientation

Coder is unusual in this list: the workspace shape is defined entirely by **Terraform**. `coderd` is "a thin API that connects workspaces, provisioners and users" and is the sole Postgres talker [14]. `provisionerd` "the execution context for infrastructure modifying providers" runs Terraform; external provisioners exist for isolating builds and avoiding cloud-secret exposure [14]. Resources in a workspace template are classified along two axes: computational vs peripheral (computational = "resources that run the agent") and persistent vs ephemeral ("ephemeral depending on whether they're destroyed on workspace stop") [14]. An agent process inside the workspace provides SSH, port-forwarding, liveness checks, and startup scripts [14].

The design lesson worth importing: separating the **infrastructure description** (Terraform) from the **session lifecycle** (coderd) is the cleanest split in the survey. Templates can use *any* Terraform provider — k8s, AWS EC2, GCP, vSphere, Docker — without coderd needing per-cloud code.

## Session persistence

States: Running, Stopped, Deleted, Failed, Unhealthy [15]. Stopped means "Ephemeral resources destroyed, persistent resources idle" [15] — directly mapping to the persistent/ephemeral resource classification. Stops triggered manually or "automatically stopped due to template updates or inactivity by scheduling configuration" [15]. Unhealthy means "Resources have been provisioned, but the agent can't facilitate connections" [15] — a useful distinct state for the homelab to mirror (it separates "the infra is gone" from "the agent is unreachable", which are very different operational problems).

On Kubernetes, the canonical persistence pattern is pod (ephemeral) + PVC (persistent) mounted at `$HOME`; this is implemented in the reference Terraform template via `kubernetes_persistent_volume_claim_v1`.

Prebuilt workspaces are a pool, not on-demand snapshots. A `prebuilds {}` block inside `coder_workspace_preset` declares `instances = N` and `expiration_policy { ttl = <seconds> }` [19]. On a user create matching the preset, "ownership transfers from the prebuilds user to the requesting user", "The workspace name changes to the user's requested name", and "terraform apply is executed using the new ownership details" — "transparent to the developer" [19]. The credential-rebind step at claim time is non-trivial — fresh terraform-apply with the new owner is how Coder handles re-injecting per-user secrets into a pre-warmed workspace.

## Browser access UX

Primary web IDE is code-server — "our supported method of running VS Code in the web browser" [21]. Other supported web IDEs: VS Code Web, JupyterLab, RStudio, Airflow, File Browser [21]. JetBrains is accessed via Gateway (a desktop client connecting to a headless backend in the workspace over SSH-over-tunnel), not browser-native.

The exposure mechanism for web IDEs and arbitrary HTTP apps is the `coder_app` Terraform resource (a wrapper that routes through the agent). IDE installation in the workspace happens via template `startup_script` or modules from the Coder registry — discovery agent finding, not re-fetched.

## Multi-tenant isolation

Coder's reference design on Kubernetes uses a namespace per developer with a ServiceAccount + RoleBinding scoped to that namespace [20]. The developer gets "full kubectl access" within the namespace boundary [20]. Pod (workspace) and PVC (persistent home) live in the namespace; only the creator can connect.

The networking layer is more architecturally interesting. Coder uses Tailscale's open source ("Tailscale's open source backs our websocket/HTTPS networking logic" [16]) — WireGuard tunnels over ephemeral UDP ports, STUN-based NAT traversal, and a DERP relay fallback when direct UDP is blocked [16]. The DERP relay is **embedded in the coderd binary by default** [16], with options to point at Tailscale's public DERP fleet (`--derp-config-url`) or run a custom DERP server (`--derp-config-path`) for lower latency [16]. For an air-gapped homelab this matters: the same binary that runs the orchestrator can serve as the relay, no separate Tailscale account required.

## Credential injection

SSH keys: "SSH keys are never stored in Coder workspaces, and are fetched only when SSH is invoked. The keys are held in-memory and never written to disk" [18]. Git uses `$GIT_SSH_COMMAND` [18]. This is the cleanest in-context SSH model in the survey — keys exist in memory only when needed, no on-disk artifact for an attacker to scrape from a stopped workspace.

Git HTTPS uses external auth providers configured via env vars: `CODER_EXTERNAL_AUTH_<N>_ID|TYPE|CLIENT_ID|CLIENT_SECRET` with type `github|gitlab|azure-devops|bitbucket-cloud|bitbucket-server|...` [17]. The `ID` field is embedded in the OAuth callback URL: `https://example.com/external-auth/{ID}/callback` [17]. Git operations in the workspace transparently use the appropriate token via "Git's `GIT_ASKPASS` mechanism, which Coder configures in each workspace" [17].

General secrets: "Coder is open-minded about how you get your secrets into your workspaces" [18] — Vault, Terraform-dynamic-providers, user-managed local are all supported patterns. Critical warning: template parameters are not secrets — "anyone with view access to a workspace can also see its parameters" [18].

## Gaps

- Whether default K8s templates apply seccomp/AppArmor/NetworkPolicies out of the box not verified at primary source in this pass.
- Multi-cluster auth (coderd → remote workspace cluster) mechanism not pulled here.
- "Agent Boundaries" wrapping AI agents with per-agent firewall/process isolation referenced in discovery but not fetched in this pass.
- Tailscale tunnel bandwidth/latency in pure DERP-relay mode not quantified in [16].
