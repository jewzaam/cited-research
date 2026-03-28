# Prompt Injection and Exfiltration Defenses

Dimension: How Claude Code handles prompt injection via untrusted content and prevents data exfiltration.

See `../citations.md` for full source details.

---

## Model-Level Defenses

Anthropic uses reinforcement learning to build prompt injection robustness directly into Claude's capabilities. During model training, they expose Claude to prompt injections embedded in simulated web content and reward it when it correctly identifies and refuses to comply with malicious instructions. [23]

## Runtime Defenses

### Auto Mode Prompt-Injection Probe

At the input layer, a server-side prompt-injection probe scans tool outputs (file reads, web fetches, shell output, external tool responses) before they enter the agent's context. When content looks like an attempt to hijack behavior, the probe adds a warning to the agent's context before the result is passed along. [5]

### Isolated Context Windows

Web fetch uses a separate context window to avoid injecting potentially malicious prompts into the main conversation. [1]

The web fetch tool can only fetch URLs that have previously appeared in the conversation context -- it cannot fetch arbitrary URLs that Claude generates. [from search results]

### Trust Verification

First-time codebase runs and new MCP servers require trust verification. [1]

### Command Injection Detection

Suspicious bash commands require manual approval even if previously allowlisted. [1]

### Fail-Closed Matching

Unmatched commands default to requiring manual approval. [1]

## Infrastructure-Level Defenses

### Sandbox Isolation

Sandboxing ensures that even a successful prompt injection is fully isolated and cannot impact overall user security. A compromised Claude Code cannot steal SSH keys or phone home to an attacker's server. [6]

### Network Isolation

Prevents a prompt-injected Claude from leaking sensitive information or downloading malware by restricting outbound connections to approved servers via a Unix domain socket proxy. [6]

### Filesystem Isolation

Prevents a prompt-injected Claude from modifying sensitive system files by restricting file access to specific directories. [6]

## Content Sanitization

For GitHub Actions, the action sanitizes untrusted content by stripping [10]:
- HTML comments
- Invisible characters
- Markdown image alt text
- Hidden HTML attributes
- HTML entities

Note: "new bypass techniques may emerge" per Anthropic's own documentation. [10]

## Known Attack Vectors

1. **Poisoned repository files:** Malicious instructions embedded in READMEs, code comments, and dependency metadata. Research tested 314 attack payloads against coding agents with an 84% success rate (against agents without sandbox isolation). [from search results]

2. **WebFetch as second-stage injection:** A prompt injection in a project file can direct Claude to fetch a URL containing further injection payloads. The sandbox network proxy prompts for domain approval, but the domain may appear legitimate. [from search results]

3. **CLAUDE.md poisoning:** A malicious npm package's postinstall script could write to paths including ~/.claude/CLAUDE.md and skill files. [from search results]

4. **Git remote exfiltration:** Prior to 2026-03-05c, prompt injection could add an attacker-controlled git remote and push commit history. Now blocked. [11]

5. **Settings self-modification:** If Claude can modify its own config, a prompt injection can disable all other protections. [from search results]

## What Does NOT Constitute a Defense

- CLAUDE.md instructions are advisory-only with no enforcement mechanism [14]
- Hooks are "not a security boundary" per Trail of Bits -- described as "structured prompt injection at opportune times" [21]
- Permission prompts are approved 93% of the time, suggesting limited human oversight value [5]

## Gaps and Limitations

- No published false-positive/false-negative rates for the prompt-injection probe
- Content sanitization acknowledges "new bypass techniques may emerge" [10]
- Model-level RL training provides probabilistic, not deterministic, resistance
- The 84% attack success rate against unsandboxed agents is a sobering baseline [from search results]
- Hook scripts can be modified by Claude via Edit/Write tools [15]
- Agent can modify its own permissions file within sandbox [16]
