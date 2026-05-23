# OpenClaw — direct profile

## Dimension scope

The asker has heard the name "OpenClaw" but knows nothing about it, and is asking whether it is relevant to the "browser-accessible coding sandbox in k3s" framing. This reference confirms what OpenClaw is, profiles it on the same axes as [`openshell.md`](openshell.md), and ends with a verdict.

Source numbers refer to [`citations.md`](../citations.md).

## Identifying the right project

Search returned a single coherent project under "OpenClaw" in the AI-agent space. No competing project of the same name was found at meaningful adoption level. The project's identity is well-established because of repeated rebranding [6]:

- **Clawdbot** — initial public release, November 2025 [6].
- **Moltbot** — renamed 2026-01-27 after Anthropic trademark complaints [6].
- **OpenClaw** — renamed three days later (around 2026-01-30) [6].

Creator: **Peter Steinberger**, Austrian developer [4, 6]. On 2026-02-14 Steinberger announced joining OpenAI, with plans for a non-profit foundation to oversee the project [6, 7].

## Maintainer + activity

| Field | Value | Source |
|---|---|---|
| Maintainer | Peter Steinberger / community / OpenAI-sponsored foundation (in progress) | [4, 6, 7] |
| License | MIT | [4, 6] |
| Primary language(s) | TypeScript (with Swift for macOS/iOS clients) | [4, 6] |
| Star count | 374k stars and 51,743 commits as of 2026-05-23 fetch [4]; 247k stars and 47,700 forks as of 2026-03-02 [6] |
| Status | Active, aggressively iterated | [4, 6] |

Growth from 247k → 374k stars between March and May 2026 indicates rapid adoption.

## Architecture

OpenClaw is **a personal AI assistant**, not a coding sandbox runtime [4, 5]. Its primary user interface is _messaging_ — the agent answers the user "on the channels you already use" (WhatsApp, Telegram, Slack, Discord, Signal, iMessage, and 15+ others) [4].

Operator interaction modes [4]:

- CLI: `openclaw onboard`, `openclaw gateway`, `openclaw agent --message "..."`.
- macOS menu-bar app with voice-wake capability.
- iOS and Android companion apps.
- WebChat browser interface (chat surface, not a terminal).
- Visual "Canvas" workspace rendered by the agent.

A browser is involved only in two distinct ways: (a) the WebChat interface where a human chats with the agent in a browser, and (b) the agent's own headless Chromium sandbox for browser automation tasks. Neither exposes a coding shell.

## Security model

The agent's tool-execution layer runs in Docker sandbox containers with seccomp/namespaces/AppArmor (signal from discovery sub-agent; not deeply verified in-session). The headless browser sandbox for agent automation has had security advisories (auth bypass on sandbox-browser bridge; Chromium launched with `--no-sandbox` in the inner container) attributed to it via sub-agent findings, but the underlying advisory pages were not fetched in this session. Treat those as unverified — see [`citations.md`](../citations.md) §"Sources noted but not verified in-session."

## Deployment story

| Path | Status | Source |
|---|---|---|
| npm/pnpm/bun global install | Recommended (Node ≥22.19 or 24) | [4] |
| Docker | "the default sandbox backend for non-main sessions" | [4] |
| Kubernetes / Helm chart | **No official chart or operator in the upstream repo's README** | [4] |
| Third-party k8s-operator | Exists in `openclaw-rocks/openclaw-operator` (community, unaffiliated) | discovery agent — not verified in-session |

The upstream project does not publish a Kubernetes deployment path. Self-hosted operators must use the npm/Docker paths or the third-party operator (which is in a different GitHub org and not endorsed by the project).

## Access UX (browser-TTY story)

**OpenClaw does not expose a browser-accessible terminal for human users.**

- The TUI / CLI runs on the operator's local machine.
- The WebChat is a messaging interface, not a coding shell.
- The Chromium sandbox is for the agent's browser-automation, not for a human's interactive use.
- The `exec` tool with `pty: true` exists for agent-driven shell exec, not for a human-attached PTY over a browser socket.

## Multi-tenant story

OpenClaw is architecturally **single-user, local-first** [4, 5]. Multi-tenant deployments require one full instance per user (each with its own config, secrets, and storage). The brief's "~12 concurrent sandboxes" pattern does not match OpenClaw's design.

## Verdict

**Unrelated to the framing — discard as a runtime candidate.**

OpenClaw is an autonomous personal AI assistant. It is not a browser-accessible coding sandbox runtime, and it does not have a Kubernetes deployment story endorsed by the upstream maintainers. The brief's question ("which browser-TTY tool + which deployment shape") cannot be answered with OpenClaw.

The only crossover would be using OpenClaw _inside_ a sandbox Pod as the AI agent that runs alongside the developer in the browser-TTY. That is a separate question — what software runs inside the Pod — explicitly out of scope for this research per the brief.

## Gaps and Limitations

- The full README and docs at docs.openclaw.ai were not read end-to-end; profile is built primarily from the GitHub repository landing page [4], the marketing site [5], the Wikipedia article [6], and one creator blog post [7].
- Third-party security advisories attributed to OpenClaw (GHSA-h9g4-589h-68xv, the "ClawJacked" WebSocket hijacking, "Claw Chain" CVEs) were not fetched in this session. Treat as unverified.
- The community `openclaw-rocks/openclaw-operator` Kubernetes operator was discovered by a sub-agent but not profiled directly. If a future revisit treats OpenClaw as worth deploying, this operator should be the first source to verify.
- The `OpenShell` referenced inside OpenClaw documentation (as a sandbox backend) appears to be unrelated to NVIDIA/OpenShell — verify before assuming a relationship.
