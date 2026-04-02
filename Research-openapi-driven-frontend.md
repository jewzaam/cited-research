# Research Brief: OpenAPI-Driven Type-Safe Frontend Development

## Context

The frontend project (the frontend project) uses a three-layer OpenAPI
pipeline for type-safe API integration:

1. **openapi-typescript** generates TypeScript types from the backend's
   OpenAPI YAML specs
2. **openapi-fetch** provides a type-safe HTTP client using those types
3. **openapi-react-query** bridges the client with TanStack Query hooks

The generated types live in a separate `application-contracts` package within the
monorepo. The backend (FastAPI) auto-generates OpenAPI specs from SQLModel
definitions, creating an end-to-end type chain from database to UI.

## Research Questions

1. What is the openapi-typescript ecosystem — how do openapi-typescript,
   openapi-fetch, and openapi-react-query work together, and what are the
   alternatives (orval, swagger-typescript-api, hey-api)?
2. What are the best practices for managing generated types in a monorepo —
   generation triggers, version pinning, drift detection between spec and
   generated code?
3. How do teams handle OpenAPI spec evolution — breaking changes,
   versioning strategies, backward compatibility in generated clients?
4. What patterns exist for error type safety — mapping backend error
   responses (including RFC 9457 problem details) to typed frontend error
   handling?
5. How does the "contract-first" approach compare to "code-first" for
   frontend-backend API integration in practice?
6. What are the limitations of OpenAPI-generated clients — edge cases in
   spec translation, unsupported OpenAPI features, runtime vs compile-time
   type safety?

## Relationship to Existing Research

- **Research-rfc9457-problem-details.md** — the frontend error parsing
  handles RFC 9457 responses. Findings from that research inform how
  error types flow through the generated client.

## Why This Matters

The OpenAPI pipeline is how frontend achieves end-to-end type safety. Every
API call goes through generated types. Understanding this pipeline is
necessary for adding new API endpoints, debugging type mismatches, or
evaluating whether the current toolchain is the right choice.
