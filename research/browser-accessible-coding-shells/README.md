# Browser-accessible coding shells

Citation-backed research on browser-TTY runtimes and Kubernetes deployment patterns for self-hosting interactive AI-coding sandboxes on a k3s homelab, accessible from any tailnet device by a single URL. Scope is the access layer only.

Last revised: 2026-05-23.

## What this answers

> Given ~12 concurrent sandbox Pods, PVC-backed `$HOME`, Tailscale tailnet access — which tool + which deployment shape is the lowest-blast-radius starting point?

## TL;DR

**One ttyd Pod per operator, deployed via Argo CD ApplicationSet, fronted by the Tailscale Operator's Ingress class, with an optional oauth2-proxy sidecar, and a per-operator ReadWriteOnce PVC at `$HOME`.**

Why ttyd over the alternatives:

| Project | Disqualifying factor | Cite |
|---|---|---|
| code-server | ≥1 GB RAM floor and 265.68 MB image per pod; CVE-2025-47269 (CVSS 8.3, May 2025); Coder docs say it's not for multi-user | [19, 21, 22, 25] |
| wetty | Last release v2.7.0 from Sep 2023; Snyk flags as inactive; SSH-bridge architecture forces an `sshd` in every sandbox Pod | [16, 17] |
| gotty (sorenisanerd) | Strong defaults but fork-of-archived-project; no official Docker image | [14, 15] |
| NVIDIA OpenShell | Wrong category — agent sandbox runtime, not browser-TTY | [1] |
| OpenClaw | Wrong category — personal AI assistant in messaging shape | [4] |

ttyd's selling points: 6.9 MB Alpine image [11], documented `--auth-header X-WEBAUTH-USER` integration for upstream auth proxies [10], no opinion about multi-tenancy (deploy 12 Pods).

## Key facts table

| Project | Latest | Date | Image (compressed) | Notes |
|---|---|---|---|---|
| ttyd 1.7.7 | 1.7.7 | 2024-03-30 [9] | 6.9 MB Alpine [11] | Stable; ~26 months since release; auth-header pattern supported [10] |
| gotty (sorenisanerd) 1.7.2 | v1.7.2 | 2026-05-17 [15] | ~19 MB community Alpine (gap — unverified) | Fork of archived yudai/gotty; new process per client [14] |
| wetty 2.7.0 | v2.7.0 | 2023-09-16 [16] | ~105 MB (gap) | SSH-bridge architecture; Snyk flags inactive [17] |
| code-server 4.121.0 | v4.121.0 | 2026-05-20 [20] | 265.68 MB Debian [25] | ≥1 GB RAM floor [19]; CVE-2025-47269 [21] |
| NVIDIA OpenShell | v0.0.47 | 2026-05-22 [2] | n/a | Alpha agent-sandbox runtime [1]; CLI-only, no browser TTY |
| OpenClaw | (active) | active 2026 [4, 6] | n/a | Personal AI assistant [4]; messaging interface, no shell |
| CloudTTY | 0.8.9 | 2025-01-27 [27] | n/a | ttyd-on-k8s operator [26]; README quickstart references 0.5.0 (stale) |

Source numbers refer to [`citations.md`](citations.md).

## Decision framework

1. **Is the requirement a coding shell or a coding IDE?**
   - Coding shell → ttyd. Proceed.
   - IDE (need VS Code's UI) → code-server. Accept the higher RAM floor and CVE history; isolate per pod, do not share a code-server across operators.
2. **Are there 2+ humans on the tailnet who should be distinguishable in logs?**
   - Yes → oauth2-proxy sidecar in front of ttyd's unix socket, `X-WEBAUTH-USER` flows through [10].
   - No → Tailscale ACLs gate the URL; ttyd may run with auth disabled.
3. **Where do per-operator sandbox configs live?**
   - Argo CD ApplicationSet List generator [32], one element per operator, parameterizing PVC name and Ingress hostname.
4. **How is the URL exposed?**
   - Tailscale Operator Ingress class [28]. MagicDNS hostname, automatic Let's Encrypt, lazy first-connect cert provisioning (warm by touching once).
5. **What about nginx-ingress?**
   - Do not adopt. Archived 2026-03-24 [30]. Use Traefik (k3s default) for in-cluster routing, Tailscale Operator for tailnet exposure.

## Detail

- [`browser-accessible-coding-shells.md`](browser-accessible-coding-shells.md) — the full analysis
- [`citations.md`](citations.md) — every source numbered, tier-tagged, exact extracts
- [`references/openshell.md`](references/openshell.md) — NVIDIA OpenShell deep profile
- [`references/openclaw.md`](references/openclaw.md) — OpenClaw deep profile
- [`references/browser-tty-comparison.md`](references/browser-tty-comparison.md) — ttyd / gotty / wetty / code-server side-by-side
- [`references/k8s-deployment-patterns.md`](references/k8s-deployment-patterns.md) — Helm, ApplicationSet, ingress, probes, footguns
- [`references/synthesis.md`](references/synthesis.md) — the lowest-blast-radius recommendation, fully cited
- [`audit/citation-audit.md`](audit/citation-audit.md) — verification of every cited URL against source content
- [`audit/consistency-review.md`](audit/consistency-review.md) — cross-file numerical and logical consistency
