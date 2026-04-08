# Small Project Application

Dimension covering how C4 applies to self-contained, single-purpose applications and when it becomes overhead.

See [citations.md](../citations.md) for full source details.

## What Counts as "Small"

For this analysis, a small project is a self-contained, single-purpose application — typically a monolith or simple client-server setup with fewer than five containers. Examples: a CLI tool with a database, a web app with an API backend, a single-purpose microservice.

## Which Levels Matter

The consistent guidance from both the C4 creator and practitioners is that **Levels 1 and 2 are sufficient for most teams** [2][24]:

| Level | Value for Small Projects | Recommendation |
|-------|------------------------|----------------|
| 1 — System Context | High — shows external interactions | Always use |
| 2 — Container | High — shows technical building blocks | Always use |
| 3 — Component | Low — info exists in code | Skip unless complex internals |
| 4 — Code | Very low — IDEs generate this | Skip |

"Level 1 (System Context) and Level 2 (Container) are where most of the value lies" [24]. Levels 3 and 4 "require substantial maintenance effort while their information often exists elsewhere in code repositories and documentation" [24].

Simon Brown himself suggests Level 3 and 4 are rarely necessary [13]. ADEO Tech, managing ~10 feature teams, uses only Levels 1 and 2: "simpler and already covers all our needs" [28].

## When C4 Is Valuable for Small Projects

C4 provides value even for small projects in these scenarios:

1. **Onboarding** — serves as "one source of truth for onboarding new staff" [28]
2. **Cross-team communication** — makes architecture "accessible for many different stakeholders" [28]
3. **Security review** — helps "identify security risks and attack areas easily" [28]
4. **External dependency mapping** — a system context diagram shows what talks to what [24]
5. **Growth anticipation** — if the project may grow, starting with C4 establishes a framework that scales

A system context diagram takes minutes to create and immediately shows external dependencies. A container diagram clarifies the boundary between front-end, back-end, and data stores.

## When C4 Is Overkill

C4 adds overhead without proportional value when:

- The system is trivially simple (single container, no external dependencies beyond a database)
- The team is very small (1-2 people) with full shared context
- The project is temporary or experimental
- The system doesn't fit C4's hierarchical model (e.g., hardware-intensive systems) [2]

"For simpler systems, the layered abstraction may prove excessive" [2]. The model is designed for "custom-built, bespoke software systems" and suits less well for embedded systems/firmware [2].

## Practical Approach for Small Projects

Based on practitioner guidance [24]:

1. **Start with a landscape diagram** if struggling with context boundaries — "small-to-medium architectures can use this as their primary diagram" [24]
2. **Use Level 1 + Level 2 only** — skip Component and Code levels
3. **Skip explicit user modeling** when obvious — it "just adds clutter without adding clarity" [24]
4. **Merge deployment into Level 2** — "including deployment context directly in the same diagram often adds more value than splitting it out" [24]
5. **Number relationships for sequences** instead of creating separate dynamic diagrams [24]
6. **Link to existing docs** (READMEs, ADRs, OpenAPI specs) rather than duplicating information [24]

## Tooling for Small Projects

For small projects, lightweight tooling is appropriate:

| Tool | Fit for Small Projects | Why |
|------|----------------------|-----|
| draw.io | Excellent | Free, built-in C4 shapes, no learning curve [26] |
| Mermaid | Good | Embeds in markdown/GitHub, lightweight [19] |
| C4-PlantUML | Good | Code-based, version controllable [27] |
| Structurizr DSL | Moderate | More powerful but requires technical proficiency [20] |

For design sessions, "you might find a whiteboard or flip chart paper better for collaboration, and iterating quickly" [8].

## Lightweight Alternatives

When C4 feels too formal for a small project:

- **Concrete diagramming models** — bottom-up, fact-based, no fixed abstraction levels [29]
- **Ad-hoc boxes and lines** — with C4-inspired labeling (type, technology, description) for structure
- **arc42 template** — for projects needing documentation beyond just diagrams (quality requirements, risks, decisions) [14]

"Both concrete models and C4 models have their place" [29]. The key insight from concrete models: "A database instance is a database instance; debating whether it is also a Container or a Component just isn't worthwhile" [29].

## Decision Framework

```
Is the project custom-built software? → No → C4 likely unsuitable [2]
                                       → Yes ↓
Does it have >1 container?            → No → Context diagram only, skip the rest
                                       → Yes ↓
Will anyone beyond you need to understand it? → No → Informal sketch sufficient
                                               → Yes ↓
Use C4 Levels 1 + 2. Add Level 3 only if internals are genuinely complex.
```

## Gaps and Limitations

- No published case studies specifically measuring C4 overhead for small projects
- No quantitative threshold for when C4 becomes valuable (e.g., container count, team size)
- The "minutes to confidence" learning curve claim [21] is plausible but not formally validated
- Limited guidance on transitioning from minimal C4 to comprehensive C4 as projects grow
