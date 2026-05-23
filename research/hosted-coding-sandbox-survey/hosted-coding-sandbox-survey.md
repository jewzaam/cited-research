# Hosted coding sandbox products — design-inspiration survey

## Overview

Eight hosted coding sandbox products, surveyed for design choices on four recurring problems: **session persistence**, **browser access UX**, **multi-tenant isolation**, and **credential injection**. Scope: design-pattern mining for a self-hosted 3-node k3s homelab build. Adoption of any surveyed product is out of scope; no pricing data.

Products covered: GitHub Codespaces, Gitpod (Classic + Flex/Ona), Coder, Replit, StackBlitz/WebContainers, Daytona (post-Feb-2025 AI-sandbox pivot), Eclipse Che, Devpod. Original prompt asked for five; Daytona, Eclipse Che, and Devpod were added during plan review because each represents an architectural class missing from the original list (open-core devcontainer-native, k8s-native operator-pattern, client-side orchestrator respectively).

Per dimension, each product reference (in [`references/`](references/)) summarises the design choice in ~2–4 paragraphs with inline citations to [`citations.md`](citations.md). [`references/cross-product-comparison.md`](references/cross-product-comparison.md) is the side-by-side table. [`references/synthesis.md`](references/synthesis.md) is the bulleted list of design patterns worth importing into the k3s build. Audit reports are in [`audit/`](audit/).

All citations come from web pages visited in this session. Vendor docs (Tier 2) are the primary sources; engineering blogs and independent technical writeups (Tier 3) backstop architectural claims; a few Tier 4 community sources cover gaps. Source publication dates are noted where visible — dev sandbox tooling moves quickly, so a 2-year-old architectural post may describe a now-historical design.

## How to read this document

- [`references/codespaces.md`](references/codespaces.md)
- [`references/gitpod.md`](references/gitpod.md)
- [`references/coder.md`](references/coder.md)
- [`references/replit.md`](references/replit.md)
- [`references/stackblitz.md`](references/stackblitz.md)
- [`references/daytona.md`](references/daytona.md)
- [`references/eclipse-che.md`](references/eclipse-che.md)
- [`references/devpod.md`](references/devpod.md)
- [`references/cross-product-comparison.md`](references/cross-product-comparison.md) — side-by-side table on the four recurring problems
- [`references/synthesis.md`](references/synthesis.md) — design patterns worth importing
- [`citations.md`](citations.md) — every cited URL with publication date and quoted material

## Headline observations

The eight products cluster into five architectural classes on the workspace-orchestration axis:

1. **VM-per-tenant, vendor-managed control plane**: Codespaces, Gitpod Flex, Replit (post-microVM rollout). Strong isolation, slower cold-create absent prebuild pools.
2. **K8s-pod-per-tenant with operator pattern**: Eclipse Che, Coder (default K8s deployment), Gitpod Classic (sunsetting). Cluster-native, requires explicit NetworkPolicy + UID-NS hardening.
3. **Sysbox-container-per-tenant**: Daytona (current). VM-grade isolation without hypervisor overhead.
4. **Browser-tab-per-tenant**: StackBlitz/WebContainers. No server-side runtime; tenancy is the user-agent process boundary.
5. **Client-orchestrated, provider-agnostic**: Devpod. No server backend; local CLI drives any backend via providers.

The four recurring problems are solved very differently across these classes. The cross-product comparison table makes the variance explicit; the synthesis file is where the cross-class lessons live.

## What the survey actually shows

**On session persistence.** Three persistence patterns dominate:
- Persistent home directory mounted into ephemeral compute (Codespaces' `/workspaces` [1], Coder's PVC at `$HOME` [14], Eclipse Che's PVC strategies [46]).
- COW block storage with manifest-based versioning (Replit Snapshot Engine [23]). The most architecturally interesting persistence story in the survey because forks/snapshots are constant-time, enabling the AI-agent safety pattern of snapshot-before-risky-op.
- Ephemeral runtime + Git as truth (StackBlitz [29][32], implicitly all products that auto-clone-on-create).

The shared design lesson: **separate persistent from ephemeral resources at the template/spec layer** so the user (and operator) knows what survives what. Coder's persistent-vs-ephemeral classification [14] is the cleanest articulation; Codespaces' `/workspaces`-versus-rest split [1] is the most user-visible.

**On browser access UX.** Convergent design: wildcard subdomain proxy per port, hosted IDE-in-browser, optional desktop access via SSH-over-tunnel. The variations matter:
- Auto-port-forward on terminal `http://localhost:PORT` output (Codespaces [6]) is the only zero-config discovery pattern in the survey.
- Two auth modes per preview — header-token (programmatic) and signed-subdomain (shareable) — is Daytona's contribution [39]; the rest tend to do one or the other.
- Single-gateway-with-Routing-OIDC-RBAC-stacked is Eclipse Che's pattern [45]; reusing kube-rbac-proxy means the access control layer is K8s-native instead of bespoke.
- The browser-tab IS the workspace (StackBlitz [29]) is the architectural outlier — most patterns don't transfer to a server-hosted build, but the **structural enforcement of the trust boundary** (COOP/COEP non-bypassable [30]) is a useful invariant.

**On multi-tenant isolation.** The strongest stated guarantee is Codespaces: "Two codespaces are never co-located on the same VM" [3]. Most other products in the K8s-pod class layer multiple defenses: pod-per-tenant + user-namespace UID/GID mapping + NetworkPolicies + RBAC. Replit's published shift toward microVMs [22] confirms that pod-with-seccomp is no longer considered sufficient for untrusted AI-generated code.

Daytona's Sysbox runtime [37] is the most homelab-portable middle ground: VM-grade isolation guarantees without per-VM startup cost, deployable on k3s via RuntimeClass.

For the K8s east-west problem specifically — "By default, all Pods in a Kubernetes cluster can communicate with each other even if they are in different namespaces" [48] — Eclipse Che ships an explicit three-policy bundle [48] that's worth cribbing as the explicit template.

**On credential injection.** Four distinct patterns, useful in combination:
- Fresh control-plane-minted token on every workspace start, scoped narrowly, auto-expiring (Codespaces `GITHUB_TOKEN` [3]).
- In-memory-only credential fetch at-invocation, no on-disk persistence (Coder SSH keys [18]).
- Label-driven secret automount on standard K8s primitives, no custom CRD (Eclipse Che [47]).
- Control-plane-signed identity tokens with verifier public keys statically injected (Replit Repl Identity [24]). The most novel pattern in the survey; the homelab analog is K8s ServiceAccount projected tokens + OIDC discovery.

Anti-pattern surfaced explicitly: env-var-only secret injection where the runtime is untrusted (StackBlitz [31] is forced into this; mainstream AI-sandbox guidance flags it as fragile).

## Stylistic disclaimer

Because counter-perspective discovery was set to "Skip" per the prompt, this survey reports vendor architectural framing without seeking independent contradicting evidence. Tier 3 independent sources (InfoQ, third-party engineering writeups, conference talks) were sought per the bias-mitigation choice in plan review and are included where available. Where a vendor claim could not be independently corroborated in this pass, the reference file flags it as a gap.

A blunt reading: vendor security and isolation claims should be treated as marketing-influenced until verified at the deployment layer (configs, NetworkPolicies, runtime classes). The synthesis file lists *design ideas to import*, not *guarantees to inherit*.

## Reflection (Phase 3 self-check)

Before finalizing, scanned the deliverable and reference files for over-claims, suppressed contradictions, and missing alternatives:

- Per-product reference files include explicit "Gaps" sections — sources not pulled in this pass, claims that remain unverified at primary source, conflicting reports across discovery and fetch.
- Gitpod Classic-vs-Flex divergence is surfaced rather than collapsed; Flex docs URL 404s in the middle of the Ona migration are flagged in [`references/gitpod.md`](references/gitpod.md) rather than papered over.
- Daytona's pre-pivot devcontainer-CDE product is deliberately excluded; current product (AI sandbox) is the one analysed.
- StackBlitz is included as architectural counterpoint with explicit "what does and does not transfer" framing in [`references/stackblitz.md`](references/stackblitz.md), not as a 5th equivalent option.
- Synthesis file ends with explicit "non-patterns" — design choices the survey suggests NOT importing — so the reader isn't left with only the positive recommendations.
