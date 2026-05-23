# Gitpod (Classic + Flex / Ona rebrand)

Dimension: how Gitpod solves the four recurring problems across two architectures — Classic (Kubernetes-based, sunsetting) and Flex (post-Kubernetes, current). Sources in [citations.md](../citations.md).

## Context: the pivot

Gitpod published "We are leaving Kubernetes" on Oct 31, 2024, stating "Kubernetes is built to run well controlled application workloads, not unruly development environments" [12]. They tried Firecracker, Cloud Hypervisor, and QEMU as microVM replacements in mid-2023 — Firecracker "Lacked GPU support and virtiofs support at the time of our experiments"; Cloud Hypervisor had "slower snapshot and restore processes due to the lack of userfaultfd support" [12]. The replacement is "Gitpod Flex" with "a control plane heavily inspired by Kubernetes" plus development-environment-specific abstractions [12][13]. As of May 2026 the company has rebranded to Ona; docs URLs redirect from `gitpod.io` to `ona.com`.

Architectural implication: Classic and Flex solve the four recurring problems differently. The asker's homelab work should mine Classic for the k8s-native patterns it solved well, and Flex for the post-k8s rationale.

## Session persistence

Classic states: Starting / Running / Stopping / Stopped [9]. Default 30-minute idle timeout — "workspaces stop following 30 minutes without user input" [9]. Hard lifetime caps: 8 hours (free) / 36 hours (paid) regardless of activity [9]. Multi-stage deletion: soft delete 14 days after last active (28 days if uncommitted changes), full delete 21 days after soft, database record deleted 365 days after full [9]. `gp timeout set` extends inactivity on a running workspace [9].

Flex shifts persistence semantics by abandoning the pod-with-PVC pattern entirely — environments become provisioned VMs in customer cloud accounts via "runners" [12][13]. Primary-source detail on Flex persistence is currently a gap; the Flex docs URLs are mid-migration to Ona and the `flex/introduction`, `flex/secrets`, `flex/runners/aws` pages 404 as of the fetch in this research [12][13].

## Browser access UX

Classic exposes per-workspace URLs of the form `<workspace-id>.ws-<region>.gitpod.io`; ports get a prefixed subdomain — example "3000-yourworkspace.ws-eu45.gitpod.io" [11]. Port visibility is binary, `private` (default) or `public` [11]; private ports require auth, with browser fetch requests needing `credentials: "include"` and the server returning `Access-Control-Allow-Credentials` for cross-origin [11]. Default browser editor is a VS Code variant built on the openvscode-server fork — confirmed in discovery; not re-fetched in this pass.

## Multi-tenant isolation

Classic isolates per workspace at the Kubernetes pod boundary, with user-namespace wrapping for in-pod UID/GID mapping (csweichel's PR #2048 design — discovery agent finding, not re-fetched). Network policy gaps and at least one published cross-workspace escape (CSO Online coverage in discovery) shaped the Flex rationale.

Flex inverts the model: each developer's environment is its own VM via a runner [12]. Deployment is also single-tenant — the runner lives in the customer's cloud account (AWS first, GCP/Azure planned) [12]. So the multi-tenant isolation problem partially dissolves: tenancy boundary moves to a VM and the deployment moves to a single-tenant account, eliminating the noisy-neighbour and namespace-escape vectors of the Classic shared-cluster pattern.

## Credential injection

Classic uses static OAuth integrations for GitHub/GitLab/Bitbucket (custom integrations for generic OAuth). Env vars have two explicit scopes — Repository-level and User-level — with "Repository-specific Environment Variables will take precedence over User-specific Environment Variables" [10]. Org-level access boundary: "Only members of the Gitpod organization where the repository resides will be able to access the environment variables inside a running workspace" [10]. By default `GITPOD_IMAGE_AUTH`-type secrets are "not mounted into workspaces for security reasons" [10] — a sensible default that protects registry creds from leaking into user processes.

Flex introduces a Secrets primitive distinct from env vars: encryption at rest (AES256-GCM per discovery agent's reading of the changelog), env-or-file delivery, and the discipline that "Secret updates apply to new environments only; existing environments keep old value" (discovery finding; the `ona.com/docs/flex/secrets` page 404s as of this research).

## Self-managed history (relevant for the homelab)

The user-installable Gitpod Self-Managed product was discontinued in Dec 2022; replaced by Dedicated (single-tenant managed in customer AWS) then absorbed into Flex. Source code remains AGPL on github.com/gitpod-io/gitpod, but the Helm charts are unmaintained as a deployable product. The most useful design artifacts for a self-hosted k3s build are the ws-manager/ws-daemon components (worth reading as design references) and the documented "leaving Kubernetes" failure modes [12] — knowing what burned Gitpod helps avoid the same traps.

## Gaps

- Flex control-plane substrate not publicly disclosed beyond "inspired by k8s" framing [12][13]; no source surfaced the actual tech stack.
- Conflicting Classic sunset dates (some sources cite April 2025, others September 2025) not resolved here.
- Flex docs URLs in the middle of an `ona.com` migration produce 404s for several pages cited in plans [12][13].
- Flex per-environment isolation depth (1 EC2 always? sometimes shared?) not verified at primary source in this pass.
- CSO Online vulnerability that prompted Flex rationale: specific CVE / disclosure detail not pulled in this pass.
