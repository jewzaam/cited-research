# AI-Assisted Documentation Tools

Assessment of AI-powered documentation platforms for solo developers. Sources: [citations.md](../citations.md).

## Pricing Comparison

| Tool | Free Tier | Paid Start | AI Features | Per-User Cost | Lock-in Risk |
|------|-----------|------------|-------------|---------------|--------------|
| Mintlify | Yes (full platform) [34] | $250/month [34] | Agent, Assistant (250 msg/month) [34] | $20/seat [34] | Low (MDX in GitHub) |
| GitBook | Yes (1 user/site) [7] | $65/site/month [7] | Writing tools (beta), AI Assistant (Ultimate+) [7] | $12/user [7] | Medium (platform) |
| ReadMe | No free tier visible | ~$99/month (est.) | Linter, Agent Owlbert, Ask AI, MCP, Docs Audit [35] | Project-based | Medium (platform) |
| Swimm | Free (limited repos) | $29/user/month (est.) | Code-coupled auto-sync [37] | Per-user | Low (Markdown in git) |
| Grammarly | Free (basic) | $12-25/user/month [39] | Grammar, style, tone | Per-user [39] | None (overlay) |
| Notion AI | No (Business required) | $20/user/month (est.) | Writing, summarization, agents | Per-user | Medium (platform) |

## Platform Analysis

### Mintlify

"Intelligent Knowledge Platform" [33]. Content stored as Markdown/MDX in user's GitHub repository — strongest lock-in mitigation among commercial platforms. Customers include Anthropic (2M+ monthly developers), Coinbase, HubSpot, Perplexity, Notion, PayPal [33]. SOC 2 compliant [33].

AI features: Context-aware Agent that drafts, edits, and maintains content. LLMs.txt & MCP support for AI discoverability [33]. Pro plan includes 250 AI Assistant messages/month with $0.25/message overage [34].

**Solo developer assessment**: Free tier provides full platform access with custom domain and LLM optimizations — genuinely usable for individual projects [34]. The $250/month Pro tier is prohibitive for solo use but the free tier is competitive.

### GitBook

Per-site pricing model [7]. Free tier limited to 1 user per site with gitbook.io subdomain [7]. Custom domains require Premium at $65/site/month [7]. AI Assistant only available at Ultimate tier ($249/site/month) [7].

AI features: GitBook Agent scans Intercom conversations and GitHub Issues to suggest documentation improvements. GitBook Assistant provides MCP-powered Q&A. Built-in llms.txt support [36]. Uses GPT-4o, does not use content for model training [36].

**Solo developer assessment**: Free tier is limiting (1 user, no custom domain). Cost scales per-site, which is problematic for someone maintaining multiple projects. Many open source projects have migrated away [2]. Not recommended for the stated use case.

### ReadMe

AI Linter scores content on a 10-point scale, detecting passive voice, variable integrity, typos, tone consistency, wordiness [35]. Agent Owlbert "edits for clarity, suggests what's missing, and keeps docs aligned with your API" [35]. Ask AI provides "real-time, source-backed answers from your docs" [35]. MCP Server compatible with Claude, OpenAI, Gemini, Copilot, Grok, DeepSeek [35]. Docs Audit enforces consistency across documentation with historical tracking [35].

**Solo developer assessment**: Strongest AI review features but project-based pricing. Designed for API documentation specifically. No visible free tier for the stated use case.

### Swimm

Code-coupled documentation where Smart Tokens auto-update when code changes [37]. Continuous Documentation paradigm — documentation as part of regular development workflow [37]. IDE plugins for VS Code and JetBrains [37]. Documentation stored as Markdown in git repository [37].

**Solo developer assessment**: Interesting concept but solves a different problem (code documentation sync rather than user-facing docs). Pricing has reportedly shifted toward enterprise-only. (Discovery agent noted ambiguity in current pricing model.)

### Grammarly

Audience selection (knowledgeable/expert), domain selection (engineering, CS, medicine) [38]. Limitations: "Incorrect suggestions for discipline-specific or overly technical work" [38]. Technical writers often ignore Variety/Vocabulary suggestions — synonym swapping is inappropriate for technical docs where consistent terminology matters [38].

**Solo developer assessment**: Useful as a general writing overlay but not a documentation platform. Cannot enforce project-specific style guides. False positives for technical content are a documented issue [38]. Better used alongside Vale (which handles technical style rules) rather than as a replacement.

## Solo Developer Recommendation

For a solo developer maintaining multiple open source projects:

1. **Skip commercial AI documentation platforms** — the free tiers are either too limited (GitBook) or the AI features are behind paywalls that don't justify the cost for individual projects
2. **Use Mintlify's free tier** if you need a hosted solution with zero configuration — it provides full platform access, custom domain, and LLM optimizations at $0 [34]
3. **Use Vale + your own LLM** for AI-assisted review — Vale handles automated style enforcement, and tools like Claude can review docs against frameworks like Diátaxis (as demonstrated in the Sequin case study [25])
4. **Grammarly as an overlay** for general prose quality, understanding its technical writing limitations [38]

The most cost-effective "AI documentation review" for a solo developer is: Vale for automated enforcement + LLM prompts for structural review + Diátaxis for organizational assessment. This combination costs $0 and avoids vendor lock-in.

## Gaps and Limitations

- No peer-reviewed studies on AI-generated software documentation quality (clinical documentation research dominates) (from discovery agent)
- Swimm pricing model is ambiguous — may have shifted to enterprise-only
- ReadMe pricing not confirmed from official source
- No independent benchmarks comparing AI documentation quality across platforms
- ROI claims (70% time reduction, 200-400% ROI) from discovery agents lack clear attribution to specific studies
