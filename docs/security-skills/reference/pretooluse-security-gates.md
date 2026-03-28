# PreToolUse Hooks as Deterministic Security Gates

## Dimension

How PreToolUse hooks function as mandatory security gates that fire on every tool invocation matching the matcher pattern, with specific patterns for dependency management, file protection, and command validation.

## PreToolUse Hook Architecture

PreToolUse hooks fire "before a tool call executes" and "can block it" [1]. The hook receives JSON input on stdin containing `tool_name` and `tool_input` (e.g., the exact command string for Bash tools) [1].

### Exit Code Semantics

The exit code is the enforcement mechanism [1]:

- **Exit 0**: Action proceeds (allow)
- **Exit 2**: Action is blocked. Stderr message is fed back to Claude as feedback
- **Any other exit code**: Action proceeds (non-blocking error, logged but not shown to Claude)

A critical implementation detail: "The most common hook mistake: writing a security gate with exit 1 instead of exit 2. The hook appears to work during testing because the warning message prints to the terminal. But exit 1 is a non-blocking warning. The dangerous command still executes" [15].

### Structured JSON Output

For more granular control, hooks can return JSON on stdout [1]:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Use rg instead of grep for better performance"
  }
}
```

Three permission decisions are available: `"allow"` (skip interactive prompt), `"deny"` (cancel tool call), `"ask"` (show permission prompt to user) [1].

### Precedence Rules

"Returning 'allow' skips the interactive prompt but does not override permission rules. If a deny rule matches the tool call, the call is blocked even when your hook returns 'allow'" [1]. Deny rules from managed settings always take precedence over hook approvals [1].

## Security Gate Patterns

### Pattern 1: Block Edits to Protected Files

From official documentation, a `protect-files.sh` script [1]:

```bash
#!/bin/bash
INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')
PROTECTED_PATTERNS=(".env" "package-lock.json" ".git/")
for pattern in "${PROTECTED_PATTERNS[@]}"; do
  if [[ "$FILE_PATH" == *"$pattern"* ]]; then
    echo "Blocked: $FILE_PATH matches protected pattern '$pattern'" >&2
    exit 2
  fi
done
exit 0
```

Configuration:
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/protect-files.sh"
          }
        ]
      }
    ]
  }
}
```

### Pattern 2: Block Dangerous Bash Commands

From official documentation [1]:

```bash
#!/bin/bash
INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command')
if echo "$COMMAND" | grep -q "drop table"; then
  echo "Blocked: dropping tables is not allowed" >&2
  exit 2
fi
exit 0
```

### Pattern 3: Dependency Scanning Gate

A PreToolUse hook on `Bash` that intercepts `npm install` or `pip install` commands and runs security scanning before allowing the installation [22]:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {"type": "command", "command": "./scripts/dependency-gate.sh"}
        ]
      }
    ]
  }
}
```

The dependency gate script can parse `tool_input.command` for install commands and run `npm audit` or `pip-audit` before allowing execution [22].

### Pattern 4: Secret Scanning

The `mintmcp/agent-security` project provides a "standalone, local-first scanner" running as "editor/agent hooks entirely on your machine. Pre hooks block when secrets are detected" [from WebSearch results].

### Pattern 5: Tool Input Modification

Starting in v2.0.10, PreToolUse hooks can modify tool inputs before execution rather than blocking. This enables "transparent sandboxing, automatic security enforcement (dry-run flags, secret redaction)" [from WebSearch results on hooks-guide].

## Subagent Coverage

A critical property: "If Claude spawns a subagent via the Agent tool, your PreToolUse and PostToolUse hooks execute for every tool the subagent uses" [1]. This means security gates cannot be bypassed by delegating work to a subagent.

## Performance Considerations

"Hooks run synchronously. A hook that takes 5 seconds adds 5 seconds to every matched tool use. Keep hooks under 2 seconds, ideally under 500 milliseconds" [from WebSearch results].

## Limitations

- PreToolUse hooks cannot prevent a tool call after the fact; they only gate before execution [1]
- Exit codes other than 0 and 2 result in the action proceeding (fail-open for hook errors) [1]
- `PermissionRequest` hooks do not fire in non-interactive mode (`-p`); use `PreToolUse` hooks for automated permission decisions [1]
- Hooks themselves can be targets for modification attacks [16] unless protected via managed settings

## Citations

Key sources: [1] Official hooks guide (WebFetch), [15] Hook exit code tutorial, [16] CVE research, [22] Dependency management guide. All citations reference `../citations.md`.
