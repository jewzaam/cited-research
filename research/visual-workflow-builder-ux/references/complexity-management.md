# Complexity Management

Covers Dimension 2: grouping/collapsing, sub-workflows, conditional branching, parallel execution, and large workflow handling.

See [citations.md](../citations.md) for full source details.

## Node Grouping and Collapsing

| Tool | Mechanism | Behavior |
|------|-----------|----------|
| Airflow | TaskGroup | "Organize tasks into hierarchical groups in Graph view... useful for creating repeating patterns and cutting down visual clutter" [10] |
| React Flow | useExpandCollapse hook | Maintains "complete graph structure while only rendering the currently visible portions" [32] |
| Retool | Expand/Collapse all | Layout control toggles block visibility [1] |
| Power Automate Desktop | Subflow tabs | "Subflows are separated into tabs to help design large, complex flows" [34] |

React Flow's expand/collapse pattern tracks expanded/collapsed state in node data properties. Dynamic node addition triggers automatic layout recalculation via dagre integration [32].

Airflow TaskGroups keep tasks on the same DAG with uniform settings. Child tasks/TaskGroups are prefixed with parent's group_id by default [10].

## Sub-Workflow / Nested Workflow Approaches

| Tool | Mechanism | Execution Model |
|------|-----------|-----------------|
| n8n | Execute Sub-workflow node | Fire-and-Forget or wait-for-completion [41] |
| Prefect | Nested @flow calls | "Nested flow runs block execution of the parent flow run until completion" [9] |
| Prefect | Deployment triggers | Separate infrastructure, independent cancellation [9][21] |

### Prefect's Four Composition Patterns [21]

1. **Monoflow**: Single flow, sequential tasks — "simple to set up and maintain; only two abstraction levels" [21]
2. **Flow of Subflows**: Nested flows in same process — "facilitates clear ownership boundaries and code reuse" [21]
3. **Flow of Deployments**: Separate infrastructure — "treats deployed flows like external services" [21]
4. **Event-Triggered Flows**: State change events — "achieves conceptual, execution, and awareness separation" [21]

Key limitation: "A nested flow run cannot be cancelled without cancelling its parent flow run" [9].

## Conditional Branching Visualization

| Tool | Pattern | Visual Approach |
|------|---------|-----------------|
| Retool | If/Else/Else-if blocks | Green highlighting for true condition during testing [7] |
| Zapier | Paths | Panoramic view showing all paths simultaneously, up to 5 primary + 3 nested [23] |
| Slack | Visual switch statement | Color-coded branches, up to 10 rules + fallback, drag-and-drop reordering [22] |
| Make.com | Router module | Sequential route evaluation, fallback route, "select whole branch" function [31] |
| Airflow | Edge labels | `Label("When empty")` clarifies "conditions under which certain branches might run" [10] |

Retool Branch blocks provide "a visual alternative to traditional JavaScript if...else statements" where "the condition that evaluates as true is highlighted in green" during testing [7]. Each conditional statement has "its own connector for connecting different blocks" [7].

Zapier's visual editor displays branching through "a panoramic view that shows all the different paths an automation could take" — "beta users overwhelmingly said the new Editor was easier to use—especially when building Zaps with paths" [23].

Slack's conditional branching is designed as "a visual switch statement, built for the millions of builders who don't necessarily think of themselves as programmers" [22].

## Parallel Execution Path Visualization

Power Automate supports parallel branches with connecting lines showing control flow [34]. Airflow's Gantt chart view shows "when each task started, how long it ran, and where tasks ran in parallel" and is "excellent for identifying bottlenecks in your pipeline" [27].

Retool blocks with two inputs execute after both complete, and loop blocks support parallel mode [1].

## Large Workflow Handling

| Approach | Tool | Details |
|----------|------|---------|
| TaskGroup collapsing | Airflow | Hierarchical groups reduce visual clutter [10] |
| Subflow tabs | Power Automate | Separate tabs for large flows [34] |
| Lazy rendering | Synergy Codes | "Renders only visible diagram elements in real-time" [18] |
| Expand/collapse | React Flow | Renders only visible portions of graph [32] |
| Autolayout | Retool | Automatically positions blocks [1] |

Airflow recommends: "try and keep the topology (the layout) of your Dag tasks relatively stable; dynamic Dags are usually better used for dynamically loading configuration options" [10].

## Gaps and Limitations

- No quantitative data found on performance degradation thresholds (at what node count do editors slow down).
- Nested workflow depth limits are not documented across platforms.
- Visual density vs comprehension research specific to workflow builders was not found.
