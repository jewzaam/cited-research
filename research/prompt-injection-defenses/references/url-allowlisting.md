# Domain and URL Allowlisting

Dimension covering approaches to constraining which sources an agent can fetch from, and how production systems manage trust boundaries for external content. Sources referenced via `[N]` — see [citations.md](../citations.md) for full entries.

## Overview

URL allowlisting operates at a different layer than other prompt injection defenses. Rather than detecting or surviving injection payloads, it prevents the agent from fetching untrusted content in the first place. The consensus across sources is **deny-by-default** — block all outbound requests except to explicitly allowlisted domains [16] [17] [18] [23].

## Deny-by-Default Architecture

LoginRadius [16] describes a zero-trust outbound model for AI agents:

- Each agent requires distinct registration with metadata specifying approved integrations
- "If a request falls outside that defined boundary, it is blocked automatically" [16]
- Enforcement must be at the **network/proxy layer**, not via system prompt instructions — the LLM should never directly decide whether to fetch a URL [16] [23]

### Multi-Layer Enforcement

| Layer | Controls | Purpose |
|-------|----------|---------|
| Infrastructure | Egress firewalls, DNS filtering, service mesh controls | Prevent direct network bypass [16] |
| Gateway | API gateways with identity validation, scope evaluation | Real-time allowlist comparison [16] |
| Authentication | Short-lived, scoped tokens aligned with destination | Prevent privilege amplification [16] |

### Identity-Bound Logging

Every outbound request should be logged with [16]:
- Agent identity metadata
- Tenant context
- Destination domain
- Delegation status
- Authorization outcome

"Behavioral baselining can identify deviations in outbound traffic patterns" [16].

## Production Implementations

### OpenAI Codex

OpenAI Codex implements a tiered internet access model [17]:

| Setting | Behavior |
|---------|----------|
| **Off** (default) | Complete network blockade during agent execution |
| **On** | Permits connectivity with optional restrictions |

Three allowlist strategies when access is on:
1. **None:** Empty list, manual domain specification required
2. **Common dependencies:** Preset covering ~60 domains (package managers, registries, VCS platforms)
3. **All (unrestricted):** No filtering [17]

**HTTP method restriction:** Non-allowlisted access restricted to read-only methods — `GET`, `HEAD`, `OPTIONS` only. `POST`, `PUT`, `PATCH`, `DELETE` are blocked [17].

OpenAI's documentation explicitly warns about prompt injection via fetched content, providing a concrete example where hidden instructions in GitHub issue descriptions could trick agents into leaking commit data [17].

### GitHub Copilot MCP Allowlist

GitHub implements enterprise-level MCP server allowlisting through a registry-based approach. However, current enforcement is based on server name/ID matching, which can be bypassed by editing configuration files [31].

### Goose (Block)

Block's Goose AI agent implements extension allowlisting via URL-based allowlist fetching with environment variable configuration.

## MCP Security Considerations

The Model Context Protocol documentation [18] addresses several security patterns relevant to agents fetching external content:

### SSRF Prevention

MCP clients must implement mitigations against Server-Side Request Forgery [18]:

- **Block private IP ranges:** 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16, 169.254.0.0/16 (cloud metadata), localhost
- **Validate redirect targets:** Apply same restrictions to redirect destinations; don't blindly follow
- **Use egress proxies:** Tools like Stripe's Smokescreen prevent SSRF by design
- **Pin DNS resolution:** Prevent TOCTOU attacks where domains resolve to safe IPs during validation but internal IPs during fetch

### Scope Minimization

MCP recommends progressive, least-privilege scope models [18]:
- Minimal initial scope (e.g., `mcp:tools-basic`) for low-risk discovery
- Incremental elevation via targeted challenges when privileged operations are attempted
- Server should accept reduced scope tokens; auth server MAY issue subsets

### Local MCP Server Risks

Local MCP servers (downloaded and executed on user machines) introduce code execution risks [18]:
- Malicious startup commands embedded in configuration
- Sandbox escapes from inadequately restricted servers
- MCP clients MUST display exact commands and require explicit approval before execution

## Tool Composition and Trust Boundaries

When one tool's output becomes another tool's input (e.g., search results → fetch_url), each tool may be safe in isolation but the chain creates emergent attack surface. This was identified in multiple sources as a key structural vulnerability [1] [30].

The ambient authority problem is structural: traditional OS models grant coarse network access (open sockets = any host), but agents need fine-grained, capability-based access [16].

## Delegation-Aware Governance

Delegation tokens must encode inherited permissions from the original principal [16]. If a user lacks data export authority, agents acting on their behalf cannot transmit that data — preventing privilege amplification through delegation chains.

## Gaps and Limitations

- **Allowlist granularity trade-offs are unexplored.** Domain-level vs. path-level vs. endpoint-level allowlisting — no published evaluation of the practical minimum for agentic use cases.
- **Dynamic content sources.** Agents that need to access user-specified URLs (e.g., "summarize this article") cannot operate under static allowlists. No production system has published a solution for dynamic URL trust evaluation.
- **MCP lacks protocol-level security.** Security depends entirely on implementation and operational controls, not the protocol itself [18].
- **Allowlists don't address content within allowed domains.** A page on an allowlisted domain can still contain prompt injection payloads. Allowlisting reduces attack surface but does not eliminate it.
