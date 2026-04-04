# Response Headers: Rate Limit Data

This reference covers Dimension 1: what the Anthropic API exposes in HTTP response headers related to rate limits, remaining capacity, and reset windows.

Source details: [citations.md](../citations.md)

---

## Rate Limit Headers

The API returns rate limit headers on every response (both successful and error responses) [1]. There are 18 documented headers across four categories.

### Request-Count Headers

| Header | Description |
|--------|-------------|
| `anthropic-ratelimit-requests-limit` | Maximum requests allowed in the rate limit period [1] |
| `anthropic-ratelimit-requests-remaining` | Requests remaining before rate limiting [1] |
| `anthropic-ratelimit-requests-reset` | Time when request limit is fully replenished (RFC 3339) [1] |

### Aggregate Token Headers

| Header | Description |
|--------|-------------|
| `anthropic-ratelimit-tokens-limit` | Maximum tokens allowed in the rate limit period [1] |
| `anthropic-ratelimit-tokens-remaining` | Tokens remaining, rounded to nearest thousand [1] |
| `anthropic-ratelimit-tokens-reset` | Time when token limit is fully replenished (RFC 3339) [1] |

These aggregate headers reflect the **most restrictive limit currently in effect**. If a workspace per-minute limit is exceeded, these headers show the workspace limit values rather than the organization-level values [1].

### Granular Input/Output Token Headers

| Header | Description |
|--------|-------------|
| `anthropic-ratelimit-input-tokens-limit` | Maximum input tokens allowed in the rate limit period [1] |
| `anthropic-ratelimit-input-tokens-remaining` | Input tokens remaining, rounded to nearest thousand [1] |
| `anthropic-ratelimit-input-tokens-reset` | Time when input token limit is fully replenished (RFC 3339) [1] |
| `anthropic-ratelimit-output-tokens-limit` | Maximum output tokens allowed in the rate limit period [1] |
| `anthropic-ratelimit-output-tokens-remaining` | Output tokens remaining, rounded to nearest thousand [1] |
| `anthropic-ratelimit-output-tokens-reset` | Time when output token limit is fully replenished (RFC 3339) [1] |

### Priority Tier Headers (Priority Tier Only)

These are returned only when using Priority Tier (committed spend model with `service_tier` parameter) [1] [24].

| Header | Description |
|--------|-------------|
| `anthropic-priority-input-tokens-limit` | Maximum Priority Tier input tokens per period [1] |
| `anthropic-priority-input-tokens-remaining` | Priority Tier input tokens remaining, rounded to nearest thousand [1] |
| `anthropic-priority-input-tokens-reset` | Time when Priority Tier input limit replenishes (RFC 3339) [1] |
| `anthropic-priority-output-tokens-limit` | Maximum Priority Tier output tokens per period [1] |
| `anthropic-priority-output-tokens-remaining` | Priority Tier output tokens remaining, rounded to nearest thousand [1] |
| `anthropic-priority-output-tokens-reset` | Time when Priority Tier output limit replenishes (RFC 3339) [1] |

### Fast Mode Headers

When using fast mode (`speed: "fast"` on Opus 4.6), dedicated `anthropic-fast-*` headers indicate fast mode rate limit status. These are separate from standard Opus rate limits [1].

### Error and Retry Headers

| Header | Description |
|--------|-------------|
| `retry-after` | Seconds to wait before retrying (on 429 responses) [1] |

On 429 errors, the response body has `type: "rate_limit_error"` and the `retry-after` header gives the number of seconds to wait. Earlier retries will fail [1].

## Other Response Headers

Beyond rate limits, the API also returns identification headers on every response:

- `request-id` — globally unique per-request identifier (from discovery agent findings, based on API overview page [5])
- `anthropic-organization-id` — identifies the organization (from discovery agent findings [5])

## Reset Timestamp Format

All `-reset` headers use **RFC 3339 format** (e.g., `2026-04-04T12:30:00Z`) [1]. The `retry-after` header uses an integer number of seconds [1].

## Token Rounding

The `-remaining` headers for tokens (both aggregate and granular) are **rounded to the nearest thousand** [1]. This means the headers provide an approximation, not an exact count.

## Gaps and Limitations

- The exact header names for fast mode (`anthropic-fast-*`) are referenced but not individually enumerated in the rate limits documentation [1]. The fast mode documentation is referenced for details.
- Whether headers are returned on streaming responses (SSE) is not explicitly stated in the rate limits documentation; headers would be on the initial HTTP response before the event stream begins.
- The `request-id` and `anthropic-organization-id` headers were identified from discovery agent search snippets, not directly from a fetched page.
