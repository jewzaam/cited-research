# Agentic Automation

Dimension covering how AI coding tools interact with GitHub Issues for planning, triage, and execution.

Sources: see [citations.md](../citations.md) for full details.

## Claude Code

Claude Code integrates with GitHub Issues via the `@claude` mention system and GitHub Actions [25]:

| Capability | How It Works |
|-----------|-------------|
| Issue-to-PR | @claude in issue comment triggers analysis, creates complete PR |
| PR review | @claude in PR comment provides code review |
| Automated workflows | GitHub Actions with `anthropics/claude-code-action@v1` |
| Custom automation | Scheduled workflows (daily reports, issue summaries) |

**Configuration**: Requires GitHub App installation with read/write permissions for contents, issues, PRs [25]. Follows `CLAUDE.md` guidelines for project-specific standards [25]. Built on Claude Agent SDK [25].

**Triggers**: `issue_comment`, `pull_request_review_comment`, `issues` (opened/assigned) [25].

**Costs**: API tokens (per prompt/response) + GitHub Actions minutes [25].

## GitHub Copilot Coding Agent

The most mature official integration with GitHub Issues [26]:

- **Assignment**: Assign issues directly to Copilot like assigning to a human teammate [26]
- **Workflow**: Creates draft PR tagged [WIP] → explores repo context → writes code → runs tests → updates PR → tags for review [26]
- **Security**: Pushes only to `copilot/*` branches. Cannot approve/merge own work. Sandboxed with limited internet. All commits co-authored for traceability [26]
- **Scope**: Bug fixes, incremental features, refactoring, test coverage, documentation, tech debt [26]
- **Cost**: One premium Copilot request per task + Actions minutes [26]

## GitHub Agentic Workflows

Technical preview launched February 2026 [27]:

- **Authoring**: Workflows written in plain Markdown with YAML frontmatter [27]
- **Execution**: Coding agents (Copilot CLI, Claude Code, OpenAI Codex) run in GitHub Actions [27]
- **Capabilities**: Issue triage (summarize, label, route), documentation updates, code quality improvements, test coverage, CI/CD support, repository health reports [27]
- **Safety**: Read-only by default; write operations require explicit "safe outputs" approval. PRs never auto-merged [27]
- **Patterns**: ChatOps, DailyOps, DataOps, IssueOps, ProjectOps, MultiRepoOps, Orchestration [27]

## Cursor

Cursor **lacks native GitHub Issues integration** as of the search date [28]. Community members have requested native issue creation similar to VS Code's GitHub Issues extension [28]. Cursor focuses on GitHub Actions integration for CI/CD rather than direct issue management.

Workarounds: external tools like `claude-task-master` for PRD-to-ticket conversion; `gh` CLI for manual issue operations.

## AI-Powered Issue Triage

Multiple approaches for automated triage:

| Tool/Approach | Method |
|--------------|--------|
| GitHub Agentic Workflows [27] | Markdown-authored workflows for auto-labeling, routing, summarization |
| trIAge (open-source) | LLM-based triage assistant for issues, discussions, PRs |
| GitHub Security Lab Taskflow Agent | AI vulnerability triage (discovered ~30 real vulnerabilities) |
| Custom GitHub Actions + LLM | Label-triggered or event-triggered AI classification |

## Issue-to-PR Automation Patterns

| Pattern | Trigger | Agent |
|---------|---------|-------|
| @claude mention [25] | Comment in issue | Claude Code |
| Copilot assignment [26] | Issue assigned to Copilot | GitHub Copilot |
| Label trigger | Specific label applied | GitHub Actions + AI |
| Webhook trigger | Issue event | External automation |

## Kanban Board as Agent Task Queue

An emerging category of tools treats kanban boards as task queues for AI agents:

| Tool | Approach |
|------|----------|
| VS Code Agent Kanban | Copilot Chat integration with 'plan'/'implement' verbs, git worktree support |
| Vibe Kanban | Parallel agent orchestration (Claude Code, Cursor, Copilot, Gemini CLI) with isolated worktrees |
| Agent Kanban | AI agents as first-class team members with cryptographic identities |

**Key innovation**: parallel agent execution with isolated git worktrees removes sequential queuing constraint.

## Emerging Patterns

1. **Isolated worktrees per agent/task** for parallel execution
2. **Markdown-based task definitions** resistant to context rot
3. **Leader-worker patterns** — one agent decomposes goals, assigns to workers
4. **REST APIs** for agent-to-platform communication
5. **Shift from single-agent sequential to multi-agent parallel orchestration** with human review as the bottleneck

## Gaps and Limitations

- Cursor lacks native GitHub Issues integration [28]
- Success rate data for autonomous issue-to-PR workflows is sparse and potentially biased
- Limited evidence on multi-agent coordination when working on interdependent issues
- No established patterns for handling mono-repo-specific challenges (cross-package impact) in agentic workflows
- GitHub Agentic Workflows still in technical preview [27]
