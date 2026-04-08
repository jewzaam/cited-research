# C4 Model Fundamentals

Dimension covering the core model, its four levels, design philosophy, and relationship to other modeling approaches.

See [citations.md](../citations.md) for full source details.

## Origins and History

The C4 model was created by Simon Brown. Its roots trace to 2006-2009, with diagram types named in early 2010 and the "C4" name adopted in 2011 [2]. The fourth level was originally called "classes" and renamed to "code" during 2015-2016 [2]. The model draws inspiration from UML and the 4+1 architectural view model [2], designed as "a simplified version of the underlying concepts" to "minimise the gap between the software architecture model/description and the source code" [2].

Brown developed C4 when agile teams resisted UML [2]. The 2018 InfoQ article significantly expanded the technique's visibility and adoption [15]. It is described as "a lean graphical notation technique for modeling the architecture of software systems" [15].

## The Four Levels

| Level | Name | What It Shows | Audience |
|-------|------|--------------|----------|
| 1 | System Context | System in scope + users + external systems | Technical and non-technical |
| 2 | Container | Applications, data stores, and their interactions | Technical people |
| 3 | Component | Internal building blocks within a container | Developers and architects |
| 4 | Code | Implementation details (classes, functions) | Developers |

**Level 1 — System Context:** Shows the software system's relationship with users and other systems. Color coding distinguishes existing systems from those being built [13].

**Level 2 — Container:** Zooms into the system to show individual deployable units — web applications, databases, microservices — and their technologies [13]. A container is "an application or a data store" that "needs to be running in order for the overall software system to work" [3].

**Level 3 — Component:** Reveals "a grouping of related functionality encapsulated behind a well-defined interface" within a container [4]. Components are NOT separately deployable [4]. Eliminates "code-level noise" while preserving architectural understanding [4].

**Level 4 — Code:** Implementation-level detail via UML class diagrams or equivalent. Brown notes this level is "rarely necessary since IDEs generate this automatically" [13].

## Supplementary Diagrams

Beyond the four core levels, C4 includes supplementary diagram types:

| Diagram | Purpose | Based On |
|---------|---------|----------|
| System Landscape | Portfolio/enterprise view across multiple systems [6] | — |
| Dynamic | Runtime interaction sequences for specific features [9] | UML communication diagram |
| Deployment | Mapping containers to infrastructure per environment [7] | UML deployment diagram |

**System Landscape** operates as "a system context diagram without a specific focus on a particular software system" [6]. Recommended "particularly for larger organisations" [6].

**Dynamic diagrams** should be used "sparingly to show interesting/recurring patterns or features that require a complicated set of interactions" [9]. Support collaboration and sequence styles [9].

**Deployment diagrams** show deployment nodes (physical, virtual, containerised) and infrastructure nodes (DNS, load balancers, firewalls) [7]. Can incorporate cloud provider icons [7].

## Core Design Principles

1. **Notation independent** — "The C4 model is notation independent" and doesn't prescribe specific notation [10]
2. **Tooling independent** — can be implemented with any software tool [1]
3. **Developer-friendly** — designed for technical teams [1]
4. **Hierarchical zoom** — functions as "Google Maps for your code" [13]
5. **Small vocabulary** — five basic elements: persons, software systems, containers, components, relationships [15]

## Notation Requirements

Every diagram must include a title and key/legend [10]. Elements require explicit type designation and short description [10]. Relationships must be unidirectional, labeled with direction and intent, specific beyond "Uses," and include technology labels for inter-process communication [10]. Colors are optional but should consider accessibility (B&W printing, color blindness) [10].

## Relationship to UML

C4 is not a replacement for UML [12]. If UML works for a team, they should continue using it [2]. However, "many teams have reverted to using ad hoc boxes and lines diagrams" after abandoning UML [2], and C4 provides structure for those teams. C4 focuses on static structures; teams should supplement with "UML state diagrams, timing diagrams, etc if you need to" [2].

## Which Levels to Use

Simon Brown and multiple practitioners confirm that Levels 1 and 2 provide the most value [2][24]. "System context and container diagrams sufficient for most software development teams" [2]. Levels 3 and 4 are more situational, have smaller audiences, and require higher maintenance effort [24]. Level 4 (Code) is "rarely necessary" [13].

## Adoption

C4 has been taught to over 10,000 people across approximately 40 countries [2]. Major adopters include Spotify, Decathlon, and Co-op [2]. The model appears on Wikipedia, InfoQ articles, and within Open Group standards [2].

## Gaps and Limitations

- C4 focuses on "static structures" only; dynamic behavior requires supplementary diagrams [2]
- Not designed for embedded systems/firmware or heavily customized solutions (SAP, Salesforce) [2]
- Does not cover quality requirements, crosscutting concepts, risks, or architecture decision rationale [14]
- For libraries, frameworks, and SDKs, "you might be better off using something like UML" [2]
