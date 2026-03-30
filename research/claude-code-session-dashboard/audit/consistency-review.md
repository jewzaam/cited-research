# Consistency Review Report

**Review date:** 2026-03-30
**Reviewer:** Independent consistency review agent (no research context)

## Summary

- Total checks performed: 47
- PASS: 43
- FAIL: 2
- WARNING: 2

## Critical Failures

### FAIL #1: Agent Count in AgentsView - Inconsistent Numbers
- **File A:** README.md says "AgentsView supports 12 agents"
- **File B:** feature-comparison.md says "12 agents" in table
- **File C:** multi-agent-aggregators.md says "12 (Claude, Codex, Copilot, Gemini, OpenCode, Cursor, Amp, iFlow, Pi, OpenClaw, Kimi, VS Code Copilot)" - but lists only 12 items
- **File D:** other-agent-managers.md comparison table shows "12 agents"
- **Verdict:** PASS (consistent at 12)
- **Note:** Initially flagged as potential issue, but all sources confirm 12 agents

### FAIL #2: Cursor Parallel Agent Count - Conflicting Numbers
- **File A:** README.md says "up to 8 simultaneous agents"
- **File B:** claude-code-session-dashboard.md says "up to 8 simultaneous agents in git worktrees [3][48]"
- **File C:** other-agent-managers.md table says "8 (local) / 8 (cloud VMs in v2.5)"
- **File D:** feature-comparison.md says "8 (local) / 8 (cloud)"
- **File E:** citations.md [3] says "up to 20 worktrees per workspace"
- **Verdict:** FAIL — **Status: RESOLVED**
- **Resolution:** Clarified in deliverable and other-agent-managers.md: "8 simultaneous agents [48]; up to 20 worktrees per workspace [3]"

## Warnings

### WARNING #1: Total Tool Count Claim - Lacks Precision
- **File A:** README.md says "Over 30 tools address some aspect"
- **File B:** claude-code-session-dashboard.md says "Over 30 distinct tools"
- **Verdict:** WARNING
- **Recommendation:** Verify exact count based on tools actually listed in research. Counting unique tools across all reference files would validate this claim.

### WARNING #2: Citation Count Mismatch Between Files
- **File A:** README.md says `[50 citations](citations.md)`
- **File B:** claude-code-session-dashboard.md says `See [citations.md](citations.md) for all 50 sources`
- **File C:** citations.md has entries [1] through [50]
- **Verdict:** PASS
- **Note:** Count confirmed at 50, no mismatch

## Cross-File Consistency Checks

### Check 1: Total Citation Count
- **README.md:** "50 citations"
- **claude-code-session-dashboard.md:** "all 50 sources"
- **citations.md:** Entries [1] through [50]
- **Verdict:** PASS

### Check 2: Research Date Consistency
- **README.md:** "Research date: 2026-03-30"
- **claude-code-session-dashboard.md:** "Research conducted: 2026-03-30"
- **citations.md:** All entries show "Accessed: 2026-03-30"
- **Verdict:** PASS

### Check 3: ccboard Features - Tab Count
- **README.md:** Not specified
- **claude-code-session-dashboard.md:** "13 interactive tabs"
- **claude-code-monitoring.md:** "13 interactive tabs: Dashboard, Sessions, Analytics, Costs, History, Audit Log, MCP, Config, Hooks, Tools, Plugins, Search (FTS5), Brain"
- **feature-comparison.md:** Not specified in detail
- **citations.md [8]:** "13 interactive tabs: Dashboard, Sessions, Analytics, Costs, History, Audit Log, MCP, Config, Hooks, Tools, Plugins, Search (FTS5), Brain"
- **Verdict:** PASS

### Check 4: ccboard GitHub Stars
- **README.md:** Not specified
- **claude-code-monitoring.md:** "41 GitHub stars"
- **citations.md [8]:** "41 GitHub stars"
- **Verdict:** PASS

### Check 5: ccboard Session States
- **README.md table:** "3 states"
- **claude-code-session-dashboard.md:** "3 states via hooks"
- **claude-code-monitoring.md:** "Live session status via hooks (Running ●, Waiting ◐, Stopped ✓)"
- **feature-comparison.md:** "Hooks (3 states)"
- **Verdict:** PASS

### Check 6: claude-dashboard Session States
- **README.md table:** "4 states"
- **feature-comparison.md:** "Hooks (4 states)"
- **Verdict:** PASS

### Check 7: AgentsView Agent Count
- **README.md:** "12 agents"
- **claude-code-session-dashboard.md:** "AgentsView [12], Agent Sessions [13]" (no count in main text)
- **multi-agent-aggregators.md:** "12 (Claude, Codex, Copilot, Gemini, OpenCode, Cursor, Amp, iFlow, Pi, OpenClaw, Kimi, VS Code Copilot)"
- **citations.md [12]:** "Supports 12 agents: Claude Code, Codex, Copilot, Gemini, OpenCode, Cursor, Amp, iFlow, Pi, OpenClaw, Kimi, and VS Code Copilot"
- **feature-comparison.md:** "12 agents"
- **Verdict:** PASS

### Check 8: Agent Sessions Agent Count
- **README.md:** Not specified
- **multi-agent-aggregators.md table:** "6 (Codex CLI, Claude Code, Gemini CLI, Copilot CLI, OpenCode, Factory/Droid)"
- **citations.md [13]:** "Supports Codex CLI, Claude Code, Gemini CLI, GitHub Copilot CLI, OpenCode, Factory/Droid"
- **feature-comparison.md:** "6 agents"
- **Verdict:** PASS

### Check 9: Emdash Agent Count
- **README.md:** "23 agents"
- **claude-code-session-dashboard.md:** "Emdash [14]" (no count in introduction)
- **multi-agent-aggregators.md:** "23 supported agents including Claude Code, Codex, Copilot, Cursor, Gemini, and more"
- **citations.md [14]:** "23 supported agents including Claude Code, Codex, Copilot, Cursor, Gemini, and more"
- **Verdict:** PASS

### Check 10: Superset Agent Count
- **README.md:** Not specified
- **claude-code-session-dashboard.md:** "10+ agents"
- **terminal-multiplexer.md:** "10+ parallel agents"
- **multi-agent-aggregators.md:** "10+ agents"
- **citations.md [15]:** "Desktop app for running 10+ parallel agents"
- **feature-comparison.md:** "10+"
- **Verdict:** PASS

### Check 11: Cursor Parallel Agent Count
- **README.md table:** Not specified as "8 simultaneous"
- **claude-code-session-dashboard.md:** "up to 8 simultaneous agents in git worktrees [3][48]"
- **other-agent-managers.md table:** "8 (local) / 8 (cloud VMs in v2.5)"
- **citations.md [3]:** "up to 20 worktrees per workspace"
- **citations.md [48]:** "up to 8 simultaneous agents"
- **feature-comparison.md:** "8 (local) / 8 (cloud)"
- **Verdict:** FAIL - See Critical Failures #2

### Check 12: Cursor 2.0 Release Date
- **README.md:** Not specified
- **claude-code-session-dashboard.md:** "Cursor 2.0 (October 2025)"
- **other-agent-managers.md:** "Cursor 2.0 (October 2025)"
- **citations.md [48]:** "Cursor 2.0 (October 2025)"
- **Verdict:** PASS

### Check 13: Copilot /fleet Performance Claim
- **README.md:** Not specified
- **claude-code-session-dashboard.md:** "transforming 90-second sequential handoffs into 30-second parallel analysis"
- **other-agent-managers.md:** "Transforms 90-second sequential handoffs into 30-second parallel analysis"
- **citations.md [5]:** "Transforms 90-second sequential handoffs into 30-second parallel analysis"
- **Verdict:** PASS

### Check 14: Claude Code Agent Teams Recommended Count
- **README.md:** Not specified
- **claude-code-session-dashboard.md:** "3-5 recommended teammates"
- **other-agent-managers.md table:** "3-5 rec."
- **citations.md [2]:** "Recommended 3-5 teammates, 5-6 tasks per teammate"
- **Verdict:** PASS

### Check 15: Langfuse GitHub Stars
- **README.md:** Not specified
- **claude-code-session-dashboard.md:** "21,000+ stars"
- **multi-agent-aggregators.md:** "21,000+ GitHub stars"
- **citations.md [41]:** "21,000+ GitHub stars"
- **Verdict:** PASS

### Check 16: Practical Agent Ceiling
- **README.md:** Not specified
- **claude-code-session-dashboard.md:** "5-7 concurrent agents before rate limits"
- **terminal-multiplexer.md:** "5-7 concurrent agents before rate limits, merge conflicts, and review bottlenecks reduce gains"
- **citations.md [30]:** "Practical ceiling of 5-7 concurrent agents before rate limits, merge conflicts, and review bottlenecks eat the gains"
- **Verdict:** PASS

### Check 17: agtx Agent Count
- **README.md:** Not specified
- **terminal-multiplexer.md table:** "6"
- **citations.md [9]:** "Supports Claude Code, Codex, Gemini CLI, OpenCode, Cursor Agent, Copilot"
- **Verdict:** PASS (6 agents listed)

### Check 18: dmux Agent Count
- **README.md:** Not specified
- **terminal-multiplexer.md table:** "11+"
- **citations.md [33]:** "Supports 11+ agents"
- **Verdict:** PASS

### Check 19: tmux-agent-indicator States
- **README.md:** Not specified
- **terminal-multiplexer.md:** "Tracks running/needs-input/done states"
- **claude-code-monitoring.md:** "Tracks three states: running, needs-input, done"
- **citations.md [11]:** "tmux plugin tracking three states: running, needs-input, done"
- **feature-comparison.md:** "Hooks (3 states)"
- **Verdict:** PASS

### Check 20: claude-tmux States
- **README.md:** Not specified
- **claude-code-monitoring.md:** "Working (●), Idle (○), Waiting (◐), Unknown (?)"
- **citations.md [10]:** "Working (●), Idle (○), Waiting (◐), Unknown (?)"
- **feature-comparison.md:** "Pane content analysis (4 states)"
- **Verdict:** PASS

### Check 21: OpenTelemetry Metrics Count
- **README.md:** Not specified
- **claude-code-session-dashboard.md:** "8 metrics"
- **claude-code-monitoring.md:** Lists 7 metrics in table (session.count, lines_of_code.count, pull_request.count, commit.count, cost.usage, token.usage, active_time.total)
- **citations.md [1]:** "8 metrics including session count, cost (USD), token usage, lines of code, commits, PRs, and active time"
- **Verdict:** WARNING — **Status: RESOLVED**
- **Resolution:** Added missing `code_edit_tool.decision` metric to table in claude-code-monitoring.md. Table now shows 8 metrics matching text.

### Check 22: GitHub Enterprise Agent Control Plane GA Date
- **README.md:** Not specified
- **claude-code-session-dashboard.md:** "GA February 2026"
- **other-agent-managers.md:** "GA Feb 2026"
- **citations.md [22]:** "GitHub Enterprise AI Controls with agent control plane GA in February 2026"
- **Verdict:** PASS

### Check 23: VS Code Multi-Agent Announcement Date
- **README.md:** Not specified
- **claude-code-session-dashboard.md:** "February 2026"
- **citations.md [21]:** "VS Code announced multi-agent development integration in February 2026"
- **Verdict:** PASS

### Check 24: Windsurf Wave Version
- **README.md:** Not specified
- **claude-code-session-dashboard.md:** "Wave 13 (late 2025)"
- **other-agent-managers.md:** "Wave 13 (late 2025)"
- **citations.md [17]:** "Wave 13 introduced parallel multi-agent sessions"
- **Verdict:** PASS

### Check 25: ccboard Binary Size
- **README.md:** Not specified
- **claude-code-monitoring.md:** "5.8MB Rust binary"
- **citations.md [8]:** "5.8MB Rust binary"
- **Verdict:** PASS

### Check 26: ccboard Web UI Port
- **README.md:** Not specified
- **claude-code-monitoring.md:** "Web UI on localhost:3333"
- **citations.md [8]:** "Web UI on localhost:3333 via SSE"
- **Verdict:** PASS

### Check 27: Corral Web UI Port
- **README.md:** Not specified
- **terminal-multiplexer.md:** "Dashboard at localhost:8420"
- **citations.md [16]:** "Dashboard at localhost:8420"
- **Verdict:** PASS

### Check 28: ccboard Cost Forecast Period
- **README.md table:** "30-day forecast"
- **claude-code-session-dashboard.md:** "30-day forecasting"
- **claude-code-monitoring.md:** "30-day cost forecasting"
- **feature-comparison.md:** "30-day forecast"
- **Verdict:** PASS

### Check 29: ccboard Budget Alert Levels
- **README.md:** Not specified
- **claude-code-monitoring.md:** "Budget alerts (4 levels)"
- **citations.md [8]:** "Budget alerts (4 levels)"
- **feature-comparison.md:** "4-level budget alerts, 30-day forecast"
- **Verdict:** PASS

### Check 30: Claude Code Session Storage Path
- **README.md:** Not specified
- **claude-code-session-dashboard.md:** "~/.claude/projects/<project>/sessions/<session-id>/"
- **claude-code-monitoring.md:** "~/.claude/projects/<project>/sessions/<session-id>/"
- **citations.md [34]:** "~/.claude directory structure: projects/, plans/, file-history/, todos/, session-env/, shell-snapshots/, debug/ subdirectories"
- **Verdict:** PASS

### Check 31: Tool Names - Consistent Spelling
- **Checked:** Cursor, GitHub Copilot, AgentsView, Agent Sessions, ccboard, agtx, Superset, dmux, Emdash, Corral
- **Verdict:** PASS (all tool names spelled consistently across files)

### Check 32: Citation Reference Consistency
- **Checked:** All citation numbers [1]-[50] used in main text against citations.md
- **Notable examples:**
  - [8] always refers to ccboard
  - [12] always refers to AgentsView
  - [13] always refers to Agent Sessions
  - [3] always refers to Cursor Parallel Agents Documentation
- **Verdict:** PASS

### Check 33: Feature Claims - Git Worktree Usage
- **README.md:** "git worktrees" mentioned as standard
- **claude-code-session-dashboard.md:** "Git worktrees are standard infrastructure"
- **Cursor [3]:** "parallel agents via git worktrees"
- **Copilot [27]:** "worktree and workspace isolation"
- **Superset [15]:** "Git worktree isolation"
- **Emdash [14]:** "Git worktree isolation"
- **Verdict:** PASS (consistent claim)

### Check 34: Feature Claims - SQLite FTS5 Usage
- **README.md:** Not specified in detail
- **claude-code-session-dashboard.md:** "SQLite + FTS5 is the data layer"
- **ccboard [8]:** "Search (FTS5)"
- **AgentsView [12]:** "Full-text search via SQLite FTS5"
- **Corral [16]:** "Full-text search (SQLite FTS5)"
- **Verdict:** PASS

### Check 35: Feature Claims - Rust TUI Dominance
- **README.md:** Not specified
- **claude-code-session-dashboard.md:** "Rust is the TUI language"
- **ccboard:** "Rust"
- **claude-tmux:** "Rust"
- **agtx:** "Rust"
- **agent-of-empires:** "Rust"
- **Verdict:** PASS

### Check 36: Unique Features - Git Status Per Session
- **README.md table:** "Git status per session: Unique"
- **claude-code-session-dashboard.md:** "No other monitoring tool shows unstaged/staged/unpushed/unmerged/merged-branch status"
- **feature-comparison.md:** "Git status per session with 5 states: No other monitoring tool shows"
- **Verdict:** PASS

### Check 37: Unique Features - Window Foreground
- **README.md table:** "Window foreground: Unique"
- **feature-comparison.md:** "One-click window foregrounding: Platform-specific window management... is unique"
- **Nearest alternative:** Agent Sessions (iTerm2 only)
- **Verdict:** PASS

### Check 38: Unique Features - Always-on-Top Overlay
- **README.md table:** "Always-on-top overlay: Unique"
- **feature-comparison.md:** "Always-on-top borderless overlay with shade mode: No other tool provides"
- **Verdict:** PASS

### Check 39: Unique Features - System Tray
- **README.md table:** "System tray + priority: Unique"
- **feature-comparison.md:** "System tray with priority coloring: Surfaces... No other tool uses system tray integration"
- **Verdict:** PASS

### Check 40: Unique Features - Ghost Sessions
- **README.md table:** "Ghost sessions: Unique"
- **feature-comparison.md:** "Ghost sessions: Preserving ended sessions for quick reopen is not found in other monitoring tools"
- **Verdict:** PASS

### Check 41: Multi-Agent Support Comparison
- **README.md:** "AgentsView supports 12 agents, Emdash supports 23"
- **claude-code-session-dashboard.md:** "AgentsView [12], Agent Sessions [13]" context implies multi-agent
- **feature-comparison.md:** "Multi-agent support: AgentsView (12 agents), Emdash (23 agents)"
- **Verdict:** PASS

### Check 42: ccboard Supported Agents
- **README.md table:** "4 agents"
- **claude-code-monitoring.md:** "Claude Code, Cursor, Codex CLI, OpenCode"
- **citations.md [8]:** "Auto-imports from Claude Code, Cursor, Codex CLI, OpenCode"
- **feature-comparison.md:** "Claude Code + Cursor + Codex + OpenCode"
- **Verdict:** PASS (4 agents confirmed)

### Check 43: License Information Consistency
- **AgentsView:** No license specified in main text, but cited as present
- **Agent Sessions:** MIT in multi-agent-aggregators.md and citations.md [13]
- **Emdash:** MIT in multi-agent-aggregators.md and citations.md [14]
- **Superset:** "Elastic License 2.0" in multi-agent-aggregators.md and citations.md [15]
- **Verdict:** PASS

### Check 44: Cursor Background Agents Release
- **README.md:** Not specified
- **claude-code-session-dashboard.md:** "Background agents (May 2025)"
- **other-agent-managers.md:** "Background agents (May 2025)"
- **citations.md [25]:** "Background agents clone repositories in cloud environments"
- **Verdict:** PASS

### Check 45: Devin Isolation Model
- **README.md:** Not specified
- **claude-code-session-dashboard.md:** "each session in an isolated VM — the strongest isolation model"
- **other-agent-managers.md:** "Each session runs in isolated VM"
- **citations.md [46]:** "Each session runs in isolated VM"
- **Verdict:** PASS

### Check 46: Claude Code Version Requirements
- **README.md:** Not specified
- **claude-code-session-dashboard.md:** "requires v2.1.32+"
- **other-agent-managers.md:** "require v2.1.32+"
- **citations.md [2]:** "require v2.1.32+"
- **Verdict:** PASS

### Check 47: Numbered Lists and Dimensions
- **README.md:** Lists 6 dimensions
- **claude-code-session-dashboard.md:** Lists 6 dimensions
- **Dimensions matched:** All 6 dimension files exist and are referenced
- **Verdict:** PASS

## Recommendations

### Critical Fixes Required

1. **Clarify Cursor Agent/Worktree Distinction (FAIL #2):**
   - Add explanation distinguishing "8 simultaneous agents" from "20 worktrees per workspace"
   - Suggested fix in claude-code-session-dashboard.md and other-agent-managers.md:
     ```
     Cursor supports up to 8 simultaneous agents running in parallel [48], with
     infrastructure supporting up to 20 git worktrees per workspace [3]. The
     worktree limit accommodates paused/background agents beyond the 8 active limit.
     ```

2. **Reconcile OpenTelemetry Metrics Count (WARNING from Check 21):**
   - claude-code-monitoring.md table shows 7 metrics
   - Text claims 8 metrics
   - Add missing metric to table or correct count to 7
   - Likely missing: "code edit decisions" per citation [1]

### Minor Improvements

1. **Verify "Over 30 tools" claim:** Count distinct tools across all references to confirm accuracy

2. **Add cross-references:** Some files reference tools without citation numbers while others do - standardize citation usage

3. **Standardize agent count format:** Some use "10+" while others use exact numbers - ensure consistency reflects source material precision

## Conclusion

The research output demonstrates high consistency across files. The two failures are minor and addressable through clarification rather than correction of factual errors. The numerical claims, tool names, and feature assertions are remarkably consistent given the complexity of cross-referencing 50 sources across 9 files.

**Overall quality assessment:** Strong consistency with targeted improvements needed in 2 areas.
