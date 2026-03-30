# Claude Code Session Dashboard: Competitive Landscape

**What this answers:** What tools exist for monitoring, managing, and navigating
multiple AI coding agent sessions in parallel — and where does `claude-dashboard`
fit?

**Research date:** 2026-03-30 | **Sources:** [50 citations](citations.md)

---

## TL;DR

Over 30 tools address some aspect of AI coding agent session management. They
segment into four categories: IDE-native parallel agents (Cursor, Copilot),
cross-agent session browsers (AgentsView, Agent Sessions), terminal multiplexer
orchestrators (agtx, Superset, dmux), and comprehensive dashboards (ccboard).

**No single tool replicates claude-dashboard's combination** of real-time session
state + git status per session + one-click window foregrounding + permission
notification + system tray overlay. The closest competitor is **ccboard** (Rust
TUI + web), which has deeper analytics (30-day cost forecasting, budget alerts,
cross-session knowledge base) but lacks git status awareness, window management,
and overlay UI.

The main competitive gap is **multi-agent support** — AgentsView supports 12
agents, Emdash supports 23, while claude-dashboard is Claude Code-only.

## Key Comparison

| Feature | claude-dashboard | ccboard | AgentsView | Cursor | Copilot |
|---------|:---:|:---:|:---:|:---:|:---:|
| Git status per session | **Unique** | No | No | SCM pane | PR workflow |
| Window foreground | **Unique** | No | No | IDE tabs | Web/CLI |
| Always-on-top overlay | **Unique** | No | No | No | No |
| System tray + priority | **Unique** | No | No | No | No |
| Ghost sessions | **Unique** | No | No | No | No |
| Session state detection | 4 states | 3 states | JSONL | Built-in | Session logs |
| Cost tracking | Daily | 30-day forecast | Analytics | Subscription | Premium req. |
| Sub-agent awareness | Count | Parent tree | No | Best-of-N | /fleet |
| Full-text search | No | FTS5 | FTS5 | No | No |
| Multi-agent support | Claude only | 4 agents | 12 agents | Cursor only | Copilot only |
| Team features | No | No | PostgreSQL | Teams plan | Enterprise |

## Decision Framework

When sharing claude-dashboard with teammates, position it based on their workflow:

1. **"I run 3+ Claude Code sessions in parallel"** → claude-dashboard is purpose-built
   for this. No other tool provides git status + window management + permission
   notification in a single overlay.

2. **"I use Cursor/Copilot, not Claude Code CLI"** → Those IDEs have built-in
   parallel agent support. claude-dashboard doesn't apply unless they also run
   Claude Code CLI sessions.

3. **"I use multiple AI coding tools"** → Recommend **AgentsView** (12 agents) or
   **Emdash** (23 agents) alongside claude-dashboard for cross-tool visibility.

4. **"I want deep cost analytics"** → Recommend **ccboard** alongside
   claude-dashboard — ccboard has 30-day forecasting, budget alerts, anomaly
   detection.

5. **"I want team-wide visibility"** → Claude Code's official analytics dashboard
   (Teams/Enterprise) or **AgentsView** with PostgreSQL for team aggregation.

## Files

| File | Description |
|------|-------------|
| [claude-code-session-dashboard.md](claude-code-session-dashboard.md) | Full analysis with methodology |
| [citations.md](citations.md) | All 50 sources, numbered |
| [references/claude-code-monitoring.md](references/claude-code-monitoring.md) | Dimension 1: Claude Code monitoring tools |
| [references/other-agent-managers.md](references/other-agent-managers.md) | Dimension 2: Other AI agent session managers |
| [references/terminal-multiplexer.md](references/terminal-multiplexer.md) | Dimension 3: Terminal multiplexer approaches |
| [references/community-github-projects.md](references/community-github-projects.md) | Dimension 4: Community GitHub projects |
| [references/multi-agent-aggregators.md](references/multi-agent-aggregators.md) | Dimension 5: Multi-agent aggregators |
| [references/feature-comparison.md](references/feature-comparison.md) | Dimension 6: Feature comparison matrix |
| [audit/citation-audit.md](audit/citation-audit.md) | Citation verification results |
| [audit/consistency-review.md](audit/consistency-review.md) | Cross-file consistency check |
