# Recent Security Updates (2024-2025)

Dimension: Security-relevant changes to Claude Code from the changelog and announcements.

See `../citations.md` for full source details.

---

## Major Security Features Added

| Feature | Source |
|---------|--------|
| Sandbox mode for BashTool on Linux and Mac | [11] |
| Auto mode with two-layer defense (prompt-injection probe + transcript classifier) | [5] |
| `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` to strip credentials from subprocess environments | [10] [11] |
| `sandbox.failIfUnavailable` setting to exit with error when sandbox cannot start | [11] |
| `allowRead` sandbox setting to re-allow read access within `denyRead` regions | [11] |
| `ConfigChange` hook event for enterprise security auditing | [11] |
| `CwdChanged` and `FileChanged` hook events for reactive environment management | [11] |
| `allowUnsandboxedCommands` setting to disable sandbox escape hatch at policy level | [11] |
| `disallowedTools` field for custom agent definitions | [11] |
| Checkpointing for automatic code state saves before each change | [19] |
| Claude Code Security vulnerability scanning (research preview) | [9] |
| Remote MCP with native OAuth support | [22] |

## Security Fixes

| Fix | Source |
|-----|--------|
| PreToolUse hooks returning "allow" bypassing deny permission rules (including enterprise managed settings) | [11] |
| Sandbox permission issues: file write operations incorrectly allowed without prompting | [11] |
| Symlink bypass: writing through symlinked parent directory could escape working directory in acceptEdits mode | [11] |
| `.git`, `.claude`, and protected directories writable without prompt in bypassPermissions mode | [11] |
| `deny: ["mcp__servername"]` not removing MCP tools from model context | [11] |
| CVE-2025-66032: 8 ways to bypass deny list, patched in v1.0.93 | [11] |
| "Always Allow" on compound bash commands saving single rule for full string instead of per-subcommand | [11] |
| Silent sandbox disable when dependencies missing -- now shows warning | [11] |
| `sandbox.filesystem.allowWrite` not working with absolute paths | [11] |
| Sandbox prompting for non-allowed domains when `allowManagedDomainsOnly` enabled -- now blocks automatically | [11] |
| Interactive tools silently auto-allowed when in skill's allowed-tools | [11] |
| Git remote add/push exfiltration vector blocked (2026-03-05c) | [11] |
| Various hooks bugs (transcript_path wrong directory, PostToolUse block reason displaying twice, async hooks stdin issues) | [11] |

## Security Research and Publications

| Publication | Date | Source |
|-------------|------|--------|
| "Making Claude Code more secure and autonomous" (sandboxing blog) | Oct 2025 | [6] |
| "Claude Code auto mode: a safer way to skip permissions" | 2025 | [5] |
| "Our framework for developing safe and trustworthy agents" | 2025 | [8] |
| "Mitigating the risk of prompt injections in browser use" | 2025 | [23] |
| Claude Code Security vulnerability scanning announcement | 2025 | [9] |

## Open Security Issues (as of research date)

| Issue | GitHub Issue |
|-------|-------------|
| Hooks cannot be protected from modification (Edit/Write bypass permissions.deny) | #11226 [15] |
| Agent can modify own permissions file within sandbox | #11815 [16] |
| CLAUDE.md and .claude/rules/ advisory-only with no enforcement | #34132 [14] |
| Sandbox escape hatch goes through normal permissions flow | #20259 |
| `allowUnsandboxedCommands` defaults to `true` | [11] |
| `dangerouslyDisableSandbox` bypasses permission prompts for auto-approved tools | #14268 |

## Gaps and Limitations

- Security updates are tracked in CHANGELOG.md but lack severity ratings or CVE details beyond CVE-2025-66032
- No published security advisory feed (RSS/Atom) for Claude Code security issues
- Open security issues (#11226, #11815, #34132) represent fundamental architectural concerns (self-modification, advisory-only rules) that have not been resolved
- The pace of security fixes suggests ongoing discovery of bypass techniques
