# Large Project — Fragmented Platform

Dimension covering how C4 handles multi-repo platform architectures with cross-repo dependencies and central orchestration points.

See [citations.md](../citations.md) for full source details.

## The Multi-Repo Challenge

Fragmented platforms — multiple repositories, multiple teams, shared infrastructure, central orchestration — present C4's hardest scaling problem. Individual systems are easy to model; the relationships between them across repository boundaries are not.

Key challenges:
- No single codebase to derive the full architecture from
- Team ownership is distributed
- Cross-repo dependencies must be explicitly modeled
- System landscape view requires aggregation across teams

## System Landscape as the Entry Point

For fragmented platforms, the **system landscape diagram** is essential. It provides "a map of the software systems within the chosen scope" and operates as "a system context diagram without a specific focus on a particular software system" [6]. This is the portfolio-level view that shows how all services relate.

Scope can be "enterprise/organisation/department/etc." [6], and the audience includes "technical and non-technical people" [6]. This is where platform-level concerns — API gateways, service meshes, shared databases — become visible.

## Modeling Multi-Repo Services

### When services are one system vs. separate systems

The C4 model provides explicit guidance via Conway's Law [5]:

| Situation | C4 Modeling Approach |
|-----------|---------------------|
| One team owns all services | Services as containers within one system [5] |
| Multiple teams own services | Each team's services as separate systems [5] |
| Mixed ownership | Hybrid — some systems contain multiple containers, others are standalone |

"As organizations scale and apply Conway's Law, microservices transition from 'an implementation detail inside a single software system' to separate software systems" [5].

### Cross-repo dependencies

Each software system gets its own context and container diagrams. Cross-system interactions appear in the system landscape and in each system's context diagram showing external systems it depends on.

## Structurizr Enterprise Patterns

Structurizr provides the most mature tooling for multi-repo C4. The recommended approach explicitly warns against the "uber workspace" anti-pattern [18]:

### Anti-Pattern: Uber Workspace

"The Structurizr tooling was never designed to handle workspaces that contain hundreds or thousands of software systems" [18]. Four specific problems:

1. **Scale:** Tooling can't handle hundreds of systems
2. **Ordering:** Imperative DSL parsing creates dependencies and duplication
3. **Single failure:** "An error in any [fragment] will cause the entire workspace generation process to fail" [18]
4. **Restricted autonomy:** Teams can't use advanced features independently

### Recommended: Three-Step Composition

1. **System Catalog:** Extract minimal system definitions (name, description, metadata only) into shared DSL file — no internal architecture details [18]
2. **Workspace Extension:** Teams use `workspace extends` + `!element` to add their system's internal architecture while reusing shared definitions [18]
3. **Centralized Landscape:** `generate system-landscape` aggregates all systems across workspaces [18]

**Key principle:** "Value composition over inheritance" [18]. Keep DSL colocated with source code in team repos. Server as central visibility layer, not single source of truth.

## Handling Platform-Level Concerns

### API Gateways and Service Meshes

These are infrastructure elements that appear differently at different C4 levels:

- **System landscape:** May not appear (infrastructure, not a software system)
- **Container diagram:** API gateway as a container handling external traffic
- **Deployment diagram:** Service mesh sidecars, load balancers, DNS as deployment/infrastructure nodes [7]

### Shared Databases and Message Brokers

Individual topics should be modeled as separate containers rather than treating the entire broker as one monolithic container [12]. This better illustrates point-to-point and pub/sub relationships.

External services like S3 and RDS should "be shown as containers because they are an integral part of your software architecture" [3], even when externally hosted.

### Central Orchestration

Orchestration points (API gateways, workflow engines, event buses) appear as:
- Software systems in the landscape diagram if owned/operated by a platform team
- Containers within a system if part of a specific application
- The choice depends on ownership and operational responsibility

## Managing Complexity at Scale

The fundamental problem: "with serverless, you are deploying your UML collaboration diagram!" [11]. Distributed architectures with many services have lots of elements/relationships at the container level.

### Solution: Focused Diagrams

"Split that single complex diagram into a larger number of simpler diagrams, each with a specific focus" [2]. Options for focus:
- Business area or bounded context
- Individual service + direct dependencies
- Use case or user journey
- Functional grouping

Structurizr DSL supports this via model-driven approach: define the full model once, generate multiple focused views using `include` expressions [11].

### Solution: Shift from Diagramming to Modeling

Brown advocates abandoning general-purpose tools for model + views tooling [11]. "A model is just data" [8] — it enables querying, validation, alternative visualizations, and consistent multi-view generation from a single source of truth.

### Dynamic Diagrams for Orchestration

For complex cross-service interactions, use dynamic diagrams "sparingly to show interesting/recurring patterns or features that require a complicated set of interactions" [9]. These show runtime collaboration sequences across service boundaries.

## Real-World Scale Indicators

ADEO Tech found that with "five different services, more than ten different places injecting data, and more than ten consumers," diagrams become "completely unreadable" [28]. Their solution: filtering to follow entity flows end-to-end without distraction [28].

The Structurizr documentation explicitly states the tooling "was never designed to handle workspaces that contain hundreds or thousands of software systems" [18], suggesting an upper bound on what a single workspace can represent.

## Deployment Diagrams for Platform Architecture

Deployment diagrams are critical for fragmented platforms because "the 4 main diagram types in the C4 model focus on the structure of the architecture, but they don't explain how your software is deployed" [30]. Use cases:
- Scalability assessment and planning
- Cloud migrations
- Disaster recovery strategies
- Infrastructure cost analysis across providers [30]

Create separate deployment diagrams per environment (dev/staging/prod) [7].

## Gaps and Limitations

- No published case studies from large platform companies (Netflix, Amazon, Google) using C4
- Structurizr workspace extension is the only mature multi-repo pattern; limited alternatives
- Cross-repo consistency requires organizational discipline — tooling alone doesn't enforce it
- No automated way to discover cross-repo dependencies and generate landscape diagrams
- Event-driven and saga patterns have limited C4 representation guidance
- Scale limits: no quantitative benchmarks for when C4/Structurizr breaks down
