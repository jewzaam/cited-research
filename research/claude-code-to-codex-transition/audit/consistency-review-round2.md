# Internal Consistency Review, Round 2 — claude-code-to-codex-transition

> **Post-review note (added by the coordinator after fixes were applied).**
> Every issue in this report is **RESOLVED**:
> 1. **The "18" was wrong; the correct count is 20.** Both round-2 auditors
>    independently counted the enumerated list and got 20. Corrected in all five
>    places across `references/observability.md`, the deliverable and the README.
>    The enumerated list itself was already correct and was not changed.
> 2. The `[1]` and `[3]` citation entries now carry their Dimension-7 content —
>    the full `[otel]` key table and `analytics.enabled` row on `[1]`, and the
>    observability/telemetry section, event catalogue, default metric tags and
>    the two-unreconciled-metric-tables quality note on `[3]`.
> 3. `[77]` and `[78]` are now cited inline in `references/observability.md`
>    §4, where the conventions' new repository home is established.
> 4. The `citations.md` preamble now enumerates every dated source in the pool,
>    including the Dimension-7 additions `[87]`, `[89]`, `[90]`, `[91]` and the
>    two relative-dated help-centre articles.
>
> One further fix came from the citation audit rather than this report: the
> pre-v2.1.214 multi-frame usage-inflation quote was attributed to `[73]` but
> the sentence lives on `[71]`. Reattributed.


Reviewed: README.md, claude-code-to-codex-transition.md, citations.md, all
seven files under references/ (including the new observability.md), and
audit/consistency-review.md (the round-1 report). No web access used; all
checks are file-internal cross-references and arithmetic on the documents'
own enumerated evidence. This round focuses on the seventh dimension
(observability, citations [71]-[92]) and re-verifies round 1's fixes are
still in place.

## Summary table

| # | Severity | Issue | File(s) |
|---|---|---|---|
| 1 | CRITICAL | "Eighteen"/"18" undocumented Codex metric names claimed, but the enumerated list contains 20 distinct entries | references/observability.md (×3), claude-code-to-codex-transition.md (×2) |
| 2 | MODERATE | Citations [1] and [3] are relied on for extensive new OTel-specific facts (default metric tags, event catalogue, `analytics.enabled` behaviour, `[otel]` block structure, doc-internal inconsistencies) that are absent from their citations.md summaries, making those claims unverifiable from citations.md alone | citations.md, references/observability.md |
| 3 | MINOR | New orphan citations [77] and [78] — defined in citations.md, never cited in README, the deliverable, or any reference file | citations.md |
| 4 | MINOR | citations.md's "recurring caveat" preamble listing which sources carry dates was not updated for dimension 7 — omits [87] (dated OpenAI blog) and the dated Tier-3 blogs [89]/[90]/[91] | citations.md |

No dangling citation numbers, no broken internal links, no anchor-target
mismatches, and no arithmetic errors in the hook-count (11+20=31) or
search-coverage (32+12=44, 17+12=29) figures were found. Details below.

---

## Issue 1 — "18 undocumented metric names" claim contradicted by its own enumerated list

**Files:** `references/observability.md` lines 29, 187, 427; `claude-code-to-codex-transition.md` lines 236, 518
**Severity:** CRITICAL
**Status:** RESOLVED

`references/observability.md` states, in three places:

- Line 29 (comparison table): "**18 metrics in source are undocumented** [3][75]"
- Line 187: "**Eighteen metric names exist in source and appear nowhere in the documentation** [3][75]:"
- Line 427 (Gaps §3): "The 18 undocumented metric names may not exist in any shipped build."

The deliverable repeats the figure twice:

- Line 236: "**18 metric names that exist in source and appear nowhere in the docs** [3][75]."
- Line 518 (Limitations item 12): "**The 18 undocumented Codex metric names were read from the `main` branch**"

The list immediately following the line-187 claim, extracted and counted
programmatically (`grep -o` on backtick-quoted `codex.*` tokens, deduplicated),
contains **20 distinct entries**, not 18:

```
codex.artifact.operation.expected_output_count
codex.artifact.operation.started
codex.goal.blocked
codex.goal.budget_limited
codex.goal.completed
codex.goal.created
codex.goal.duration_s
codex.goal.resumed
codex.goal.token_count
codex.goal.usage_limited
codex.guardian.review
codex.guardian.review.duration_ms
codex.guardian.review.token_usage
codex.guardian.review.ttft.duration_ms
codex.plugins.install_elicitation.sent
codex.plugins.install_suggestion
codex.process.start
codex.startup.phase.duration_ms
codex.thread.skills.description_truncated_chars
codex.turn.unified_exec.running_processes
```

Grouped by family this is unambiguous: `codex.goal.*` alone contributes 8
distinct constants (created, resumed, completed, budget_limited,
usage_limited, blocked, token_count, duration_s); `codex.guardian.review*`
contributes 4; `codex.artifact.operation.*` and `codex.plugins.*` contribute 2
each; the remaining four entries (`codex.process.start`,
`codex.turn.unified_exec.running_processes`, `codex.startup.phase.duration_ms`,
`codex.thread.skills.description_truncated_chars`) are singletons. 8+4+2+2+4 = 20.

This is one of the two headline "docs are incomplete" findings for the new
dimension, and it is stated as a precise count ("Eighteen") in the dimension's
prose, its own summary table, its own Gaps section, and twice in the
deliverable's core findings and Limitations section — five load-bearing
repetitions of the same wrong number, all traceable to a single miscount
against the source's own list.

**Expected:** "20" (or the list trimmed to 18 genuinely distinct entries).
**Actual:** "18"/"Eighteen," enumerated list contains 20.
**Grade:** FAIL (formula validity / self-contradiction against own evidence).

---

## Issue 2 — Citations [1] and [3] carry new OTel-specific claims absent from their citations.md summaries

**Files:** `citations.md` entries [1] and [3]; `references/observability.md` §2–3
**Severity:** MODERATE
**Status:** RESOLVED

Dimension 7 cites `[1]` (Configuration Reference) and `[3]` (Advanced
Configuration) repeatedly for facts that do not appear anywhere in those two
citations' summaries in citations.md. citations.md's own stated purpose for
these summaries is to let a reader confirm "what the entry says the source
supplied" without re-fetching the page.

`citations.md`'s [1] summary (lines 29–43) covers: config locations, the ten
project-scope-ignored keys, `sandbox_mode`/`approval_policy` enumerations,
`model_providers.*` schema, `model_reasoning_effort` values,
`model_context_window`, the `mcp_servers.*` key table, `requirements.toml`
admin keys, and the `approval_policy = "untrusted"` conflict with [6]. It
contains **no mention of `otel`, `analytics`, `metrics_exporter`, or
`statsig`.**

`citations.md`'s [3] summary (lines 51–57) covers: `model_providers.*` worked
examples, `openai_base_url`, `--oss`/`oss_provider`, profile overlay files and
the 0.134.0 breaking change, `project_root_markers`, the project-scope
startup warning, and `CODEX_HOME` layout. It likewise contains **no mention of
OTel, metrics, events, or analytics.**

Yet `references/observability.md` attributes all of the following to [1]
and/or [3], none of which is traceable to the citations.md summaries above:

- "`otel.metrics_exporter` … 'defaults to `statsig`' [1]" (§2)
- The full `[otel]` TOML block schema — `exporter`, `metrics_exporter`,
  `trace_exporter`, `log_user_prompt`, per-exporter sub-keys [1][3] (§2)
- The Codex event catalogue: `codex.conversation_starts`,
  `codex.api_request`, `codex.sse_event`, `codex.websocket_request`,
  `codex.websocket_event`, `codex.user_prompt`, `codex.tool_decision`,
  `codex.tool_result` [3] (§2)
- "Each metric below also includes default metadata tags: `auth_mode`,
  `originator`, `session_source`, `model`, and `app.version`" [3] (§2, §5)
- The `codex.turn.token_usage` histogram and its `token_type` values [3] (§5)
- The `analytics.enabled` mechanism and its "When unset, the client default
  applies" wording [1], and "By default, Codex periodically sends a small
  amount of anonymous usage and health data back to OpenAI… Metrics
  collection is independent of OTel log/trace export" [3] (§3)
- Two internal documentation inconsistencies attributed to [3]: the
  `codex.websocket.request`/`codex.websocket_request` naming mismatch, and
  the "10 metrics" vs. "roughly 90 metrics" table discrepancy (§2)

None of this is evidence the underlying claims are false — [1] and [3] are
real Tier-1 config-reference pages plausibly broad enough to contain OTel
config documentation. The gap is that citations.md's summaries were not
extended when these two pre-existing citations were reused for dimension 7,
so a reader checking these claims against citations.md alone — the review
method this document's own methodology prescribes — cannot confirm them.
This is the same failure mode round 1 flagged once as Issue 2
(`project_doc_max_bytes = 65536` not traceable to [5]'s then-summary) and
which was fixed there by extending the citation summary; the same fix was not
applied here for [1]/[3] when dimension 7 was added.

**Expected:** [1] and [3]'s citations.md summaries extended to mention the
`[otel]`/`analytics` config surface, matching the pattern used to fix round
1's Issue 2.
**Actual:** Summaries unchanged since before dimension 7; the OTel-specific
supplied facts are not listed.
**Grade:** FAIL (citation traceability) — claims are plausible, not shown
false, but unverifiable from citations.md as written.

---

## Issue 3 — Orphan citations [77] and [78]

**File:** `citations.md` lines 747–755
**Severity:** MINOR
**Status:** RESOLVED

`[77]` (*semantic-conventions-genai* repository, metadata: 274 stars, 82
forks, 620 commits) and `[78]` (*semantic-conventions-genai* README) are
defined in citations.md but never cited by bracket number in README.md,
claude-code-to-codex-transition.md, or any file under references/ — confirmed
by extracting every `[N]` occurrence across all seven other files and
diffing against the defined set 1–92; `77` and `78` are the only two numbers
in range that never appear outside citations.md.

This is the same pattern round 1 flagged and fixed for [49]/[50] (Issue 4 in
`audit/consistency-review.md`) — that fix is still in place ([49] and [50]
are both now cited inline) — but the same category of gap has recurred for
two of the dimension-7 citations.

**Expected:** [77] and/or [78] cited inline where the repository move or
metadata is discussed (e.g., alongside [83]/[84] in
`references/observability.md` §4, "Current home"), or removed if genuinely
redundant with [79]–[82].
**Actual:** Defined only, never cited.
**Grade:** FAIL (completeness) — low impact; the repository-move fact they'd
support is independently covered by [83] and [84], which are cited.

---

## Issue 4 — citations.md's "dated sources" preamble is stale for dimension 7

**File:** `citations.md` lines 14–18
**Severity:** MINOR
**Status:** RESOLVED

The top-of-file caveat reads:

> "A recurring caveat applies to every `developers.openai.com` and
> `learn.chatgpt.com` page in this list: none of them states a publication or
> last-updated date. Only the Codex changelog [6], the OpenAI research post
> [31], the Anthropic announcement [61], and the GitHub issues/PRs carry
> dates. Everything else is undated and is cited as 'as fetched 2026-08-21'."

This was accurate for citations 1–70. Dimension 7 added several more dated,
non-`developers.openai.com`/`learn.chatgpt.com` sources that this enumeration
does not mention:

- [87] *Running Codex safely*, an `openai.com/index/...` post dated
  2026-05-08 — the same kind of source as [31] (which the preamble does
  name), but [87] is not listed alongside it.
- [89] Praesidia blog, dated 2026-08-03 (Tier 3, not a GitHub issue/PR).
- [90] Shah Vatsal blog, "Released June 22, 2026" (Tier 3, not a GitHub
  issue/PR).
- [91] Codex Insider blog, published 2026-07-15 (Tier 3, not a GitHub
  issue/PR).

([88] and [92] are GitHub issues, so they are covered by the existing
"GitHub issues/PRs" catch-all and are not part of this gap.)

**Expected:** The preamble's enumeration updated to include [87] alongside
[31], and to acknowledge the dated Tier-3 blogs [89]–[91] as a category, or
generalized to "and any source whose citations.md entry states a publication
date" rather than a closed list of citation numbers.
**Actual:** Preamble unchanged since before dimension 7; several dated
dimension-7 sources are not covered by its own description of which sources
carry dates.
**Grade:** FAIL (documentation staleness) — does not affect any individual
claim's accuracy, since each affected citation states its own date inline.

---

## Prior-round fixes — confirmed still in place

All five issues from `audit/consistency-review.md` (round 1) were re-checked
against the current files and remain resolved; none has been undone by the
dimension-7 changes:

1. **Failed-fetch count.** citations.md's "could not be read" sections now
   list six FAILED entries ([66], [67], [68], [69], [70], [92] — the last
   added for dimension 7). Both the deliverable ("Six pages could not be
   read," Limitations item 5) and README ("six pages could not be fetched")
   state six and enumerate all six, including the new [92] with its
   not-material reasoning. Confirmed via `grep -c FAILED citations.md` = 6.
2. **`project_doc_max_bytes = 65536` traceability.** [5]'s citations.md
   summary still carries the added sentence: "The page's 'Customize fallback
   filenames' example also supplies the raised-limit form used elsewhere in
   this research — `project_doc_fallback_filenames = [...]` together with
   `project_doc_max_bytes = 65536`…". Still present and unchanged.
3. **Anthropic price-quad labelling.** The deliverable's Step 2 now states
   Anthropic's figures as an explicitly labelled five-column shape ("base
   input / 5-minute cache write / 1-hour cache write / cache hit / output")
   next to OpenAI's four-column shape, with an explicit warning the two rate
   cards don't share a column shape. Still present. README does not restate
   the quad at all, so no regression risk there.
4. **Orphan citations [49]/[50].** Both are now cited inline —
   [50] in `references/harness-and-shift-cost.md` line 382, [49] in
   `references/openshell-sandbox-implications.md` line 405. Still in place.
   (See Issue 3 above for a new, unrelated instance of the same category.)
5. **`wikipedia`-exclusion explanation.** The deliverable's Limitations item 1
   still states: "`wikipedia` was excluded because it is an encyclopedia
   lookup returning a single result rather than a web index; the health
   probe's own suggested list was `brave,yahoo` for the same reason." Still
   present, and the dimension-7 addendum below it follows the same pattern
   ("suggested list of `yahoo` alone").

---

## Items verified consistent

- **Dimension count and numbering.** The deliverable states "Seven
  dimensions" and links exactly seven files; each reference file's own
  `# Dimension N` header is numbered 1–7 matching the deliverable's link
  order (setup=1, models=2, harness=3, pricing=4, openshell=5,
  coexistence=6, observability=7).
- **Findings count.** The deliverable's "## The five findings that matter"
  heading is followed by exactly five numbered findings (harness gap,
  sandbox/proxy, cost, models, observability). README does not independently
  assert a stale "four findings" or "six dimensions" figure anywhere.
- **Failed-fetch citation set.** citations.md contains exactly 6 entries
  marked FAILED ([66], [67], [68], [69], [70], [92]); both README and the
  deliverable's Limitations section state "six pages" and enumerate all six.
- **Search-coverage arithmetic.** Phase-1 (dimensions 1–6): 32 queries, 17
  single-wave. Phase-2 (dimension 7): 12 queries, all single-wave.
  32 + 12 = 44 and 17 + 12 = 29, matching the deliverable's and README's
  stated aggregate "29 of 44 queries returned a single engine population."
  Backend-availability narrative (3-of-7 alive for phases 1–6, dropping to
  2-of-7 once `brave` stopped answering for dimension 7) is consistent
  between the deliverable and `references/observability.md`'s own Gaps
  section.
- **Hook-event arithmetic.** Codex's 11 events are a verified strict subset
  (identical spelling) of Claude Code's 31; 31 − 11 = 20, and the "20 with no
  Codex counterpart" list in `references/harness-and-shift-cost.md` was
  counted item-by-item and contains exactly 20 distinct names. Both the
  README's short-form table and the deliverable's finding 1 restate 11/31
  correctly.
- **Claude Code's "eight metrics."** The metrics table in
  `references/observability.md` §1 contains exactly 8 rows
  (`session.count`, `lines_of_code.count`, `pull_request.count`,
  `commit.count`, `cost.usage`, `token.usage`, `code_edit_tool.decision`,
  `active_time.total`), matching "the eight metrics" claim there and in
  citations.md's [71] summary.
- **GenAI attribute-registry badge counts.** "118 `Development` badges and
  zero `Stable` badges" is stated identically in README, the deliverable,
  `references/observability.md`, and citations.md's [80] summary.
- **Claude Code's six GenAI convention names.** `gen_ai.system`,
  `gen_ai.request.model`, `gen_ai.response.id`, `gen_ai.response.finish_reasons`,
  `gen_ai.tool.call.id`, and the span event `gen_ai.request.attempt` — counted,
  six distinct names, matching the "six convention names" claim in both the
  deliverable and `references/observability.md`, including the note that
  `gen_ai.system` is deprecated.
- **`names.rs` constant count (54).** Stated identically in citations.md's
  [75] summary and `references/observability.md` §2. No enumerated list is
  given to cross-count against, but no contradiction between the two
  statements of the figure.
- **Cost-metric and session-identifier findings agree across files.** README,
  the deliverable (finding 5), and `references/observability.md` (§5 and its
  comparison table) all state, without contradiction: Claude Code has a
  direct `USD` cost metric and a default `session.id` on metrics; Codex has
  no cost metric and no session/conversation identifier in its documented
  default metric tag set.
- **Contradiction transparency — GenAI stability dispute [89] vs [90].**
  `references/observability.md` §4 presents both sources, lays out primary
  evidence for each specific sub-claim in a table, and states an explicit,
  reasoned verdict ("primary evidence supports [89] and refutes [90]") rather
  than silently picking a side. [90] is cited only in the two sentences that
  refute it — confirmed by grep — and is never used as supporting evidence
  anywhere else in the corpus.
- **Contradiction transparency — `analytics.enabled` default, [91].**
  `references/observability.md` §3 quotes the practitioner claim, quotes both
  primary pages directly, and states explicitly which part of the claim is
  rejected (the "documented conflict" framing) versus which part is
  independently confirmed (the "treat unset as on" operational advice,
  corroborated by [76]). Not silently resolved.
- **Docs-vs-source metric-name divergence.** Presented explicitly as a named
  finding with citations to both the documentation [3] and the source [75]
  in both `references/observability.md` and the deliverable — not silently
  resolved (though see Issue 1 for the count itself being wrong).
- ***(local)* marker usage.** In both `references/openshell-sandbox-implications.md`
  and `references/observability.md`, every *(local)* fact is either under a
  header scoped `(local)`, tagged inline `(local)`/`(local gotcha N)`, or
  attributed to a specific local file/path — no *(local)*-tagged fact also
  carries a bracketed `[N]` citation, and no web-sourced `[N]` fact is
  mistagged `(local)`. The two apparent matches from a regex sweep were
  table rows where the `(local)` tag belongs to one column and the `[N]`
  citation to an adjacent, unrelated column — not the same fact double-marked.
- **Cross-reference links.** Every internal markdown link across all nine
  files (README, deliverable, citations.md, seven reference files) resolves
  to a file that exists at the stated relative path, including the new links
  to and from `references/observability.md` (README → observability.md;
  deliverable → observability.md; observability.md → pricing-plans-quota.md;
  observability.md → openshell-sandbox-implications.md; observability.md →
  `../claude-code-to-codex-transition.md#the-trial-protocol`). All `#`-anchor
  targets correspond to an existing heading: `#limitations` and
  `#the-trial-protocol` in the deliverable, `#gaps-and-limitations` in
  observability.md's own self-link.
- **Citation-number validity.** Every `[N]` used across README, the
  deliverable, and all seven reference files resolves to a defined entry in
  citations.md (range 1–92, each number defined exactly once, no gaps, no
  duplicates) — no dangling citation numbers found anywhere.
- **README completeness for the new dimension.** Every observability-related
  factual claim in README's "## If you run an OTel stack" section and its
  two comparison-table rows carries at least one citation, and each of those
  citations resolves to a defined, on-topic citations.md entry.
- **Miscellaneous pre-existing figures unaffected by dimension 7.** The ten
  project-scope-ignored keys, the 5-host `anthropic_api` block vs. 4-host
  proposed `codex_api` block, the 14-domain devcontainer allowlist, the
  SWE-bench arithmetic (138/500=27.6%, 35.5+18.8+5.1=59.4%), and the
  2026-08-21→2026-08-31 "ten days" arithmetic were all re-spot-checked and
  remain correct and unchanged.
