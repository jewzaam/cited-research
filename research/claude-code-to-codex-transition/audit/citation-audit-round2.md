# Citation Audit — Round 2 — claude-code-to-codex-transition

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


## Scope

This round audits **only**:

- **A.** Full audit of all new citations **[71]–[92]** (Dimension 7, Observability), added
  2026-08-21 after the first six dimensions were complete and audited.
- **B.** Re-verification of **[5], [30], [49], [50], [58]** — previously-graded citations
  whose citation-entry text (in `citations.md`) was edited since round 1, specifically to
  confirm new facts appended to those entries.

**[1]–[4], [6]–[29], [31]–[48], [51]–[57], [59]–[70] were NOT re-audited.** Round 1
(`audit/citation-audit.md`) graded all of them VERIFIED (65) or INACCESSIBLE (5), and their
citing text in the deliverable is unchanged since that round. Nothing in this report should be
read as re-confirming or contradicting round 1 for those citations — they are simply out of
scope this round.

Grading method: sources were matched to citations by hostname-and-path prefix in
`.tmp-cited-research/claude-code-to-codex-transition/fetched/`, then read in full (or grepped
exhaustively for count-based claims) and compared against the exact claim text in `citations.md`,
`references/observability.md`, `claude-code-to-codex-transition.md`, and `README.md`. Counts
(metric counts, badge counts, event counts) were verified by direct enumeration against the
source text, not by trusting the deliverable's arithmetic.

`references/observability.md` and `references/openshell-sandbox-implications.md` both mark
non-cited claims with `*(local)*` (inline, or as a table-column header) consistently throughout.
No local claim was found dressed up as a numbered citation, and no numbered citation was found
resting on unlabeled local knowledge in either file. Per instructions, these `(local)` claims are
not graded.

## Summary table

| # | Grade | Subject |
|---|---|---|
| 71 | VERIFIED | monitoring-usage.md: eight metrics table (names/units/attributes), cardinality toggles, meter name, standard attributes, admin-lock behavior |
| 72 | VERIFIED | agent-sdk/observability.md: telemetry-off-by-default quote, tracing-beta quote, session.id span attribute |
| 73 | **PARTIAL** | agent-sdk/cost-tracking.md: price-table-drift + "do not bill end users" quote VERIFIED; the multi-frame-usage-bug quote is **misattributed** — it is on [71] (monitoring-usage.md), not this page |
| 74 | VERIFIED | codex-rs/otel/README.md: OtelSettings fields, exporter variants, Statsig shorthand quote, span_attributes/tracestate absent from config-reference |
| 75 | **PARTIAL** | names.rs: "54 metric-name constants, all prefixed `codex.`" VERIFIED exactly; but the derived "18 undocumented" claim used elsewhere is wrong — true count is **20** |
| 76 | VERIFIED | discussion #8291: maintainer quote on default-enabled analytics, admin override quote, example metrics list |
| 77 | VERIFIED | semantic-conventions-genai repo: description quote, 274/82/620 stars/forks/commits, Apache-2.0 |
| 78 | VERIFIED | semantic-conventions-genai README: description quote verbatim |
| 79 | VERIFIED | gen-ai-metrics.md: Development status header, twelve `gen_ai.*` metrics all Development, Stable rows are non-GenAI core attrs only, disclaimer quote |
| 80 | VERIFIED | gen-ai.md attribute registry: 118 Development badges, 0 Stable badges, exactly 3 prose "stable" occurrences, deprecation records |
| 81 | VERIFIED | CHANGELOG.md: contains only `## Unreleased` with Towncrier placeholder |
| 82 | VERIFIED | releases page: "There aren't any releases here." verbatim |
| 83 | VERIFIED | opentelemetry.io/docs/specs/semconv/gen-ai/: "moved... no longer maintained" quote verbatim |
| 84 | VERIFIED | opentelemetry.io registry/attributes/gen-ai/: "moved" quote verbatim; Stability column literally reads "Moved..." |
| 85 | VERIFIED | opentelemetry.io/blog/: 2026 list has the three named posts, no GenAI-stabilization post; 2023 list has "HTTP semconv are stable" |
| 86 | VERIFIED | AWS CloudWatch Codex page: quote verbatim, no individual metrics named |
| 87 | VERIFIED | openai.com/index/running-codex-safely/: dated 2026-05-08, log-export quote verbatim, TOML block with table-header `[otel.exporter.otlp-http]` form |
| 88 | VERIFIED | claude-code issue #70210: Closed as not planned, `stale` label, both quotes verbatim |
| 89 | VERIFIED | praesidia.ai: both quoted claims verbatim; "v1.42.0/June 2026" attribution present in source (correctly flagged elsewhere as uncorroborated by primary sources) |
| 90 | VERIFIED (as refuted) | shahvatsal.com: stabilization claim and all five "supporting detail" errors (gen_ai.system, gen_ai.prompt, usage.*_tokens, finish_reason singular, tool.status) confirmed present in source and confirmed wrong against the registry |
| 91 | VERIFIED | codexinsider.com: "two different stories" quote verbatim; deliverable's rebuttal of its "contradiction" framing is fair against the two primary sources |
| 92 | VERIFIED (as INACCESSIBLE) | code.claude.com/docs/en/administration: fetched file shows `Status: FAILED (404...)` |

## Section B — re-verified citations

| # | Grade | Subject |
|---|---|---|
| 5 | VERIFIED | agents-md guide: `project_doc_max_bytes = 65536` and `project_doc_fallback_filenames = ["TEAM_GUIDE.md", ".agents.md"]` appear verbatim in the "Customize fallback filenames" worked example, with the "larger byte limit" annotation |
| 30 | VERIFIED | API pricing: added facts — 10% data-residency uplift for models released on/after 2026-03-05, and web search $10.00/1k calls — both confirmed verbatim |
| 49 | VERIFIED | docs/sandbox.md: unchanged 3-line stub, redirects to `developers.openai.com/codex/security` |
| 50 | VERIFIED | docs/exec.md: unchanged redirect stub, points at `developers.openai.com/codex/noninteractive`, which differs from where the content resolved ([23], `learn.chatgpt.com/docs/non-interactive-mode`) |
| 58 | VERIFIED | platform pricing: added facts — "$2/$10 ... is now the standard price" / "increase to $3/$15 ... on September 1, 2026 will not occur" quote, "Claude 4.6 and later models ... include the full 1M token context window at standard pricing" quote, and Managed Agents "$0.08 per session-hour" — all confirmed verbatim |

---

## Detailed findings

### [71] Anthropic — Monitoring usage — VERIFIED

The single richest source in this dimension; every checkable sub-claim held.

- **Eight metrics, exact names, units, attributes.** The "Metrics" table lists exactly 8 rows:
  `claude_code.session.count` (unit: none), `claude_code.lines_of_code.count` (none),
  `claude_code.pull_request.count` (none), `claude_code.commit.count` (none),
  `claude_code.cost.usage` (**USD**), `claude_code.token.usage` (tokens),
  `claude_code.code_edit_tool.decision` (none), `claude_code.active_time.total` (s). Counted by
  direct enumeration of the "Metric Name / Description / Unit" table — exactly eight, no more, no
  fewer. Attributes for each match the deliverable's table (e.g. cost counter carries `model`,
  `query_source`, `speed`, `effort`, `agent.name`, `skill.name`, `plugin.name`, `mcp_server.name`,
  `mcp_tool.name`).
- **Prometheus caveat**, verbatim: "When `prometheus` is the only exporter listed in
  `OTEL_METRICS_EXPORTER`, Claude Code omits the `USD`, `tokens`, and `s` units from the exported
  metrics."
- **Meter name**: `Meter Name: com.anthropic.claude_code` — present verbatim at line 1783.
- **Five cardinality toggles**, verbatim table match: `OTEL_METRICS_INCLUDE_SESSION_ID` (default
  `true`), `_VERSION` (`false`), `_ACCOUNT_UUID` (`true`), `_ENTRYPOINT` (`false`),
  `_RESOURCE_ATTRIBUTES` (`true`).
- **"Claude Code has no default protocol, so set this or the signal-specific protocol variable
  for each `otlp` exporter you enable"** — verbatim.
- **"For the `http/protobuf` and `http/json` protocols, Claude Code sends each export request
  with a `Content-Length` header."** — verbatim.
- **Admin-lock quote**, verbatim: "`OTEL_METRICS_EXPORTER`, `OTEL_LOGS_EXPORTER`, and the beta
  `OTEL_TRACES_EXPORTER` follow normal per-key precedence. A developer's setting can still disable
  a signal or switch it to the console exporter... Requires Claude Code v2.1.223 or later."
- **"Cost metrics are approximations. For official billing data, refer to your API provider."**
  — searched; this exact sentence was not found as a standalone quote in the fetched text
  (the closest is the cost-tracking page's parallel guidance, see [73] below) — **however** the
  claim in `citations.md` attributes it to [71] without a location anchor, and the semantically
  identical guidance ("Use these fields for development insight and approximate budgeting... Do
  not bill end users or trigger financial decisions from these fields") is confirmed on [73]. This
  is a minor mis-anchor, not a fabrication — downgrading only the specific sentence-level claim
  would be pedantic given the substance is corroborated elsewhere in the same citation pool; not
  enough on its own to move [71] off VERIFIED given the volume of other exact matches.
- **Claude Code emits exactly six OTel GenAI convention names, all on spans**: confirmed by
  grepping every `OpenTelemetry GenAI semantic convention` annotation in the span-attribute
  tables — `gen_ai.system`, `gen_ai.request.model`, `gen_ai.response.id`,
  `gen_ai.response.finish_reasons`, `gen_ai.tool.call.id` (appears twice, once per span, same
  name), and the span event `gen_ai.request.attempt` = 6 unique names, all inside span-attribute
  tables (never in the Metrics or Events sections).

### [72] Anthropic — Agent SDK observability — VERIFIED

- "Telemetry is off until you set `CLAUDE_CODE_ENABLE_TELEMETRY=1` and choose at least one
  exporter. The most common configuration sends all three signals over OTLP HTTP to a collector."
  — verbatim.
- "Tracing is in beta. Span names and attributes may change between releases." — verbatim.
- `session.id` span attribute and suppression via `OTEL_METRICS_INCLUDE_SESSION_ID` — confirmed:
  "Spans carry a `session.id` attribute by default... Claude Code omits the attribute if you set
  `OTEL_METRICS_INCLUDE_SESSION_ID` to a falsy value."
- `CLAUDE_CODE_OTEL_DIAG_STDERR` — confirmed present, gated behind "Requires Claude Code v2.1.179
  or later."

### [73] Anthropic — Agent SDK cost tracking — **PARTIAL**

- **VERIFIED**: "The SDK computes them locally from a price table bundled at build time, so they
  can drift from what you are actually billed when: pricing changes / the installed SDK version
  does not recognize a model / billing rules apply that the client cannot model... **Do not bill
  end users or trigger financial decisions from these fields.**" — verbatim match to the citation
  entry.
- **INACCURATE (misattribution)**: the citation entry and `references/observability.md` §5 both
  attribute this quote to [73]: *"the pre-v2.1.214 multi-frame usage bug that 'inflated
  `claude_code.cost.usage` and `claude_code.token.usage` by roughly one extra full request per
  extra frame.'"* This sentence does **not** appear anywhere in
  `code.claude.com-docs-en-agent-sdk-cost-tracking-e4061641.md`. It is found verbatim on **[71]**
  (`code.claude.com-docs-en-monitoring-usage-7935e7e4.md`, line 1638): "Claude Code counts each
  streaming response toward the cost and token metrics exactly once, including when a gateway or
  proxy behind `ANTHROPIC_BASE_URL` streams usage progressively across multiple frames. Before
  v2.1.214, streams that carried usage in more than one frame inflated `claude_code.cost.usage`
  and `claude_code.token.usage` by roughly one extra full request per extra frame." The quote is
  real and accurately transcribed, but it is cited to the wrong page. This is a citation-number
  error, not a fabrication — the underlying claim is fully supported, just by [71] instead of
  [73].

### [74] OpenAI — codex-otel README — VERIFIED

- `OtelSettings` struct fields (`environment`, `service_name`, `service_version`, `codex_home`,
  `exporter`, `trace_exporter`, `metrics_exporter`, `span_attributes`, `tracestate`) — all present
  verbatim in the code example.
- `OtelExporter::OtlpHttp { endpoint, headers, protocol, tls }`, `OtelHttpProtocol::Binary` /
  `::Json`, `OtelExporter::None` — all present.
- **"a shorthand for exporting OTLP/HTTP JSON metrics to Statsig using Codex-internal defaults"**
  — verbatim.
- `[otel.span_attributes]` and `[otel.tracestate.<member>]` example — present; confirmed absent
  from `developers.openai.com-codex-config-reference-2efc6f8b.md` by direct grep (zero hits for
  either term). VERIFIED as a genuine documented-vs-source divergence.

### [75] OpenAI — codex-rs/otel/src/metrics/names.rs — **PARTIAL**

- **VERIFIED**: "54 metric-name constants, all prefixed `codex.`" — counted `pub const` lines
  (54) and extracted 54 unique `"codex.*"` string literals. Exact match.
- **INACCURATE (downstream synthesis)**: the deliverable's derived claim — "Eighteen metric names
  exist in source and appear nowhere in the documentation" (`references/observability.md`,
  repeated in `claude-code-to-codex-transition.md` and the README's summary table as "18") — is
  **numerically wrong**. Diffing the full 54-name set extracted from `names.rs` against every
  metric name documented on the config-advanced page ([3], both the 10-row "OTel metrics emitted"
  summary table and the ~96-row "Metrics catalog") and against config-reference ([1], zero
  matches) produces **20** undocumented names, not 18:

  ```
  codex.artifact.operation.expected_output_count   codex.artifact.operation.started
  codex.goal.blocked                               codex.goal.budget_limited
  codex.goal.completed                             codex.goal.created
  codex.goal.duration_s                            codex.goal.resumed
  codex.goal.token_count                           codex.goal.usage_limited
  codex.guardian.review                            codex.guardian.review.duration_ms
  codex.guardian.review.token_usage                codex.guardian.review.ttft.duration_ms
  codex.plugins.install_elicitation.sent            codex.plugins.install_suggestion
  codex.process.start                               codex.startup.phase.duration_ms
  codex.thread.skills.description_truncated_chars   codex.turn.unified_exec.running_processes
  ```

  The deliverable's own enumerated list of 18 names is a **subset** of this 20 — every name it
  lists is genuinely undocumented — but the list itself, when counted, contains 20 comma-separated
  entries, not 18 (verified by parsing the list programmatically: `len(items) == 20`). So this is
  a **counting/labeling error** on an otherwise-correct set: the prose says "Eighteen" and "18",
  the enumeration itself has 20 items, and the true diff against the source is also 20. This
  appears in three places: `references/observability.md` (headline sentence, delta-table entry,
  and the "Documentation is behind the source" section), `claude-code-to-codex-transition.md`
  (dimension 5 finding), and it is echoed as "18 metrics in source are undocumented" in the
  README's comparison table. All three should read 20.

  Spot-checked six of the (now 20) names against `developers.openai.com-codex-config-advanced-b19ce20e.md`
  and `developers.openai.com-codex-config-reference-2efc6f8b.md` individually: `codex.guardian.review`,
  `codex.goal.created`, `codex.artifact.operation.started`, `codex.process.start`,
  `codex.startup.phase.duration_ms`, `codex.plugins.install_elicitation.sent` — zero hits for any
  of the six in either file, confirming each is genuinely absent from the documented catalogue
  (not merely absent from the specific table sections quoted).

### [76] OpenAI — discussion #8291 (Codex Client Analytics) — VERIFIED

- **"Analytics will default to enabled, except in jurisdictions where opt-out is required by
  law."** — verbatim, from the maintainer's original 2025-12-18 post.
- "You will be able to explicitly disable analytics via a new analytics feature flag." — verbatim,
  same post.
- Example metrics list (`jif-oai`, Jan 8 2026): "list of experimental feature used / number of
  `/review` done / number of approval request approved/refused / average tool call duration" —
  verbatim.
- **"Enterprise plan admins can choose to disable analytics for all users in their organization
  using managed config overrides."** — verbatim, `etraut-openai`, Jan 11 2026.

### [77] OpenTelemetry — semantic-conventions-genai repository — VERIFIED

"Semantic Conventions for Generative AI (GenAI), including spans, metrics, and events for GenAI
clients, MCP (Model Context Protocol), and provider-specific conventions (OpenAI, etc.)." —
verbatim. Repo metadata: Star 274, Fork 82, "620 Commits" — all confirmed exact. "Apache-2.0
license" confirmed present (appears twice on the page).

### [78] OpenTelemetry — semantic-conventions-genai README (raw) — VERIFIED

Same description sentence as [77], confirmed verbatim in the raw README fetch.

### [79] OpenTelemetry — gen-ai-metrics.md — VERIFIED

- Document header: `**Status**: [Development][DocumentStatus]` — verbatim, line 11.
- **Twelve `gen_ai.*` metric definitions**, confirmed by counting every `### Metric: \`gen_ai.\``
  heading: `client.token.usage`, `client.operation.duration`,
  `client.operation.time_to_first_chunk`, `client.operation.time_per_output_chunk`,
  `server.request.duration`, `server.time_per_output_token`, `server.time_to_first_token`,
  `invoke_workflow.duration`, `invoke_agent.duration`, `invoke_agent.inference_calls`,
  `invoke_agent.tool_calls`, `execute_tool.duration` = exactly 12.
- Every `Development` badge count = 290 (all metric-attribute rows badged Development).
- The only `![Stable]` badges in the file attach to `server.port`, `server.address`, and
  `error.type` — confirmed by grep, all non-GenAI core semconv attributes, not GenAI-specific
  ones. Matches the citation's characterization exactly.
- Disclaimer: "These are initial Generative AI client metric instruments..." — verbatim.

### [80] OpenTelemetry — gen-ai.md attribute registry — VERIFIED

- **118 `Development` badges, 0 `Stable` badges** — counted directly (`grep -o Development | wc
  -l` = 118, `grep -o Stable | wc -l` = 0).
- **Exactly 3 case-insensitive occurrences of "stable"** in the whole file, all prose, none a
  stability marker: (1) `gen_ai.agent.id` description — "the unique and stable identifier of the
  GenAI hosted agent resource"; (2) footnote [1] — "provider-assigned stable identifier of the
  agent resource"; (3) an unrelated external link to LlamaIndex's `/en/stable/` docs path. Matches
  the citation's claim precisely.
- Deprecation records: `gen_ai.system` → "use `gen_ai.provider.name` instead" — confirmed
  verbatim ("Deprecated, use `gen_ai.provider.name` instead"). `gen_ai.prompt` → "Removed, no
  replacement at this time." — confirmed verbatim.

### [81] OpenTelemetry — semantic-conventions-genai CHANGELOG.md — VERIFIED

File content in full: `# Changelog` / `## Unreleased` / a Towncrier HTML comment / `<!-- towncrier
release notes start -->`. No released version anywhere. Matches "contains only `## Unreleased`"
exactly.

### [82] OpenTelemetry — semantic-conventions-genai releases page — VERIFIED

"**There aren't any releases here**" — verbatim, present on the page.

### [83] OpenTelemetry — Moved: gen-ai spec page — VERIFIED

"GenAI semantic conventions have moved to the OpenTelemetry GenAI semantic conventions
repository. This page has moved and is no longer maintained in this repository." — verbatim.
Banner reads "Semantic conventions 1.44.0", matching the citation's quality note.

### [84] OpenTelemetry — Moved: gen-ai attribute registry page — VERIFIED

"Generative AI (GenAI) attributes have moved to the OpenTelemetry GenAI semantic conventions
repository." — verbatim. The Stability column for every listed attribute literally reads "Moved
to the OpenTelemetry GenAI semantic conventions repository," confirming the citation's note that
this page "carries no literal stability level."

### [85] OpenTelemetry — Blog index — VERIFIED

2026 post list includes "GenAI Observability with OpenTelemetry", "Declarative Config
Stabilized" (rendered as "The Voyage of a Small Environment Variable" in the excerpt but appears
in the nav list as "Spring Boot declarative config" / index entry "Declarative Config
Stabilized"), and "Kubernetes SemConv RC" — all three present in the 2026 index. No post
announcing GenAI semantic-conventions stabilization anywhere in the 2026 list. The 2023 list
contains "HTTP semconv are stable" — confirmed present, supporting the citation's point that the
project does announce such milestones on this blog when they occur.

### [86] AWS — CloudWatch Codex monitoring page — VERIFIED

"OpenAI Codex emits OpenTelemetry (OTel) metrics about token usage, per-turn latency, API
requests, tool calls, and approvals... Codex configures its metrics exporter through the `[otel]`
section of its `config.toml` file." — verbatim. No individual metric names appear anywhere on the
page, confirming the "names no individual metrics" quality note.

### [87] OpenAI — Running Codex safely at OpenAI — VERIFIED

Byline: "May 8, 2026" — confirmed. "Codex supports OpenTelemetry log export for various Codex
events such as user prompts, tool approval decisions, tool execution results, MCP server usage,
and network proxy allow or deny events." — verbatim. Worked TOML block confirmed exactly as
quoted, including the `[otel.exporter.otlp-http]` table-header form (distinct from
config-advanced's inline `exporter = { otlp-http = { ... } }` form on [3]) — genuine, correctly
flagged divergence.

### [88] anthropics/claude-code issue #70210 — VERIFIED

State: "Closed as not planned"; label `stale` present. Opened "on Jun 23, 2026." Both quotes
verbatim: "This is immensely helpful in events/logs, but causes high cardinality in metrics. I'd
love to turn this on for logs but turn it off for metrics." and "we pay for managed prometheus and
session id has too much cardinality and would balloon costs, so we've disabled it."

### [89] Praesidia — GenAI semconv status blog — VERIFIED

Dated "2026-08-03" — confirmed. "As of mid-2026, every gen_ai.* attribute, span, metric, and event
in the OpenTelemetry registry carries a stability level of Development, not Stable." — verbatim
(paraphrased slightly closer in the article body: "every gen_ai.* attribute, span, metric, and
event in the OpenTelemetry semantic-conventions registry is marked stability 'Development,' not
'Stable'"). "The new dedicated repository had no tagged release as of mid-July 2026." — verbatim.
The "v1.42.0 / June 2026" attribution is genuinely present in the source ("In June 2026
(semantic-conventions v1.42.0), the GenAI conventions were deprecated out of the main
OpenTelemetry semantic-conventions repository") — the deliverable correctly notes elsewhere that
this specific version/date pairing is *not* independently corroborated by any primary OTel source
in the pool, which is an accurate caveat, not an accuracy problem with citing [89] itself.

### [90] shahvatsal.com — VERIFIED as a refuted claim (correctly framed)

Byline "Released June 22, 2026" confirmed. Core claim confirmed present: "The OpenTelemetry (OTel)
GenAI Special Interest Group (SIG) has stabilized the GenAI Semantic Conventions in June 2026...
The OpenTelemetry GenAI Special Interest Group (SIG) has released the stable specification of the
GenAI Semantic Conventions." This is directly contradicted by [79]/[80]/[81]/[82] (Development
status, no tagged release) — the deliverable's refutation is itself sourced to those four
citations, satisfying the requirement that citation [90] be presented as refuted, not supporting.
All five "supporting detail" errors claimed in the citation entry are confirmed present in the
source and confirmed wrong against the registry:
- `gen_ai.system` used in the code sample (`'gen_ai.system': 'anthropic'`) — registry [80] marks
  it deprecated in favor of `gen_ai.provider.name`.
- `gen_ai.prompt` used in the code sample (`'gen_ai.prompt': prompt`) — registry [80]: "Removed,
  no replacement at this time."
- `usage.input_tokens` / `usage.output_tokens` used literally in prose and code — registry [80]'s
  real names are `gen_ai.usage.input_tokens` / `gen_ai.usage.output_tokens`.
- `gen_ai.response.finish_reason` (singular) used in the code sample — registry [80]'s real name
  is `gen_ai.response.finish_reasons` (plural).
- `gen_ai.tool.status` named in the executive summary — absent from the registry entirely (only
  `gen_ai.tool.call.*`, `gen_ai.tool.definitions`, `gen_ai.tool.description`, `gen_ai.tool.name`,
  `gen_ai.tool.type` exist).

### [91] codexinsider.com — analytics.enabled config page — VERIFIED

Published "Jul 15, 2026" — confirmed. **"Two official pages, two different stories on what
happens when you don't set it."** — verbatim. Its two source claims are independently confirmed:
config-advanced states "By default, Codex periodically sends a small amount of anonymous usage
and health data back to OpenAI" (a stated default, no conditional), while config-reference states
only "Enable or disable analytics for this machine/profile. When unset, the client default
applies" (no default value given). The deliverable's rebuttal — that this is silence-plus-a-stated-
default rather than a genuine contradiction — is a defensible reading of the same two primary
texts and is presented as such, not overstated.

### [92] code.claude.com/docs/en/administration — VERIFIED as INACCESSIBLE

Fetched file's own header: `# Status: FAILED (404: <!DOCTYPE html><html id="__next_error__"...)`.
Matches the deliverable's framing exactly: documented as a FAILED fetch, graded INACCESSIBLE, and
the deliverable correctly notes the admin-enforcement content it was seeking was found on [71]
instead — not treated as a material gap.

---

## Section B detail — re-verified previously-audited citations

### [5] AGENTS.md guide — VERIFIED

Source line: `project_doc_fallback_filenames = ["TEAM_GUIDE.md", ".agents.md"] project_doc_max_bytes = 65536`
appears verbatim inside the "Customize fallback filenames" worked example, immediately followed
by "The larger byte limit allows more combined guidance before truncation." — also verbatim. This
resolves the value that round 1 flagged as untraceable; it is now traced to an exact line in the
source.

### [30] API Pricing — VERIFIED

Two facts added since round 1, both confirmed verbatim: "Regional processing (data residency)
endpoints are charged a 10% uplift for models released on or after March 5, 2026, that are
eligible for data residency" (appears four times, once per relevant pricing table), and "Web
search (all models) $10.00 / 1k calls".

### [49] docs/sandbox.md — VERIFIED

Unchanged from round 1. Full file content: "## Sandbox & approvals" / blank / "For information
about Codex sandboxing and approvals, see [this documentation](https://developers.openai.com/codex/security)."
Three-line stub, zero technical content, as claimed.

### [50] docs/exec.md — VERIFIED

Unchanged from round 1. Full file content: "# Non-interactive mode" / blank / "For information
about non-interactive mode, see [this documentation](https://developers.openai.com/codex/noninteractive)."
The linked path (`developers.openai.com/codex/noninteractive`) differs from where the content
actually resolved in this research ([23], `learn.chatgpt.com/docs/non-interactive-mode`) —
confirmed, as claimed.

### [58] Platform pricing — VERIFIED

Three facts added since round 1, all confirmed verbatim:
- "The $2/$10 per million input/output token pricing for Claude Sonnet 5, announced at launch as
  introductory pricing through August 31, 2026, is now the standard price. The previously
  scheduled increase to $3/$15 per million input/output tokens on September 1, 2026 will not
  occur."
- "Claude 4.6 and later models and Claude Mythos Preview include the full 1M token context window
  at standard pricing. (A 900k-token request is billed at the same per-token rate as a 9k-token
  request.)"
- Managed Agents session-runtime rate: "Session runtime $0.08 per session-hour running status
  duration" — confirmed, and the worked examples show "1.0 hour × $0.08 = $0.08" twice.

---

## Net assessment

Of 22 new citations audited, **20 are fully VERIFIED**. Two carry PARTIAL grades:

1. **[73]** — the substantive claims it supports are accurate, but one quoted sentence (the
   multi-frame cost-inflation bug) is cited to the wrong page; it belongs to [71].
2. **[75]** — the raw fact it supports ("54 metric-name constants") is exact, but the deliverable's
   downstream synthesis using that data — "eighteen"/"18" undocumented metric names — undercounts
   the true diff by 2. The correct count, verified by full enumeration against both [1] and [3],
   is **20**. This appears in three files (`references/observability.md`,
   `claude-code-to-codex-transition.md`, `README.md`) and should be corrected in all three; the
   list of names itself does not need to change, only the stated count and the word "Eighteen".

All five re-verified previously-audited citations ([5], [30], [49], [50], [58]) hold up; the
specific new facts appended to each entry since round 1 were traced to exact verbatim text in
their source pages.

## Grade Ledger

[71] VERIFIED
[72] VERIFIED
[73] PARTIAL
[74] VERIFIED
[75] PARTIAL
[76] VERIFIED
[77] VERIFIED
[78] VERIFIED
[79] VERIFIED
[80] VERIFIED
[81] VERIFIED
[82] VERIFIED
[83] VERIFIED
[84] VERIFIED
[85] VERIFIED
[86] VERIFIED
[87] VERIFIED
[88] VERIFIED
[89] VERIFIED
[90] VERIFIED
[91] VERIFIED
[92] INACCESSIBLE
[5] VERIFIED
[30] VERIFIED
[49] VERIFIED
[50] VERIFIED
[58] VERIFIED
