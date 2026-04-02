# Onboarding and Progressive Disclosure

Covers Dimension 4: how workflow builders handle first-time users, template-based onboarding, guided tours, and progressive complexity.

See [citations.md](../citations.md) for full source details.

## Onboarding Approaches by Platform

| Tool | Primary Onboarding | Template Support | Guided Help |
|------|-------------------|-----------------|-------------|
| n8n | Quickstart with templates + expressions [40] | Workflow templates gallery [40] | Progressive disclosure in node config [13] |
| Zapier | Visual editor with panoramic view [23] | Extensive template library | Step notes, path renaming [23] |
| Power Automate | Template gallery [39] | Browse/search by category, "Send a copy" sharing [39] | Flow checker guidance [37] |
| Retool | Block library + outline tab [1] | Via Blocks tab | Split view for complex editing [1] |

### Template-Based Onboarding

Power Automate's templates are "pre-packaged flows that get you up and running quickly, using popular use cases and saving you loads of time versus building the same thing from scratch" [39]. Users can browse by category, then "tweak templates by adding, editing, or removing triggers and actions to create your own flows" [39].

n8n's quickstart "introduces two key features: workflow templates and expressions" [40], using templates as the entry point for new users.

### Onboarding UX Patterns (General)

Research across 200+ onboarding flows identified 8–14 distinct onboarding types [42][43]:

- **Product tours/walkthroughs**: Show key workflows using tooltips and interactive elements [42]
- **Welcome messages**: "About 9 in 10 new user onboarding sequences begin with a welcome message" [42]
- **Tooltips**: Contextual boxes pointing to specific UI elements [42]
- **Persona-based onboarding**: Users self-segment, each option leads to different first experience [42]
- **In-app guidance**: Layer on top of application for non-disruptive help [42]

Best practice: "Get users to their first win as fast as possible" [43].

## Progressive Disclosure in Workflow Builders

n8n implements progressive disclosure across its interface [13]:
- Beginners access pre-configured node options
- Experts can access JavaScript code nodes and detailed settings
- Three-panel layout: palette (left) → canvas (center) → properties (right, on demand)
- Consistent interaction patterns across node types reduce learning overhead

Nielsen Norman Group defines progressive disclosure as a technique that "defers advanced or rarely used features to a secondary screen, making applications easier to learn and less error-prone" [12]. Proven strategy after 30+ years [12].

Key design rules [12]:
- Max 2 disclosure levels (3+ disorients users)
- Use task analysis and frequency-of-use statistics to prioritize features
- Don't offer multiple paths to secondary options — choose one clear route
- Progressive (importance-based, optional) differs from Staged (sequence-based, required)

## Gaps and Limitations

- No comparative usability studies found measuring onboarding effectiveness across workflow builders.
- Prefect and Airflow onboarding for non-technical users is largely undocumented — both are code-first tools.
- Specific tooltip/guided tour implementations in workflow builders are poorly documented in public sources.
- Agent C (primary researcher for this dimension) was rate-limited; findings supplemented from other agents and general UX sources.
