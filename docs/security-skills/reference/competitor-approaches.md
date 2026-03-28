# Competitor Approaches to Mandatory Security Checks

## Dimension

How GitHub Copilot, Cursor, and Windsurf handle mandatory security enforcement, compared to Claude Code's hook system.

## GitHub Copilot

### Hooks System (2026)

GitHub Copilot now has a hooks system with direct parallels to Claude Code [4][5][6][25]:

- **Events**: `sessionStart`, `sessionEnd`, `userPromptSubmitted`, `preToolUse`, `postToolUse`, `errorOccurred` [6]
- **Configuration**: `.github/hooks/*.json` files committed to the repository's default branch [5]
- **Deterministic enforcement**: "Hooks are deterministic. They execute your code at specific lifecycle points with guaranteed outcomes. Unlike instructions that guide agent behavior, a hook can guarantee that a dangerous command never runs" [25]
- **Permission decisions**: `preToolUse` can return `allow`, `deny`, or `ask` [4]
- **Execution**: Multiple hooks of the same type run sequentially; if any returns "deny," the tool is blocked [4]

Key distinction from Claude Code: "Hook failures don't block execution. If a hook exits with a non-zero code or times out, Copilot logs the failure and moves on" [4]. This is a **fail-open** design for hook errors, whereas Claude Code's exit-code-other-than-0-or-2 also proceeds (similar fail-open behavior) [1].

Copilot hooks were described as the shift from "'instruction' to 'enforcement.' Writing 'please don't' in Custom Instructions versus returning `deny` in `preToolUse` are fundamentally different in certainty" [4].

### Other Security Mechanisms

- CodeQL integration for semantic analysis [from WebSearch]
- Secret detection and dependency vulnerability analysis built into GitHub platform [from WebSearch]
- Custom agents via `.github/agents/` files [from WebSearch]
- `copilot-instructions.md` for advisory guidance (non-deterministic, similar to CLAUDE.md) [from WebSearch]

## Cursor

### Hooks System (2025-2026)

Cursor released hooks for organizations "to observe, control, and extend Cursor's agent loop using custom scripts" [8].

Security partners using Cursor hooks [8]:

| Partner | Hook Type | Function |
|---|---|---|
| Semgrep | afterFileEdit + stop | Scan AI-generated code for vulnerabilities, agent regenerates until findings resolved [7] |
| Endor Labs | preToolUse | Intercept package installations, scan for malicious dependencies [27] |
| 1Password | preToolUse | Validate environment files are properly mounted before shell commands [8] |
| Noma Security | preToolUse | Real-time agent runtime security, inline decisioning before actions [10] |

Semgrep's integration is particularly notable: "Before hooks, securing coding agents with Semgrep required individual developers to opt in and explicitly prompt for security checks. Now, agent security is easy to deploy, deterministic, and fully observable across the organization" [7].

### Rules Files Are Not Deterministic

Cursor's `.cursor/rules` files are explicitly non-deterministic. Analysis from Knostic: "The AI coding tool Cursor doesn't follow rules because it is fundamentally a prediction engine rather than a policy enforcer" [9]. This directly parallels Claude Code's CLAUDE.md/skills being advisory.

### Known Vulnerabilities

The "Rules File Backdoor" (March 2025) demonstrated that malicious hidden Unicode characters in `.cursorrules` could inject instructions that "subtly modify generated code in ways that introduce security vulnerabilities while appearing completely legitimate to developers" [19].

CurXecute vulnerability (CVE-2025-54135) showed attackers could rewrite MCP configuration files through prompt injection via Slack messages [from WebSearch]. Cursor patched in version 1.3 (July 2025) with mandatory approval prompts for MCP configuration changes.

## Windsurf

### No Deterministic Hook System Found

Windsurf (formerly Codeium, acquired by Cognition AI) does **not** appear to have a deterministic hook system comparable to Claude Code or Copilot [26]. Security mechanisms found:

- `.windsurf/rules` files for advisory guidance (non-deterministic, LLM-interpreted) [from WebSearch]
- `.codeiumignore` for excluding sensitive files from AI processing [from WebSearch]
- Human-in-the-loop approval for Cascade agent actions [from WebSearch]
- Enterprise controls: SSO/SCIM, RBAC, audit logs [26]
- SOC 2 Type II and FedRAMP High certification [26]

The absence of hooks means Windsurf relies on:
1. LLM-interpreted rules (probabilistic)
2. Enterprise access controls (organizational, not per-action)
3. External CI/CD pipelines (not integrated into the agent loop)

## Comparison Matrix

| Capability | Claude Code | GitHub Copilot | Cursor | Windsurf |
|---|---|---|---|---|
| Deterministic pre-tool hooks | Yes (PreToolUse) | Yes (preToolUse) | Yes (hooks) | No |
| Deterministic post-tool hooks | Yes (PostToolUse) | Yes (postToolUse) | Yes (hooks) | No |
| Hook can block actions | Yes (exit 2) | Yes (deny) | Yes | No |
| Advisory rules file | CLAUDE.md | copilot-instructions.md | .cursorrules | .windsurf/rules |
| Enterprise managed policies | managed-settings.json | Org-level settings | Enterprise hooks | SSO/RBAC |
| Subagent hook coverage | Yes (explicit) | Unknown | Unknown | N/A |
| Hook types | command, http, prompt, agent | command | command | N/A |
| Security scanner integration | Via hooks + plugins | CodeQL + hooks | Semgrep, Endor Labs, Noma, 1Password | External only |

## Key Finding

As of March 2026, three of the four major AI coding assistants (Claude Code, GitHub Copilot, Cursor) have converged on the same architectural pattern: deterministic hooks that fire at lifecycle events, independent of LLM reasoning. Windsurf is the outlier, relying on compliance certifications and enterprise access controls instead of per-action enforcement.

The convergence validates the core thesis: LLM-interpreted rules (CLAUDE.md, .cursorrules, copilot-instructions.md, .windsurf/rules) are insufficient for security enforcement. All three hook-capable systems explicitly position hooks as the enforcement layer that compensates for the unreliability of prompt-based instructions.

## Citations

Key sources: [1] Claude Code hooks guide, [4] Copilot hooks guide, [5][6] GitHub official docs, [7] Semgrep-Cursor integration, [8] Cursor hooks blog, [9] Knostic analysis, [10] Noma Security, [19] Pillar Security rules file backdoor, [25] Copilot hooks tutorial, [26] Windsurf security, [27] Endor Labs. All citations reference `../citations.md`.
