# Client-Side Spend Tracking

This reference covers Dimension 3: patterns for tracking spend from the client side when the API doesn't provide a real-time budget endpoint.

Source details: [citations.md](../citations.md)

---

## The Core Mechanism: Response Usage Object

Every non-streaming API response includes a `usage` object with exact token counts [5] [8]:

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

This is the primary mechanism for client-side cost reconstruction. The formula for total billable input tokens is [1]:

```
total_input_tokens = cache_read_input_tokens + cache_creation_input_tokens + input_tokens
```

Where `input_tokens` represents only tokens **after the last cache breakpoint**, not the full input [1].

### Streaming Responses

During streaming, the `message_start` SSE event includes initial usage with `input_tokens`. The `message_delta` event at the end of the stream includes the final `output_tokens` count [9]. The `usage` object on the accumulated final message should contain complete token counts.

### Server Tool Usage

Responses involving server-side tools include additional usage tracking [2]:

```json
{
  "usage": {
    "input_tokens": 105,
    "output_tokens": 6039,
    "server_tool_use": {
      "web_search_requests": 1,
      "code_execution_requests": 1
    }
  }
}
```

## Cost Calculation Formula

To compute cost from the usage object, apply the published pricing rates [2]:

```
cost = (input_tokens × input_rate)
     + (cache_creation_input_tokens × cache_write_rate)
     + (cache_read_input_tokens × cache_read_rate)
     + (output_tokens × output_rate)
     + (web_search_requests × $0.01)
     + (code_execution time-based charges if applicable)
```

### Current Pricing (April 2026) [2]

| Model | Input ($/MTok) | Output ($/MTok) |
|-------|----------------|-----------------|
| Claude Opus 4.6 | $5 | $25 |
| Claude Opus 4.5 | $5 | $25 |
| Claude Opus 4.1 | $15 | $75 |
| Claude Opus 4 | $15 | $75 |
| Claude Sonnet 4.6 | $3 | $15 |
| Claude Sonnet 4.5 | $3 | $15 |
| Claude Sonnet 4 | $3 | $15 |
| Claude Haiku 4.5 | $1 | $5 |
| Claude Haiku 3.5 | $0.80 | $4 |
| Claude Haiku 3 | $0.25 | $1.25 |

### Pricing Multipliers [2]

| Modifier | Multiplier |
|----------|------------|
| 5-minute cache write | 1.25× base input |
| 1-hour cache write | 2× base input |
| Cache read (hit) | 0.1× base input |
| Batch API | 0.5× (all tokens) |
| Fast mode (Opus 4.6 only) | $30/$150 MTok (calculated: 6× standard rates) |
| Data residency US-only (Opus 4.6+) | 1.1× all categories |

Multipliers stack: batch + cache, data residency + fast mode, etc. [2].

## Pre-Request Token Estimation

The `/v1/messages/count_tokens` endpoint estimates input token consumption **before** sending a request [7]:

- Free to use (no token charges) [7]
- Separate RPM limits (100-8,000 by tier) that don't count against message creation limits [7]
- Results are **estimates, not exact counts** [7]
- Supports tools, images, and PDFs in the count [7]

This enables pre-flight cost checks: estimate input tokens, multiply by rate, compare against budget before sending.

## Agent SDK Cost Tracking

The Anthropic Agent SDK provides built-in cost tracking [8]:

- `total_cost_usd` field on `ResultMessage` for each `query()` call [8]
- `model_usage` / `modelUsage` breakdown per model [8]
- **Deduplication required**: parallel tool calls produce duplicate assistant messages sharing the same `id`; dedup by ID to avoid double-counting [8]
- Session-level totals must be accumulated manually — the SDK does not provide them [8]
- Cost is reported even on error paths [8]

## Client-Side Tracking Patterns

### Pattern 1: Local Ledger

Maintain a running total by extracting `usage` from every response:

1. After each API call, read `usage.input_tokens` and `usage.output_tokens`
2. Apply the per-model pricing rate
3. Add to a running total (in-memory, database, or file)
4. Compare against budget threshold before each subsequent call

This is the simplest pattern and works without any additional infrastructure.

### Pattern 2: Proxy/Gateway Layer

Route all API calls through a proxy that intercepts responses and logs usage [12] [15]:

- **LiteLLM** — open-source proxy that automatically tracks spend for 100+ LLMs; stores in Redis/PostgreSQL; provides per-key/user/team aggregation [12]. Offers `max_budget` per user with hard 400-error block when exceeded [13]. Also available as a standalone `BudgetManager` class without the proxy [32].
- **Portkey** — AI gateway with hierarchical budget management (Customer, Team, Virtual Key, Provider Configuration); supports USD or token-based hard limits with Slack/email/webhook alerts [15] [16].
- **Helicone** — open-source gateway with property-based cost attribution; per-user breakdown; pricing data for 300+ models from an open-source pricing repo [17].

### Pattern 3: Observability Instrumentation

Attach usage data to OpenTelemetry spans or custom telemetry [28] [14]:

- **OpenLLMetry** (Traceloop) — Apache 2.0 OTel extensions with span attributes for per-user and per-feature cost attribution [28].
- **Langfuse** — MIT-licensed, self-hostable; per-generation cost tracking; custom model pricing definitions; Metrics API with user/session/tag filters [14].
- **AgentOps** — auto-instrumentation for Anthropic SDK; captures usage fields automatically [26].

### Pattern 4: Admin API Polling (Organization-Level)

For server-side reconciliation rather than real-time client tracking:

- Poll `/v1/organizations/usage_report/messages` at 1-minute intervals [3]
- Compare against internal ledger for drift detection
- ~5-minute data freshness lag means this is not suitable for real-time budget enforcement [3]

## Gaps and Limitations

- **No real-time budget endpoint** from Anthropic — all client-side tracking requires computing cost from the `usage` object yourself [3].
- **Pricing changes are not signaled** — if Anthropic updates pricing, client-side calculations using hardcoded rates will drift until updated. No webhook or API endpoint announces pricing changes.
- **Streaming usage bug** — GitHub issues #424 and #454 on anthropic-sdk-python reported `get_final_message().usage.output_tokens` always returning `1` during streaming [5]. Resolution status is unconfirmed from available sources.
- The `count_tokens` endpoint provides estimates, not exact counts, so pre-flight cost checks have some margin of error [7].
- Tool use system prompt overhead (346 tokens with `auto`/`none` tool choice, 313 tokens with `any`/specific tool choice for Claude 4.x models) is an additional cost not visible in the `usage` object breakdown [2].
