# C4 Architecture Model: Application to Small and Large Projects

Citation-backed analysis of the C4 model and how to apply it at different project scales — from single-purpose apps to distributed multi-repo platforms.

## TL;DR

The C4 model provides four zoom levels for architecture visualization (Context → Container → Component → Code). **Levels 1 and 2 deliver the majority of value regardless of project scale.** The difference between small and large projects isn't which levels you use — it's how you manage the model.

## Key Decision Table

| Project Scale | What to Use | Tooling | Key Concern |
|--------------|-------------|---------|-------------|
| **Small** (1-5 containers, 1 repo) | Context + Container diagrams only | draw.io, Mermaid, or C4-PlantUML | Don't over-engineer |
| **Monorepo** (many modules, 1 repo) | Context + Container + selective Component; DSL alongside code | Structurizr DSL or C4-PlantUML | Map containers to deployable units, not code structure |
| **Fragmented platform** (multi-repo, multi-team) | System Landscape + per-system Context/Container; workspace composition | Structurizr with workspace extension | Avoid uber-workspace anti-pattern; compose, don't consolidate |

## Quick Decision Framework

1. **How many deployable things?** 1 → Context only. 2-5 → Context + Container. 6+ → Model-driven with focused views.
2. **How many teams?** 1 → One system. 2+ → Consider separate systems per team domain.
3. **How many repos?** 1 → DSL with code. Multiple → Workspace extension pattern.
4. **Need behavior diagrams?** Use dynamic diagrams sparingly or supplement with UML.

## What C4 Does NOT Cover

Runtime behavior, data flows, business processes, quality requirements, risks, decision rationale. Supplement with arc42 (documentation template), UML (behavior), ADRs (decisions).

## Files

| File | Contents |
|------|----------|
| [c4-architecture-analysis.md](c4-architecture-analysis.md) | Full analysis with methodology |
| [citations.md](citations.md) | All 30 sources with URLs and extracted data |
| [references/c4-fundamentals.md](references/c4-fundamentals.md) | Four levels, principles, history, notation |
| [references/small-project-application.md](references/small-project-application.md) | When C4 helps vs. is overkill for small projects |
| [references/large-project-monorepo.md](references/large-project-monorepo.md) | Module mapping, team ownership, auto-generation |
| [references/large-project-fragmented-platform.md](references/large-project-fragmented-platform.md) | Multi-repo patterns, workspace composition, scale limits |
| [references/tooling-ecosystem.md](references/tooling-ecosystem.md) | 9 tools compared across 3 categories |
| [references/diagrams-as-code.md](references/diagrams-as-code.md) | DSL workflows, CI/CD, auto-generation, keeping diagrams alive |
| [references/criticisms-and-limitations.md](references/criticisms-and-limitations.md) | Pitfalls, alternatives (arc42, 4+1, ArchiMate), when to use what |
| [audit/citation-audit.md](audit/citation-audit.md) | Independent citation verification |
| [audit/consistency-review.md](audit/consistency-review.md) | Cross-file consistency check |
