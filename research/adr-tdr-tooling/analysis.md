# ADR/TDR Tooling: Survey and Agentic Readiness Analysis

## Summary

This analysis surveys the architecture/technical decision record tooling
landscape, evaluating alternatives to the unmaintained adr-tools (npryce) with
emphasis on simplicity and suitability for AI agent consumption. Fifty sources
were consulted across five dimensions: tool landscape, agentic consumption
readiness, simplicity and adoption friction, format ecosystem, and a no-tool
baseline.

The field has evolved significantly since adr-tools' last release in 2018 [9].
Three tools stand out for agentic consumption: **adrs** (Rust) [11], **ADG**
(Go) [10], and the **Structured MADR** format with its reference implementation
[12]. The no-tool approach (plain markdown + git) remains viable for small teams
but lacks the metadata filtering that AI agents benefit from [5].

## Methodology

Five research dimensions were investigated via parallel discovery agents (one
per dimension) plus counter-discovery agents seeking contradicting evidence.
Multi-engine search augmentation (DuckDuckGo) supplemented WebSearch results.
All sources were visited in-session via WebSearch or WebFetch on 2026-07-07.
Full source details in [citations](citations.md). Detailed findings per
dimension in [references/](references/).

## The Landscape in 2026

The adr.github.io community catalogs 36 distinct ADR tools [1], but most are
thin ports of adr-tools' basic functionality into different languages. Eight
tools are actively maintained with releases within the last 12 months. The
field splits into three camps:

1. **CLI tools** — binary or script-based, create/manage markdown files
2. **Format specifications** — define template structure and metadata schemas
3. **Platform integrations** — Backstage plugins, VS Code extensions, web apps

### The Baseline: adr-tools (npryce) [9]

| Metric | Value |
|--------|-------|
| Stars | ~5,600 |
| Last release | v3.0.0 (July 2018) |
| Language | Bash |
| License | GPL |
| Open issues/PRs | 32 / 37 |
| Format | Nygard (5 sections) |

Still functional. Still in Homebrew. The 37 unmerged PRs and Travis CI config
suggest genuine dormancy, not stable-complete. The tool does one thing well
(auto-numbered Nygard ADRs) but lacks YAML frontmatter, MADR support, JSON
export, MCP integration, or any machine-readable output beyond plain markdown.

## Agentic Readiness Comparison

The core question: which tools support AI agent consumption?

### Tier 1: Purpose-Built for Agents

| Tool | MCP Server | YAML Frontmatter | JSON Export | AI Plugin | Format |
|------|-----------|-----------------|-------------|-----------|--------|
| **adrs** [11] | Yes | Yes (NextGen mode) | JSON-ADR | — | Nygard + MADR 4.0 |
| **ADG** [10] | Yes (5 tools) | Yes (YAML metadata) | — | VS Code MCP | Custom + Nygard/MADR |
| **Structured MADR** [12] | Referenced | Required (10 fields) | MIF JSON-LD | Claude Code plugin | Structured MADR |

### Tier 2: Scriptable but Not Agent-Optimized

| Tool | CLI Scriptable | Machine-Readable Output | Notes |
|------|---------------|------------------------|-------|
| @meza/adr-tools [15] | Yes | No (plain markdown) | Full npryce feature parity |
| Log4brains [14] | Partial | Static HTML | Interactive init |
| adr-tool [17] | Yes | No | Git commit integration |
| pyadr [16] | Yes | No | Pre-alpha, incomplete features |
| dotnet-adr [46] | Yes | No | .NET ecosystem |

### Tier 3: No Programmatic Access

| Tool | Notes |
|------|-------|
| adr-tools [9] | Plain bash, no structured output |
| ADR Manager [30] | Web/VS Code GUI, GitHub API connection |

Note: adr.zone [40] is web-based but provides an API for programmatic
generation, placing it between Tier 2 and 3.

### The Goldilocks Finding

Evidence from LLM format research [18] reveals a critical nuance: **strict
format constraints degrade LLM reasoning performance** (Claude-3-Haiku
GSM8K accuracy dropped from 86.99% to 23.44% under JSON schema constraints),
but **lightweight structure aids filtering and routing**.

The optimal architecture for agent consumption is:
- **Structured frontmatter** for metadata queries (which decisions? what
  status? what technologies?)
- **Free-form markdown body** for reasoning content (context, rationale,
  consequences)

Structured MADR [2] and adrs NextGen mode [11] both implement this pattern.
Nygard without frontmatter forces full-text parsing. Tyree-Akerman's 15+
sections add structure without machine-readability.

## Format Decision Matrix

Based on the empirical study [6] and format comparison [4]:

| Context | Recommended Format | Why |
|---------|-------------------|-----|
| Solo developer, quick decisions | Nygard | Lowest friction, 81% preferred in study [6] |
| Small team, moderate decisions | MADR | Structured options without overhead |
| AI-assisted development | Structured MADR | Required YAML frontmatter, JSON Schema validation [2] |
| Cross-repo AI tooling | adrs + JSON-ADR | Export/import with federation [11] |
| Decision summary/register | Y-Statement | Single sentence, fits anywhere [39] |
| Enterprise governance | Tyree-Akerman or Structured MADR | Audit trails, compliance [4] |

## Simplicity Analysis

Setup time to first ADR, ordered by simplicity:

| Rank | Approach | Setup Time | Dependencies |
|------|----------|-----------|--------------|
| 1 | No tool (copy template) | ~1 min | None |
| 2 | adrs (brew/cargo) | ~2 min | None (binary) |
| 3 | adr-tools (brew) | ~2 min | Bash |
| 4 | adr-tool (binary) | ~2 min | None (binary) |
| 5 | ADG (binary download) | ~3 min | None (binary) |
| 6 | @meza/adr-tools (npm) | ~3 min | Node.js |
| 7 | pyadr (pip) | ~3 min | Python |
| 8 | Structured MADR (npm) | ~5 min | Node.js (for validation) |
| 9 | Log4brains (npm) | ~5 min | Node.js |
| 10 | dotnet-adr | ~5 min | .NET SDK |

Binary-distributed tools (adrs, ADG, adr-tool) offer the best simplicity-to-
capability ratio: no runtime dependencies, single file, immediate use.

## Counter-Perspectives

### "You May Not Need a Tool" [8][22][32]
Multiple authoritative sources (Fowler [8], Red Hat [22]) center on plain
markdown in git. In-repo markdown is the most popular approach [50].
"Keep your ADRs stupid simple" [32]. The tooling ecosystem is fragmented [24]
and adding another tool may create net negative value unless it integrates
into existing workflows.

### "ADRs Become Write-Only Graveyards" [44]
A recurring failure mode affecting tooled and no-tool approaches equally.
Measuring ADR volume signals friction, not maturity [44]. The solution is
cultural (clear triggers, review habits), not tooling.

### "Over-Structuring Harms AI Reasoning" [18]
Strict format schemas degrade LLM reasoning performance. JSON key ordering
forces direct answering over chain-of-thought [18]. But lightweight structure
(YAML frontmatter for metadata) aids filtering without constraining reasoning
content.

### "Simplicity Is Context-Dependent" [6][25]
What works for a small team breaks at organizational scale [25]. Decision
volume, concurrent development, cross-repo discovery, and lifecycle management
all push toward tooling.

## Reflection

Before finalizing: the strongest finding is that **no single tool dominates**.
The landscape is fragmented because ADR needs are genuinely diverse — a solo
developer writing occasional decisions has different needs from an enterprise
team with compliance requirements and AI-assisted development.

The agentic readiness dimension revealed a genuine gap: only 2 tools (adrs,
ADG) have MCP servers, and only 1 format (Structured MADR) has a Claude Code
plugin. This is a nascent ecosystem. The Agent Decision Records project [13]
addresses a different problem (capturing AI agent provenance) but its tooling
patterns (JSON Schema validation, pre-commit hooks, slash commands) are
instructive for any agentic ADR workflow.

The counter-evidence on format restrictions [18] is important: the instinct
to add more structure for AI consumption is partially wrong. Structure helps
with *metadata filtering* but hurts *reasoning content*. The tools that get
this right (Structured MADR, adrs NextGen) separate structured frontmatter
from free-form body.

## Decision Framework

For the user's specific context (simple, agentic consumption, replacing
unmaintained adr-tools):

**If you want the simplest agent-ready tool today:**
→ **adrs** (Rust) [11]. Single binary via Homebrew, adr-tools compatible (works
  with existing repos), MCP server, JSON-ADR export, NextGen YAML frontmatter
  mode. 95 stars, actively maintained, MIT/Apache-2.0.

**If you want the richest agentic ecosystem:**
→ **Structured MADR** format [2][12] with the Claude Code plugin. Required YAML
  frontmatter, JSON Schema validation, GitHub Action, conformance levels.
  Newer (2026), smaller community (9 stars), but purpose-built for AI
  integration.

**If you want decision modeling and enforcement:**
→ **ADG** [10]. MCP server, architectural rule DSL, decision models. Academic
  origin, Go binary, Apache 2.0. More complex but provides enforcement that
  other tools lack.

**If you don't actually need a tool:**
→ Plain markdown with a Nygard or MADR minimal template. Copy template, edit,
  commit. Add a tool when concurrency collisions, scale, or agent filtering
  needs justify it.

## Supporting Files

- [citations.md](citations.md) — 50 sources with tier ratings
- [references/tool-landscape.md](references/tool-landscape.md) — Complete tool catalog
- [references/agentic-readiness.md](references/agentic-readiness.md) — MCP, formats, AI integration
- [references/simplicity-friction.md](references/simplicity-friction.md) — Setup complexity, failure modes
- [references/format-ecosystem.md](references/format-ecosystem.md) — Format comparison, empirical data
- [references/no-tool-baseline.md](references/no-tool-baseline.md) — Plain markdown viability
