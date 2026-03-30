# Dimension 3: Terminal Multiplexer Approaches for AI Agent Workflows

Research on tmux, screen, Zellij, and similar terminal multiplexer integrations
adapted for AI coding agent workflows.

See [citations.md](../citations.md) for full source details.

## Architectural Patterns

The terminal multiplexer ecosystem for AI agent workflows has converged on five
distinct patterns [discovery agent C]:

### Pattern 1: Session Persistence

The foundational use case. AI agents run in tmux sessions that survive SSH
disconnections, laptop closures, and network drops. Configuration typically
involves binding a hotkey to spawn Claude Code in a tmux popup, with session
names derived from directory MD5 hashes for one-session-per-project [30].

### Pattern 2: Parallel Multi-Agent

The most sophisticated pattern runs 4-8 agents in parallel, each in isolated tmux
panes/windows with git worktrees. Practical ceiling is 5-7 concurrent agents before
rate limits, merge conflicts, and review bottlenecks reduce gains [30].

### Pattern 3: Status Visibility

Plugins expose agent state in the tmux status bar. **tmux-agent-indicator** tracks
three states (running, needs-input, done) via Claude Code hooks, displaying through
pane borders, window titles, and status bar icons [11].

### Pattern 4: Orchestration

Orchestrator agents manage teams of worker agents via tmux. **agtx** features
an orchestrator that manages a kanban board via MCP [9]. Separate planning agents
from coding agents using tmux to isolate and coordinate.

### Pattern 5: Hook-Driven Automation

Claude Code's hooks system integrates with tmux for lifecycle automation [47][38].
**Codeman** provides presets for automation workflows (solo-work, subagent-workflow,
team-lead, overnight-autonomous) [38].

## Key Tools

### tmux-Native Session Managers

| Tool | Language | Key Features |
|------|----------|-------------|
| **claude-tmux** [10] | Rust | All-session view, status indicators (●○◐?), live preview, fuzzy filter, create/kill/rename |
| **tmux-agent-indicator** [11] | Bash | 3-state tracking via hooks, pane borders/window titles/status icons, supports Claude/Codex/OpenCode |
| **tmux-agent-status** | Bash | At-a-glance status for which sessions have Claude working vs idle |
| **claude-session-driver** | — | Controller session launches workers in tmux, monitors progress, reviews tool calls |

### Purpose-Built AI Agent Multiplexers

| Tool | Key Features |
|------|-------------|
| **agtx** [9] | Kanban TUI, MCP orchestrator, spec-driven plugins, 6 supported agents, Rust |
| **Superset** [15] | 10+ parallel agents, agent-agnostic, IDE deep-linking, worktree isolation |
| **dmux** [33] | Worktree + tmux, one-key merge, lifecycle hooks, 11+ agents |
| **Chloe** [32] | Terminal multiplexer for AI agents with Kanban task management |
| **amux** [31] | Claude Code multiplexer for dozens of parallel agents |
| **Agent of Empires** [49] | Rust TUI on tmux, visual interface, keyboard shortcuts |

### Orchestration Platforms

| Tool | Key Features |
|------|-------------|
| **Corral** [16] | Python + JS, PULSE protocol for real-time status, agent teams with worktrees, message board, FTS5 search |
| **KanVibe** [39] | Self-hosted Kanban with browser terminals, tmux + Zellij support, hook-driven tracking |
| **Codeman** [38] | WebUI for tmux sessions, 4 automation presets, hook auto-configuration |
| **ccmanager** [50] | Multi-AI session manager, 10+ agents, context transfer, automation hooks |

### Web-Based Dashboards Over tmux

| Tool | Key Features |
|------|-------------|
| **Corral** [16] | FastAPI dashboard at localhost:8420 with PULSE protocol |
| **Codeman** [38] | Modern WebUI for tmux session management |
| **KanVibe** [39] | Browser-based Kanban with embedded terminals |
| **AgentDock** | Web dashboard for parallel agents with tmux + worktrees |

## Zellij Integration

Zellij support exists but is less mature than tmux:

| Tool/Resource | Status |
|---------------|--------|
| **claude-code-zellij-status** [24] | Monitors Claude Code across Zellij panes via zjstatus |
| **Zellij MCP Server** | MCP server for Zellij session management |
| **Feature requests** | Claude Code issues #24122 (split-pane) and #31901 (native support as tmux alternative) |
| **KanVibe** [39] | Supports both tmux and Zellij |

Claude Code agent teams currently require tmux or iTerm2 for split-pane mode —
Zellij is not natively supported [2].

## Technical Configuration Patterns

Key tmux settings for AI agent workflows [discovery agent C]:

- **Scrollback limits:** Increase to 50,000+ lines for AI panes
- **Agent teams:** `CLAUDE_CODE_SPAWN_BACKEND=tmux` for split-pane mode
- **Session naming:** Directory hashing or manual naming for organization
- **Notification systems:** Sound alerts (chime, bell, fanfare, TTS) on completion
- **Permission systems:** Range from auto-approve to per-command confirmation

## Gaps and Limitations

- **tmux dominance:** Screen has negligible AI agent integration; Zellij is emerging
  but immature for this use case
- **No standardized protocol:** Each tool invents its own status detection mechanism
  (hooks, PULSE markers, process detection, JSONL parsing)
- **Practical agent ceiling:** 5-7 concurrent agents before rate limits and review
  bottleneck reduce gains [30]
- **Port conflicts:** tmux isolates files (via worktrees) but not runtime — agents
  share ports, databases, and services
- **Manual merge burden:** Each completed agent's work must be reviewed and merged,
  creating a bottleneck that scales linearly with agent count
- **Zellij feature gap:** No native support in Claude Code agent teams [2]; community
  tools fill the gap partially [24]
