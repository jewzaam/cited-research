# OpenShell — direct profile

## Dimension scope

The asker named "OpenShell" as inspiration for a self-hosted browser-accessible coding sandbox. Multiple projects use the name; this section identifies the candidate that fits the framing, profiles it on maintenance, architecture, security, deployment, and access UX, and ends with an adoption verdict.

Source numbers refer to [`citations.md`](../citations.md).

## Identifying the right project

Three distinct projects appear under the name "OpenShell" in current search results:

1. **NVIDIA/OpenShell** — open-source sandbox runtime for autonomous AI agents, announced at GTC 2026 [1, 3].
2. **Open-Shell/Open-Shell-Menu** — "Classic Shell Reborn," a Windows Start Menu replacement. Unrelated to coding sandboxes.
3. **LobsterTrap/OpenShell** — a small fork visible in search results; purpose not verified in-session.

Only NVIDIA/OpenShell fits the "isolated runtime for AI-coding workloads" framing the asker is exploring. The rest of this reference covers it specifically.

## Maintainer + activity

| Field | Value | Source |
|---|---|---|
| Maintainer | NVIDIA Corporation | [1] |
| License | Apache 2.0 | [1] |
| Primary language | Rust (89.6%) | [1] |
| Status (self-described) | Alpha — "proof-of-life: one developer, one environment, one gateway" | [1] |
| Latest release | v0.0.47 (2026-05-22) | [2] |
| Release cadence | Roughly daily through May 2026 (v0.0.43 → v0.0.47 in five days) | [2] |
| Launch | GTC 2026 (March 2026) | [3] |

The cadence is unusually fast — five tagged releases in five consecutive days — consistent with active early-alpha development rather than stable maintenance.

## Architecture

OpenShell is **not** a browser-TTY runtime. It is a CLI-driven sandbox host for autonomous AI agents [1].

- The operator invokes commands like `openshell sandbox create` and `openshell policy set` from a CLI [1].
- An optional TUI dashboard (`openshell term`) is described as "a real-time terminal dashboard for monitoring gateways, sandboxes, and providers." It is keyboard-driven (Tab, j/k, Enter, :) and used for monitoring, not interactive coding [1].
- No browser-based terminal endpoint is documented in the README [1].

The session model is built around _agents_ executing inside a sandbox, with policy enforcement at filesystem, network, process, and inference layers [1]. The human's role is to author policy and inspect outcomes from outside the sandbox.

## Security model

Compute drivers supported: Docker, Podman, MicroVM, and Kubernetes [1]. Policy enforcement is declarative YAML — "governed by declarative YAML policies that prevent unauthorized file access, data exfiltration, and uncontrolled network activity" [1].

Third-party CVE claims were surfaced by a discovery sub-agent (CVE-2026-44112 and others, attributed to OpenShell), but the underlying sources were not cross-referenced against NIST NVD or NVIDIA's security advisory page in this session. These CVE numbers are **not** cited from this reference — see [`citations.md`](../citations.md) §"Sources noted but not verified in-session" for the unverified pointers.

## Deployment story

| Driver | Status | Source |
|---|---|---|
| Docker | First-class (default for local dev) | [1] |
| Podman | Supported | [1] |
| MicroVM | Supported | [1] |
| Kubernetes (Helm chart) | **Experimental** | [1] |

The Kubernetes path is the most relevant to the homelab framing, and NVIDIA flags it as experimental. The README's own framing ("one developer, one environment, one gateway") is single-tenant and not designed for the ~12-concurrent-sandbox use case described in the brief.

## Access UX

Browser-only: **no**. CLI-bridged: **yes (CLI is primary)**. The TUI dashboard runs in a local terminal, not a browser. A human operator on a Chromebook or Android phone over a Tailscale tailnet cannot open a sandbox via a URL — they would need an SSH-attached `openshell` CLI somewhere with terminal access.

## Verdict

**Reference architecture to copy ideas from, not a directly adoptable runtime.**

Reasoning:

1. The framing is wrong. OpenShell sandboxes _agents_ executing on behalf of a human; the asker's framing is a human directly typing in a browser-attached shell. The two surfaces are architecturally different — OpenShell is the security layer that wraps the agent, not the layer that renders a terminal for a human.
2. Alpha-stage Kubernetes support, single-tenant by design [1].
3. Ideas worth borrowing: declarative YAML policy enforcement; per-binary network egress allow-lists; sandbox-as-Pod with policy CRDs.

For the access-layer question this brief asks, OpenShell does not answer it. For the eventual question "how do I sandbox the agent running inside my browser-attached coding shell," OpenShell becomes interesting — but that is the next research topic, not this one.

## Gaps and Limitations

- The full content of the NVIDIA documentation site (architecture diagrams, Helm chart specifics, PVC behavior) was not exhaustively read.
- The third-party CVE claims for OpenShell (sourced from secondary tech-press URLs by sub-agents) are not cited here pending direct NVD verification.
- The `Open-Shell-Community` repository, which the README references for community-contributed sandbox definitions, was not profiled in detail.
