# Alternatives to Context7 for Library Documentation in AI Context

## Comparison Matrix

| Tool | Pricing | Offline? | Open Source | Accuracy | Token/Response | Library Coverage |
|------|---------|----------|-------------|----------|---------------|-----------------|
| **Context7** | Free 1K/mo; $10/mo Pro | No | MIT (MCP only) | 65% [2] | ~3,300 [8] | 33K–104K [2][3] |
| **Grounded Docs** | Free | Yes | MIT | — | — | Any source [12] |
| **Context (Neuledge)** | Free | Yes | Apache 2.0 | — | ~2,000 [11] | User-built indexes [11] |
| **Docfork** | Free 1K/mo | No | MIT | — | — | 9,000+ [11] |
| **Deepcon** | $8–20/mo | No | No | 90% (vendor) [11] | ~1,000 [11] | Python, JS, TS, Go, Rust [11] |
| **Nia** | $14.99/mo+ | No | No | 52.1% hallu. [11] | — | Codebase+docs+deps [11] |
| **GitMCP** | Free | No | Yes | — | — | Any public GitHub repo [11] |
| **DeepWiki** | Free (public) | No | No | — | — | Any public repo [11] |
| **Ref Tools** | $9/mo | No | No | — | ~5,000 [11] | — |

## Self-Hosted / Local-First Options

### Grounded Docs MCP Server (docs-mcp-server)

Open-source alternative to Context7 that runs entirely locally [12]:

- **Formats**: PDF, Word, Excel, Jupyter, 90+ source code languages, HTML, Markdown, AsciiDoc, JSON, YAML, Dockerfile, Makefile, Terraform, archives [12]
- **Sources**: Websites, GitHub repos, npm, PyPI, local folders, zip archives [12]
- **Modes**: CLI (one-off queries via npx) and server (persistent with web UI at localhost:6280) [12]
- **Search**: Optional embedding models (OpenAI, Ollama, Gemini, Azure) for semantic vector search [12]
- **Requires**: Node.js 22+, optional Docker [12]
- **License**: MIT [12]
- **Strength**: Can index the developer's local repos directly, bridging the gap between local knowledge and MCP-accessible documentation

### Context by Neuledge

Fully offline documentation tool [4][11]:

- **Technology**: SQLite with FTS5 full-text search and BM25 scoring [4]
- **Performance**: Sub-10ms query latency [4]
- **Packages**: Portable SQLite databases, 1–5MB each [11]
- **Setup**: `npm install -g @neuledge/context`, `context add [repo URL]`, `context mcp` [4]
- **License**: Apache 2.0 [11]
- **Limitation**: No community-maintained library index — users must build indexes from repos [11]
- **Quality concern**: Performance claims come from the vendor [4]

### DocShark

Local-first documentation crawler [25]:

- Uses Crawl4AI engine with Playwright for browser automation
- Claims 1,000 pages/min crawling speed [25]
- Outputs clean Markdown or JSON
- Enhanced internal version at CyberAGI with public release "coming soon" [25]

## Cloud Documentation MCPs

### Deepcon

Semantic search-based documentation retrieval [11]:

- Claims 90% accuracy vs Context7's 65% across 20 real-world scenarios [11]
- Tested using Autogen, LangGraph, OpenAI Agents, Agno, OpenRouter SDK [11]
- Averages ~1,000 tokens per response (most efficient cloud option) [11]
- $8–20/month tiers [11]
- **Quality concern**: Benchmark is vendor-reported [11]

### Docfork

Context isolation-focused documentation MCP [11]:

- "Cabinets" feature hard-locks agents to verified stacks to prevent context poisoning [11]
- 9,000+ libraries, MIT license, edge-cached at ~200ms p95 [11]
- Free 1,000 requests/month per org [11]
- Supports MCP OAuth and team collaboration [11]

## Non-MCP Approaches

### WebFetch Pattern (Built into Claude Code)

No additional server needed — Claude Code's built-in WebFetch tool can fetch documentation on demand:

- Fetches URL, converts HTML to Markdown via Turndown, truncates to 100KB [7]
- Haiku 3.5 summarizes content based on prompt [7]
- 15-minute cache TTL [7]
- Certain trusted domains (docs.python.org, react.dev, developer.mozilla.org) receive simplified handling [7]
- **Limitation**: Lossy summarization, 100KB truncation, requires knowing the URL [7]

### llms.txt Standard

Proposed standard (September 2024) for /llms.txt at domain root to provide LLM-optimized documentation.

**Effectively dead**: 97% of llms.txt files received zero requests in May 2026 across 137,210 domains studied [13]. Google's John Mueller confirmed "no AI system currently uses llms.txt" [35]. A 300K domain study found no correlation between llms.txt presence and AI citations [35]. 77% of bot traffic to llms.txt files was not from AI tools [13].

### CLAUDE.md + Structured Local Docs

The developer's current approach. Anthropic's official guidance recommends keeping CLAUDE.md under ~200 lines as an entry point [32], with detailed knowledge in organized files that the LLM discovers on demand [30].

**Strengths**: Zero latency, no rate limits, no cost, complete privacy, version control of knowledge itself.
**Weakness**: Requires manual maintenance; does not cover library API surfaces.

## Relevance Assessment for This Developer

| Alternative | Relevant? | Why |
|------------|-----------|-----|
| Grounded Docs | **Yes** | Could index local repos as MCP-accessible knowledge, bridging the gap. Supports the developer's file formats. |
| Context (Neuledge) | **Maybe** | Fully offline is appealing but requires building indexes manually. No community library index. |
| Deepcon | **No** | Paid, cloud-only, covers similar ground as Context7 with unverified accuracy claims. |
| Docfork | **Maybe** | Free tier matches Context7's; Cabinets feature addresses security concerns. |
| WebFetch | **Yes** | Already available, no setup needed. Good for ad-hoc documentation lookups. |
| llms.txt | **No** | Empirically dead standard [13]. |

## Gaps and Limitations

1. All competitor accuracy benchmarks are vendor-reported — no independent verification exists [11].
2. Grounded Docs Node.js 22+ requirement may be a friction point.
3. DocShark's enhanced version is not yet publicly available [25].
4. The MCP ecosystem has systemic issues: 3× slower per call than direct API, 9.4× on first call, 21K+ token overhead in unoptimized configurations [33].
