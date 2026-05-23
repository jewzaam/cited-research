# Citations

All sources visited via WebSearch or WebFetch on 2026-05-23 unless noted otherwise. Tier scheme:
**Tier 1** = peer-reviewed / government / standards body, **Tier 2** = vendor official / established reference site, **Tier 3** = industry blog / well-known practitioner, **Tier 4** = forum / personal blog / social media.

## Anthropic-official (Tier 2)

[1] **Claude Code — Development containers (official docs).** Anthropic. `https://code.claude.com/docs/en/devcontainer`. Source for: reference devcontainer architecture, ~/.claude volume mount pattern, `CLAUDE_CONFIG_DIR` env var, NET_ADMIN/NET_RAW capability requirement, official warning that `--dangerously-skip-permissions` inside a devcontainer "do not prevent a malicious project from exfiltrating anything accessible inside the container, including the Claude Code credentials stored in `~/.claude`", recommendation to use auto mode instead, `permissions.disableBypassPermissionsMode` enforcement. Fetched verbatim.

[2] **Claude Code — Permission modes (official docs).** Anthropic. `https://code.claude.com/docs/en/permission-modes`. Source for: full mode taxonomy (default, acceptEdits, plan, auto, dontAsk, bypassPermissions), what each bypasses, auto-mode classifier semantics, auto-mode requirements (Sonnet 4.6 / Opus 4.6 / 4.7; **Anthropic API only — not Bedrock/Vertex/Foundry**), root/sudo refusal text verbatim, protected paths list, auto-mode allow/block defaults.

[3] **Claude Code — Security (official docs).** Anthropic. `https://code.claude.com/docs/en/security`. Source for: permission model, credential storage paths, write-scope restriction to working dir + subfolders, prompt-injection safeguards, "Trust verification is disabled when running non-interactively with the -p flag" (with `--worktree` exception), recommendation to use VMs for untrusted content, Claude Code on the Web isolation guarantees including scoped git credential proxy.

[4] **Claude Code — Authentication (official docs).** Anthropic. `https://code.claude.com/docs/en/authentication`. Source for: full auth-mode list, credential storage paths per OS, `apiKeyHelper` mechanism, authentication precedence order (cloud-provider > `ANTHROPIC_AUTH_TOKEN` > `ANTHROPIC_API_KEY` > `apiKeyHelper` > `CLAUDE_CODE_OAUTH_TOKEN` > subscription OAuth), OAuth fragility note for WSL2/SSH/containers, `claude setup-token` one-year token, **explicit June 15 2026 dual-bucket billing change verbatim**.

[5] **Claude Code — Amazon Bedrock (official docs).** Anthropic. `https://code.claude.com/docs/en/amazon-bedrock`. Source for: `CLAUDE_CODE_USE_BEDROCK=1` + required `AWS_REGION`, IAM policy JSON (`bedrock:InvokeModel`, `bedrock:InvokeModelWithResponseStream`, `bedrock:ListInferenceProfiles`, `bedrock:GetInferenceProfile`), credential chain via AWS SDK (IRSA-compatible), `awsAuthRefresh` and `awsCredentialExport` settings, `/login`/`/logout` disabled under Bedrock.

[6] **Auto mode for Claude Code (official Anthropic blog).** Anthropic, 2026-03-24. `https://claude.com/blog/auto-mode`. Source for: launch date, "a safer long-running alternative to --dangerously-skip-permissions" framing, classifier-blocks-then-redirects behavior, eventual user-prompt fallback, "reduces risk compared to --dangerously-skip-permissions but doesn't eliminate it entirely".

[7] **Claude Code auto mode: a safer way to skip permissions (Anthropic engineering blog).** Anthropic, 2026-03-25 (per [2]'s back-reference). `https://www.anthropic.com/engineering/claude-code-auto-mode`. Source for: two-stage classifier (Sonnet 4.6 single-token filter then chain-of-thought), five threat categories (overeager, mistakes, prompt injection, model misalignment), performance table (Stage-1 FPR 8.5% on 10K real traffic; Full pipeline FPR 0.4%; Stage-1 FNR 1.8% on 1K synthetic exfil; Full pipeline FNR 5.7% / 17%), escalation rule "3 consecutive denials or 20 total", Anthropic's explicit caveat "It is not a drop-in replacement for careful human review on high-stakes infrastructure".

[8] **New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels (official Anthropic blog).** Anthropic, 2026-05-19. `https://claude.com/blog/claude-managed-agents-updates`. Source for: Self-Hosted Sandboxes public-beta launch date, "The sandbox runs on your own infrastructure, or with managed providers like Cloudflare, Daytona, Modal, or Vercel", architecture split (Anthropic-side agent loop / customer-side tool execution), Kubernetes **not mentioned** as a directly supported target, MCP Tunnels research-preview status.

[9] **Anthropic API rate limits (official docs).** Anthropic. `https://platform.claude.com/docs/en/api/rate-limits`. Source for: token-bucket algorithm verbatim, "Limits are set at the organization level", tier RPM/ITPM/OTPM tables for Sonnet/Opus/Haiku, tier spend thresholds ($5/$40/$200/$400), cache-aware ITPM (cached reads don't count for non-Haiku-3.5 models), 429 response headers, Workspace sub-limits cannot exceed org limits, Managed Agents create-300-rpm/read-600-rpm separate from Messages API.

## Anthropic reference Dockerfile and devcontainer (Tier 2, raw)

[10] **`anthropics/claude-code/.devcontainer/Dockerfile` (raw source).** Anthropic. `https://github.com/anthropics/claude-code/blob/main/.devcontainer/Dockerfile`. Raw URL `https://raw.githubusercontent.com/anthropics/claude-code/main/.devcontainer/Dockerfile`. Source for: base image `FROM node:20`, exact apt-get package list, non-root `node` user, npm-global path, Zsh setup, `npm install -g @anthropic-ai/claude-code@${CLAUDE_CODE_VERSION}` install, passwordless-sudo for firewall script only. Fetched verbatim.

[11] **`anthropics/claude-code/.devcontainer/devcontainer.json` (raw source).** Anthropic. `https://github.com/anthropics/claude-code/blob/main/.devcontainer/devcontainer.json`. Source for: `runArgs: ["--cap-add=NET_ADMIN","--cap-add=NET_RAW"]`, `remoteUser: "node"`, per-devcontainer-id named volumes for `~/.claude` and bash history, `NODE_OPTIONS: "--max-old-space-size=4096"`, `CLAUDE_CONFIG_DIR=/home/node/.claude`, `postStartCommand: "sudo /usr/local/bin/init-firewall.sh"`, `workspaceMount` bind type. Fetched verbatim.

[12] **`anthropics/claude-code/.devcontainer/init-firewall.sh` (raw source).** Anthropic. `https://github.com/anthropics/claude-code/blob/main/.devcontainer/init-firewall.sh`. Source for: exact allowlisted domains (`registry.npmjs.org`, `api.anthropic.com`, `sentry.io`, `statsig.anthropic.com`, `statsig.com`, `marketplace.visualstudio.com`, `vscode.blob.core.windows.net`, `update.code.visualstudio.com`), dynamic GitHub IP CIDR fetch from `https://api.github.com/meta`, default-DROP iptables policy on INPUT/OUTPUT/FORWARD, allow DNS UDP/53 + SSH TCP/22 + loopback + host network /24 + ESTABLISHED,RELATED, verification step (`example.com` must fail, `api.github.com/zen` must succeed). Fetched verbatim.

## Community Dockerfiles + Kubernetes patterns (Tier 3)

[13] **Running Claude Code in Docker: Anthropic's Official Devcontainer, No VS Code Required.** Software Thug, 2026-02-19. `https://www.softwarethug.com/posts/running-claude-code-in-docker-setup-that-works/`. Source for: standalone-Docker pattern via sparse clone of upstream `.devcontainer/`, patched init-firewall.sh to allow dev-server port range 3000–9000, authentication persistence via Docker volume (not host).

[14] **Running Claude Code as a Kubernetes Job / CronJob.** Daniel Hnyk, 2026-02-26. `https://danielhnyk.cz/claude-code-kubernetes-cronjob/`. Source for: K8s CronJob YAML, `envFrom: secretRef` injection pattern, `nikolaik/python-nodejs:python3.13-nodejs22` image, headless invocation `claude -p --dangerously-skip-permissions --verbose --output-format stream-json -- "$SKILL_PROMPT"`, `timeout 10800` wrapper with exit-code-124 backup, `{"hasCompletedOnboarding": true}` in `~/.claude.json` for non-TTY environments, gh CLI for PR opening.

[15] **[BUG] `--dangerously-skip-permissions` cannot be used with root/sudo (issue #9184).** anthropics/claude-code, GitHub issue. `https://github.com/anthropics/claude-code/issues/9184`. Source for: exact error message verbatim, Closed status, evidence that the root block is the documented behavior (not a regression). v2.0.10. Comments not captured in fetch.

[16] **AI Coding Agent Horror Stories.** Docker, Inc., engineering blog, 2026. `https://www.docker.com/blog/ai-coding-agent-horror-stories-security-risks/`. Source for: full incident catalog (Mac home-dir wipe Dec 2025; Wolak Oct 2025; family photos Jan 2026; AWS Kiro 13-hr regional outage; **s1ngularity malware (Aug 26 2025) explicitly using `--dangerously-skip-permissions`, `--yolo`, `--trust-all-tools` as payload flags**, ClawHavoc 335+ malicious skills Feb 2026, Replit DB wipe July 2025), CodeRabbit study (2.74× more vulns in AI code), GitGuardian secrets-sprawl stats (28.65M leaks 2025, 81% AI-credential surge), Docker Sandboxes mitigation primitives, 10-step hardening list including verbatim **"Avoid --dangerously-skip-permissions flags on host systems"**.

## Anthropic API key + harness detection (Tier 3, billing)

[17] **Anthropic's Harness Detection Bug: 3 Things That…** MindStudio, 2026. `https://www.mindstudio.ai/blog/anthropic-harness-detection-git-commit-billing-overcharge`. Source for: "Anthropic pulls git status into Claude Code's system prompt and scans for strings like `hermes.md` and `OpenClaw`", purely-keyword-based detection (not behavioral), On Patel $200.98 incident on Claude Max 20x plan, Theo Brown empty-repo reproduction, Anthropic apology via Tariq. **Does not directly address whether ANTHROPIC_API_KEY usage bypasses detection in containers.**

[18] **Reloader — restart pods when secret changes.** Stakater (official). `https://docs.stakater.com/reloader/latest/how-to-guides/restart-pods-when-secret-changes.html`. Source for: `reloader.stakater.com/auto: "true"` annotation, rolling-restart-on-secret-change workflow.

## GitHub access scoping (Tier 1, GitHub official + community)

[19] **Permissions required for fine-grained personal access tokens (official GitHub docs).** GitHub. `https://docs.github.com/en/rest/authentication/permissions-required-for-fine-grained-personal-access-tokens`. Source for: per-endpoint permission requirements; minimum permissions for push branch + open PR = Contents (write) + Pull requests (write) + Metadata (read).

[20] **Generating an installation access token for a GitHub App (official GitHub docs).** GitHub. `https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-an-installation-access-token-for-a-github-app`. Source for: "The installation access token will expire after 1 hour" verbatim, `repository_ids` parameter for per-repo scoping (max 500 per request), stateless `ghs_APPID_JWT` format rolled out April 27 2026.

[21] **Fine-grained PATs are now generally available (GitHub changelog).** GitHub, 2025-03-18. `https://github.blog/changelog/2025-03-18-fine-grained-pats-are-now-generally-available/`. Source for: GA date, fine-grained PATs enabled by default for orgs unless previously disabled, approval-workflow requires owner authorization, **explicit unsupported scenarios at GA: Packages and Checks APIs (no ghcr.io), multi-org single-token, outside collaborator access, Enterprise object APIs (SCIM, org creation)**.

[22] **Fine-grained PAT silent reset bug (community discussion #188472).** GitHub community. `https://github.com/orgs/community/discussions/188472`. Source for: confirmed reproducible UI bug — editing a fine-grained PAT silently reverts "Only select repositories" to "All repositories", unresolved status, security-implications framing ("silent privilege escalation").

[23] **GitHub Terms of Service (official site policy).** GitHub. `https://docs.github.com/en/site-policy/github-terms/github-terms-of-service`. Source for: machine-account policy verbatim ("one free Account... if you choose to control a machine account as well, that's fine, but it can only be used for running a machine"), "A machine account is used exclusively for performing automated tasks", "no more than one free machine account in addition to your free Personal Account".

## Sandbox security + dangerously-skip-permissions (Tier 1-3)

[24] **A Sandbox That Wasn't: How a Tiny Logic Error Disabled Claude Code's Network Isolation (CVE-2025-66479).** Aonan Guan, 2025-12. `https://oddguan.com/blog/anthropic-sandbox-cve-2025-66479/`. Source for: exact bug (`needsNetworkProxy = allowedDomains.length > 0` logic inversion), affected Claude Code versions (launch through v2.0.54), patched v2.0.55 with "Fixed proxy DNS resolution" changelog (no security mention), CVE assigned only to sandbox-runtime library not Claude Code, Anthropic quote "The root cause is in the library", attacker capability via bypass.

[25] **Anthropic Silently Patches Claude Code Sandbox Bypass.** SecurityWeek, May 2026. `https://www.securityweek.com/anthropic-silently-patches-claude-code-sandbox-bypass/`. Source for: SOCKS5 null-byte injection (`attacker-host.com\x00.google.com`), affected period Oct 20 2025 (sandbox GA) through April 2026, patched Claude Code v2.1.88 (Mar 31 2026), no CVE assigned to SOCKS5 bug, Anthropic stated their fix predated researcher's disclosure.

[26] **RCE and API Token Exfiltration through Claude Code Project Files (CVE-2025-59536 + CVE-2026-21852).** Check Point Research, 2026-02-25. `https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/`. Source for: `.claude/settings.json` hooks executing on SessionStart, MCP `enableAllProjectMcpServers` bypass, malicious `ANTHROPIC_BASE_URL` redirecting API to attacker proxy with key in plaintext Authorization header, required user interaction (clone repo + run `claude` + click "Yes, proceed"), commands run before trust dialog completes.

[27] **Claude Code `--dangerously-skip-permissions`: Reckless or Required?** Thomas Wiegold blog, 2026. `https://thomas-wiegold.com/blog/claude-code-dangerously-skip-permissions/`. Source for: Wolak incident (Oct 2025, issue #10077, `rm -rf` from `/`), Reddit Dec 2025 home directory wipe via `~/` expansion, Tilde Directory Trick (issue #12637, Nov 2025), McAulay Jan 2026 11 GB Claude Cowork deletion, PromptArmor Jan 2026 hidden-text exfil demo, subagent inheritance verbatim ("they all get full, unsupervised system access"), author's position that the flag IS safe in network-isolated containers with whitelisted domains.

[28] **Network Policies (official Kubernetes docs).** Kubernetes. `https://kubernetes.io/docs/concepts/services-networking/network-policies/`. Source for: default-allow-all-egress behavior, `policyTypes: [Egress]` semantics, default-deny egress YAML pattern, allow-DNS-to-kube-system pattern, **IP-CIDR-only limitation (no DNS-based rules)**, CNI implementation variation, "traffic to and from the node where a Pod is running is always allowed".

[29] **Disabling automountServiceAccountToken Prevents Abuse.** HackersVanguard, 2026-01-23. `https://hackersvanguard.com/disabling-automountserviceaccounttoken-prevents-abuse/`. Source for: default mount path `/var/run/secrets/kubernetes.io/serviceaccount`, attacker capability with compromised SA token ("create, delete, or modify Kubernetes resources; essentially taking control of the namespace"), ServiceAccount-level YAML, Pod-level YAML.

[30] **Schneier on LLM Vulnerabilities, Agentic AI, and Trusting Trust (relay).** Bruce Schneier via Herb Sutter, 2025-10-23. `https://herbsutter.com/2025/10/23/schneier-on-llm-vulnerabilities-agentic-ai-and-trusting-trust/`. Source for Schneier verbatim quotes: "There is no privilege separation, and there is no separation between the data and control paths." "Prompt injection might be unsolvable in today's LLMs."

## Counter-discovery sources NOT independently fetched in iter 2

The following sources were surfaced by Counter-Discovery agents in iter 1. Claims cited to these are marked `[NNa]` (advisory tier) and flagged as such in reference files. Audit phase will fetch.

[31a] **Lyrie Research: TrustFall — Agentic RCE in Claude Code, Gemini CLI, GitHub Copilot.** 2026-05-09. `https://lyrie.ai/research/research/2026-05-09-trustfall-agentic-rce`. Cited for: headless / containerized Claude Code is the worst configuration for MCP-based supply-chain attack because the trust dialog never appears.

[32a] **Adversa AI: TrustFall coding-agent security flaw.** 2026. `https://adversa.ai/blog/trustfall-coding-agent-security-flaw-rce-claude-cursor-gemini-cli-copilot/`. Cited for: MCP server processes run at OS-level not container-limited.

[33a] **GitGuardian State of Secrets Sprawl Report 2025.** GitGuardian. `https://www.gitguardian.com/state-of-secrets-sprawl-report-2025`. Cited for: 28.65M secrets leaked on public GitHub in 2025, 96% of leaked GitHub tokens have write access, AI-assisted commits leak at 3.2% vs human 1.5%.

[34a] **State of Secrets Sprawl 2025 (blog).** GitGuardian. `https://blog.gitguardian.com/the-state-of-secrets-sprawl-2025/`. Companion to [33a].

[35a] **Code to Cloud Attacks: GitHub PAT to Cloud Control Plane.** Wiz. `https://www.wiz.io/blog/github-attacks-pat-control-plane`. Cited for: long-lived org-wide PAT as "master key" pattern, fine-grained or App tokens narrow blast radius.

[36a] **Replacing a GitHub Personal Access Token with a GitHub Application.** Aembit, 2025-06. `https://aembit.io/blog/replacing-a-github-personal-access-token-with-a-github-application/`. Cited for: PAT-to-App migration narrative, installation-token blast-radius comparison.

[37a] **Still Using PATs in 2025? Time to move to GitHub Apps.** bmterra.eu, 2025-06-01. `https://bmterra.eu/articles/010625-using-github-apps/`. Cited for: GitHub Apps as preferred over PATs in 2025+, short-lived tokens, independent identity.

[38a] **Knostic: Claude Code auto-reads .env files without disclosure.** Knostic. `https://www.knostic.ai/blog/claude-cursor-env-file-secret-leakage`. Cited for: any `.env` in working dir silently ingested; persisted to `~/.claude/projects/`.

[39a] **The Register: Anthropic Tosses Agents into the API Billing Pool.** The Register, 2026-05-14. `https://www.theregister.com/ai-ml/2026/05/14/anthropic-tosses-agents-into-the-api-billing-pool`. Cited for: June 15 2026 dual-bucket billing structural change applies to all Agent SDK / `claude -p` use.

[40a] **Cymulate / Penligent: CVE-2025-54794 + CVE-2025-54795 sandbox bypass research.** `https://cymulate.com/blog/cve-2025-547954-54795-claude-inverseprompt/`. Cited for: path restriction bypass (CVSS 7.7) and command injection via null-terminated allowed commands (CVSS 8.7).

[41a] **Northflank: How to run untrusted code on Kubernetes.** Northflank. `https://northflank.com/blog/how-to-run-untrusted-code-on-kubernetes`. Cited for: OWASP Top 10 for Agentic Apps 2026 explicitly classifies standard containers as insufficient for production AI agents with code execution; recommends Firecracker/gVisor/Kata; three runc CVEs Nov 2025 (CVE-2025-31133, CVE-2025-52565, CVE-2025-52881).

[42a] **Sculptor — Local AI Agent Sandbox.** Imbue, 2026. `https://imbue.com/blog/sculptor-announce`. Cited for: third-party Mac desktop app running parallel Claude Code agents in isolated Docker containers; uses user's own subscription or API key; not Anthropic-managed.

[43a] **Claude Code on the Web.** Anthropic. `https://www.anthropic.com/news/claude-code-on-the-web`. Cited for: Anthropic-managed VM per task, GitHub repo cloned into VM, credentials never inside sandbox — custom proxy handles git auth with scoped credentials.

[44a] **Claude Code SDK billing split (June 15 2026 transition guide).** apiyi.com, 2026-06. `https://help.apiyi.com/en/anthropic-claude-subscription-agent-sdk-billing-split-june-2026-en.html`. Cited for: dual-bucket billing date and $2,000/day overage cap.

## Notes on missing fetches

- Issue #9184 [15] body captured; comments thread not visible in fetch output.
- Stakater Reloader [18] page did not detail ESO integration or other workload types beyond Deployment.
- softwarethug post [13] returned summary not literal Dockerfile content (the post itself describes sparse-cloning Anthropic's upstream `.devcontainer/`).

The audit phase will re-fetch any URL where verification requires fuller content.
