# GitHub Issues as Kanban for Multi-User Mono-Repos

Citation-backed research on using GitHub Issues and Projects (v2) as a kanban
board for multiple users in a single mono-repo. Covers mechanics, best practices,
risks, tooling automation, and agentic AI capabilities.

## TL;DR

GitHub Projects v2 provides a competent kanban system for teams under 20-30
developers. Beyond that threshold, the lack of hierarchy, reporting, and
permission granularity creates friction that dedicated tools (Jira, Linear) handle
natively. Mono-repos add unique challenges — CODEOWNERS only affects PRs (not
issues), labels are repo-scoped, and notification noise scales with contributor
count.

The strongest use case is developer-centric teams that value zero
context-switching between code and project management. The weakest is teams
needing cross-project portfolio visibility, Agile metrics, or non-technical
stakeholder access.

AI agent integration (Claude Code, GitHub Copilot, Agentic Workflows) is
closing the automation gap fast — issue-to-PR workflows now work with a single
@mention or assignment.

## Quick Decision Framework

1. **Team size under 20?** GitHub Projects likely sufficient.
2. **Need velocity/burndown charts?** Consider Jira or Linear.
3. **Multiple packages in mono-repo?** Set up CODEOWNERS + Area: labels + Monorobot.
4. **Want AI automation?** Configure Claude Code (@claude) or Copilot assignment.
5. **Over 30 developers?** Evaluate dedicated tools — GitHub's 20-30 dev threshold is consistent across sources.

## Key Comparison

| Factor | GitHub Projects | Jira |
|--------|----------------|------|
| Cost | Free with GitHub | $7.53/user/month |
| Kanban | Yes (board view) | Yes |
| Hierarchy | Sub-issues (beta) | Epic → Story → Subtask |
| Reporting | Minimal | Advanced |
| AI integration | Claude Code, Copilot, Agentic Workflows | Limited |
| Context switching | None (same platform) | Separate tool |

## Files

| File | Contents |
|------|----------|
| [github-issues-kanban-monorepo.md](github-issues-kanban-monorepo.md) | Full analysis with methodology |
| [citations.md](citations.md) | All 39 sources, numbered |
| [references/](references/) | One file per research dimension (8 total) |
| [audit/](audit/) | Citation audit + consistency review |

## Research Details

- **Date**: 2026-03-30
- **Sources**: 39 (GitHub docs, open-source projects, practitioner blogs)
- **Dimensions**: Kanban mechanics, multi-user patterns, best practices, risks/tensions, tooling automation, agentic automation, comparison with dedicated tools, monorepo considerations
- **Verification**: Two independent audit agents (citation accuracy + cross-file consistency)
