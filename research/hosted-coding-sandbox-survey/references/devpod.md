# Devpod (Loft Labs)

Dimension: how Devpod solves the four recurring problems. Notable because the orchestrator is **client-side**, not server-side. Sources in [citations.md](../citations.md).

## Architecture orientation — client-only

"No need to install a server backend, DevPod runs solely on your computer" [57]. The local CLI (or desktop app) is the orchestrator; "providers" plug in to deploy the workspace against any backend — Docker, Kubernetes, SSH, AWS, GCP, etc. Architecture is "client-agent": "the client deploys it's own agent to host various servers, such as a grpc server or SSH server" [51].

Communication uses a vendor-specific "tunnel": "Devpod establishes a connection to the workspace using a vendor specific API. This vendor specific communication channel is referred to as the 'tunnel'" [51]. AWS uses instance-connect; Kubernetes uses kubectl. The agent inside the workspace "starts a SSH server using the STDIO of the secure tunnel" [51] — every IDE access path is SSH-over-tunnel rather than HTTP-over-Ingress.

This is architecturally the inverse of every other product in the survey. There is no shared server-side control plane in the OSS edition. Multi-tenancy isn't solved at the Devpod layer; it's whatever the underlying provider provides (kubeconfig + RBAC for K8s, IAM for AWS, etc).

## Session persistence

Inactivity timeout handling depends on the provider class [54]:
- **Container providers** (Docker, Kubernetes, SSH): "DevPod can automatically kill the container its running in by terminating the process with pid 1." A side process tracks activity and "kill itself when the user hasn't connected for the given duration."
- **Machine providers** (VMs): "DevPod will install itself as a Daemon into the remote VM and track the activity from there." The daemon may "automatically shutdown the machine or even delete it, based on what's cheaper for the given cloud provider."

The K8s provider specifically uses PersistentVolume sized by the `persistentVolumeSize` provider option (discovery; not re-fetched here — the deploy-k8s page surfaced the tunnel mechanism but not the PV story [52]).

## Browser access UX

Browser IDE is **OpenVSCode Server** installed into the workspace, reached via the local Devpod client's localhost tunnel [55]. "DevPod is able to open VS Code in a browser in a workspace" via `devpod up my-workspace --ide openvscode` [55]. JetBrains IDEs (Goland, PyCharm, IntelliJ, etc) launch via Gateway, again over SSH-over-tunnel [55]. SSH access: "DevPod will automatically modify the ~/.ssh/config to include an entry for WORKSPACE_NAME.devpod" [55]. The CLI fallback `devpod ssh my-workspace` [55] gives raw SSH without an IDE.

**Crucial architectural fact**: "browser access" still flows through the local client. There is no public URL — the browser hits `localhost` and the local Devpod client tunnels to the workspace. This is architecturally distinct from server-orchestrated products that expose a hosted URL behind an Ingress. For a homelab build this means there are two valid patterns: (a) server-orchestrated public-URL-per-workspace (Coder / Eclipse Che / Daytona style), and (b) client-orchestrated localhost-tunnel-per-workspace (Devpod style). They have very different threat models and operational profiles.

## Multi-tenant isolation

OSS Devpod has no native multi-tenancy — each developer runs their own client and supplies their own kubeconfig (or cloud creds). Isolation is whatever the underlying provider gives. For K8s specifically the tunnel is "set up using the kubernetes control plane (e.g. kubectl ...) so an agent is not necessary to be run on the kubernetes node" [52] — which means provider-level RBAC on the kubeconfig is the tenancy boundary.

Devpod Pro (paid, Loft Labs) adds a centralized control plane with templated workspaces and removes the need for per-engineer cluster IAM. (Discovery agent finding; Pro pages not pulled in this pass.)

## Credential injection

Devpod's credential model is **forward from the client, never broker centrally**. Because the client is local, "credentials never traverse a third-party server — they flow client → tunnel → agent → container". The catalogue [53]:
- **Git HTTPS** via "git credentials helper".
- **Git SSH** via "agent-forwarding that will be configured automatically on the ssh configuration for the workspace."
- **Docker registry** via "docker credentials helper".
- **GPG signing** via "an ssh tunnel" — opt-in only with `GPG_AGENT_FORWARDING=true` or `--gpg-agent-forwarding`.

Opt-out flags [53]:
- `SSH_INJECT_GIT_CREDENTIALS=false`
- `SSH_INJECT_DOCKER_CREDENTIALS=false`

Provider-level toggles in `provider.yaml` `agent` section [56]: `injectGitCredentials`, `injectDockerCredentials`.

Agent injection on workspace creation handles "deploying the container, forward credentials, ssh server, auto-shutdown after a period of inactivity" [56].

## Lessons for a k3s homelab

Devpod's value to a homelab build is mostly **anti-pattern** clarity — by being the inverse of server-orchestrated products, it reveals what server orchestration is actually buying. Things to import:
- **Forward-credentials-from-client** pattern reduces the central credential store's blast radius. Even for a server-orchestrated homelab, brokering credentials via Vault / external-secrets and never persisting long-lived tokens is a usable adaptation.
- **Devcontainer.json compatibility** as a portable workspace spec. Devpod's whole providers system runs against `devcontainer.json`; the same spec works in Codespaces, Coder (via envbuilder), Daytona, Eclipse Che (devfile is broader but devcontainer-compatible).
- **Tunnel-over-kubectl** for K8s provider [52] — no Ingress needed for the control path. Useful for a homelab behind NAT.
- **Provider abstraction with declared opt-ins per credential type** [56] — explicit > implicit.

## Gaps

- Default `persistentVolumeSize` for K8s provider not confirmed at primary source in this pass.
- Default inactivity timeout values per provider class not stated on the inactivity-timeout doc [54].
- Devpod Pro details (control plane, on-cluster footprint) not pulled.
- `--ide none` and pure-SSH workflow referenced by discovery agent but not explicitly named on the connect-to-workspace doc [55].
- Specific SSH-over-kubectl tunnel mechanism (port-forward? exec stdio?) not detailed on the deploy-k8s page [52].
