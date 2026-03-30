# Best Practices

Dimension covering community-validated patterns for using GitHub Issues as a kanban board.

Sources: see [citations.md](../citations.md) for full details.

## Label Taxonomy

The community has converged on a prefix-based labeling system [15]:

| Category | Examples | Rule |
|----------|----------|------|
| Status: | In Progress, Blocked, Review Needed, Abandoned | Only one per issue |
| Type: | Bug, Enhancement, Feature, Question, Documentation | Classifies nature of work |
| Priority: | Critical, High, Medium, Low | Optional; prone to inflation |
| Area: / Component: | frontend, api, database, infra | For mono-repos; identifies affected module |

**Naming convention**: `[Category]: [Specific Label]` (e.g., "Status: In Progress") [15].

Priority labels have a known anti-pattern: "as soon as priority labels are introduced...every issue suddenly becomes 'absolutely-mission-critical'" [15].

## Issue Template Design

GitHub supports two template formats [16]:

| Format | File Type | Best For |
|--------|-----------|----------|
| Markdown templates | `.md` | Simple templates, fewer constraints |
| YAML issue forms | `.yml` | Structured web forms, validation |

Templates stored in `.github/ISSUE_TEMPLATE/` directory [16].

YAML forms support field types: markdown, input, textarea, dropdown (with `multiple: true`), checkboxes, upload [16]. Templates can auto-apply labels and assign users at creation time [16].

Best practice naming: numerical prefixes for ordering (`1-bug.yml`, `2-feature-request.yml`, `3-epic.yml`) [16].

## Triage Process (Kubernetes Model)

The Kubernetes project provides the most mature open-source triage model [17]:

**5-Step Workflow:**

1. **Review** — `needs-triage` label auto-applied to new issues [17]
2. **Categorize** — Support requests (`kind/support`), bugs (validate reproducibility), incomplete (`triage/needs-information`), community (`help wanted`, `good first issue`) [17]
3. **Prioritize** — `priority/critical-urgent` through `priority/backlog` [17]
4. **Route** — Assign SIG label, mention team with `@kubernetes/sig-<name>` [17]
5. **Follow up** — 30-day nudge if no PR, 90-day `lifecycle/stale`, eventual auto-close [17]

## Project Board Configuration

GitHub's official best practices [11]:

- Use @mentions for team accountability
- Create issue dependencies to show blocking relationships
- Decompose large issues into smaller sub-issues
- Maintain project READMEs with purpose and contact info
- Post status updates ("On track" / "At risk")
- Create multiple views (backlog, sprint, roadmap)
- Apply column limits to focus attention
- Use iteration fields for sprint planning

## Milestone Strategy

Two common approaches:

| Strategy | Pattern | Use Case |
|----------|---------|----------|
| Sprint-based | `2026-Q2-Sprint-3` | Time-boxed iterations |
| Version-based | `v1.2.0` | Release coordination |

Milestones group issues planned for completion within a time period, enabling progress tracking and capacity management [11].

## Lifecycle Management

Recommended lifecycle with automation touch-points:

```
New → Triage (needs-triage label auto-applied)
Triage → Backlog (triage/accepted, area/component assigned)
Backlog → In Progress (status field change)
In Progress → Review (PR linked)
Review → Done (PR merged, auto-closes issue via built-in workflow)
Done → Archived (auto-archive after 30/60/90 days)
```

## Naming Conventions That Scale

| Element | Convention |
|---------|-----------|
| Labels | Prefix-based (`Type:`, `Priority:`, `Status:`, `Area:`) [15] |
| Templates | Numbered for ordering (`1-bug.yml`, `2-feature.yml`) [16] |
| Milestones | Version-based or time-based [11] |
| Projects | Product-focused, not repo-focused [11] |

## Gaps and Limitations

- Labels are repository-scoped — changes in one repo don't propagate across the organization [15]
- No standard for label taxonomy exists; different communities use different separators (colon vs slash vs hyphen) [15]
- Auto-add workflows limited to one repository per workflow [18]
- GITHUB_TOKEN cannot access projects — requires GitHub App or PAT [18]
- Limited documentation on triage patterns for teams >100 contributors [17]
