# Complementarity Analysis: Context7 vs Local Knowledge Repos

## What Each System Covers

| Dimension | Context7 | Local Knowledge Repos |
|-----------|---------|----------------------|
| **Content type** | Public library API docs and code examples [17] | Internal conventions, vendor quirks, CLI usage facts, project rules |
| **Source** | Community-contributed, auto-crawled from GitHub/docs sites [14] | Hand-curated by developer, derived from experience |
| **Update model** | Auto-refresh daily–45 days by popularity tier [3] | Manual updates when knowledge changes |
| **Scope** | 33,000–104,000+ public libraries [2][3] | Specific to developer's toolchain and environment |
| **Privacy** | Queries sent to cloud (LLM-generated, not original prompt) [8] | 100% local — queries never leave machine [4] |
| **Cost** | Free 1,000 req/month; Pro $10/seat/month [2] | Free (disk space only) |
| **Rate limits** | 60 req/hour typical on free tier [4] | None [4] |
| **Latency** | 100–500ms per lookup [4] | <10ms via local file reads [4] |
| **Version control** | Indexes latest version by default [4] | Developer controls exactly what's documented |
| **Offline** | Requires internet [3] | Always available |

## Where Context7 Fills Gaps Local Repos Don't Cover

1. **Fast-moving public library APIs**: When React, FastAPI, or K8s client libraries ship breaking changes, Context7 auto-refreshes while local repos require manual updates [3].
2. **Version-specific API reference**: Context7 provides exact method signatures and code examples for specific library versions [7]. Local repos typically document patterns and conventions, not API surfaces.
3. **Breadth across unfamiliar libraries**: When working with a new library for the first time, Context7 provides immediate access without needing to build local documentation [3].
4. **Reducing API hallucination**: Context7 benchmarked at 65% accuracy on bleeding-edge features vs 0% for Claude Sonnet without any MCP context [11].

## Where Context7 Is Irrelevant Given Local Repos

1. **Internal coding standards** (~/source/standards/): Prescriptive rules about naming, project structure, Makefile patterns — Context7 cannot know these [32].
2. **Vendor quirk documentation** (~/source/knowledgebase/): Discovered failure modes, error envelopes, API taxonomies specific to the developer's environment — not in any public library docs.
3. **CLI tool usage facts** (~/source/gws-cli-notes/): Custom tooling behavior that exists nowhere on the public web.
4. **Project-specific conventions** (CLAUDE.md): Architecture decisions, review workflows, commit standards — inherently local.
5. **Stable, slow-moving libraries**: "Less useful if you mostly work with stable, slow-moving libraries" where training data remains accurate [3].

## The Gap Neither System Covers Well

**Cross-cutting integration knowledge** — how specific library versions interact with each other in the developer's particular environment (e.g., "Ansible 2.5 + kubernetes.core collection + Python 3.12 interaction quirks"). Context7 documents libraries in isolation. Local repos document conventions. Neither captures integration edge cases systematically.

## Token Budget Trade-off

Adding Context7 as an MCP server consumes context tokens:
- Without Tool Search: 50,000–100,000 tokens for multiple servers [15]
- With Tool Search enabled: ~8,700 tokens regardless of server count [15]
- Context7 specifically: ~3,300 tokens per query after 2026 redesign [8]

The developer's local repos are loaded via CLAUDE.md references, which Anthropic recommends keeping under ~200 lines [32]. Local file reads via Read tool consume tokens only when accessed on-demand.

**Net assessment**: Context7 adds value specifically for fast-moving public library API lookups. For a developer with well-maintained local knowledge repos, the complementary value is **narrow but real** — concentrated in the "what exact API does library X version Y expose?" use case that local repos don't address.

## Gaps and Limitations

1. Performance comparison (local <10ms vs cloud 100–500ms) comes from vendor of competing product [4]. Numbers are plausible but not independently validated.
2. Rate limit of 60 req/hour cited as "typical" [4] but exact free-tier limits vary and are not publicly documented [18].
3. Token overhead numbers assume Tool Search is disabled; with it enabled, overhead drops to ~8,700 tokens [15].
