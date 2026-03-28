# Sandbox/Container Execution

Dimension: Claude Code's isolation mechanisms, filesystem and network boundaries, and containerization.

See `../citations.md` for full source details.

---

## Architecture Overview

Claude Code's sandboxing architecture isolates code execution with filesystem and network controls, automatically allowing safe operations, blocking malicious ones, and asking permission only when needed. [6]

The sandbox is built on top of OS-level primitives [6]:
- **Linux:** bubblewrap
- **macOS:** seatbelt

These cover not just Claude Code's direct interactions but also any scripts, programs, or subprocesses spawned by commands. [6]

## Two Isolation Boundaries

### Filesystem Isolation

Ensures Claude can only access or modify specific directories. [6]

Configuration via settings [4]:
- `sandbox.filesystem.allowWrite` -- directories Claude can write to
- `sandbox.filesystem.denyRead` -- directories Claude cannot read
- `sandbox.filesystem.allowRead` -- re-allows read access within denyRead regions [11]

### Network Isolation

Works by only allowing internet access through a Unix domain socket connected to a proxy server running outside the sandbox. The proxy server enforces restrictions on the domains a process can connect to and handles user confirmation for newly requested domains. [6]

Configuration:
- `sandbox.network.allowManagedDomainsOnly` -- when enabled in managed settings, non-allowed domains are blocked automatically with no bypass [11]

## Why Both Boundaries Are Required

Without network isolation, a compromised agent could exfiltrate sensitive files like SSH keys. Without filesystem isolation, a compromised agent could easily escape the sandbox and gain network access. [6]

## Impact

In internal usage, Anthropic found that sandboxing safely reduces permission prompts by 84%. [6]

## Cloud Execution Security

When using Claude Code on the web, each cloud session runs in an isolated, Anthropic-managed VM with [1] [6]:
- Network access controls (limited by default, configurable)
- Credential protection through a secure proxy using scoped credentials
- Branch restrictions
- Audit logging
- Automatic cleanup after session completion

Credentials (such as git credentials or signing keys) are never inside the sandbox with Claude Code, so even if code running in the sandbox is compromised, the user is kept safe. [6]

## Sandbox Settings

| Setting | Purpose |
|---------|---------|
| `sandbox.enabled` | Enable/disable sandbox |
| `sandbox.failIfUnavailable` | Exit with error when sandbox enabled but cannot start [11] |
| `allowUnsandboxedCommands` | Controls the `dangerouslyDisableSandbox` escape hatch [11] |
| `sandbox.filesystem.allowWrite` | Directories writable by Claude |
| `sandbox.filesystem.denyRead` | Directories Claude cannot read |
| `sandbox.filesystem.allowRead` | Re-allow reads within denyRead regions |
| `sandbox.network.allowManagedDomainsOnly` | Restrict to managed domain list |

## Sandbox Mode for BashTool

A sandbox mode for the BashTool was released on Linux and Mac. [11]

## Known Security Issues

- Silent sandbox disable when `sandbox.enabled: true` was set but dependencies were missing -- now shows a visible startup warning [11]
- Agent can modify its own permissions file within sandbox environment [16]
- `sandbox.filesystem.allowWrite` did not work with absolute paths (previously required `//` prefix) -- fixed [11]
- Sandbox escape hatch: users can request to "retry outside sandbox," and this goes through the normal permissions flow that users click through repeatedly, so it may not receive adequate scrutiny [from GitHub issue #20259]
- `dangerouslyDisableSandbox` bypasses permission prompts when tool is auto-approved [from GitHub issue #14268]

## Gaps and Limitations

- Sandbox escape hatch (`allowUnsandboxedCommands`) defaults to `true`, meaning users must explicitly opt out [11]
- Agent self-modification of settings within sandbox has been reported [16]
- Sandbox depends on OS-level tooling (bubblewrap/seatbelt) which may not be available in all environments
- `sandbox.failIfUnavailable` must be explicitly set -- without it, sandbox failures may be silent
