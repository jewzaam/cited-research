# Criticisms and Limitations

Dimension covering where C4 falls short, common pitfalls, and alternatives.

See [citations.md](../citations.md) for full source details.

## Common Pitfalls

These are mistakes practitioners commonly make when adopting C4 [12]:

| Pitfall | Why It's Wrong | Correct Approach |
|---------|---------------|-----------------|
| Confusing containers and components | "Containers are deployable units, while components are non-deployable elements inside a container" [12] | Ask: does it run independently? Container. Is it inside something that runs? Component. |
| Adding arbitrary levels (e.g., "subcomponents") | "Reintroduces the chaos C4 aims to avoid" [12] | Stick to the four defined levels |
| Removing metadata labels | "Introduces ambiguity, making diagrams harder to interpret" [12] | Always label element types |
| Shared libraries as containers | Libraries aren't deployable units [12] | Represent as components across multiple diagrams |
| Message broker as single container | Misses pub/sub relationship structure [12] | Model individual topics as separate containers |
| Showing internal details of external systems | Introduces coupling and volatility [12] | Focus on boundaries and abstract interactions |
| Treating C4 as UML replacement | "C4 was never designed to replace UML" [12] | Use both; C4 for structure, UML for behavior |
| Thinking C4 is recent | Dates to 2007 [12] | Unchanged core since creation |

## What C4 Does NOT Model

C4 focuses on "static structures that make up a software system, at different levels of abstraction" [2]. It explicitly does not cover:

| Not Covered | Alternative |
|-------------|------------|
| Runtime behavior / temporal interactions | Dynamic diagrams (supplementary) [9], UML sequence/state diagrams [2] |
| Data flows and data models | Entity relationship diagrams [2] |
| Business processes and workflows | BPML, ArchiMate [2] |
| Quality requirements | arc42 template [14] |
| Crosscutting concepts | arc42 template [14] |
| Risks | arc42 template [14] |
| Architecture decision rationale | ADRs [12] |
| State machines | UML state diagrams [2] |

C4's dynamic diagrams are supplementary, not core, and should be used "sparingly" [9]. They cannot fully substitute for UML sequence diagrams for complex behavioral modeling.

## Terminology Criticism

The term "container" at Level 2 is C4's most criticized naming choice:

- "Referring to the backend and database as components resonates so much better than referring to them as containers" [23]
- Predates Docker's popularity but now creates confusion with infrastructure containers [3]
- IcePanel renamed "Container" to "Apps and Stores" in their tool to reduce confusion
- Proposed revision: Context → System, Container → Component, Component → Sub-component, Code → Deployment [23]

Simon Brown acknowledges the term was "deliberately chosen as generic terminology" [3] but the collision with Docker/Kubernetes containers is widely noted.

## Scalability Criticisms

### Diagram Clutter

"Diagrams exceeding 20+ elements quickly become difficult to comprehend" [11]. ADEO Tech found that with "five different services, more than ten different places injecting data, and more than ten consumers," diagrams become "completely unreadable" [28].

### Enterprise Scale

"The Structurizr tooling was never designed to handle workspaces that contain hundreds or thousands of software systems" [18]. Organizations with many teams may have hundreds of software systems, each needing context diagrams.

### Distributed Systems Myth

The claim that "C4 is unsuited for distributed systems" is explicitly false [11]. The problem is "tooling limitations and our reliance on static PNG files" [11], not the model itself. Solutions: focused subset diagrams, interactive visualizations, model-driven approaches.

## Level 4 (Code) Questioned

Multiple sources question the value of Level 4:

- "Rarely necessary since IDEs generate this automatically" [13]
- Proposed replacement with Deployment as the 4th level: deployment is "even more important than sub-component views" [23]
- In practice, most tools support only the top 3 levels [20]

## Opinionated Abstractions

The concrete diagramming models critique argues C4 forces diverse resources into rigid categories [29]:

- "A database instance is a database instance; debating whether it is also a Container or a Component just isn't worthwhile" [29]
- Abstraction emphasis can obscure concrete resources: "A system's concrete resources... are almost always more important than the abstractions used to simplify them" [29]
- C4's top-down approach contrasts with bottom-up, fact-based alternatives

However: "Both concrete models and C4 models have their place" [29]. C4 excels at introductory overviews and standardized communication.

## Maintenance Burden

Architecture diagrams "frequently become outdated because applications change constantly through naming updates and major refactoring" [25]. The biggest practical risk is diagrams falling out of sync with code, producing misleading documentation that's worse than no documentation.

Mitigation strategies:
- Auto-generation from code [25]
- Diagrams-as-code in version control [28]
- Model-driven tools that propagate changes [8]
- Limiting scope to Levels 1-2 to reduce update surface [24]

## Alternatives to C4

### arc42

Complete documentation template covering quality requirements, crosscutting concepts, risks — everything C4 omits [14]. C4 shares "many similarities to a few sections from arc42" but is less comprehensive [14]. Complementary use is common: arc42 template + C4 diagrams.

**Mapping:** Context/Scope → System Context; Building Block View level 1 → Container; level 2 → Component; level 3 → Code [2].

### 4+1 View Model

Created by Philippe Kruchten, 1995 [22]. Five views: Logical, Process, Development, Physical, Scenarios. The **Process view** covers runtime behavior that C4 doesn't — concurrency, distribution, performance, scalability [22]. Generic and notation-independent [22].

C4 drew inspiration from 4+1 [2] but simplified it. ADEO Tech evaluated both and chose C4: "simpler and already covers all our needs" [28].

### ArchiMate

"Enterprise-grade strategic framework" bridging business strategy and IT [21]. Three layers: Business, Application, Technology. "Not competitors — they are symbiotic" with C4 [21].

| Dimension | C4 | ArchiMate |
|-----------|-----|-----------|
| Learning curve | "Minutes to confidence" [21] | Weeks of study [21] |
| Audience | Developers, DevOps [21] | Enterprise architects, CTOs [21] |
| Use case | "Agile development, API design" [21] | "Digital transformation, IT governance" [21] |

Recommended integration: ArchiMate for strategy, C4 for technical execution [21].

### Views & Beyond (V&B)

SEI framework. Flexible view selection (Module, Component & Connector, Allocation). Notation/language independent. ISO/IEC 42010 compliant. More customizable than C4's fixed levels.

### Concrete Diagramming Models

Bottom-up, fact-based alternative [29]. Domain-agnostic, flexible abstraction levels, focuses on concrete resources. Better for detailed diagrams of existing systems; C4 better for introductory overviews [29].

## When to Choose Alternatives

| Choose | When |
|--------|------|
| arc42 | Need comprehensive documentation beyond diagrams |
| 4+1 | Need runtime/process views, formal stakeholder perspectives |
| ArchiMate | Enterprise governance, business-IT alignment |
| V&B (SEI) | Regulated industries, ISO compliance requirements |
| Concrete models | Detailed existing system documentation, diverse resource types |
| UML | Behavioral modeling (state machines, sequences), library/SDK documentation [2] |

## The Creator's Response

Simon Brown has given conference talks specifically on "Misconceptions, Misuses, and Mistakes" [12], showing awareness and transparency about common problems. His key responses:

- C4 is for static structure; supplement with other diagram types [2]
- Split complex diagrams rather than cramming everything in [2]
- Shift from diagramming to modeling for scale [11]
- The model implies nothing about process or team structure [2]

## Gaps and Limitations

- No peer-reviewed studies evaluating C4 effectiveness vs alternatives
- No empirical data on adoption failure rates or organizational resistance
- Criticisms come primarily from practitioner blogs (Tier 3-4), not formal analysis
- The "container" naming debate has no resolution — Simon Brown defends the choice, practitioners continue to find it confusing
- No published comparison measuring documentation effort across C4, arc42, 4+1, and ArchiMate
