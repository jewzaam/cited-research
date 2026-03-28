# Trust and Safety Documentation

Dimension: Anthropic's published trust, safety, and security documentation for Claude Code.

See `../citations.md` for full source details.

---

## Official Documentation Sources

### 1. Claude Code Security Docs

URL: https://docs.anthropic.com/en/docs/claude-code/security

Covers [1]:
- Core security model (read-only by default)
- Permission prompts for modifications
- MCP server trust verification
- Command injection detection
- Fail-closed matching
- Isolated context windows for web fetch
- Network request approval
- Secure credential storage
- Cloud execution security

### 2. Safe and Trustworthy Agents Framework

URL: https://www.anthropic.com/news/our-framework-for-developing-safe-and-trustworthy-agents

Key principles [8]:
- Agents should be safe, reliable, and trustworthy
- Balance agent autonomy with human oversight
- Read-only permissions by default
- Humans can stop Claude whenever they want and redirect its approach
- Must ask for human approval before taking actions that modify code or systems
- Users can grant persistent permissions for routine tasks
- Privacy: agents might inappropriately carry sensitive information across contexts
- MCP includes controls for tool access
- Threat Intelligence team conducts ongoing monitoring

### 3. Anthropic Trust Center

URL: https://trust.anthropic.com

Centralized trust and compliance portal for Anthropic products. [13]

### 4. Claude Code Sandboxing Blog

URL: https://www.anthropic.com/engineering/claude-code-sandboxing

Documents the two-boundary sandbox architecture (filesystem + network), OS-level primitives, past security incidents, and the 84% permission prompt reduction. [6]

### 5. Auto Mode Blog

URL: https://www.anthropic.com/engineering/claude-code-auto-mode

Documents the two-layer defense system (prompt-injection probe + transcript classifier), the 93% approval rate finding, and auto mode as a middle ground. [5]

### 6. Claude Code Security Announcement

URL: https://www.anthropic.com/news/claude-code-security

Documents the Claude Code Security vulnerability scanning feature with multi-stage verification. [9]

### 7. claude-code-action Security Documentation

URL: https://github.com/anthropics/claude-code-action/blob/main/docs/security.md

Documents subprocess environment scrubbing, hidden markdown sanitization, output security, and commit signing. [10]

### 8. Prompt Injection Research

URL: https://www.anthropic.com/research/prompt-injection-defenses

Documents reinforcement learning approach to building prompt injection robustness into the model during training. [23]

## Core Security Principles (Synthesized)

Based on all official sources, Claude Code's security model rests on these principles:

1. **Default deny:** Read-only by default, fail-closed on unmatched commands [1]
2. **Human oversight:** Permission prompts for modifications, human can stop/redirect anytime [8]
3. **Layered defense:** Permissions + sandbox + hooks + model-level training [1] [6] [23]
4. **Credential isolation:** Credentials kept outside sandbox in cloud environments [6]
5. **Ongoing monitoring:** Threat Intelligence team for emerging threats [8]
6. **Configurable scope:** Enterprise managed settings override project/user settings [4]

## What Anthropic Does NOT Promise

- Does not manage or audit MCP servers [1]
- Does not guarantee hooks are a security boundary [21]
- Does not auto-detect credential files for protection
- Does not promise sandbox availability on all platforms
- Acknowledges that "the rapid implementation of agents means it's crucial that developers build agents that are safe" -- framing this as a shared responsibility [8]

## Gaps and Limitations

- No centralized security architecture document -- security information is spread across docs, blog posts, GitHub repos, and announcements
- Trust Center content was not fetched in detail during this session [13]
- No published threat model document specific to Claude Code
- No published penetration testing results or security audit reports
- Security guidance relies heavily on user configuration rather than secure defaults
