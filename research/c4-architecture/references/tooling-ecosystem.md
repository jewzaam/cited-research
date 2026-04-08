# Tooling Ecosystem

Dimension covering tools for creating and maintaining C4 diagrams.

See [citations.md](../citations.md) for full source details.

## Tool Categories

The C4 tooling landscape divides into three categories [8][20]:

| Category | Characteristics | Examples |
|----------|----------------|----------|
| Visual Modeling | Maintain reusable objects, semantic understanding | IcePanel, Archi, Enterprise Architect |
| Diagrams-as-Code | Text-based, version controllable, CI-compatible | Structurizr DSL, C4-PlantUML, Mermaid |
| Visual Diagramming | Quick sketches, drag-and-drop, manual updates | draw.io, Visual Paradigm, Lucidchart |

Simon Brown's official tooling page explicitly distinguishes **diagramming** from **modeling** [8]:
- Diagramming: "boxes and lines" — cannot validate, query, or reuse elements without copy-paste
- Modeling: non-visual models with views — enables validation, renaming across views, semantic queries. "A model is just data" [8]

## Detailed Tool Comparison

### Structurizr (Reference Implementation)

Created by Simon Brown. "A way to define a software architecture model (based upon the C4 model) using a text-based domain specific language" [16].

**Features:**
- All C4 diagram types (context, container, component, code, landscape, dynamic, deployment) [16]
- Built-in ADR support [16]
- Markdown/AsciiDoc documentation [16]
- Export to PlantUML and Mermaid [16]
- Workspace extensions for multi-team use [18]
- Cookbook: AWS, Kubernetes, Docker, microservices patterns [16]
- Scripting and automation [16]

**Deployment options:** Cloud service (being sunset early 2026), Lite (free, open source, no further updates), on-premises (licensed, open core)

**Best for:** Teams wanting model-driven architecture documentation with full C4 support

### C4-PlantUML

"Combines the benefits of PlantUML and the C4 model" [27]. Open source, MIT license.

**Features:**
- Macros for all C4 levels + dynamic + deployment + sequence diagrams [27]
- VSCode snippets and IntelliJ live templates [27]
- Custom tags, sprites, and element linking [27]
- Auto legend generation [27]
- Multiple language themes [27]

**Best for:** Teams already using PlantUML or wanting diagrams-as-code with automatic layout

### Mermaid

**Status: EXPERIMENTAL** — "The syntax and properties can change in future releases" [19].

**Supported C4 types:** Context, Container, Component, Dynamic, Deployment [19]

**Limitations:**
- No sprites, tags, links, legend, or layout statements [19]
- Fixed CSS styling [19]
- No fully automated layout [19]
- Syntax compatible with PlantUML [19]

**Best for:** Teams wanting lightweight C4 embedded in markdown/GitHub, accepting limitations

### draw.io / diagrams.net

Built-in C4 shape library with Person, Software system, Container, Component [26].

**Features:**
- Multi-page support with cross-page linking [26]
- Shape metadata with tooltips [26]
- Additional libraries (UML, infrastructure, threat modeling) [26]
- Free and open source [26]

**Best for:** Quick visual diagrams, non-technical stakeholders, teams not ready for code-based tools

### IcePanel

Interactive C4 zooming into top 3 levels. Tags for overlaying perspectives. Real-time collaborative modeling [20].

**Pricing:** Free and paid [20]

**Best for:** Enterprise teams needing visual, collaborative C4 modeling

### Archi

Open source ArchiMate modeling tool that maps C4 abstractions to ArchiMate format [20]. Desktop application.

**Best for:** Teams bridging C4 with enterprise architecture (ArchiMate)

### Enterprise Architect (Sparx)

Paid. C4 addon available. Interactive zooming between all C4 levels, extendable with UML [20].

**Best for:** Enterprise organizations already invested in EA tooling

### Visual Paradigm

Paid. Built-in C4 shapes, templates, real-time collaboration [20].

### Lucidchart

Free and paid. C4 model template for all 4 levels, drag-and-drop [20].

## Tool Selection Decision Matrix

| Factor | Code-Based | Visual Modeling | Visual Diagramming |
|--------|-----------|----------------|-------------------|
| Version control | Native (text files) | Requires export | Requires export |
| CI/CD integration | Yes | Limited | No |
| Non-technical users | Difficult | Easy | Easy |
| Element reuse | Automatic (model) | Automatic (model) | Manual (copy-paste) |
| Learning curve | Moderate-High | Low-Moderate | Low |
| Collaboration | Via Git | Real-time | Real-time |
| Long-term accuracy | High (model-driven) | High (model-driven) | Low (manual sync) |

## Official Recommendations

Simon Brown's tooling page [8] recommends modeling tools over diagramming tools. The officially listed modeling tools are Structurizr, Archi, Gaphor, Overarch, and C4InterFlow [8]. Diagramming tools listed are draw.io, Mermaid, C4-PlantUML, and BAC4 Standalone [8].

For design sessions: "you might find a whiteboard or flip chart paper better for collaboration, and iterating quickly" [8].

## Level Support Across Tools

| Tool | L1 Context | L2 Container | L3 Component | L4 Code | Landscape | Dynamic | Deployment |
|------|-----------|-------------|-------------|---------|-----------|---------|------------|
| Structurizr | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| C4-PlantUML | Yes | Yes | Yes | — | — | Yes | Yes |
| Mermaid | Yes | Yes | Yes | — | — | Yes | Yes |
| draw.io | Yes | Yes | Yes | Via UML | — | — | — |
| IcePanel | Yes | Yes | Yes | — | Yes | Yes (flows) | Yes (groups) |

## Gaps and Limitations

- Structurizr Lite and CLI sunset in early 2026 creates uncertainty for current users
- Mermaid C4 support is explicitly experimental [19]
- No single tool supports all C4 features perfectly
- Auto-generation tools are language-specific (Go, .NET) rather than language-agnostic [25]
- Pricing details for commercial tools change frequently; verify current pricing before decisions
