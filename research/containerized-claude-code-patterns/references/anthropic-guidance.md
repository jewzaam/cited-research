# Dimension 1 — Anthropic's own guidance for containerized Claude Code

**What this covers:** what Anthropic officially says about running Claude Code in a container, the security model of `--dangerously-skip-permissions`, the stance on unattended/agentic use, and the hosted-sandbox alternatives that may obviate self-hosting altogether.

All facts cite [`citations.md`](../citations.md). Date of research: 2026-05-23.

---

## TL;DR

Anthropic ships an official **dev container reference** ([1], [10], [11], [12]) and explicitly endorses it for `--dangerously-skip-permissions` use, but with a warning that even the dev container does NOT prevent credential exfiltration from a malicious project ([1]). In March 2026 Anthropic introduced **auto mode** as a "safer long-running alternative to `--dangerously-skip-permissions`" ([6], [7]) — using the dangerous flag now runs against Anthropic's own preferred direction. In May 2026 Anthropic launched **Self-Hosted Sandboxes** for Claude Managed Agents ([8]), which moves tool execution into the customer's infrastructure (Cloudflare, Daytona, Modal, Vercel are the named managed providers) while the agent loop stays on Anthropic infrastructure — this is a strict alternative to self-hosting Claude Code in a Pod and may be a better fit if you do not need to run the Claude Code CLI specifically.

## 1.1 Official Anthropic devcontainer reference

Anthropic publishes a working `.devcontainer/` directory at `anthropics/claude-code/.devcontainer/` consisting of three files [1]:

| File | Purpose |
|---|---|
| `Dockerfile` | Base image (`FROM node:20`), dev tools, Claude Code install [10] |
| `devcontainer.json` | Volume mounts, `runArgs` capabilities, `remoteUser`, `postStartCommand` [11] |
| `init-firewall.sh` | iptables/ipset egress allowlist [12] |

Anthropic explicitly describes it as "a working example rather than a maintained base image" [1] — there is no official base image like `ghcr.io/anthropics/claude-code:latest` claimed in some community summaries.

Distribution path: a separate **devcontainer feature** at `ghcr.io/anthropics/devcontainer-features/claude-code:1.0` can be added to any existing devcontainer; the tag pins the feature install script, NOT the Claude Code release [1]. To pin the CLI version in a Dockerfile use `npm install -g @anthropic-ai/claude-code@X.Y.Z` and set `DISABLE_AUTOUPDATER=1` [1].

For the literal Dockerfile, devcontainer.json, and firewall script contents, see [`community-dockerfiles.md`](community-dockerfiles.md) §2.1.

## 1.2 Security model of `--dangerously-skip-permissions` per Anthropic

The flag (also accessible as `--permission-mode bypassPermissions`) disables every permission gate Claude Code would normally enforce [2]. Specifically [2]:

| Check | bypassPermissions | auto mode | Plan / default |
|---|---|---|---|
| File-write prompts | Bypassed | Classifier-reviewed | Prompted |
| Bash command prompts | Bypassed | Classifier-reviewed | Prompted |
| Network-request prompts | Bypassed | Classifier-reviewed | Prompted |
| MCP tool-call prompts | Bypassed | Classifier-reviewed | Prompted |
| Writes to protected paths (`.git`, `.vscode`, `.husky`, `.bashrc`, `.mcp.json`, `.claude.json`, etc.) | **Bypassed** as of v2.1.126 (earlier versions still prompted) | Routed to classifier | Prompted |
| `rm -rf /` and `rm -rf ~` | Still prompts (circuit breaker against model error) | Routed to classifier | Prompted |
| Root/sudo refusal | Refuses to start on Linux/macOS unless inside a recognized sandbox or non-root user | N/A | N/A |

Anthropic's root/sudo refusal message verbatim [2]:

> `--dangerously-skip-permissions cannot be used with root/sudo privileges for security reasons`

This is confirmed reproducible in issue #9184 [15], which was closed without a documented exception path. The check "is skipped automatically inside a recognized sandbox" [2] — in a Kubernetes Pod this means setting `securityContext.runAsNonRoot: true` and `runAsUser: <non-zero UID>`.

Anthropic's stated acceptable use [2] (verbatim):

> Only use this mode in isolated environments like containers, VMs, or dev containers without internet access, where Claude Code cannot damage your host system.

And the warning, also verbatim [1]:

> While the dev container provides substantial protections, no system is completely immune to all attacks. When executed with `--dangerously-skip-permissions`, dev containers do not prevent a malicious project from exfiltrating anything accessible inside the container, including the Claude Code credentials stored in `~/.claude`. Only use dev containers when developing with trusted repositories, and monitor Claude's activities.

The reference firewall script [12] enforces a default-DROP egress policy with a small allowlist (npm registry, `api.anthropic.com`, GitHub IP CIDRs, telemetry endpoints, VS Code marketplace). DNS over UDP/53 and SSH over TCP/22 are allowed. The script's verification step intentionally tries to reach `example.com` and fails-closed if successful [12].

## 1.3 Auto mode — Anthropic's preferred replacement for the dangerous flag (March 2026)

In March 2026 Anthropic introduced **auto mode** explicitly framed as "a safer long-running alternative to `--dangerously-skip-permissions`" [6]. Auto mode uses a two-stage classifier on Sonnet 4.6: a fast single-token filter, then chain-of-thought reasoning if the filter flags [7]. Performance (Anthropic-reported) [7]:

| Dataset | Stage 1 FPR | Stage 1 FNR | Full pipeline FPR | Full pipeline FNR |
|---|---|---|---|---|
| Real traffic (n=10,000) | 8.5% | — | 0.4% | — |
| Real overeager actions (n=52) | 6.6% | — | — | 17% |
| Synthetic exfiltration (n=1,000) | — | 1.8% | — | 5.7% |

**Auto mode availability constraints** [2] — these are critical for a Pod design:

- **Status**: **"research preview"** [2] — Anthropic explicitly flags it as such on the permission-modes docs page. Operators should expect behavior changes and treat it as not-yet-GA.
- **Plan**: All plans
- **Admin**: on Team and Enterprise, an admin must enable it; can lock it off via `permissions.disableAutoMode: "disable"` in managed settings
- **Model**: Claude Sonnet 4.6, Opus 4.6, or Opus 4.7. Sonnet 4.5, Opus 4.5, Haiku, and claude-3 are NOT supported
- **Provider**: **Anthropic API only — not Bedrock, Vertex, or Foundry**

Implication: if you want to use Bedrock/Vertex/IRSA for credential isolation in a Pod, auto mode is unavailable and you fall back to `--dangerously-skip-permissions` (or to manual approval, which defeats unattended use). For unattended Pod use, "auto mode" and "cloud-provider auth" are mutually exclusive.

What auto mode blocks by default, per Anthropic [2]:

- Downloading and executing code (`curl | bash`)
- Sending sensitive data to external endpoints
- Production deploys and migrations
- Mass deletion on cloud storage
- Granting IAM or repo permissions
- Force push, or pushing directly to `main`

What it allows by default [2]:

- Local file ops in working directory
- Installing dependencies declared in lock files
- Reading `.env` and sending credentials to their matching API
- Read-only HTTP requests
- Pushing to the branch you started on or one Claude created

Auto-mode fallback: after 3 consecutive denials or 20 total, auto mode pauses and CC resumes prompting. **In non-interactive mode (`-p`), repeated blocks abort the session** [2] — a real risk for unattended CronJob-style Pods that can run into a denial wall and exit non-zero.

Anthropic's own caveat verbatim [7]: "It is not a drop-in replacement for careful human review on high-stakes infrastructure."

## 1.4 Anthropic's stance on agentic / unattended use

Headless / unattended use is explicitly supported via `claude -p` / `--print` ([2], cross-referenced from [4]). Anthropic recommends:

- Minimum necessary permissions
- Reversible actions preferred over irreversible
- Output verifiable post-hoc
- "Use virtual machines (VMs) to run scripts and make tool calls, especially when interacting with external web services" [3]

Notably, in headless mode "Trust verification is disabled when running non-interactively with the `-p` flag. The exception is `--worktree`, which still requires that trust has been accepted for the directory" [3] — this is the precise condition exploited by the CVE-2025-59536 family (see [`dangerously-skip-permissions.md`](dangerously-skip-permissions.md) §5.2): containerized + headless + clone-untrusted-repo is the worst-possible posture for malicious `.claude/settings.json` hooks.

## 1.5 Hosted-sandbox alternatives — do you need to self-host at all?

The single most important question for this whole research: **does the user need to run the Claude Code CLI specifically, or does an Anthropic-hosted equivalent solve the same problem with less work?**

### 1.5.1 Claude Managed Agents — Self-Hosted Sandboxes (public beta, May 19 2026)

Announced four days before this research (2026-05-19) at Code with Claude London [8]. Architecture (verbatim from [8]):

> The sandbox runs on your own infrastructure, or with managed providers like Cloudflare, Daytona, Modal, or Vercel to handle the compute and isolation for you.

| Layer | Where it runs |
|---|---|
| Agent loop (orchestration, context management, error recovery) | Anthropic infrastructure |
| Tool execution (file management, packages, compute) | Customer infrastructure |

**Notably, Kubernetes is not listed as a directly supported target** [8]. The named providers are Cloudflare, Daytona, Modal, and Vercel. Bringing your own infrastructure (Kubernetes Pod, bare metal) is presented as a path but without an explicit Kubernetes integration guide as of the launch announcement.

MCP Tunnels (research preview, also announced 2026-05-19) lets the managed agent reach internal services without exposing them publicly — "no inbound firewall rules, no public endpoints, and traffic encrypted end to end" [8].

Use cases Anthropic explicitly names: compliance, data residency, security requirements [8].

**Trade-offs vs self-hosting Claude Code CLI in a Pod:**

| Dimension | Managed Agents + Self-Hosted Sandbox | Self-host Claude Code in K8s Pod |
|---|---|---|
| Agent loop | Anthropic-managed | Self-managed |
| Tool execution | Customer-managed | Customer-managed |
| Credential exposure | Tool-side creds only; agent loop never holds them | All creds in Pod |
| Setup effort | Provider account + tunnel setup | Full image build + RBAC + NetworkPolicy + Reloader + … |
| Kubernetes-native | Not explicitly | Yes |
| CLI access for interactive debugging | Via Anthropic's UI/API surface | Via the Pod (e.g., browser TTY) |
| Maturity | Public beta (Day 5 at time of research) | Production-pattern Dockerfile available since 2024 |
| Per-token billing | Same Anthropic API rates | Same rates, plus harness-detection risk [17] |

If the operator goal is "Claude agent runs my tools safely" rather than specifically "Claude Code CLI runs in my container," Self-Hosted Sandboxes is the lighter path. If the goal explicitly requires the CLI (e.g., for `claude -p` invocation patterns, browser-TTY operator access, MCP servers configured in `.mcp.json`), self-hosting the Pod remains the right answer.

### 1.5.2 Claude Code on the Web

Anthropic also offers "Claude Code on the Web" — an Anthropic-managed VM per task, with the GitHub repo cloned into the VM, isolated execution, and credentials kept out of the sandbox via a custom proxy that translates a scoped credential to the user's actual GitHub token [3], [43a]. Per [3]: "Git push operations are restricted to the current working branch." This is arguably the lowest-friction safe path for "I want Claude to open PRs against my own repos and nothing else" — assuming the integration with the operator's existing workflow is acceptable.

### 1.5.3 Sculptor (third-party)

Imbue ships **Sculptor**, a Mac desktop app that runs parallel Claude Code agents in isolated Docker containers per agent, using the user's own Claude Code subscription or API key [42a]. Free in beta as of May 2026. Useful for multi-session workflows on a workstation but it does not address the K8s Pod scenario.

### 1.5.4 Other hosted developer sandboxes

Independent of Anthropic, several vendor sandboxes have emerged for AI-driven code execution (Daytona, Modal, Vercel sandboxes, Cloudflare microVMs). These are the same names Anthropic lists as Self-Hosted Sandbox providers [8]; using one directly without Anthropic's agent loop is a separate architectural path that this research does not survey in depth — see the separate hosted-coding-sandbox-survey research run if one was performed.

## 1.6 Gaps and limitations

- **`ghcr.io/anthropics/claude-code` image:** community sources mention an official image at this path but Anthropic's own docs describe only the devcontainer-features image `ghcr.io/anthropics/devcontainer-features/claude-code:1.0` [1]. No evidence of a published runnable base image for production K8s pods was confirmed in the iter-2 fetches. Treat any claim of an "official Anthropic Docker image" as community shorthand for the reference devcontainer.
- **Self-Hosted Sandboxes Kubernetes guide:** does not exist as of 2026-05-23. Anthropic's docs only enumerate the four managed providers. Adapting to a Pod is "BYO" but not documented end-to-end.
- **Anthropic on root in containers:** the docs say the root check "is skipped automatically inside a recognized sandbox" [2] but do not enumerate which sandbox detectors trigger this. Empirically the only documented escape is "run as non-root inside the container," which is what the reference devcontainer does (`remoteUser: "node"`, UID-from-base-image).
- **`--dangerously-skip-permissions` post-CVE story:** Anthropic's docs page on permission modes [2] continues to list `bypassPermissions` as an available mode without any reference to the CVE-2025-66479 / SOCKS5 / CVE-2025-59536 history. Anthropic positions auto mode as the recommended replacement [6] but does not deprecate the dangerous flag.
- **Auto mode + Bedrock / Vertex:** the explicit "Anthropic API only" constraint [2] is decisive for K8s deployments that want cloud-provider credential isolation. There is no documented workaround.
