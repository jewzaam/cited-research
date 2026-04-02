# Research Brief: MSW and Mock-Driven Frontend Development

## Context

The frontend project (the frontend project) uses Mock Service Worker (MSW)
with @mswjs/http-middleware to run a complete mock API server for
development. The mock API lives in a separate `mock-api` package in
the monorepo and serves realistic data (including example workflows from
the actual backend repo). This allows full UI development without running
the Python/FastAPI backend, PostgreSQL, Temporal, or Redis.

## Research Questions

1. What is MSW's architecture — service worker interception vs Node.js
   server mode, handler patterns, request matching — and what changed in
   MSW 2.0?
2. What are the best practices for maintaining mock data that stays in sync
   with the real API — schema validation, contract testing, OpenAPI spec
   enforcement?
3. How do teams use MSW across the development lifecycle — local
   development, component testing (Vitest), integration testing, E2E
   testing (Playwright)?
4. What patterns exist for mock data management at scale — factories,
   fixtures, scenario-based mocking, stateful mock servers?
5. How does MSW compare to alternatives for API mocking — Mirage JS,
   json-server, Prism (OpenAPI mock server), WireMock?
6. What are the trade-offs of mock-driven development — development speed
   vs API drift risk, testing confidence vs maintenance burden?

## Relationship to Existing Research

No overlap with existing research topics.

## Why This Matters

The mock API is what enables frontend developers to work independently of
the backend team. Understanding MSW patterns and mock data management
prevents API drift (where mocks diverge from the real API) and informs
how to extend the mock API as new features are added.
