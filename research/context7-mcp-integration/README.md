# Context7 MCP + Local Knowledge Repos: Integration Assessment

*Last revised: 2026-06-17*

Context7 is a cloud MCP server that injects up-to-date public library documentation into LLM context. This research evaluates whether it complements a developer's existing local knowledge management setup (coding standards, vendor knowledgebase, CLI notes repos) used with Claude Code.

## Key Finding

Context7 fills a **narrow but real gap**: version-specific API reference for fast-moving public libraries (React, FastAPI, Next.js). It does not overlap with local repos, which cover internal conventions, vendor quirks, and project-specific knowledge. The trade-offs — cloud dependency, 1,000 req/month free tier, supply chain risk (ContextCrush), token overhead — make the value proposition stack-dependent.

## Stack Coverage (Verified 2026-06-17)

| Library | Context7? | Value Add |
|---------|-----------|-----------|
| React / Next.js | Yes (trust 10) | **High** — fast-moving APIs, updated hourly |
| FastAPI | Yes (trust 9.9) | **High** — frequent breaking changes |
| Django | Yes (trust 8.8) | Medium — version transitions |
| Ansible AAP 2.5 | Yes (trust 10) | Low — monthly updates; local KB more targeted |
| Go (golang) | Yes (trust 8.3) | Low — stable, training data sufficient |
| Anthropic SDK Go | Yes (trust 8.8) | Medium — thin coverage (132 snippets) |
| K8s client libs | **Not found**\* | Gap — complex, version-specific |
| pytest, click, Podman | **Not found**\* | Low impact — stable APIs |

\* "Not found" means search did not surface these libraries; they may exist under different names. Search was not exhaustive.

## Quick Decision

1. **Work frequently with React/FastAPI/Next.js?** → Install Context7 (`claude mcp add --scope user --transport http context7 https://mcp.context7.com/mcp`)
2. **Mostly infrastructure/K8s/Ansible/Go?** → Skip it. Your local repos + training data cover it.
3. **Want local repos MCP-accessible?** → Look at [Grounded Docs](https://github.com/arabold/docs-mcp-server) (MIT, indexes local folders, 90+ formats)
4. **Security-conscious about cloud MCP?** → Consider [Docfork](https://neuledge.com/blog/2026-02-06/top-7-mcp-alternatives-for-context7-in-2026/) (Cabinets for context isolation) or Context by Neuledge (fully offline)

## Key Numbers

| Metric | Value | Source |
|--------|-------|--------|
| Free tier | 1,000 req/month (cut 83% from 6,000 in Jan 2026; some users saw 92% cut to 500) | [ChatForest review](https://chatforest.com/reviews/context7-mcp-server/) |
| Pro tier | $10/seat/month, 5,000 req | [AltexSoft](https://www.altexsoft.com/blog/context7/) |
| Avg tokens per query | ~3,300 (down from 9,700) | [Upstash](https://upstash.com/blog/new-context7) |
| Tool Search overhead | ~8,700 tokens total (85% reduction) | [Builder.io](https://www.builder.io/blog/claude-code-mcp-servers) |
| Library count | 33,000–104,000+ (sources disagree; no official count) | [ChatForest](https://chatforest.com/reviews/context7-mcp-server/), [AltexSoft](https://www.altexsoft.com/blog/context7/) |
| Accuracy | 65% (vs 0% without any MCP context — vendor benchmarks) | [ChatForest](https://chatforest.com/reviews/context7-mcp-server/) |
| ContextCrush | Patched Feb 23, 2026; no exploitation in wild | [Noma Security](https://noma.security/blog/contextcrush-context7-the-mcp-server-vulnerability/) |

## Files

- [analysis.md](analysis.md) — Full analysis with methodology and decision framework
- [citations.md](citations.md) — 36 sources with quality tiers
- [references/](references/) — One file per research dimension
- [audit/](audit/) — Independent citation and consistency verification
