# Hooks System

Dimension: Claude Code's event-driven hook system for automation, validation, and security enforcement.

See `../citations.md` for full source details.

---

## Hook Event Types

Claude Code supports the following hook events [2]:

| Event | When It Fires | Can Block? |
|-------|--------------|------------|
| PreToolUse | After Claude creates tool parameters, before processing | Yes (exit 2 or permissionDecision: deny) |
| PostToolUse | Immediately after a tool completes successfully | Yes (decision: block), but cannot undo |
| PostToolUseFailure | When a tool execution fails | No |
| UserPromptSubmit | When the user submits a prompt, before Claude processes it | Yes (exit 2) |
| Stop | When Claude finishes responding | Yes (decision: block) |
| SubagentStart | When a subagent task begins | No (context only) |
| SubagentStop | When a subagent task completes | Yes (decision: block) |
| PreCompact | Before conversation compaction | No (context only) |
| SessionStart | When a session begins | No (context only) |
| SessionEnd | When a session ends | No (context only) |
| Notification | When Claude Code sends notifications | No |
| PermissionRequest | When a permission prompt would be shown | No (context only) |
| ConfigChange | When configuration files change during a session | Yes |
| CwdChanged | When working directory changes | No (context only) |
| FileChanged | When a file changes on disk | No (context only) |

Sources: [2], [11]

## Four Hook Types

1. **Command hooks** (`type: "command"`): Run a shell command. Receives JSON input on stdin, communicates via exit codes and stdout. [2]
2. **HTTP hooks** (`type: "http"`): Send event JSON as HTTP POST to a URL. Response body uses same JSON output format. [2]
3. **Prompt hooks** (`type: "prompt"`): Send a prompt to a Claude model for single-turn evaluation. Returns yes/no decision as JSON. [2]
4. **Agent hooks** (`type: "agent"`): Spawn a subagent that can use tools like Read, Grep, Glob to verify conditions before returning a decision. [2]

## Configuration Schema

Hooks are defined in JSON settings files with three levels of nesting [2]:

```json
{
  "hooks": {
    "EventName": [
      {
        "matcher": "ToolPattern",
        "hooks": [
          {
            "type": "command",
            "command": "your-command-here"
          }
        ]
      }
    ]
  }
}
```

### Matcher System

- `matcher` is case-sensitive, only applicable for PreToolUse and PostToolUse [2]
- Simple strings match exactly: `Write` matches only the Write tool [2]
- Pipe-separated patterns match multiple tools: `"Edit|MultiEdit|Write"` [2]
- `*` matches all tools [2]
- Empty string or omitted matcher fires on every occurrence [2]

## Exit Code Behavior

| Exit Code | Meaning | Behavior |
|-----------|---------|----------|
| 0 | Success | Claude Code parses stdout for JSON output fields [2] |
| 2 | Blocking error | Stderr text fed to Claude as error message. JSON in stdout ignored. [2] |
| Other | Non-blocking error | Stderr logged but not shown to Claude [2] |

For UserPromptSubmit and SessionStart, stdout is added as context visible to Claude. For most other events, stdout is only shown in verbose mode (Ctrl+O). [2]

## PreToolUse Output — Security-Critical

PreToolUse hooks can return permissionDecision values [2]:

| Value | Effect |
|-------|--------|
| `"allow"` | Skip the interactive permission prompt |
| `"deny"` | Cancel the tool call; reason sent to Claude as feedback |
| `"ask"` | Show the permission prompt to the user |

**Critical security property:** If a deny rule matches the tool call, the call is blocked even when a hook returns "allow". Deny rules from any settings scope, including managed (enterprise) settings, always take precedence over hook approvals. [2]

## PostToolUse and Stop Output

PostToolUse and Stop hooks use a top-level `decision: "block"` field. PostToolUse hooks cannot undo actions since the tool has already executed. [2]

Stop hooks fire whenever Claude finishes responding, not only at task completion. They do not fire on user interrupts. [2]

## What Hooks Can Do

- Block dangerous commands before execution (PreToolUse) [3]
- Add context before Claude processes prompts (UserPromptSubmit) [3]
- Log prompts with timestamps and session IDs [3]
- Validate content for dangerous patterns, secrets, or policy violations [3]
- Enforce formatting or linting after file changes (PostToolUse) [3]
- Audit configuration changes (ConfigChange) [11]

## What Hooks Cannot Do

- PostToolUse hooks cannot undo actions already taken [2]
- Hooks returning "allow" cannot override deny rules from settings [2]
- Hooks are "not a security boundary" per Trail of Bits -- they are described as "structured prompt injection at opportune times" [21]
- Hook scripts themselves can be modified by Claude via Edit/Write tools, bypassing permissions.deny [15]
- Hooks have been reported to fail completely in subdirectories (blocking CI/CD pipelines) [from search results on GitHub issues]

## Known Issues

- PreToolUse and PostToolUse hook events sometimes not fired despite proper configuration [from GitHub issue #6305]
- Hooks completely non-functional in subdirectories (v2.0.27) [from GitHub issue #10367]
- PreToolUse hooks returning "allow" previously bypassed deny permission rules including enterprise settings -- fixed in changelog [11]

## Gaps and Limitations

- No integrity checking for hook scripts (no hash validation at execution time) [15]
- No immutable hook mode to prevent Claude from modifying its own hooks [15]
- Hook reliability issues in subdirectories may affect CI/CD deployments
- Trail of Bits assessment that hooks are not a security boundary suggests they should be layered with other controls, not relied upon alone [21]
