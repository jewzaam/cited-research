# Internal Consistency Review — claude-code-to-codex-transition

Reviewed: README.md, claude-code-to-codex-transition.md, citations.md, and all
six files under references/. No web access used; all checks are file-internal
cross-references.

## Summary table

| # | Severity | Issue | File(s) |
|---|---|---|---|
| 1 | MODERATE | "Four pages could not be read" undercounts citations.md's own 5-entry failed-fetch list ([66]-[70]); [70] is silently omitted | claude-code-to-codex-transition.md, README.md, citations.md |
| 2 | MODERATE | `project_doc_max_bytes = 65536` attributed to [5] but not traceable to citations.md's summary of that source (which states only the 32 KiB default) | references/coexistence.md, references/openshell-sandbox-implications.md |
| 3 | MODERATE | Anthropic 4-number price groupings reorder/drop a pricing column relative to the reference table, producing a quad that doesn't positionally correspond to the Codex quad it's placed next to | README.md, claude-code-to-codex-transition.md |
| 4 | MINOR | Citations [49] and [50] are defined but never cited by bracket number anywhere in the deliverable | citations.md |
| 5 | MINOR | Unexplained internal gap: "three [backends] were alive... queries ran against two" — no stated reason only 2 of 3 were used | claude-code-to-codex-transition.md (Limitations §1) |

No CRITICAL issues found. Hook-count arithmetic, all spot-checked prices/rates,
citation-number validity, cross-references, and contradiction-transparency all
passed verification (see "Verified consistent" section).

> **Post-review note (added by the coordinator after fixes were applied).**
> All five issues are **RESOLVED**. What changed:
> 1. "Four pages" → "five pages" in both the deliverable and the README, with
>    [70] listed and its lower significance explained.
> 2. `project_doc_max_bytes = 65536` **was** traceable to [5] after all — it
>    appears in that page's "Customize fallback filenames" worked example,
>    annotated "The larger byte limit allows more combined guidance before
>    truncation." The reviewer correctly flagged it as unverifiable from
>    `citations.md` alone; the fix was to add the value to [5]'s citation
>    summary rather than to change the claim.
> 3. Both vendors' price groupings are now column-labelled inline, with an
>    explicit warning that the two rate cards do not share a column shape.
> 4. [49] and [50] are now cited inline — [49] in
>    `references/openshell-sandbox-implications.md` and [50] in
>    `references/harness-and-shift-cost.md`.
> 5. The Limitations section now states why `wikipedia` was excluded from the
>    query backends (it is a single-result encyclopedia lookup, not a web
>    index; the health probe's own suggested list was `brave,yahoo`).

---

## Issue 1 — "Four pages could not be read" undercounts citations.md's own list

**Files:** `claude-code-to-codex-transition.md` (Limitations §5, ~line 396-403), `README.md` (line 102-104), `citations.md` (lines 598-622)
**Severity:** MODERATE
**Status:** RESOLVED

`citations.md`'s "Sources that could not be read" section lists **five** entries,
each marked FAILED:

- [66] `developers.openai.com/codex/getting-started` — FAILED (404)
- [67] Tarek Alaaddin coexistence blog — FAILED (0 bytes)
- [68] `learn.chatgpt.com/docs/import-from-another-agent` — FAILED (404)
- [69] `learn.chatgpt.com/docs/internet-access` — FAILED (404)
- [70] `developers.openai.com/codex/cli-reference` — FAILED (404)

`claude-code-to-codex-transition.md` Limitations item 5 states: **"Four pages
could not be read"** and then enumerates exactly [68], [69], [66], [67] —
omitting [70] entirely, with no explanation for its exclusion. `README.md`
echoes the same count: "four pages could not be fetched." Both undercount by
one relative to citations.md's own list.

[70]'s citations.md entry does note "the actual command reference resolved at
[9]," which is a defensible reason to treat it as a non-gap (the content was
found elsewhere) — but that reasoning is never stated in the Limitations
section, so the "four pages" figure reads as an arithmetic miscount against
the document's own citation list rather than a deliberate, explained
exclusion.

**Expected:** Either "five pages could not be read" with [70] listed and a
one-line reason it doesn't count as a gap, or an explicit note that [70] is
excluded because its content was recovered from [9].
**Actual:** "Four pages could not be read," enumerating only [66]-[69].
**Grade:** FAIL (numerical/completeness).

---

## Issue 2 — `project_doc_max_bytes = 65536` not traceable to the cited source

**Files:** `references/coexistence.md` line 91, `references/openshell-sandbox-implications.md` line 346
**Severity:** MODERATE
**Status:** RESOLVED

Both files state, citing [5]:

> "`project_doc_max_bytes = 65536` is the documented lever [5]."

`citations.md`'s summary of source [5] (`developers.openai.com/codex/guides/agents-md`)
states only: **"`project_doc_max_bytes` default 32 KiB"** (32,768 bytes) — it
never mentions 65536. `references/setup-and-installation.md`, which treats the
same source in the most detail (including its cross-page ambiguity about
per-file vs. combined), also states only the 32 KiB default and never
mentions 65536.

65536 (64 KiB) is exactly double 32768, so it reads as a plausible
"raise it to double the default" example — but as written, the citation `[5]`
implies OpenAI's own documentation states this specific value, and nothing in
this citation pool corroborates that. This reviewer cannot fetch the live
page to confirm or refute it (out of scope for this review), so it is flagged
for verification rather than asserted wrong.

**Expected:** Either a citation-backed statement that OpenAI's docs give 65536
as a worked example, or the value re-labeled as the research team's own
suggested doubling (not "the documented lever [5]").
**Actual:** Presented as a documented value sourced to [5], uncorroborated
elsewhere in the citation pool.
**Grade:** FAIL (citation-traceability) — PLAUSIBLE, not confirmed wrong.

---

## Issue 3 — Anthropic price quads reorder/drop a column relative to the reference table

**Files:** `README.md` line 319, `claude-code-to-codex-transition.md` line 319, `references/pricing-plans-quota.md` (Anthropic table, lines 197-202)
**Severity:** MODERATE
**Status:** RESOLVED

Both the README and the deliverable state, identically:

> "Claude: Opus 5 $5/$6.25/$0.50/$25, Sonnet 5 $2/$2.50/$0.20/$10 [58]"

placed directly alongside the Codex quad, whose stated column order is
**Input / Cached input / Cache writes / Output**:

> "Codex: `gpt-5.6-sol` $5.00/$0.50/$6.25/$30.00 per MTok short context..."

`references/pricing-plans-quota.md`'s Anthropic table has five columns per
model: **Base input / 5m cache write / 1h cache write / Cache hit / Output**.
For Opus 5 those are $5 / $6.25 / $10 / $0.50 / $25. The README/deliverable's
four numbers ($5/$6.25/$0.50/$25) are individually correct values pulled from
that row, but they:

1. Silently drop the 1h-cache-write column ($10).
2. Order the remaining values as Input / 5m-cache-**write** / cache-**hit** /
   Output — the opposite of the Codex quad's Input / cached-**input** /
   cache-**write** / Output ordering.

A reader visually pattern-matching the two quads (both immediately followed
by "[N]") would map Claude's 2nd number to Codex's "cached input" position,
but Claude's 2nd number is actually the *write* price (more expensive than
base), not the *cheap cached-read* price. The numbers themselves are not
wrong, but the juxtaposition invites a wrong-position read.

**Expected:** Either label each number (e.g., "input/cache-write-5m/cache-hit/output")
or reorder to Input/Cache-hit/Cache-write/Output to align positionally with
the Codex quad, and state that the 1h-cache-write tier is omitted.
**Actual:** Four unlabeled numbers in an order that doesn't correspond
position-for-position to the adjacent Codex quad.
**Grade:** FAIL (clarity/potential-misread), values individually correct.

---

## Issue 4 — Orphan citations [49] and [50]

**File:** `citations.md` lines 452-463
**Severity:** MINOR
**Status:** RESOLVED

`[49]` (`docs/sandbox.md`, "3-line redirect stub... Zero technical content.
Listed so that its emptiness is on the record") and `[50]` (`docs/exec.md`,
"1-line redirect stub... a path that differs from where the content actually
resolved ([23])") are defined in citations.md but never cited by bracket
number in the README, the deliverable, or any references/ file — confirmed by
grepping every `[N]` occurrence across all seven other files.

This is a milder version of the pattern in Issue 1: `[66]`-`[69]` (also
empty/failed sources) *are* cited inline in the Limitations discussion so
their gaps are visible where a reader would look for them; `[49]` and `[50]`
are not, so the "listed so that its emptiness is on the record" intent stated
in `[49]`'s own citations.md entry is not actually fulfilled anywhere outside
citations.md itself.
**Grade:** FAIL (completeness) — low impact, since both sources are
independently confirmed to contribute no content.

---

## Issue 5 — Search-coverage detail: 3 backends alive but queries ran against 2

**File:** `claude-code-to-codex-transition.md`, Limitations §1 (~line 379-385)
**Severity:** MINOR
**Status:** RESOLVED

> "Of seven search backends probed, three were alive (`brave`, `wikipedia`,
> `yahoo`) and queries ran against two."

No file explains why only two of the three alive backends were actually
queried. This is not a cross-file contradiction (the figures 3/7 and 17/32
are stated consistently in both `README.md` and the deliverable), but it is
an internal gap in the Limitations narrative itself — a reader cannot tell
whether `yahoo` (or one of the other two) was excluded by choice, by failure
mid-run, or is a transcription slip for "three." The adjacent sentinel-pool
warning ("fallback pool returned 3 results — backends matching it are not
isolated") may be the intended explanation but is never explicitly linked to
the "alive vs. queried" gap.
**Grade:** FAIL (clarity), not a numerical contradiction.

---

## Verified consistent

The following were checked and found consistent across all files, with no
discrepancies:

- **Hook-event arithmetic.** Codex's 11 events are a verified strict subset
  (identical spelling) of Claude Code's 31; the 31-event list minus the
  11-event list produces exactly the 20-event "missing" list stated in
  `references/harness-and-shift-cost.md`, matching item-for-item and in the
  same order. 11 + 20 = 31 holds exactly. The README's shortened example list
  of missing events is a proper subset of the full 20.
- **SWE-bench figures.** 138/500 = 27.6% (exact); 35.5% + 18.8% + 5.1% = 59.4%
  (exact); "74.9% to 80.9%" and "64 runs" and "at least six experienced
  software engineers" are stated identically in `citations.md` and
  `references/models-available.md`.
- **`project_doc_max_bytes` = 32 KiB default** — stated identically (with the
  same citation [5]) in README, the deliverable, both affected reference
  files, and citations.md.
- **Per-file-vs-combined and other vendor self-contradictions** — all four
  flagged contradictions (`approval_policy = "untrusted"` retired,
  `wire_api`/Chat-Completions, `project_doc_max_bytes` per-file vs. combined,
  MCP-tool hook handlers) are surfaced explicitly in the deliverable's
  Limitations section and/or the relevant reference file, each with citations
  naming both sides of the conflict — none is silently resolved.
- **Codex API pricing table** ($5.00/$0.50/$6.25/$30.00 short,
  $10.00/$1.00/$12.50/$45.00 long for `gpt-5.6-sol`) is identical across
  README, deliverable, and `references/pricing-plans-quota.md`.
- **OpenAI credit rate card** — every model row keeps a consistent 10%
  cached-input-to-input ratio (e.g., Sol 12.50/125, Terra 5/50, Luna 0.5/5,
  GPT-5.4 6.25/62.5, GPT-5.4-mini 1.875/18.75, GPT-5.3-Codex 4.375/43.75),
  and all values match identically between `citations.md` and
  `references/pricing-plans-quota.md`.
- **ChatGPT Local-Message-per-5h ranges** — every one of the 6 model rows'
  Pro-5x and Pro-20x columns is exactly 5x/20x the Plus column, for both
  lower and upper bounds, confirming internal arithmetic integrity of the
  table in `references/pricing-plans-quota.md`.
- **Context window figures** — `1.05M` context / `128K` max output /
  `Feb 16, 2026` knowledge cutoff for the three GPT-5.6 models is identical
  in `citations.md`, the deliverable, and `references/models-available.md`;
  Claude's `967K`-token auto-compact figure is likewise consistent between
  `citations.md` and `references/models-available.md`.
- **Vendor cost ballparks** — "$100–$200 per developer per month" [33] and
  "$150-250 per developer per month" [56] are quoted identically (including
  dash style, which reflects the source) in README, deliverable, and
  `references/pricing-plans-quota.md`.
- **2026-08-31 retirement date** — stated as "ten days after this research"
  (research date 2026-08-21); arithmetic verified correct (Aug 21 → Aug 31 =
  10 days), consistent across README, deliverable, and
  `references/models-available.md`.
- **Ten project-scope-ignored keys** — the abbreviated "five named + five
  more" phrasing in README/deliverable/openshell-sandbox-implications.md sums
  correctly against the full 10-key list quoted in
  `references/setup-and-installation.md` and `citations.md`.
- **14-domain devcontainer allowlist**, **7 added Linux capabilities**, **53
  built-in slash commands**, **23.8k/1.8k GitHub stars/forks**, **60k
  AGENTS.md-projects figure**, **12-entry Codex env-var list (no proxy var)**,
  **port 3128 collision**, **six reasoning-effort CLI levels**, **five vs.
  four host-list counts (anthropic_api vs. proposed codex_api block)** — all
  counted and confirmed to match their enumerated lists exactly wherever
  restated.
- **Citation-number validity.** Every `[N]` citation used across README, the
  deliverable, and all six reference files resolves to a defined entry in
  `citations.md` (1-70) — no dangling citation numbers found.
- **Cross-reference links.** All internal markdown links (README →
  deliverable, README → citations.md, README → deliverable#limitations,
  deliverable → citations.md, deliverable → references/*.md, each
  references/*.md → ../citations.md and sibling reference files) resolve to
  files that exist at the stated relative paths. The `#limitations` anchor
  target (`## Limitations`) exists in the deliverable.
- ***(local)* marker usage** in `references/openshell-sandbox-implications.md`
  is applied consistently: local-only facts are either under a header
  explicitly scoped `(local)`, tagged inline `(local)` / `(local, gotcha N)`,
  or attributed to a specific local file path (`Containerfile:23`, repo
  `CLAUDE.md`) — no local-only fact carries a bracketed `[N]` web-citation
  number, and no web-sourced fact is mistagged `(local)`.
- **Six dimensions** — the deliverable's dimension list and links match the
  six files present under `references/`, and each file's own "Dimension N"
  header is numbered 1-6 consistent with the deliverable's ordering.
