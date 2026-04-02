# Research Brief: OPA (Open Policy Agent) for API Authorization

## Context

The application (the backend project) is evaluating OPA for API authorization,
with two approaches under consideration: sidecar deployment vs embedded
(in-process) evaluation. The project already has JWT authentication in
progress and needs a policy engine for fine-grained access control across
its domain modules (workflows, invocations, tools, files, approvals).

## Research Questions

1. What is OPA's architecture — Rego policy language, data model, partial
   evaluation, bundle management — and what is the current state of the
   project?
2. Sidecar vs embedded vs library (opa-python, regorus): what are the
   latency, operational, and failure-mode trade-offs for each deployment
   model?
3. How does OPA integrate with FastAPI — middleware patterns, per-route
   authorization, request/response context injection?
4. What are Rego language best practices for API authorization policies
   (RBAC, ABAC, resource-scoped permissions)?
5. How do teams manage OPA policy lifecycle — testing, versioning, bundle
   distribution, policy-as-code CI/CD?
6. What are the alternatives to OPA (Casbin, Cedar, Cerbos, OSO/Polar)
   and how do they compare for Python/FastAPI authorization?
7. What are the performance characteristics — policy evaluation latency,
   memory footprint, cold start — under production loads?

## Relationship to Existing Research

No overlap with existing research topics.

## Why This Matters

Authorization is a foundational concern for any multi-user system. OPA is
the leading open-source policy engine but has significant complexity.
Understanding deployment models, Rego patterns, and alternatives informs
the authorization architecture decision application is actively making.
