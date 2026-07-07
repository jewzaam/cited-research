# ADR/TDR Tooling: Alternatives to adr-tools for Agentic Consumption

> Last revised: 2026-07-07

Survey of architecture decision record tooling beyond the unmaintained
adr-tools (npryce, last release 2018). Emphasis on simplicity and AI agent
consumption readiness. 50 sources consulted, 36 tools cataloged, 5 ADR format
families compared.

## Key Finding

Three tools stand out for agentic consumption. All are actively maintained,
simple to set up, and produce machine-readable output:

| Tool | Language | Install | MCP Server | YAML Frontmatter | Best For |
|------|----------|---------|-----------|-----------------|----------|
| **[adrs](https://github.com/joshrotenberg/adrs)** | Rust | `brew install` | Yes | Yes (NextGen) | Drop-in adr-tools replacement with agent features |
| **[ADG](https://github.com/adr/ad-guidance-tool)** | Go | Binary download | Yes (5 tools) | Yes | Decision modeling + rule enforcement |
| **[Structured MADR](https://smadr.dev/)** | JS/MDX | npm | Referenced | Required (10 fields) | Claude Code plugin, JSON Schema validation |

## Quick Decision Guide

1. **Want simplest path from adr-tools?** → `adrs` (Rust). Compatible with
   existing repos, single binary, MCP server, JSON export.
2. **Want Claude Code integration?** → Structured MADR format + its plugin.
   Required YAML frontmatter, GitHub Action validator.
3. **Want enforcement rules?** → ADG. DSL for architectural rules, decision
   models, MCP server.
4. **Don't actually need a tool?** → Plain markdown + Nygard template. Add
   tooling when concurrency, scale, or agent filtering justify it.

## The Agentic Goldilocks Zone

Research shows strict format schemas degrade LLM reasoning (Claude-3-Haiku
accuracy dropped 63.5 percentage points under JSON schema constraints). But
lightweight YAML frontmatter aids filtering without constraining reasoning.

**Optimal pattern:** Structured YAML frontmatter (metadata for filtering) +
free-form markdown body (reasoning content). Both `adrs --ng` and Structured
MADR implement this.

## Full Analysis

- [analysis.md](analysis.md) — Complete comparison with methodology
- [citations.md](citations.md) — 50 sources with quality tiers
- [references/](references/) — Detailed findings per dimension
- [audit/](audit/) — Independent verification reports
