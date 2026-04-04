# Billing and Usage Endpoints

This reference covers Dimension 2: whether the Anthropic API or Console exposes programmatic billing/usage data.

Source details: [citations.md](../citations.md)

---

## Overview

Anthropic provides a **Usage & Cost Admin API** with two endpoints for programmatic access to historical usage and cost data [3]. This is part of the broader Admin API [4]. The Admin API is **unavailable for individual (non-organization) accounts** [3].

## Authentication

All Admin API endpoints require an **Admin API key** with prefix `sk-ant-admin...` [3] [4]. Only organization members with the **admin** role can provision these keys through Console → Settings → Admin Keys [4]. Standard API keys (`sk-ant-...`) do not work with Admin endpoints.

Admin API keys cannot be created programmatically — they can only be provisioned through the Claude Console [4].

## Usage Endpoint

**`GET /v1/organizations/usage_report/messages`** [3]

Tracks token consumption with breakdowns by model, workspace, and service tier.

### Query Parameters

| Parameter | Description |
|-----------|-------------|
| `starting_at` | Start time (ISO 8601, required) [3] |
| `ending_at` | End time (ISO 8601, required) [3] |
| `bucket_width` | Time granularity: `1m`, `1h`, or `1d` [3] |
| `group_by[]` | Dimensions to group by (repeatable): `model`, `workspace_id`, `api_key_id`, `service_tier`, `context_window`, `inference_geo`, `speed` [3] |
| `models[]` | Filter by model (e.g., `claude-opus-4-6`) [3] |
| `api_key_ids[]` | Filter by API key ID [3] |
| `workspace_ids[]` | Filter by workspace ID [3] |
| `service_tiers[]` | Filter by service tier (e.g., `batch`) [3] |
| `context_window[]` | Filter by context window (e.g., `0-200k`) [3] |
| `inference_geos[]` | Filter by data residency: `global`, `us`, `not_available` [3] |
| `speeds[]` | Filter by speed: `standard`, `fast` (requires `fast-mode-2026-02-01` beta header) [3] |
| `limit` | Page size [3] |
| `page` | Pagination cursor [3] |

### Time Granularity Limits

| Granularity | Default Buckets | Maximum Buckets | Use Case |
|-------------|-----------------|-----------------|----------|
| `1m` | 60 | 1,440 | Real-time monitoring [3] |
| `1h` | 24 | 168 | Daily patterns [3] |
| `1d` | 7 | 31 | Weekly/monthly reports [3] |

### Token Types Tracked

The usage endpoint tracks: uncached input tokens, cached input tokens, cache creation tokens, and output tokens [3]. Server-side tool usage (web search requests, code execution) is also tracked [3].

## Cost Endpoint

**`GET /v1/organizations/cost_report`** [3]

Retrieves service-level cost breakdowns in USD.

### Key Characteristics

- All costs in USD, reported as decimal strings [3]
- **Daily granularity only** (`1d` bucket width) [3]
- Cost types: token usage, web search, code execution [3]
- Group by: `workspace_id`, `description` [3]
- When grouping by `description`, responses include parsed fields like `model` and `inference_geo` [3]

### Limitations

- **Priority Tier costs are NOT included** in the cost endpoint [3]. Priority Tier usage must be tracked via the usage endpoint with `service_tier` filter/grouping.
- Code execution costs appear grouped under `Code Execution Usage` in the description field [3].
- Workbench usage has `null` for `api_key_id` [3].
- Default workspace usage has `null` for `workspace_id` [3].

## Pagination

Both endpoints support cursor-based pagination [3]:

1. Make initial request
2. If `has_more` is `true`, use the `next_page` value in the next request
3. Continue until `has_more` is `false`

## Data Freshness

Usage and cost data typically appears **within 5 minutes** of API request completion [3]. Recommended polling frequency: **once per minute** for sustained use; more frequent polling is acceptable for short bursts (e.g., downloading paginated data) [3].

## Claude Code Analytics API

A separate endpoint provides Claude Code-specific analytics [30]:

**`GET /v1/organizations/usage_report/claude_code`**

Returns per-user estimated costs and developer productivity metrics: sessions, lines of code, commits, PRs, tool acceptance rates [30]. Data delay up to 1 hour [30].

## Console UI Reporting

The Claude Console provides visual cost and usage reporting without the Admin API [29]:
- Usage page: token consumption charts, rate limit charts, cache hit rates [1]
- Cost page: spend breakdowns [29]

The Console also allows setting customer-defined spend limits (lower than the tier ceiling) via Settings → Limits [1].

## What Does NOT Exist

Based on the fetched documentation:

- **No budget alert/webhook endpoint** — Anthropic does not provide programmatic budget alerts or webhooks. Monitoring platforms (Datadog, Grafana, Honeycomb) build alerting on top of the polling API [3].
- **No per-end-user cost attribution** — The API groups by workspace, API key, model, and service tier, but not by arbitrary end-user IDs. Per-user attribution requires proxy-layer solutions [3].
- **No workspace spend limit API** — Workspace spend limits are configurable only through the Console UI; the Admin API manages workspace membership and API keys but does not expose spend limit fields [4].

## Partner Integrations

Anthropic officially lists five partner integrations for usage monitoring [3]:

| Partner | Integration Type |
|---------|-----------------|
| CloudZero | Cloud intelligence / cost forecasting [3] |
| Datadog | LLM Observability with automatic tracing; FinOps FOCUS format [20] |
| Grafana Cloud | Agentless integration; built-in dashboards and alerts [18] [19] |
| Honeycomb | OpenTelemetry receiver [21] |
| Vantage | FinOps cost & usage observability [3] |

## Gaps and Limitations

- Exact response schema field names for the usage endpoint (e.g., the JSON keys for token counts in each bucket) were not enumerated in the fetched page — the page shows examples and concepts but links to the API reference for full schemas [3].
- Whether the cost endpoint supports filtering by API key or model (beyond grouping by description) is not clear from the fetched content [3].
- The Claude Code Analytics API endpoint was not directly fetched; details come from discovery agent findings [30].
