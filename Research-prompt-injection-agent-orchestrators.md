# Research Brief: Prompt Injection Defenses in Agent Orchestrators

## Context

The application (the backend project) runs an agent orchestrator that processes
user prompts, routes them to specialist agents, and executes tools (including
shell scripts, API calls, and AAP job templates) on behalf of users. This
creates a direct prompt injection attack surface: malicious input could
hijack agent behavior, exfiltrate data via tool calls, or escalate privileges
through the approval system.

## Research Questions

1. What prompt injection attack vectors are specific to multi-agent
   orchestrators (vs. simple chatbots) — inter-agent injection, tool-call
   manipulation, approval bypass?
2. What defenses have been deployed in production agent orchestrators —
   input sanitization, output filtering, privilege separation between agents?
3. How do teams implement least-privilege for tool access in agent systems —
   per-agent tool scoping, capability-based security, approval gates?
4. What is the current state of prompt injection detection — classifiers,
   canary tokens, semantic analysis — and their false positive rates?
5. How do agent frameworks (LangChain, LangGraph, CrewAI) handle security
   boundaries between agents and tools?
6. What are the implications of the "confused deputy" problem in agent
   orchestrators that execute actions with elevated privileges?

## Relationship to Existing Research

- **prompt-injection-defenses** (`research/prompt-injection-defenses/`) —
  covers general prompt injection defenses for LLM agents fetching external
  content. This topic focuses specifically on the orchestrator attack surface
  where agents execute tools and actions. Consider updating the existing
  research with orchestrator-specific findings.

## Why This Matters

application executes real actions (shell scripts, API calls, AAP jobs) based on
LLM-processed input. A successful prompt injection could have operational
impact beyond the LLM itself. Understanding orchestrator-specific attack
vectors and defenses is critical for the security posture of the system.
