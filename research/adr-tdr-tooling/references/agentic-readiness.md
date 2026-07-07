# Agentic Consumption Readiness

Dimension covering how well ADR/TDR tools support consumption by AI/LLM
agents. Machine-parseable formats, CLI scriptability, MCP integration, and
programmatic access.

Sources: [citations](../citations.md) referenced as [N].

## Machine-Readable Formats

### Format Spectrum

| Format | Machine-Readability | Frontmatter | Validation | AI-Optimized |
|--------|-------------------|-------------|------------|--------------|
| Nygard | Limited — section headers only | None | None | No |
| Y-Statement | Limited — single sentence, no delimiters | None | None | No |
| MADR 4.0 | Partial — optional YAML frontmatter | Optional (status, date, decision-makers) | markdownlint | No |
| Structured MADR | Full — required YAML frontmatter | Required (10 fields) | JSON Schema + GitHub Action | Yes [2][5] |
| JSON-ADR | Full — JSON interchange format | N/A (pure JSON) | Schema-based | Designed for tooling [11] |

### Structured MADR — The Agentic-First Format

Structured MADR [2][3] is purpose-built for AI consumption with four design
goals: backward compatibility with MADR, forward compatibility via extensible
schema, tool interoperability via standard YAML/Markdown, and "AI Optimization —
metadata designed for LLM context injection" [2].

Required YAML frontmatter fields [3]:

| Field | Purpose for AI Agents |
|-------|----------------------|
| `tags`, `category` | Filter relevant decisions |
| `technologies` | Surface by tech stack |
| `status` | Route agent behavior (proposed → suggest, accepted → follow, deprecated → warn) [5] |
| `related` | Navigate decision chains |
| `created`, `updated` | Assess freshness |
| `project` | Scope context |

### JSON-ADR Interchange Format

The adrs Rust tool [11] provides JSON-ADR export/import: `adrs export json >
decisions.json`. Described as "handy for feeding a decision log to other tools
or to an AI agent that reasons over it." Supports bulk and single-ADR export
with federation (cross-repo import with renumbering).

## MCP Server Implementations

Two tools provide built-in MCP servers:

### ADG [10]
- Transport: stdio
- Setup: `adg mcp run --model <path>`
- VS Code integration via `.vscode/mcp.json`
- 5 exposed tools:

| Tool | Purpose |
|------|---------|
| `list_adrs` | List all decisions with ID, title, status |
| `get_adr` | Retrieve full ADR content |
| `get_dsl_reference` | Return rule DSL language reference |
| `list_rule_files` | List existing rule files |
| `validate_rule` | Validate rule syntax/semantics |

### adrs (Rust) [11]
- MCP server for AI agent integration (documented in README)
- Details on exposed tools not fully extracted

## CLI Scriptability

All CLI tools are non-interactive when invoked with arguments, making them
agent-scriptable:

| Tool | Non-Interactive | Exit Codes | stdout-Friendly |
|------|----------------|------------|-----------------|
| adr-tools [9] | Yes (title as args) | Basic | Yes |
| ADG [10] | Yes (all flags) | Yes | Yes |
| adrs [11] | Yes | Yes | JSON export |
| @meza/adr-tools [15] | Yes | Yes | Yes |
| adr-tool [17] | Yes | Yes | Yes |
| log4brains [14] | Partial (init is interactive) | Yes | Build output |

## AI Integration Patterns

### Claude Code Plugin (Structured MADR) [12]
- Commands: `/mif-validate`, `/mif-project`
- Agent: `adr-mif-author` for authoring ADRs
- Skill: `mif-compliance` for validation
- Hook: Authoring-time enforcement
- Claude Code reads YAML frontmatter to filter, understand relationships,
  and surface relevant decisions [5]

### Agent Decision Records (AgDR) [13]
Separate concept from traditional ADRs. Captures AI agent decisions in
real-time with required metadata:
- `agent` — which agent (claude-code, codex, copilot, cursor)
- `model` — specific model (e.g., claude-opus-4-5)
- `trigger` — what initiated (user-prompt, hook, automation)
- `timestamp` — ISO-8601 with time
- Tooling: Claude Code `/decide` command, Codex skill, Cursor rules,
  Copilot instructions, Windsurf rules, pre-commit hooks [13]

### AI-Generated ADRs
Multiple teams use LLMs to draft ADRs using MADR templates [26][27].
Metaprompting with structured headings and explicit constraints produces
consistent output [27].

## Counter-Perspectives on Agentic Readiness

### Over-Structuring Harms LLM Reasoning [18]
Empirical research shows format restrictions significantly degrade LLM
reasoning. On GSM8K math reasoning, JSON schema constraints dropped
Claude-3-Haiku accuracy from 86.99% to 23.44% [18]. Key ordering forces direct
answering over chain-of-thought reasoning.

**Implication:** Strict YAML frontmatter schemas are beneficial for *metadata
filtering* (which decisions apply?) but should not constrain the *body content*
where reasoning is documented. Structured MADR gets this right — frontmatter is
structured, body is free-form Markdown [2].

### Plain Text Outperforms Complex Systems [36]
AGENTS.md files outperform vector databases and RAG systems for AI agent memory
(74% vs 68.5% benchmark) [36]. Instruction ceiling of ~150-200 instructions
limits what structured metadata can achieve.

### Simple Per-Record Labeling Beats Traditional Formats [37]
Markdown-KV format achieved 60.7% accuracy vs CSV at 44.3% for LLM
consumption [37]. The optimal format is lightweight structure (markdown
headings, key-value pairs), not complex schemas.

**Synthesis:** The evidence suggests a Goldilocks zone — lightweight structured
frontmatter for filtering/routing plus free-form markdown body for reasoning
content. Both fully unstructured (Nygard without frontmatter) and heavily
structured (Tyree-Akerman, strict JSON schemas) are suboptimal for AI agents.

## Gaps and Limitations

- MCP server support in only 2 tools (ADG, adrs) — nascent ecosystem
- No empirical validation of Structured MADR's AI optimization claims
- Agent Decision Records are a GitHub repo standard, not a tool — adoption unknown
- No tool implements bidirectional AI integration (agent both reads and proposes ADRs programmatically via MCP)
- JSON-ADR format lacks independent specification — defined only in adrs-core library
