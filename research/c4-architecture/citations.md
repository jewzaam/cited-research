# Citations

All sources visited in-session on 2026-04-08 via WebSearch and WebFetch.

## Citation Index

**[1]** c4model.com — "The C4 Model for Software Architecture"
- URL: https://c4model.com/
- Author: Simon Brown
- Type: Official project site
- Tier: 2 (Established reference site)
- Data extracted: Core definition, four levels, design principles, notation/tooling independence, CC BY 4.0 license, O'Reilly book availability

**[2]** c4model.com — "FAQ"
- URL: https://c4model.com/faq
- Author: Simon Brown
- Type: Official FAQ
- Tier: 2
- Data extracted: History (2006-2009 origins, 2011 naming), inspiration from UML and 4+1, adoption (10,000+ people, ~40 countries, Spotify/Decathlon/Co-op), scope limitations (static structures only), scalability guidance (split complex diagrams), arc42 mapping, applicability (custom-built systems, less suited for embedded/firmware)

**[3]** c4model.com — "Container Abstraction"
- URL: https://c4model.com/abstractions/container
- Author: Simon Brown
- Type: Official documentation
- Tier: 2
- Data extracted: Container definition (application or data store, runtime boundary), examples (web apps, databases, serverless functions), what is NOT a container (JARs, DLLs, modules), deployment as separate concern, web app splitting criteria, external service modeling

**[4]** c4model.com — "Component Abstraction"
- URL: https://c4model.com/abstractions/component
- Author: Simon Brown
- Type: Official documentation
- Tier: 2
- Data extracted: Component definition (grouping of related functionality behind well-defined interface), not separately deployable, varies by paradigm (OO/procedural/functional), what components are NOT (JARs, assemblies, packages)

**[5]** c4model.com — "Microservices"
- URL: https://c4model.com/abstractions/microservices
- Author: Simon Brown
- Type: Official documentation
- Tier: 2
- Data extracted: Two modeling options (single team → containers within one system; multiple teams → separate systems), Conway's Law application, ownership determines approach, modeling evolves with org structure

**[6]** c4model.com — "System Landscape Diagram"
- URL: https://c4model.com/diagrams/system-landscape
- Author: Simon Brown
- Type: Official documentation
- Tier: 2
- Data extracted: Definition (system context without specific focus), recommended for larger organisations, bridges to enterprise architecture, scope (enterprise/organisation/department), audience (technical and non-technical)

**[7]** c4model.com — "Deployment Diagram"
- URL: https://c4model.com/diagrams/deployment
- Author: Simon Brown
- Type: Official documentation
- Tier: 2
- Data extracted: Based on UML deployment diagrams, deployment nodes (physical/virtual/containerised), infrastructure nodes (DNS, load balancers), per-environment scope, audience includes operations staff, cloud provider icons supported

**[8]** c4model.com — "Tooling"
- URL: https://c4model.com/tooling
- Author: Simon Brown
- Type: Official documentation
- Tier: 2
- Data extracted: Diagramming vs modeling distinction, modeling advantages (validation, querying, element reuse), recommended modeling tools (Structurizr, Archi, Gaphor, Overarch, C4InterFlow), diagramming tools (draw.io, Mermaid, C4-PlantUML)

**[9]** c4model.com — "Dynamic Diagram"
- URL: https://c4model.com/diagrams/dynamic
- Author: Simon Brown
- Type: Official documentation
- Tier: 2
- Data extracted: Based on UML communication diagrams, free-form with numbered interactions, use "sparingly," two styles (collaboration and sequence), optional not essential

**[10]** c4model.com — "Notation"
- URL: https://c4model.com/diagrams/notation
- Author: Simon Brown
- Type: Official documentation
- Tier: 2
- Data extracted: Title and key/legend required, element type designation, relationship labeling (unidirectional, specific intent, technology labels), notation independence, accessibility (color blindness, B&W printing)

**[11]** Simon Brown — "Diagramming distributed architectures with the C4 model"
- URL: https://dev.to/simonbrown/diagramming-distributed-architectures-with-the-c4-model-51cm
- Author: Simon Brown
- Type: Blog post by C4 creator
- Tier: 3 (Well-known practitioner)
- Data extracted: C4 not less suitable for distributed than monolithic, problem is tooling not model, 20+ element threshold, focused subset diagrams, Structurizr DSL `include` syntax, interactive visualizations (D3.js, Ilograph), diagramming-to-modeling shift

**[12]** Working Software — "Misuses and Mistakes of the C4 Model"
- URL: https://www.workingsoftware.dev/misuses-and-mistakes-of-the-c4-model/
- Author: Working Software (industry blog)
- Type: Practitioner analysis
- Tier: 3
- Data extracted: C4 dates to 2007, not designed to replace UML, notation independent, removing metadata introduces ambiguity, container vs component confusion, arbitrary levels reintroduce chaos, shared libraries not containers, message broker topics as separate containers, external system internals as anti-pattern

**[13]** InfoQ — "The C4 Model for Software Architecture"
- URL: https://www.infoq.com/articles/C4-architecture-model/
- Author: Simon Brown (published by InfoQ)
- Type: Industry publication article
- Tier: 3
- Data extracted: "Google Maps for your code," four levels description, notation agnostic, Level 4 "rarely necessary since IDEs generate this automatically," addresses post-Agile documentation decline

**[14]** arc42 FAQ — "B-17: arc42 and C4"
- URL: https://faq.arc42.org/questions/B-17/
- Author: arc42 project
- Type: Official FAQ
- Tier: 2
- Data extracted: C4 shares "many similarities to a few sections from arc42," C4 "omits certain parts (e.g. quality requirements, crosscutting concepts, risks)," complementary rather than competing

**[15]** Wikipedia — "C4 model"
- URL: https://en.wikipedia.org/wiki/C4_model
- Author: Wikipedia contributors
- Type: Encyclopedia
- Tier: 2 (Established reference)
- Data extracted: "Lean graphical notation technique," created 2006-2011, five basic elements, 2018 InfoQ article expanded adoption, CC license

**[16]** Structurizr — "DSL"
- URL: https://docs.structurizr.com/dsl
- Author: Structurizr/Simon Brown
- Type: Official documentation
- Tier: 2
- Data extracted: "Text-based domain specific language" for C4, supports all diagram types, Markdown/AsciiDoc docs, built-in ADR, scripting, PlantUML/Mermaid export, workspace extensions, cookbook for AWS/K8s/Docker/microservices

**[17]** Structurizr — "Workspaces"
- URL: https://docs.structurizr.com/workspaces
- Author: Structurizr
- Type: Official documentation
- Tier: 2
- Data extracted: Workspace wraps model + views + documentation + ADRs

**[18]** Structurizr — "Enterprise"
- URL: https://docs.structurizr.com/workspaces/enterprise
- Author: Structurizr
- Type: Official documentation
- Tier: 2
- Data extracted: "Uber workspace" anti-pattern (scale limits, ordering deps, single-failure risk, restricted autonomy), three-step solution (system catalog, workspace extension, centralized landscape), composition over inheritance, DSL colocated with source code

**[19]** Mermaid — "C4 Diagrams"
- URL: https://mermaid.js.org/syntax/c4.html
- Author: Mermaid project
- Type: Official documentation
- Tier: 2
- Data extracted: EXPERIMENTAL status, supports 5 C4 diagram types (Context, Container, Component, Dynamic, Deployment), PlantUML-compatible syntax, limitations (no sprites/tags/links/legend/layout), fixed CSS styling

**[20]** IcePanel — "Top 9 Tools for C4 Model Diagrams"
- URL: https://icepanel.io/blog/2025-08-28-top-9-tools-for-c4-model-diagrams
- Author: IcePanel
- Type: Vendor blog
- Tier: 3
- Data extracted: Nine tools in three categories (visual modeling: IcePanel/Archi/Enterprise Architect; code-based: Structurizr/Mermaid/PlantUML; visual diagramming: draw.io/Visual Paradigm/Lucidchart), modeling vs diagramming distinction

**[21]** Tech Posts — "C4 and ArchiMate Comparison"
- URL: https://www.tech-posts.com/a-comprehensive-guide-to-c4-and-archimate-choosing-the-right-modeling-approach-for-modern-software-architecture/
- Author: Tech Posts
- Type: Industry blog
- Tier: 3
- Data extracted: C4 "developer-first" vs ArchiMate "enterprise-grade," C4 "minutes to confidence" vs ArchiMate weeks, C4 for agile/API/microservices, ArchiMate for transformation/governance, "not competitors—they are symbiotic"

**[22]** Wikipedia — "4+1 architectural view model"
- URL: https://en.wikipedia.org/wiki/4%2B1_architectural_view_model
- Author: Wikipedia contributors
- Type: Encyclopedia
- Tier: 2
- Data extracted: Created by Philippe Kruchten 1995, five views (Logical, Process, Development, Physical, Scenarios), generic and notation-independent, process view covers runtime behavior C4 doesn't

**[23]** Nikolas Chou — "Let us revise the C4 model"
- URL: https://nikolaschou.medium.com/let-us-revise-the-c4-model-for-software-architecture-diagrams-e2ae0d3de41c
- Author: Nikolas Chou
- Type: Practitioner blog
- Tier: 4
- Data extracted: "Container" confusion, proposed renaming (Context→System, Container→Component, Component→Sub-component, Code→Deployment), deployment "even more important than sub-component views," metadata clutter criticism

**[24]** Revision App — "Practical C4 Modeling Tips"
- URL: https://revision.app/blog/practical-c4-modeling-tips
- Author: Revision App
- Type: Practitioner blog
- Tier: 3
- Data extracted: "Level 1 and Level 2 are where most of the value lies," skip user modeling when obvious, merge deployment into Level 2, number relationships for sequences, landscape diagram as entry point for small-medium, "pragmatism over purity"

**[25]** Three Dots Labs — "Auto-Generated C4 Architecture Diagrams in Go"
- URL: https://threedots.tech/post/auto-generated-c4-architecture-diagrams-in-go/
- Author: Three Dots Labs
- Type: Engineering blog
- Tier: 3
- Data extracted: go-structurizr library, scraper + view + integration components, regex-based package scanning, tag-based styling, CI integration for auto-regeneration, demonstrated on wild-workouts-go-ddd-example

**[26]** draw.io — "C4 Modelling"
- URL: https://www.drawio.com/blog/c4-modelling
- Author: diagrams.net/draw.io
- Type: Official blog
- Tier: 2
- Data extracted: Built-in C4 shape library (Person, Software system, Container, Component), multi-page support, cross-page linking, shape metadata with tooltips, free and open source

**[27]** C4-PlantUML — GitHub README
- URL: https://github.com/plantuml-stdlib/C4-PlantUML
- Author: C4-PlantUML contributors
- Type: Open source project
- Tier: 3
- Data extracted: Combines PlantUML + C4, macros for all levels + dynamic + deployment + sequence, VSCode/IntelliJ support, custom tags/sprites, MIT license, multiple language themes

**[28]** ADEO Tech — "How do we document architecture across multiple teams"
- URL: https://medium.com/adeo-tech/how-do-we-document-architecture-across-multiple-teams-1e406883b402
- Author: ADEO Services
- Type: Engineering case study
- Tier: 3
- Data extracted: ~10 feature teams, chose C4 over 4+1 ("simpler and already covers all our needs"), Levels 1-2 only, DOT+Graphviz for auto-generation, per-repo documentation, aggregation via API/UI, clutter at scale (5+ services, 10+ data sources), entity flow filtering solution

**[29]** Ilograph — "Concrete Diagramming Models"
- URL: https://www.ilograph.com/blog/posts/concrete-diagramming-models/
- Author: Ilograph
- Type: Vendor blog
- Tier: 3
- Data extracted: Bottom-up vs C4's top-down, concrete resources (database tables, APIs, servers), C4 shortcomings (opinionated abstractions, abstraction blindness), "both have their place," C4 suitable for overviews, concrete for existing system detail

**[30]** IcePanel — "Deployment Diagrams in the C4 Model"
- URL: https://icepanel.io/blog/2024-08-27-deployment-diagram-c4-model
- Author: IcePanel
- Type: Vendor blog
- Tier: 3
- Data extracted: Deployment not in core 4 levels, typically at Level 2 but flexible, use cases (scalability, cloud migration, DR, cost analysis), Groups for nodes, Tags for attributes
