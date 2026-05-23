# Containerized Claude Code patterns + GitHub auth scoping

Research date: 2026-05-23.
All factual claims cite [`citations.md`](citations.md). Counter-perspective handling: Find-and-gate (user gated through to deliverable after iter 1 — see §0 for gating findings).

---

## Overview (≤200 words)

The asker wants to host Claude Code inside a Kubernetes Pod where `--dangerously-skip-permissions` is acceptable because the Pod has no host FS, no LAN reach, and only narrowly-scoped credentials. Operator access via browser TTY (out of scope). The research finds: **(a)** Anthropic has shipped two paths that may obviate this work — Self-Hosted Sandboxes for Managed Agents (May 19 2026, [8]) and auto mode (March 2026, [6], [7]) which is "a safer long-running alternative to `--dangerously-skip-permissions`"; **(b)** Anthropic's own network sandbox was bypassed twice in 2025-2026 ([24], [25]) and a malicious `.claude/settings.json` can RCE + exfil the API key before the trust dialog completes ([26]) — the dangerous flag's intended-safe environments are themselves under active research attack; **(c)** for GitHub auth, a private GitHub App is structurally lower-blast-radius than a fine-grained PAT or fork-account ([20] vs [22], [23]); **(d)** Pod-level "no LAN reach" requires explicit NetworkPolicy, `automountServiceAccountToken: false`, IMDS blocking, and a non-root user — none of which K8s does by default ([28], [29]). Per user direction, the recommended primary path is **auto mode in a hardened Pod**, with `--dangerously-skip-permissions` reserved only for Bedrock/Vertex auth (which loses auto mode per [2]).

---

## 0. Gating findings (read these first)

These were surfaced to the user before iter 2 per "Find-and-gate" counter-perspective handling. They reframe the prompt.

1. **Anthropic auto mode (March 2026) is the recommended replacement for `--dangerously-skip-permissions`** [6], [7]. User has accepted the swap. The deliverable's recommended path is auto mode in the Pod, not the dangerous flag.

2. **Anthropic Managed Agents — Self-Hosted Sandboxes (May 19 2026, public beta)** [8] separates orchestration (Anthropic-side) from tool execution (customer-side), with supported managed providers Cloudflare, Daytona, Modal, Vercel. **Kubernetes is not listed as a directly-supported target.** If the operator goal is "Claude agent runs my tools safely" rather than specifically "Claude Code CLI runs in my container," this is the lighter path. If the goal requires CLI features (`-p` invocation, browser-TTY operator, `.mcp.json`), self-hosting remains the right answer.

3. **`--dangerously-skip-permissions` appears verbatim in malware payloads.** The s1ngularity supply-chain attack (Aug 26 2025) explicitly passes this flag to Claude Code / Gemini CLI / Amazon Q for unattended credential exfiltration [16]. Using the flag is no longer just "be careful" — it's a documented attacker primitive.

4. **Anthropic's own network sandbox was broken for ~5.5 months.** Two distinct bugs, non-overlapping patch windows: **CVE-2025-66479** (`allowedDomains: []` logic inversion) [24] affected Claude Code from Nov 2025 launch through v2.0.54, patched in v2.0.55. **SOCKS5 null-byte injection** (no CVE) [25] affected from sandbox GA (Oct 20 2025) through the v2.1.88 patch (Mar 31 2026) — ~5.5 months, ~130 releases. Both were silently patched without security advisories. Treat in-container Claude Code sandbox controls as defense-in-depth, not primary.

5. **TrustFall + CVE-2025-59536 + CVE-2026-21852** [26] — cloning a malicious repo with `.claude/settings.json` hooks achieves RCE and API-key exfil **before the trust dialog completes**. In headless `-p` mode the trust dialog never appears [3], making containerized + headless the **worst-case configuration** for this attack family.

6. **Anthropic harness-detection billing trap (April 2026 → structural June 15 2026).** Anthropic scans git status for harness keywords; subscription accounts have been silently routed to API billing with $200+ surprise charges [17]. From June 15 2026, `claude -p` on subscription plans draws from a separate Agent SDK credit with overages at full API rates [4]. For a Pod authenticating with `ANTHROPIC_API_KEY` (API billing already), this is moot — but operators using `CLAUDE_CODE_OAUTH_TOKEN` for subscription consumption need to verify the Pod's git history has no harness markers.

7. **OWASP Top 10 for Agentic Applications 2026** [41a] explicitly classifies standard containers as insufficient for production AI agents with code execution; recommends Firecracker, gVisor, or Kata Containers. Three runc CVEs in November 2025 simultaneously broke containerd/Docker/K8s/CRI-O containment.

8. **Schneier on prompt injection** [30] (verbatim): "There is no privilege separation, and there is no separation between the data and control paths." "Prompt injection might be unsolvable in today's LLMs." Container isolation is an OS-level boundary; prompt injection is an instruction-level attack. They are on different layers.

---

## 1. Anthropic's own guidance for containerized Claude Code

Full treatment in [`references/anthropic-guidance.md`](references/anthropic-guidance.md).

### Reference devcontainer

Anthropic publishes a working `.devcontainer/` directory ([1], [10], [11], [12]) consisting of:
- A Dockerfile (`FROM node:20`, non-root `node` user, npm install of `@anthropic-ai/claude-code`)
- A `devcontainer.json` (named volumes for `~/.claude` and bash history per `${devcontainerId}`, `NODE_OPTIONS: --max-old-space-size=4096`, `CLAUDE_CONFIG_DIR=/home/node/.claude`, `runArgs: [--cap-add=NET_ADMIN, --cap-add=NET_RAW]`)
- An `init-firewall.sh` (default-DROP iptables policy + allowlist of npm registry, `api.anthropic.com`, GitHub IP CIDRs, telemetry/marketplace; verifies `example.com` is unreachable)

Anthropic describes it explicitly as "a working example rather than a maintained base image" [1]. There is no published `ghcr.io/anthropics/claude-code` runnable base image — only the devcontainer-feature image `ghcr.io/anthropics/devcontainer-features/claude-code:1.0` [1].

### What `--dangerously-skip-permissions` actually does (per Anthropic)

Disables every interactive prompt — file writes, Bash commands, network, MCP — and as of v2.1.126 also writes to protected paths [2]. Keeps only the `rm -rf /` / `rm -rf ~` circuit breaker and the root/sudo refusal. Anthropic's verbatim warning [1]:

> When executed with `--dangerously-skip-permissions`, dev containers do not prevent a malicious project from exfiltrating anything accessible inside the container, including the Claude Code credentials stored in `~/.claude`.

### Auto mode (preferred replacement)

Introduced March 24 2026 [6]. Two-stage Sonnet 4.6 classifier (fast token filter + chain-of-thought) [7]. Performance per [7]:

| Dataset | Stage 1 FPR | Stage 1 FNR | Full pipeline FPR | Full pipeline FNR |
|---|---|---|---|---|
| Real traffic (n=10K) | 8.5% | — | 0.4% | — |
| Real overeager (n=52) | 6.6% | — | — | 17% |
| Synthetic exfil (n=1K) | — | 1.8% | — | 5.7% |

Anthropic's caveat: "It is not a drop-in replacement for careful human review on high-stakes infrastructure" [7]. **Anthropic labels auto mode a "research preview"** [2] — operators should plan for behavior changes. **Constraints:** Sonnet 4.6 / Opus 4.6 / 4.7 only; **Anthropic API only — not Bedrock, Vertex, or Foundry** [2]. For unattended Pod use, "auto mode" and "cloud-provider auth" are mutually exclusive.

### Hosted alternatives that may obviate self-hosting

- **Self-Hosted Sandboxes** for Claude Managed Agents — public beta May 19 2026 [8]. Cloudflare, Daytona, Modal, Vercel as named providers. Kubernetes not directly listed. Agent loop stays Anthropic-side; tools run customer-side.
- **Claude Code on the Web** [3], [43a] — Anthropic-managed VM per task, isolated git credential via proxy, branch restriction to current working branch.
- **Sculptor** [42a] — Mac desktop app; out of scope for K8s.

---

## 2. Community Dockerfiles and Kubernetes deployment patterns

Full treatment in [`references/community-dockerfiles.md`](references/community-dockerfiles.md).

### The reference Dockerfile (Anthropic, verbatim in §2.1 of the reference file)

`FROM node:20` + apt packages for iptables/ipset/jq/dig/gh + non-root `node` user + npm-global Claude Code install + passwordless-sudo scoped only to the firewall script [10]. The devcontainer.json caps Node heap at 4 GB [11].

### The canonical K8s pattern (Hnyk CronJob, [14])

```yaml
kind: CronJob
spec:
  schedule: "0 8 * * 1-5"
  concurrencyPolicy: Forbid
  jobTemplate:
    spec:
      activeDeadlineSeconds: 14400
      backoffLimit: 1
      template:
        spec:
          restartPolicy: Never
          containers:
          - name: claude
            image: nikolaik/python-nodejs:python3.13-nodejs22
            envFrom:
            - secretRef: { name: claudie-secrets }
            resources:
              limits: { cpu: 2, memory: 4Gi }
            command: ["/bin/bash", "-c"]
            args:
            - timeout 10800 bash -c 'claude -p --dangerously-skip-permissions --verbose --output-format stream-json -- "$SKILL_PROMPT"'
```

Key choices [14]: `envFrom: secretRef` for credentials (envs visible in `kubectl describe pod` — see §3); `{"hasCompletedOnboarding": true}` baked into `~/.claude.json`; `timeout` wrapper for runaway protection; `concurrencyPolicy: Forbid` to avoid rate-limit pile-up.

### Footguns (top five)

1. **Root user block** — `--dangerously-skip-permissions` refuses to start as root [15]; `securityContext.runAsNonRoot: true` + `runAsUser: 1000` is mandatory.
2. **OAuth doesn't work in containers** [4] — only `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, `CLAUDE_CODE_OAUTH_TOKEN` (pre-generated), `apiKeyHelper`, or cloud-provider auth are viable.
3. **Memory** — pair `NODE_OPTIONS: --max-old-space-size=4096` [11] with `resources.limits.memory: 4Gi` [14] or be OOMKilled.
4. **`~/.claude` persistence requires two files** — both `.credentials.json` AND the home-level `.claude.json` must persist or auth resets on rebuild.
5. **Auto-updater** — pin `@X.Y.Z` AND set `DISABLE_AUTOUPDATER=1` [1] or your built image silently runs a different CLI version at runtime.

### Image size and cold start

No first-party data found. Community figures (~487 MB compressed; 15–60 s cold start) were not independently verified. Measure your own build.

---

## 3. Anthropic API key injection

Full treatment in [`references/api-key-injection.md`](references/api-key-injection.md).

### Auth-mode precedence (verbatim from [4])

1. Cloud provider (`CLAUDE_CODE_USE_BEDROCK=1` etc.)
2. `ANTHROPIC_AUTH_TOKEN` env (gateway/proxy)
3. `ANTHROPIC_API_KEY` env (direct API)
4. `apiKeyHelper` script
5. `CLAUDE_CODE_OAUTH_TOKEN` env (subscription, ~1 year)
6. Interactive `/login` (broken in containers)

### Secret injection in K8s

| Pattern | Surface | Use when |
|---|---|---|
| `envFrom: secretRef` (envvar) | Exposed in `kubectl describe pod`, `/proc/<pid>/environ`, child processes | Smallest setup; acceptable if Pod is short-lived and namespace-RBAC tight |
| Projected Secret volume + entrypoint exports env from file | Not in `kubectl describe`; readable only by container user; not in subprocess env unless re-exported | Recommended for long-running Pods |
| `apiKeyHelper` reading file | Refreshes on HTTP 401; cleanest in-process rotation | Best for rotation-sensitive deployments |
| Cloud-provider auth (IRSA / Workload Identity) | No static key in the Pod at all | Best for AWS/GCP-native deployments; **loses auto mode** [2] |

### Rate limits (per organization, NOT per key) [9]

For Sonnet 4.x [9]:

| Tier | Spend | RPM | ITPM | OTPM |
|---|---|---|---|---|
| 1 | $5 | 50 | 30,000 | 8,000 |
| 2 | $40 | 1,000 | 450,000 | 90,000 |
| 3 | $200 | 2,000 | 800,000 | 160,000 |
| 4 | $400 | 4,000 | 2,000,000 | 400,000 |

**Minting N keys does NOT raise aggregate limits** — limits are per-org [9]. Cache-aware ITPM (cached reads don't count [9]) gives a free 5–10× headroom and is the best lever for N-Pod scaling.

### Harness detection + dual-bucket billing

Harness detection [17] scans git status for `hermes.md` / `OpenClaw` and silently switches subscription accounts to API billing. June 15 2026 [4] formally separates Agent SDK / `claude -p` usage into a separate billing pool with $2,000/day overage cap per [44a]. **For a Pod with `ANTHROPIC_API_KEY` this is moot** (already on API billing). For `CLAUDE_CODE_OAUTH_TOKEN` (subscription) Pods, audit git history before deploying.

### Bedrock / Vertex for AWS-native deployments [5]

Set `CLAUDE_CODE_USE_BEDROCK=1` + `AWS_REGION`; attach IRSA-bound IAM policy with `bedrock:InvokeModel`, `bedrock:InvokeModelWithResponseStream`, `bedrock:ListInferenceProfiles`, `bedrock:GetInferenceProfile`. No static Anthropic key. **Trade-off: no auto mode** [2].

---

## 4. GitHub access scoping — Verdict: GitHub App

Full treatment in [`references/github-access-scoping.md`](references/github-access-scoping.md).

### Comparison

| Dimension | Pattern A — fine-grained PAT | Pattern B — second account | Pattern C — GitHub App |
|---|---|---|---|
| Credential lifetime | ≤366 days [21] | ≤366 days [21] | **1 hour** (installation token) [20] |
| Work-repo isolation | Token scoping (fragile per UI bug [22]) | Account boundary (structural) | App install scope (structural) |
| Blast radius on leak | All scoped repos, ≤366 days; UI bug → all personal repos | Account B repos, ≤366 days | Installed repos, ≤1h per token |
| ToS compliance | Compliant [21] | Gray zone — machine-account-only OR ban risk [23] | Compliant [20] |
| Identity | Human (commits credit user) | Second account (reviewer confusion) | `app-name[bot]` (clear) |
| Setup time | ~5 min | ~20 min + ongoing | ~10–15 min |
| Rotation burden | Manual ≤366 days; UI bug risk | Manual ≤366 days × N | Auto via Octokit; rare PEM rotation |

### Recommendation

**Use a private GitHub App.** Three structural reasons:

1. Token lifetime is two to three orders of magnitude shorter than a PAT [20] vs [21]
2. Work-repo isolation is structural — a private App installed only on personal repos cannot reach the user's work org because the App isn't installed there
3. Identity is clearly bot (`app-name[bot]`) — disambiguates AI work from human work

### Setup ([20], [19])

1. Register a private GitHub App ("Only on this account" visibility) under the user's personal account
2. Permissions: Contents=write, Pull requests=write, Metadata=read [19]
3. Install only on personal repos at install time
4. Store the PEM in a K8s Secret using projected-volume file mount (per §3)
5. Pod entrypoint mints a 1-hour installation token at session start via JWT + `POST /app/installations/{install_id}/access_tokens`, scoped via `repository_ids` to the working repo [20]
6. Pass the token to `gh` / `git` via `GITHUB_TOKEN` env var

### Pattern A only acceptable if

Operator commits to **never editing the PAT after creation**. The silent-reset UI bug [22] makes any subsequent edit a privilege-escalation event. Unresolved as of 2026-05-23. For a long-lived sandbox, this risk dominates.

### Pattern B not recommended for sandbox use

ToS gray zone if used interactively [23]; PR-from-fork CI-approval friction for AI-generated PRs; double-identity maintenance. The isolation property is real but Pattern C achieves it with less ergonomic cost.

---

## 5. `--dangerously-skip-permissions` and broader sandbox security

Full treatment in [`references/dangerously-skip-permissions.md`](references/dangerously-skip-permissions.md).

### What it disables

Every interactive prompt — file writes, Bash, network, MCP, protected paths (as of v2.1.126) [2]. Keeps the `rm -rf /` / `rm -rf ~` circuit breaker and the root/sudo refusal. **Cannot be combined with auto mode** (they are mutually exclusive permission modes).

### Documented attack surfaces (3 CVE families)

1. **CVE-2025-66479** [24] — `allowedDomains: []` logic inversion disabled network restrictions. Affected: Nov 2025 launch through v2.0.54. Patched v2.0.55 with changelog "Fixed proxy DNS resolution" (no security mention). CVE assigned to library, not Claude Code.
2. **SOCKS5 null-byte injection** (no CVE) [25] — `attacker.com\x00.google.com` bypasses `endsWith()` allowlist. Affected from sandbox GA (Oct 20 2025) through the v2.1.88 patch (Mar 31 2026) — **~5.5 months, ~130 releases**.
3. **CVE-2025-59536 + CVE-2026-21852** [26] — `.claude/settings.json` hooks + `enableAllProjectMcpServers` execute before trust dialog; `ANTHROPIC_BASE_URL` redirection exfils API key in plaintext. Headless `-p` mode skips the trust dialog entirely [3] — **catastrophic for containerized + headless clone-and-run patterns**.

### Pod-egress threat surface (the "no LAN reach" claim)

K8s default behavior contradicts the prompt's framing:

| Default | Reality | Mitigation |
|---|---|---|
| Egress | All outbound allowed without NetworkPolicy [28] | Default-deny + allowlist [28] |
| IMDS (169.254.169.254) | Reachable from any non-`hostNetwork` Pod | NetworkPolicy deny `169.254.0.0/16` (CNI-dependent) OR IMDSv2 hop-limit=1 OR EKS Pod Identity |
| ServiceAccount token | Auto-mounted at `/var/run/secrets/kubernetes.io/serviceaccount/token` [29] | `automountServiceAccountToken: false` |
| kube-apiserver | Reachable via `kubernetes.default.svc` if SA token present | Disable SA automount [29] |
| Sidecars | Share network namespace; reachable via localhost | Don't run sidecars in sandbox Pod, or audit each |
| DNS-based egress rules | NetworkPolicy uses IP CIDRs only [28] | Cilium FQDN policy, egress proxy, or in-container iptables firewall [12] |

### Semantic-agency threats (added per framing challenge)

Container isolation bounds OS-level access. It does NOT bound:

- **Repo poisoning** — agent can embed prompt-injection payloads in source, README, `.claude/settings.json` (the exact vector CVE-2025-59536 [26] exploits) that persist after session ends
- **Exfil via legitimate channels** — agent's required egress (`api.github.com`, `api.anthropic.com`) is also its exfil channel. PR descriptions, branch names, commit messages, fabricated user messages in next API call. PromptArmor demo [27] used exactly this.
- **API key as ammunition** — in-Pod key is callable for arbitrary inference. Rate-limit caps damage budget but does not prevent it.
- **Per Schneier** [30]: "no separation between the data and control paths" — instruction-level attacks are unbounded by container-level controls.

### Recommended path

**Use auto mode in the Pod whenever the account + provider supports it** (per user direction). Path A in the checklist below.

When auto mode is unavailable (Bedrock/Vertex auth, older Anthropic model versions, account tier without auto-mode access), fall through to Path B with `--dangerously-skip-permissions` + defense-in-depth.

### Checklist — minimum isolation for the Pod

**Path A — auto mode (preferred):**
- [ ] `claude --permission-mode auto` (NOT `--dangerously-skip-permissions`)
- [ ] `securityContext.runAsNonRoot: true`, `runAsUser: 1000`
- [ ] `securityContext.readOnlyRootFilesystem: true`
- [ ] `automountServiceAccountToken: false`
- [ ] `resources.limits.memory: 4Gi` + `NODE_OPTIONS: --max-old-space-size=4096`
- [ ] NetworkPolicy default-deny egress + allowlist (DNS, `api.anthropic.com`, `api.github.com`, npm registry) [28]
- [ ] IMDS blocked (NetworkPolicy deny `169.254.0.0/16` or IRSA / Pod Identity)
- [ ] GitHub App credential (private App, installed only on personal repos, per §4) [20]
- [ ] Anthropic key via projected Secret volume (file mount, not env var)
- [ ] Pinned CC version + `DISABLE_AUTOUPDATER=1` [1]
- [ ] Ephemeral workspace per session/PR
- [ ] **No cloning of untrusted PRs into the Pod** (CVE-2025-59536 mitigation) [26]
- [ ] PRs from Pod require human review before merge

**Path B — `--dangerously-skip-permissions` (when auto mode unavailable):**
- [ ] All of Path A above
- [ ] In-container `init-firewall.sh` as defense-in-depth alongside NetworkPolicy
- [ ] Per-session ephemeral Pods only (CronJob or Job with `restartPolicy: Never`); no long-lived Deployment holding credentials
- [ ] Egress proxy for FQDN-based allowlist (since NetworkPolicy is CIDR-only [28])
- [ ] Acknowledged: prompt-injection-via-cloned-content can still trigger exfil via legitimate channels

**Path C — DON'T:** headless `-p` + `--dangerously-skip-permissions` + repo clone of arbitrary content + no NetworkPolicy + automounted SA token. This matches the s1ngularity [16] and CVE-2025-59536 [26] attack surface.

---

## 6. Reflection pass

Before assembling the README, re-examining the draft for overstated claims, suppressed contradictions, and alternative interpretations:

- **Auto mode + Bedrock claim:** stated as "mutually exclusive" — verified directly from [2] which says "Anthropic API only. Not available on Bedrock, Vertex, or Foundry." This is a hard constraint and the deliverable correctly reflects it.

- **GitHub App as "lowest blast radius":** the verdict treats 1-hour token lifetime as a strict win, but the PEM itself is a longer-lived secret. The Pattern C blast-radius calculation depends on PEM rotation discipline. Section 4.3.4 acknowledges this; the verdict in §4 could be read as understating it. Strengthened in the reference file's setup steps; the deliverable summary is appropriately qualified.

- **Hosted Sandboxes alternative:** the deliverable's §0 surfaces it as a possibly-better option; §1 details it. The user has already chosen to proceed with self-hosting (gating answer "option 1") so the recommendation is to lead with the gating findings (done) and proceed with the self-host architecture (done). No suppression here.

- **Anthropic harness-detection impact:** §3 says "for a Pod with `ANTHROPIC_API_KEY` this is moot." Worth re-checking: harness detection per [17] is keyword-based on git status, and **could in principle still misclassify an API-key-authenticated session** if Anthropic chose to use the signal for something beyond billing routing. No public evidence this happens, but absence of evidence isn't evidence of absence. The reference file [3.5.3](references/api-key-injection.md#353-what-this-means-for-a-pod-with-anthropicapikey) is appropriately hedged.

- **Container vs runc CVE family:** §0 cites [41a] (OWASP recommending Firecracker/gVisor/Kata) without recommending the operator switch container runtimes. The deliverable's recommendation is "harden the Pod" not "switch to Kata" — this is a judgment call the user can override if their threat model includes container-escape attackers. Flagged in §5 gaps.

- **Rate-limit numbers** — the deliverable's Sonnet 4.x tier table matches [9] verbatim. Opus / Haiku tables in the reference file. No interpolation.

- **Issue #9184 [15]**: the fetch captured the issue body but not the comments thread. The deliverable correctly cites only what was confirmed (Closed status, error message verbatim) and does not speculate on Anthropic's stated rationale beyond what the docs [2] independently confirm.

- **PromptArmor demo [27]**: claimed "demonstrated, recorded, and published." This is a tier-3 source (Wiegold blog); the demo itself was not directly viewed in iter 2. Treat with appropriate weight — it's plausible and consistent with the broader pattern, but tier-3 not tier-1.

- **CVE-2025-59536 fix versions** [26]: the disclosure post does not enumerate fix versions. The deliverable says "patches deployed before Feb 25 2026 disclosure" — appropriately vague, with verification instruction in the reference file gaps.

- **The `~/.claude` two-file requirement**: stated in §2.5.4 of the reference but sourced from counter-discovery rather than a directly-fetched Anthropic doc. Treat as community-confirmed footgun, not Anthropic-acknowledged behavior.

No edits required after reflection.

---

## 7. Decision framework

A reader who needs to decide between approaches in 60 seconds:

1. **Do you specifically need the Claude Code CLI**, or just "Claude agent runs my tools safely"?
   - If just-an-agent: investigate Claude Managed Agents Self-Hosted Sandboxes [8] first
   - If specifically the CLI (browser TTY, `.mcp.json`, `-p` invocation patterns): proceed
2. **Can you use Anthropic API directly** (not Bedrock/Vertex/Foundry)?
   - Yes: auto mode is available [2] — use it; deploy via Path A checklist (§5)
   - No (e.g., AWS-only with IRSA): auto mode unavailable; deploy via Path B checklist (§5)
3. **For GitHub credential**: private GitHub App, installed only on personal repos (§4 verdict)
4. **For Anthropic credential**: projected Secret volume + `apiKeyHelper` for in-process rotation (§3.2.3)
5. **Critical**: do NOT clone untrusted PRs into the Pod (CVE-2025-59536 [26]). Always pin to repos the operator controls; treat AI-opened PRs as untrusted code requiring human review before merge.

---

## 8. Limitations and what was NOT researched

- **Browser TTY** (operator access to the Pod) — explicitly out of scope per the prompt; separate research run.
- **Container-runtime alternatives** (Firecracker, gVisor, Kata) — flagged as OWASP-recommended [41a] but not detailed. The deliverable's recommendation is "harden the runc Pod" not "switch runtimes."
- **Image size + cold start** — no first-party data found; community figures not verified.
- **Bedrock-side rate limits + cost** under high concurrency — referenced but not benchmarked.
- **MCP server transport modes** beyond stdio — sidecar / HTTP-SSE patterns in K8s not detailed in fetched sources.
- **Anthropic's anomaly detection on API requests** — no public source documenting whether Anthropic detects exfiltration encoded in agent-generated content; the deliverable assumes no such detection.
- **The complete current Anthropic-recommended sandbox stack post-CVE family** — Anthropic has not published a "here is what's safe now" architectural statement after CVE-2025-66479 [24] and the SOCKS5 bypass [25]; the deliverable's recommendations combine the docs-as-written [1], [2], [3] with the CVE history.

---

## Appendix — Source map

- 30 numbered primary sources in [`citations.md`](citations.md)
- 14 advisory-tier (counter-discovery) sources marked [Na]
- All Anthropic-official sources are tier 2
- All GitHub-official sources are tier 1
- CVE disclosures are tier 1 (Check Point [26]) or tier 2-3 (Aonan Guan [24], SecurityWeek [25])
- Pod-egress patterns are tier 1 (Kubernetes docs [28]) or tier 2 (HackersVanguard [29])
