# Visual Workflow Builder UX Patterns

A citation-backed analysis of UX patterns across production workflow builders (n8n, Retool, Zapier, Power Automate, Prefect, Airflow) covering interaction design, complexity management, cognitive load, onboarding, validation, versioning, and accessibility.

## Key Findings

| Dimension | Dominant Pattern | Notable Innovation | Industry Gap |
|-----------|-----------------|-------------------|--------------|
| Interaction | Left-side palette with search | React Flow add-on-edge-drop | No touch/mobile patterns |
| Complexity | Sub-workflows + TaskGroups | Prefect's 4 composition patterns | No scale threshold data |
| Cognitive Load | Progressive disclosure | n8n's three-panel layout | No production UX studies |
| Onboarding | Template-based start | Zapier's panoramic path view | No comparative studies |
| Validation | Power Automate Flow Checker | Zapier AI-powered troubleshooting | No connection type checking |
| Versioning | Draft/Publish + auto-versioning | Airflow 3 structural detection | No visual workflow diff |
| Accessibility | React Flow built-in a11y | React Aria accessible D&D | No WCAG audit published |

## Decision Framework

1. **Choose your layout algorithm based on complexity**: d3-hierarchy for linear flows, Dagre for moderate branching, ELK.js for complex interactive workflows (57× size trade-off).

2. **Implement progressive disclosure from day one**: Max 2 levels. Show essential options initially; defer advanced configuration to panels opened on demand.

3. **Use the draft/publish model**: Every major platform separates editing from production execution. Auto-save to draft; explicit publish for activation.

4. **Build on React Flow for accessibility**: Provides Tab/Enter/Escape keyboard navigation, ARIA labels, and auto-pan out of the box. Supplement with React Aria for accessible drag-and-drop.

5. **Plan for visual diff early**: No platform has solved visual workflow comparison. This is the largest gap and potential differentiator.

## Files

- [Full analysis](visual-workflow-builder-ux.md) — Complete deliverable with methodology
- [Citations](citations.md) — All 49 numbered sources
- **References/**
  - [Interaction patterns](references/interaction-patterns.md)
  - [Complexity management](references/complexity-management.md)
  - [Cognitive load & learnability](references/cognitive-load-learnability.md)
  - [Onboarding & progressive disclosure](references/onboarding-progressive-disclosure.md)
  - [Validation UX](references/validation-ux.md)
  - [Versioning & collaboration](references/versioning-collaboration.md)
  - [Accessibility](references/accessibility.md)
- **Audit/**
  - [Citation audit](audit/citation-audit.md)
  - [Consistency review](audit/consistency-review.md)
