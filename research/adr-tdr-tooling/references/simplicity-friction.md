# Simplicity and Adoption Friction

Dimension covering setup complexity, dependencies, and minimal viable workflow
for ADR/TDR tools.

Sources: [citations](../citations.md) referenced as [N].

## Setup Complexity by Tool

| Tool | Install Command | Runtime | Dependencies | Time to First ADR |
|------|----------------|---------|--------------|-------------------|
| adr-tools [9] | `brew install adr-tools` | Bash | None (shell scripts) | ~2 min |
| adrs [11] | `brew install joshrotenberg/brew/adrs` or `cargo install adrs` | None (binary) | None | ~2 min |
| ADG [10] | Download binary or `go install` | None (binary) | None | ~3 min |
| adr-tool [17] | Download binary | None (binary) | None | ~2 min |
| @meza/adr-tools [15] | `npm install --save-dev @meza/adr-tools` | Node.js | npm packages | ~3 min |
| Log4brains [14] | `npm install -g log4brains` | Node.js | npm packages | ~5 min (interactive init) |
| pyadr [16] | `pip install pyadr` | Python | pip packages | ~3 min |
| dotnet-adr [46] | `dotnet tool install -g adr` | .NET SDK | .NET runtime | ~5 min (template setup) |
| Structured MADR [12] | `npm install` (for validation) | Node.js | npm packages | ~5 min |
| No tool | Copy template file | None | None | ~1 min |

## Dependency Weight

| Tool | Install Footprint | Notes |
|------|------------------|-------|
| adr-tools [9] | Minimal (bash scripts) | Requires only bash + basic Unix utils |
| adrs [11] | Single binary (~10 MB) | Also available via Docker |
| ADG [10] | Single binary | Go cross-compiled |
| adr-tool [17] | Single binary | Go cross-compiled, RPM available |
| @meza/adr-tools [15] | npm package tree | Moderate dependency count |
| Log4brains [14] | Heavy npm tree | Next.js under the hood |
| pyadr [16] | pip packages | Uses Poetry |
| dotnet-adr [46] | .NET SDK required | Heavyweight if .NET not already present |

## Minimal Viable Workflow

The simplest path to a working ADR setup:

**With a binary tool (adrs, ADG, adr-tool):**
```
<tool> init          # creates directory + first ADR
<tool> new "Title"   # auto-numbered, opens in editor
git add && commit    # tracked in version control
```

**Without any tool:**
```
mkdir -p docs/decisions
cp template.md docs/decisions/0001-first-decision.md
# edit in any editor
git add && commit
```

## Adoption Failure Modes

Three primary friction points cause ADR rollout failure [29]:

1. **Too much ceremony** — heavyweight templates requiring 15+ fields
   discourage writing. ADRs should take 10-20 minutes to write [48].

2. **No clear trigger points** — teams don't know when to write an ADR.
   Without triggers, the practice fades.

3. **Tooling friction** — manual folder creation, file naming, number
   tracking, and template copying. Tools that automate these basics
   reduce the "activation energy" for writing.

Martin Fowler reinforces brevity: "Keep the ADR short and to the point —
typically a single page" [8]. The inverted pyramid writing style front-loads
the decision.

## Counter-Perspectives: When Simple Isn't Enough

### Scale Changes Requirements
Simple tools work for small teams but break at organizational scale [25]:
- Decision volume exceeds browsability
- Multiple teams need coordination
- Decision chains and superseding relationships become complex
- Cross-repo discovery requires dedicated infrastructure (Backstage plugin [1])

Organizations that consolidated fragmented tooling saw 30% deployment time
reduction [25].

### Lifecycle Complexity Is Real
AWS documents ADR lifecycle states: Draft/Proposed, Accepted, Active,
Superseded, Deprecated [45]. Managing these transitions manually is
error-prone. Tools with state machine workflows (pyadr [16], ADG [10])
enforce valid transitions.

### Concurrency Breaks Manual Numbering
When multiple developers create ADRs simultaneously in separate PRs, manual
numbering produces duplicates [33]. Auto-numbering tools prevent this.

### Visualization Needs
Minimal tools lack decision chain visualization. Structurizr provides
force-directed graphs showing ADR relationships [28] — impossible with
text-only tools.

## Gaps and Limitations

- No tool provides complexity-proportional templating (auto-adjusting
  template weight based on decision significance)
- Log4brains' `help` command takes 12+ seconds — heavyweight for simple
  operations (unverified, from discovery agent)
- No standardized ADR trigger framework exists across tools
- RPM/deb packaging available only for adr-tool [17] — most tools
  require language-specific package managers
