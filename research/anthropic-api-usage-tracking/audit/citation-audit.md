# Citation Audit: Anthropic API Usage Tracking and Limits

**Auditor:** Claude Sonnet 4.6 (independent citation verification pass)
**Date:** 2026-04-04
**Scope:** All 32 citations used across analysis.md, README.md, and references/*.md
**Method:** Citations [1]–[4] verified against pre-fetched source content in `/tmp/cited-research/anthropic-api-usage-tracking/`. Citations [5]–[32] assessed for consistency between the claims in the documents and the citation descriptions in citations.md.

---

## Summary Table

| Citation | Grade | Notes |
|----------|-------|-------|
| [1] Rate limits | VERIFIED | All specific claims check out against source content |
| [2] Pricing | PARTIAL | Pricing numbers verified; "fast mode 6×" framing is derived, not literal; "313–346 token overhead" attribution is misplaced |
| [3] Usage & Cost API | VERIFIED | All endpoint details, parameters, and constraints confirmed |
| [4] Admin API overview | VERIFIED | Scope, roles, limitations all confirmed |
| [5] Python SDK | UNVERIFIABLE | No fetched content; claims consistent with citation description |
| [6] TypeScript SDK | UNVERIFIABLE | No fetched content; claims consistent with citation description |
| [7] Token counting | UNVERIFIABLE | No fetched content; claims consistent with citation description |
| [8] Agent SDK cost tracking | UNVERIFIABLE | No fetched content; claims consistent with citation description |
| [9] Messages streaming | UNVERIFIABLE | No fetched content; claims consistent with citation description |
| [10] Rate limit philosophy | UNVERIFIABLE | No fetched content; used only for background context |
| [11] Tier 2 advancement | UNVERIFIABLE | No fetched content; consistent with [1] source data |
| [12] LiteLLM cost tracking | UNVERIFIABLE | No fetched content; claims consistent with citation description |
| [13] LiteLLM budget management | UNVERIFIABLE | No fetched content; claims consistent with citation description |
| [14] Langfuse token/cost tracking | UNVERIFIABLE | No fetched content; claims consistent with citation description |
| [15] Portkey budget limits blog | UNVERIFIABLE | No fetched content; claims consistent with citation description |
| [16] Portkey virtual key limits | UNVERIFIABLE | No fetched content; claims consistent with citation description |
| [17] Helicone cost tracking | UNVERIFIABLE | No fetched content; claims consistent with citation description |
| [18] Grafana Anthropic integration blog | UNVERIFIABLE | No fetched content; claims consistent with citation description |
| [19] Grafana Cloud Anthropic docs | UNVERIFIABLE | No fetched content; used only to attribute setup requirement |
| [20] Datadog Anthropic docs | UNVERIFIABLE | No fetched content; claims consistent with citation description |
| [21] Honeycomb Anthropic docs | UNVERIFIABLE | No fetched content; claims consistent with citation description |
| [22] Morphllm rate limits | UNVERIFIABLE | No fetched content; used for cross-reference only |
| [23] Aifreeapi quota tiers | UNVERIFIABLE | No fetched content; used for cross-reference only |
| [24] Service tiers | UNVERIFIABLE | No fetched content; consistent with [1] |
| [25] Revenium middleware | UNVERIFIABLE | No fetched content; claims consistent with citation description |
| [26] AgentOps integration | UNVERIFIABLE | No fetched content; claims consistent with citation description |
| [27] Simon Willison X post | UNVERIFIABLE | No fetched content; flagged as historical context only |
| [28] OpenLLMetry | UNVERIFIABLE | No fetched content; claims consistent with citation description |
| [29] Console cost/usage reporting | UNVERIFIABLE | No fetched content; claims consistent with citation description |
| [30] Claude Code Analytics API | UNVERIFIABLE | No fetched content; claims consistent with citation description |
| [31] LiteLLM GitHub | UNVERIFIABLE | No fetched content; claims consistent with citation description |
| [32] LiteLLM BudgetManager | UNVERIFIABLE | No fetched content; claims consistent with citation description |

---

## Detailed Findings: Citations [1]–[4]

### [1] Rate Limits
**URL:** https://platform.claude.com/docs/en/api/rate-limits
**Fetch status:** OK (source-1-rate-limits.md)
**Grade: VERIFIED**

All specific claims in the documents were confirmed against the source. Detailed findings:

#### Claim: "Every API response includes 18 rate limit headers across four categories" (analysis.md §1, response-headers.md)
**Verdict: VERIFIED**
Source enumerates exactly 18 headers: 3 requests headers + 3 aggregate tokens headers + 3 input token headers + 3 output token headers + 6 priority tier headers = 18. Note that `retry-after` is listed separately as an error header and is not part of the 18 rate limit headers — the documents correctly treat it as a distinct category.

Supporting source text: The source lists 18 named headers in the response headers table, with `retry-after` as an additional error response header.

#### Claim: "Reset timestamps use RFC 3339 format" (analysis.md, response-headers.md)
**Verdict: VERIFIED**
Source verbatim: "anthropic-ratelimit-requests-reset: Time when request rate limit fully replenished, RFC 3339 format"

#### Claim: "Remaining token counts are rounded to the nearest thousand" (analysis.md, response-headers.md)
**Verdict: VERIFIED**
Source verbatim: "anthropic-ratelimit-tokens-remaining: Number of tokens remaining (rounded to nearest thousand)"

#### Claim: "The aggregate tokens-* headers reflect the most restrictive limit currently in effect" (analysis.md, response-headers.md)
**Verdict: VERIFIED**
Source confirms: "Aggregate headers reflect most restrictive limit in effect"

#### Claim: Spend tier table — $5/$40/$200/$400 thresholds, monthly caps $100/$500/$1,000/$200,000 (analysis.md, rate-limit-structure.md)
**Verdict: VERIFIED**
Source verbatim matches: Tier 1 $5/$100, Tier 2 $40/$500, Tier 3 $200/$1,000, Tier 4 $400/$200,000.

#### Claim: Rate limit tables — specific RPM/ITPM/OTPM values by tier and model class (analysis.md, rate-limit-structure.md)
**Verdict: VERIFIED**
All values confirmed from source:
- Tier 1 Sonnet 4.x: 50/30,000/8,000 ✓
- Tier 2 Sonnet 4.x: 1,000/450,000/90,000 ✓
- Tier 3 Haiku 4.5: 2,000/1,000,000/200,000 ✓
- Tier 4 Haiku 4.5: 4,000/4,000,000/800,000 ✓
- All other entries confirmed.

#### Claim: "Token bucket algorithm: capacity replenishes continuously" (analysis.md, rate-limit-structure.md)
**Verdict: VERIFIED**
Source confirms: "Uses token bucket algorithm, capacity replenishes continuously"

#### Claim: "Cache-aware ITPM: only uncached input tokens count toward ITPM for most models" (analysis.md, rate-limit-structure.md)
**Verdict: VERIFIED**
Source confirms: "Only uncached input tokens count toward ITPM for most models"

#### Claim: "Fast mode has dedicated anthropic-fast-* headers separate from standard limits" (analysis.md §1, response-headers.md)
**Verdict: VERIFIED**
Source confirms: "Fast mode has dedicated anthropic-fast-* headers separate from standard limits"

#### Claim: "On 429 responses, retry-after gives the number of seconds to wait" (analysis.md §1)
**Verdict: VERIFIED**
Source verbatim: "retry-after: The number of seconds to wait until you can retry the request"

---

### [2] Pricing
**URL:** https://platform.claude.com/docs/en/about-claude/pricing
**Fetch status:** OK (source-2-pricing.md)
**Grade: PARTIAL**

Most pricing claims are confirmed. Two issues identified:

#### Claim: Model pricing table (analysis.md §4, client-side-tracking.md)
**Verdict: VERIFIED**
Source confirms all model prices as stated:
- Opus 4.6/4.5: $5 input / $25 output ✓
- Opus 4.1/4: $15 input / $75 output ✓
- Sonnet 4.x: $3 input / $15 output ✓
- Haiku 4.5: $1 input / $5 output ✓
- Haiku 3.5: $0.80 input / $4 output ✓
- Haiku 3: $0.25 input / $1.25 output ✓

#### Claim: "Cache write 1.25× (5-min) or 2× (1-hour); cache read 0.1×" (analysis.md §4)
**Verdict: VERIFIED**
Source verbatim: "5-minute cache write: 1.25x base input price", "1-hour cache write: 2x base input price", "Cache read (hit): 0.1x base input price"

#### Claim: "Web search $10/1,000 searches" (analysis.md §4, client-side-tracking.md)
**Verdict: VERIFIED**
Source verbatim: "Web Search: $10 per 1,000 searches plus standard token costs"

#### Claim: "Code execution $0.05/hr/container beyond 1,550 free org hours/month" (analysis.md §4, citations.md [2] description)
**Verdict: VERIFIED**
Source verbatim: "Code Execution: Free with web search/fetch; otherwise $0.05/hr/container beyond 1,550 free org hours/month"

#### Claim: "Fast mode 6×; $30/$150 MTok for Opus 4.6" (analysis.md §4 multiplier table, client-side-tracking.md)
**Verdict: PARTIAL — framing issue**
Source confirms the fast mode pricing ($30/$150 MTok input/output) and notes it is "Opus 4.6 only." The 6× multiplier in the documents is a derived calculation ($30/$5 = 6× standard input, $150/$25 = 6× standard output) presented as if it is a documented multiplier. The source does not use the "6×" framing; it states the absolute prices. The derived value is arithmetically correct but is not sourced text. This is a minor presentation issue, not an inaccuracy.

#### Issue: "Tool use system prompt overhead (313-346 tokens)" attributed to [2] (analysis.md §6 caveat 6, client-side-tracking.md)
**Verdict: PARTIAL — attribution confirmed but numbers require clarification**
Source confirms the overhead figures and attributes them to [2] correctly: "Claude 4.x models: 346 tokens (auto/none), 313 tokens (any/tool)". However, analysis.md states "313-346 tokens per tool-using request" without clarifying that these are two different tool_choice configurations, not a range for a single configuration. The analysis presentation slightly flattens the distinction captured in the source. This is not inaccurate but does lose information.

---

### [3] Usage & Cost API
**URL:** https://platform.claude.com/docs/en/api/usage-cost-api
**Fetch status:** OK (source-3-usage-cost-api.md)
**Grade: VERIFIED**

All specific claims confirmed.

#### Claim: "Usage endpoint GET /v1/organizations/usage_report/messages" (analysis.md §3, billing-usage-endpoints.md)
**Verdict: VERIFIED**
Source confirms this endpoint name verbatim.

#### Claim: "Cost endpoint GET /v1/organizations/cost_report" (analysis.md §3, billing-usage-endpoints.md)
**Verdict: VERIFIED**
Source confirms.

#### Claim: "Admin API key (sk-ant-admin...) required; provisioned by org admins through Console" (analysis.md §3, billing-usage-endpoints.md)
**Verdict: VERIFIED**
Source confirms: "Admin API Key Required: sk-ant-admin... prefix, admin role only, provisioned through Console"

#### Claim: Time bucket limits — 1m max 1,440; 1h max 168; 1d max 31 (analysis.md §3 table)
**Verdict: VERIFIED**
Source verbatim: "1m: default 60, max 1440 buckets", "1h: default 24, max 168 buckets", "1d: default 7, max 31 buckets"

#### Claim: Filter dimensions list (analysis.md §3 table)
**Verdict: VERIFIED**
Source lists: models[], api_key_ids[], workspace_ids[], service_tiers[], context_window[], inference_geos[], speeds[] — matches the documents exactly.

#### Claim: "Data freshness ~5 minutes after request completion" (analysis.md §3, billing-usage-endpoints.md)
**Verdict: VERIFIED**
Source: "Data Freshness: typically within 5 minutes"

#### Claim: "Pagination uses has_more / next_page" (analysis.md §3)
**Verdict: VERIFIED**
Source: "Pagination: cursor-based with has_more and next_page"

#### Claim: "Priority Tier costs are excluded from the cost endpoint" (analysis.md §3)
**Verdict: VERIFIED**
Source: "Priority Tier costs NOT included"

#### Claim: "Partner integrations: CloudZero, Datadog, Grafana Cloud, Honeycomb, Vantage" (analysis.md §3)
**Verdict: VERIFIED**
Source: "Partner Solutions (officially listed): CloudZero, Datadog, Grafana Cloud, Honeycomb, Vantage"

#### Claim: "Admin API unavailable for individual accounts" (analysis.md §3, billing-usage-endpoints.md)
**Verdict: VERIFIED**
Source: "Admin API unavailable for individual accounts"

#### Claim: "No budget alert/webhook endpoint — Anthropic does not push notifications when spend thresholds are crossed" (analysis.md §3)
**Verdict: VERIFIED**
Source-4 (Admin API overview) explicitly states: "No budget alert or webhook endpoint mentioned." Source-3 does not list any such endpoint in the documented feature set. The absence-of-feature claim is confirmed.

#### Claim: "No per-end-user cost attribution" (analysis.md §3)
**Verdict: VERIFIED**
Source confirms group_by dimensions are model, workspace_id, api_key_id, service_tier, context_window, inference_geo, speed — no end-user ID dimension.

---

### [4] Admin API Overview
**URL:** https://platform.claude.com/docs/en/api/administration-api
**Fetch status:** OK (source-4-admin-api.md)
**Grade: VERIFIED**

#### Claim: "Admin API scope: organization members, invites, workspaces, workspace members, API keys, organization info" (analysis.md §3, billing-usage-endpoints.md)
**Verdict: VERIFIED**
Source lists all these scopes plus usage/cost reports and Claude Code analytics.

#### Claim: "Authentication: sk-ant-admin... key, admin role required" (billing-usage-endpoints.md)
**Verdict: VERIFIED**
Source: "Admin API Key: sk-ant-admin... prefix, admin role only, provisioned through Claude Console"

#### Claim: "Five organization roles: user, claude_code_user, developer, billing, admin" (citations.md [4] description)
**Verdict: VERIFIED**
Source lists exactly these five roles with matching descriptions.

#### Claim: "/v1/organizations/me endpoint" (citations.md [4] description)
**Verdict: VERIFIED**
Source: "/v1/organizations/me (organization info)"

#### Claim: "API keys cannot be created via API (Console only)" (citations.md [4] description, billing-usage-endpoints.md)
**Verdict: VERIFIED**
Source: "API keys cannot be CREATED via API (Console only, security reasons)"

#### Claim: "Admin members cannot be removed via API" (citations.md [4] description)
**Verdict: VERIFIED**
Source: "Admin members cannot be removed via API"

#### Claim: "No workspace spend limit API — workspace spend limits configurable only through Console UI" (analysis.md §3, billing-usage-endpoints.md)
**Verdict: VERIFIED**
Source: "No mention of workspace spend limits being configurable via API"

---

## Assessment of Citations [5]–[32]

For the unverifiable citations, the audit checks whether the claims made in the documents are internally consistent with the descriptions provided in citations.md, and whether any red flags exist.

### [5] Python SDK — UNVERIFIABLE
Claims in documents: `message.usage` object, `with_raw_response` pattern, `DefaultHttpxClient`, `messages.stream()` returning `MessageStreamManager`, streaming output_tokens bug (issues #424/#454). All of these are standard patterns documented in the anthropic-sdk-python README and are consistent with the citation description. The streaming bug caveat is appropriately qualified as "unconfirmed fix status." No red flags.

### [6] TypeScript SDK — UNVERIFIABLE
Claims: `.on('message', cb)`, `.on('contentBlock', cb)`, `.finalMessage()`, `.withResponse()`. Consistent with TypeScript SDK patterns. The documents appropriately note these come from snippets and the API may have evolved. No red flags.

### [7] Token counting — UNVERIFIABLE
Claims: `/v1/messages/count_tokens`, free to use, separate RPM limits 100-8,000 by tier, estimates not exact, supports tools/images/PDFs. Consistent with citation description. The RPM range "100-8,000" across tiers is specific; the documents appropriately source this to the discovery agent's confirmed fetch rather than a search snippet. No red flags.

### [8] Agent SDK cost tracking — UNVERIFIABLE
Claims: `total_cost_usd` on `ResultMessage`, `model_usage`/`modelUsage` breakdown, parallel tool call deduplication by message ID, session accumulation manual. Consistent with citation description. The deduplication detail (same `id` on parallel tool calls) is specific and plausible. No red flags.

### [9] Messages streaming — UNVERIFIABLE
Claims: `message_delta` event containing final output_tokens; `message_start` contains initial usage with input_tokens. Consistent with the SSE protocol for Anthropic streaming. No red flags.

### [10] Rate limit philosophy — UNVERIFIABLE
Used only for background on "automatic tier advancement" philosophy. No specific quantitative claims made against this source. No red flags.

### [11] Tier 2 advancement — UNVERIFIABLE
Claim: "$40 cumulative purchase requirement for Tier 2; immediate advancement." The $40 figure is independently confirmed by [1] source (verified). The citation is consistent. No red flags.

### [12] LiteLLM cost tracking — UNVERIFIABLE
Claims: 100+ models, Redis/PostgreSQL backend, per-key/user/team aggregation. These are LiteLLM's publicly documented core features and are consistent with the citation description.

### [13] LiteLLM budget management — UNVERIFIABLE
Claims: `max_budget`, `budget_duration`, hard 400-error block, `user_id` parameter. Consistent with citation description. The documents appropriately caveat whether blocking is pre- or post-request as unconfirmed.

### [14] Langfuse — UNVERIFIABLE
Claims: per-generation cost tracking, custom model pricing, Metrics API filters (user, session, tag). Consistent with citation description.

### [15] Portkey blog — UNVERIFIABLE
Claims: four-component architecture (request layer, usage logging, budget manager, alerting), progressive throttling vs. hard block. Consistent with citation description. The four-component pattern is sourced as a blog post (Tier 3); the documents appropriately do not present it as an API specification.

### [16] Portkey virtual key limits — UNVERIFIABLE
Claims: USD or token-based hard limits, expiry on breach, Slack/email/webhook alerts. Consistent with citation description. The documents correctly flag "enterprise-feature" in the URL as a possible paid-only gate. No red flags.

### [17] Helicone — UNVERIFIABLE
Claims: property-based cost attribution, per-user breakdown, AI Gateway vs. async logging modes, open-source pricing repo for 300+ models. Consistent with citation description.

### [18] Grafana blog — UNVERIFIABLE
Claims: Released August 2025, agentless design, Prometheus-format metrics, three built-in alert rules including `AnthropicDailyCostSpike`. Consistent with citation description. The "v1.0.0, updated to v1.1.1" detail in cost-surfacing-patterns.md appears to come from the discovery agent snippet and is not a fabricated version number; it is consistent with citation description.

### [19] Grafana Cloud docs — UNVERIFIABLE
Used only to attribute "Admin API key setup" and "dashboard panels." No specific quantitative claims.

### [20] Datadog — UNVERIFIABLE
Claims: FinOps Foundation FOCUS format normalization, Cloud Cost Management integration, grouping by model/workspace/service tier/API key. Consistent with citation description.

### [21] Honeycomb — UNVERIFIABLE
Claims: OpenTelemetry receiver for Anthropic Admin API. Consistent with citation description. No specific quantitative claims.

### [22] Morphllm — UNVERIFIABLE
Used for cross-reference only; official docs [1] cited as authoritative. Appropriate use of a Tier 3 source.

### [23] Aifreeapi — UNVERIFIABLE
Used for cross-reference only. Appropriate.

### [24] Service tiers — UNVERIFIABLE
Claims: Priority Tier description, `service_tier` request parameter, 99.5% uptime target, automatic overflow. The `service_tier` parameter and priority-specific headers are consistent with the priority tier headers confirmed in [1]. The "99.5% uptime target" detail is specific and comes from discovery agent snippets; it is not contradicted by any verified source.

### [25] Revenium middleware — UNVERIFIABLE
Claims: wraps `messages.create`/`messages.stream`, metadata dict pattern. Consistent with citation description.

### [26] AgentOps — UNVERIFIABLE
Claims: auto-instrumentation, captures usage fields. Consistent with citation description.

### [27] Simon Willison X post — UNVERIFIABLE
Used only for historical context (Tier 4 flagged). The $40 Tier 2 requirement is confirmed by [1]. The historical ITPM change (40k → 450k for Sonnet Tier 2) is plausible context. Documents correctly cite [1] as authoritative for current values.

### [28] OpenLLMetry — UNVERIFIABLE
Claims: Apache 2.0, OTel extensions for Anthropic/OpenAI/Cohere, cost span attributes. Consistent with citation description.

### [29] Console cost/usage reporting — UNVERIFIABLE
Claims: Console UI provides cost/usage views, workspace breakdown. No specific quantitative claims made against this source.

### [30] Claude Code Analytics API — UNVERIFIABLE
Claims: `/v1/organizations/usage_report/claude_code` endpoint, per-user estimated costs, productivity metrics (sessions, LOC, commits, PRs, tool acceptance rates), up to 1-hour data delay. Consistent with citation description. The endpoint path mirrors the pattern of the confirmed usage endpoint in [3].

### [31] LiteLLM GitHub — UNVERIFIABLE
Used only for "open-source proxy supporting 100+ LLM providers." Consistent with publicly known LiteLLM positioning.

### [32] LiteLLM BudgetManager — UNVERIFIABLE
Claims: standalone `BudgetManager` class for client-side use without proxy. Consistent with citation description.

---

## Issues Requiring Attention

### Issue 1: [2] — Fast mode multiplier presented as documented rather than derived
**Severity: Minor**
**Location:** analysis.md §4 multiplier table, client-side-tracking.md multiplier table
**Details:** The "6×" multiplier for fast mode is a calculation derived from the absolute prices ($30/$5 = 6, $150/$25 = 6). The source states the absolute prices; it does not publish a "6×" multiplier. The arithmetic is correct but the framing implies the source documents this as a multiplier. Should be noted as "(derived: $30/$150 MTok)" or similar.

### Issue 2: [2] — Tool overhead token range flattens two distinct configurations
**Severity: Minor**
**Location:** analysis.md §6 caveat 6
**Details:** The claim "313-346 tokens per tool-using request" flattens two distinct cases: 346 tokens applies to `tool_choice: auto` or `tool_choice: none`; 313 tokens applies to `tool_choice: any` or `tool_choice: tool`. The source does not present these as a range but as configuration-specific values. The analysis loses that distinction.

### Issue 3: [1] — Header count of "18" excludes retry-after but documents are internally consistent
**Severity: None (no error)**
**Location:** analysis.md §1, response-headers.md
**Details:** The claim "18 rate limit headers" matches the source's explicit enumeration of 18 named headers. `retry-after` is correctly treated separately as an error response header in both the documents and the source. No correction needed.

### Issue 4: Usage object in analysis.md includes `server_tool_use` field; client-side-tracking.md version does not
**Severity: Minor**
**Location:** analysis.md §4 code block vs. client-side-tracking.md code block
**Details:** The `usage` object shown in analysis.md includes `server_tool_use.web_search_requests: 1`, attributed to [1]. The server tool usage tracking attribution should be [2] or [3] — the pricing source [2] confirms this field format, and [3] confirms server tool usage is tracked. The [1] citation on this code block is slightly off; [1] covers rate limit headers, not the usage object structure. This is an attribution specificity issue rather than a factual error.

---

## Grade Count

| Grade | Count | Citations |
|-------|-------|-----------|
| VERIFIED | 3 | [1], [3], [4] |
| PARTIAL | 1 | [2] |
| INACCURATE | 0 | — |
| INACCESSIBLE | 0 | — |
| NOT FOUND | 0 | — |
| UNVERIFIABLE | 28 | [5]–[32] |
| **Total** | **32** | |

---

## Overall Assessment

The four directly verifiable citations ([1]–[4]) are well-sourced and accurately represent the source material. No fabricated numbers were found. The two issues noted for [2] are presentation choices (derived multiplier, range flattening) rather than factual errors — the underlying numbers are correct.

For the 28 unverifiable citations, the claims in the documents are internally consistent with the citation descriptions in citations.md. No claims exceed what the citation descriptions attribute to those sources. The research team appropriately flagged all discovery-agent-only sources as "not directly fetched" and explicitly cautioned against using third-party tool capabilities (LiteLLM, Portkey, Langfuse, etc.) for implementation decisions without further verification.

The research documents follow reasonable epistemic hygiene: Tier 3/4 sources are used only for context or cross-reference, not as primary evidence for specific technical claims. Absence-of-feature claims (no webhook, no per-user attribution, no workspace spend limit API) are grounded in the directly verified sources [3] and [4].
