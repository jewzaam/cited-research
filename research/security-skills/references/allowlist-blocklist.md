# Allowlist/Blocklist System

Dimension: How Claude Code's permission rules are structured, scoped, and merged across configuration levels.

See `../citations.md` for full source details.

---

## Settings Hierarchy

Claude Code uses a scope system with the following precedence (highest to lowest) [4]:

| Scope | Location | Shared? |
|-------|----------|---------|
| Managed (enterprise) | Set by organization admins | Organization-wide |
| Project shared | `.claude/settings.json` | Checked into source control |
| Project local | `.claude/settings.local.json` | Gitignored, per-developer |
| User | `~/.claude/settings.json` | Per-user, all projects |

If a permission is allowed in user settings but denied in project settings, the project setting takes precedence and the permission is blocked. [4]

The same precedence applies whether running from CLI, VS Code extension, or JetBrains IDE. [4]

## Array Settings Merge Behavior

When the same array-valued setting (such as `sandbox.filesystem.allowWrite` or `permissions.allow`) appears in multiple scopes, the arrays are concatenated and deduplicated, not replaced. [4]

Example: If managed settings set `allowWrite` to `["/opt/company-tools"]` and a user adds `["~/.kube"]`, both paths are included in the final configuration. [4]

## Permission Rule Format

Rules are declared in `permissions.allow` and `permissions.deny` arrays in settings.json [4]:

```
"permissions": {
  "allow": [
    "Edit",
    "Bash(git commit:*)",
    "mcp__puppeteer__puppeteer_navigate"
  ],
  "deny": [
    "Read(./.env)",
    "Read(./.env.*)",
    "Read(./secrets/**)"
  ]
}
```

## Ways to Configure Permissions

1. Select "Always allow" when prompted during a session [4]
2. Use the `/permissions` command to add or remove tools from the allowlist [4]
3. Manually edit `.claude/settings.json` or `~/.claude/settings.json` [4]
4. Use the `--allowedTools` CLI flag for session-specific permissions [4]

## SDK Permission Destinations

The `PermissionUpdateDestination` type supports [7]:

| Destination | Scope |
|-------------|-------|
| `"userSettings"` | Global user settings |
| `"projectSettings"` | Per-directory project settings |
| `"localSettings"` | Gitignored local settings |
| `"session"` | Current session only |
| `"cliArg"` | CLI argument |

## SDK Permission Controls

- `allowed_tools` and `disallowed_tools` add entries to the allow and deny rule lists [7]
- They control whether a tool call is approved, not whether the tool is available to Claude [7]
- `disallowedTools` field added to custom agent definitions for explicit tool blocking [11]

## Deny Rule Precedence

Deny rules from any settings scope, including managed settings, always take precedence over hook approvals. [2]

If a deny rule matches a tool call, the call is blocked even when a PreToolUse hook returns "allow". [2]

## Fail-Closed Matching

Unmatched commands default to requiring manual approval. [1]

## Known Security Issues

- `deny: ["mcp__servername"]` permission rules did not remove MCP server tools before sending to the model, allowing it to see and attempt blocked tools -- fixed [11]
- Security researchers found 8 ways to bypass Claude Code's deny list (CVE-2025-66032, patched in v1.0.93) [11]
- "Always Allow" on compound bash commands saved a single rule for the full string instead of per-subcommand, leading to dead rules -- fixed [11]

## Gaps and Limitations

- Deny list bypasses have been found multiple times (CVE-2025-66032), suggesting ongoing adversarial pressure on this surface
- CLAUDE.md and .claude/rules/ are advisory-only with no enforcement mechanism [14]
- Array merging means lower-priority scopes can add allow entries that may conflict with organizational intent (though deny rules still take precedence)
