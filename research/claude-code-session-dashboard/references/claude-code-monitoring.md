# Dimension 1: Claude Code Session Monitoring Tools

Research on dashboards, TUIs, web UIs, and IDE extensions purpose-built for
monitoring or managing Claude Code sessions.

See [citations.md](../citations.md) for full source details.

## Official Built-in Capabilities

### Session Management (Native CLI)

Claude Code stores sessions locally at `~/.claude/projects/<project>/sessions/<session-id>/`
as JSONL files [34]. Session continuation uses `claude -c` (continue last) and
`claude -r <id>` (resume specific session). `claude --resume` provides an interactive
session picker. Sessions are scoped to directory — `/resume` shows only current
directory sessions [34].

There is no built-in `/sessions` or `/list-sessions` command — this was requested
as a community feature (GitHub issue #16901) but the feature described in
community plugins [34].

### OpenTelemetry Monitoring

Claude Code exports telemetry via OpenTelemetry (opt-in) [1]:

| Metric | Description | Unit |
|--------|-------------|------|
| `claude_code.session.count` | Sessions started | count |
| `claude_code.lines_of_code.count` | Lines modified | count |
| `claude_code.pull_request.count` | PRs created | count |
| `claude_code.commit.count` | Commits created | count |
| `claude_code.cost.usage` | Session cost | USD |
| `claude_code.token.usage` | Tokens used | tokens |
| `claude_code.code_edit_tool.decision` | Code edit permission decisions | count |
| `claude_code.active_time.total` | Active time | seconds |

Events exported: user prompts, tool results, API requests, API errors, tool
decisions [1]. No built-in dashboard — requires external backends (Grafana,
Datadog, Honeycomb, Prometheus) [1].

### Analytics Dashboard (Teams/Enterprise)

Official analytics dashboard at `claude.ai/analytics/claude-code` for Teams and
Enterprise tiers [23]. Tracks lines of code accepted, suggestion acceptance rate,
daily active users, sessions, total spend, PR contributions. Analytics API for
programmatic access (admin-only). CSV export. Leaderboard [23].

### Agent Teams (Experimental)

See [Dimension 2](other-agent-managers.md) for Claude Code agent teams as a
multi-session management feature. Experimental, requires v2.1.32+ [2].

### Hooks System

SessionStart, SessionEnd, PreToolUse, PostToolUse hooks for lifecycle events [47].
CLAUDE_ENV_FILE for session state persistence. Hooks can block operations. Agent
teams add TeammateIdle, TaskCreated, TaskCompleted hooks [2][47].

### VS Code Extension

Official Claude Code VS Code extension has sessions list in left sidebar.
Status indicators: blue dot = permission pending, orange = finished while hidden.
Supports multiple sessions per workspace folder. "Open in New Tab" / "Open in New
Window" for parallel conversations [37].

### JetBrains Plugin

Official Claude Code [Beta] plugin shares session storage with CLI/VS Code at
`~/.claude/projects/`. Can resume sessions created by other local interfaces.
Third-party "Claudia" plugin adds session browser with fork/delete [discovery agent].

## Third-Party Dashboards

### TUI (Terminal UI) Dashboards

| Tool | Language | Key Features | Sessions Supported | Stars |
|------|----------|-------------|-------------------|-------|
| **ccboard** [8] | Rust | 13 tabs, budget alerts, 30-day forecasting, Brain knowledge base, web UI | Claude Code, Cursor, Codex CLI, OpenCode | 41 |
| **claude-tmux** [10] | Rust | tmux session manager, status indicators, live preview, fuzzy filtering | Claude Code (tmux) | — |
| **claude-swarm-monitor** | — | Swim lanes per agent, live JSONL status, sub-agent tracking | Claude Code (swarm) | — |
| **claude-sessions-monitor** | — | Lightweight CLI, live dashboard, web mode (--web), history view | Claude Code | — |

**ccboard** is the most comprehensive TUI, offering 13 interactive tabs including
cost analytics, audit logs, MCP server management, and a cross-session "Brain"
knowledge base [8]. It auto-imports sessions from four agents and provides live
status via hook integration (Running ●, Waiting ◐, Stopped ✓) with subagent
parent-child tree visualization [8]. Installation via Homebrew, Cargo, or pre-built
binary (5.8MB) [8].

### Web Dashboards

| Tool | Key Features |
|------|-------------|
| **Stargx/claude-code-dashboard** [35] | Lightweight real-time multi-session monitoring, token usage, costs, active tools, subagents |
| **claude-code-ui** (KyleAMathews) | Real-time tracker with Durable Streams, PR/CI status |
| **Codeman** [38] | WebUI for Claude Code in tmux, automation presets (solo-work, subagent-workflow, team-lead, overnight-autonomous) |

### VS Code Extension Dashboards

**Claude Code Dashboard** (jspw.claude-code-dashboard) provides a real-time dashboard
showing all projects, sessions, usage, and tokens within VS Code [37].

### Usage Analytics Tools

| Tool | Type | Key Features |
|------|------|-------------|
| **ccusage** [36] | CLI | JSONL analysis, daily/monthly/session usage, formatted tables |
| **Claude-Code-Usage-Monitor** | CLI | Real-time usage, ML predictions, burn rate, cost analysis |
| **SigNoz** [43] | Enterprise | OTel dashboards, token consumption, cache efficiency |
| **Datadog** [44] | Enterprise | AI Agents Console, organization-wide tracking, ROI analysis |

### Session Management Tools

| Tool | Key Features |
|------|-------------|
| **claude-session-manager** (PyPI) | Context preservation, create/resume/delete |
| **ccmanager** [50] | Multi-AI tool manager (Claude, Gemini, Codex, Cursor), real-time state detection |
| **claude-sessions** (iannuttall) | Custom slash commands for session tracking |

## Gaps and Limitations

- No native built-in dashboard or session listing command in Claude Code CLI
- Official analytics dashboard requires Teams/Enterprise tier
- OpenTelemetry monitoring is powerful but requires infrastructure setup (collector,
  backend, dashboard) — not turnkey
- VS Code extension shows sessions per-workspace, not a unified cross-workspace view
- Third-party TUI/web dashboards are community-maintained with varying stability
- No official mobile app for session monitoring
- Session state detection relies on hooks (active integration) or JSONL parsing
  (passive, no real-time status)
