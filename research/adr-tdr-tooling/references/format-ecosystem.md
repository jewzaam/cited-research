# Format and Template Ecosystem

Dimension covering ADR format families, their structure, parseability,
human-friendliness, and template customization support.

Sources: [citations](../citations.md) referenced as [N].

## Format Families

### Nygard (2011)

The original ADR format, credited to Michael Nygard [8]. Five sections:

1. **Title** — short, descriptive
2. **Status** — proposed, accepted, deprecated, superseded
3. **Context** — forces, concerns, constraints
4. **Decision** — what was decided
5. **Consequences** — what follows from the decision

Characteristics [4][6]:
- Machine-readability: Limited (section headers only, no frontmatter)
- Human-friendliness: Extremely high — "can be written in minutes" [4]
- Overhead: Minimal
- Best for: Quick decisions, small teams, agile environments

In the empirical study (n=33), Nygard outperformed MADR with 81% probability
of superiority (Wilcoxon W=84.0, p=0.002, Cliff's Delta=0.6364) [6].
Participants valued its conciseness and low cognitive overhead.

### Y-Statement (2013)

Single-sentence format by Olaf Zimmermann [39]:

> "In the context of **[situation]**, facing **[concern]**, we decided
> **[option]** to achieve **[quality]**, accepting **[downside]**."

Characteristics [4]:
- Machine-readability: Limited (no field delimiters)
- Human-friendliness: Very high (extreme brevity)
- Overhead: Lowest of all formats
- Best for: Decision registers, summary documents, "dozens of small
  decisions" [4]
- Limitation: "No room for detailed analysis" [4]

### MADR (2018, current: v4.0.0)

Markdown Architectural Decision Records [7][20][23]. Ten sections extending
Nygard with structured option analysis:

1. YAML Front Matter (optional: status, date, decision-makers, consulted, informed)
2. Title
3. Context and Problem Statement
4. Decision Drivers (optional)
5. Considered Options
6. Decision Outcome (with Consequences and Confirmation subsections)
7. Pros and Cons of Options (optional)
8. More Information (optional)

Template variants [7]: Full (annotated), Minimal, Bare
File naming: `NNNN-title-with-dashes.md` in `docs/decisions/`
License: MIT OR CC0-1.0

Characteristics [4][6]:
- Machine-readability: Partial (optional YAML frontmatter added in v3.x)
- Human-friendliness: High ("good balance of structure and simplicity" [4])
- Overhead: Moderate
- Best for: Teams wanting structured option analysis without compliance tracking

### Structured MADR (2026, v1.0.0)

Superset of MADR 4.0 adding machine-readable YAML frontmatter, risk assessment,
and required audit sections [2][3].

13 required components [2]:
YAML Frontmatter → Title → Status → Context → Decision Drivers → Considered
Options → Decision → Consequences → Decision Outcome → Related Decisions →
Links → More Information → Audit Section

10 required frontmatter fields [3]: title, description, type, category, tags,
status, created, updated, author, project

3 optional frontmatter fields [3]: technologies, audience, related

Characteristics [4]:
- Machine-readability: Full (JSON Schema validation, GitHub Action [12])
- Human-friendliness: Moderate (requires YAML knowledge)
- Overhead: Moderate-to-high (audit section adds maintenance)
- Best for: "Compliance-driven projects, AI-assisted development, large
  codebases, and long-lived projects" [4]

### Tyree-Akerman (2005)

15+ sections including assumptions, constraints, implications, related
decisions, notes [4][6]. Most comprehensive but heaviest.

Characteristics [4]:
- Machine-readability: Limited (no frontmatter despite thoroughness)
- Human-friendliness: Low — "can feel bureaucratic for smaller decisions" [4]
- Overhead: Highest
- Best for: "Large enterprise environments with formal governance processes" [4]

## Format Comparison Matrix

From [4]:

| Aspect | Structured MADR | MADR | Nygard | Y-Statement | Tyree-Akerman |
|--------|----------------|------|--------|-------------|---------------|
| Sections | 12+ | 10 | 5 | 1 | 15+ |
| Frontmatter | Required YAML | None (optional in 4.0) | None | None | None |
| Options Detail | Narrative + Risk | Pros/Cons | Implicit | Single | Detailed |
| Consequences | Pos/Neg/Neutral | Single list | Prose | Implicit | Impact analysis |
| Audit Trail | Required | None | None | None | None |
| Machine-Readable | Full | Limited | Limited | Limited | Limited |

## Empirical Findings

The controlled experiment [6] found:

- Expert Feature Analysis (step 1) ranked MADR highest (0.900) over Nygard
  (0.868), but the controlled experiment (step 2) reversed this
- **Structural comprehension scores were identical** between MADR and Nygard —
  format differences matter less than assumed for basic knowledge capture
- Template suitability depends on three contextual factors:
  1. Structural granularity needs (completeness vs speed)
  2. Temporal constraints (short cycles → Nygard)
  3. Project scale (large/high-stakes → MADR)
- Limitation: Student participants (proxy for junior developers)

## Template Customization

| Tool | Custom Templates | Mechanism |
|------|-----------------|-----------|
| adrs [11] | Yes | `--format`/`--variant` flags, Jinja2 templating |
| ADG [10] | Yes | Configurable section headers with anchor tags |
| Log4brains [14] | Yes | MADR default, customizable |
| adr-tools [9] | Limited | Template file replacement |
| MADR [7] | Encouraged | "Free to revise the MADR template" but "stick to what you have decided for" [7] |
| Structured MADR [2] | Limited | Must preserve required components |

## Counter-Perspectives

### Format Matters Less Than Assumed [6][31][32]
Empirical study showed identical structural comprehension between MADR and
Nygard [6]. "The act of writing the ADR is often more valuable than the ADR
itself" [31]. "Keep your ADRs stupid simple" — five essential elements
sufficient [32].

### Template Rigidity Creates Anti-Patterns [20][21]
Over-standardized templates encourage Mega-ADRs, Blueprint in Disguise,
Novel/Epic patterns [20][21]. Rigid templates squeeze entire architecture
documents into single ADRs.

### MADR Internal Inconsistencies [34]
Options section uses flat list with Good/Bad prefixes while Outcome uses
subsections, preventing copy-paste workflow [34].

### Format Doesn't Solve Adoption [29][32]
Real problem is cultural (getting team buy-in), not structural (picking
optimal template). Elaborate templates create barriers: "Documentation is
boring and nobody likes to do it" [32].

## Migration Paths

- Nygard → MADR: Add structured option analysis sections
- MADR → Structured MADR: Add required YAML frontmatter + audit section [2]
- Any → Y-Statement: Compress to single sentence (information loss)
- adrs tool supports both Nygard and MADR 4.0 via `--format` flag [11]

## Gaps and Limitations

- No format converter tool exists between MADR, Nygard, and Y-Statement
- Structured MADR adoption data unavailable — format is new (2026)
- Y-Statement's single-sentence format is unparseable by simple regex
- No empirical study comparing AI agent performance across ADR formats
- MADR's YAML frontmatter parsing is "not standardized" across Markdown parsers [7]
