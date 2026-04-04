# Anthropic API Usage Tracking and Limits: Full Analysis

A citation-backed analysis of what the Anthropic API exposes for usage tracking, rate limits, and cost monitoring — and what wrapper applications must build themselves.

**Methodology:** All factual claims trace to web sources visited in-session. Citation numbers reference [citations.md](citations.md). Two independent review agents audit this document for citation accuracy and internal consistency.

---

## 1. What the API Exposes in Response Headers

Every API response includes **18 rate limit headers** across four categories [1].

### Standard Headers (All Responses)

The core set covers three dimensions — requests, input tokens, and output tokens — each with limit/remaining/reset triples:

| Dimension | `-limit` | `-remaining` | `-reset` |
|-----------|----------|-------------|----------|
| Requests | `anthropic-ratelimit-requests-limit` | `anthropic-ratelimit-requests-remaining` | `anthropic-ratelimit-requests-reset` |
| Tokens (aggregate) | `anthropic-ratelimit-tokens-limit` | `anthropic-ratelimit-tokens-remaining` | `anthropic-ratelimit-tokens-reset` |
| Input tokens | `anthropic-ratelimit-input-tokens-limit` | `anthropic-ratelimit-input-tokens-remaining` | `anthropic-ratelimit-input-tokens-reset` |
| Output tokens | `anthropic-ratelimit-output-tokens-limit` | `anthropic-ratelimit-output-tokens-remaining` | `anthropic-ratelimit-output-tokens-reset` |

Key details:
- Reset timestamps use **RFC 3339 format** (e.g., `2026-04-04T12:30:00Z`) [1]
- Remaining token counts are **rounded to the nearest thousand** [1]
- The aggregate `tokens-*` headers reflect the **most restrictive limit** currently in effect (workspace vs. organization) [1]

### Priority Tier Headers

Six additional headers (`anthropic-priority-input-tokens-*` and `anthropic-priority-output-tokens-*`) appear only when using Priority Tier [1] [24].

### Error Headers

On 429 responses, a `retry-after` header gives the **number of seconds** to wait [1]. The response body contains `type: "rate_limit_error"`.

### Fast Mode Headers

Fast mode (`speed: "fast"` on Opus 4.6) returns dedicated `anthropic-fast-*` headers [1]. Specific header names are documented in the fast mode documentation rather than the rate limits page.

### Identification Headers

Every response also includes `request-id` (unique per request) and `anthropic-organization-id` [5].

## 2. Rate Limit Structure

### Spend Limit Tiers

Tier advancement is **automatic and immediate** upon reaching cumulative credit purchase thresholds [1] [11]:

| Tier | Cumulative Purchase | Max Single Purchase | Monthly Spend Limit |
|------|--------------------|--------------------|---------------------|
| Tier 1 | $5 | $100 | $100 |
| Tier 2 | $40 | $500 | $500 |
| Tier 3 | $200 | $1,000 | $1,000 |
| Tier 4 | $400 | $200,000 | $200,000 |
| Monthly Invoicing | N/A | N/A | No limit |

### Per-Minute Rate Limits (Current Models, April 2026)

Rate limits are measured in RPM, ITPM, and OTPM per model class [1]:

| Model Class | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|-------------|--------|--------|--------|--------|
| **Opus 4.x** | 50 RPM / 30K ITPM / 8K OTPM | 1K / 450K / 90K | 2K / 800K / 160K | 4K / 2M / 400K |
| **Sonnet 4.x** | 50 / 30K / 8K | 1K / 450K / 90K | 2K / 800K / 160K | 4K / 2M / 400K |
| **Haiku 4.5** | 50 / 50K / 10K | 1K / 450K / 90K | 2K / 1M / 200K | 4K / 4M / 800K |

Opus 4.x limits are shared across Opus 4.6, 4.5, 4.1, and 4. Sonnet 4.x limits are shared across Sonnet 4.6, 4.5, and 4 [1].

### Token Bucket Algorithm

The API uses a **token bucket** algorithm: capacity replenishes continuously, not at fixed intervals [1]. This means:
- Short bursts above the sustained rate are possible if the bucket has accumulated capacity
- Conversely, a 60 RPM limit may be enforced as ~1 RPS, causing bursts to trigger 429s [1]

### Cache-Aware ITPM

For most current models, **only uncached input tokens count toward ITPM** [1]:
- `input_tokens` + `cache_creation_input_tokens` → count toward ITPM
- `cache_read_input_tokens` → **do not count** toward ITPM

This means effective throughput with 80% cache hit rate can be 5× the nominal ITPM limit [1]. Older models (marked with †) also count cached reads [1].

## 3. Billing and Usage Endpoints

### The Admin API

Anthropic provides a **Usage & Cost Admin API** for programmatic access to historical data [3]. It requires an Admin API key (`sk-ant-admin...`) provisioned only by org admins through the Console [4].

**Important constraint:** The Admin API is **unavailable for individual accounts** — an organization must be set up first [3].

### Usage Endpoint

**`GET /v1/organizations/usage_report/messages`** [3]

| Feature | Details |
|---------|---------|
| Time buckets | `1m` (max 1,440), `1h` (max 168), `1d` (max 31) [3] |
| Filter dimensions | `api_key_ids`, `workspace_ids`, `models`, `service_tiers`, `context_window`, `inference_geos`, `speeds` [3] |
| Group-by dimensions | `model`, `workspace_id`, `api_key_id`, `service_tier`, `context_window`, `inference_geo`, `speed` [3] |
| Data freshness | ~5 minutes after request completion [3] |
| Pagination | Cursor-based (`has_more` / `next_page`) [3] |

### Cost Endpoint

**`GET /v1/organizations/cost_report`** [3]

- Daily granularity only (`1d`) [3]
- All costs in USD [3]
- Group by `workspace_id` or `description` [3]
- **Priority Tier costs are excluded** — track via usage endpoint instead [3]

### What Does Not Exist

Based on the fetched documentation:
- **No budget alert/webhook endpoint** — Anthropic does not push notifications when spend thresholds are crossed [3]
- **No per-end-user cost attribution** — the API groups by workspace, API key, model, and service tier, but not by arbitrary end-user IDs [3]
- **No workspace spend limit API** — spend limits for workspaces are set only through the Console UI [4]

### Partner Integrations

Anthropic officially lists five monitoring partners: CloudZero, Datadog, Grafana Cloud, Honeycomb, and Vantage [3]. Of these:
- **Grafana Cloud** provides agentless pull from the Admin API with three built-in alert rules including `AnthropicDailyCostSpike` [18]
- **Datadog** normalizes to FinOps FOCUS format and integrates with Cloud Cost Management [20]
- **Honeycomb** uses an OpenTelemetry receiver [21]

## 4. Client-Side Spend Tracking

### The Usage Object

Every response includes a `usage` object with exact token counts [5] [2]:

```json
{
  "usage": {
    "input_tokens": 50,
    "output_tokens": 239,
    "cache_creation_input_tokens": 7345,
    "cache_read_input_tokens": 7123,
    "server_tool_use": {
      "web_search_requests": 1
    }
  }
}
```

Total billable input: `input_tokens + cache_creation_input_tokens + cache_read_input_tokens` [1]. Note that `input_tokens` represents only tokens **after the last cache breakpoint** [1].

### Cost Calculation

Apply per-model rates to token counts [2]:

| Model | Input ($/MTok) | Output ($/MTok) |
|-------|----------------|-----------------|
| Opus 4.6 / 4.5 | $5 | $25 |
| Opus 4.1 / 4 | $15 | $75 |
| Sonnet 4.x | $3 | $15 |
| Haiku 4.5 | $1 | $5 |

Multipliers: cache write 1.25× (5-min) or 2× (1-hour); cache read 0.1×; batch 0.5×; fast mode $30/$150 MTok (calculated: 6× standard Opus 4.6 rates); data residency US-only 1.1× [2]. Multipliers stack [2].

Additional costs: web search $10/1,000 searches; code execution $0.05/hr/container beyond 1,550 free org hours/month [2].

### Pre-Request Estimation

`/v1/messages/count_tokens` estimates input token count before sending [7]:
- Free to use [7]
- Separate RPM limits (100-8,000 by tier) [7]
- Results are estimates, not exact [7]
- Supports tools, images, PDFs [7]

### Agent SDK

The Anthropic Agent SDK provides `total_cost_usd` on each `query()` result [8]. Parallel tool calls produce duplicate messages (same `id`) requiring deduplication [8]. Session totals must be accumulated manually [8].

## 5. SDK-Level Hooks for Intercepting Usage Data

### Python SDK

| Pattern | Mechanism | What It Provides |
|---------|-----------|-----------------|
| `message.usage` | Direct attribute access | Token counts per response [5] |
| `.with_raw_response.create()` | `APIResponse` wrapper | All HTTP headers including rate limits [5] |
| `DefaultHttpxClient(transport=...)` | Custom httpx transport | Transport-level interception for logging, metrics [5] |
| `.messages.stream()` → `get_final_message()` | Streaming accumulation | Final usage on streamed responses [5] |
| `.messages.count_tokens()` | Pre-flight estimation | Input token estimate before sending [7] |

### TypeScript SDK

| Pattern | Mechanism | What It Provides |
|---------|-----------|-----------------|
| `message.usage` | Direct property access | Token counts per response [6] |
| `.withResponse().create()` | Response + headers | All HTTP headers alongside parsed body [6] |
| `new Anthropic({ fetch: ... })` | Custom fetch | Transport-level interception [6] |
| `.messages.stream()` → `.on('message', ...)` | Event hooks | Fires on full message with usage [6] |
| `.finalMessage()` | Streaming accumulation | Accumulated message with final usage [6] |

### No Native Middleware

Neither SDK provides a formal middleware/interceptor registration API. Extension points are custom transport (httpx in Python, fetch in TypeScript) and raw response access [5] [6].

### Third-Party Instrumentation

- **OpenLLMetry** — OTel span attributes for per-user/feature cost (Apache 2.0) [28]
- **Langfuse** — per-generation cost tracking with custom pricing (MIT, self-hostable) [14]
- **AgentOps** — auto-instrumentation capturing usage fields [26]
- **Revenium** — middleware wrapping `messages.create`/`messages.stream` [25]

## 6. Patterns for Surfacing Cost in Wrapper Applications

### Gateway/Proxy (Recommended for Multi-User Apps)

The dominant pattern: route all requests through a gateway that attaches user metadata and enforces budgets [15].

**LiteLLM** is the most feature-complete open-source option [12] [13]:
- Automatic cost tracking for 100+ LLMs stored in Redis/PostgreSQL [12]
- `max_budget` per user with `budget_duration` and hard 400-error enforcement [13]
- Also available as standalone `BudgetManager` class [32]

**Portkey** provides hierarchical budget management with alert routing [15] [16]. Budget limits may require an enterprise plan [16].

**Helicone** offers property-based cost attribution with an open-source pricing repo [17].

### Observability Integration (Recommended for Operations Teams)

For organizations with existing monitoring infrastructure, the five Anthropic partner integrations provide ready-to-use dashboards:

| Platform | Key Feature | Cost |
|----------|-------------|------|
| Grafana Cloud | Agentless, 3 built-in alerts [18] | Grafana Cloud pricing |
| Datadog | FinOps FOCUS format, CCM integration [20] | Datadog pricing |
| Honeycomb | OTel-native [21] | Honeycomb pricing |
| CloudZero | Cost forecasting [3] | CloudZero pricing |
| Vantage | FinOps observability [3] | Vantage pricing |

### Self-Hosted (Recommended for Privacy/Compliance)

Langfuse (MIT) [14] and Helicone (open-source) [17] both support self-hosting. OpenLLMetry (Apache 2.0) [28] provides OTel instrumentation that works with any compatible backend.

### Decision Framework

1. **Individual developer, single-user app** → Read `message.usage` directly, maintain a local running total, compare against the Console's cost page for reconciliation
2. **Multi-user app, need per-user budgets** → Deploy LiteLLM proxy or Portkey gateway with `max_budget` enforcement
3. **Organization with existing monitoring** → Connect Grafana/Datadog/Honeycomb to the Admin API
4. **Privacy-sensitive or air-gapped** → Self-host Langfuse or Helicone
5. **Agent workflows** → Use Agent SDK's `total_cost_usd` with manual session accumulation [8]

## Limitations and Caveats

1. **No real-time budget enforcement from Anthropic** — all per-user budget logic must be implemented externally [3].
2. **Admin API requires an organization** — individual accounts cannot access Usage & Cost endpoints [3].
3. **~5-minute data lag** on the Admin API makes it unsuitable for real-time budget gates [3].
4. **Pricing changes are not signaled** — no webhook or API announces when rates change. Client-side calculators using hardcoded rates will drift.
5. **Streaming usage bug** — Python SDK issues #424/#454 reported `output_tokens` always returning `1` during streaming. Fix status unconfirmed [5].
6. **Tool use overhead is hidden** — system prompt overhead (346 tokens with `auto`/`none` tool choice, 313 tokens with `any`/specific tool choice for Claude 4.x models) is billed but not broken out in the `usage` object [2].
7. **Token rounding** — rate limit remaining headers round to the nearest thousand, limiting precision for fine-grained tracking [1].

## Cross-Source Synthesis Notes

The analysis combines data from official Anthropic documentation (directly fetched) with discovery agent findings from SDK repos, third-party tool docs, and community sources. The Anthropic documentation was the authoritative source for all rate limit, pricing, and API endpoint claims. Third-party tool capabilities (LiteLLM, Portkey, Langfuse, etc.) were identified from search snippets and not directly fetched — these claims should be verified against current documentation before implementation decisions.
