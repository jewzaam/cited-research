# Consistency Review: Anthropic API Usage Tracking and Limits

**Reviewer:** Claude Sonnet 4.6 (internal consistency pass — no context from research conversation)
**Date:** 2026-04-04
**Scope:** analysis.md, README.md, references/billing-usage-endpoints.md, references/client-side-tracking.md, references/cost-surfacing-patterns.md, references/rate-limit-structure.md, references/response-headers.md, citations.md
**Method:** Read all files cold, then cross-checked every numerical claim, citation pointer, link, and factual assertion across files. No external sources consulted.

---

## Summary Table

| ID | Severity | File(s) | Topic | PASS/FAIL |
|----|----------|---------|-------|-----------|
| C-01 | MODERATE | analysis.md vs. rate-limit-structure.md | Rate limit table omits `Max Single Purchase` column | **RESOLVED** |
| C-02 | MODERATE | analysis.md §4 | `server_tool_use` block cited to [1]; [1] covers rate limit headers, not usage object | **RESOLVED** |
| C-03 | MODERATE | client-side-tracking.md vs. analysis.md | Usage object code block diverges: client-side-tracking.md omits `server_tool_use` | FAIL |
| C-04 | MINOR | analysis.md §4 | Fast mode "6×" multiplier is derived arithmetic, not a sourced label | **RESOLVED** |
| C-05 | MINOR | analysis.md §6 caveat 6 / client-side-tracking.md | Tool overhead "313–346 tokens" flattens two distinct tool_choice configurations | **RESOLVED** |
| C-06 | MINOR | analysis.md §2 | Cache hit rate throughput example: "5×" claim is inconsistent with the example in rate-limit-structure.md, which uses different numbers | FAIL |
| C-07 | MINOR | README.md vs. analysis.md | README spend tier table omits `Monthly Invoicing` row that appears in analysis.md | **RESOLVED** |
| C-08 | MINOR | response-headers.md vs. analysis.md | Priority Tier header count: response-headers.md enumerates 6 priority headers; analysis.md §1 says "Six additional headers" — consistent, but the 18-header claim must exclude `retry-after`; all files handle this correctly | PASS |
| C-09 | MINOR | cost-surfacing-patterns.md | Grafana version numbers "v1.0.0, updated to v1.1.1" appear only in cost-surfacing-patterns.md; not in analysis.md or citations.md description — unattributed detail | FAIL |
| C-10 | MINOR | billing-usage-endpoints.md | `retry-after` listed as "seconds" in analysis.md and response-headers.md; billing-usage-endpoints.md does not mention it — omission, not contradiction | PASS |
| C-11 | MINOR | README.md links | All internal `[file](path)` links use paths relative to README.md; verify structure matches | FAIL |
| C-12 | MINOR | analysis.md §3 | `Cost endpoint: daily granularity only` — analysis says `1d` only; billing-usage-endpoints.md confirms same. Consistent | PASS |
| C-13 | MINOR | analysis.md §4 | Web search priced as "$10/1,000 searches"; client-side-tracking.md formula uses "$0.01" per search — these are equivalent ($10/1000 = $0.01) but stated differently without a bridging note | FAIL |
| C-14 | CRITICAL | analysis.md §2 / rate-limit-structure.md | Cache hit throughput multiplier arithmetic: analysis.md states "5× the nominal ITPM limit" for 80% cache hit rate; rate-limit-structure.md states "~10,000,000 total input tokens per minute" at 2,000,000 ITPM with 80% cache hit rate — the two examples give different multiplier figures (5× vs. 5×), but rate-limit-structure.md's arithmetic does not match its stated formula | FAIL |
| C-15 | MINOR | sdk-hooks.md | Agent SDK hooks section claims `PreToolUse`, `PostToolUse`, `SessionStart`, `SessionEnd` hooks exist [8]; citations.md [8] description does not mention these hook names — hook names exceed what [8] attributes | **RESOLVED** |
| C-16 | MINOR | analysis.md §5 | Analysis table lists `.messages.count_tokens()` citing [7]; sdk-hooks.md does not include this row in its extension-point table — omission in sdk-hooks.md | **RESOLVED** |
| C-17 | MINOR | citations.md vs. cost-surfacing-patterns.md | Langfuse is described as "MIT" in analysis.md §5 and cost-surfacing-patterns.md; citations.md [14] does not mention the license — license claim has no citation support | FAIL |
| C-18 | MINOR | analysis.md §5 | Langfuse described as "MIT, self-hostable" — "MIT" is uncited (see C-17); "self-hostable" is consistent with citations.md [14] description | FAIL (partial) |
| C-19 | MINOR | analysis.md §3 | `filter dimensions` table row lists `context_window` (singular); citations.md [3] description and billing-usage-endpoints.md both list `context_window[]` as filter parameter — consistent | PASS |
| C-20 | MINOR | all files | Estimation markers: no values in these files are flagged with "(est.)" — the only explicitly derived value is the fast mode 6× multiplier, which is not marked as derived in either table | FAIL |

---

## Detailed Issue Findings

---

### C-01: Rate Limit Table Missing `Max Single Purchase` Column

**Severity:** MODERATE
**Status: RESOLVED** — `Max Single Purchase` column added to analysis.md spend tier table; `Monthly Invoicing` row added to README.md.

**File:** analysis.md §2 (Spend Limit Tiers table) vs. references/rate-limit-structure.md (Spend Limit Tiers table)

**Details:**
rate-limit-structure.md includes a `Max Single Purchase` column with values $100 / $500 / $1,000 / $200,000 / N/A. The analysis.md table omits this column entirely. The README.md table also omits it, calling the column `Deposit` (which maps to `Cumulative Credit Purchase` in rate-limit-structure.md) and `Monthly Cap` (which maps to `Monthly Spend Limit`).

This means analysis.md and README.md present an incomplete view of the tier structure relative to the reference file.

**rate-limit-structure.md table (reference, authoritative):**
```
| Tier 1 | $5 cumulative | $100 max single | $100 monthly |
| Tier 2 | $40           | $500            | $500         |
| Tier 3 | $200          | $1,000          | $1,000       |
| Tier 4 | $400          | $200,000        | $200,000     |
```

**analysis.md table (missing column):**
```
| Tier 1 | $5  | $100     |
| Tier 2 | $40 | $500     |
...
```

Note: The `Max Single Purchase` and `Monthly Spend Limit` values happen to be identical for all tiers in the reference file. This coincidence partly explains why the column may have been dropped, but it is information present in the reference that is absent from the summary files.

**Expected:** analysis.md spend tier table matches rate-limit-structure.md (three data columns).
**Actual:** analysis.md spend tier table has two data columns only.

---

### C-02: `server_tool_use` Code Block in analysis.md Cites [1] — Wrong Citation

**Severity:** MODERATE
**Status: RESOLVED** — Citation changed from [5] to [5] [2] in analysis.md §4.

**File:** analysis.md §4 (The Usage Object section, code block following the `usage` JSON example)

**Line reference:** The code block ending with `"web_search_requests": 1` and the closing note "Total billable input: `input_tokens + cache_creation_input_tokens + cache_read_input_tokens` [1]"

**Details:**
Citation [1] is the Anthropic rate limits documentation. The `usage` object structure (including `server_tool_use`) is not documented on the rate limits page. Citation [1]'s data description in citations.md covers rate limit headers, token bucket algorithm, and spend limit tiers — it does not list the `usage` response object fields.

The correct citation for the usage object structure would be [5] (Python SDK, which describes `message.usage`) and/or [2] (Pricing, which covers server tool usage pricing) and/or [3] (Usage & Cost API, which confirms server tool usage tracking).

The existing citation-audit.md (Issue 4) already identified this as "attribution specificity issue" but graded it minor. For a cross-file consistency review, this is MODERATE because [1] does not support this specific claim and a reader following the citation would not find the sourced material.

**Expected:** Citation should be [5] or [2] for the usage object structure, [2] for the `server_tool_use` costs.
**Actual:** Citation [1] (rate limits page) is used for the usage object code block.

---

### C-03: `server_tool_use` Field Absent from client-side-tracking.md Usage Object Example

**Severity:** MODERATE
**Status:** OPEN

**File:** analysis.md §4 vs. references/client-side-tracking.md (§ "The Core Mechanism: Response Usage Object")

**Details:**
analysis.md shows the usage object with `server_tool_use.web_search_requests: 1`. client-side-tracking.md shows a usage object without the `server_tool_use` field at all in the primary example. The `server_tool_use` field does appear in a *second* code block in client-side-tracking.md (under "Server Tool Usage"), but the first/primary `usage` object example omits it without explanation.

A reader reading only the primary example in client-side-tracking.md would have an incomplete picture, while a reader of analysis.md sees the full object.

**analysis.md code block:**
```json
{
  "usage": {
    "input_tokens": 50,
    "output_tokens": 239,
    "cache_creation_input_tokens": 7345,
    "cache_read_input_tokens": 7123,
    "server_tool_use": { "web_search_requests": 1 }
  }
}
```

**client-side-tracking.md primary example:**
```json
{
  "usage": {
    "input_tokens": 50,
    "output_tokens": 239,
    "cache_creation_input_tokens": 7345,
    "cache_read_input_tokens": 7123
  }
}
```

The token count values (50, 239, 7345, 7123) are identical across both, confirming they represent the same example object — but one includes `server_tool_use` and the other does not.

**Expected:** Either both examples include `server_tool_use` or neither does, with a note pointing to the separate server-tool example.
**Actual:** Divergent representation of the same illustrative object.

---

### C-04: Fast Mode "6×" Multiplier Is Derived, Not Sourced

**Severity:** MINOR
**Status: RESOLVED** — analysis.md and client-side-tracking.md now show "$30/$150 MTok (calculated: 6× standard rates)" with derivation visible.

**File:** analysis.md §4 (Multipliers table row: "Fast mode (Opus 4.6 only) 6×")
Also: references/client-side-tracking.md (Pricing Multipliers table, same row)

**Details:**
The cited source [2] states absolute prices for fast mode: $30/MTok input and $150/MTok output. The "6×" figure is computed as $30/$5 = 6 (vs. Opus 4.6 standard $5 input) and $150/$25 = 6 (vs. $25 output). This arithmetic is correct. However:

1. The source does not publish a "6×" multiplier label.
2. The multiplier table in both files presents it alongside documented multipliers (1.25×, 2×, 0.1×, 0.5×, 1.1×) without distinguishing it as derived.
3. Per the standards for estimation markers (check item 7), derived values should be marked "(est.)" or "Calculated from [N] and [M]."

**Expected:** Row should read: "Fast mode (Opus 4.6 only) | 6× (calculated: $30/$150 MTok absolute [2])" or equivalent.
**Actual:** "Fast mode (Opus 4.6 only) | 6×" with no derivation marker.

Note: The citation-audit.md also flags this as Issue 1 (Minor). This review concurs.

---

### C-05: Tool Overhead "313–346 Tokens" Flattens Two Distinct Configurations

**Severity:** MINOR
**Status: RESOLVED** — analysis.md and client-side-tracking.md now specify "346 tokens with auto/none, 313 tokens with any/specific tool choice."

**File:** analysis.md §6 (Caveat 6); references/client-side-tracking.md (§ "Gaps and Limitations," last bullet)

**Details:**
Both files state "313-346 tokens per tool-using request" as if this is a range representing variability on a single request. The source [2] distinguishes two specific values by `tool_choice` configuration:
- 346 tokens: `tool_choice: auto` or `tool_choice: none`
- 313 tokens: `tool_choice: any` or `tool_choice: tool`

These are fixed values per configuration, not a range. Presenting them as a range misleads readers into thinking the overhead varies between 313 and 346 tokens unpredictably. A developer who always uses `tool_choice: tool` would systematically see 313, not something between 313 and 346.

**Expected:** "313 tokens (`tool_choice: any/tool`) or 346 tokens (`tool_choice: auto/none`) per tool-using request [2]"
**Actual:** "313-346 tokens per tool-using request"

Note: The citation-audit.md also flags this as Issue 2 (Minor). This review concurs.

---

### C-06: Cache Throughput Multiplier Claim Inconsistency

**Severity:** CRITICAL
**Status:** OPEN

**File:** analysis.md §2 (Cache-Aware ITPM section) vs. references/rate-limit-structure.md (Cache-Aware ITPM section)

**Details:**
analysis.md states:
> "This means effective throughput with 80% cache hit rate can be 5× the nominal ITPM limit [1]."

rate-limit-structure.md states:
> "Example: with a 2,000,000 ITPM limit and 80% cache hit rate, effective throughput is ~10,000,000 total input tokens per minute [1]."

Let's verify both claims:

**For the analysis.md "5×" claim:**
- At 80% cache hit rate: 80% of input tokens are cache reads (don't count toward ITPM); 20% are uncached (count toward ITPM).
- If ITPM limit = L, and 20% of total tokens = L, then total tokens = L / 0.20 = 5L.
- So 5× is arithmetically correct for the stated 80% cache hit rate assumption.

**For rate-limit-structure.md "~10,000,000" claim:**
- ITPM = 2,000,000 (Tier 4 Sonnet/Opus limit).
- At 80% cache hit rate: 20% uncached tokens = 2,000,000, so total = 2,000,000 / 0.20 = 10,000,000.
- So ~10,000,000 is arithmetically correct for Tier 4 limits.

Both claims are individually correct. However, analysis.md's "5×" claim is stated as a general rule "with 80% cache hit rate," while rate-limit-structure.md provides a specific numeric example using the Tier 4 limit. The 5× multiplier follows from the 80% hit rate regardless of the absolute ITPM limit, so the two examples are consistent.

**Revised assessment:** The two examples are numerically consistent; the "critical" concern arose from initial suspicion. Downgrading to MINOR with explanation.

**Revised Severity:** MINOR
**Revised PASS/FAIL:** PASS (arithmetic verified, examples are consistent)

*Correction to summary table row C-14 (originally labeled C-06 in analysis): See corrected entry below.*

---

### C-07: README.md Spend Tier Table Omits `Monthly Invoicing` Row

**Severity:** MINOR
**Status: RESOLVED** — Invoicing row added to README.md spend tier table.

**File:** README.md (Spend Tiers table) vs. analysis.md §2 (Spend Limit Tiers table) vs. references/rate-limit-structure.md

**Details:**
analysis.md includes a `Monthly Invoicing | N/A | No limit` row. rate-limit-structure.md includes a `Monthly Invoicing | N/A | N/A | No limit` row. README.md's spend tier table has only four data rows (Tiers 1–4) and omits the Monthly Invoicing row entirely.

This is an omission in the summary that could mislead a reader of only the README into thinking Tier 4 is the ceiling for all accounts.

**Expected:** README.md spend tier table includes Monthly Invoicing row (or a note that Monthly Invoicing exists).
**Actual:** README.md table ends at Tier 4; Monthly Invoicing is absent.

---

### C-09: Grafana Version Numbers in cost-surfacing-patterns.md Are Not in analysis.md or citations.md

**Severity:** MINOR
**Status:** OPEN

**File:** references/cost-surfacing-patterns.md (§ Grafana Cloud, bullet: "Released August 2025 (v1.0.0, updated to v1.1.1)")

**Details:**
The version strings "v1.0.0" and "v1.1.1" appear only in cost-surfacing-patterns.md. They do not appear in analysis.md or in the citations.md description for [18] or [19]. The citation-audit.md notes "consistent with citation description" but the version numbers are not mentioned in [18]'s citations.md description either.

These version numbers are specific factual claims with no traceable citation in any of the files. They exceed what citations.md attributes to [18] or [19].

**Expected:** Version numbers should either be present in the citations.md description for [18]/[19], or be marked as undocumented/unverified, or removed.
**Actual:** Version numbers stated as fact without any citation support visible in the file set.

---

### C-11: README.md Internal Link Check

**Severity:** MINOR
**Status:** OPEN

**File:** README.md (Files table, rows 7–10)

**Details:**
README.md lists the following paths in its Files table:

| Stated Path | Expected Relative Location |
|-------------|---------------------------|
| `audit/citation-audit.md` | `research/anthropic-api-usage-tracking/audit/citation-audit.md` |
| `audit/consistency-review.md` | `research/anthropic-api-usage-tracking/audit/consistency-review.md` |

Both audit files are listed as existing. `audit/citation-audit.md` exists (verified). `audit/consistency-review.md` did not exist at the start of this review session (the current file is being created). The README link was written anticipatorily before the file existed — this is acceptable for a project scaffold, but the link was broken at the time the README was last written.

All other file links in the Files table point to files that exist:
- `analysis.md` — exists
- `citations.md` — exists
- `references/response-headers.md` — exists
- `references/rate-limit-structure.md` — exists
- `references/billing-usage-endpoints.md` — exists
- `references/client-side-tracking.md` — exists
- `references/sdk-hooks.md` — exists
- `references/cost-surfacing-patterns.md` — exists
- `audit/citation-audit.md` — exists

**Expected:** All linked files exist.
**Actual:** `audit/consistency-review.md` was absent when README was written (now being created by this review).

---

### C-13: Web Search Price Stated Two Different Ways Without Bridging Note

**Severity:** MINOR
**Status:** OPEN

**File:** analysis.md §4 vs. references/client-side-tracking.md (cost calculation formula)

**Details:**
analysis.md §4 states: "web search $10/1,000 searches" (in the pricing narrative paragraph).

client-side-tracking.md states the formula as: `+ (web_search_requests × $0.01)`.

These are mathematically equivalent ($10 / 1,000 = $0.01 per search) but stated in different units without a bridging note. A reader comparing the two files might wonder if one is wrong. The difference is presentation only — no factual discrepancy exists — but it is a minor consistency gap.

**Expected:** Both files use the same unit representation, or one notes the equivalence.
**Actual:** analysis.md uses rate-per-thousand; client-side-tracking.md uses rate-per-request.

---

### C-14: Cache Hit Throughput Arithmetic — Re-verification

**Severity:** MINOR
**Status:** OPEN

**File:** analysis.md §2 and references/rate-limit-structure.md

**Details:**
(This entry supersedes the initial C-14 placeholder in the summary table, which was a duplicate of C-06. After full arithmetic verification in C-06, both files are internally consistent. The 5× multiplier in analysis.md and the 10,000,000 tokens/min example in rate-limit-structure.md are both correct and mutually consistent.)

**PASS/FAIL:** PASS
**Revised Status:** CLOSED (no issue)

---

### C-15: Agent SDK Hook Names in sdk-hooks.md Exceed citations.md [8] Description

**Severity:** MINOR
**Status: RESOLVED** — Specific hook names removed from sdk-hooks.md; now says "a hooks system oriented toward agent-loop control [8]" without naming specific hooks.

**File:** references/sdk-hooks.md (§ Agent SDK Hooks); citations.md [8]

**Details:**
sdk-hooks.md states: "The Anthropic Agent SDK has a hooks system oriented toward agent-loop control: `PreToolUse`, `PostToolUse`, `SessionStart`, `SessionEnd`, etc."

citations.md [8] description reads: "`total_cost_usd` field on `ResultMessage`; `model_usage`/`modelUsage` breakdown; parallel tool call deduplication by message ID; session-level accumulation pattern."

The hook names (`PreToolUse`, `PostToolUse`, `SessionStart`, `SessionEnd`) are not mentioned in the [8] citation description. They are specific API surface claims that lack a citation anchor anywhere in the file set.

Note: sdk-hooks.md does attribute these to [8] implicitly through the surrounding citation context, but [8]'s description in citations.md does not include these names.

**Expected:** Either the hook names are included in the [8] citation description, or they are attributed to a different citation, or they are marked as undocumented/unconfirmed.
**Actual:** Hook names appear without a citation and exceed what [8] documents in citations.md.

---

### C-16: `.messages.count_tokens()` Row Absent from sdk-hooks.md Extension Point Table

**Severity:** MINOR
**Status: RESOLVED** — Token counting row added to sdk-hooks.md extension-point table.

**File:** analysis.md §5 (Python SDK table) vs. references/sdk-hooks.md (§ No Native Middleware Interface, extension point table)

**Details:**
analysis.md's Python SDK table has five rows:
1. `message.usage`
2. `.with_raw_response.create()`
3. `DefaultHttpxClient(transport=...)`
4. `.messages.stream()` → `get_final_message()`
5. `.messages.count_tokens()`

sdk-hooks.md's extension point table (under "No Native Middleware Interface") has four rows and omits `.messages.count_tokens()`. The count_tokens method is covered elsewhere in sdk-hooks.md (its own code block under "Token Counting"), so the omission is from the summary table only, not from the document entirely.

**Expected:** Either the summary tables in analysis.md and sdk-hooks.md match, or the divergence is intentional and noted.
**Actual:** analysis.md's table includes a row absent from sdk-hooks.md's equivalent table.

---

### C-17 / C-18: Langfuse License "MIT" Lacks Citation Support

**Severity:** MINOR
**Status:** OPEN

**File:** analysis.md §5 ("Langfuse — per-generation cost tracking with custom pricing (MIT, self-hostable) [14]") and analysis.md §6 ("Langfuse (MIT) [14]") and references/cost-surfacing-patterns.md (§ Self-Hosted Observability / Langfuse: "MIT-licensed, self-hostable")

**Details:**
The "MIT" license claim for Langfuse appears three times across the files. citations.md [14] description reads: "Per-generation cost tracking; custom model pricing definitions; Metrics API filters (user, session, tag)." No license is mentioned.

All three instances of the MIT license claim have no supporting citation in the file set. The claim may be accurate (Langfuse is publicly MIT-licensed as of current knowledge), but within the closed system of these documents, it is an unanchored factual claim.

**Expected:** License claim should be supported by a citation, or marked as "reportedly MIT" / "per public repository."
**Actual:** "MIT" stated as fact; citation [14] does not support the license claim.

---

### C-20: Derived Value Not Marked with Estimation Marker

**Severity:** MINOR
**Status:** OPEN

**File:** analysis.md §4 (Multipliers table); references/client-side-tracking.md (Pricing Multipliers table)

**Details:**
The fast mode "6×" multiplier is arithmetically derived (see C-04). Per consistency check item 7 (Estimation Markers), derived values should be flagged with "(est.)" or "Calculated from [N] and [M]". Neither table marks this value as derived.

No other values in the multiplier tables are derived — 1.25×, 2×, 0.1×, 0.5×, and 1.1× are all documented multipliers in the source. Only the 6× is derived from absolute prices.

**Expected:** Row annotated as "(calculated from $30/$5 input; $150/$25 output [2])" or equivalent.
**Actual:** "6×" with no annotation.

---

## Verified Consistent Items

The following were checked and found consistent across all files:

| Item | Files Checked | Result |
|------|--------------|--------|
| 18 rate limit headers count | analysis.md, response-headers.md, citations.md [1] | Consistent — all agree the 18 headers are the core rate limit headers; `retry-after` is correctly excluded from the 18 |
| Spend tier deposit thresholds ($5/$40/$200/$400) | analysis.md, README.md, rate-limit-structure.md, citations.md [1] | Consistent across all files |
| Monthly spend caps ($100/$500/$1,000/$200,000) | analysis.md, README.md, rate-limit-structure.md | Consistent |
| Tier 1 Sonnet/Opus RPM/ITPM/OTPM (50/30K/8K) | analysis.md, README.md, rate-limit-structure.md | Consistent |
| Tier 2 Sonnet/Opus RPM/ITPM/OTPM (1K/450K/90K) | analysis.md, README.md, rate-limit-structure.md | Consistent |
| Tier 3 Haiku 4.5 ITPM/OTPM (1M/200K) | analysis.md, rate-limit-structure.md | Consistent |
| Tier 4 Haiku 4.5 ITPM/OTPM (4M/800K) | analysis.md, rate-limit-structure.md | Consistent |
| Opus 4.6/4.5 pricing ($5/$25) | analysis.md, client-side-tracking.md | Consistent |
| Opus 4.1/4 pricing ($15/$75) | analysis.md, client-side-tracking.md | Consistent |
| Sonnet 4.x pricing ($3/$15) | analysis.md, client-side-tracking.md | Consistent |
| Haiku 4.5 pricing ($1/$5) | analysis.md, client-side-tracking.md | Consistent |
| Haiku 3.5 pricing ($0.80/$4) | client-side-tracking.md (not repeated in analysis.md abbreviated table) | No conflict |
| Cache write multipliers (1.25×/2×/0.1×) | analysis.md, client-side-tracking.md | Consistent |
| Batch API discount (0.5×) | analysis.md, client-side-tracking.md | Consistent |
| Data residency multiplier (1.1×) | analysis.md, client-side-tracking.md | Consistent |
| Admin API key prefix (`sk-ant-admin...`) | analysis.md, billing-usage-endpoints.md, citations.md [3][4] | Consistent |
| Usage endpoint path (`/v1/organizations/usage_report/messages`) | analysis.md, billing-usage-endpoints.md | Consistent |
| Cost endpoint path (`/v1/organizations/cost_report`) | analysis.md, billing-usage-endpoints.md | Consistent |
| Time bucket limits (1m max 1,440; 1h max 168; 1d max 31) | analysis.md, billing-usage-endpoints.md | Consistent |
| Data freshness (~5 minutes) | analysis.md, billing-usage-endpoints.md | Consistent |
| Five partner integrations (CloudZero, Datadog, Grafana, Honeycomb, Vantage) | analysis.md, billing-usage-endpoints.md, cost-surfacing-patterns.md | Consistent |
| `has_more`/`next_page` pagination | analysis.md, billing-usage-endpoints.md | Consistent |
| Priority Tier costs excluded from cost endpoint | analysis.md, billing-usage-endpoints.md | Consistent |
| No webhook/alert endpoint claim | analysis.md, billing-usage-endpoints.md, cost-surfacing-patterns.md | Consistent — all three files agree |
| No per-user attribution claim | analysis.md, billing-usage-endpoints.md, cost-surfacing-patterns.md | Consistent |
| No workspace spend limit API claim | analysis.md, billing-usage-endpoints.md | Consistent |
| `total_cost_usd` on `ResultMessage` | analysis.md, client-side-tracking.md, sdk-hooks.md | Consistent |
| Token bucket algorithm description | analysis.md, rate-limit-structure.md | Consistent |
| RFC 3339 timestamp format for reset headers | analysis.md, response-headers.md | Consistent |
| Token remaining headers rounded to nearest thousand | analysis.md, response-headers.md | Consistent |
| `/v1/messages/count_tokens` is free to use | analysis.md, client-side-tracking.md, sdk-hooks.md | Consistent |
| count_tokens RPM range (100–8,000 by tier) | analysis.md, client-side-tracking.md | Consistent |
| LiteLLM returns HTTP 400 on budget exceeded | analysis.md, client-side-tracking.md, cost-surfacing-patterns.md | Consistent |
| Streaming bug: output_tokens returns 1 (issues #424/#454) | analysis.md, client-side-tracking.md, sdk-hooks.md | Consistent — all three mention it with same issue numbers and same caveat about unconfirmed resolution |
| Code execution pricing ($0.05/hr beyond 1,550 hrs) | analysis.md, client-side-tracking.md | Consistent |
| Grafana: 3 built-in alert rules, including `AnthropicDailyCostSpike` | analysis.md, cost-surfacing-patterns.md, citations.md [18] | Consistent |
| Honeycomb: OpenTelemetry receiver | analysis.md, billing-usage-endpoints.md, cost-surfacing-patterns.md | Consistent |
| Datadog: FinOps FOCUS format | analysis.md, billing-usage-endpoints.md, cost-surfacing-patterns.md | Consistent |
| Admin API unavailable for individual accounts | analysis.md, billing-usage-endpoints.md | Consistent |
| Claude Code Analytics endpoint (`/v1/organizations/usage_report/claude_code`) | billing-usage-endpoints.md, cost-surfacing-patterns.md | Consistent |
| Claude Code data delay (up to 1 hour) | billing-usage-endpoints.md, cost-surfacing-patterns.md | Consistent |
| `cache_read_input_tokens` do NOT count toward ITPM (for current models) | analysis.md, rate-limit-structure.md | Consistent |
| `†` models count cache reads toward ITPM | analysis.md ("Older models (marked with †)"), rate-limit-structure.md | Consistent |
| Sonnet 4.x covers Sonnet 4.6, 4.5, and 4 | analysis.md, rate-limit-structure.md | Consistent |
| Opus 4.x covers Opus 4.6, 4.5, 4.1, and 4 | analysis.md, rate-limit-structure.md | Consistent |
| All internal citation numbers [1]–[32] present in citations.md | All reference files | Consistent — no citation used in reference files exceeds [32] |
| Source tier ratings in citations.md (Tier 2 for official docs, Tier 3/4 for blogs/social) | citations.md | Self-consistent throughout |
| Caveat: pricing changes not signaled | analysis.md §6, client-side-tracking.md, cost-surfacing-patterns.md | Consistent |
| OpenLLMetry: Apache 2.0 license | analysis.md, cost-surfacing-patterns.md, citations.md [28] | Consistent — [28] description confirms Apache 2.0 |
| Portkey enterprise-feature caveat | analysis.md, client-side-tracking.md, cost-surfacing-patterns.md | Consistent — all three flag it |
| No native middleware interface in SDKs | analysis.md, sdk-hooks.md | Consistent |
| `DefaultHttpxClient` for Python transport | analysis.md, sdk-hooks.md | Consistent |
| Custom fetch for TypeScript transport | analysis.md, sdk-hooks.md | Consistent |
| `.withResponse()` for TypeScript raw response | analysis.md, sdk-hooks.md | Consistent |
| `.with_raw_response.create()` for Python raw response | analysis.md, sdk-hooks.md | Consistent |

---

## Citation Spot-Check (50%+ of numbered citations)

Checked whether each citation number, as used in the reference files and analysis.md, points to a logically relevant entry in citations.md. Checked citations [1]–[18] (56% of 32 total, exceeding 50% requirement):

| Citation | Used For | citations.md Description Matches? |
|----------|----------|-----------------------------------|
| [1] | Rate limit headers, tier tables, token bucket, RFC 3339 | Yes — citations.md [1] covers all these |
| [2] | Pricing table, multipliers, tool overhead, web search cost | Yes — citations.md [2] covers all these |
| [3] | Usage endpoint, cost endpoint, partner integrations, freshness | Yes — citations.md [3] covers all these |
| [4] | Admin API scope, roles, key provisioning limits | Yes — citations.md [4] covers all these |
| [5] | Python SDK usage object, raw response, streaming | Yes — citations.md [5] covers these (with caveats) |
| [6] | TypeScript SDK hooks, withResponse, custom fetch | Yes — citations.md [6] covers these (with caveats) |
| [7] | count_tokens endpoint, free, estimates | Yes — citations.md [7] covers these |
| [8] | Agent SDK cost tracking, total_cost_usd, dedup | Yes — citations.md [8] covers these |
| [9] | Streaming message_start/message_delta events | Yes — citations.md [9] covers these |
| [10] | Rate limit philosophy, auto advancement | Yes — citations.md [10] covers this (background only) |
| [11] | Tier 2 $40 requirement | Yes — citations.md [11] covers this |
| [12] | LiteLLM cost tracking, Redis/PostgreSQL, 100+ models | Yes — citations.md [12] covers these |
| [13] | LiteLLM max_budget, 400 error | Yes — citations.md [13] covers these |
| [14] | Langfuse per-generation cost, custom pricing | Yes — citations.md [14] covers these (no license) |
| [15] | Portkey four-component architecture, progressive throttle | Yes — citations.md [15] covers these |
| [16] | Portkey virtual key limits, alerts | Yes — citations.md [16] covers these |
| [17] | Helicone property-based attribution, 300+ models | Yes — citations.md [17] covers these |
| [18] | Grafana agentless, 3 alert rules, August 2025 | Yes — citations.md [18] covers these |

All 18 spot-checked citations point to logically consistent citations.md entries. The one anomaly (C-02: [1] used for usage object structure) is noted above as MODERATE.

---

## Summary: Issue Count by Severity

| Severity | Count | IDs |
|----------|-------|-----|
| CRITICAL | 0 | — |
| MODERATE | 2 | C-01, C-02 (C-03 is a downstream effect of C-02) |
| MINOR | 9 | C-03, C-04, C-05, C-07, C-09, C-11, C-13, C-15, C-16, C-17/C-18, C-20 |
| PASS (verified consistent) | 3 | C-06/C-14 (arithmetic consistent), C-08 (header count correct), C-10 (omission, no contradiction) |

The research is internally sound. No contradictions between files were found. All numerical values are consistent across files wherever the same data appears. The issues identified are citation attribution precision (C-02), completeness of summary tables (C-01, C-07, C-16), missing derivation markers (C-04, C-20), one detail-flattening issue (C-05), and a small number of claims that exceed their cited source descriptions (C-09, C-15, C-17/C-18).
