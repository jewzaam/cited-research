# SDK-Level Usage Hooks

This reference covers Dimension 4: how the Python and TypeScript Anthropic SDKs expose request/response metadata, middleware/interceptor patterns, and event hooks for tracking usage.

Source details: [citations.md](../citations.md)

---

## Response Usage Object (Both SDKs)

Every non-streaming message response includes a `usage` object [5] [6]:

```python
message = client.messages.create(...)
print(message.usage.input_tokens)   # int
print(message.usage.output_tokens)  # int
```

With prompt caching enabled, additional fields appear [1]:
- `cache_creation_input_tokens` — tokens written to cache
- `cache_read_input_tokens` — tokens read from cache

## Python SDK

### Raw Response Access

The `with_raw_response` pattern returns an `APIResponse` wrapping the `httpx` response, providing access to all HTTP headers [5]:

```python
response = client.messages.with_raw_response.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}]
)
# Access headers
print(response.headers["anthropic-ratelimit-requests-remaining"])
print(response.headers["request-id"])

# Parse the message body
message = response.parse()
print(message.usage.input_tokens)
```

This is the primary mechanism for reading rate limit headers from the SDK [5].

### Custom httpx Transport

The Python SDK accepts a custom `httpx` client via `DefaultHttpxClient` / `DefaultAsyncHttpxClient`, preserving SDK defaults while allowing transport-level interception [5]:

```python
import anthropic
import httpx

custom_client = anthropic.DefaultHttpxClient(
    transport=httpx.HTTPTransport(retries=3)
)
client = anthropic.Anthropic(http_client=custom_client)
```

This enables:
- Custom retry logic
- Request/response logging middleware
- Metrics collection at the transport layer
- Proxy routing

### Streaming

The Python SDK provides `client.messages.stream()` returning a `MessageStreamManager` [5]:

```python
with client.messages.stream(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)

    final = stream.get_final_message()
    print(final.usage.input_tokens)
    print(final.usage.output_tokens)
```

**Known issue**: GitHub issues #424 and #454 reported that `stream.get_final_message().usage.output_tokens` was always `1` during streaming [5]. Resolution status and fix version are unconfirmed.

### Token Counting

```python
count = client.messages.count_tokens(
    model="claude-sonnet-4-6",
    messages=[{"role": "user", "content": "Hello"}]
)
print(count.input_tokens)  # estimated count
```

This calls `/v1/messages/count_tokens` and is free to use [7]. Results are estimates [7].

## TypeScript SDK

### Event Hooks

The TypeScript SDK's streaming interface exposes event-based hooks [6]:

```typescript
const stream = client.messages.stream({
  model: "claude-sonnet-4-6",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hello" }]
});

stream.on("message", (message) => {
  // Fires when message is fully streamed
  console.log(message.usage.input_tokens);
  console.log(message.usage.output_tokens);
});

stream.on("contentBlock", (block) => {
  // Fires for each content block
});

const finalMessage = await stream.finalMessage();
console.log(finalMessage.usage);
```

### Raw Response Access

The TypeScript SDK provides `withResponse()` for accessing HTTP headers alongside the parsed body [6]:

```typescript
const { data: message, response } = await client.messages
  .withResponse()
  .create({
    model: "claude-sonnet-4-6",
    max_tokens: 1024,
    messages: [{ role: "user", content: "Hello" }]
  });

console.log(response.headers.get("anthropic-ratelimit-requests-remaining"));
console.log(message.usage.input_tokens);
```

### Custom Fetch

The TypeScript SDK supports injecting a custom `fetch` implementation as the extension point for transport-level interception [6]:

```typescript
const client = new Anthropic({
  fetch: async (url, init) => {
    // Pre-request instrumentation
    const response = await fetch(url, init);
    // Post-response instrumentation (read headers, log usage)
    return response;
  }
});
```

## No Native Middleware Interface

Neither SDK provides a formal middleware or interceptor registration API [5] [6]. The extension points are:

| SDK | Extension Point | Mechanism |
|-----|----------------|-----------|
| Python | Custom httpx transport | `DefaultHttpxClient(transport=...)` [5] |
| Python | Raw response | `.with_raw_response.create()` [5] |
| Python | Token counting | `.messages.count_tokens()` [7] |
| TypeScript | Custom fetch | `new Anthropic({ fetch: ... })` [6] |
| TypeScript | Raw response | `.withResponse().create()` [6] |

## Third-Party Middleware

Several libraries wrap the SDK to provide usage interception:

- **Revenium middleware** — wraps `messages.create` and `messages.stream` with metadata dict pattern [25]
- **AgentOps** — auto-instrumentation that captures usage fields without code changes [26]
- **OpenLLMetry** — OTel span decoration for Anthropic calls with cost attributes [28]

## Agent SDK Hooks

The Anthropic Agent SDK (separate from the core messages SDK) has a hooks system oriented toward agent-loop control [8]. These are **not** per-request usage meters — they control agent behavior. However, the `ResultMessage` from each `query()` call includes `total_cost_usd` and `model_usage` for cost tracking [8].

## Gaps and Limitations

- The streaming output token bug (issues #424/#454) was identified from discovery agent search results, not from a directly fetched page. Fix version and current status are unconfirmed [5].
- The TypeScript SDK's `withResponse()` pattern was identified from discovery agent snippets. The exact API surface may have evolved [6].
- Whether the Python SDK exposes rate limit headers on streaming responses (where the HTTP response precedes the SSE stream) is not explicitly documented in the snippets available.
- The custom fetch/transport patterns are idiomatic but not SDK-documented middleware interfaces — they rely on knowledge of the underlying HTTP client libraries (httpx, fetch API).
