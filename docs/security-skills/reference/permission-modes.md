# Permission Modes

Dimension: How Claude Code's permission system controls what actions are allowed, prompted, or blocked.

See `../citations.md` for full source details.

---

## Default Behavior

Claude Code runs on a permission-based model: by default, it is read-only. It asks for permission before making modifications or running any commands. [1] [8]

Exceptions: Safe commands like `echo` or `cat` are auto-allowed. [1]

## Permission Modes

| Mode | Behavior | Use Case |
|------|----------|----------|
| Manual (default) | Users must approve actions individually | Standard interactive development |
| `acceptEdits` | Approves file operations (Edit, Write, MultiEdit). Other actions fall through to manual prompt. | Faster editing with command oversight |
| `bypassPermissions` | Approves everything that reaches the permission step | Controlled/sandboxed environments only |
| Auto mode | Delegates approvals to model-based classifiers | Middle ground between manual and bypass |

Sources: [5], [7]

## Auto Mode (Detail)

Auto mode was introduced to address "approval fatigue" -- Anthropic found that Claude Code users approve 93% of permission prompts. [5]

Auto mode uses two layers of defense [5]:

1. **Input layer:** A server-side prompt-injection probe scans tool outputs (file reads, web fetches, shell output, external tool responses) before they enter the agent's context. When content looks like a hijack attempt, the probe adds a warning to the agent's context.

2. **Output layer:** A transcript classifier evaluates each action against decision criteria before it executes, acting as a substitute for a human approver. The classifier runs in two stages: a fast single-token filter, followed by chain-of-thought reasoning only if the first filter flags the transcript.

## The `--dangerously-skip-permissions` Flag

This flag bypasses all permission checks. Anthropic's Best Practices documentation warns it should only be used "in a sandbox without internet access." [17]

**Known contradiction:** The Devcontainer documentation encourages using this flag while noting the container has internet access via whitelisted domains and permits outbound DNS and SSH connections. [17]

**Restrictions:**
- Cannot be used with root/sudo privileges for security reasons [from GitHub issue #9184]
- Does not bypass the workspace trust prompt ("Quick safety check: Is this a project you created or one you trust?") [from GitHub issue #28506]

## `dontAsk` Mode (SDK)

For locked-down agents, pairing `allowedTools` with `permissionMode: "dontAsk"` means listed tools are approved and anything else is denied outright instead of prompting. [7]

## Approval Flow

The evaluation flow for each tool call [7]:

1. Check deny rules (from all settings scopes)
2. Check allow rules (from all settings scopes)
3. Check hooks (PreToolUse permissionDecision)
4. Apply permission mode (manual prompt, acceptEdits auto-approve, or bypass)
5. If nothing matches: fail-closed (manual approval required) [1]

## Known Security Issues with Permission Modes

- `.git`, `.claude`, and other protected directories were writable without a prompt in `bypassPermissions` mode -- fixed [11]
- Symlink bypass: writing new files through a symlinked parent directory could escape the working directory in `acceptEdits` mode -- fixed [11]
- Interactive tools (e.g., AskUserQuestion) were silently auto-allowed when listed in a skill's allowed-tools, bypassing the permission prompt -- fixed [11]

## Gaps and Limitations

- The 93% approval rate suggests most users do not carefully review prompts, creating a baseline security risk regardless of mode [5]
- Auto mode's transcript classifier is a probabilistic defense, not a deterministic one
- No published false-positive/false-negative rates for auto mode's classifiers
- `bypassPermissions` mode has had multiple security regressions (protected directories writable, symlink escapes) suggesting it should be used with extreme caution [11]
