# Policy-as-Code Applied to AI Coding Assistants

## Dimension

How policy-as-code frameworks (OPA, Rego, etc.) can be applied to AI coding assistant security enforcement, and the current state of integration.

## Policy-as-Code Fundamentals

Open Policy Agent (OPA) "generates policy decisions by evaluating query input against policies and data" and is "domain-agnostic" -- "you can describe almost any kind of invariant in your policies" [12].

Policy-as-code "solves governance challenges by encoding organizational rules -- security requirements, compliance standards, resource limits -- into machine-readable, version-controlled code that evaluates automatically" [from WebSearch on PaC tools].

Key property: "Unlike traditional compliance tools that run periodic checks, Policy-as-Code systems evaluate decisions before execution -- blocking violations in real time" [11].

## Current State: AI Agent Governance

NexaStack describes applying PaC to AI agent governance: "Policy-as-Code represents a paradigm shift in AI governance, transforming rigid, manual oversight into a dynamic and scalable framework that keeps pace with autonomous systems. By codifying policies into executable rules, organisations can enforce compliance in real time" [11].

Integration points for AI agent governance include [11]:
- Kubernetes (OPA Gatekeeper, Kyverno)
- Cloud providers (IAM, Lambda, API Gateway)
- Service meshes (Istio, Linkerd)
- CI/CD pipelines

## The Gap: No Direct OPA Integration with AI Coding Assistants

As of March 2026, no AI coding assistant (Claude Code, Copilot, Cursor, Windsurf) has native OPA/Rego integration. The policy enforcement mechanisms are:

| Tool | Enforcement Mechanism | Policy Language |
|---|---|---|
| Claude Code | Hooks (shell scripts) + managed-settings.json | Shell scripts, JSON config |
| GitHub Copilot | Hooks (shell scripts in `.github/hooks/`) | Shell scripts, JSON config |
| Cursor | Hooks (shell scripts) | Shell scripts |
| Windsurf | Enterprise RBAC | Administrative controls |
| OPA/Rego | Policy Decision Points | Rego (declarative) |

However, the hook systems in Claude Code, Copilot, and Cursor can call OPA as an external service. A PreToolUse hook could query an OPA server to evaluate whether a tool call should be permitted, effectively bridging the gap:

```bash
#!/bin/bash
# PreToolUse hook that queries OPA
INPUT=$(cat)
DECISION=$(echo "$INPUT" | curl -s -X POST http://localhost:8181/v1/data/coding_agent/allow -d @-)
if [ "$(echo "$DECISION" | jq -r '.result')" != "true" ]; then
  echo "Policy violation: action denied by OPA" >&2
  exit 2
fi
exit 0
```

This is architecturally possible but not documented or productized by any vendor.

## Security Invariants as Policy

The concept of "security invariants" maps directly to policy-as-code:

"Invariants are conditions that must always hold true, regardless of input, prompt variation, or model drift -- acting as the 'laws of physics' for the agent" [13].

"A state transition (State A -> State B) must be treated as an atomic operation. If any invariant fails on the resulting state, the entire transition must be rejected, keeping State A unchanged -- directly analogous to database transactions" [13].

This framing aligns with how PreToolUse hooks work: the tool call is a state transition, the hook evaluates invariants, and exit code 2 rejects the transition.

## Policy-as-Code for Hook Configuration

An underexplored approach: using policy-as-code to manage the hook configurations themselves. Rather than hand-writing hook scripts, organizations could:

1. Define security policies in Rego
2. Generate hook configurations from policies
3. Deploy via managed-settings.json
4. Audit compliance programmatically

The GitHub issue proposing an "immutable session manifest" [14] moves in this direction: defining a declarative specification of allowed capabilities rather than enumerating denials.

## The Denylist vs Allowlist Problem

The allowlist-only proposal from GitHub Issue #37471 frames the policy architecture problem precisely [14]:

- "Denylists answer: 'What should we block?' -- an unbounded question"
- "Allowlists answer: 'What should we permit?' -- a bounded question"

This mirrors how container security works: "A Docker container starts with zero capabilities and is granted only what it needs via a manifest. The manifest is immutable at runtime, declarative, and auditable" [14].

OPA's natural model is allowlist-based (policy defines what is permitted; everything else is denied by default), which would be a better fit for AI agent governance than the current denylist-oriented systems.

## Complementary Perspective

"Without runtime enforcement, your 'governance' is just a hope that developers remember to follow rules. With policy-as-code, your governance becomes executable, testable, and provable" [28].

## Gaps and Limitations

1. **No vendor has shipped OPA integration** for AI coding assistants as of March 2026
2. **Hook-based enforcement is ad hoc** -- each hook script is custom code, not declarative policy
3. **No policy testing framework** exists specifically for AI coding assistant hook configurations
4. **Cross-tool policy portability** is nonexistent -- Claude Code hooks, Copilot hooks, and Cursor hooks all use different configuration formats

## Citations

Key sources: [11] NexaStack PaC governance, [12] OPA official docs, [13] SakuraSky formal verification, [14] GitHub Issue #37471 manifest proposal, [28] SakuraSky PaC enforcement. All citations reference `../citations.md`.
