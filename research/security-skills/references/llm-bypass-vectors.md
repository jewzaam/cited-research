# LLM Bypass Vectors and Threat Model

## Dimension

Specific ways that LLM-triggered security checks can be bypassed, and why deterministic enforcement is necessary.

## The Core Problem

Claude Code's enforcement model has been characterized as "probabilistic -- whether a rule is followed depends on whether the model 'chooses' to comply, or whether a denylist happens to cover the specific bypass vector the model attempts" [14].

LLMs "confidently drift, invent non-existing methods, misinterpret constraints, break invariants, and introduce security issues" [18]. The recommendation: "if there's a deterministic tool for the job, don't prompt the model to do the tool's work" [18].

## Bypass Vector Categories

### 1. Description Mismatch (Skills Only)

Skills trigger based on LLM interpretation of the `description` field [2][3]. Bypass occurs when:
- The user's request doesn't match the description keywords
- The LLM decides a different approach is more appropriate
- Context window pressure pushes skill descriptions out of loaded context
- The skill description budget is exceeded (2% of context window, fallback 16,000 chars) [2]

A community developer confirmed: "Claude Code often ignores available skills entirely and proceeds with generic responses instead of leveraging specialized skill knowledge" [20].

### 2. Rules File Manipulation

The "Rules File Backdoor" attack (March 2025) demonstrated that configuration files for AI coding assistants (.cursorrules, copilot-instructions.md, and by extension CLAUDE.md) can be weaponized [19]:

- Hidden Unicode characters and sophisticated evasion techniques
- "Rule files can instruct AI assistants to subtly modify generated code in ways that introduce security vulnerabilities while appearing completely legitimate to developers" [19]
- This affects ALL advisory/rules-based enforcement across all tools

### 3. Hook Script Modification

Claude Code's own tools can potentially modify hook scripts. GitHub Issue #11226 reported that "Edit/Write tools can bypass permissions.deny to modify hook scripts" [from existing citations.md, citation 15 in old numbering].

Mitigations:
- Store hooks in managed-settings.json (enterprise-controlled, cannot be overridden) [21]
- Use `allowManagedHooksOnly` to block user/project/plugin hooks [21]
- Place hook scripts outside the project directory

### 4. Denylist Gaps

The current permission system forces a denylist model [14]:
- "Every new bypass vector requires a new rule"
- Compound commands may not match individual deny patterns
- Tool aliasing or indirect execution paths may not be caught

GitHub Issue #32226 showed Claude listing GPG private keys despite `~/.gnupg/**` being in `sandbox.filesystem.denyRead` [from WebSearch].

### 5. Inter-Agent Trust Exploitation

In multi-agent systems, research showed "100% success rate" for inter-agent communication exploits [from WebSearch on LLM agent security]. "LLMs that successfully resist direct command injections will execute identical payloads when requested by peer agents."

Claude Code mitigates this partially: hooks fire for subagent actions too [1]. But the agent-to-agent trust boundary remains a concern.

### 6. Prompt Injection via Tool Outputs

When an AI coding assistant reads a file containing malicious instructions, the LLM may follow those instructions. This is distinct from hook bypass -- hooks still fire on the resulting tool calls -- but can cause the LLM to attempt unexpected actions that the hook system must then catch.

### 7. Fail-Open Design

Both Claude Code and GitHub Copilot have fail-open semantics for hook errors:
- Claude Code: exit codes other than 0 and 2 result in action proceeding [1]
- Copilot: "If a hook exits with a non-zero code or times out, Copilot logs the failure and moves on" [4]

This means a crashed security gate allows the action through. A fail-closed design (any error blocks) would be more secure but could halt all work if a hook has a bug.

## Why Deterministic Enforcement Matters

The fundamental argument from Simon Willison: "I still want my coding agents to run in a robust sandbox by default, one that restricts file access and network connections in a deterministic way. I trust those a whole lot more than prompt-based protections" [24].

The distinction between enforcement layers:

| Layer | Type | Reliability | Bypass Resistance |
|---|---|---|---|
| CLAUDE.md / .cursorrules | Advisory (LLM-interpreted) | Probabilistic | Low -- LLM can ignore |
| Skills | Advisory (LLM-triggered) | Probabilistic | Low -- may not trigger |
| Permissions (allow/deny) | Structural | High but with known bugs | Medium -- denylist gaps |
| PreToolUse hooks | Deterministic (code-level) | High | High -- outside LLM |
| OS Sandbox | Deterministic (OS-level) | Highest | Highest -- kernel-enforced |
| Managed settings | Organizational | High | High -- cannot be overridden |

## The Defense-in-Depth Model

No single layer is sufficient. The recommended stack from strongest to weakest:

1. **OS sandbox** (bubblewrap/seatbelt) -- kernel-level filesystem and network isolation [from existing research]
2. **Managed settings** -- enterprise-controlled deny rules that cannot be overridden [30]
3. **PreToolUse hooks** -- deterministic per-action gates for security checks [1]
4. **PostToolUse hooks** -- deterministic post-action validation [1]
5. **Permission rules** -- structural allow/deny (has known bugs) [30]
6. **CLAUDE.md / rules** -- advisory guidance (probabilistic) [2]
7. **Skills** -- LLM-triggered specialized instructions (probabilistic) [2][3]

## Citations

Key sources: [1] Official hooks guide, [2] Official skills docs, [3] Skills deep dive, [14] GitHub Issue #37471, [18] Agentic coding guardrails, [19] Rules file backdoor, [20] Mandatory skill hook, [21] MintMCP enterprise security, [24] Simon Willison, [30] Permissions documentation. All citations reference `../citations.md`.
