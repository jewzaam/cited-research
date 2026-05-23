# Containerized Claude Code patterns + GitHub auth scoping

**What this answers:** how to host Claude Code in a Kubernetes Pod such that the operator can run it with relaxed permissions safely, and how to scope the Pod's GitHub credential so a leak does not reach the operator's other repositories.

**Key insight:** Anthropic released **auto mode** in March 2026 [6], [7] explicitly as "a safer long-running alternative to `--dangerously-skip-permissions`" and **Self-Hosted Sandboxes** for Managed Agents in May 2026 [8]. The original framing of the question — "make `--dangerously-skip-permissions` safe via container isolation" — should be inverted: **use auto mode in a hardened Pod, with the dangerous flag reserved only for cases where auto mode is unavailable** (Bedrock/Vertex auth — see [2]). For GitHub credentials, a **private GitHub App** ([20]) has structurally lower blast radius than a fine-grained PAT or a fork-account.

## Quick decision

```
Do you specifically need the Claude Code CLI in a container?
  No → consider Claude Managed Agents Self-Hosted Sandbox [8] first
       (Cloudflare, Daytona, Modal, Vercel as named providers).
  Yes → proceed below.

Can you use Anthropic API directly (not Bedrock/Vertex/Foundry)?
  Yes → use AUTO MODE in the Pod (Path A below).
        --permission-mode auto  (NOT --dangerously-skip-permissions)
  No  → AUTO MODE is unavailable on Bedrock/Vertex/Foundry [2].
        Fall back to --dangerously-skip-permissions with all of Path B's
        defense-in-depth.

For GitHub credential:
  → Private GitHub App installed only on personal repos. [20]
    Installation tokens expire after 1 hour; per-repo `repository_ids`
    scoping at mint time; `app-name[bot]` identity excluded from
    contribution graph.

For Anthropic credential:
  → Projected Secret volume (file mount) + apiKeyHelper for in-process
    rotation. Pair with External Secrets Operator + Stakater Reloader [18].
```

## The three credential patterns at a glance

| Dimension | Pattern A — fine-grained PAT | Pattern B — second account / fork | Pattern C — GitHub App |
|---|---|---|---|
| Credential lifetime | ≤366 days [21] | ≤366 days [21] | **1 hour** (installation token) [20] |
| Work-repo isolation | Token scoping — **fragile per UI bug [22]** | Account boundary — structural | App install scope — structural |
| ToS compliance | Compliant | Gray zone unless machine account [23] | Compliant |
| Identity | Human user (commits credit user) | Second account (reviewer confusion) | `app-name[bot]` |
| Setup | ~5 min | ~20 min + ongoing | ~10–15 min |
| Recommended for AI sandbox? | Only if PAT will never be edited | No (ToS + ergonomics) | **Yes** |

## Minimum-isolation checklist (Path A — auto mode, preferred)

- [ ] `claude --permission-mode auto` (not `--dangerously-skip-permissions`)
- [ ] `securityContext.runAsNonRoot: true`, `runAsUser: 1000`
- [ ] `securityContext.readOnlyRootFilesystem: true`
- [ ] `automountServiceAccountToken: false` [29]
- [ ] `resources.limits.memory: 4Gi` + `NODE_OPTIONS: --max-old-space-size=4096` [11]
- [ ] NetworkPolicy default-deny egress + allowlist (DNS, `api.anthropic.com`, `api.github.com`, npm) [28]
- [ ] IMDS blocked (NetworkPolicy deny `169.254.0.0/16` or IRSA / Pod Identity)
- [ ] Private GitHub App credential, installed only on user's personal repos [20]
- [ ] Anthropic key via projected Secret volume (file mount, not env var)
- [ ] Pinned CC version + `DISABLE_AUTOUPDATER=1` [1]
- [ ] Ephemeral workspace per session/PR
- [ ] **NO cloning of untrusted PRs into the Pod** (CVE-2025-59536 mitigation [26])
- [ ] PRs from Pod require human review before merge

## Minimum-isolation additions for Path B (`--dangerously-skip-permissions`)

Use only when auto mode is unavailable (Bedrock/Vertex auth). All of Path A above, plus:

- [ ] In-container `init-firewall.sh` ([12]) as defense-in-depth alongside K8s NetworkPolicy — the in-container layer survives NetworkPolicy misconfiguration; the NetworkPolicy layer survives in-container CVEs like [24], [25]
- [ ] Per-session ephemeral Pods only (CronJob or Job, `restartPolicy: Never`)
- [ ] Egress proxy for FQDN-based allowlist (K8s NetworkPolicy is CIDR-only [28])
- [ ] Acknowledged: prompt-injection-via-cloned-content can still trigger exfil via legitimate channels ([`dangerously-skip-permissions.md`](references/dangerously-skip-permissions.md) §5.4)

## Anti-pattern to avoid (Path C)

Headless `-p` + `--dangerously-skip-permissions` + repo clone of arbitrary content + no NetworkPolicy + automounted SA token. This matches the **s1ngularity** ([16]) and **CVE-2025-59536** ([26]) attack surface. Do not deploy.

## What changed since the question was framed

| When | What | Implication |
|---|---|---|
| Mar 24 2026 | Anthropic auto mode [6], [7] | Preferred replacement for `--dangerously-skip-permissions` (when available) |
| Mar 31 2026 | SOCKS5 sandbox bypass patched [25] | The recommended in-container sandbox was bypassable for ~5.5 months — defense in depth |
| Apr 27 2026 | Stateless `ghs_APPID_JWT` token format [20] | GitHub App installation tokens no longer fixed-length |
| May 19 2026 | Self-Hosted Sandboxes for Managed Agents [8] | Alternative to self-hosting CC in a Pod for "agent runs my tools" use cases |
| Jun 15 2026 | Agent SDK billing pool separation [4] | `claude -p` on subscription draws separate credit; consider API-key billing for predictability |

## Reading order

For full methodology, sources, and detail:

1. [`containerized-claude-code-patterns.md`](containerized-claude-code-patterns.md) — full deliverable with gating findings, dimension summaries, decision framework
2. [`references/anthropic-guidance.md`](references/anthropic-guidance.md) — what Anthropic says officially (devcontainer + auto mode + hosted alternatives)
3. [`references/community-dockerfiles.md`](references/community-dockerfiles.md) — the reference Dockerfile verbatim, K8s CronJob pattern, footguns
4. [`references/api-key-injection.md`](references/api-key-injection.md) — auth modes, Secret patterns, rate limits, **harness detection + dual-bucket billing**
5. [`references/github-access-scoping.md`](references/github-access-scoping.md) — Pattern A/B/C comparison + verdict
6. [`references/dangerously-skip-permissions.md`](references/dangerously-skip-permissions.md) — CVE history, Pod-egress threats, semantic-agency threats, full checklist
7. [`citations.md`](citations.md) — 30 numbered primary sources + 14 advisory-tier sources

## Adjacent research in this monorepo

Touches but does not duplicate:
- `research/claude-code-sandbox/` — hooks vs in-process sandbox feature; different scope (host machine, not Pod)
- `research/browser-accessible-coding-shells/` (if separately researched) — operator-access path to the Pod, explicitly out of scope here

Date of research: 2026-05-23. Anthropic and the agentic-tooling landscape move quickly — verify CVE versions, billing dates, and auto-mode availability constraints against current docs before deploying.
