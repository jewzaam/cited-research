# Dimension 4: Community GitHub Projects for Claude Code Workflow Management

Research on open-source projects providing Claude Code workflow management,
session orchestration, or monitoring.

See [citations.md](../citations.md) for full source details.

## Project Categories

### Session Monitoring & Dashboards

| Project | Type | Language | Key Features | Citations |
|---------|------|----------|-------------|-----------|
| **ccboard** | TUI + Web | Rust | 13 tabs, budget alerts, Brain knowledge base, subagent trees | [8] |
| **claude-tmux** | TUI | Rust | tmux session manager, status indicators, live preview | [10] |
| **Stargx/claude-code-dashboard** | Web | — | Lightweight multi-session monitoring, token usage, costs | [35] |
| **claude-code-ui** | Web | — | Real-time tracker with Durable Streams, PR/CI status | — |
| **claude-code-monitor** | TUI + Mobile Web | — | Real-time dashboard with QR code mobile access (macOS) | — |
| **claude-swarm-monitor** | TUI | — | Swim lanes per agent, sub-agent tracking | — |
| **claude-dashboard** (Tpain166) | TUI | — | Real-time monitoring, conversation history | — |
| **claude-sessions-monitor** | CLI | — | Lightweight, live dashboard, web mode, history | — |

### Usage Analytics

| Project | Type | Key Features | Citations |
|---------|------|-------------|-----------|
| **ccusage** | CLI | JSONL analysis, daily/monthly/session usage, formatted tables | [36] |
| **Claude-Code-Usage-Monitor** | CLI | ML predictions, burn rate, cost analysis | — |
| **claude-JSONL-browser** | Web | JSONL to markdown converter with file explorer | — |

### Session Management

| Project | Type | Key Features | Citations |
|---------|------|-------------|-----------|
| **claude-session-manager** (PyPI) | Python lib | Context preservation, create/resume/delete | — |
| **ccmanager** | TUI | Multi-AI tool support, real-time state detection | [50] |
| **claude-sessions** (iannuttall) | Skill | Custom slash commands for session tracking | — |
| **ccswitch** | CLI | Run multiple sessions without conflicts | — |
| **plural** | CLI | Parallel sessions in separate git branches, compare approaches | — |

### Workflow Orchestration

| Project | Key Features | Citations |
|---------|-------------|-----------|
| **Citadel** (SethGammon) | Four-tier routing, campaign persistence, parallel worktree agents, 6 production skills | — |
| **Claude-Code-Workflow** (catlog22) | JSON-driven multi-agent with CLI orchestration (Gemini/Qwen/Codex) | — |
| **claude-code-workflow-orchestration** (barkain) | Auto task decomposition, parallel agents, real-time SendMessage | — |
| **agent-flow** (patoles) | Real-time visualization of agent orchestration | — |
| **claude-code-spec-workflow** (Pimzino) | Spec-driven development, 60-80% token reduction | — |

### MCP Servers

| Project | Key Features | Citations |
|---------|-------------|-----------|
| **claude-code-mcp** (steipete) | Claude Code as MCP server, session continuity, async execution | — |
| **tmux MCP server** | tmux session management via MCP | — |
| **Zellij MCP server** | Zellij session management via MCP | — |

### Awesome Lists (Meta-Resources)

| List | Scope | Citations |
|------|-------|-----------|
| **awesome-claude-code** (hesreallyhim) | Selectively curated skills, agents, plugins, hooks, tools | — |
| **awesome-claude-code-toolkit** (rohitg00) | 135 agents, 35 skills, 42 commands, 150+ plugins, 19 hooks | — |
| **awesome-claude-skills** (ComposioHQ) | Practical skills for Claude.ai, Claude Code, API | — |
| **awesome-claude-plugins** (quemsah) | Automated plugin adoption metrics via n8n | — |

### VS Code Extensions

| Extension | Key Features | Citations |
|-----------|-------------|-----------|
| **Claude Code Dashboard** (jspw) | Real-time project/session/usage/token dashboard | [37] |
| **Claude Sessions Explorer** | Browse/resume sessions from Explorer sidebar | — |
| **Beautiful Claude Code Chat** | Chat interface for Claude Code | — |

### JetBrains Plugins

| Plugin | Key Features | Citations |
|--------|-------------|-----------|
| **Claudia** | Session browser with fork/delete capabilities | — |
| **Claude Code Plus** | GUI plugin for Claude Code | — |

## Ecosystem Maturity

The Claude Code community tooling ecosystem shows clear patterns:

1. **Rust dominance for TUIs:** ccboard, claude-tmux, agent-of-empires, agtx are all
   Rust binaries — fast startup, small binaries, cross-platform
2. **SQLite + FTS5 standard:** Multiple tools converge on SQLite with FTS5 for
   full-text session search (ccboard [8], AgentsView [12], Corral [16])
3. **Hook integration standard:** Most monitoring tools use Claude Code hooks for
   real-time status rather than polling JSONL files
4. **Git worktree convergence:** Nearly all parallel execution tools use git worktrees
   for isolation

## Gaps and Limitations

- No single community project provides the complete feature set of claude-dashboard
  (session state + git status + window management + cost tracking in one tool)
- Most projects are individual/hobby-maintained with uncertain long-term support
- Fragmented ecosystem — users must combine multiple tools for a complete workflow
- Few projects support Windows (ccboard is experimental, most are macOS/Linux)
- MCP servers for session monitoring are emergent but immature
- No standard protocol for session state exchange between tools
