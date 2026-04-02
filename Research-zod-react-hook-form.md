# Research Brief: Zod + React Hook Form for Schema-Driven Validation

## Context

The frontend project (the frontend project) uses Zod 4 for schema validation
and react-hook-form for form state management, connected via
@hookform/resolvers. The workflow builder has complex forms for each node
type (actions, conditions, loops, AI agents) with nested fields, dynamic
arrays, and conditional validation. Server-side errors (FastAPI 422
responses) are mapped back to form fields via a custom
useFormMutationErrorHandler hook.

## Research Questions

1. What is Zod 4 — what changed from Zod 3, what are the new APIs, and
   what are the migration considerations?
2. How does react-hook-form handle complex form patterns — nested objects,
   dynamic field arrays (useFieldArray), conditional fields, cross-field
   validation?
3. What are the patterns for mapping server validation errors back to
   form fields — especially FastAPI's 422 validation error format with
   loc arrays?
4. How do teams share validation schemas between frontend (Zod) and
   backend (Pydantic) — is there tooling for generating one from the other?
5. What are the performance characteristics of react-hook-form vs
   alternatives (Formik, Final Form, native forms) for complex,
   deeply-nested forms?
6. How do Zod schemas integrate with TypeScript — type inference,
   branded types, schema composition patterns?

## Relationship to Existing Research

No overlap with existing research topics.

## Why This Matters

Every user interaction that creates or modifies data goes through a form.
The Zod + react-hook-form combination is how frontend validates user input
and communicates errors. Understanding these patterns is necessary for
building new node type forms, debugging validation issues, or handling
the increasingly complex form structures in the workflow builder.
