# Dimension 2 — Community Dockerfiles + deployment patterns

**What this covers:** the canonical reference Dockerfile and devcontainer.json (Anthropic-published), community Kubernetes patterns, base-image choices, install methods, and the documented footguns specific to running Claude Code in a container.

All facts cite [`citations.md`](../citations.md). Date of research: 2026-05-23.

---

## TL;DR

The highest-quality reference Dockerfile is **Anthropic's own** at `anthropics/claude-code/.devcontainer/Dockerfile` [10]. It uses `node:20`, a non-root `node` user, npm-global install of `@anthropic-ai/claude-code`, and a passwordless-sudo escape narrowly scoped to running the iptables firewall script. For Kubernetes specifically there are no Anthropic-official manifests; the canonical community pattern is **Daniel Hnyk's CronJob** [14] using `nikolaik/python-nodejs:python3.13-nodejs22`, `envFrom: secretRef` for the API key, and `claude -p --dangerously-skip-permissions --verbose --output-format stream-json` as the invocation. Several footguns are documented: the root-user block on the dangerous flag [15], the OAuth-from-container failure [4], heavy memory usage that mandates a hard `NODE_OPTIONS: --max-old-space-size` cap [11], the `~/.claude` two-file persistence requirement, and the npm-vs-native-installer transition.

## 2.1 The reference Dockerfile, devcontainer.json, and firewall — verbatim

These are the canonical Anthropic-shipped files. Reproduced here because the prompt asks for "the most-referenced or highest-quality reference Dockerfile pattern verbatim if one exists."

### 2.1.1 `Dockerfile` ([10])

```dockerfile
FROM node:20

ARG TZ
ENV TZ="$TZ"

ARG CLAUDE_CODE_VERSION=latest

# Install basic development tools and iptables/ipset
RUN apt-get update && apt-get install -y --no-install-recommends \
  less git procps sudo fzf zsh man-db unzip gnupg2 gh \
  iptables ipset iproute2 dnsutils aggregate jq nano vim \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

# Ensure default node user has access to /usr/local/share
RUN mkdir -p /usr/local/share/npm-global && \
  chown -R node:node /usr/local/share

ARG USERNAME=node

# Persist bash history.
RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" \
  && mkdir /commandhistory \
  && touch /commandhistory/.bash_history \
  && chown -R $USERNAME /commandhistory

ENV DEVCONTAINER=true

# Create workspace and config directories and set permissions
RUN mkdir -p /workspace /home/node/.claude && \
  chown -R node:node /workspace /home/node/.claude

WORKDIR /workspace

ARG GIT_DELTA_VERSION=0.18.2
RUN ARCH=$(dpkg --print-architecture) && \
  wget "https://github.com/dandavison/delta/releases/download/${GIT_DELTA_VERSION}/git-delta_${GIT_DELTA_VERSION}_${ARCH}.deb" && \
  sudo dpkg -i "git-delta_${GIT_DELTA_VERSION}_${ARCH}.deb" && \
  rm "git-delta_${GIT_DELTA_VERSION}_${ARCH}.deb"

USER node

ENV NPM_CONFIG_PREFIX=/usr/local/share/npm-global
ENV PATH=$PATH:/usr/local/share/npm-global/bin
ENV SHELL=/bin/zsh
ENV EDITOR=nano
ENV VISUAL=nano

ARG ZSH_IN_DOCKER_VERSION=1.2.0
RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v${ZSH_IN_DOCKER_VERSION}/zsh-in-docker.sh)" -- \
  -p git -p fzf \
  -a "source /usr/share/doc/fzf/examples/key-bindings.zsh" \
  -a "source /usr/share/doc/fzf/examples/completion.zsh" \
  -a "export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" \
  -x

# Install Claude
RUN npm install -g @anthropic-ai/claude-code@${CLAUDE_CODE_VERSION}

# Copy and set up firewall script
COPY init-firewall.sh /usr/local/bin/
USER root
RUN chmod +x /usr/local/bin/init-firewall.sh && \
  echo "node ALL=(root) NOPASSWD: /usr/local/bin/init-firewall.sh" > /etc/sudoers.d/node-firewall && \
  chmod 0440 /etc/sudoers.d/node-firewall
USER node
```

### 2.1.2 `devcontainer.json` ([11])

```json
{
  "name": "Claude Code Sandbox",
  "build": {
    "dockerfile": "Dockerfile",
    "args": {
      "TZ": "${localEnv:TZ:America/Los_Angeles}",
      "CLAUDE_CODE_VERSION": "latest",
      "GIT_DELTA_VERSION": "0.18.2",
      "ZSH_IN_DOCKER_VERSION": "1.2.0"
    }
  },
  "runArgs": ["--cap-add=NET_ADMIN", "--cap-add=NET_RAW"],
  "remoteUser": "node",
  "mounts": [
    "source=claude-code-bashhistory-${devcontainerId},target=/commandhistory,type=volume",
    "source=claude-code-config-${devcontainerId},target=/home/node/.claude,type=volume"
  ],
  "containerEnv": {
    "NODE_OPTIONS": "--max-old-space-size=4096",
    "CLAUDE_CONFIG_DIR": "/home/node/.claude",
    "POWERLEVEL9K_DISABLE_GITSTATUS": "true"
  },
  "workspaceMount": "source=${localWorkspaceFolder},target=/workspace,type=bind,consistency=delegated",
  "workspaceFolder": "/workspace",
  "postStartCommand": "sudo /usr/local/bin/init-firewall.sh",
  "waitFor": "postStartCommand"
}
```

### 2.1.3 `init-firewall.sh` ([12])

Allowlisted domains, verbatim:

```
registry.npmjs.org
api.anthropic.com
sentry.io
statsig.anthropic.com
statsig.com
marketplace.visualstudio.com
vscode.blob.core.windows.net
update.code.visualstudio.com
```

Plus GitHub IP CIDRs fetched dynamically from `https://api.github.com/meta` (web + api + git), plus DNS UDP/53, SSH TCP/22, loopback, host network /24, and ESTABLISHED/RELATED state. Default-DROP policy on INPUT/OUTPUT/FORWARD. Verification step at the end confirms `example.com` is unreachable and `api.github.com/zen` is reachable. Full script in [12].

## 2.2 Base image selection

The Anthropic reference uses `FROM node:20` (the full Debian Bookworm image) [10] rather than `node:20-slim` or `node:20-alpine`. Trade-offs from community sources:

| Base | Pros | Cons |
|---|---|---|
| `node:20` (full Debian) | Has all the tools the reference uses (iptables, ipset, dnsutils, jq, etc.) | ~487 MB layer; longer pulls |
| `node:20-slim` / `node:22-slim` | ~280 MB possible; smaller cache footprint | Must install iptables, ipset, jq, dnsutils, gh, etc. yourself |
| `node:20-alpine` / `node:22-alpine` | Smallest | musl libc breaks some native npm modules used by Claude Code (community-reported); not used by the reference |
| `nikolaik/python-nodejs:python3.13-nodejs22` | Python + Node in one image (needed for skills that invoke Python) | Larger than node-only |

The Hnyk CronJob pattern [14] uses `nikolaik/python-nodejs:python3.13-nodejs22` specifically because the example skills are Python.

Node version notes: Node 20 is the current Anthropic-pinned version [10]. Node 20 reaches end-of-life in April 2026; the reference Dockerfile had not been updated to Node 22 as of 2026-05-23 [10].

## 2.3 Install method: npm vs native installer

The reference Dockerfile uses `npm install -g @anthropic-ai/claude-code@${CLAUDE_CODE_VERSION}` [10]. Anthropic offers an alternative native installer (`curl -fsSL https://claude.ai/install.sh | bash`) that bypasses npm entirely; whether this is preferable depends on whether you also want gh, git, jq, etc. in the same image. The reference Dockerfile still uses npm install; no public update to the native installer in the reference repo was confirmed in iter-2 fetches.

Version pinning: omit the `:latest` tag in production. Pin via `CLAUDE_CODE_VERSION` ARG or directly in `RUN npm install -g @anthropic-ai/claude-code@X.Y.Z` and set `DISABLE_AUTOUPDATER=1` per [1]. Without pinning, the in-Pod CLI will auto-update behind the operator's back.

## 2.4 Kubernetes deployment patterns

### 2.4.1 The CronJob pattern ([14])

Daniel Hnyk's published K8s pattern for long-running marketing jobs:

```yaml
apiVersion: batch/v1
kind: CronJob
spec:
  schedule: "0 8 * * 1-5"
  concurrencyPolicy: Forbid
  jobTemplate:
    spec:
      activeDeadlineSeconds: 14400  # 4 hours
      backoffLimit: 1
      template:
        spec:
          restartPolicy: Never
          containers:
          - name: claude
            image: nikolaik/python-nodejs:python3.13-nodejs22
            envFrom:
              - secretRef:
                  name: claudie-secrets
            resources:
              requests: { cpu: 100m, memory: 512Mi }
              limits:   { cpu: 2,    memory: 4Gi   }
            command: ["/bin/bash", "-c"]
            args:
              - |
                timeout 10800 bash -c 'claude -p --dangerously-skip-permissions --verbose \
                  --output-format stream-json -- "$SKILL_PROMPT"'
                if [ $? -eq 124 ]; then
                  # Backup claude run to collect partial state
                  claude -p --dangerously-skip-permissions -- "what was completed?"
                fi
```

Key choices from [14]:

- **`envFrom: secretRef`** for API key + GitHub token (env-var injection — see [`api-key-injection.md`](api-key-injection.md) §3.2 for trade-offs)
- **`{"hasCompletedOnboarding": true}` in `~/.claude.json`** baked into the image to skip interactive setup in non-TTY environments
- **`timeout 10800`** wrapper to catch agent loops
- **`concurrencyPolicy: Forbid`** to avoid the rate-limit pileup described in [`api-key-injection.md`](api-key-injection.md) §3.3
- **gh CLI configured in entrypoint** so skills can `gh pr create` directly

### 2.4.2 The standalone-Docker pattern ([13])

For non-CronJob, non-VS-Code use, Software Thug's approach [13] is to sparse-clone Anthropic's upstream `.devcontainer/` directory, patch `init-firewall.sh` to allow a dev-server port range (`iptables -A INPUT -p tcp --dport 3000:9000 -j ACCEPT`), and invoke via the devcontainer CLI rather than `docker run` directly. Authentication persists in a Docker named volume kept deliberately separate from host credentials [13].

### 2.4.3 Reusable Pod-level resource settings

From [11] and [14], the K8s-translated equivalent of the reference devcontainer's resource controls:

| Setting | Value | Source |
|---|---|---|
| `NODE_OPTIONS` | `--max-old-space-size=4096` | [11] |
| Pod `securityContext.runAsNonRoot` | `true` | required for `--dangerously-skip-permissions` per [2], [15] |
| Pod `securityContext.runAsUser` | `1000` (the `node` user from Debian) | implied by [10] |
| `resources.limits.memory` | 4Gi (`14` uses this; matches Node `--max-old-space-size`) | [14] |
| Linux capabilities | `NET_ADMIN`, `NET_RAW` (only if running in-Pod iptables; not required if you use NetworkPolicy externally) | [1], [11] |

For NetworkPolicy translation of the egress allowlist, see [`dangerously-skip-permissions.md`](dangerously-skip-permissions.md) §5.3.

## 2.5 Known footguns

### 2.5.1 Root-user block (the #1 footgun for K8s)

`--dangerously-skip-permissions` refuses to start as root with the message:

> `--dangerously-skip-permissions cannot be used with root/sudo privileges for security reasons`

Confirmed in issue #9184 [15] and documented in [2]. The check "is skipped automatically inside a recognized sandbox" [2] — empirically the canonical workaround in K8s is `securityContext.runAsUser` set to a non-zero UID matching a user that exists in the image (UID 1000 for the `node` user in `node:20`). The reference devcontainer sets `remoteUser: "node"` for exactly this reason [11].

### 2.5.2 OAuth doesn't work from a container

From the official auth docs [4]:

> If your browser shows a login code instead of redirecting back after you sign in, paste it into the terminal at the 'Paste code here if prompted' prompt. This happens when the browser can't reach Claude Code's local callback server, which is common in WSL2, SSH sessions, and containers.

For an unattended Pod with no terminal operator, the OAuth flow is unusable. Only headless-compatible auth modes work: `ANTHROPIC_API_KEY` env var, `CLAUDE_CODE_OAUTH_TOKEN` from a pre-generated `claude setup-token`, cloud-provider auth (`CLAUDE_CODE_USE_BEDROCK=1` + AWS creds via IRSA), or `apiKeyHelper`. Details in [`api-key-injection.md`](api-key-injection.md) §3.1.

### 2.5.3 Memory: documented unbounded growth

Heavy memory consumption is reported widely; the reference devcontainer caps Node heap at 4 GB via `NODE_OPTIONS: "--max-old-space-size=4096"` [11], and the Hnyk K8s pattern matches with `resources.limits.memory: 4Gi` [14]. Without the cap, agent loops in large repos can exhaust container memory and trigger OOMKill. Always pair `NODE_OPTIONS` with a Pod-level memory limit.

### 2.5.4 `~/.claude` persistence requires two files

The Anthropic devcontainer mounts a named volume at `/home/node/.claude` to persist auth across rebuilds [1], [11]. Community reports confirm that BOTH `~/.claude/.credentials.json` AND `~/.claude.json` (the dotfile at the user's home, not inside `~/.claude/`) must be persisted for auth to survive — losing `.claude.json` triggers a full re-login flow regardless of valid credentials. The reference mount only covers `/home/node/.claude/`; for `~/.claude.json` persistence at the project-isolated level, an additional volume or a `setup-token`-derived `CLAUDE_CODE_OAUTH_TOKEN` env var is required.

If mounting somewhere other than `~/.claude`, set `CLAUDE_CONFIG_DIR` to the mount path [1] — the reference devcontainer does this explicitly: `CLAUDE_CONFIG_DIR=/home/node/.claude` [11].

### 2.5.5 MCP servers inside the same container

The reference devcontainer treats MCP servers as project-scope: define them in a `.mcp.json` at the repo root checked into source control [1]. Stdio-based MCP servers (the default transport) run as child processes of Claude Code and share the container's filesystem and network — fine for trusted MCP servers, but means a compromised MCP server has the same access as the agent.

Important security note from Check Point Research [26]: a malicious project can place `enableAllProjectMcpServers: true` in `.claude/settings.json` and auto-initialize MCP servers without user consent — and this fires **before** the trust dialog completes. In a headless container with `-p`, the trust dialog never appears at all [3].

### 2.5.6 The `init-firewall.sh` overwrite footgun (devcontainer features)

The `ghcr.io/anthropics/devcontainer-features/claude-code:1.0` feature [1] installs its own `init-firewall.sh` to `/usr/local/bin/init-firewall.sh`. If your existing devcontainer has a script with the same name there, the feature silently overwrites it. Mitigation: use a different filename (e.g., `project-firewall.sh`) and update `postStartCommand` accordingly.

### 2.5.7 The auto-updater can desync your image

By default Claude Code auto-updates inside the container [1]. To pin in a Dockerfile: install via `npm install -g @anthropic-ai/claude-code@X.Y.Z` AND set `DISABLE_AUTOUPDATER=1` in `containerEnv` or `ENV` [1]. Without `DISABLE_AUTOUPDATER`, your pinned image can run a different CLI version than you built.

### 2.5.8 Anthropic harness detection on git state ([17])

Detection scans git-status content (which includes staged changes, branch state, and recent commit information) for keywords like `hermes.md` and `OpenClaw` per [17]. False positives have caused subscription users to be silently billed at API rates (the $200.98 On Patel incident [17]). For a Pod with `ANTHROPIC_API_KEY`, this likely does not apply (you're already on API billing), but if you ever switch to `CLAUDE_CODE_OAUTH_TOKEN` for subscription consumption, audit the Pod's git state first. See [`api-key-injection.md`](api-key-injection.md) §3.5 for full treatment.

## 2.6 Image size and cold-start (no reliable data found)

The prompt asked for image-size and cold-start numbers if found. The reference Dockerfile [10] without optimisation produces an image of approximately 1.0–1.5 GB based on the `FROM node:20` base + the apt package list, but **no Anthropic-published or independently verified number was confirmed** in the iter-2 fetches. Community summaries claim figures (~487 MB compressed, 15–37 s cold start for minimal images, 30–60 s for full CC containers) but these were from tier-3/4 search snippets not directly fetched. Treat any specific image-size or cold-start number from the literature as "no Anthropic-confirmed figure" until you measure your own build.

## 2.7 Gaps and limitations

- **Image size numbers**: no first-party data; community figures were not directly verified.
- **Native installer in container**: appears in tier-3 sources but the official reference Dockerfile [10] still uses npm; whether the native installer in a Pod has the same OAuth fragility as npm-installed CC was not confirmed.
- **`@anthropic-ai/claude-code` SDK in containers**: counter-discovery found community reports of `spawn node ENOENT` errors when the Agent SDK is invoked inside Docker — not directly verified in iter 2; if you plan to drive Claude Code programmatically from inside a Pod (rather than using the CLI), verify this against the latest SDK before committing to a design.
- **MCP server transports in K8s**: stdio MCP servers as child processes are well-documented; HTTP/SSE MCP servers as sidecar containers in the same Pod are mentioned but not detailed in iter-2 fetches. Service-mesh sidecar interaction (Istio, Linkerd) with the egress allowlist is not addressed in any fetched source.
- **`ghcr.io/anthropics/claude-code` published image**: claimed by some community sources but no Anthropic doc confirms a runnable base image of this name. The only ghcr.io path Anthropic publishes is the devcontainer feature.
