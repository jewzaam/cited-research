# Dimension 6: Feature Comparison Matrix

Synthesis of how alternatives handle session state detection, window/tab navigation,
git status aggregation, permission/input notification, cost tracking, session
persistence/recovery, and sub-agent awareness.

See [citations.md](../citations.md) for full source details.

## Comparison Scope

This comparison evaluates tools most relevant to the `claude-dashboard` use case:
purpose-built tools for monitoring and managing parallel AI coding agent sessions.
General-purpose frameworks (LangChain, CrewAI) and enterprise control towers
(ServiceNow) are excluded as they serve different needs.

## Feature Matrix: Session Monitoring Tools

| Feature | claude-dashboard | ccboard [8] | AgentsView [12] | Agent Sessions [13] | claude-tmux [10] | tmux-agent-indicator [11] |
|---------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Session State Detection** | Hooks (4 states) | Hooks (3 states) | JSONL parsing | Directory scanning + iTerm2 | Pane content analysis (4 states) | Hooks (3 states) |
| **Real-Time Status** | Yes | Yes | Yes (SSE) | Yes (Cockpit beta) | Yes (live preview) | Yes |
| **Window/Tab Navigation** | One-click foreground (Win32, D-Bus, VS Code) | No (tmux popup) | No | One-click (iTerm2) | tmux attach | No |
| **Git Status per Session** | Yes (5 states, color-coded) | No | No | No | No | No |
| **Permission/Input Notification** | Yes (debounced, priority coloring) | Yes (Waiting ◐) | No | Yes (active/waiting) | Yes (Waiting ◐) | Yes (needs-input state) |
| **Cost Tracking** | Yes (OAuth usage, daily cost) | Yes (4-level budget alerts, 30-day forecast) | Yes (analytics dashboard) | Yes (Claude rate limits) | No | No |
| **Session Persistence** | Ghost sessions for ended sessions | Session history + Brain | SQLite FTS5 database | Full archive + search | tmux session persistence | No |
| **Sub-Agent Awareness** | Yes (count, debounce) | Yes (parent-child tree) | No | No | No | No |
| **Multi-Agent Support** | Claude Code only | Claude Code + Cursor + Codex + OpenCode | 12 agents | 6 agents | Claude Code (tmux) | Claude + Codex + OpenCode |
| **Platform** | Windows, Linux (Wayland) | macOS, Linux, Windows (experimental) | macOS, Linux, Windows | macOS only | Any (tmux) | Any (tmux) |
| **UI Type** | Desktop (Tkinter) | TUI + Web | Desktop + Web | Native macOS | TUI (tmux popup) | tmux status bar |
| **Always-on-Top** | Yes (borderless, shade mode) | No | No | No | No | N/A (integrated) |
| **System Tray** | Yes (priority coloring) | No | No | No | No | N/A |
| **Configurable** | Full settings dialog | Config file | Settings | Preferences | tmux config | 3 color presets |

## Feature Matrix: Parallel Agent Orchestrators

| Feature | Cursor [3] | GitHub Copilot [4] | Superset [15] | Emdash [14] | agtx [9] | Corral [16] |
|---------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Session State Detection** | Built-in IDE | Agents tab + logs | Dashboard status | Dashboard | Spinner/check/pause icons | PULSE protocol |
| **Real-Time Status** | Side-by-side cards | Session logs | Yes | Yes | Yes (15s idle detect) | Yes (inline markers) |
| **Window/Tab Navigation** | IDE tabs | GitHub web/CLI/VS Code | Agent switching | Agent switching | tmux windows | Web dashboard |
| **Git Status per Session** | SCM pane (optional) | PR workflow | Worktree status | Worktree status | Per-worktree | Git integration |
| **Permission/Input Notification** | IDE notifications | Mid-session steering | Notification system | — | — | Message board |
| **Cost Tracking** | Subscription-based | Premium requests | No API proxying | No | No | No |
| **Session Persistence** | Worktree cleanup configurable | Session transfer | Terminal persistence | SQLite | Task lifecycle | SQLite FTS5 |
| **Sub-Agent Awareness** | Best-of-N comparison | /fleet subagents | No | No | Orchestrator agent | Message board |
| **Max Parallel** | 8 (local) / 8 (cloud) | Multiple | 10+ | 23 agents | Per-kanban | Per-team |
| **Isolation** | Git worktrees / cloud VMs | Worktrees / workspace | Git worktrees | Git worktrees + SSH | Git worktrees + tmux | Git worktrees + tmux |
| **License** | Proprietary ($20/mo) | Proprietary (subscription) | ELv2 | MIT | — | — |

## Key Differentiators for claude-dashboard

Based on the feature comparison, `claude-dashboard` has several unique capabilities
that no single alternative provides:

### Unique to claude-dashboard

1. **Git status per session with 5 states:** No other monitoring tool shows
   unstaged/staged/unpushed/unmerged/merged-branch status per session with three
   merge detection strategies. ccboard and AgentsView track sessions but not git
   status. Cursor shows SCM status but only within its own IDE.

2. **One-click window foregrounding:** Platform-specific window management (Win32,
   D-Bus/GNOME Wayland, VS Code CLI fallback) is unique. Other tools either run
   inside tmux (requiring terminal attachment) or inside IDEs (requiring tab
   switching).

3. **Always-on-top borderless overlay with shade mode:** No other tool provides a
   persistent floating overlay that can minimize to a title bar. TUIs run in
   terminal windows; web dashboards run in browser tabs.

4. **System tray with priority coloring:** Surfaces the most important session state
   (permission required) at the OS level. No other tool uses system tray integration
   for agent status.

5. **Ghost sessions:** Preserving ended sessions for quick reopen is not found in
   other monitoring tools. Session browsers (AgentsView, Agent Sessions) archive
   history but don't provide one-click reopen of ended sessions in new terminals.

### Competitive Parity

1. **Session state detection:** Hooks-based, similar to ccboard and tmux-agent-indicator
2. **Permission/input notification:** Several tools detect this state
3. **Cost tracking:** ccboard has more advanced cost analytics (30-day forecast,
   4-level budgets)
4. **Sub-agent awareness:** ccboard also tracks sub-agents with parent-child trees
5. **Configurability:** ccboard offers comparable depth via config files

### Where Alternatives Excel

1. **Multi-agent support:** AgentsView (12 agents), Emdash (23 agents), Superset
   (agent-agnostic) all support more tools than claude-dashboard's Claude Code focus
2. **Full-text search:** ccboard, AgentsView, Corral all provide FTS5-powered search
   across session history
3. **Cost analytics depth:** ccboard provides 30-day forecasting, anomaly detection,
   hourly heatmaps — more analytical than claude-dashboard's daily cost display
4. **Team features:** AgentsView's PostgreSQL integration, Continue.dev's Mission
   Control, GitHub Enterprise's agent control plane
5. **Cross-session knowledge:** ccboard's "Brain" feature captures insights across
   sessions — no equivalent in claude-dashboard

## Gaps and Limitations

- No single alternative matches claude-dashboard's combination of features
- The closest competitor in scope is ccboard, which has deeper analytics but lacks
  git status, window management, and overlay UI
- Multi-agent support is the clearest gap — most competitors support 6-23 agents
  vs. claude-dashboard's Claude Code focus
- Full-text session search is absent from claude-dashboard but present in 4+
  competitors
- Team/remote collaboration features are absent from claude-dashboard
- Cost analytics depth is lower than ccboard's forecasting and budget system
