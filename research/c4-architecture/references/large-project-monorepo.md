# Large Project — Monorepo

Dimension covering how C4 maps to module boundaries, internal dependencies, and team ownership within large single-repo codebases.

See [citations.md](../citations.md) for full source details.

## C4 Mapping to Monorepo Structures

In a monorepo, the mapping between C4 abstractions and code organization depends on how the monorepo is structured:

| Monorepo Structure | C4 Mapping |
|-------------------|------------|
| Single deployable (monolith) | One software system, one container, components map to modules |
| Multiple deployable services | One software system with multiple containers, or multiple systems |
| Shared libraries + services | Libraries as components (not containers), services as containers |

**Key principle:** A C4 container is "an application or a data store" that "needs to be running" [3]. Shared libraries are NOT containers — they're components because they aren't separately deployable [12]. "A Java JAR, C# assembly, DLL, module, etc" do not qualify as containers [3].

## Module Boundaries and Components

A C4 component represents "a grouping of related functionality encapsulated behind a well-defined interface" [4]. In a monorepo context:

- Modules with well-defined public interfaces map naturally to C4 components [4]
- Package/namespace boundaries don't automatically equal component boundaries — "a Java JAR, C# assembly, DLL, module, package, namespace, folder etc" are typically NOT components [4]
- Component diagrams (Level 3) are where monorepo internal structure becomes visible
- For monoliths, Level 2 shows the single deployable + database; Level 3 zooms into modules/controllers [13]

## Team Ownership and System Boundaries

C4's guidance on ownership is explicit through the microservices abstraction [5]:

**Single team, single system:** When one team owns all services as one product, each service is "a group of one or more containers" within the system boundary [5]. The system context diagram remains unchanged.

**Multiple teams, multiple systems:** As organizations scale, services transition from "an implementation detail inside a single software system" to separate software systems [5]. Each team's domain gets its own system with distinct context and container diagrams.

**Conway's Law applies:** The diagramming approach should follow organizational structure, not just technical boundaries [5]. Ownership determines the approach.

## Managing Diagram Complexity

The fundamental scaling problem: "diagrams exceeding 20+ elements quickly become difficult to comprehend" [11]. Solutions from Simon Brown:

1. **Focused subset diagrams** — "split that single complex diagram into a larger number of simpler diagrams, each with a specific focus around a business area, functional area, functional grouping, bounded context, use case, user interaction, feature set, etc." [2]
2. **Model-driven approach** — use Structurizr DSL's `include` syntax to auto-generate focused views from a unified model [11]
3. **Interactive visualizations** — move beyond static images to D3.js force-directed graphs or navigational tools [11]

## Diagrams-as-Code in Monorepos

For monorepos, the diagrams-as-code approach is natural:

- Store C4 DSL files alongside the code they describe
- Changes to architecture documentation happen in the same PR as code changes
- Version control tracks architectural evolution alongside code evolution

ADEO Tech implemented this with DOT + Graphviz: each team maintains two files per repo (context and container), with changes requiring "only a few lines of changes" [28]. The textual format means "you can see changes to diagrams in your git diff" [28].

## Practical Recommendations

1. **Start with Level 1 + 2** — container diagrams show deployable boundaries within the monorepo
2. **Use Level 3 selectively** — only for containers with genuinely complex internal structure
3. **Align container boundaries with deployment units** — deployment is a separate concern from code organization [3]
4. **Don't model everything** — focus on "elements difficult to discover through code inspection: complex service orchestration, critical business rules governing interactions, and non-obvious data dependencies" [24]
5. **Link to generated docs** — use OpenAPI, AsyncAPI, and schema generators for details that change frequently [24]

## Auto-Generation from Monorepo Code

Language-specific tools exist for generating C4 diagrams from code:

- **go-structurizr** (Go): Scrapes Go structures via regex rules, generates PlantUML, supports CI integration [25]
- **C4InterFlow** (.NET/C#): Architecture-as-code framework [8]
- **Oselvar C4** (generic): Decorator-based approach (@C4SoftwareSystem, @C4Container annotations)

The go-structurizr approach: configure package regex rules → scraper crawls structures → view renders to PlantUML → CI auto-regenerates on code changes [25]. This ensures "diagrams reflect current code structure" and eliminates manual maintenance [25].

## Real-World Example: ADEO Tech

ADEO Services (~10 feature teams, one international platform) [28]:
- Chose C4 over 4+1: "simpler and already covers all our needs"
- Levels 1-2 only
- Per-repository documentation with standardized conventions
- Aggregation via API + custom UI across all teams
- Limitation: large systems (5+ services, 10+ data sources) cause clutter
- Solution: entity flow filtering

## Gaps and Limitations

- No published monorepo-specific case studies from major companies (Google, Meta, etc.)
- Auto-generation tools are language-specific and fragmented [25]
- No quantitative data on maintenance burden of C4 in monorepos
- Limited guidance on handling shared code/libraries that span container boundaries
- No established pattern for mapping build system targets (Bazel, Nx) to C4 abstractions
