# Secrets and Credentials Protection

Dimension: How Claude Code protects against leaking secrets, API keys, credentials, and sensitive environment data.

See `../citations.md` for full source details.

---

## Built-In Protections

### Secure Credential Storage

Claude Code provides encrypted API keys and tokens storage. [1]

### Isolated Context Windows for Web Fetch

Web fetch uses a separate context window to avoid injecting potentially malicious prompts. [1]

For security, the web fetch tool can only fetch URLs that have previously appeared in the conversation context -- it cannot fetch arbitrary URLs that Claude generates. [from search results]

### Credential Isolation in Cloud Environments

Sensitive credentials (such as git credentials or signing keys) are never inside the sandbox with Claude Code, so even if code running in the sandbox is compromised, the user is kept safe. [6]

Each cloud session runs in an isolated, Anthropic-managed VM with credential protection through a secure proxy using scoped credentials. [6]

### Subprocess Environment Scrubbing

`CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` makes Claude Code (v2.1.79+) strip credentials from the environment of subprocesses it spawns. [10]

The parent Claude process keeps these variables for its own API calls -- only child subprocess environments are scrubbed. [10]

**What is scrubbed** [10]:
- Anthropic auth tokens
- Cloud provider credentials
- GitHub Actions OIDC and runtime tokens
- OTEL auth headers

This setting is automatically enabled for workflows that configure `allowed_non_write_users` in claude-code-action. [10]

### GitHub Actions Output Security

`show_full_output` is disabled by default for security reasons. When enabled, it outputs ALL Claude Code messages including full outputs from tool executions that may contain tokens or credentials. These logs are publicly visible in GitHub Actions for public repositories. [10]

## Configurable Protections

### Deny Access to Sensitive Files

Users can deny access to credential files via `permissions.deny` [4]:

```json
{
  "permissions": {
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)",
      "Read(./config/credentials.json)"
    ]
  }
}
```

### Network Isolation

Network isolation prevents a compromised agent from exfiltrating sensitive files by restricting outbound connections to approved servers only. [6]

### Hidden Markdown Sanitization

For GitHub Actions, the action sanitizes content by stripping HTML comments, invisible characters, markdown image alt text, hidden HTML attributes, and HTML entities to prevent hidden injection of credential-exfiltration instructions. [10]

## Prompt Injection as Exfiltration Vector

A malicious issue body could trick Claude into running a Bash command that reads credential environment variables via shell expansion and leaks them through an observable side channel. Subprocess environment scrubbing removes the read primitive entirely. [10]

Prior to 2026-03-05c, a prompt injection could `git remote add` an attacker-controlled remote and push the entire commit history (which might contain secrets). This is now blocked via deny rules covering all five variants. [11]

## Known Security Issues

- Without network isolation, a compromised agent could exfiltrate sensitive files like SSH keys [6]
- Prompt injection in project files can direct Claude to fetch URLs containing further injection payloads (WebFetch as second-stage injection vector) [from search results]
- Prior git remote add/push exfiltration vector was unblocked until March 2026 [11]

## Gaps and Limitations

- Subprocess environment scrubbing "reduces but does not eliminate" prompt injection risk [10]
- Users must manually configure deny rules for their specific credential files -- no auto-detection of .env or credential files
- Sandbox network isolation must be explicitly enabled
- The default configuration does not block reading of .env files
- Credential scrubbing only covers known token patterns -- novel credential formats may not be caught
