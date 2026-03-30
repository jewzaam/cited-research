# Dimension 5: Commercial or Open-Source Multi-Agent Session Aggregators

Research on tools that aggregate sessions across multiple AI agents or coding
tools into a single interface.

See [citations.md](../citations.md) for full source details.

## Coding-Specific Session Aggregators

### Cross-Agent Session Browsers

| Tool | Agents Supported | Key Features | License | Citations |
|------|-----------------|-------------|---------|-----------|
| **AgentsView** | 12 (Claude, Codex, Copilot, Gemini, OpenCode, Cursor, Amp, iFlow, Pi, OpenClaw, Kimi, VS Code Copilot) | FTS5 search, activity heatmaps, tool analytics, velocity metrics, SSE live updates, team PostgreSQL | — | [12] |
| **Agent Sessions** | 6 (Codex CLI, Claude Code, Gemini CLI, Copilot CLI, OpenCode, Factory/Droid) | Native macOS app, Agent Cockpit (live HUD), rate limit tracking, one-click resume | MIT | [13] |
| **ccmanager** | 10+ (Claude, Gemini, Codex, Cursor, etc.) | TUI, multi-repo, real-time state detection, context transfer | — | [50] |

**AgentsView** is the broadest cross-agent browser, supporting 12 agents with full-text
search via SQLite FTS5, activity heatmaps, and team features via PostgreSQL
integration [12]. Architecture: Go backend, Svelte 5 frontend, Tauri desktop wrapper.
vim-style navigation (j/k for messages, [/] for sessions) [12].

**Agent Sessions** is the most polished single-platform offering — native macOS Swift
app with Agent Cockpit (beta) providing real-time HUD for iTerm2 sessions with
active/waiting status indicators and Claude usage tracking [13]. Read-only access
to agent directories ensures safety [13].

### Parallel Orchestration Platforms

| Tool | Architecture | Key Features | License | Citations |
|------|-------------|-------------|---------|-----------|
| **Emdash** | Desktop (Electron) | 23 agents, git worktree isolation, SSH/SFTP, ticket integration (Linear/GitHub/Jira) | MIT (YC W26) | [14] |
| **Superset** | Desktop | 10+ agents, agent-agnostic, IDE deep-linking, MCP support, port forwarding | ELv2 | [15] |
| **Corral** | Web + tmux | PULSE protocol, agent teams, message board, FTS5 search, AI summaries | — | [16] |
| **agtx** | TUI + tmux | Kanban board, MCP orchestrator, spec-driven plugins, 6 agents | — | [9] |

**Emdash** (YC W26) is the most agent-diverse orchestration platform with 23
supported agents, provider-agnostic design, and ticket integration for Linear,
GitHub, and Jira [14]. MIT license, local-first with SQLite [14].

**Superset** positions as "The Code Editor for AI Agents" with agent-agnostic
architecture supporting any CLI agent [15]. Used by developers at Microsoft,
OpenAI, Netflix, Google [15]. Elastic License 2.0 with self-hosting option [15].

**Corral** introduces the PULSE protocol where agents broadcast inline status markers
(||PULSE:STATUS [msg]||) for real-time dashboard parsing without polling [16].

## General Multi-Agent Observability Platforms

These platforms monitor AI agents broadly (not coding-specific):

### Open-Source

| Platform | Key Features | Stars | Citations |
|----------|-------------|-------|-----------|
| **Langfuse** | Tracing, cost tracking, evaluation, OpenTelemetry support | 21,000+ | [41] |
| **AgentOps** | Session replays, time-travel debugging, prompt injection detection | — | [40] |
| **Arize Phoenix** | Tracing, evaluation, LangChain/CrewAI integration | — | — |

**Langfuse** is the open-source leader with 21,000+ GitHub stars, MIT license [41].
Supports OpenTelemetry and integrates with LangChain, CrewAI, AutoGen [41].

### Commercial

| Platform | Key Features | Citations |
|----------|-------------|-----------|
| **LangSmith** | Official LangChain platform, P50/P99 latency, PagerDuty alerting | — |
| **Datadog AI Agents Console** | Organization-wide Claude Code tracking, ROI analysis | [44] |
| **SigNoz** | OTel dashboards, token consumption, cache efficiency | [43] |

## Enterprise AI Control Towers

For organizations managing dozens or hundreds of AI agents:

| Platform | Type | Key Features | Citations |
|----------|------|-------------|-----------|
| **ServiceNow AI Control Tower** | Enterprise SaaS | Centralized governance, token consumption, compliance, ROI | [42] |
| **GitHub Enterprise Agent Control Plane** | Platform | Session filters, activity tracking across organizations | [22] |
| **Covasant AI Agent Control Tower** | Enterprise SaaS | Vendor-agnostic agent governance | — |

**ServiceNow** and **Covasant** launched Control Tower products in 2025 — centralized
governance tracking performance, compliance, and ROI across all AI agents [42].

**GitHub Enterprise** (GA February 2026) provides agent control plane with session
filters for discovering and managing agent activity [22].

## Key Differentiation Patterns

The aggregator ecosystem segments into clear tiers:

1. **Developer-facing session browsers** (AgentsView, Agent Sessions): Focus on
   history, search, and analytics across past and current sessions. Read-only,
   local-first.

2. **Developer-facing orchestrators** (Emdash, Superset, agtx, Corral): Focus on
   launching, monitoring, and coordinating parallel agents in real-time. Active
   session management.

3. **Framework observability** (Langfuse, AgentOps, LangSmith): Focus on tracing,
   cost, and evaluation for LLM applications built on specific frameworks.

4. **Enterprise governance** (ServiceNow, GitHub Enterprise, Covasant): Focus on
   organizational-level visibility, compliance, and cost control across all AI
   agent activity.

## Gaps and Limitations

- No single tool provides end-to-end coverage from session management through
  cost analytics through enterprise governance
- Coding-specific aggregators are all < 1 year old — ecosystem maturity is low
- Cross-agent session browsers (AgentsView, Agent Sessions) are passive observers —
  they don't manage or control agents
- Enterprise control towers are designed for ServiceNow/ITSM workflows, not
  developer coding workflows
- Most aggregators are local-first with limited team/remote capabilities
  (AgentsView's PostgreSQL integration is the exception)
- Platform fragmentation: macOS-only (Agent Sessions), Linux-centric (most TUIs),
  cross-platform aspirational but untested
