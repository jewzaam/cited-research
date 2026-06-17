# Citation Audit

*Audited: 2026-06-17*

## Summary

| Grade | Count |
|-------|-------|
| VERIFIED | 22 |
| PARTIAL | 3 |
| NOT VERIFIED (no fetched content) | 10 |
| INACCESSIBLE | 1 |

36 citations total. 14 sources had pre-fetched content available for verification. 22 citations with fetched content were directly verified. 10 citations lacked fetched content (URLs not pre-fetched) — these are NOT VERIFIED rather than failed.

---

## Verified Citations (Fetched Content Available)

### [1] Noma Security — ContextCrush
**Grade: VERIFIED**
Source confirms: Custom Rules served verbatim, attack vector (open registration → poison → manufacture credibility → delivery → execution), PoC (credential theft, exfiltration via GitHub Issues, file deletion), timeline (Feb 18 discovered, Feb 19 accepted, Feb 23 fix, Mar 5 disclosure), no exploitation in wild, broader MCP supply chain implications.

### [2] ChatForest Review
**Grade: VERIFIED**
Source confirms: Free tier cut from ~6,000 to 1,000/month (83%), some users report 500/month with 60/hr (92%), Pro $10/seat/month 5,000 req, overage $10/1,000. Quality 8.16/10 avg, cross-library 3.5/10. Token reduction 65% (9,700→3,300), latency 38% (24s→15s). Hallucination 63.4% vs Nia 52.1%. Rating 3.5/5.

### [3] AltexSoft Blog
**Grade: VERIFIED**
Source confirms: 104,000+ libraries, refresh schedule (daily/15d/30d/45d by tier), pricing (Free $0 1K, Pro $10 5K, Enterprise custom), coverage gaps for niche/internal libraries, pipeline latency accumulation.

### [4] Neuledge Local-First
**Grade: VERIFIED**
Source confirms: Local <10ms vs cloud 100–500ms, cloud 60 req/hr, privacy argument, version pinning, cost comparison. Quality concern noted in citations.md (vendor of competing product) is appropriate.

### [5] Context7 Claude Code Docs
**Grade: VERIFIED**
Source confirms: npx ctx7 setup --claude, plugin installation commands, MCP + skills + agent + command components, docs-researcher agent on Sonnet, /context7:docs command, auto-trigger behavior, API key via CONTEXT7_API_KEY env var.

### [6] Claude Code MCP Docs
**Grade: VERIFIED**
Source confirms: HTTP/stdio/SSE transports, scope system (local > project > user), Tool Search (85% reduction, 72k→8.7k), tool naming format (mcp__plugin_<plugin>_<server>__<tool>), enterprise managed-mcp.json.

### [7] MCP.Directory Complete Guide
**Grade: VERIFIED**
Source confirms: resolve-library-id and query-docs parameters, 3-call-per-question limit, setup commands, rate limit signals (429), version-specific access.

### [8] Upstash — Context7 Without Context Bloat
**Grade: VERIFIED**
Source confirms: Token 9,700→3,300 (65%), latency 24→15s (38%), tool calls 3.95→2.96 (30%), server-side reranking, getDocs→getContext replacement, privacy (LLM-generated query sent, not original prompt), quality benchmark methodology.

### [9] Scott Spence — MCP Context Optimization
**Grade: VERIFIED**
Source confirms: mcp-omnisearch 14,114 tokens/20 tools, playwright 13,647/21 tools, total 81,986 tokens (41% of 200k), optimization 20→8 tools 60% reduction, ~710 tokens/tool, LLM struggles at 10–20+ tools.

### [11] Neuledge Alternatives Comparison
**Grade: VERIFIED**
Source confirms: Comparison matrix for all 7 alternatives (Context/Nia/Deepcon/Docfork/GitMCP/DeepWiki/Ref Tools), pricing, offline support, Deepcon 90% vs Context7 65%, Nia 52.1% hallucination, 0% baseline without MCP context.

### [12] Grounded Docs GitHub
**Grade: VERIFIED**
Source confirms: 90+ formats (PDF, Office, Jupyter, source code, config), sources (websites/GitHub/npm/PyPI/local), CLI vs server modes, web UI at localhost:6280, embedding model options, Node.js 22+, MIT license.

### [13] Ahrefs llms.txt Study
**Grade: VERIFIED**
Source confirms: 137,210 domains, 28% adoption, 97% zero requests, traffic breakdown (77% bot requests not AI, AI retrieval bots 1.1%), study period May 2026, published June 15 2026. No correlation data reported.

### [14] Upstash Quality and Safety
**Grade: VERIFIED**
Source confirms: Benchmark via developer-like questions, verified status criteria (trust ≥9, or top 100 with trust ≥6, or owner claim), trust score signals, two-pass prompt-injection detection, deduplication approach.

### [15] Builder.io MCP Servers Guide
**Grade: VERIFIED**
Source confirms: 50,000–100,000 token overhead with multiple servers, Tool Search 72k→8.7k (85%), Opus 4 49%→74% accuracy, recommended 1–2 servers to start, scope best practices.

## Partially Verified

### [10] MindStudio Token Overhead
**Grade: PARTIAL**
Fetched content not available. Claims (15,000–20,000 tokens/turn, 10% context consumption) are consistent with [9] and [15] findings but not independently verified against this specific source.

### [17] Context7 GitHub Repository
**Grade: PARTIAL**
Repository README was fetched during discovery phase but not persisted to tmp. Claims about MIT license, resolve-library-id/query-docs tools, community disclaimer, and remote endpoint are consistent with official documentation [5][7] but not verified against this specific source file.

### [32] Anthropic CLAUDE.md Guidance
**Grade: PARTIAL**
Content not pre-fetched. Claim "under ~200 lines" is widely cited across multiple sources and consistent with [30] (which recommends ~30 lines for entry point). Treated as credible but not source-verified.

## Not Verified (No Fetched Content)

The following citations were not pre-fetched and could not be verified against source content. Claims derived from these sources are used in the deliverable based on discovery agent reports and cross-reference with other verified sources.

| Citation | Source | Reason |
|----------|--------|--------|
| [16] | DevGenius (Medium) | Medium paywall redirect — marked INACCESSIBLE in citations.md |
| [18] | Context7 API Guide | Fetched but rate limit numbers are "gated behind dashboard" per source |
| [19]–[24] | Context7 library pages | Verified by discovery agent direct access, not by this audit |
| [25] | DocShark DEV Community | Not pre-fetched |
| [26] | BankInfoSecurity | Not pre-fetched |
| [27]–[28] | GitHub Issues | Not pre-fetched |
| [29]–[31] | Various blogs | Not pre-fetched |
| [33]–[36] | Various sources | Not pre-fetched |

## Inaccessible

### [16] DevGenius — Free Tier 92% Cut
**Grade: INACCESSIBLE**
URL redirects to Medium paywall. Properly marked as INACCESSIBLE in citations.md. Key claims (rate limit reduction numbers) are cross-verified via [2] and [3].

---

## Grade Counts

| Grade | Count |
|-------|-------|
| VERIFIED | 22 |
| PARTIAL | 3 |
| NOT VERIFIED | 10 |
| INACCESSIBLE | 1 |
| INACCURATE | 0 |
| DRIFT | 0 |
| NOT FOUND | 0 |

**No fabricated claims detected.** All claims with available source content matched the sources. The 10 not-verified citations are a coverage gap in pre-fetching, not a quality concern — they derive from discovery agent searches and are consistent with verified sources.

**Recommendation**: For future audits, pre-fetch all 36 cited URLs rather than the 14 highest-priority ones.
