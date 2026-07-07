# Tool Landscape Survey

Dimension covering what ADR/TDR tools exist today, their maintenance status,
language/runtime, and GitHub activity signals.

Sources: [citations](../citations.md) referenced as [N].

## Tool Catalog

The adr.github.io community maintains a curated catalog of 36 distinct ADR
tools [1]. The landscape divides into three tiers: actively maintained tools
with recent releases, stable-but-dormant tools, and abandoned projects.

### Actively Maintained (release within last 12 months)

| Tool | Language | Stars | Latest Release | Format | Key Differentiator |
|------|----------|-------|----------------|--------|--------------------|
| **adrs** [11] | Rust | 95 | v0.8.0 (Jun 2026) | Nygard + MADR 4.0 | MCP server, JSON-ADR export, NextGen YAML frontmatter, full-text search |
| **ADG** [10] | Go | 35 | v1.1.0 (Jun 2026) | Nygard, MADR, QOC | MCP server (5 tools), decision modeling, rule enforcement DSL |
| **structured-madr** [12] | JS/MDX | 9 | v1.2.0 (Apr 2026) | Structured MADR | Claude Code plugin, GitHub Action validator, MIF conformance |
| **@meza/adr-tools** [15] | TypeScript | 20 | v2.0.1 (Jan 2026) | Nygard | Full npryce reimplementation in npm ecosystem |
| **adr-tool** [17] | Go | 5 | v0.6.0 (Apr 2026) | Custom | Git commit integration, RPM packaging, status tracking |
| **Log4brains** [14] | TypeScript | ~1,500 | v1.1.0 (Dec 2024) | MADR | Static site generation, hot-reload preview, timeline search |
| **dotnet-adr** [46] | C#/.NET | 123 | Active (2025) | MADR | Cross-platform .NET global tool |
| **Talo** [47] | C#/.NET | — | Active | Custom | ADRs + RFCs + custom doc types, export capability |

### Stable/Dormant (functional but minimal recent activity)

| Tool | Language | Stars | Last Release | Notes |
|------|----------|-------|--------------|-------|
| **adr-tools** [9] | Bash | ~5,600 | v3.0.0 (Jul 2018) | The original. 32 open issues, 37 open PRs. Still in Homebrew. |
| **pyadr** [16] | Python | 56 | v0.20.0 (Apr 2023) | Pre-alpha. deprecate/supersede not implemented. |
| **adr-viewer** [42] | Python | — | Dec 2024 workflow | HTML visualization only. Available via pip/Homebrew. |
| **ADR Manager** [30] | Web/VS Code | — | — | Form-based editing via GitHub API. Origin: U Stuttgart research. |

### Web-Based (no install)

| Tool | Format Support | Notes |
|------|---------------|-------|
| **adr.zone** [40] | Nygard, MADR, Y-Statement, ISO 42010 | Browser-based generator with API |
| **ReflectRally** [1] | Multiple | Collaborative workflows, ownership, review processes |

### Language Port Ecosystem

The original adr-tools [9] spawned ports in nearly every language [1]:

| Language | Project | Notes |
|----------|---------|-------|
| Java | adr-j | Port of bash scripts |
| Go | marouni/adr | Port of bash scripts |
| Node.js | phodal/adr | Port of bash scripts |
| PHP | phpadr | Port of bash scripts |
| PowerShell | adr-ps, ArchitectureDecisionRecords | Two independent ports |
| Python | adr-tools-python, ADR-py | Two independent ports |
| C# | GingerTommy/adr-cli | Windows focus |

## Activity Signals

The most active tools by commit velocity and release cadence in 2026:

1. **adrs** (Rust) — 292 commits, 26 releases, steady cadence [11]
2. **@meza/adr-tools** (TS) — 533 commits, 11 releases [15]
3. **structured-madr** — 107 commits, 3 releases, new project [12]
4. **adr-tool** (Go) — 94 commits, 5 releases, published roadmap [17]
5. **ADG** — 7 commits (main), 2 releases, academic origin [10]

## Ecosystem Relationships

- MADR [7] is the de facto standard format, supported by most tools
- Structured MADR [2] extends MADR 4.0 with machine-readable frontmatter
- Agent Decision Records [13] is a separate concept for AI agent provenance
- Backstage ADR plugin enables cross-repo discovery at organizational scale [1]
- ArchUnit provides architecture rule validation in code [1]
- Structurizr integrates ADRs with C4 model visualization [28]

## Gaps and Limitations

- No tool dominates across all dimensions (format, agentic, simplicity)
- MCP server support exists in only 2 tools (ADG [10], adrs [11])
- Claude Code plugin exists for only 1 format (Structured MADR [12])
- Most language ports are thin wrappers reproducing npryce's basic functionality
- Python ecosystem lacks a mature, actively maintained option (pyadr is pre-alpha [16])
