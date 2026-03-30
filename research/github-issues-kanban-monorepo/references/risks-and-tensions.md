# Risks and Tensions

Dimension covering known pain points of using GitHub Issues as a kanban board.

Sources: see [citations.md](../citations.md) for full details.

## Hierarchy and Structure

GitHub Issues have a **flat structure** with no native epics, parent-child relationships, or multi-level task breakdown [19][20]. The community has strongly demanded nested issues — requests include "infinite sublevels" and SAFe-style Epics→Capabilities→Features→Stories [19].

**Current state**: Tasklists were introduced then abandoned ("not planned"), replaced by sub-issues (public beta Oct 2024) [9]. Sub-issues support one parent per issue but do not address many-to-many dependency relationships [7].

## Notification Fatigue

GitHub's notification system creates overwhelming noise for active projects. Clicking notifications removes them even if work remains. The notifications page becomes unmanageable with dozens of items. Issues waiting for responses fall off the list without tracking [20].

**Common failure mode**: users disable notifications entirely, then miss critical updates ("notification bankruptcy").

## Cross-Cutting Concerns

GitHub Issues are **repository-scoped**, creating challenges for work spanning multiple areas within a mono-repo or across repositories [12][20]:
- Draft items in Projects cannot be assigned milestones or labels (which are repo-level) [12]
- No unified backlog view across repos without Projects [20]
- Teams working across functional areas cannot track a single story across boundaries without manual overhead [12]

## Ownership Ambiguity

In mono-repos where everyone has access to everything, ownership becomes unclear [34]. GitHub lacks native team ownership indicators on repositories [12]. In large organizations, users cannot easily identify which team owns code or whom to ask for access.

## Scaling Limits

| Constraint | Limit | Impact |
|-----------|-------|--------|
| Items per project | 1,200 (now 50,000 beta) [5][6] | Forces archiving or splitting projects |
| Teams per organization | 1,500 [12] | Blocks large enterprises |
| Repos per project auto-add | 1 per workflow [18] | Requires per-repo workflow files |
| Assignees per issue | 10 [10] | Insufficient for large team assignment |
| CODEOWNERS file | 3 MB max [13] | Large mono-repos may exceed |

## Dependencies and Blocking

Dependencies became GA August 2025 [7], but significant limitations remain:
- Only two relationship types: blocked by, blocking [8]
- No "relates to," "duplicates," or other relationship types [7]
- Cross-repository dependency support unclear from documentation [8]
- Historical workarounds: milestone-per-dependency or comment mentions with no programmatic tracking [7]

## Limited Reporting and Metrics

GitHub lacks native [20][24]:
- Velocity charts
- Burndown diagrams
- Cycle time analytics
- Throughput reporting
- Sprint metrics

Third-party tools (Screenful, ZenHub, Swarmia) fill the void but add cost and integration overhead [24].

## Permission Granularity

GitHub's permission model is coarse-grained [13]:
- To close issues or add labels, users need **write access to the entire repository** [13]
- No issues-only access permissions exist [13]
- Custom roles require Enterprise accounts [13]
- CODEOWNERS requires write access, not triage role [13]
- Fork-based workflows conflict with issue management permissions [13]

## Workflow Enforcement

No built-in workflow state machines exist [2]. Any status can change to any other status — no transition rules, required approvals, or guard conditions [2]. Teams wanting structured workflows must build them via GitHub Actions [18].

## Label Management at Scale

Labels are repository-scoped [15]:
- Changes in one repo don't propagate across the organization
- No organization-wide label management
- Teams must manually maintain naming convention discipline
- Too many labels create visual clutter

## Common Failure Modes

1. **Cross-team coordination collapse** — work spanning areas becomes untrackable, teams revert to spreadsheets [12]
2. **Notification bankruptcy** — users disable notifications to maintain sanity [20]
3. **Permission gridlock** — fork-based workflows conflict with issue management [13]
4. **Analytics blindness** — no native metrics means management cannot assess velocity [20][24]
5. **Ownership confusion** — in mono-repos, unclear responsibility for issues [34]
6. **Label chaos** — inconsistent labeling across repos fragments taxonomy [15]
7. **Backlog rot** — issues accumulate indefinitely without triage mechanisms [21]
8. **Automation exhaustion** — workflow limits hit at enterprise scale [18]

## Gaps and Limitations

- No quantitative threshold data for when teams typically outgrow GitHub Issues
- No systematic study of migration triggers
- Limited data on notification volume by team size
- Dependency feature still lacks cross-repo support clarity [8]
