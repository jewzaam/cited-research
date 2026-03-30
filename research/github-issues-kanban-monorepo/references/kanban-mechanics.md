# Kanban Mechanics

Dimension covering how GitHub Projects (v2) functions as a kanban board system.

Sources: see [citations.md](../citations.md) for full details.

## Views and Layouts

GitHub Projects v2 offers three view types [1]:

| View | Purpose | Key Feature |
|------|---------|-------------|
| Table | High-density data display | Grouping, field visibility controls |
| Board | Kanban columns | Drag-and-drop status transitions |
| Roadmap | Timeline visualization | Iteration/date field integration |

## Board View Configuration

Board columns are driven by a single select or iteration field [3]. When items are dragged between columns, the underlying field value updates automatically [3].

**Swimlanes** provide horizontal grouping by field values (team, priority, urgency) [3]. Items dragged to a new group automatically adopt that group's field value [3].

**Column limits** are advisory only — they display current vs. maximum counts but do not prevent exceeding the threshold [3].

**Sorting constraint**: when a board is sorted, manual reordering within columns is disabled [3].

**Cannot group, slice, or sort by**: title, labels, reviewers, or linked pull requests [3].

## Custom Fields

Projects support up to **50 fields total** (built-in + custom) [1]. Available types:

| Type | Use Case |
|------|----------|
| Text | Notes, descriptions |
| Number | Complexity, story points |
| Date | Ship dates, deadlines |
| Single Select | Status, priority (colored options) |
| Iteration | Sprint/cycle planning with break support |

No multi-select field type exists [1].

## Filtering

Multiple filters combine as logical AND [4]. Comma-separated values within the same field act as OR [4]. **No cross-field OR is supported** [4].

Key qualifiers: `assignee:`, `label:`, `repo:`, `is:state`, `has:`/`no:` for field existence [4]. Special keywords: `@me` (current user), `@current`/`@previous`/`@next` (iterations), `@today` with arithmetic [4].

## Built-in Automations

Two workflows enabled by default [2]:

1. Status → "Done" when issues/PRs are closed
2. Status → "Done" when PRs are merged

Additional built-in automations [2]:
- Auto-archive items meeting specified criteria
- Auto-add items from repositories matching filters
- Auto-set status to "Todo" when items are added

Built-in automations focus on lifecycle events; no configurable transition rules restrict which statuses can change to which others [2].

## Item Limits

| Metric | Limit |
|--------|-------|
| Items per project (original) | 1,200 [5][6] |
| Items per project (expanded, Feb 2024) | 50,000 (soft limit, expandable) [5] |
| Archive capacity | 10,000 items [6] |
| Fields per project | 50 [1] |

The 1,200 limit was set to "keep projects snappy and encourage tracking of only active work" [6]. Community pushback cited undocumented constraints and cross-repo tracking needs [6].

## Dependencies

Issue dependencies became GA in August 2025 [7]. Two relationship types [8]:

- **Blocked by**: issue depends on another being completed
- **Blocking**: issue prevents another from completion

Blocked issues display a "Blocked" icon on project boards [8]. Dependencies were a long-standing community request — sub-issues (parent-child, one parent per issue) do not address many-to-many blocking needs [7].

Community continues requesting additional relationship types: "relates to," "duplicates," "documents" [7].

## Issue Hierarchy (Sub-Issues)

GitHub's tasklists feature (for epic-like hierarchies) was closed as "not planned" and replaced by **sub-issues**, which entered public beta in October 2024 [9]. Migration from tasklists to sub-issues is planned [9].

## Gaps and Limitations

- No cross-field OR filtering [4]
- No multi-select custom fields [1]
- No private/personal views — all views visible to everyone with project access (widely reported in community discussions)
- No view-level permissions (widely reported in community discussions)
- No custom field change history in issue timelines (widely reported in community discussions)
- Column limits are advisory only, not enforced [3]
- Sorting disables manual reorder within columns [3]
