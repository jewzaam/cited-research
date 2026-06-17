# Citations

All sources visited in-session via WebSearch or WebFetch on 2026-06-17.

## Source List

[1] **ContextCrush: The Context7 MCP Server Vulnerability Hiding in Plain Sight** — Noma Security.
Published 2026-05-03. URL: https://noma.security/blog/contextcrush-context7-the-mcp-server-vulnerability/
Data extracted: ContextCrush vulnerability mechanism, attack vector, PoC demonstration, timeline (Feb 18 discovered, Feb 19 accepted, Feb 23 fix deployed, Mar 5 public disclosure), remediation details, broader MCP supply chain implications.
Tier 1 (security research disclosure).

[2] **The Context7 MCP Server — Real-Time Library Docs, Registry Risk Included** — ChatForest.
Published 2026-03-14. URL: https://chatforest.com/reviews/context7-mcp-server/
Data extracted: Free tier rate limit cuts (6,000→1,000/month, 83–92% reduction), pricing ($10/seat/month Pro), library count (33,000+), quality scores (8.16/10 avg, 3.5/10 worst), hallucination rate (63.4%), accuracy (65%), token reduction (65%), latency (24s→15s). Overall rating 3.5/5.
Tier 3 (industry review).

[3] **Our Experience Using Context7 MCP in Agentic Coding Workflow** — AltexSoft.
Published 2026. URL: https://www.altexsoft.com/blog/context7/
Data extracted: Library count (104,000+), refresh schedule (daily–45 days by tier), pricing tiers, coverage gap patterns, pipeline latency accumulation, private library limitations.
Tier 2 (established reference site).

[4] **Local-First Documentation: What It Is and Why Your AI Agent Needs It** — Neuledge.
Published 2026-02-19. URL: https://neuledge.com/blog/2026-02-19/local-first-documentation-for-ai
Data extracted: Local vs cloud performance (<10ms vs 100–500ms), rate limit comparison (none vs 60/hr), privacy argument, version pinning, cost comparison, @neuledge/context tool details.
Tier 3 (vendor blog — claims are vendor's own). Quality concern: author is vendor of competing product.

[5] **Claude Code — Context7 MCP** — Context7 (official docs).
URL: https://context7.com/docs/clients/claude-code
Data extracted: Setup commands (npx ctx7 setup --claude), plugin installation, MCP vs skill mode, docs-researcher agent, /context7:docs command, auto-trigger behavior, API key configuration.
Tier 1 (official documentation).

[6] **Connect Claude Code to tools via MCP** — Claude Code Docs (official).
URL: https://code.claude.com/docs/en/mcp
Data extracted: Transport types (HTTP, stdio, SSE), scope system (local > project > user), Tool Search feature (85% reduction, 72k→8.7k tokens), tool naming format, enterprise managed-mcp.json.
Tier 1 (official documentation).

[7] **Context7 MCP Server: Complete Setup Guide (2026)** — MCP.Directory.
Published 2026-05-11. URL: https://mcp.directory/blog/context7-mcp-complete-guide-2026
Data extracted: Tool parameters (resolve-library-id, query-docs), 3-call-per-question limit, setup commands for Claude Code, version-specific documentation access, rate limit signals, best practices.
Tier 2 (established reference site).

[8] **Context7 Without Context Bloat** — Upstash (official blog).
Published 2026. URL: https://upstash.com/blog/new-context7
Data extracted: Token reduction 9,700→3,300 (65%), latency 24s→15s (38%), tool calls 3.95→2.96 (30%), server-side reranking architecture, quality benchmark methodology (80+ questions scored by Claude Sonnet).
Tier 1 (vendor official blog).

[9] **Optimising MCP Server Context Usage in Claude Code** — Scott Spence.
Published 2026. URL: https://scottspence.com/posts/optimising-mcp-server-context-usage-in-claude-code
Data extracted: Per-server token costs (mcp-omnisearch 14,114 tokens/20 tools, playwright 13,647/21 tools), total overhead 81,986 tokens (41% of 200k context), optimization results (20→8 tools, 60% reduction), LLM struggles at 10–20+ tools.
Tier 3 (practitioner blog).

[10] **Claude Code MCP Servers and Token Overhead** — MindStudio.
Published 2026. URL: https://www.mindstudio.ai/blog/claude-code-mcp-server-token-overhead
Data extracted: Multi-server overhead 15,000–20,000 tokens/turn, 10% context consumption before work, MCP definitions injected every API call, recommendation to prune unused servers.
Tier 3 (industry blog).

[11] **Top 7 MCP Alternatives for Context7 in 2026** — Neuledge.
Published 2026-02-06. URL: https://neuledge.com/blog/2026-02-06/top-7-mcp-alternatives-for-context7-in-2026/
Data extracted: Comparison matrix for Context (Neuledge), Nia, Deepcon, Docfork, GitMCP, DeepWiki, Ref Tools — pricing, accuracy, offline support, library coverage, token efficiency, use case recommendations.
Tier 3 (vendor blog — author sells competing product). Quality concern: benchmarks are vendor-reported.

[12] **Grounded Docs MCP Server** — GitHub (arabold/docs-mcp-server).
URL: https://github.com/arabold/docs-mcp-server
Data extracted: Supported formats (90+ languages, PDF, Office, archives), source types (websites, GitHub, npm, PyPI, local), CLI vs server modes, embedding model options, Node.js 22+ requirement, MIT license.
Tier 1 (primary source — repository).

[13] **97% of llms.txt Files Get Zero Requests** — Ahrefs.
Published 2026-06-15. URL: https://ahrefs.com/blog/llmstxt-study/
Data extracted: 137,210 domains studied, 28% adoption, 97% zero requests, traffic breakdown (77% of bot requests not from AI tools, AI retrieval bots only 1.1%), no citation correlation found.
Tier 2 (established reference site — empirical study).

[14] **Context7 Quality and Safety** — Upstash (official blog).
URL: https://upstash.com/blog/context7-quality-and-safety
Data extracted: Benchmark scoring methodology, verified library criteria (trust score ≥9 or top 100), trust score signals, two-pass prompt-injection detection, content moderation pipeline, deduplication approach.
Tier 1 (vendor official blog).

[15] **The Best MCP Servers for Developers in 2026** — Builder.io.
Published 2026. URL: https://www.builder.io/blog/claude-code-mcp-servers
Data extracted: 50,000–100,000 token overhead with multiple servers, Tool Search 72k→8.7k (85%), scope best practices, recommended 1–2 servers to start, Opus 4 tool selection 49%→74%.
Tier 2 (established reference site).

[16] **Context7 Quietly Slashed Its Free Tier by 92%** — DevGenius (Medium).
Published 2026. URL: https://blog.devgenius.io/context7-quietly-slashed-its-free-tier-by-92-16fa05ddce03
Data extracted: Rate limit reduction from ~200 requests/day (~6,000/month) to 500–1,000/month. Note: page behind Medium paywall; details cross-verified via [2] and [3].
Tier 3 (industry blog). INACCESSIBLE (Medium paywall redirect).

[17] **GitHub — upstash/context7** — Context7 official repository.
URL: https://github.com/upstash/context7
Data extracted: MCP tools (resolve-library-id, query-docs), remote endpoint (https://mcp.context7.com/mcp), community-contributed model disclaimer, MIT license, 54.1K+ stars.
Tier 1 (primary source — repository).

[18] **API Guide — Context7 MCP** — Context7 (official docs).
URL: https://context7.com/docs/api-guide
Data extracted: Rate limit headers (Retry-After, RateLimit-Limit, RateLimit-Remaining, RateLimit-Reset), 429 status on exceed, 11 API endpoints including /api/v2/libs/search and /api/v2/context. Exact rate limit numbers not disclosed publicly — gated behind dashboard.
Tier 1 (official documentation).

[19] **Context7 Django page** — Context7.
URL: https://context7.com/django/django
Data extracted: 2,151,957 tokens, 24,330 snippets, trust score 8.8, last updated 2 weeks prior to verification.
Tier 1 (primary source — product page). Verified by discovery agent direct access.

[20] **Context7 FastAPI page** — Context7.
URL: https://context7.com/fastapi/fastapi
Data extracted: 127,807 tokens, 2,124 snippets, trust score 9.9, last updated 10 hours prior to verification.
Tier 1 (primary source). Verified by discovery agent direct access.

[21] **Context7 Go page** — Context7.
URL: https://context7.com/golang/go
Data extracted: 2,447,540 tokens, 13,367 snippets, trust score 8.3, last updated 1 week prior to verification.
Tier 1 (primary source). Verified by discovery agent direct access.

[22] **Context7 React page** — Context7.
URL: https://context7.com/reactjs/react.dev
Data extracted: 800,029 tokens, 7,143 snippets, trust score 10, last updated 3 hours prior to verification.
Tier 1 (primary source). Verified by discovery agent direct access.

[23] **Context7 Ansible AAP 2.5 page** — Context7.
URL: https://context7.com/websites/redhat_en_red_hat_ansible_automation_platform_2_5
Data extracted: 683,224 tokens, 10,310 snippets, trust score 10, last updated 1 month prior to verification.
Tier 1 (primary source). Verified by discovery agent direct access.

[24] **Context7 Anthropic Go SDK page** — Context7.
URL: https://context7.com/anthropics/anthropic-sdk-go
Data extracted: 22,128 tokens, 132 snippets, trust score 8.8, last updated 4 weeks prior to verification.
Tier 1 (primary source). Verified by discovery agent direct access.

[25] **DocShark: a local-first documentation MCP server for AI** — DEV Community.
Published 2026-03-19. URL: https://dev.to/dev_michael/docshark-a-local-first-documentation-mcp-server-for-ai-ia9
Data extracted: Local-first alternative using Crawl4AI, broader website coverage than Context7. Claims 1,000 pages/min crawl speed.
Tier 3 (developer blog).

[26] **Context7 Flaw Let Attackers Slip Commands to AI Agents** — BankInfoSecurity.
Published 2026. URL: https://www.bankinfosecurity.com/context7-flaw-let-attackers-slip-commands-to-ai-agents-a-30974
Data extracted: PoC demonstrated .env exfiltration and file deletion. Underlying problem described as architectural, not Context7-specific. MCP spec acknowledges tool descriptions should be considered untrusted.
Tier 2 (established security news).

[27] **Being rate limited on every request — Issue #808** — GitHub (upstash/context7).
URL: https://github.com/upstash/context7/issues/808
Data extracted: User complaints about rate limiting even with API key.
Tier 1 (primary source — issue tracker).

[28] **context7 mcp in claude CLI preventing agents from spinning up — Issue #877** — GitHub (upstash/context7).
URL: https://github.com/upstash/context7/issues/877
Data extracted: Tool name collision issues, parallel agent launch failures.
Tier 1 (primary source — issue tracker).

[29] **I Built a Context7 Local-First Alternative With Claude Code** — Medium (Moshe Simantov).
Published 2026-02-08. URL: https://medium.com/@moshesimantov/i-built-a-context7-local-first-alternative-with-claude-code-eb14c9fd654f
Data extracted: Developer motivation for building local alternative — rate limits, latency, privacy concerns. Note: author is Neuledge CEO; product interest.
Tier 3 (developer blog). Quality concern: author is vendor of competing product.

[30] **You Don't Need a CLAUDE.md** — DEV Community (byme8).
URL: https://dev.to/byme8/you-dont-need-a-claudemd-jgf
Data extracted: Argument for minimal 30-line CLAUDE.md as entry point + organized docs/ folder. LLM discovers relevant docs on-demand.
Tier 4 (personal blog).

[31] **Context Window Management for LLM Apps: Dev Guide** — Redis.
URL: https://redis.io/blog/context-window-management-llm-apps-developer-guide/
Data extracted: "Lost-in-the-middle" problem, 7× latency increase at 15,000 words, fewer high-quality docs outperform more marginal ones.
Tier 2 (established reference site).

[32] **Give Claude context: CLAUDE.md and better prompts** — Anthropic (official).
URL: https://support.claude.com/en/articles/14553240-give-claude-context-claude-md-and-better-prompts
Data extracted: CLAUDE.md should be under ~200 lines. Exclude API docs, changelogs, obvious info, aspirational rules.
Tier 1 (official documentation).

[33] **MCP is dead** — Quandri engineering blog.
URL: https://www.quandri.io/engineering-blog/mcp-is-dead
Data extracted: MCP 3× slower per call, 9.4× slower on first call, 21K+ token overhead, init failures, mid-session crashes.
Tier 3 (engineering blog).

[34] **Context7 MCP Server: Complete Setup Guide (2026)** — QuantizeLab.
Published 2026-04-07. URL: https://www.quantizelab.dev/articles/context7-mcp-claude-code-guide
Data extracted: ctx7 setup automation, CLAUDE.md integration patterns, security considerations, ContextCrush context.
Tier 3 (tutorial site).

[35] **llms.txt Shows No Clear Effect on AI Citations** — Search Engine Journal.
URL: https://www.searchenginejournal.com/llms-txt-shows-no-clear-effect-on-ai-citations-based-on-300k-domains/561542/
Data extracted: 300K domain study finding no correlation between llms.txt and AI citations. Removing the variable improved ML model accuracy.
Tier 2 (established reference site).

[36] **Context7 MCP FAQ** — Context7MCP.com (unofficial).
URL: https://context7mcp.com/faq/
Data extracted: Privacy policy notes, tool names (resolve-library-id and get-library-docs naming variant), HTTPS connection, Upstash infrastructure.
Tier 3 (unofficial FAQ aggregation).

## Discrepancies

| Data Point | Source A | Source B | Resolution |
|-----------|---------|---------|-----------|
| Library count | 104,000+ [3] | 33,000+ [2] | Unclear. [3] may count all indexed entries including duplicates/versions. [2] may count unique libraries. Both are third-party estimates; Context7 does not publish an official count. |
| Tool name for doc retrieval | `query-docs` [7] | `get-library-docs` [36] | Both names appear in different sources. The MCP server may have been renamed; `query-docs` is used in current official documentation [5][7]. |
| Rate limit: free tier | 1,000/month [2][3] | 500/month [2] | [2] reports both: 1,000 as the stated limit, 500 as what some users experienced. May reflect per-account vs per-IP enforcement. |

## Retracted Sources

None.
