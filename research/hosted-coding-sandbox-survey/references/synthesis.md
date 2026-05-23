# Synthesis — design patterns worth importing into a self-hosted k3s sandbox

Bulleted patterns from the survey worth adopting in a self-hosted k3s AI-coding sandbox. Each tagged with the source product, the recurring problem it addresses, and the citation. Per the asker's request: no code proposals, no Helm chart proposals — design choices only.

Numbering is for reference, not priority. The survey deliberately includes more candidates than any one build should adopt; the asker filters.

## Session persistence

1. **`/workspaces`-style persistent mount with explicit rebuild semantics** — one directory survives stop/start AND container rebuild; everything else only survives stop/start. Makes the contract with the user obvious: "your code is safe; your global pip cache isn't." From Codespaces [1] — addresses persistence + sets clear user expectations.

2. **Persistent vs ephemeral resource classification at the template layer** — make the template author declare which resources die on stop. Maps cleanly to the K8s pod (ephemeral) + PVC (persistent) split but generalizes to other backends. From Coder [14][15] — addresses persistence + lifecycle clarity.

3. **PVC strategy as an admin-level choice** — `per-user`, `per-workspace`, `ephemeral` configurable at the cluster level with per-workspace override. Avoids hard-coding a single persistence model. From Eclipse Che [46] — addresses persistence + multi-tenant flexibility.

4. **Pool-based prebuilds, not on-demand snapshots** — keep N warm workspaces ready; user-create claims one and transfers ownership rather than building from scratch. The hard part is credential rebind on claim (Coder does fresh `terraform apply` with new owner). From Codespaces ([5][8] — "pools of codespaces, fully cloned and bootstrapped, waiting to be connected") and Coder [19] — addresses cold-create time.

5. **Snapshot Engine pattern** — manifest-based COW block storage. Filesystem state is a manifest of pointers; `checkpoint` copies the manifest, `restore` swaps it; forks are constant-time. The killer feature for AI sandboxes is fork-before-risky-op + restore-on-failure. From Replit [23] — addresses persistence + AI-agent safety.

6. **Idle "activity" includes terminal I/O, not just keyboard input** — long-running builds and test loops keep the workspace alive when output is streaming. Otherwise long CI-style work gets killed mid-run. From Codespaces [7] — addresses session persistence ergonomics.

7. **Ephemeral mode that revokes session-scoped credentials on stop** — credential lifecycle bound to sandbox lifecycle, not separate. From Daytona [37] — addresses persistence + credential hygiene jointly.

8. **Soft-delete + full-delete + record-delete staircase** — three-stage cleanup with different timeouts (e.g. 14d / +21d / +365d). Recovery window for accidents, hard cleanup eventually, audit trail beyond. From Gitpod Classic [9] — addresses persistence + ops accountability.

## Browser access UX

9. **Wildcard subdomain proxy for per-port previews** — one Ingress, wildcard DNS, URL pattern `https://{port}-{workspace}.{proxy-domain}`. Avoids per-port Ingress objects and works with cert-manager wildcard certificates. From Codespaces [6], Gitpod [11], Daytona [39], Eclipse Che [45] — convergent across the survey. Addresses browser access UX.

10. **Two preview-auth modes: header-token (programmatic) and signed-subdomain-token (shareable)** — programmatic clients use a header, humans share URLs. Different threat models, different TTL defaults. Plus a `public=true` flag for explicit anonymous access. From Daytona [39] — addresses browser access UX + auth model.

11. **Web terminal exposed as another preview port** — terminal is just an HTTP server inside the sandbox on a reserved port (Daytona uses 22222), surfaced via the same proxy fabric. No special-cased terminal protocol. From Daytona (discovery; not in cited primary sources) — addresses browser access UX simplification.

12. **Auto-port-forward on `http://localhost:PORT` terminal output** — when a build prints its dev-server URL, the proxy auto-exposes the port. Zero-configuration discovery. From Codespaces [6] — addresses browser access UX.

13. **URL-as-entry-point onboarding** — swap a domain prefix (`github.com` → `pr.new`) to open any repo or PR in the sandbox. Low-cost affordance for the AI-collab flow where someone shares a PR URL. From StackBlitz [34] — addresses onboarding (and indirectly browser access UX).

14. **Single gateway Deployment combining Routing + OIDC + RBAC enforcement** — Traefik + OAuth2-Proxy + kube-rbac-proxy in one Deployment, instead of three separate ingress/auth layers to configure. From Eclipse Che [45] — addresses browser access UX + auth uniformity.

15. **JetBrains Gateway support via SSH-over-tunnel** — JetBrains IDEs don't browser-render; they need a desktop client + headless backend in the workspace. Surveyed products that support this (Coder, Devpod, Daytona via SSH) all use SSH-over-tunnel rather than inventing a new protocol. From Coder [21], Devpod [55] — addresses browser-or-desktop access flexibility.

## Multi-tenant isolation

16. **Per-workspace VM as tenancy unit** — most defensible isolation primitive in the survey. Codespaces' "Two codespaces are never co-located on the same VM" [3] is the strongest stated guarantee. For k3s on a 3-node homelab the analog is Kata Containers / gVisor / Firecracker-via-Kata, with the trade-off being startup time and complexity. Codespaces [3], Replit (rollout) [22], Gitpod Flex [12] — addresses multi-tenant isolation. Worth importing as the *aspiration*; pod + UID-NS is usually the pragmatic baseline.

17. **Sysbox runtime for VM-grade isolation without hypervisor overhead** — RuntimeClass on k3s nodes, root inside maps to unprivileged outside, partial procfs/sysfs virtualization, selective syscall interception. Preserves docker-in-docker for the AI agent's tooling. From Daytona [37] — addresses multi-tenant isolation at lower cost than full microVMs.

18. **Workspace as a Custom Resource, reconciled by an operator** — `DevWorkspace` CR per workspace; operator translates CR → Deployment + PVC + Service. Standard K8s tooling (`kubectl get devworkspaces`) for ops; standard reconciliation semantics. From Eclipse Che [43] — addresses architectural alignment with k3s.

19. **Namespace per user with auto-provisioning template** — namespace name derived from userid via a configurable template; Che server creates on first login; admins can pre-create with required labels. From Eclipse Che [44] — addresses multi-tenant isolation.

20. **Bidirectional sync from admin namespace to user namespaces with revert-on-tamper** — admin pushes shared configs/secrets to all user namespaces, and any user-namespace modifications get reverted. Keeps the user-namespace state managed-from-the-center without giving up per-tenant separation. From Eclipse Che [44] — addresses isolation + central control.

21. **Three explicit NetworkPolicies for the workspace pattern** — the K8s default ("all Pods in a Kubernetes cluster can communicate with each other even if they are in different namespaces" [48]) is wrong for multi-tenant workspaces. Eclipse Che's bundle (`allow-from-eclipse-che`, `allow-from-openshift-apiserver`, `allow-from-workspaces-namespaces`) is the explicit template to crib. From Eclipse Che [48] — addresses east-west isolation.

22. **`INTER_SANDBOX_NETWORK_ENABLED=false` default** with explicit opt-in for inter-sandbox networking. Default-deny posture for the most likely undesired traffic. From Daytona [38] — addresses east-west isolation.

23. **Subpath-isolated shared volumes** — one S3 / PVC volume, per-sandbox subpaths, no cross-read possible. Lets a homelab share a model-weights cache or a build cache across sandboxes without compromising isolation. From Daytona [41] — addresses storage isolation.

24. **Tailscale WireGuard mesh for agent ↔ client tunnels with embedded DERP fallback** — direct UDP when possible (STUN-discovered), relayed via DERP when blocked, end-to-end encryption preserved. DERP server is embedded in the orchestrator binary so the air-gapped homelab needs no separate Tailscale dependency. From Coder [16] — addresses connectivity + isolation (no exposed inbound ports on the workspace pod).

25. **Pull-based runners** — runners poll the control plane for jobs rather than receiving inbound RPC. Compute nodes need no Ingress, no port-forwards, no NodePorts. Operationally simpler for nodes behind NAT or with constrained Ingress. From Daytona [35] — addresses operational topology.

26. **Per-customer-cloud-project isolation as a *deployment* boundary** (separate from per-sandbox isolation as a *runtime* boundary) — Replit gives every customer their own GCP Project even on free tier [22]. For a homelab the analog is per-user namespace + per-user PV-class + per-user network-class — same idea, narrower scope.

## Credential injection

27. **SSH keys in-memory only, never written to workspace disk** — fetched at SSH invocation, held in memory, gone when not needed. No on-disk artifact for an attacker (or a curious AI agent) to grep. From Coder [18] — addresses credential safety.

28. **Git HTTPS via `GIT_ASKPASS` per workspace** — git's existing extension point handles HTTPS auth without the workspace storing tokens. The askpass helper looks up the right token by repo URL at request time. From Coder [17] — addresses credential safety + ergonomics.

29. **External-auth env-var matrix** — `<PRODUCT>_EXTERNAL_AUTH_<N>_ID|TYPE|CLIENT_ID|CLIENT_SECRET` is a clean, multi-provider-friendly config schema. The `ID` field is reused as the OAuth callback URL path, so adding a new provider is a small config change without re-deploying. From Coder [17] — addresses credential infra.

30. **Label-driven secret/configmap automount** — standard K8s Secret + labels `controller.devfile.io/mount-to-devworkspace=true` + `watch-secret=true` + annotation `mount-as: file|subpath|env`. No custom CRD, no new secrets API. The DevWorkspace Operator handles the rest. From Eclipse Che [47] — addresses credential injection on K8s.

31. **Three-tier secret hierarchy (user / repo / org) with explicit precedence** — repo-level secrets override org-level on name collision. Lets a team standardize creds at the org level while letting a single repo override for special cases. From Codespaces [4] — addresses credential scoping.

32. **Short-lived federated tokens for registry pulls** — Daytona's ECR pattern: assume an IAM role on every pull, fetch a short-lived token, throw it away. "No long-lived AWS credentials are shared" [42]. Generalizes beyond ECR to anything supporting OIDC / SAML / Kubernetes-ServiceAccount-projection. From Daytona [42] — addresses credential infra blast-radius.

33. **Repl Identity pattern: control-plane-signed PASETO tokens with verifier public keys injected into workspaces** — workspaces authenticate to each other (and to internal services) by exchanging tokens that the control plane signs, verified using ED25519 keys statically injected via `REPL_PUBKEYS`. No per-service secret distribution. From Replit [24] — addresses inter-service auth in a multi-workspace deployment. K8s analog: projected ServiceAccount tokens + OIDC discovery.

34. **`GITPOD_IMAGE_AUTH`-style "registry creds default-not-mounted into user processes"** — secrets the platform needs (image pull, registry auth) are deliberately scoped away from user-process env. Opt-in to expose. From Gitpod Classic [10] — addresses credential blast-radius.

35. **Forward-credentials-from-client pattern (Devpod)** — credentials never traverse the central control plane; the local client tunnels them directly to the workspace. Even for a server-orchestrated build, partial adoption is possible: broker via Vault / external-secrets at workspace-create time, never persist long-lived tokens on the control plane. From Devpod [53][56] — addresses credential infra blast-radius.

36. **Secrets distinct from env vars as a first-class primitive (file-or-env delivery)** — Flex's secret primitive supports file-mount via devcontainer at a user-chosen path, recommended over env for complex/sensitive data. Avoids leaking secrets via process env exposure (e.g. `ps`, child-process env inheritance). From Gitpod Flex (discovery; primary URL 404 in this pass; referenced in [12][13] context) — addresses credential safety.

## Architectural ideas crossing all four dimensions

37. **Three-plane separation (interface / control / compute)** — make the control plane stateful and small, the interface plane a thin client surface, the compute plane stateless and pull-based. Maps cleanly to k3s. From Daytona [35] — addresses architectural shape.

38. **Defense-in-depth invariant: "No single control is the last line of defense. Every layer assumes the one above it might fail"** [22] — adopt this as an axiom rather than a slogan. Translates concretely: workspace pod can't reach control plane DB even if it escapes; control plane can't see workspace user creds even if compromised; user can't bypass NetworkPolicies even with shell access. From Replit [22] — addresses everything.

39. **Devcontainer.json as the portable workspace spec** — multiple products in the survey use this (Codespaces, Coder via envbuilder, Daytona pre-pivot, Devpod, Eclipse Che via devfile). Lets a homelab workspace be portable in/out without rewriting. Convergent across the survey — addresses architectural openness.

40. **Snapshot-then-mutate as the safety primitive for AI agents** — Replit Agent's pattern. Before letting the AI do anything destructive, snapshot the filesystem (and DB); on failure, restore. The Snapshot Engine [23] is the concrete substrate; the design idea is what's worth importing. Addresses the AI-coding-specific failure modes that all of the recurring problems amplify.

## Non-patterns — things to NOT adopt

- **Env-var-only credential injection as the only path** — StackBlitz [31] and the broader AI-sandbox ecosystem flag this as fragile when the runtime host isn't trusted. Have env-var support, but offer broker / file-mount / on-demand-helper alternatives.
- **Pod-isolation as the sole tenant boundary without user-namespaces + NetworkPolicies** — Gitpod Classic's real-world cross-workspace escape ([12] history) shows what happens when you stop at pod-per-tenant. Defence in depth from day one.
- **Always-on long-running dev containers as the persistence model for hosted apps** — Replit deprecated it ([28]) because the dev-time and prod-time concerns conflated. Separate dev workspace lifecycle from deploy lifecycle.
- **Kubernetes as the workspace orchestrator** if your workspaces are spiky, stateful, and need GPU-class flexibility — Gitpod's "leaving Kubernetes" rationale [12] is worth reading. On a 3-node k3s homelab this caveat doesn't necessarily apply (scale is small, workloads predictable), but the failure modes Gitpod hit at scale are warnings about what becomes painful first.
