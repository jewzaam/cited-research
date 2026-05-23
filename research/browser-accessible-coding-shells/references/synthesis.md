# Synthesis — most boring, lowest-blast-radius starting point

## Dimension scope

Given the findings across [openshell.md](openshell.md), [openclaw.md](openclaw.md), [browser-tty-comparison.md](browser-tty-comparison.md), and [k8s-deployment-patterns.md](k8s-deployment-patterns.md): which tool + which deployment shape is the lowest-blast-radius starting point for the brief's use case? The brainstorm session that follows this research will design the actual build. This section does not propose code or a Helm chart.

Source numbers refer to [`citations.md`](../citations.md).

## The verdict in one sentence

**One ttyd Pod per operator, deployed via Argo CD ApplicationSet, fronted by the Tailscale Operator's Ingress class, with an oauth2-proxy sidecar (or none, if Tailscale ACLs are deemed sufficient) and a per-operator ReadWriteOnce PVC mounted at `$HOME`.**

## Why ttyd

Per [`browser-tty-comparison.md`](browser-tty-comparison.md):

- **Smallest blast radius.** 6.9 MB Alpine image, single C binary plus libwebsockets. The smallest attack surface of the four candidates. [§ttyd in `browser-tty-comparison.md`, ref 11]
- **Cleanest auth hook.** The `--auth-header X-WEBAUTH-USER` mode plugs directly into an oauth2-proxy sidecar with minimal moving parts — this is the documented integration pattern, not a workaround. [§ttyd, ref 8, 10]
- **Boring transport.** Works under Traefik v3 with no special configuration. [§Ingress in `k8s-deployment-patterns.md`, ref 29]
- **No multi-user assumptions.** ttyd is a single-tenant gateway; the multi-tenancy is achieved by deploying one Pod per operator. This matches the brief's "one Pod, one operator" framing exactly.

## Why not the alternatives

- **code-server.** [§code-server in `browser-tty-comparison.md`] Heaviest per-pod footprint (≥1 GB RAM stated min [19], 265.68 MB Debian image [25]). 12 concurrent operators = ≥12 GB RAM committed before any actual coding happens. Recent named CVE (CVE-2025-47269, May 2025 [21]) and Coder's own positioning that code-server is wrong for multi-user deployments make this overshoot the brief.
- **gotty (sorenisanerd fork).** [§gotty in `browser-tty-comparison.md`] Strong defaults — new process per connection by design [14] — and active 2026 release cadence [15]. But the fork-of-archived-project lineage and absence of an official Docker image are unnecessary risks when ttyd's auth-header story is more mature and its image is smaller.
- **wetty.** [§wetty in `browser-tty-comparison.md`] v2.7.0 from September 2023 is the latest release [16], Snyk flags it as inactive [17], and the SSH-bridge architecture forces an `sshd` inside every sandbox Pod for negligible benefit in this scenario. The wh0 Glitch incident [18] is a platform-deployment story rather than an upstream WebSocket-protocol flaw, so it is not the primary disqualifier — the maintenance signal is.
- **NVIDIA OpenShell.** [`openshell.md`] Wrong category — agent sandbox runtime, not a browser-TTY [1]. Worth borrowing the policy-YAML model in a future iteration; not the runtime for this iteration.
- **OpenClaw.** [`openclaw.md`] Wrong category — personal AI assistant, not a coding sandbox [4]. Discard.

## Why not CloudTTY (the obvious ttyd operator)

CloudTTY [26] wraps ttyd in a Kubernetes operator with a CRD and Helm chart. It is the natural pull-of-gravity answer to "deploy ttyd on k8s." However:

- It is designed for ephemeral kubectl-against-cluster shells, not persistent coding sandboxes [26]. No persistence story is documented.
- The README's quickstart references chart `0.5.0` while latest is `0.8.9` [26, 27]. The docs-to-reality gap signals limited maintenance attention.
- The CRD adds a dependency (the operator) that needs to be installed, watched, upgraded, and debugged separately. For ~12 sandboxes managed by a single operator (the human), a plain Deployment + PVC per Application is simpler.

CloudTTY is a reference implementation worth reading. It is not the starting point.

## Why Argo CD ApplicationSet over a single Helm release

Per [`k8s-deployment-patterns.md`](k8s-deployment-patterns.md):

- One Application per operator gives independent sync, independent rollback, independent ingress hostname.
- The List generator [32] makes adding/removing operators a one-line edit to the ApplicationSet.
- Each Application can parameterize its own PVC name (`existingClaim`), avoiding shared-storage assumptions.

The known multi-tenant anti-patterns for ApplicationSet (mixing infra+dev, self-service Application creation) do not apply here because the operator authors the ApplicationSet themselves.

## Why Tailscale Operator over a tailscale sidecar or plain Ingress

- **Single URL per sandbox.** Each Application gets an Ingress with `ingressClassName: tailscale`, producing a stable MagicDNS hostname [28].
- **No per-device tooling.** Tailscale already runs on every device the operator uses; once the URL is in the tailnet, any device can open it.
- **TLS handled by the operator.** Let's Encrypt certs provisioned automatically [28]. The lazy-on-first-connect quirk [28] is documented and trivially worked around (touch the URL once after creation).

## Auth: oauth2-proxy sidecar vs Tailscale ACLs only

The brief excludes the question of per-sandbox identity (Tailscale ACLs gate the URL itself). For a homelab where the operator is the only person on the tailnet, Tailscale ACLs may be sufficient and the oauth2-proxy sidecar is overhead.

However, ttyd's `-c user:pass` plaintext credential exposure [13] argues against enabling basic auth even as defense-in-depth. The two reasonable options are:

1. **No auth in ttyd.** Trust Tailscale ACLs to gate reachability. Run ttyd on a Pod-local socket if paranoia warrants.
2. **oauth2-proxy sidecar.** ttyd exposes a unix socket only [10], oauth2-proxy fronts it with OIDC against your IdP, and the `X-WEBAUTH-USER` header carries the verified identity into ttyd. This is the documented pattern [10].

Option 2 is the lower-blast-radius answer because it preserves identity-aware logging and survives any future tailnet ACL misconfiguration.

## Why a per-operator ReadWriteOnce PVC

- One pod per operator means ReadWriteOnce is correct — no need for NFS / Longhorn complexity.
- PVC-backed `$HOME` survives Pod restarts and node reschedules (within the k3s storage class's constraints).
- The code-server Helm chart's default of `10 Gi ReadWriteOnce` [23] is a sensible per-operator starting size for the ttyd Pod too.

## Design recommendations

Each bullet cites the section it depends on.

1. **Runtime: ttyd, official Alpine image** — smallest blast radius, simplest auth-header integration. Refs [8, 10, 11], [§ttyd in `browser-tty-comparison.md`].

2. **One Deployment + Service + Ingress + PVC per operator**, packaged as a single chart used by an Argo CD ApplicationSet List generator [32], with the operator name as the parameter that produces a unique Application, PVC name, and Ingress hostname. [§Argo CD ApplicationSet in `k8s-deployment-patterns.md`].

3. **ttyd runs on a unix socket, not on a TCP port**; an oauth2-proxy sidecar (or other forward-auth proxy) terminates HTTPS-from-Tailscale, validates identity, and injects `X-WEBAUTH-USER` before forwarding to the socket. Justification: ttyd auth-proxy docs require unix socket for header-pass-through security [10]. [§ttyd in `browser-tty-comparison.md`].

4. **PVC: ReadWriteOnce, 10 Gi (starting), `existingClaim` parameterized per operator**. Lets sandboxes survive Pod restarts and node reschedules. [§Persistent home directory patterns in `k8s-deployment-patterns.md`, ref 23].

5. **Ingress class: Tailscale Operator** with `spec.ingressClassName: tailscale`. MagicDNS hostname per sandbox; auto-Let's-Encrypt cert; first-hit slow as documented [28]. [§Tailscale Operator in `k8s-deployment-patterns.md`].

6. **Liveness/readiness: `httpGet /` against the ttyd port**. Minimal viable. Tool-specific probe shapes are sparse on the public web. [§Liveness/readiness probes in `k8s-deployment-patterns.md`].

7. **Do not adopt CloudTTY** for the first iteration. Read its CRD as inspiration only; the Argo CD ApplicationSet shape gives multi-tenancy without an extra operator to babysit. [§CloudTTY in `k8s-deployment-patterns.md`, refs 26, 27].

8. **Do not adopt NVIDIA OpenShell or OpenClaw** as the runtime. OpenShell is the agent-sandbox layer (worth revisiting later for the inside-the-Pod question); OpenClaw is a personal AI assistant in a different category. [§Verdict in `openshell.md`, `openclaw.md`].

9. **Do not adopt nginx-ingress.** The repository was archived 2026-03-24 [30] and the long-standing WebSocket-drop-on-reload behavior [31] is structural. Use the Tailscale Operator's ingress (which routes via the operator's own infrastructure) or Traefik (k3s default) [29, 30, 31]. [§Ingress and WebSocket behavior in `k8s-deployment-patterns.md`].

10. **Plan for the WebSocket CSRF threat model** [33]. Whatever auth proxy fronts ttyd must validate the `Origin` header on the WebSocket handshake — cookies alone are not enough. This is a structural risk class, not a per-tool quirk. [§Cross-cutting risks in `browser-tty-comparison.md`].

## Gaps and Limitations

- The recommendation favors operational boring over feature richness. If the eventual workflow requires VS Code's UI (not just a shell), the synthesis points to code-server as a second iteration with the trade-offs accepted (higher RAM floor, CVE history).
- The "no per-operator identity" defense-in-depth assumes a homelab with one or two trusted operators. For a multi-person tailnet, the oauth2-proxy path becomes mandatory rather than optional.
- The brief explicitly excludes what runs inside the sandbox; this synthesis takes that exclusion seriously and does not pre-decide whether Claude Code, OpenClaw, or any other agent runs in the Pod. The Pod is whatever the next research topic decides.
