# Tooling Automation

Dimension covering GitHub Actions, bots, CLI, and third-party tools for automating issue lifecycle.

Sources: see [citations.md](../citations.md) for full details.

## GitHub Projects Built-in Automations

Two workflows enabled by default [2]:

| Trigger | Action |
|---------|--------|
| Issue/PR closed | Status → "Done" |
| PR merged | Status → "Done" |

Additional built-in automations [2]:
- Auto-set status to "Todo" when items are added
- Auto-archive items meeting criteria
- Auto-add items from repositories matching filters

**Limitation**: Built-in workflows are limited to status field changes tied to issue/PR lifecycle events. Custom field automation requires GitHub Actions [2].

## GitHub Actions for Issue Management

### actions/add-to-project
Official GitHub action for automatically adding issues/PRs to projects [18][23]. Key constraint: `GITHUB_TOKEN` is scoped to repository level and **cannot access projects** — requires a GitHub App or PAT with `project` scope [18].

### actions/stale
De facto standard for managing inactive issues [21]:

| Setting | Default | Purpose |
|---------|---------|---------|
| days-before-stale | 60 | Idle days before marking stale |
| days-before-close | 7 | Days after stale before closure |
| operations-per-run | 30 | API rate limit protection |
| close-issue-reason | not_planned | Configurable: completed or not_planned |

Supports exemptions by label, milestone, assignee, and draft PR status [21].

### GraphQL API for Projects

Core mutations for project automation [18]:
- `addProjectV2ItemById` — add items to projects
- `updateProjectV2ItemFieldValue` — set field values (status, dates)
- `archiveProjectV2Item` — archive items
- `createProjectV2Field` — create custom fields

Authentication requires `read:project` scope for queries, `project` scope for mutations [18].

## IssueOps Pattern

IssueOps uses GitHub Issues as an interface for triggering automation workflows [22]:

- **Concept**: Issues, Actions, and PRs serve as control interfaces for CI/CD and operational tasks
- **Framework**: Finite-state machine with states, events, transitions, guards, and actions [22]
- **Triggers**: Opening issues, adding labels, posting comments
- **Benefits**: Immutable audit trails in issue timelines, customizable workflows, transparency [22]

Use cases: deployment gates, team membership approvals, resource provisioning [22].

## Stale Issue Management

The `actions/stale` workflow [21]:
1. Auto-applies "Stale" label after configurable inactivity period (default 60 days)
2. Posts comment notifying contributors
3. Closes issue after additional period (default 7 days) if no activity
4. Removes stale label if activity resumes
5. Rate-limits API operations (default 30/run) to avoid GitHub rate limits

## Webhook-Based Automation

GitHub supports 73+ webhook events covering the complete issue lifecycle. Common patterns:
- Slack notifications on issue events
- External system synchronization (Jira, Linear)
- Deployment triggers from issue state changes

## Auto-Labeling

GitHub's `github/issue-labeler` action applies labels based on issue body content using regex patterns. For mono-repos, the `monorepo-pr-repo-labeler` action automatically labels PRs with affected modules based on changed file paths.

## Key Constraints

| Constraint | Impact |
|-----------|--------|
| GITHUB_TOKEN cannot access projects [18] | Every project automation needs GitHub App or PAT |
| Auto-add limited to one repo per workflow [18] | Mono-repos need per-component workflow files |
| Workflows are repo-specific [18] | Projects spanning repos require duplicate workflows |
| 30 operations/run default for stale action [21] | Large repos need multiple runs to process backlog |

## Gaps and Limitations

- No native workflow state machine for enforcing transitions [2]
- Limited automation triggers compared to dedicated PM tools [2]
- GitHub Actions rate limits constrain high-volume automation [21]
- No built-in automation for cross-project field synchronization [12]
