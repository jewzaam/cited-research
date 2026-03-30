# Citations

All sources visited in-session via WebSearch or WebFetch. Each entry includes the
specific data extracted and a quality tier rating.

## Source Quality Tiers

- **Tier 1:** Peer-reviewed papers, institutional reports
- **Tier 2:** Official documentation, manufacturer specs, established reference sites
- **Tier 3:** Industry blogs, conference talks, well-known practitioners
- **Tier 4:** Forums, personal blogs, GitHub discussions, social media

---

## [1] Claude Code Monitoring Documentation (Official)

- **URL:** https://code.claude.com/docs/en/monitoring-usage
- **Accessed:** 2026-03-30
- **Tier:** 2 (Official documentation)
- **Data extracted:** Claude Code exports telemetry via OpenTelemetry. Metrics include
  session count, lines of code, pull requests, commits, cost (USD), token usage,
  code edit decisions, and active time. Events include user prompts, tool results,
  API requests, API errors, and tool decisions. Supports OTLP, Prometheus, and
  console exporters. Session-level, user-level, and organization-level attributes
  available. No built-in dashboard—requires external backends (Grafana, Datadog,
  Honeycomb, etc.).

## [2] Claude Code Agent Teams Documentation (Official)

- **URL:** https://code.claude.com/docs/en/agent-teams
- **Accessed:** 2026-03-30
- **Tier:** 2 (Official documentation)
- **Data extracted:** Agent teams are experimental (disabled by default), require
  v2.1.32+. One session acts as team lead coordinating teammates. Each teammate is
  a separate Claude Code instance with its own context window. Shared task list with
  self-coordination. Two display modes: in-process (Shift+Down to cycle) and split
  panes (tmux or iTerm2). Teammates can message each other directly. No session
  resumption for in-process teammates. Recommended 3-5 teammates, 5-6 tasks per
  teammate. Teams stored at ~/.claude/teams/{team-name}/config.json.

## [3] Cursor Parallel Agents Documentation

- **URL:** https://cursor.com/docs/configuration/worktrees
- **Accessed:** 2026-03-30
- **Tier:** 2 (Official documentation)
- **Data extracted:** Cursor supports parallel agents via git worktrees with up to
  20 worktrees per workspace. Each agent gets isolated files. Features include
  side-by-side comparison cards, SCM pane visualization (git.showCursorWorktrees
  setting), notification settings for completion, automatic worktree cleanup
  (configurable interval), and "Apply" functionality to merge changes back. Supports
  "Best-of-N" execution across multiple models.

## [4] GitHub Copilot Agent Management Documentation

- **URL:** https://docs.github.com/en/copilot/concepts/agents/coding-agent/agent-management
- **Accessed:** 2026-03-30
- **Tier:** 2 (Official documentation)
- **Data extracted:** Copilot supports multiple concurrent agent sessions. Agents tab
  in repos provides session initiation, monitoring, and management. Real-time session
  log viewing. Mid-session steering without stopping runs (consumes one premium
  request). Session transfer to VS Code or Copilot CLI. Centralized control page
  prevents losing context.

## [5] GitHub Copilot /fleet Command Documentation

- **URL:** https://docs.github.com/en/copilot/concepts/agents/copilot-cli/fleet
- **Accessed:** 2026-03-30 (via discovery agent search snippets)
- **Tier:** 2 (Official documentation)
- **Data extracted:** The /fleet command uses subagents to execute tasks in parallel,
  breaking plans into smaller independent tasks. Four specialized agents: Explore,
  Task, Plan, Code-review. Transforms 90-second sequential handoffs into 30-second
  parallel analysis.

## [6] Devin Session Tools Documentation

- **URL:** https://docs.devin.ai/work-with-devin/devin-session-tools
- **Accessed:** 2026-03-30
- **Tier:** 2 (Official documentation)
- **Data extracted:** Devin provides unified Progress Tab across Shell, IDE, and
  Browser tools. Full command history, code edit diffs, browser screenshots. Supports
  parallel execution within sessions (multiple concurrent actions). Pause/stop/resume
  session controls. Toggle between read-only and writable terminal modes. Note:
  documentation focuses on single-session collaboration, not multi-session management
  dashboard.

## [7] Aider Parallel Workflow GitHub Issue

- **URL:** https://github.com/Aider-AI/aider/issues/302
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 4 (GitHub issue)
- **Data extracted:** Filed October 2023 requesting multiple parallel instances.
  Running two Aider processes simultaneously causes log file overwrites, stale file
  contents, and work mixing during diff creation. No native multi-session support
  as of 2026. Users rely on manual git worktree workflows.

## [8] ccboard — Claude Code Monitoring Dashboard

- **URL:** https://github.com/FlorianBruniaux/ccboard
- **Accessed:** 2026-03-30
- **Tier:** 3 (Open-source project)
- **Data extracted:** Rust TUI + web dashboard with 13 interactive tabs: Dashboard,
  Sessions, Analytics, Costs, History, Audit Log, MCP, Config, Hooks, Tools, Plugins,
  Search (FTS5), Brain (cross-session knowledge). Live session status via hooks
  (Running ●, Waiting ◐, Stopped ✓). Subagent parent-child tree visualization.
  30-day cost forecasting. Budget alerts (4 levels). Auto-imports from Claude Code,
  Cursor, Codex CLI, OpenCode. 5.8MB Rust binary. 89x faster startup via SQLite cache.
  Web UI on localhost:3333 via SSE. macOS notifications. 41 GitHub stars.

## [9] agtx — Multi-Agent AI Coding Terminal

- **URL:** https://github.com/fynnfluegge/agtx
- **Accessed:** 2026-03-30
- **Tier:** 3 (Open-source project)
- **Data extracted:** Rust TUI with kanban board (Backlog, Planning, Running, Review,
  Done). MCP-driven orchestrator agent autonomously manages the board. Each task gets
  its own git worktree and tmux window. Supports Claude Code, Codex, Gemini CLI,
  OpenCode, Cursor Agent, Copilot. 7 built-in plugins for spec-driven workflows.
  Status indicators: spinners (active), checkmarks (phase complete), pause icons
  (idle 15+ sec). Session auto-resume on phase transitions.

## [10] claude-tmux — TUI for Claude Code Sessions in tmux

- **URL:** https://github.com/nielsgroen/claude-tmux
- **Accessed:** 2026-03-30
- **Tier:** 3 (Open-source project)
- **Data extracted:** Rust TUI for managing Claude Code instances in tmux. Shows all
  tmux sessions with status indicators: Working (●), Idle (○), Waiting (◐),
  Unknown (?). Live preview with ANSI color support. Fuzzy filtering. Create/kill/rename
  sessions. git worktree and PR support (requires gh CLI). Activated via tmux popup
  keybinding.

## [11] tmux-agent-indicator — Visual AI Agent State in tmux

- **URL:** https://github.com/accessd/tmux-agent-indicator
- **Accessed:** 2026-03-30
- **Tier:** 3 (Open-source project)
- **Data extracted:** tmux plugin tracking three states: running, needs-input, done.
  Visual feedback via pane borders, window titles, status bar icons (🤖 claude,
  🧠 codex, 💻 opencode). Integrates with Claude Code hooks (UserPromptSubmit,
  PermissionRequest, Stop). Process fallback detection for aider, cursor. Three color
  presets (balanced, high-contrast, subtle). Knight Rider animation for running state.
  Requires tmux 3.0+.

## [12] AgentsView — AI Agent Session Browser

- **URL:** https://github.com/wesm/agentsview
- **Accessed:** 2026-03-30
- **Tier:** 3 (Open-source project)
- **Data extracted:** Supports 12 agents: Claude Code, Codex, Copilot, Gemini,
  OpenCode, Cursor, Amp, iFlow, Pi, OpenClaw, Kimi, and VS Code Copilot. Full-text
  search via SQLite FTS5. Activity heatmaps, tool usage analytics, velocity metrics.
  Live updates via SSE. Go backend, Svelte 5 frontend, Tauri desktop wrapper.
  PostgreSQL integration for team dashboards. vim-style keyboard navigation (j/k).
  Local-first with SQLite storage.

## [13] Agent Sessions — macOS Native Session Manager

- **URL:** https://github.com/jazzyalex/agent-sessions
- **Accessed:** 2026-03-30
- **Tier:** 3 (Open-source project)
- **Data extracted:** Native macOS app (Swift, requires macOS 14+). Supports Codex CLI,
  Claude Code, Gemini CLI, GitHub Copilot CLI, OpenCode, Factory/Droid. Session
  browser with full-text transcript search. Agent Cockpit (beta): live activity
  summaries for iTerm2 sessions, active/waiting status, Claude usage tracking.
  Rate limit visibility. One-click session resumption. Read-only access to agent
  directories. MIT license.

## [14] Emdash — Agentic Development Environment

- **URL:** https://github.com/generalaction/emdash
- **Accessed:** 2026-03-30
- **Tier:** 3 (Open-source project, YC W26)
- **Data extracted:** Provider-agnostic desktop app for parallel coding agents. 23
  supported agents including Claude Code, Codex, Copilot, Cursor, Gemini, and more.
  Git worktree isolation. SSH/SFTP for remote development. Linear, GitHub, and Jira
  ticket integration. Local-first SQLite storage. MIT license. No code transmitted to
  external servers.

## [15] Superset — Parallel Coding Agent Platform

- **URL:** https://superset.sh/
- **Accessed:** 2026-03-30
- **Tier:** 3 (Open-source project)
- **Data extracted:** Desktop app for running 10+ parallel agents. Agent-agnostic
  (Claude Code, OpenCode, Cursor, Codex, etc.). Git worktree isolation. Real-time
  monitoring with instant agent switching. IDE deep-linking (Cursor, VS Code, Xcode,
  JetBrains, Sublime). Port forwarding. MCP server support. Elastic License 2.0.
  Self-hosting available. Used by developers at Microsoft, OpenAI, Netflix, Google.

## [16] Corral — Unified Agent Dashboard

- **URL:** https://github.com/cdknorow/corral
- **Accessed:** 2026-03-30
- **Tier:** 3 (Open-source project)
- **Data extracted:** Python + JS dashboard for managing multiple AI agents. PULSE
  protocol for real-time agent status (agents broadcast ||PULSE:STATUS [msg]||).
  Agent teams with isolated git worktrees, role-specific behavior prompts. Message
  board for inter-agent communication with cursor-based delivery. Full-text search
  (SQLite FTS5). AI-generated session summaries. Git integration (commits, branches,
  file changes). Installable via PyPI (agent-coral). Dashboard at localhost:8420.

## [17] Windsurf Wave 13 — Parallel Agent Sessions

- **URL:** https://windsurf.com/blog/windsurf-wave-13
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 2 (Official blog)
- **Data extracted:** Wave 13 introduced parallel multi-agent sessions with git
  worktrees and side-by-side Cascade panes. Users can run multiple Cascade sessions
  simultaneously. Background planning agent continuously refines long-term plans.
  Conflicting reports on true background execution capabilities.

## [18] Continue.dev Mission Control

- **URL:** https://docs.continue.dev/mission-control
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 2 (Official documentation)
- **Data extracted:** Team-oriented session management. Session assignment to teammates.
  Shared Inbox for Cloud Agent Tasks. View active runs, logs, outcomes for every
  session. Hooks system for CLI event interception (added 2026).

## [19] Nimbalyst — Best Tools for Parallel AI Coding Agents

- **URL:** https://nimbalyst.com/blog/best-tools-for-running-parallel-ai-coding-agents/
- **Accessed:** 2026-03-30
- **Tier:** 3 (Industry blog)
- **Data extracted:** Comparison of 6 tools: ccmanager (CLI, 10+ agents, no dashboard),
  dmux (CLI + tmux, one-key merge, lifecycle hooks), Superset (desktop IDE, 10+
  agents, visual status), agentree (CLI, git isolation only), Cursor (IDE, 8 parallel
  agents, multi-agent judging), Nimbalyst (desktop, kanban, iOS app, voice sessions).
  Key differentiators: visual dashboard, git worktree support, multi-agent support
  count, diff review, mobile access.

## [20] Nimbalyst — Best Session Managers for Claude Code and Codex

- **URL:** https://nimbalyst.com/blog/best-session-managers-for-claude-code-and-codex/
- **Accessed:** 2026-03-30
- **Tier:** 3 (Industry blog)
- **Data extracted:** Comparison of native and third-party session managers. Claude
  Squad: terminal UI, tmux multiplexing, git worktree isolation. ccmanager: terminal
  UI, multi-repo, real-time state detection. Claudine: VS Code extension, kanban
  board, auto-status detection. Opcode: desktop GUI, timeline/checkpoints, usage
  analytics. Nimbalyst: session kanban, git worktrees, files-edited sidebar, iOS app.

## [21] VS Code Multi-Agent Development Announcement

- **URL:** https://code.visualstudio.com/blogs/2026/02/05/multi-agent-development
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 2 (Official blog)
- **Data extracted:** VS Code announced multi-agent development integration in
  February 2026, positioning itself as a unified home for multiple AI agents.

## [22] GitHub Enterprise Agent Control Plane

- **URL:** https://github.blog/changelog/2026-02-26-enterprise-ai-controls-agent-control-plane-now-generally-available/
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 2 (Official changelog)
- **Data extracted:** GitHub Enterprise AI Controls with agent control plane GA in
  February 2026. Session filters for discovering and managing agent activity.

## [23] Anthropic Claude Code Analytics

- **URL:** https://docs.anthropic.com/en/docs/claude-code/analytics
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 2 (Official documentation)
- **Data extracted:** Official analytics dashboard at claude.ai/analytics/claude-code
  for Teams/Enterprise. Tracks lines of code accepted, suggestion acceptance rate,
  daily active users, sessions, total spend, PR contributions. Claude Code Analytics
  API for programmatic access (admin-only). CSV export. Leaderboard of top
  contributors.

## [24] claude-code-zellij-status

- **URL:** https://github.com/thoo/claude-code-zellij-status
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 3 (Open-source project)
- **Data extracted:** Monitors Claude Code activity across multiple Zellij panes via
  zjstatus. Provides status visibility for AI agents in Zellij terminal multiplexer.

## [25] Cursor Background Agents Documentation

- **URL:** https://docs.cursor.com/en/background-agent
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 2 (Official documentation)
- **Data extracted:** Background agents clone repositories in cloud environments
  (isolated Ubuntu VMs). Work autonomously, open PRs when finished. Up to 8 parallel
  sessions in isolated Ubuntu VMs (Cursor 2.5). Internet access and package
  installation capabilities.

## [26] Copilot CLI Session Tracking

- **URL:** https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/track-copilot-sessions
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 2 (Official documentation)
- **Data extracted:** Sessions trackable from GitHub CLI, GitHub Mobile, VS Code,
  Raycast, and JetBrains IDEs. Session resumption via `copilot --resume=SESSION-ID`.
  VS Code Agent Sessions view for centralized management.

## [27] Copilot CLI Subagents Documentation

- **URL:** https://code.visualstudio.com/docs/copilot/agents/subagents
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 2 (Official documentation)
- **Data extracted:** VS Code supports multiple Copilot CLI sessions in parallel with
  worktree and workspace isolation modes.

## [28] Amazon Q Developer Agentic Coding

- **URL:** https://aws.amazon.com/about-aws/whats-new/2025/05/amazon-q-developer-agentic-coding-experience-ide/
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 2 (Official announcement)
- **Data extracted:** Amazon Q Developer performs autonomous tasks: implementing
  features, documenting, testing, reviewing, refactoring. Multi-turn conversations
  maintaining context. Available in VS Code. No explicit parallel session support
  documented.

## [29] Roo Code Session Management Issue

- **URL:** https://github.com/RooCodeInc/Roo-Code/issues/4934
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 4 (GitHub issue)
- **Data extracted:** Roo Code's Claude Code integration lacks session management.
  Each CLI call operates independently without conversation continuity. Users must
  re-explain context in every request. Community developed Memory Bank workarounds.

## [30] tmux Claude Code Workflow Guides

- **URL:** https://ksingh7.medium.com/watch-claude-code-agents-work-side-by-side-a-tmux-setup-guide-1ef3ba1531c4
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 3 (Practitioner blog)
- **Data extracted:** Side-by-side agent setup using tmux split panes. Practical
  ceiling of 5-7 concurrent agents before rate limits, merge conflicts, and review
  bottlenecks eat the gains.

## [31] amux — Claude Code Agent Multiplexer

- **URL:** https://github.com/mixpeek/amux
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 3 (Open-source project)
- **Data extracted:** Open-source Claude Code agent multiplexer for running dozens of
  parallel agents. Designed for high-concurrency agent workflows.

## [32] Chloe — Terminal Multiplexer for AI Agents

- **URL:** https://getchloe.sh
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 3 (Open-source project)
- **Data extracted:** Terminal multiplexer for AI coding agents with Kanban task
  management. Purpose-built for AI agent workflows.

## [33] dmux — Dev Agent Multiplexer

- **URL:** https://github.com/standardagents/dmux
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 3 (Open-source project)
- **Data extracted:** Dev agent multiplexer for git worktrees and coding agents.
  One-key merge when tasks complete. Lifecycle hooks for CI automation. Supports
  11+ agents.

## [34] Claude Code Sessions Storage Structure

- **URL:** https://gist.github.com/samkeen/dc6a9771a78d1ecee7eb9ec1307f1b52
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 4 (GitHub gist)
- **Data extracted:** ~/.claude directory structure: projects/, plans/, file-history/,
  todos/, session-env/, shell-snapshots/, debug/ subdirectories. Sessions stored as
  JSONL (one JSON object per line). Session files contain user/assistant messages,
  file-history-snapshot, queue-operation entries.

## [35] Stargx/claude-code-dashboard

- **URL:** https://github.com/Stargx/claude-code-dashboard
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 3 (Open-source project)
- **Data extracted:** Lightweight real-time multi-session monitoring dashboard.
  Shows token usage, costs, active tools, subagents. Localhost web UI.

## [36] ccusage — CLI Usage Analyzer

- **URL:** https://ccusage.com/
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 3 (Open-source project)
- **Data extracted:** CLI tool for analyzing Claude Code usage from JSONL files.
  Daily/monthly/session usage breakdowns with formatted tables.

## [37] Claude Code Dashboard VS Code Extension

- **URL:** https://marketplace.visualstudio.com/items?itemName=jspw.claude-code-dashboard
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 3 (VS Code extension)
- **Data extracted:** Real-time dashboard showing all projects, sessions, usage, and
  tokens within VS Code.

## [38] Codeman — WebUI for Claude Code in tmux

- **URL:** https://github.com/Ark0N/Codeman
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 3 (Open-source project)
- **Data extracted:** Modern WebUI to manage Claude Code & Opencode in tmux sessions.
  Presets for automation workflows (solo-work, subagent-workflow, team-lead,
  overnight-autonomous) with auto-configured hooks.

## [39] KanVibe — Self-hosted Kanban with Browser Terminals

- **URL:** https://github.com/rookedsysc/kanvibe
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 3 (Open-source project)
- **Data extracted:** Self-hosted Kanban board with browser terminals for AI coding
  agents. Web-based drag-and-drop interface. Supports both tmux and Zellij.
  Hook-driven auto-tracking of agent status.

## [40] AgentOps — Python SDK for AI Agent Monitoring

- **URL:** https://github.com/AgentOps-AI/agentops
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 3 (Open-source project)
- **Data extracted:** Python SDK for AI agent monitoring. LLM cost tracking,
  benchmarking, session replays, time-travel debugging, prompt injection detection.
  Integrates with LangGraph and CrewAI.

## [41] Langfuse — Open-Source LLM Observability

- **URL:** https://langfuse.com/blog/2024-07-ai-agent-observability-with-langfuse
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 3 (Open-source project)
- **Data extracted:** Open-source observability platform. 21,000+ GitHub stars, MIT
  license. Tracing, cost tracking, evaluation for multi-agent workflows. Supports
  OpenTelemetry. Integrates with LangChain, CrewAI, AutoGen.

## [42] ServiceNow AI Control Tower

- **URL:** https://www.servicenow.com/products/ai-control-tower.html
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 2 (Commercial product)
- **Data extracted:** Enterprise AI agent governance platform. Centralized tracking of
  performance metrics, token consumption, compliance, and ROI. Vendor-agnostic across
  native, in-house, and third-party agents.

## [43] SigNoz Claude Code Dashboard Template

- **URL:** https://signoz.io/docs/dashboards/dashboard-templates/claude-code-dashboard/
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 3 (Open-source platform)
- **Data extracted:** Enterprise dashboards for Claude Code via OpenTelemetry exports.
  Token consumption, costs, cache efficiency, session duration, code changes.

## [44] Datadog AI Agents Console

- **URL:** https://www.datadoghq.com/blog/claude-code-monitoring/
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 2 (Commercial product blog)
- **Data extracted:** Organization-wide Claude Code tracking via Datadog AI Agents
  Console. Performance trends, ROI analysis.

## [45] Anthropic Building C Compiler with Parallel Claudes

- **URL:** https://www.anthropic.com/engineering/building-c-compiler
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 2 (Official blog)
- **Data extracted:** Anthropic internal case study of building a C compiler using
  parallel Claude Code sessions with git worktrees.

## [46] Devin Parallel Session Capabilities

- **URL:** https://cognition.ai/blog/devin-2
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 2 (Official blog)
- **Data extracted:** Devin 2.0 designed for parallelization. Each session runs in
  isolated VM. Users can spin up multiple Devins working in parallel. Orchestration
  of Managed Devins, session analysis, playbook creation.

## [47] Claude Code Hooks Documentation

- **URL:** https://code.claude.com/docs/en/hooks
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 2 (Official documentation)
- **Data extracted:** SessionStart and SessionEnd hooks for lifecycle events.
  PreToolUse/PostToolUse hooks. CLAUDE_ENV_FILE for session state persistence. Hooks
  can block operations. TeammateIdle, TaskCreated, TaskCompleted hooks for agent teams.

## [48] Cursor 2.0 Parallel Agent Announcement

- **URL:** https://www.techzine.eu/news/devops/135916/cursor-2-0-introduces-parallel-agents-and-new-model/
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 3 (Tech news)
- **Data extracted:** Cursor 2.0 (October 2025) introduced native parallel agent
  support with up to 8 simultaneous agents. Each operates in isolated git worktrees
  or remote machines. Background agents (May 2025) clone repos in cloud environments.

## [49] Agent of Empires — Terminal Session Manager

- **URL:** https://github.com/njbrake/agent-of-empires
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 3 (Open-source project)
- **Data extracted:** Terminal session manager for AI coding agents on Linux/macOS.
  Built on tmux, written in Rust. Multiple agents in parallel across branches.
  Visual interface with status at a glance and keyboard shortcuts.

## [50] ccmanager — Multi-AI Session Manager

- **URL:** https://github.com/kbwo/ccmanager
- **Accessed:** 2026-03-30 (via discovery agent)
- **Tier:** 3 (Open-source project)
- **Data extracted:** Coding Agent Session Manager supporting Claude Code, Gemini CLI,
  Codex CLI, Cursor, and more. Multi-repo support, real-time state detection,
  context transfer between sessions, automation hooks.
