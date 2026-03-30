# Citations

All sources were visited in-session via WebSearch or WebFetch on 2026-03-30.

## Dimension 1: Kanban Mechanics

[1] GitHub Docs. "About Projects." docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects. Tier 2.
- Data extracted: Projects v2 supports up to 50 fields total (built-in + custom). Three view layouts: table, board, roadmap. Custom field types: text, number, date, single select, iteration. Auto-sync between projects and source issues/PRs.

[2] GitHub Docs. "Using the built-in automations." docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations. Tier 2.
- Data extracted: Two default workflows enabled: status→Done on issue close, status→Done on PR merge. Additional automations: auto-archive, auto-add items from repos. Limited trigger set (item added, issue closed, PR merged).

[3] GitHub Docs. "Customizing the board layout." docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/customizing-the-board-layout. Tier 2.
- Data extracted: Board columns use single select or iteration fields. Drag-and-drop updates field values automatically. Swimlanes via horizontal grouping. Column limits are advisory (display-only, not enforced). When sorting is enabled, manual reorder within columns is disabled. Cannot group/slice/sort by: title, labels, reviewers, or linked PRs.

[4] GitHub Docs. "Filtering projects." docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects. Tier 2.
- Data extracted: Multiple filters combine as AND. Comma-separated values within same field act as OR. No cross-field OR support. Special keywords: @me, @current/@previous/@next for iterations, @today with arithmetic. Negation via hyphen prefix. Qualifiers include assignee, label, repo, is:state, has:/no: field existence.

[5] GitHub Changelog. "GitHub Issues & Projects – Projects without limits (Private Beta)." github.blog/changelog/2024-02-12-github-issues-projects-projects-without-limits-private-beta/. Tier 2.
- Data extracted: Previous limit was 1,200 items per project. New limit expanded to 50,000 items (soft limit, expandable). Announced February 12, 2024. Private beta with waitlist access.

[6] GitHub Community Discussion #9678. "Increase limit of 1200 items." github.com/orgs/community/discussions/9678. Tier 4.
- Data extracted: Mario Rodriguez (GitHub PM) stated limit was to prevent projects becoming unlimited backlogs and keep them "snappy." Archive limit is 10,000 items separately. Community pushback cited undocumented constraint and cross-repo tracking needs.

[7] GitHub Community Discussion #4928. "Issue dependencies and relationships." github.com/orgs/community/discussions/4928. Tier 2.
- Data extracted: Dependencies feature (blocked by / is blocking) became GA in August 2025. Sub-issues don't address dependency needs (one parent per issue, not many-to-many). Community continues requesting additional relationship types (relates to, duplicates, documents).

[8] GitHub Docs. "Creating issue dependencies." docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-issue-dependencies. Tier 2.
- Data extracted: Two relationship types: "blocked by" and "blocking." Blocked issues display a "Blocked" icon on project boards. Created via Relationships section in issue sidebar. Source did not specify cross-repo support limits or maximum dependency counts.

[9] GitHub Roadmap #760. "Issue Hierarchy powered by Tasklists." github.com/github/roadmap/issues/760. Tier 2.
- Data extracted: Tasklists feature closed as "not planned" — replaced by sub-issues. Sub-issues received public beta October 2024. Migration from tasklists to sub-issues planned. Markdown-based tasklists with Tracks/Tracked-by columns.

## Dimension 2: Multi-User Collaboration

[10] GitHub Docs. "Assigning issues and pull requests." docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/assigning-issues-and-pull-requests-to-other-github-users. Tier 2.
- Data extracted: Up to 10 assignees per issue/PR. Team-based assignment not natively supported for issues (only for PR reviewers).

[11] GitHub Docs. "Best practices for Projects." docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/best-practices-for-projects. Tier 2.
- Data extracted: Use @mentions for team coordination. Create issue dependencies to clarify blocking. Maintain project READMEs with purpose and contact info. Post status updates marking health as "On track" or "At risk." Use column limits on board views. Link projects to teams for transparency.

[12] GitHub Community Discussion #137358. "Managing multiple teams with GitHub Projects V2." github.com/orgs/community/discussions/137358. Tier 3.
- Data extracted: Separate projects per team: custom field metadata doesn't sync reliably between projects. Unified single project: scalability concerns for day-to-day team operations. Discussion remained unanswered — no established best practices from GitHub.

[13] GitHub Docs. "About code owners." docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners. Tier 2.
- Data extracted: CODEOWNERS file in .github/, root, or docs/. Patterns follow gitignore rules (no negation, no character ranges). Code owners auto-requested for PR review (not issues). Requires write access. File size limit: 3 MB. Case-sensitive paths.

[14] Jeff Wilcox. "Scaling from 2,000 to 25,000 engineers on GitHub at Microsoft." jeff.wilcox.name/2019/06/scaling-25k/. Tier 3.
- Data extracted: Source inaccessible (ECONNREFUSED). Discovery agent preliminary finding: Microsoft scaled GitHub usage from 2,000 to 25,000 engineers with heavy tooling/process investment.
- **Status: INACCESSIBLE**

## Dimension 3: Best Practices

[15] Dave Lunny. "Sane GitHub Labels." medium.com/@dave_lunny/sane-github-labels-c5d2e6004b63. Tier 4.
- Data extracted: Three label categories with prefix convention: Status: (In Progress, Abandoned, Accepted, Completed — only one per issue), Type: (Bug, Enhancement, Question), Priority: (optional, with caveat about priority inflation). Naming pattern: [Category]: [Specific Label].

[16] GitHub Docs. "Syntax for issue forms." docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms. Tier 2.
- Data extracted: YAML schema with required keys: name, description, body. Supported field types: markdown, input, textarea, dropdown (supports multiple:true), checkboxes, upload. Top-level auto-labeling and auto-assignment. Projects field for auto-adding to boards.

[17] Kubernetes Contributor Guide. "Issue Triage." kubernetes.dev/docs/guide/issue-triage/. Tier 2.
- Data extracted: 5-step process: review new issues (needs-triage label auto-applied), categorize by type, assign priority (critical-urgent through backlog), route to SIG ownership, follow up (30-day nudge, 90-day lifecycle/stale). Tools: Triage Party, Project Boards, DevStats.

[18] GitHub Docs. "Automating projects using Actions." docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/automating-projects-using-actions. Tier 2.
- Data extracted: GITHUB_TOKEN cannot access projects (scoped to repo level). Requires GitHub App or PAT with project scope. GraphQL mutations: addProjectV2ItemById, updateProjectV2ItemFieldValue. Projects span multiple repos but workflows are repo-specific.

## Dimension 4: Risks and Tensions

[19] GitHub Community Discussion #5714. "Hierarchical issues in Projects." github.com/orgs/community/discussions/5714. Tier 2.
- Data extracted: Strong demand for nested issues (SAFe structure: Epics→Capabilities→Features→Stories). Multiple users requested "infinite sublevels." Tasklists offered as solution (Jan 2023), later replaced by sub-issues (Oct 2024).

[20] Shortcut Blog. "GitHub Issues Alternatives." shortcut.com/blog/github-issues-alternatives-why-engineering-teams-choose-shortcut. Tier 3.
- Data extracted: Lack of hierarchy (no built-in Epics, Roadmaps, Objectives). Limited collaboration beyond engineering (long comment threads, missing attachments). Insufficient progress tracking (no velocity, no sprint insights). Scalability issues with multiple projects/sprints/releases. No quantitative data provided.

[21] GitHub Stale Action. github.com/actions/stale. Tier 2.
- Data extracted: Default: mark stale after 60 days inactivity, close after 7 more days. Configurable exempt labels, milestones, assignees. Rate limiting: 30 operations per run default. Outputs: staled-issues-prs, closed-issues-prs lists. Close reason configurable: completed or not_planned.

## Dimension 5: Tooling Automation

[22] GitHub Blog. "IssueOps: Automate CI/CD and more with GitHub Issues and Actions." github.blog/engineering/issueops-automate-ci-cd-and-more-with-github-issues-and-actions/. Tier 2.
- Data extracted: IssueOps uses Issues, Actions, and PRs as control interfaces. Finite-state machine framework: states, events, transitions, guards, actions. Event-driven (open issues, add labels, post comments trigger workflows). Benefits: transparency via immutable audit trails, customizable workflows.

[23] GitHub Docs. "Automating projects using Actions." (Same as [18]). Tier 2.
- Data extracted: actions/add-to-project maintained by GitHub. Key constraint: GITHUB_TOKEN scoped to repo, cannot access projects. GraphQL API for field updates (single select, date fields).

[24] Everhour Blog. "Jira vs GitHub." everhour.com/blog/jira-vs-github/. Tier 3.
- Data extracted: GitHub Issues: basic kanban, limited custom workflows, minimal reporting. Jira: $7.53/user/month vs GitHub $4/user/month. GitHub setup in minutes vs Jira hours. Most teams under 30 developers never need to switch. GitHub free tier has unlimited repos.

## Dimension 6: Agentic Automation

[25] Claude Code Docs. "GitHub Actions." code.claude.com/docs/en/github-actions. Tier 2.
- Data extracted: @claude mention in issues/PRs triggers Claude Code. Creates complete PRs from issue descriptions. Follows CLAUDE.md guidelines. Built on Claude Agent SDK. Permissions: contents, issues, PRs read/write. Triggers: issue_comment, PR review comment, issues opened/assigned. Cost: API tokens + GitHub Actions minutes.

[26] GitHub Blog. "GitHub Copilot coding agent 101." github.blog/ai-and-ml/github-copilot/github-copilot-coding-agent-101-getting-started-with-agentic-workflows-on-github/. Tier 2.
- Data extracted: Assign issues directly to Copilot like a human teammate. Creates draft PR tagged [WIP], explores repo context, writes code, runs tests. Pushes only to copilot/* branches. Cannot approve/merge own work. Operates in sandboxed environment with limited internet. Costs one premium Copilot request per task + Actions minutes.

[27] GitHub Blog. "Automate repository tasks with GitHub Agentic Workflows." github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/. Tier 2.
- Data extracted: Technical preview Feb 2026. Workflows authored in Markdown with YAML frontmatter. Executed by coding agents (Copilot CLI, Claude Code, OpenAI Codex) in GitHub Actions. Capabilities: issue triage, documentation, code quality, test coverage, CI/CD support. Read-only by default; write requires "safe outputs" approval. Patterns: ChatOps, DailyOps, IssueOps, ProjectOps, MultiRepoOps.

[28] Cursor Forum. "Native GitHub issue creation integration." forum.cursor.com/t/native-github-issue-creation-integration/32646. Tier 4.
- Data extracted: Feature request for native GitHub Issues integration in Cursor — not yet built-in as of search date. Community workarounds via external tools.

## Dimension 7: Comparison with Dedicated Tools

[29] Spring Framework Blog. "Migration from Jira to GitHub Issues." spring.io/blog/2019/01/15/spring-framework-s-migration-from-jira-to-github-issues/. Tier 2.
- Data extracted: Source inaccessible (JavaScript-only page, no content extracted). Discovery agent reported: motivation was single login/platform, markdown simplicity, unified view. Challenges: markup conversion ("most painful part"), 25 Jira components → 5 GitHub labels.
- **Status: INACCESSIBLE**

[30] Apache Accumulo Blog. "Moving to GitHub Issues." accumulo.apache.org/blog/2018/03/16/moving-to-github-issues.html. Tier 2.
- Data extracted: Selective migration strategy (only active/community-interest issues). Creating issue before PR made optional. Automated issue closure via commit messages. JIRA transitioned to read-only. Pragmatic, iterative approach.

[31] IdeaPlan. "Jira vs GitHub Projects." ideaplan.io/compare/jira-vs-github-projects. Tier 3.
- Data extracted: Discovery agent reported: enterprise depth vs developer simplicity. GitHub lacks workflow enforcement, custom transitions, approval gates. Jira has 5,000+ marketplace apps. GitHub Teams at $44/user/year vs Jira Premium pricing.

[32] GitHub Community Discussion #7267. "Handling epics/umbrellas in GitHub Projects." github.com/orgs/community/discussions/7267. Tier 2.
- Data extracted: Discovery agent reported: community workarounds for hierarchical issue management in Projects.

## Dimension 8: Monorepo Considerations

[33] GitHub Well-Architected. "Monorepos." wellarchitected.github.com/library/scenarios/monorepos/. Tier 2.
- Data extracted: Align repo organization with logical projects, team boundaries, release cadences. Use matrix builds, labeled PRs, subdirectory-based triggers for CI. Assign permissions precisely for high-impact areas. Adopt clear versioning strategies. Plan for clone time growth.

[34] Digma.ai. "10 Common Problems of Working with a Monorepo." digma.ai/10-common-problems-of-working-with-a-monorepo/. Tier 3.
- Data extracted: 10 problems: large repo size, complex dependencies, build performance, lack of clear boundaries, CI challenges, steep learning curve, technical debt, version conflicts, collaboration overhead, merge conflicts. Solutions: smaller commits, feature flags, pre-commit hooks.

[35] Ahrefs. "Monorobot." github.com/ahrefs/monorobot. Tier 2.
- Data extracted: Slackbot for GitHub monorepos. Routes notifications based on file prefixes, issue/PR labels, CI build statuses. Link unfurling for commits/PRs/issues. Maps GitHub handles to Slack users. Built in OCaml. Requires webhook configuration.

[36] Kubernetes Issue #24343. "Monorepo challenges." github.com/kubernetes/kubernetes/issues/24343. Tier 1.
- Data extracted: Discovery agent reported: "a large monorepo works for Google, but not on GitHub" — ACLs, notification management, issue triage, PR reviews, merge conflicts cited as velocity limiters. Uses labels like area/code-organization, sig/architecture. Peribolos for team permission management.

[37] Microsoft ISE Blog. "Working with a Monorepo." devblogs.microsoft.com/ise/working-with-a-monorepo/. Tier 2.
- Data extracted: Discovery agent reported: Microsoft ISE team practices for mono-repo coordination and ownership patterns.

[38] monorepo.tools. "Monorepo tools comparison." monorepo.tools/. Tier 2.
- Data extracted: Best-in-class features: local/remote caching, distributed task execution, affected detection, task splitting, flaky test detection. References Nx specifically. Comparison available at /compare page (not fully extracted).

[39] FreeCodeCamp. "Using GitHub Native Features for a Mid-Size Distributed Team." freecodecamp.org/news/using-github-native-features-for-a-mid-size-distributed-team-3acdfd0f027c/. Tier 3.
- Data extracted: Discovery agent reported: case study of 15-person team (10 developers) using GitHub native features.

## Additional Sources (Added 2026-03-30)

[40] Vibe Kanban. "Vibe Kanban." vibekanban.com/. Tier 3.
- Data extracted: Multi-agent orchestration platform by Bloop AI Limited. Supports 9 AI agents: Claude Code, ChatGPT, Gemini, OpenCode, Cursor, Amp, Aider, Copilot, Windsurf. Three-phase workflow: Plan → Prompt → Review. Automated git worktree creation for parallel agent execution. Features: kanban board interface, built-in code review with syntax highlighting, integrated browser for QA, hierarchical task breakdown (parent tasks with sub-issues), automatic status updates when agents start work or PRs are created/merged. Community metrics: 100,000+ PRs created, 30,000+ active users, 24.1k GitHub stars. Entry point: `npx vibe-kanban`.
