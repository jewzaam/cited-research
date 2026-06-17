# Context7 MCP Integration with Local Knowledge Repos

*Last revised: 2026-06-17*

## Summary

Context7 is a cloud-hosted MCP server that fetches up-to-date public library documentation into LLM context [17]. This analysis evaluates whether it adds value for a developer who already maintains local knowledge repositories (`~/source/standards/`, `~/source/knowledgebase/`, `~/source/gws-cli-notes/`) and uses Claude Code as their primary AI coding tool.

**Bottom line**: Context7 fills a narrow but real gap — up-to-date API reference for fast-moving public libraries — that local knowledge repos do not cover. Whether that gap justifies the trade-offs (cloud dependency, rate limits, supply chain risk, token overhead) depends on how frequently the developer works with rapidly changing library APIs versus stable tooling.

## Methodology

Research conducted via 10 parallel sub-agents (5 discovery + 5 counter-discovery) across 5 dimensions, augmented by multi-engine search (DuckDuckGo) and 12 deep-read WebFetch calls. All claims traced to web sources visited in-session. Two independent audit agents verified citations and consistency (see [audit/](audit/)).

---

## 1. What Context7 Actually Provides

Context7 exposes two MCP tools: `resolve-library-id` (converts library name to Context7 ID) and `query-docs` (fetches documentation for that ID) [7]. Both are capped at 3 calls per question [7]. The two-step flow is mandatory — skipping the resolve step is "the #1 mistake seen in agent traces" [7].

After a January 2026 architecture redesign, Context7 performs server-side reranking rather than client-side filtering, reducing average context tokens from ~9,700 to ~3,300 (65%), latency from 24s to 15s (38%), and tool calls from 3.95 to 2.96 per query (30%) [8].

Library coverage is **popularity-driven and community-submitted** [3]. Exact count is disputed: one source reports 104,000+ [3], another 33,000+ [2]. Context7 does not publish an official count. Refresh frequency ranges from daily (top 100 libraries) to every 45 days (long tail) [3].

The free tier was reduced from ~6,000 to 1,000 requests/month in January 2026 — an 83% cut with no advance notice [2][16]. Some users experienced even lower limits of 500/month with 60 requests/hour caps, representing a 92% reduction [2]. The 83% and 92% figures reflect different user experiences: 83% is the official reduction (6,000→1,000), 92% is what some users actually encountered (6,000→500) [2]. Pro tier is $10/seat/month for 5,000 requests with private repo indexing [2][3].

### Security: ContextCrush

On February 18, 2026, Noma Security discovered a critical supply chain vulnerability (ContextCrush) where Context7's "Custom Rules" feature served attacker-controlled instructions verbatim to AI agents with no sanitization [1]. A proof-of-concept demonstrated .env file exfiltration and local file deletion [1]. Upstash accepted the findings on Feb 19, deployed a fix on Feb 23, and Noma publicly disclosed on March 5 [1]. No exploitation in the wild was observed [1].

The broader implication extends beyond Context7: "Any MCP server that aggregates user-generated or third-party content and serves it into an agent's context creates the same trust confusion" [1]. The attack surface is not what the MCP server can do, but what it can make the AI agent do [1].

---

## 2. Complementarity with Local Knowledge Repos

Context7 and local knowledge repos serve fundamentally different purposes:

| What You Need | Where It Lives |
|--------------|----------------|
| "What method signature does FastAPI 0.115 use for dependency injection?" | Context7 [20] |
| "What naming convention does this project use for CLI flags?" | ~/source/standards/ |
| "What's the K8s client-go quirk where Watch connections drop after 10 minutes?" | ~/source/knowledgebase/ |
| "What does `gws worktree create` do exactly?" | ~/source/gws-cli-notes/ |

Context7 covers **public library API surfaces** — method signatures, code examples, configuration options. Local repos cover **internal knowledge** — conventions, quirks, decisions, and facts that exist nowhere on the public web.

The overlap is minimal. Context7 does not and cannot index local repos [17]. Local repos typically do not document library API surfaces. The gap between them — cross-cutting integration knowledge about how libraries interact in a specific environment — is covered by neither system.

### When Context7 Adds Value

For fast-moving libraries where training data becomes stale:
- **FastAPI**: Updated every 10 hours on Context7, frequent breaking changes between versions [20]
- **React/Next.js**: Updated within hours, active API additions (Server Components, App Router) [22]
- **Anthropic SDK**: Rapidly evolving API surface [24]

### When Context7 Adds No Value

For the developer's primary knowledge needs:
- Internal coding standards (descriptive variable names, snake_case conventions, Makefile patterns)
- Vendor quirks discovered through experience (K8s gotchas, OAuth token behavior, NINA plugin internals)
- CLI tool usage facts (gws, gwt wrappers)
- Stable libraries where training data is accurate (Go standard library, pytest, click)

---

## 3. Integration Architecture

Adding Context7 to Claude Code is one command [7]:

```bash
claude mcp add --scope user --transport http context7 https://mcp.context7.com/mcp
```

With an API key: add `--header "Authorization: Bearer YOUR_KEY"` [7].

### Token Overhead

The critical concern with adding any MCP server is context window consumption. Without Tool Search enabled, a typical multi-server setup (several servers, 50+ tools) can consume 50,000–100,000 tokens before any work begins [15]. One practitioner measured 81,986 tokens (41% of 200k context) from 12 MCP servers with combined tool definitions [9] — these are different measurements of the same phenomenon at different scales.

**Tool Search solves this**. Enabled by default in Claude Code, it activates when MCP tools exceed 10% of context, reducing overhead from ~72,000 to ~8,700 tokens (85% reduction) regardless of server count [6][15]. It requires Sonnet 4+ or Opus 4+ and improved Opus 4 tool selection accuracy from 49% to 74% [15].

With Tool Search, adding Context7 as one additional MCP server is low-cost — tool definitions load on-demand rather than upfront [6].

### Known Issues

1. **Tool name conflicts**: Context7 has caused "Tool names must be unique" errors with parallel agents [28]
2. **LLM confusion**: Models struggle with 10–20+ tools — confuse similar tools, hallucinate tool names [9]
3. **Network dependency**: Remote endpoint requires internet; no graceful offline fallback documented [6]
4. **Restart required**: Config changes need Claude Code restart [15]

### Coexistence with CLAUDE.md

CLAUDE.md and MCP servers are complementary systems [6]. CLAUDE.md is loaded at session start as persistent context. Context7 tools are invoked on-demand. There is no documented conflict between them. Anthropic recommends keeping CLAUDE.md under ~200 lines [32] and fetching documentation via MCP on demand rather than embedding API references directly [15].

---

## 4. Practical Value for the Developer's Stack

Direct verification on context7.com (2026-06-17) confirmed coverage for 8 of 14 tested libraries:

| Library | Indexed | Trust Score | Tokens | Value Add |
|---------|---------|-------------|--------|-----------|
| Django | Yes [19] | 8.8 | 2.1M | Medium — stable but version transitions matter |
| FastAPI | Yes [20] | 9.9 | 127K | **High** — fast-moving, frequent breaking changes |
| Go (golang) | Yes [21] | 8.3 | 2.4M | Low — stable, training data sufficient |
| React | Yes [22] | 10 | 800K | **High** — active development, API additions |
| Next.js | Yes [22] | 10 | 527K | **High** — fast-moving, frequent breaking changes |
| Docker Compose | Yes | — | — | Low — stable API |
| Anthropic SDK Go | Yes [24] | 8.8 | 22K | Medium — thin coverage (132 snippets) |
| Ansible AAP 2.5 | Yes [23] | 10 | 683K | Low — updated monthly; local knowledgebase more targeted |

**Not found**: pytest, click, pip, Podman, Kubernetes client-go, Kubernetes client-python, Helm core. These may exist under different names — absence in search is not definitive [3].

**Net assessment**: Context7 provides genuine value for React/Next.js and FastAPI work. For the rest of the stack (Go, Ansible, K8s, containers, CLI tools), the developer's existing local repos and Claude's training data likely suffice.

---

## 5. Alternatives Worth Considering

### Grounded Docs MCP Server (docs-mcp-server)

Open-source (MIT), runs locally, indexes 90+ formats including PDF, Office, and local folders [12]. Could bridge the gap by making the developer's local repos accessible via MCP tools rather than only via CLAUDE.md references and Read tool calls. Requires Node.js 22+ [12].

### Context by Neuledge

Fully offline alternative using SQLite FTS5 with BM25 scoring [4]. Sub-10ms query latency, no rate limits, portable 1–5MB packages [4][11]. But requires building indexes manually — no community library index [11]. Apache 2.0 license [11]. **Quality concern**: performance claims come from the vendor who sells a competing product [4].

### WebFetch (Already Available)

Claude Code's built-in WebFetch tool can fetch and summarize any documentation URL on demand [7]. No setup required. Good for ad-hoc lookups but lossy (Haiku summarizes, 100KB truncation) and requires knowing the URL [7].

### llms.txt

**Dead standard**. 97% of llms.txt files received zero requests in May 2026 across 137,210 domains [13]. Google confirmed no AI system uses it [35]. A 300K domain study found no correlation with AI citations [35]. Not worth pursuing [13][35].

### MCP Ecosystem Concerns

MCP has systemic issues: 3× slower per call than direct APIs, 9.4× slower on first call, 21K+ token overhead in unoptimized configurations [33]. The ecosystem has 10,000+ servers with 30 CVEs discovered in 60 days [33]. Tool Search in Claude Code addresses the token problem but not the security surface area.

---

## Reflection

Before finalizing, the following was reconsidered:

1. **Is the complementarity assessment too generous to Context7?** The developer's stack leans toward infrastructure (K8s, Ansible, containers) where Context7 coverage is weaker, and toward stable tools (Go, pytest) where training data suffices. The high-value libraries (React, FastAPI) may not be the developer's primary work surface.

2. **Is the ContextCrush vulnerability dismissed too quickly?** The fix was deployed rapidly, but the structural concern remains: any cloud MCP aggregating community content can serve attacker-controlled instructions. For a developer with a security-conscious mindset (CLAUDE.md has explicit restrictions against destructive ops), adding a cloud trust vector is a real trade-off, not a box to check.

3. **Are the alternative accuracy claims too credible?** All competitor benchmarks (Deepcon's 90%, Nia's 52.1% hallucination) are vendor-reported with no independent validation [11]. They should inform awareness of the landscape, not drive tool selection decisions.

---

## Decision Framework

1. **How often do you work with fast-moving public library APIs (React, FastAPI, Next.js)?**
   - Frequently → Context7 adds real value. Install with user scope.
   - Rarely → Your local repos + training data likely suffice. Skip it.

2. **Are you comfortable with the security trade-off?**
   - Yes → Proceed with installation.
   - No → Consider Grounded Docs (local, MIT) or Docfork (Cabinets for context isolation) instead.

3. **Does the 1,000 requests/month free tier fit your workflow?**
   - Yes → Free tier with API key for rate limit tracking.
   - No → Either pay $10/month or use ad-hoc WebFetch for occasional lookups.

4. **Do you want your local repos accessible via MCP (not just Read tool)?**
   - Yes → Grounded Docs can index local folders as an MCP-accessible knowledge base [12]. This is a separate, complementary addition to Context7.
   - No → Current CLAUDE.md + Read tool approach works fine.

---

## Supporting Files

- [citations.md](citations.md) — All 36 sources with quality tiers and data extracted
- [references/context7-capabilities.md](references/context7-capabilities.md) — Tools, coverage, rate limits, security
- [references/complementarity.md](references/complementarity.md) — Gap analysis vs local repos
- [references/integration-architecture.md](references/integration-architecture.md) — Setup, coexistence, token management
- [references/practical-value.md](references/practical-value.md) — Stack coverage verification
- [references/alternatives.md](references/alternatives.md) — Other approaches compared
- [audit/citation-audit.md](audit/citation-audit.md) — Independent citation verification
- [audit/consistency-review.md](audit/consistency-review.md) — Cross-file consistency check
