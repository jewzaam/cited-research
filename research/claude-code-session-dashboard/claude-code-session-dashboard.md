# Claude Code Session Dashboard and Multi-Session Management Tools

## Research Question

What tools exist for monitoring, managing, and navigating multiple AI coding agent
sessions running in parallel — and how do they compare to a purpose-built Claude
Code session dashboard?

## Methodology

This analysis was produced using the cited-research methodology. Every factual
claim traces to a URL visited in-session. Two independent review agents audited
the output: one checked cited URLs against source content, the other checked
numerical and logical consistency across files.

**Research conducted:** 2026-03-30

**Dimensions covered:**
1. Claude Code session monitoring tools
2. AI coding agent session managers for other tools
3. Terminal multiplexer approaches
4. Community GitHub projects for Claude Code
5. Commercial/open-source multi-agent session aggregators
6. Feature comparison matrix

See [citations.md](citations.md) for all 50 sources. Reference files for each
dimension are in [references/](references/).

---

## Executive Summary

The landscape for AI coding agent session management has exploded in 2025-2026.
Over 30 distinct tools now address some aspect of this problem, but they segment
into clear categories with different strengths:

- **IDE-native parallel agents** (Cursor [3], GitHub Copilot [4]) provide the
  deepest integration but lock you into their ecosystem
- **Cross-agent session browsers** (AgentsView [12], Agent Sessions [13]) provide
  broad visibility across 6-12 agents but are passive observers
- **Terminal multiplexer orchestrators** (agtx [9], Superset [15], dmux [33])
  provide hands-on parallel agent management via tmux
- **Comprehensive TUI dashboards** (ccboard [8]) provide deep analytics with
  cost forecasting and session knowledge

No single tool covers the full workflow that `claude-dashboard` addresses:
real-time state detection + git status per session + one-click window navigation
+ permission notification + cost tracking + session persistence — all in a
persistent overlay. The closest competitor is ccboard [8], which has deeper
analytics but lacks git status awareness, window management, and overlay UI.

---

## 1. Claude Code Native Capabilities

### Session Management

Claude Code stores sessions at `~/.claude/projects/<project>/sessions/<session-id>/`
as JSONL files [34]. Native commands:

- `claude -c` — continue last session
- `claude -r <id>` — resume specific session
- `claude --resume` — interactive session picker
- `claude --worktree` (`-w`) — start session in isolated git worktree

There is no built-in `/sessions` listing command [34]. This is a community plugin
feature.

### Monitoring via OpenTelemetry

Claude Code exports telemetry via OpenTelemetry (opt-in) with 8 metrics including
session count, cost (USD), token usage, lines of code, commits, PRs, and active
time [1]. Events cover user prompts, tool results, API requests/errors, and tool
decisions [1]. Exporters: OTLP, Prometheus, console [1].

This is a powerful data pipeline but not a dashboard — it requires setting up a
collector backend (Grafana, Datadog, Honeycomb) [1].

### Official Analytics Dashboard

Available at `claude.ai/analytics/claude-code` for Teams/Enterprise tiers only
[23]. Tracks adoption metrics, spend, and PR contributions. Not available for
individual users or CLI-only workflows [23].

### Agent Teams (Experimental)

Experimental multi-session orchestration (disabled by default, requires v2.1.32+)
[2]. One session acts as team lead coordinating 3-5 recommended teammates [2].
Shared task list with self-coordination and direct teammate messaging [2].
Significantly higher token cost [2]. Known limitations: no session resumption for
in-process teammates, task status can lag, one team per session [2].

### Hooks System

SessionStart, SessionEnd, PreToolUse, PostToolUse hooks for lifecycle events [47].
Agent teams add TeammateIdle, TaskCreated, TaskCompleted hooks [2]. These hooks are
the primary integration point for third-party monitoring tools.

---

## 2. Competing AI Coding Tools: Multi-Session Support

### Tier 1: Native Parallel Agent Support

**Cursor** is the most mature IDE with built-in parallel agents. Cursor 2.0 (October
2025) introduced up to 8 simultaneous agents [48], with infrastructure supporting
up to 20 git worktrees per workspace [3]. Background
agents (May 2025) run in cloud Ubuntu VMs, working autonomously and opening PRs on
completion [25]. "Best-of-N" execution runs the same prompt across multiple models
[3]. Reportedly compressed an 8-hour feature task into 2 hours [48].

**GitHub Copilot** provides comprehensive multi-session management. Agents tab shows
all active sessions with real-time logs [4]. Mid-session steering without stopping
runs [4]. /fleet command parallelizes with 4 specialized agents, transforming
90-second sequential handoffs into 30-second parallel analysis [5]. Session tracking
across GitHub CLI, Mobile, VS Code, Raycast, and JetBrains [26]. Enterprise agent
control plane GA February 2026 [22].

**Devin** runs each session in an isolated VM — the strongest isolation model [46].
Users spin up multiple parallel Devins working concurrently [46]. Each session
provides unified Shell, IDE, and Browser tools via the Progress Tab, with
pause/stop/resume controls [6]. Devin can schedule other Devins [46]. Cloud-only,
subscription pricing.

### Tier 2: Emerging or Limited Support

**Windsurf** added parallel multi-agent sessions with git worktrees in Wave 13 (late
2025) [17]. Side-by-side Cascade panes with background planning agent [17].
Conflicting reports on true background execution — needs verification [17].

**Continue.dev** offers Mission Control for team session management — session
assignment, shared Inbox, active run logs [18]. Strong session persistence via
`--continue` and `--resume` commands [18]. Less emphasis on parallel execution.

**Claude Code agent teams** provide multi-session via shared task list and inter-agent
messaging, but remain experimental with significant limitations [2].

### No Multi-Session Support

**Aider** — running two processes simultaneously causes log file overwrites and work
mixing [7]. Manual git worktree workaround described as "very clunky" [7].

**Cline/Roo Code** — each CLI call operates independently without conversation
continuity [29]. Community Memory Bank workaround [29].

**Amazon Q Developer** — strong agentic capabilities but no documented parallel
session support [28].

---

## 3. Terminal Multiplexer Ecosystem

tmux has become the de facto infrastructure layer for parallel AI agent workflows.
The ecosystem organizes around five patterns [discovery agent C]:

### Purpose-Built AI Agent Multiplexers

| Tool | Agents | Key Differentiator |
|------|--------|-------------------|
| **agtx** [9] | 6 | Kanban TUI + MCP orchestrator, spec-driven plugins |
| **Superset** [15] | 10+ | Agent-agnostic IDE, deep-linking to editors |
| **dmux** [33] | 11+ | One-key merge, lifecycle hooks |
| **Chloe** [32] | — | Kanban task management |
| **amux** [31] | Claude Code | Dozens of parallel agents |

### tmux Session Managers

**claude-tmux** [10] provides an all-in-one TUI for managing Claude Code instances in
tmux — session overview with 4-state indicators (Working ●, Idle ○, Waiting ◐,
Unknown ?), live preview with ANSI colors, fuzzy filtering, and create/kill/rename
[10].

**tmux-agent-indicator** [11] adds visual feedback via pane borders, window titles,
and status bar icons. Tracks running/needs-input/done states via Claude Code hooks.
Supports Claude, Codex, and OpenCode with process fallback for Aider and Cursor [11].

### Web Dashboards Over tmux

**Corral** [16] introduces the PULSE protocol — agents broadcast status via inline
markers (||PULSE:STATUS [msg]||) for real-time dashboard parsing [16]. Web UI at
localhost:8420 with agent teams, message board, and FTS5 search [16].

**Codeman** [38] provides a WebUI for tmux sessions with automation presets
(solo-work, subagent-workflow, team-lead, overnight-autonomous) and hook
auto-configuration [38].

### Zellij

Zellij support is less mature. **claude-code-zellij-status** [24] monitors Claude
Code across Zellij panes via zjstatus. Feature requests exist for native Zellij
support in Claude Code agent teams (#24122, #31901). Claude Code agent teams
currently require tmux or iTerm2 [2].

### Practical Ceiling

5-7 concurrent agents before rate limits, merge conflicts, and review bottlenecks
reduce gains [30]. Each completed agent's work must be reviewed and merged — this
bottleneck scales linearly with agent count.

---

## 4. Cross-Agent Session Aggregators

### Session Browsers

**AgentsView** [12] is the broadest cross-agent browser, supporting 12 agents with
full-text search via SQLite FTS5, activity heatmaps, tool usage analytics, and live
updates via SSE [12]. Go backend, Svelte 5 frontend, Tauri desktop. Team features
via PostgreSQL [12].

**Agent Sessions** [13] is a native macOS app (Swift, macOS 14+) supporting 6 agents.
Agent Cockpit (beta) provides live HUD for iTerm2 with active/waiting status and
Claude usage tracking [13]. Read-only, local-only, MIT license [13].

### Orchestration Platforms

**Emdash** [14] (YC W26) is provider-agnostic with 23 supported agents, git worktree
isolation, SSH/SFTP for remote development, and ticket integration for Linear,
GitHub, and Jira [14]. MIT license, local-first [14].

**Superset** [15] positions as "The Code Editor for AI Agents" — agent-agnostic, 10+
parallel agents, IDE deep-linking, MCP support [15]. Elastic License 2.0. Used at
Microsoft, OpenAI, Netflix, Google [15].

### Enterprise Governance

**ServiceNow AI Control Tower** [42] — centralized AI agent governance for
enterprises. Performance metrics, token consumption, compliance, ROI [42].

**GitHub Enterprise Agent Control Plane** [22] — session filters for discovering and
managing agent activity across organizations. GA February 2026 [22].

### Observability Platforms

**Langfuse** [41] — open-source leader (21,000+ stars, MIT). Tracing, cost tracking,
evaluation [41]. **AgentOps** [40] — session replays, time-travel debugging, prompt
injection detection. **Datadog AI Agents Console** [44] — organization-wide Claude
Code tracking.

---

## 5. Feature Comparison

### claude-dashboard's Unique Capabilities

Based on analysis of 30+ tools, these features are unique to `claude-dashboard`:

| Feature | claude-dashboard | Nearest Alternative |
|---------|:---:|---|
| **Git status per session** (5 states, 3 merge strategies) | Yes | No tool provides this |
| **One-click window foreground** (Win32, D-Bus, VS Code) | Yes | Agent Sessions (iTerm2 only) [13] |
| **Always-on-top overlay** (borderless, shade mode) | Yes | No tool provides this |
| **System tray** (priority coloring) | Yes | No tool provides this |
| **Ghost sessions** (ended sessions for reopen) | Yes | No tool provides this |

### Full Comparison: claude-dashboard vs. Closest Alternatives

| Feature | claude-dashboard | ccboard [8] | AgentsView [12] | Agent Sessions [13] |
|---------|:---:|:---:|:---:|:---:|
| Session state (real-time) | 4 states via hooks | 3 states via hooks | JSONL parsing | iTerm2 integration |
| Git status per session | 5 states, color-coded | No | No | No |
| Window navigation | One-click foreground | No | No | One-click (iTerm2) |
| Permission notification | Debounced, priority | Waiting indicator | No | Active/waiting |
| Cost tracking | OAuth usage, daily cost | Budget alerts, 30-day forecast | Analytics dashboard | Rate limits |
| Session persistence | Ghost sessions | History + Brain | SQLite archive | Archive + search |
| Sub-agent awareness | Count + debounce | Parent-child tree | No | No |
| Multi-agent support | Claude Code only | 4 agents | 12 agents | 6 agents |
| Full-text search | No | FTS5 | FTS5 | Yes |
| Team features | No | No | PostgreSQL | No |
| Platform | Windows, Linux | macOS, Linux, Win(exp) | Cross-platform | macOS only |
| UI type | Desktop overlay | TUI + Web | Desktop + Web | Native macOS |

### Where claude-dashboard Leads

1. **Git-aware session monitoring** — the combination of session state + git status
   (unstaged/staged/unpushed/unmerged/merged-branch) in a single view is unique
2. **Desktop integration** — system tray, always-on-top overlay, and platform-native
   window foregrounding provide a level of OS integration no TUI or web dashboard
   matches
3. **Permission workflow** — debounced permission detection with priority coloring in
   the system tray surfaces the most actionable state at the OS level

### Where claude-dashboard Trails

1. **Multi-agent support** — Claude Code only vs. 4-23 agents in competitors
2. **Cost analytics** — daily cost display vs. ccboard's 30-day forecasting, budget
   alerts, and anomaly detection [8]
3. **Search** — no full-text session search vs. FTS5 in ccboard, AgentsView, Corral
4. **Cross-session knowledge** — no equivalent to ccboard's "Brain" feature [8]
5. **Team collaboration** — no team features vs. AgentsView's PostgreSQL integration

---

## 6. Market Trends

Several patterns emerge from this research:

**Git worktrees are standard infrastructure.** Nearly every tool for parallel agents
uses git worktrees for isolation — Cursor [3], Copilot [27], Superset [15], Emdash
[14], agtx [9], dmux [33]. This is the convergent solution for file isolation
without full VMs.

**2025-2026 is the inflection point.** Cursor parallel agents (October 2025 [48]),
Copilot /fleet (2025-2026), Windsurf Wave 13 (late 2025 [17]), VS Code multi-agent
(February 2026 [21]), GitHub Enterprise agent control plane (February 2026 [22]).
The major IDEs all added multi-agent capabilities within a 6-month window.

**Rust is the TUI language.** ccboard [8], claude-tmux [10], agtx [9],
agent-of-empires [49] are all Rust binaries. Fast startup, small size, cross-platform.

**SQLite + FTS5 is the data layer.** ccboard [8], AgentsView [12], Corral [16] all
converge on SQLite with FTS5 for full-text session search. Local-first with optional
remote sync.

**No protocol standard.** Each tool invents its own session state detection:
hooks (ccboard, claude-dashboard), PULSE markers (Corral [16]), process detection
(tmux-agent-indicator [11]), JSONL parsing (AgentsView [12]), pane content analysis
(claude-tmux [10]).

---

## Limitations of This Analysis

- **Rapidly evolving landscape:** Many tools found are < 6 months old. Features may
  have changed since research date (2026-03-30)
- **Self-reported features:** GitHub READMEs may describe aspirational features.
  Hands-on testing was not performed
- **English-language bias:** Non-English community tools may be underrepresented
- **Adoption metrics unavailable:** GitHub stars are proxy indicators; actual user
  counts are unknown for most tools
- **Cross-source synthesis risk:** Claims drawing on multiple sources for conclusions
  (particularly the feature comparison matrix) should be independently verified
  against each tool's current documentation
