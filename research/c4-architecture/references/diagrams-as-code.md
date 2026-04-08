# Diagrams-as-Code and Living Documentation

Dimension covering how to keep C4 diagrams in sync with code, CI/CD integration, and auto-generation approaches.

See [citations.md](../citations.md) for full source details.

## Core Concept

Diagrams-as-code uses domain-specific languages (DSLs) to define architecture diagrams in plain text. This enables version control, branching, merging, and CI/CD integration for architecture documentation — the same workflows developers use for code.

Simon Brown explicitly advocates this approach, recommending teams "adopt model + views tooling that generates multiple consistent diagrams from a single source of truth" [11].

## Structurizr DSL

The primary DSL for C4 diagrams. Defines a workspace containing a model (elements and relationships) and views (rendered as diagrams) [16].

**Key capabilities:**
- All C4 diagram types supported [16]
- Built-in ADR (Architecture Decision Records) [16]
- Markdown/AsciiDoc documentation alongside diagrams [16]
- Export to PlantUML and Mermaid [16]
- Workspace extension for multi-team use [18]
- DRY principle: define once, use in multiple views
- `include` expressions for generating focused subset diagrams from a unified model [11]

**Example workflow:**
1. Define full model in `.dsl` file
2. Define multiple views highlighting different aspects
3. Tooling renders views as diagrams
4. Store `.dsl` in version control alongside code

## Diagramming vs. Modeling

This distinction is critical for living documentation [8]:

| Aspect | Diagramming | Modeling |
|--------|------------|---------|
| Approach | Draw boxes and lines | Define elements and relationships |
| Reuse | Copy-paste | Automatic (element defined once) |
| Validation | None | Tool validates model consistency |
| Querying | Impossible | "A model is just data" [8] |
| Multi-view | Separate diagrams, manually synced | Multiple views from single model |
| Rename | Find and fix across diagrams | Change once, propagates |

The key insight: modeling tools maintain a single model that generates multiple diagram views. When something changes, you update the model and all views update automatically.

## CI/CD Integration

### Structurizr CLI

Supports Docker, GitHub Actions, and GitLab CI integration [16]:
- Docker image: `structurizr/cli:latest`
- Export to PlantUML/Mermaid/WebSequenceDiagrams
- Validate workspace definitions in pipeline

### Integration Patterns

1. **Auto-render on commit:** Generate PNG/SVG/PDF from DSL files and publish to wiki or documentation site
2. **Validation gate:** Fail builds if C4 model has errors (broken references, missing elements)
3. **Diff-friendly:** Text-based DSL produces meaningful diffs in pull requests
4. **Documentation site generation:** Combine rendered diagrams with Markdown docs from Structurizr workspace

### ADEO Tech's Approach

Uses DOT + Graphviz for auto-generation [28]:
- Each team maintains `.dot` files in their repository
- Changes are "only a few lines of changes" [28]
- "You can see changes to diagrams in your git diff" [28]
- Aggregation via API endpoints and custom UI across all teams

## Auto-Generation from Code

Tools that extract C4 models from source code:

### go-structurizr (Go)

Three components [25]:
1. **Scraper:** Crawls Go structures via regex package rules
2. **View:** Renders to PlantUML with tag-based styling
3. **Integration:** Instantiate → init app → scrape → render → convert to PNG

Benefits: "diagrams reflect current code structure," eliminates manual maintenance, CI regeneration on code changes [25].

### C4InterFlow (.NET/C#)

Architecture-as-code framework listed as official C4 modeling tool [8]. Generates C4 diagrams from YAML/JSON models or directly from C# codebases.

### Limitations of Auto-Generation

- Language-specific, not language-agnostic [25]
- Can generate Component/Code levels, but Context and Container levels require human judgment about system boundaries and external dependencies
- Risk of generating too much detail — not every code structure needs to appear in architecture diagrams
- "Don't duplicate information that tools can generate automatically" [24]

## Architecture Decision Records (ADRs)

Structurizr DSL has built-in ADR support [16], linking architectural decisions to the model. This addresses a gap in C4 alone: "architecture diagrams show the outcomes of decisions, not the decision-making process" [12].

The recommended approach: document reasoning in ADRs, reference the affected C4 elements. This keeps diagrams clean while preserving decision context.

## Keeping Diagrams Alive

The fundamental challenge: "architecture diagrams frequently become outdated because applications change constantly" [25]. Strategies:

1. **Auto-generate from code** where possible (Component/Code levels) [25]
2. **Store DSL with code** so architecture changes happen in the same PR [28]
3. **Use modeling tools** so element reuse prevents copy-paste drift [8]
4. **Link rather than duplicate** — reference OpenAPI specs, schema docs instead of repeating their content [24]
5. **Review diagrams in PR workflow** — if the DSL is in the repo, architecture changes get peer reviewed

## Version Control Benefits

Text-based DSL formats enable [28]:
- Standard git workflows (branch, merge, PR)
- Meaningful diffs showing what changed
- Date stamps for freshness: "you can check immediately upon looking at the date of the graph how old the documentation is" [28]
- History tracking of architectural evolution

## Gaps and Limitations

- Auto-generation works for lower levels but Context and Container diagrams still need human authoring
- No standard for when auto-generated diagrams should override manually authored ones
- CI/CD integration requires tooling investment (Docker images, pipeline configuration)
- No published data on how much auto-generation reduces maintenance burden
- Structurizr CLI sunset in early 2026 creates uncertainty for CI pipelines depending on it
