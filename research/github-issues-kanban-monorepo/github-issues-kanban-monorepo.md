# GitHub Issues as a Kanban Board for Multi-User Mono-Repos

A citation-backed analysis of using GitHub Issues and Projects (v2) as a kanban
board for multiple users in a single mono-repo. Covers best practices, what works
well, risks and tensions, and automation via tooling and agentic AI capabilities.

Two independent review agents audited this document — one verified every cited URL
against source content, the other checked numerical and logical consistency across
files.

## Methodology

Research conducted 2026-03-30 across 8 dimensions with 39 sources spanning GitHub
official documentation (Tier 2), open-source project documentation (Tier 1-2),
and practitioner case studies (Tier 3-4). See [citations.md](citations.md) for
the complete source list.

---

## 1. How It Works: GitHub Projects v2 Kanban Mechanics

GitHub Projects v2 provides three view types — table, board (kanban), and roadmap
— with a shared metadata layer of up to **50 custom fields** [1]. Board columns
are driven by a single select or iteration field; dragging items between columns
automatically updates the field value [3].

### Key Capabilities

| Feature | Details |
|---------|---------|
| Column fields | Single select or iteration [3] |
| Swimlanes | Horizontal grouping by any field (team, priority) [3] |
| Column limits | Advisory display only, not enforced [3] |
| Filtering | AND across fields, OR within same field, no cross-field OR [4] |
| Item limit | 50,000 (expanded from 1,200 in Feb 2024) [5] |
| Dependencies | Blocked by / Blocking (GA Aug 2025) [7][8] |
| Sub-issues | Public beta Oct 2024 (parent-child, one parent per issue) [9] |

### Built-in Automations

Two workflows are enabled by default: status→Done on issue close, and
status→Done on PR merge [2]. Additional automations include auto-archive,
auto-add from repos, and auto-set status on item addition [2]. Built-in
automations focus on lifecycle events; there are no configurable transition
rules restricting which statuses can change to which others [2].

### Notable Limitations

- No cross-field OR filtering [4]
- No multi-select custom fields [1]
- No private/personal views — all views visible to project members (GitHub community discussions report this limitation but no single authoritative source documents it)
- Sorting disables manual reorder within columns [3]
- Cannot group/slice/sort by title, labels, reviewers, or linked PRs [3]

See [references/kanban-mechanics.md](references/kanban-mechanics.md) for full
details.

---

## 2. Multi-User Collaboration: What Works and What Doesn't

### What Works

**Assignment**: Up to 10 assignees per issue/PR [10], sufficient for most team
sizes. GitHub's best practices recommend @mentions for accountability, issue
dependencies for blocking relationships, and status updates for project health
visibility [11].

**Views**: Team-specific filtered views by assignee, label, or repository
provide focused perspectives on shared boards [4]. The `@me` filter keyword
gives each user a personal work view without configuration [4].

**CODEOWNERS**: Maps directory paths to teams for automatic PR reviewer
assignment [13]. Essential for mono-repos with multiple teams owning different
packages.

### What Doesn't Work

**Team-based assignment**: Teams can only be assigned as PR reviewers, not as
issue assignees [10]. No filtering by GitHub Team membership exists in search
or Projects [12].

**Multi-team coordination**: GitHub community discussion on managing multiple
teams with Projects V2 remained unanswered after 60 days, suggesting no
established best practice exists [12]. The two obvious approaches — separate
projects per team (metadata doesn't sync) vs. single unified project
(scalability concerns) — both have significant drawbacks [12].

**View privacy**: All views are visible to everyone with project access.
Teams cannot create private views, leading to view clutter in large
organizations. (Widely reported in GitHub community discussions; no single
authoritative source.)

### Team Size Friction Points

| Size | Experience |
|------|-----------|
| 2-5 devs | Minimal friction; informal communication suffices |
| 5-15 devs | Boundary confusion emerges; need explicit CODEOWNERS [13], label conventions |
| 15+ devs | Exponential communication paths; heavy tooling investment required |

Microsoft scaled to 25,000 engineers on GitHub, but required significant tooling
and process investment [14] (source inaccessible; claim from search snippets
only). One practitioner source suggests most teams under 30 developers never
need to switch from GitHub Projects [24].

See [references/multi-user-patterns.md](references/multi-user-patterns.md) for
full details.

---

## 3. Best Practices

### Label Taxonomy

The community has converged on prefix-based labels [15]:

```
Type: Bug          Type: Feature       Type: Documentation
Priority: High     Priority: Medium    Priority: Low
Status: In Progress   Status: Blocked   Status: Review Needed
Area: api          Area: frontend      Area: shared
```

Only one status label per issue. Priority labels are prone to inflation ("every
issue suddenly becomes critical") [15]. Labels are repository-scoped and do not
propagate across the organization [15].

### Issue Templates

YAML issue forms (`.github/ISSUE_TEMPLATE/*.yml`) provide structured web forms
with supported field types: text inputs, textareas, dropdowns (with multi-select),
checkboxes, and file uploads [16]. Templates can auto-apply labels and assign
users at creation [16].

### Triage Process

The Kubernetes model provides the most mature open-source triage framework [17]:

1. `needs-triage` label auto-applied to new issues
2. Categorize: support request, bug, incomplete, community contribution
3. Prioritize: `priority/critical-urgent` through `priority/backlog`
4. Route: assign SIG label, mention team
5. Follow up: 30-day nudge, 90-day `lifecycle/stale`, eventual auto-close

### Issue Lifecycle

```
New → Triage (needs-triage auto-applied)
  → Backlog (triage/accepted, area assigned)
  → In Progress (status change)
  → Review (PR linked)
  → Done (PR merged, auto-closes issue) [2]
  → Archived (auto-archive after configurable period) [2]
```

See [references/best-practices.md](references/best-practices.md) for full
details.

---

## 4. Risks and Tensions

### High-Impact Risks

**Flat hierarchy**: No native epics or multi-level task breakdown [19][20].
Sub-issues (Oct 2024 beta) support one parent per issue but not many-to-many
relationships [7]. Teams needing SAFe-style hierarchies will find GitHub
insufficient.

**Notification fatigue**: Active mono-repos generate overwhelming notification
volume. The common failure mode is "notification bankruptcy" — users disable
notifications entirely, then miss critical updates. (Widely reported in GitHub
community discussions and practitioner blogs; no single authoritative source.)

**Permission granularity**: To close issues or add labels, users need write
access to the entire repository [13]. No issues-only permissions exist.
CODEOWNERS requires write access, not the triage role [13].

**No native reporting**: GitHub lacks velocity charts, burndown diagrams,
cycle time analytics, or throughput metrics [20][24]. Third-party tools fill
the gap but add cost and integration overhead.

### Mono-Repo-Specific Risks

**Ownership ambiguity**: Mono-repos with shared access suffer from unclear
ownership boundaries [34]. CODEOWNERS only affects PR reviews, not issue
routing [13].

**Cross-cutting concerns**: Issues spanning multiple packages have no native
mechanism for tracking impact across areas [12].

**Label chaos**: GitHub labels are repository-scoped. Without discipline,
taxonomy fragments across teams [15].

### Common Failure Modes

1. Cross-team coordination collapse → teams lose visibility across areas [12]
2. Notification bankruptcy → critical updates missed
3. Permission friction → write-access requirements conflict with least-privilege [13]
4. Analytics blindness → no velocity data for planning [24]
5. Backlog rot → issues accumulate without triage [21]
6. Automation limits → GITHUB_TOKEN cannot access Projects, workflows are repo-specific [18]

See [references/risks-and-tensions.md](references/risks-and-tensions.md) for
full details.

---

## 5. Tooling Automation

### Built-in Automations

| Automation | Mechanism |
|-----------|-----------|
| Status transitions | Built-in workflows (close→Done, merge→Done) [2] |
| Stale management | `actions/stale` (60-day mark, 7-day close default) [21] |
| Auto-add to project | `actions/add-to-project` (requires GitHub App or PAT) [18] |
| Project field updates | GraphQL API mutations [18] |
| Auto-labeling | `github/issue-labeler` (regex on issue body) |

### IssueOps Pattern

IssueOps treats issues as control interfaces for operational workflows [22].
The finite-state machine framework uses issue state, labels, and comments as
triggers for GitHub Actions [22]. Use cases: deployment gates, approval
workflows, resource provisioning. Benefits: immutable audit trails, full
transparency [22].

### Key Constraints

- `GITHUB_TOKEN` cannot access Projects (scoped to repo only) — every
  project automation requires a GitHub App or PAT [18]
- Auto-add workflows limited to one repo per workflow [18]
- Projects span repos but workflows are repo-specific [18]
- `actions/stale` rate-limits at 30 operations/run by default [21]

See [references/tooling-automation.md](references/tooling-automation.md) for
full details.

---

## 6. Agentic Automation

### Current Capabilities

| Tool | Issue Integration | Maturity |
|------|------------------|----------|
| **Claude Code** [25] | @claude in issues/PRs → creates PRs, reviews code | GA (v1) |
| **GitHub Copilot** [26] | Assign issues to Copilot → draft PR, writes code, runs tests | GA |
| **GitHub Agentic Workflows** [27] | Markdown-authored auto-triage, labeling, routing | Technical Preview |
| **Cursor** [28] | No native GitHub Issues integration | N/A |

### Claude Code Integration

Claude Code responds to `@claude` mentions in issues and PRs [25]. It creates
complete PRs from issue descriptions, follows `CLAUDE.md` project guidelines,
and supports custom automation via scheduled workflows [25]. Configuration
requires the Claude GitHub App with read/write permissions for contents, issues,
and PRs [25].

### GitHub Copilot Coding Agent

Issues can be assigned directly to Copilot [26]. The agent creates a draft PR,
explores repository context, writes code, runs tests, and requests human review
[26]. Security controls: pushes only to `copilot/*` branches, cannot
approve/merge own work, sandboxed with limited internet access [26].

### GitHub Agentic Workflows

Launched in technical preview February 2026 [27]. Workflows are authored in
plain Markdown and executed by coding agents in GitHub Actions [27].
Capabilities include automatic issue triage (summarize, label, route),
documentation updates, code quality improvements, and repository health
reports [27]. Read-only by default; write operations require explicit approval
[27].

### Kanban as Agent Task Queue

An emerging pattern treats kanban boards as task queues for AI agents. Vibe
Kanban [40] orchestrates 9 AI agents (Claude Code, Cursor, Copilot, Gemini,
ChatGPT, Amp, Aider, OpenCode, Windsurf) in parallel using automated git
worktree creation, with a Plan → Prompt → Review workflow. The platform
reports 30,000+ active users and 100,000+ PRs created [40]. VS Code Agent
Kanban provides 'plan'/'implement' verbs for Copilot with task tracking.

### Practical Workflow: Issue → AI → PR

```
1. User creates issue with acceptance criteria
2. Issue auto-labeled and triaged (Agentic Workflows) [27]
3. Issue assigned to AI agent (Copilot or @claude) [25][26]
4. Agent creates draft PR, implements changes, runs tests [25][26]
5. Human reviews and merges (agents cannot self-approve) [26]
6. Issue auto-closed via built-in workflow [2]
```

See [references/agentic-automation.md](references/agentic-automation.md) for
full details.

---

## 7. Comparison with Dedicated Tools

### Feature Gap Summary

| Capability | GitHub Projects | Jira |
|-----------|----------------|------|
| Pricing | Free with GitHub [24] | $7.53/user/month [24] |
| Kanban | Yes [1] | Yes |
| Scrum (velocity, burndown) | No [24] | Yes |
| Hierarchy | Sub-issues (beta) [9] | Full (Epic→Story→Subtask) |
| Custom workflows | Actions required [2] | Built-in state machines |
| Reporting | Minimal [24] | Advanced analytics |
| Dependencies | Basic (2 types) [7][8] | Full (multiple types, cross-project) |
| Marketplace | Growing | 5,000+ apps [31] |

### Decision Framework

**Stay with GitHub Projects when**:
- Team under 20-30 developers [24]
- Work is primarily code-centric [24]
- Simple kanban/sprint tracking suffices [24]
- Zero context-switching between code and PM is valued [24]
- Budget constraints favor free tooling [24]

**Consider dedicated tools when**:
- Team exceeds 30 developers [24]
- Non-technical stakeholders need regular access [20]
- Advanced Agile metrics required (velocity, burndown) [24]
- Multi-level hierarchy needed (epics, stories, subtasks) [19]
- Formal workflow enforcement required [2]

### Migration Stories

Open-source projects (Spring Framework, Apache Accumulo) have migrated FROM Jira
TO GitHub Issues, citing single-platform simplicity, markdown, and reduced
contributor friction [29][30]. The most painful aspect was markup conversion [29].

GitHub is actively closing feature gaps: dependencies (GA Aug 2025 [7]),
sub-issues (beta Oct 2024 [9]), expanded limits (50,000 items [5]), and Agentic
Workflows (preview Feb 2026 [27]).

See [references/comparison-with-dedicated-tools.md](references/comparison-with-dedicated-tools.md)
for full details.

---

## 8. Mono-Repo-Specific Considerations

### CODEOWNERS: Power and Limits

CODEOWNERS maps paths to teams for automatic PR reviewer assignment [13]. It is
the primary ownership signal in a mono-repo but **does not affect issue routing**
[13]. Teams must build separate automation for issue-to-team routing.

### Label Strategy for Packages

Use area/component labels to identify affected modules [15]:

```
Area: api            Area: frontend       Area: shared
Area: infrastructure Area: docs           Area: cli
```

Auto-labeling for PRs: `monorepo-pr-repo-labeler` action labels PRs by changed
file paths. For issues, custom Actions or AI triage can apply labels based on
content analysis [27].

### CI Integration

Mono-repo build tools (Nx, Turborepo, Bazel) provide affected-package detection,
but this data doesn't feed into GitHub Issues natively [33]. Teams must build
custom workflows to surface CI results in issue metadata.

GitHub Actions path filters enable subdirectory-based triggers for selective
CI per package [33].

### Notification Routing

Monorobot (by Ahrefs) solves mono-repo notification routing [35]:
- Routes GitHub notifications to Slack channels by file prefix
- Filters by issue/PR labels and CI build status
- Maps GitHub handles to Slack users

### Large-Scale Examples

**Kubernetes** [36] found that "a large monorepo works for Google, but not on
GitHub" — citing ACLs, notification management, and issue triage as velocity
limiters. They use SIG-based labels (`sig/architecture`, `area/code-organization`)
and Peribolos for team permission management.

See [references/monorepo-considerations.md](references/monorepo-considerations.md)
for full details.

---

## Key Recommendations

### For Teams Starting Out (2-15 developers)

1. **Set up CODEOWNERS** mapping package paths to teams [13]
2. **Adopt prefix-based labels**: `Type:`, `Priority:`, `Status:`, `Area:` [15]
3. **Create YAML issue templates** with auto-labeling [16]
4. **Enable built-in automations**: close→Done, merge→Done [2]
5. **Install `actions/stale`** to prevent backlog rot [21]
6. **Configure Claude Code or Copilot** for @mention-triggered automation [25][26]

### For Growing Teams (15-30 developers)

7. **Implement Kubernetes-style triage** with `needs-triage` label workflow [17]
8. **Add Monorobot** or equivalent for notification routing by file prefix [35]
9. **Set up GitHub Agentic Workflows** for automated issue triage [27]
10. **Create team-specific filtered views** in Projects [4]
11. **Evaluate whether GitHub still suffices** — 20-30 developers is the transition zone [24]

### For Large Teams (30+ developers)

12. **Seriously evaluate dedicated tools** (Jira, Linear) for hierarchy and reporting [24]
13. **If staying on GitHub**: invest in custom Actions, GraphQL automation, and third-party analytics [18]
14. **Use IssueOps pattern** for structured operational workflows [22]
15. **Build cross-package impact automation** linking CI results to issue metadata

### Automation Priority Order

| Priority | Automation | Tool |
|----------|-----------|------|
| 1 | Auto-close via PR link | Built-in workflow [2] |
| 2 | Stale issue management | `actions/stale` [21] |
| 3 | Auto-label by file path | `monorepo-pr-repo-labeler` |
| 4 | Auto-add to project | `actions/add-to-project` [18] |
| 5 | AI triage (label, route, summarize) | Agentic Workflows [27] |
| 6 | Issue-to-PR automation | Claude Code or Copilot [25][26] |

---

## Limitations of This Research

- **Microsoft scaling case study** [14] was inaccessible (ECONNREFUSED) — claims about 25K-engineer scaling come from discovery agent snippets only
- **Spring Framework migration** [29] source returned JavaScript-only page — migration details from search snippets only
- No peer-reviewed academic studies found on GitHub Issues kanban effectiveness
- Team size thresholds (20-30 developers) are consistent across sources but qualitative, not statistically derived
- Agentic automation space is rapidly evolving — capabilities described may change significantly within months
- Most comparison data predates GitHub's 2024-2025 feature additions (dependencies, sub-issues, expanded limits)

---

## Supporting Files

- [citations.md](citations.md) — All 39 sources with extracted data
- [references/kanban-mechanics.md](references/kanban-mechanics.md) — Projects v2 feature details
- [references/multi-user-patterns.md](references/multi-user-patterns.md) — Team collaboration patterns
- [references/best-practices.md](references/best-practices.md) — Labels, templates, triage
- [references/risks-and-tensions.md](references/risks-and-tensions.md) — Pain points and failure modes
- [references/tooling-automation.md](references/tooling-automation.md) — Actions, bots, CLI tools
- [references/agentic-automation.md](references/agentic-automation.md) — AI agent integration
- [references/comparison-with-dedicated-tools.md](references/comparison-with-dedicated-tools.md) — GitHub vs Jira/Linear
- [references/monorepo-considerations.md](references/monorepo-considerations.md) — Mono-repo-specific challenges
- [audit/citation-audit.md](audit/citation-audit.md) — Independent citation verification
- [audit/consistency-review.md](audit/consistency-review.md) — Cross-file consistency check
