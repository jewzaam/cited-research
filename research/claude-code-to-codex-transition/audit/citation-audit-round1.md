# Citation Audit — claude-code-to-codex-transition

Independent source verification of every numbered citation used in the
deliverable, checked against the pre-fetched source files in
`.tmp-cited-research/claude-code-to-codex-transition/fetched/`. Grades check
whether the source *entails* the specific claim made in the documents, not
merely whether it addresses the same topic.

## Summary table

| # | Grade | Subject |
|---|---|---|
| 1 | VERIFIED | config-reference: ignored project-scope keys, wire_api, reasoning effort values, requirements.toml allowlists |
| 2 | VERIFIED | config-basic: trust gate quote, precedence |
| 3 | VERIFIED | config-advanced: 0.134.0 profile breaking change, project_root_markers |
| 4 | VERIFIED | auth: sign-in modes, auth.json path, port 1455, docker cp recipe |
| 5 | VERIFIED | AGENTS.md guide: project_doc_max_bytes 32 KiB default |
| 6 | VERIFIED | changelog: version dates, custom-prompts deprecation date, PR #39630 |
| 7 | VERIFIED | models: GPT-5.4/5.4-mini retirement 2026-08-31, reasoning selector, Ultra=subagents |
| 8 | VERIFIED | CLI landing mockup strings |
| 9 | VERIFIED | slash-commands: /import scope, 53-command catalogue evidence, exec flags |
| 10 | VERIFIED | hooks: 11-event enumeration, handler-type support, hash-trust, matchers |
| 11 | VERIFIED | subagents: built-ins default/worker/explorer, TOML format, delegation quote |
| 12 | VERIFIED | custom-prompts: deprecation quote, legacy mechanism |
| 13 | VERIFIED | MCP: codex mcp add example, timeouts 10/60 |
| 14 | VERIFIED | permissions: proxy_url 127.0.0.1:3128, socks_url 8081, allow_upstream_proxy |
| 15 | VERIFIED | environment-variables: 12-variable list, no proxy variable |
| 16 | VERIFIED | Codex Pricing: plan prices, Local Messages ranges, credit rate card |
| 17 | VERIFIED | Speed: 1.5x, 2.5x/2x credit multipliers |
| 18 | VERIFIED | Codex Security: off-target redirect quote |
| 19 | VERIFIED | Sandboxing: bwrap prerequisite, fallback helper requirement |
| 20 | VERIFIED | Agent approvals & security: danger-full-access-in-container quote (verbatim) |
| 21 | VERIFIED | Build skills: agentskills.io, load paths, 8,000-char budget |
| 22 | VERIFIED | Codex SDK: npm/pip package names, Sandbox presets |
| 23 | VERIFIED | Non-interactive mode: read-only default, --skip-git-repo-check, --output-schema |
| 24 | VERIFIED | Auth mirror: byte-identical to [4] confirmed by diff |
| 25 | VERIFIED | Config-reference mirror: byte-identical to [1] confirmed by diff |
| 26 | VERIFIED | Advanced-config mirror: byte-identical to [3] confirmed by diff |
| 27 | VERIFIED | Pricing mirror: byte-identical to [16] confirmed by diff |
| 28 | VERIFIED | API Models: 1.05M context, 128K output, Feb 16 2026 cutoff (all 3 GPT-5.6 models) |
| 29 | VERIFIED | Reasoning guide: effort value list, standard/pro mode, 25,000-token reservation |
| 30 | VERIFIED | API Pricing: gpt-5.6-sol/terra/luna short+long rates, gpt-5.3-codex rates |
| 31 | VERIFIED | SWE-bench Verified post: 74.9%→80.9%, 138/500, 64 runs, 59.4/35.5/18.8/5.1%, date 2026-02-23 |
| 32 | VERIFIED | chatgpt.com/pricing: bare "/ month" render failure confirmed |
| 33 | VERIFIED | Rate card: credit table, $100–$200/dev/month, 2026-08-31 retirement note |
| 34 | VERIFIED | Using Codex with plan: banked-reset quote, no-reset-by-support quote |
| 35 | VERIFIED | Credits article: 12-month validity, non-refundable/transferable; no $/credit rate present |
| 36 | VERIFIED | Getting-started redirect: confirmed redirects to CLI landing content |
| 37 | VERIFIED | openai/codex README: install commands, releases.openai.com fallback, Apache-2.0 |
| 38 | VERIFIED | codex-universal README: "not an identical environment" quote, OpenJDK 10 error |
| 39 | VERIFIED | openai/skills: deprecation notice verbatim |
| 40 | VERIFIED | Issue #9253: exact error string, Closed state, 0.84.0 |
| 41 | VERIFIED | Issue #4242: Open state confirmed, diagnosis quote verbatim |
| 42 | VERIFIED | Issue #2267: LandlockRestrict error, NixOS, 0.21.0, Open state |
| 43 | VERIFIED | Issue #9292: PermissionDenied error, version matrix, Closed, bypass-flag quote |
| 44 | VERIFIED | PR #3455: closed 2025-10-30 unmerged, closing-comment quote verbatim |
| 45 | VERIFIED | run_in_container.sh: NET_ADMIN/NET_RAW, allowed_domains.txt, default domain |
| 46 | VERIFIED | init-firewall.sh: single-domain fallback, example.com/api.openai.com probes; confirmed it does NOT read OPENAI_ALLOWED_DOMAINS |
| 47 | VERIFIED | devcontainer.secure.json: CODEX_UNSAFE_ALLOW_NO_SANDBOX=1, 14-domain list, no `privileged` key, remoteUser vscode |
| 48 | VERIFIED | docs/config.md stub: confirmed 21-line redirect, allow_managed_hooks_only fact |
| 49 | VERIFIED | docs/sandbox.md stub: confirmed near-empty redirect |
| 50 | VERIFIED | docs/exec.md stub: confirmed redirect to a differently-resolved path |
| 51 | VERIFIED | model-config: ANTHROPIC_BASE_URL quote, sonnet[1m]/opus[1m]/opusplan aliases |
| 52 | VERIFIED | hooks: 31-event enumeration (manually counted, exact match) |
| 53 | VERIFIED | settings: permission rule evaluation order, additionalDirectories, MCP scopes |
| 54 | VERIFIED | Memory: "reads CLAUDE.md, not AGENTS.md" quote verbatim; symlink/import mechanics |
| 55 | VERIFIED | features-overview: "local > project > user" MCP precedence quote |
| 56 | VERIFIED | Manage costs: $13/day, $150-250/month, 90% under $30/day — verbatim |
| 57 | VERIFIED | CLI reference: fetch status OK, consistent with "fetched but not analysed" framing |
| 58 | VERIFIED | Platform pricing: all four model price rows, tokenizer +30% quote, 900k/9k quote, $2/$10 standard-price quote |
| 59 | VERIFIED | claude.com/pricing: plan prices, "no fixed message count" quote, Claude Code pooled-limits quote |
| 60 | VERIFIED | Support article: ANTHROPIC_API_KEY override warning, verbatim |
| 61 | VERIFIED | Higher limits: 2026-05-06 date, doubling/peak-hours quotes |
| 62 | VERIFIED | agents.md: 60k-projects count, Agentic AI Foundation/aaif.io, 88-files example |
| 63 | VERIFIED | agentsmd/agents.md repo: 23.8k stars, 1.8k forks, MIT |
| 64 | VERIFIED | Community forum post: exact error string, exact command |
| 65 | VERIFIED | mejba.me blog: version string, "Do I pay twice?", stale-read quote, mv/symlink recipe |
| 66 | INACCESSIBLE | Getting-started: confirmed FAILED (404) |
| 67 | INACCESSIBLE | tarekalaaddin blog: confirmed FAILED (0 chars) |
| 68 | INACCESSIBLE | Import-from-another-agent: confirmed FAILED (404) |
| 69 | INACCESSIBLE | Internet access: confirmed FAILED (404) |
| 70 | INACCESSIBLE | CLI reference (guessed URL): confirmed FAILED (404) |

**No INACCURATE, PARTIAL, DRIFT, or NOT FOUND findings survived verification.**
Every checkable citation is fully supported by its source, including the
negative/absence claims (no proxy variable, no dollar-per-credit rate, no
Max-20x price), which are the easiest place for this kind of research to
overreach and were not found to overreach here.

---

## Priority items — detailed verification

### Hook-count claim: Codex 11 vs Claude Code 31, strict subset

**VERIFIED.** Manually enumerated both lists against the fetched pages.

Codex (`developers.openai.com/codex/hooks`, [10]): "During a turn `PreToolUse`,
`PermissionRequest`, `PostToolUse`, `PreCompact`, `PostCompact`,
`UserPromptSubmit`, `SubagentStop`, `Stop`" + "When a session or subagent
starts `SessionStart`, `SubagentStart`" + "When the main thread ends
`SessionEnd`" = **11 events exactly**.

Claude Code (`code.claude.com/docs/en/hooks`, [52]): the lifecycle table
lists `SessionStart, Setup, UserPromptSubmit, UserPromptExpansion,
PreToolUse, PermissionRequest, PermissionDenied, PostToolUse,
PostToolUseFailure, PostToolBatch, Notification, MessageDisplay,
SubagentStart, SubagentStop, TaskCreated, TaskCompleted, Stop, StopFailure,
TeammateIdle, InstructionsLoaded, ConfigChange, CwdChanged, DirectoryAdded,
FileChanged, WorktreeCreate, WorktreeRemove, PreCompact, PostCompact,
Elicitation, ElicitationResult, SessionEnd` — counted item by item: **31
events exactly**.

Set comparison: all 11 Codex event names appear in the Claude Code list with
identical spelling (PreToolUse, PermissionRequest, PostToolUse, PreCompact,
PostCompact, UserPromptSubmit, SubagentStop, Stop, SessionStart,
SubagentStart, SessionEnd). The strict-subset claim holds. The 20-name
"no counterpart" list in `harness-and-shift-cost.md` is exactly
31 − 11 = 20 and each name was cross-checked against the Claude Code table —
correct.

### Quoted prices, credit rates, token counts, context windows, usage allowances

All spot-checked figures below matched their source verbatim:

- Codex hook/context: `gpt-5.6-sol`/`terra`/`luna` — context `1.05M`, max
  output `128K tokens`, knowledge cutoff `Feb 16, 2026` — API Models page
  ([28]), all three rows identical as claimed.
- API pricing ([30]): `gpt-5.6-sol` $5.00/$0.50/$6.25/$30.00 short,
  $10.00/$1.00/$12.50/$45.00 long; `gpt-5.6-terra` $2.00/$0.20/$2.50/$12.00
  short; `gpt-5.6-luna` $0.20/$0.02/$0.25/$1.20 short; `gpt-5.3-codex`
  $1.75/$0.175/$14.00 — all confirmed exact.
- Anthropic platform pricing ([58]): Fable 5 $10/$12.50/$20/$1/$50, Opus 5
  $5/$6.25/$10/$0.50/$25, Sonnet 5 $2/$2.50/$4/$0.20/$10, Haiku 4.5
  $1/$1.25/$2/$0.10/$5 — all confirmed exact against the source table
  (base input / 5m cache write / 1h cache write / cache hit / output).
- Tokenizer quote ([58]): "This tokenizer produces approximately 30% more
  tokens for the same text" — verbatim match.
- Long-context quote ([58]): "A 900k-token request is billed at the same
  per-token rate as a 9k-token request" — verbatim match.
- Credit rate card ([33]): GPT-5.6 Sol 125/12.50/750, Terra 50/5/300, Luna
  5/0.5/30, GPT-5.3-Codex 43.75/4.375/350 — all verbatim matches.
- "$100–$200 per developer per month" ([33]) and "$150-250 per developer per
  month" / "$13 per developer per active day" / "below $30 per active day for
  90% of users" ([56]) — both verbatim matches.
- Codex Local-Messages ranges ([16]): GPT-5.6 Sol 10–100 (Plus/Business),
  200–2,000 (Pro 20x) — confirmed in the pricing page's table.
- **No dollar-per-credit rate** ([35]): confirmed — the credits article
  covers expiry (12 months), non-refundability, non-transferability, and
  negative balances, but no source in the pool states a $/credit
  conversion. The negative claim holds.
- Claude quota quote ([59]): "there's no fixed message count... Pro gives
  you at least 5x more usage per 5-hour session than Free. Max gives you 5x
  or 20x more usage per 5-hour session than Pro" — verbatim match.

### `learn.chatgpt.com/docs/agent-approvals-security` — danger-full-access quote

**VERIFIED, verbatim.** The fetched page contains, in the Dev Containers
section: "If the container is your intended security boundary, run Codex
with `--sandbox danger-full-access` inside the container so Codex does not
try to create a second sandbox layer." This is an exact match to the quote
used in the README and the main deliverable. The surrounding context (this
is guidance for exactly the Docker/devcontainer nested-sandbox scenario, with
an explicit warning two paragraphs earlier about a malicious project
exfiltrating credentials under `danger-full-access`) supports the way the
deliverable frames it — as vendor guidance for a specific container scenario,
not a blanket endorsement.

### Environment-variable list contains no proxy variable

**VERIFIED.** The complete list on `developers.openai.com/codex/environment-variables`
([15]) is: `CODEX_HOME`, `CODEX_SQLITE_HOME`, `CODEX_NON_INTERACTIVE`,
`CODEX_INSTALL_DIR`, `CODEX_API_KEY`, `CODEX_ACCESS_TOKEN`,
`OPENAI_FEDERATION_RULE_ID`, `OPENAI_IDENTITY_TOKEN_FILE`,
`OPENAI_WORKLOAD_IDENTITY_CONTEXT`, `CODEX_CA_CERTIFICATE`, `SSL_CERT_FILE`,
`RUST_LOG` — exactly 12 entries, none of them a proxy variable (no
`HTTPS_PROXY`, `HTTP_PROXY`, `ALL_PROXY`, or Codex-specific equivalent). The
deliverable also correctly quotes the page's own scope disclaimer limiting
how far the negative claim can be pushed ("does not list internal
development variables, test variables, or provider-specific secret names").

### PR #3455 closed unmerged; issue #4242 remained open

**VERIFIED.** PR #3455 ("Use of HTTP_PROXY env var in reqwest clients") shows
status "Closed" in the fetched page, with a closing comment from
`etraut-openai` dated Oct 30, 2025 reading: "we're currently accepting
contributions for bugs and security fixes, but we're not generally accepting
new features at this time" — matching the citation's quote and the "closed
on process grounds, not technical rejection" characterization. Issue #4242
("Use proxy environment variables across Codex HTTP clients") shows status
"Open" in the fetched page (as of the 2026-08-21 fetch), and its body
contains the diagnosis quote used in the deliverable verbatim: "Today users
behind corporate proxies must patch individual call sites (login, Ollama,
etc.)."

### Anthropic's "Claude Code reads CLAUDE.md, not AGENTS.md" claim

**VERIFIED, verbatim.** `code.claude.com/docs/en/memory` ([54]) contains:
"Claude Code reads CLAUDE.md, not AGENTS.md. If your repository already uses
AGENTS.md for other coding agents, create a CLAUDE.md that imports it so both
tools read the same instructions without duplicating them." Exact match to
the quote used throughout the deliverable.

### `project_doc_max_bytes` defaults to 32 KiB

**VERIFIED, verbatim.** `developers.openai.com/codex/guides/agents-md` ([5])
states: "Codex skips empty files and stops adding files once the combined
size reaches the limit defined by `project_doc_max_bytes` (32 KiB by
default)." Exact match. (The deliverable separately and correctly flags an
unresolved cross-page inconsistency about whether the cap is "combined" [5]
or "per-file" [1][3] — that inconsistency claim was spot-checked and both
sides do appear as described in the respective source pages.)

### Dates

All four VERIFIED against source, verbatim:

- **2026-08-31** GPT-5.4/GPT-5.4-mini retirement: confirmed in both
  `developers.openai.com/codex/models` ([7]: "GPT-5.4 and GPT-5.4 mini
  retire from Codex on August 31, 2026.") and the rate-card help article
  ([33]: "On Aug 31, 2026, GPT-5.4 and GPT-5.4 mini will retire in Codex for
  users signed in with ChatGPT.").
- **2026-01-22** custom-prompt deprecation: confirmed in the changelog
  ([6]) at the dated entry "2026-01-22 / Custom prompts deprecated /
  Custom prompts are now deprecated. Use skills for reusable instructions and
  workflows instead."
- **2026-02-23** SWE-bench post: confirmed — the OpenAI post's own byline
  date reads "February 23, 2026."
- **2026-05-06** Anthropic limits post: confirmed — the article's byline
  reads "May 6, 2026," and contains both quoted sentences ("we're doubling
  Claude Code's five-hour rate limits..." and "we're removing the peak hours
  limit reduction...") verbatim.

### SWE-bench contamination figures

**VERIFIED, all figures exact**, against
`openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/` ([31]):

- "improving...from 74.9% to 80.9% in the last 6 months" — verbatim, and
  correctly flagged by the deliverable as hyperlinked to llm-stats.com
  rather than being OpenAI's own measurement.
- "500 problems" — confirmed ("a curated set of 500 problems").
- "138" — confirmed ("an audit of 138 SWE-bench Verified problems that
  OpenAI o3 did not consistently solve").
- "64 runs" — confirmed ("did not consistently solve...over 64 independent
  runs").
- 138/500 = 27.6% — confirmed as the source's own framing ("audited a
  27.6% subset of the dataset").
- "59.4%" of the 138 — confirmed ("59.4% of the 138 problems contained
  material issues"; the summary section separately hedges "at least 59.4%,"
  both phrasings appear in the source and the deliverable uses each in the
  correct place).
- "35.5%" narrow test cases, "18.8%" wide test cases, "5.1%" miscellaneous —
  all three confirmed verbatim, and they sum to 59.4% as claimed.
- "reviewed by at least six experienced software engineers" — confirmed
  verbatim.

---

## `openshell-sandbox-implications.md` — (local) vs cited claims

Confirmed: every claim in this file that is not backed by a fetched web
source is explicitly marked either inline as `(local)`/`*(local)*` or grouped
under a heading such as "## The current shape (local)" and "**Two kinds of
evidence appear in this file and they are labelled throughout**" at the top
of the file, which defines `[N]` = web citation and `(local)` = read from the
user's own repo files, not a citation. Spot-checked several — e.g. the
`anthropic_api` policy block's five hosts, the OpenShell proxy address
`10.200.0.1:3128`, the `--dangerously-skip-permissions` design-rule quote
from the repo's own `CLAUDE.md` — all carry the `(local)` marker and are not
numbered as citations. No local claim was found dressed up as a numbered
citation, and no numbered citation was found resting on unlabeled local
knowledge. The distinction is consistently and correctly maintained
throughout the file.

---

## Grade Ledger

[1] VERIFIED
[2] VERIFIED
[3] VERIFIED
[4] VERIFIED
[5] VERIFIED
[6] VERIFIED
[7] VERIFIED
[8] VERIFIED
[9] VERIFIED
[10] VERIFIED
[11] VERIFIED
[12] VERIFIED
[13] VERIFIED
[14] VERIFIED
[15] VERIFIED
[16] VERIFIED
[17] VERIFIED
[18] VERIFIED
[19] VERIFIED
[20] VERIFIED
[21] VERIFIED
[22] VERIFIED
[23] VERIFIED
[24] VERIFIED
[25] VERIFIED
[26] VERIFIED
[27] VERIFIED
[28] VERIFIED
[29] VERIFIED
[30] VERIFIED
[31] VERIFIED
[32] VERIFIED
[33] VERIFIED
[34] VERIFIED
[35] VERIFIED
[36] VERIFIED
[37] VERIFIED
[38] VERIFIED
[39] VERIFIED
[40] VERIFIED
[41] VERIFIED
[42] VERIFIED
[43] VERIFIED
[44] VERIFIED
[45] VERIFIED
[46] VERIFIED
[47] VERIFIED
[48] VERIFIED
[49] VERIFIED
[50] VERIFIED
[51] VERIFIED
[52] VERIFIED
[53] VERIFIED
[54] VERIFIED
[55] VERIFIED
[56] VERIFIED
[57] VERIFIED
[58] VERIFIED
[59] VERIFIED
[60] VERIFIED
[61] VERIFIED
[62] VERIFIED
[63] VERIFIED
[64] VERIFIED
[65] VERIFIED
[66] INACCESSIBLE
[67] INACCESSIBLE
[68] INACCESSIBLE
[69] INACCESSIBLE
[70] INACCESSIBLE
