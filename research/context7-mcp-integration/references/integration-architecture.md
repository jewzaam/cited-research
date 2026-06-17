# Integration Architecture: Context7 + Local Knowledge in Claude Code

## Setup Methods

### Remote HTTP (Recommended)

```bash
claude mcp add --transport http context7 https://mcp.context7.com/mcp
```

Add `--scope user` for all projects, or `--scope project` for current repo only [6][7]. With API key for higher rate limits:

```bash
claude mcp add --transport http context7 https://mcp.context7.com/mcp --header "Authorization: Bearer YOUR_KEY"
```

### Local stdio (for offline/restricted networks)

```bash
claude mcp add context7 -- npx -y @upstash/context7-mcp
```

Requires Node.js 18+ [17]. Pre-install globally (`npm install -g @upstash/context7-mcp`) to avoid npx cold-start hangs [15].

### Full Plugin (beyond basic MCP)

```
/plugin marketplace add upstash/context7
/plugin install context7@context7-marketplace
```

Bundles MCP server + skills (auto-trigger) + docs-researcher agent (separate Sonnet context) + /context7:docs command [5].

## Coexistence Architecture

```
┌─────────────────────────────────────────────┐
│  Claude Code Session                        │
│                                             │
│  CLAUDE.md (auto-loaded)                    │
│  ├── References ~/source/standards/         │
│  ├── References ~/source/knowledgebase/     │
│  └── References ~/source/gws-cli-notes/     │
│                                             │
│  MCP Servers:                               │
│  ├── context7 (remote HTTP)                 │
│  │   ├── resolve-library-id                 │
│  │   └── query-docs                         │
│  └── [other MCP servers...]                 │
│                                             │
│  Tool Routing:                              │
│  ├── Library API questions → context7 tools │
│  ├── Convention questions → Read local repo │
│  └── Tool descriptions drive selection [6]  │
└─────────────────────────────────────────────┘
```

CLAUDE.md and MCP servers are separate, complementary systems [6]. CLAUDE.md provides persistent project context loaded at session start. Context7 MCP provides on-demand library documentation retrieval [5].

## Scope Configuration

| Scope | Location | Visibility | Use For |
|-------|----------|-----------|---------|
| Local (default) | `~/.claude.json` under project path | Private | Testing before recommending to team [15] |
| Project | `.mcp.json` at repo root | Version controlled | Team-standard tooling [15] |
| User | `~/.claude.json` globally | All projects | Personal utilities everywhere [15] |

Precedence: local > project > user [6].

For Context7, **user scope** is most appropriate since library documentation is useful across all projects [7].

## Tool Search (Critical for Multi-Server)

Tool Search activates automatically when MCP tools exceed 10% of context [6][15]:

| Metric | Without Tool Search | With Tool Search |
|--------|-------------------|-----------------|
| Token overhead | ~72,000 tokens | ~8,700 tokens [15] |
| Reduction | — | 85% [15] |
| Tool selection accuracy (Opus 4) | 49% | 74% [15] |

Requires Sonnet 4+ or Opus 4+ — not available with Haiku [15]. Configured via `ENABLE_TOOL_SEARCH=auto` (default) [6].

**With Tool Search enabled, adding Context7 as one more server has minimal context overhead** — tool definitions load on-demand rather than upfront [6][15].

## Known Integration Issues

1. **Tool name conflicts**: Context7 can cause "Tool names must be unique" errors when running multiple Task agents [28]. Claude Code disambiguates by prefixing server names (e.g., `mcp__context7__resolve_library_id`) [6].
2. **Token overhead without Tool Search**: A typical four-server setup adds ~7,000 tokens per message [10]. With 50+ tools: 50,000–100,000 tokens consumed before any work begins [15].
3. **LLM confusion with too many tools**: Models struggle with 10–20+ tools — confuse similar tools, ignore descriptions, hallucinate tool names [9].
4. **Network dependency**: Context7 remote endpoint requires internet access. If unreachable, Claude Code falls back to other available tools but does not explicitly error [6].
5. **Restart required**: Configuration changes do not take effect until Claude Code restarts [15].

## Verification

After adding Context7:

```bash
claude mcp list          # Confirm context7 appears
claude mcp get context7  # Show configuration and available tools
```

Within a session, `/mcp` shows connection status for all servers [6].

## Recommended Configuration for This Setup

Given the developer's existing CLAUDE.md-based local repos and need for minimal overhead:

1. Add Context7 at user scope with API key for rate limit headroom
2. Keep Tool Search on `auto` (default) — it handles the overhead problem [15]
3. Do NOT add auto-invoke rules in CLAUDE.md — let the skill's built-in triggers handle it, or invoke manually with "use context7" [5][7]
4. Use docs-researcher agent for context-lean lookups during deep tasks [5]

## Gaps and Limitations

1. No official documentation on how Claude Code prioritizes between CLAUDE.md-referenced files and MCP tool results when both could answer a question.
2. Tool Search behavior at the individual tool level (vs server level) not fully documented [6].
3. Offline fallback behavior when Context7 endpoint is unreachable is not explicitly documented.
