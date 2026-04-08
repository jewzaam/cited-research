# C4 Architecture Model: Application to Small and Large Projects

## Methodology

This analysis uses the cited-research methodology: every factual claim traces to a web source visited in-session. Sources are numbered and catalogued in [citations.md](citations.md). Detailed data for each dimension is in the [references/](references/) directory. Two independent review agents audited the output for citation accuracy and internal consistency.

## Executive Summary

The C4 model is a hierarchical approach to software architecture visualization created by Simon Brown between 2006-2011 [2][15]. It provides four levels of abstraction — System Context, Container, Component, and Code — functioning as "Google Maps for your code" [13]. The model is notation-independent, tooling-independent, and developer-friendly [1].

**The most important practical finding:** Levels 1 and 2 (System Context and Container) provide the majority of value regardless of project scale [2][24]. The model scales from single-purpose applications to distributed platforms, but the approach to using it differs significantly across scales.

For small projects, C4's value lies in two diagrams that take minutes to create. For large platforms, C4's value lies in the modeling discipline — defining elements and relationships in a model that generates multiple focused views [11].

## C4 Model Overview

### The Four Levels

| Level | Name | What It Shows | Primary Audience |
|-------|------|--------------|-----------------|
| 1 | System Context | System + users + external systems | Everyone |
| 2 | Container | Deployable units (apps, databases) within the system | Technical people |
| 3 | Component | Functional groupings within a container | Developers, architects |
| 4 | Code | Implementation details (classes, functions) | Developers |

A **container** is "an application or a data store" that "needs to be running in order for the overall software system to work" [3]. This is a runtime boundary, not a code organization construct — JARs, DLLs, and modules are NOT containers [3].

A **component** is "a grouping of related functionality encapsulated behind a well-defined interface" [4]. Components are not separately deployable — all components within a container execute in the same process space [4].

Level 4 (Code) is "rarely necessary since IDEs generate this automatically" [13].

### Supplementary Diagrams

| Diagram | Purpose | Guidance |
|---------|---------|---------|
| System Landscape | Portfolio view across multiple systems [6] | "Particularly for larger organisations" [6] |
| Dynamic | Runtime interaction sequences [9] | Use "sparingly" [9] |
| Deployment | Containers mapped to infrastructure per environment [7] | Recommended as part of documentation [7] |

### Notation

The C4 model is notation-independent [10]. Every diagram must include a title and key/legend [10]. Elements require type designation and description. Relationships must be unidirectional, labeled with intent, and include technology labels for inter-process communication [10].

## Application by Project Scale

### Small Projects

**Definition:** Self-contained, single-purpose applications — typically a monolith or simple client-server with fewer than five containers.

**What to use:** Levels 1 + 2 only. "Level 1 (System Context) and Level 2 (Container) are where most of the value lies" [24]. ADEO Tech, managing ~10 feature teams, uses only Levels 1 and 2: "simpler and already covers all our needs" [28].

**What to skip:** Component diagrams (Level 3) unless internals are genuinely complex. Code diagrams (Level 4) always. Separate deployment diagrams — practitioners recommend merging deployment context into Level 2 directly: "including deployment context directly in the same diagram often adds more value than splitting it out" [24].

**When C4 is overkill:** Trivially simple systems (single container, no meaningful external dependencies), temporary/experimental projects, hardware-intensive systems [2], teams of 1-2 people with full shared context.

**Practical simplifications:**
- Skip explicit user modeling when obvious — "just adds clutter without adding clarity" [24]
- Number relationships for sequences instead of creating separate dynamic diagrams [24]
- Use a landscape diagram as the primary diagram for small-to-medium architectures [24]
- For design sessions, "you might find a whiteboard or flip chart paper better for collaboration" [8]

**Tooling:** draw.io (free, built-in C4 shapes [26]), Mermaid (embeds in markdown [19]), or C4-PlantUML (version controllable [27]). Structurizr DSL is more powerful but requires technical proficiency [20].

See [references/small-project-application.md](references/small-project-application.md) for full analysis.

### Large Projects — Monorepo

**Definition:** Large codebases with many modules in a single repository — either a monolith with internal modules or multiple deployable services in one repo.

**Key mapping:**

| Monorepo Element | C4 Abstraction |
|-----------------|----------------|
| Deployable service | Container |
| Module with public interface | Component |
| Shared library | Component (NOT container — not deployable) [12] |
| Database | Container |
| The repository as a whole | Software system (usually) |

**Team ownership drives boundaries:** When one team owns everything, it's one software system with multiple containers [5]. When multiple teams own different parts, consider modeling their domains as separate systems [5]. "As organizations scale and apply Conway's Law, microservices transition from 'an implementation detail inside a single software system' to separate software systems" [5].

**Managing complexity:** Diagrams with 20+ elements become unwieldy [11]. Solutions:
1. Split into focused diagrams by bounded context, feature, or team area [2]
2. Use model-driven tools (Structurizr DSL) to generate focused views from a unified model [11]
3. Consider interactive visualizations for very large systems [11]

**Diagrams-as-code advantage:** Store C4 DSL files alongside code. Architecture changes happen in the same PR as code changes. "You can see changes to diagrams in your git diff" [28].

**Auto-generation:** go-structurizr for Go codebases [25], C4InterFlow for .NET [8]. These work for Component/Code levels but Context and Container levels still need human judgment about system boundaries.

See [references/large-project-monorepo.md](references/large-project-monorepo.md) for full analysis.

### Large Projects — Fragmented Platform

**Definition:** Multi-repo platform architectures with multiple teams, shared infrastructure, and central orchestration points.

**The essential diagram:** System landscape — "a system context diagram without a specific focus on a particular software system" [6]. This is the portfolio-level view that makes cross-repo dependencies visible.

**System boundary decisions:**

| Situation | C4 Approach |
|-----------|------------|
| One team, all services | Services as containers within one system [5] |
| Multiple teams, owned services | Each team's services as separate systems [5] |
| Shared infrastructure | Model per ownership — platform team → platform system |

**Structurizr enterprise pattern (recommended)** [18]:
1. **System Catalog:** Shared DSL with minimal system definitions (name, description only)
2. **Workspace Extension:** Teams use `workspace extends` to add internal architecture
3. **Centralized Landscape:** `generate system-landscape` aggregates across workspaces

**Anti-pattern: Uber Workspace.** "The Structurizr tooling was never designed to handle workspaces that contain hundreds or thousands of software systems" [18]. Problems: scale limits, ordering dependencies, single-failure risk, restricted team autonomy.

**Platform-level elements:**
- API gateways → container in relevant system's container diagram
- Service meshes → deployment diagram infrastructure
- Message brokers → model individual topics as containers, not the whole broker [12]
- External services (S3, RDS) → containers, "because they are an integral part of your software architecture" [3]

**Dynamic diagrams for orchestration:** Use sparingly for "interesting/recurring patterns or features that require a complicated set of interactions" [9] across service boundaries.

**Scale indicators:** ADEO Tech found that 5+ services with 10+ data sources creates unreadable diagrams [28]. Solution: entity flow filtering to follow one concern end-to-end.

See [references/large-project-fragmented-platform.md](references/large-project-fragmented-platform.md) for full analysis.

## Decision Framework: Which Levels Do I Need?

```
Step 1: Is this custom-built software?
  No  → C4 is less suited; Context + Container may still help [2]
  Yes → Continue

Step 2: How many containers (deployable things)?
  1     → System Context diagram only
  2-5   → System Context + Container diagrams
  6-20  → System Context + Container + selective Component diagrams
  20+   → Full model-driven approach with focused views [11]

Step 3: How many teams?
  1     → One software system, containers within it [5]
  2+    → Consider separate systems per team domain [5]

Step 4: How many repos?
  1 (monorepo)   → DSL alongside code, team-scoped views
  Multiple       → Structurizr workspace extension pattern [18]

Step 5: Do you need behavior diagrams?
  Occasionally → Dynamic diagrams, used sparingly [9]
  Extensively  → Supplement with UML sequence/state diagrams [2]
```

## Tooling Recommendations

### By Project Context

| Context | Recommended Tool | Why |
|---------|-----------------|-----|
| Small project, quick start | draw.io | Free, built-in C4 shapes, zero learning curve [26] |
| Small project, developer-heavy | Mermaid or C4-PlantUML | Embeds in markdown, version controllable [19][27] |
| Medium project, need model | Structurizr DSL | Model-driven, focused views, ADR support [16] |
| Large platform, multi-team | Structurizr with workspace extension | Composition pattern, centralized landscape [18] |
| Enterprise, mixed audience | IcePanel or Archi | Visual modeling, real-time collaboration [20] |
| Enterprise architecture bridge | ArchiMate + C4 | Strategy (ArchiMate) + execution (C4) [21] |

### Diagrams-as-Code vs. Visual Tools

Use diagrams-as-code (Structurizr, PlantUML, Mermaid) when: developer-heavy teams, version control matters, CI/CD integration needed, long-term accuracy is priority.

Use visual tools (draw.io, IcePanel, Lucidchart) when: mixed technical/non-technical audience, rapid iteration in design sessions, presentation is the primary use case.

See [references/tooling-ecosystem.md](references/tooling-ecosystem.md) and [references/diagrams-as-code.md](references/diagrams-as-code.md) for full analysis.

## Keeping Diagrams Alive

The biggest risk with any architecture documentation: falling out of sync with code [25]. Strategies by effectiveness:

1. **Store DSL with code** — architecture changes happen in the same PR [28]
2. **Model-driven tools** — element changes propagate across all views [8]
3. **Auto-generate from code** — go-structurizr [25], C4InterFlow [8] for lower levels
4. **Limit scope** — stick to Levels 1-2 to reduce update surface [24]
5. **Link, don't duplicate** — reference OpenAPI specs rather than repeating API details [24]
6. **Date your diagrams** — "you can check immediately upon looking at the date how old the documentation is" [28]

## Limitations and When to Look Elsewhere

### What C4 Covers Well

- Static structural decomposition at multiple zoom levels
- System boundaries and external dependencies
- Container-level technology decisions
- Communication across technical and non-technical audiences [6]

### What C4 Does NOT Cover

Runtime behavior, data flows, business processes, quality requirements, crosscutting concepts, risks, architecture decision rationale [2][14]. Supplement with UML (behavior), arc42 (documentation template), and ADRs (decisions) [2][12].

### Key Criticisms

1. **"Container" terminology** — confusing in the Docker/Kubernetes era [23]
2. **Level 4 (Code) rarely used** — proposed replacement with Deployment [23]
3. **Static only** — dynamic diagrams are supplementary, not core [9]
4. **Opinionated abstractions** — forces resources into four categories; "a database instance is a database instance" [29]
5. **Scale limits** — tooling not designed for hundreds of systems [18]
6. **Maintenance burden** — diagrams become outdated without auto-generation or CI integration [25]

### When to Choose Alternatives

| Need | Alternative | Why |
|------|------------|-----|
| Complete documentation template | arc42 | Covers quality requirements, risks, crosscutting concerns [14] |
| Runtime behavior modeling | 4+1 View Model | Process view covers concurrency, performance [22] |
| Enterprise governance | ArchiMate | Business-IT alignment, investment justification [21] |
| Formal compliance | Views & Beyond (SEI) | ISO/IEC 42010 compliant |
| Detailed existing systems | Concrete diagramming | Bottom-up, fact-based, unlimited levels [29] |
| Behavioral design | UML | State machines, sequences, timing [2] |

**Complementary use is common.** arc42 + C4, ArchiMate + C4, and C4 + UML are all established combinations [2][14][21]. C4 alone is often insufficient for comprehensive architecture documentation.

See [references/criticisms-and-limitations.md](references/criticisms-and-limitations.md) for full analysis.

## Summary

C4's strength is proportional to how you use it:

- **Small projects:** Two diagrams (Context + Container) that take minutes. High ROI for onboarding and stakeholder communication. Don't over-engineer it.
- **Monorepos:** Map containers to deployable units, components to modules. Store DSL alongside code. Use team ownership to determine system boundaries.
- **Fragmented platforms:** System landscape for portfolio view. Composition pattern for multi-team workspaces. Focused diagrams over comprehensive ones. Model, don't just diagram.

The universal guidance: "Pragmatism over purity" [24]. Start with Levels 1 and 2. Add more only when complexity demands it. "Effective diagrams people maintain beat theoretically pure diagrams nobody updates" [24].
