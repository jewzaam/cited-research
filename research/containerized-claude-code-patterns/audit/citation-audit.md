# Citation audit report

Audit date: 2026-05-23. Audit agent: independent, no research-conversation context. Sources re-fetched via WebFetch from the agent's own session.

## Priority-claim verification

| ID | Claim | Status |
|---|---|---|
| P1 | Anthropic warning verbatim about `--dangerously-skip-permissions` in devcontainers not preventing exfil | VERIFIED |
| P2 | Auto mode is "a safer long-running alternative to `--dangerously-skip-permissions`"; launch March 24 2026 | VERIFIED |
| P3 | Auto mode NOT available on Bedrock/Vertex/Foundry | VERIFIED |
| P4 | Auto-mode performance numbers (Stage-1 FPR 8.5%, FNR 17% on real overeager) | VERIFIED |
| P5 | Self-Hosted Sandboxes launch May 19 2026; named providers Cloudflare/Daytona/Modal/Vercel; **K8s not listed** | VERIFIED |
| P6 | Root refusal message verbatim | VERIFIED |
| P7 | CVE-2025-66479 details (Nov 2025 launch through v2.0.54, patched v2.0.55) | VERIFIED |
| P8 | SOCKS5 null-byte bypass version range and patch version | **INACCURATE → Status: RESOLVED** (see Fix 1) |
| P9 | CVE-2025-59536 attack vector and required user interaction | VERIFIED with nuance — hook vector matches; ANTHROPIC_BASE_URL exfil fires *before* any click |
| P10 | K8s NetworkPolicy default allow-egress; isolation via Egress policyType | VERIFIED |
| P11 | Fine-grained PAT GA March 18 2025; Packages/Checks unsupported | VERIFIED |
| P12 | GitHub App installation token 1-hour lifetime; `repository_ids` per token; `ghs_APPID_JWT` April 27 2026 | VERIFIED |
| P13 | Fine-grained PAT silent reset UI bug #188472, unresolved | VERIFIED |
| P14 | GitHub ToS one-personal + one-machine account | VERIFIED |
| P15 | Anthropic rate limits per-organization; Tier 1 Sonnet 50/30K/8K | VERIFIED |
| P16 | Harness detection $200.98 On Patel incident, `hermes.md`/`OpenClaw` keywords | VERIFIED |
| P17 | Schneier verbatim quotes on privilege separation + prompt-injection unsolvability | VERIFIED |
| P18 | June 15 2026 Agent SDK billing pool separation | VERIFIED |
| P19 | Anthropic reference Dockerfile: `FROM node:20`, non-root `node` user, npm install | VERIFIED |
| P20 | Firewall script allowlist (exact 8 domains) | VERIFIED |

## Other findings (auditor's discretion)

- **F1 — SOCKS5 version range conflation in deliverable §0 and §5.** The deliverable and `dangerously-skip-permissions.md` had `v2.0.24 ... v2.1.89` and `v2.1.88/v2.1.90` — neither the specific v2.0.24 GA version nor v2.1.89 upper bound nor v2.1.90 co-patch is in the cited SecurityWeek source [25]. **Status: RESOLVED** — deliverable §0 point 4 split into two distinct CVE windows; deliverable §5 SOCKS5 line and `dangerously-skip-permissions.md` §5.2.2 table rewritten to say "sandbox GA (Oct 20 2025) through the v2.1.88 patch (Mar 31 2026)" with no v2.1.90 reference. citations.md [25] was already correct.

- **F2 — Auto mode "research preview" qualification missing.** The live permission-modes page [2] explicitly labels auto mode "a research preview" with the caveat "It reduces prompts but does not guarantee safety." The deliverable did not surface this. **Status: RESOLVED** — added to deliverable §1 ("Anthropic labels auto mode a 'research preview' [2]") and to `anthropic-guidance.md` §1.3 (added "Status: research preview" as the first availability-constraint bullet).

- **F3 — Devcontainer warning quote (P1) truncates one sentence.** The live page also says "Avoid mounting host secrets such as `~/.ssh` or cloud credential files into the container; prefer repository-scoped or short-lived tokens." The deliverable's quote is shorter but not inaccurate. **Status: ACKNOWLEDGED** — quote remains accurate as cited; full extended warning is in `anthropic-guidance.md` §1.2 (which quotes the longer form). No edit required.

- **F4 — CVE-2025-66479 changelog truncation.** Source says "Fixed proxy DNS resolution being forced on by default"; documents render as "Fixed proxy DNS resolution." Minor; no functional difference. **Status: ACKNOWLEDGED** — no edit.

- **F5 — CVE-2025-59536 user-interaction nuance.** For the `ANTHROPIC_BASE_URL` exfil vector specifically, the source notes the API key transmits before the trust-dialog click. The deliverable's blanket "click 'Yes, proceed'" requirement is correct for the hooks vector but slightly overstates for the exfil vector. **Status: ACCEPTED** — operational impact is identical (treat any clone-of-untrusted-repo as compromise of the API key); no edit.

## Sources re-fetched in this audit

The audit agent re-fetched the following URLs via WebFetch to verify claims: `code.claude.com/docs/en/devcontainer`, `claude.com/blog/auto-mode`, `anthropic.com/engineering/claude-code-auto-mode`, `code.claude.com/docs/en/permission-modes`, `claude.com/blog/claude-managed-agents-updates`, `oddguan.com/blog/anthropic-sandbox-cve-2025-66479`, `securityweek.com/anthropic-silently-patches-claude-code-sandbox-bypass`, `research.checkpoint.com/2026/...cve-2025-59536`, `kubernetes.io/docs/concepts/services-networking/network-policies`, `github.blog/changelog/2025-03-18-fine-grained-pats-are-now-generally-available`, `docs.github.com/.../generating-an-installation-access-token-for-a-github-app`, `github.com/orgs/community/discussions/188472`, `docs.github.com/en/site-policy/github-terms/github-terms-of-service`, `platform.claude.com/docs/en/api/rate-limits`, `mindstudio.ai/blog/anthropic-harness-detection-git-commit-billing-overcharge`, `herbsutter.com/2025/10/23/schneier-on-llm-vulnerabilities-agentic-ai-and-trusting-trust`, `code.claude.com/docs/en/authentication`, `raw.githubusercontent.com/anthropics/claude-code/main/.devcontainer/Dockerfile`, `raw.githubusercontent.com/anthropics/claude-code/main/.devcontainer/init-firewall.sh`.

## Summary

20 priority claims audited. 1 INACCURATE finding (SOCKS5 version specifics), 5 minor wording observations. All material accuracy issues **RESOLVED** via edits applied 2026-05-23.
