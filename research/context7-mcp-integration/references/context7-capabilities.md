# Context7 MCP Server Capabilities

## What Context7 Does

Context7 is a cloud-hosted MCP server that fetches up-to-date, version-specific documentation for public libraries and injects it into LLM context [17]. It exposes two MCP tools [7]:

| Tool | Parameters | Purpose |
|------|-----------|---------|
| `resolve-library-id` | `libraryName` (string) | Converts free-text library name to Context7-compatible ID with version metadata and quality score |
| `query-docs` | `context7CompatibleLibraryID` (string), `topic` (string, optional) | Fetches documentation snippets for the resolved library |

The two-step flow is mandatory: `resolve-library-id` must be called before `query-docs` unless the user provides an ID in `/org/project` format [7]. Both tools are capped at **3 calls per question** [7].

## Library Coverage

| Metric | Value | Source |
|--------|-------|--------|
| Library count | 104,000+ (or 33,000+ depending on source) | [3], [2] |
| Refresh — top 100 | Daily | [3] |
| Refresh — top 1,000 | Every 15 days | [3] |
| Refresh — top 5,000 | Every 30 days | [3] |
| Refresh — everything else | Every 45 days | [3] |
| Private library support | Pro plan only ($10/seat/month) | [3] |

Coverage is **popularity-driven and community-submitted** [3]. Libraries not already tracked must be manually submitted [3].

## Quality and Trust

Context7 scores libraries via developer-like benchmark questions [14]. Verified status requires trust score ≥ 9, or top 100 by MCP usage with trust score ≥ 6, or owner claim [14].

Quality varies: average 8.16/10 across 12 experiments, but cross-library queries scored as low as 3.5/10 [2]. Context7 acknowledges it "cannot guarantee the accuracy, completeness, or security of all community-contributed library documentation" [17].

Content moderation uses a two-pass prompt-injection detection pipeline [14]. The Enterprise edition (April 2026) added LLM-based content scanning [2].

## Performance After 2026 Redesign

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Avg context tokens | ~9,700 | ~3,300 | −65% [8] |
| Avg latency | 24s | 15s | −38% [8] |
| Avg tool calls/query | 3.95 | 2.96 | −30% [8] |

The redesign moved filtering and ranking server-side via reranking models [8]. The old `getDocs` method was replaced with `getContext`, eliminating manual pagination [8].

## Rate Limits and Pricing

| Plan | Cost | Calls/month | Notes |
|------|------|-------------|-------|
| Free (no key) | $0 | 1,000 | Public repos only. Some users report as low as 500/month [2] |
| Free (with key) | $0 | 1,000 | Higher limits via dashboard key [7] |
| Pro | $10/seat/month | 5,000 | Adds private repo indexing. Overage: $10 per 1,000 additional [2] |
| Enterprise | Custom | Custom | SOC 2 Type II, GDPR/CCPA, SSO, RBAC, on-premise Docker [2] |

Free tier was reduced from ~6,000/month to 1,000/month in January 2026 — an 83% cut with no advance notice [2][16]. Some users experienced a 60 requests/hour limit, representing a 92% reduction [2]. When the monthly cap is reached, users get 20 bonus API calls per day [2].

Rate limit headers (Retry-After, RateLimit-Limit, RateLimit-Remaining, RateLimit-Reset) are returned on 429 responses [18]. Exact limits are not publicly documented — they are gated behind the authenticated dashboard [18].

## ContextCrush Security Vulnerability

In February 2026, Noma Security discovered a critical supply chain vulnerability named ContextCrush [1]:

- **Mechanism**: The "Custom Rules" feature allowed library owners to set "AI Instructions" served verbatim to all users with no sanitization, content filtering, or distinction from legitimate documentation [1].
- **Attack vector**: Anyone with a GitHub account could register a library, poison Custom Rules, manufacture credibility via self-interaction, and have malicious instructions delivered through trusted MCP channels [1].
- **PoC demonstrated**: AI agent read .env files, exfiltrated contents via GitHub Issues, and deleted local folders [1].
- **Timeline**: Discovered Feb 18, fix deployed Feb 23, public disclosure March 5, 2026 [1].
- **No exploitation in the wild** was observed [1].
- **Broader implication**: "Any MCP server that aggregates user-generated or third-party content and serves it into an agent's context creates the same trust confusion" [1]. Read-only servers are still dangerous because the attack surface is "what it can make the AI agent do" [1].

## Gaps and Limitations

1. Library count discrepancy (104,000+ vs 33,000+) unresolved — Context7 does not publish an official count [2][3].
2. Tool naming inconsistency (`query-docs` vs `get-library-docs`) across sources [7][36].
3. No public documentation of exact rate limit numbers [18].
4. Version-specific access mechanism not fully documented — UI shows "Latest" rather than specific versions [7].
5. Private library refresh is not automatic — requires manual triggers [3].
