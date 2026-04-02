# Research Brief: SQLModel as Unified Schema Layer

## Context

The application (the backend project) uses SQLModel as the single source of
truth for both database schemas and API models. Models inherit from composable
base classes (BaseResource, NamedResource, SoftDeletableResource,
UserOwnedResource, Resource) that provide standard fields (id, timestamps,
labels, soft delete, audit). Template expressions (`${...}`) bypass Pydantic
validation for dynamic workflow definitions. The project uses Alembic for
migrations with asyncpg as the PostgreSQL driver.

## Research Questions

1. What is SQLModel's architecture — how does it layer Pydantic v2 on top of
   SQLAlchemy, and what does "single model" actually mean at the ORM level?
2. What are the known limitations and pitfalls (relationship handling, async
   session compatibility, migration generation, validation edge cases)?
3. How does the "single model for DB + API" pattern compare to the traditional
   "separate Pydantic + SQLAlchemy" pattern in real projects — what trade-offs
   emerge at scale?
4. What is the state of SQLModel's maintenance and community (tiangolo
   maintains it alongside FastAPI — is it keeping pace with Pydantic v2 and
   SQLAlchemy 2.0)?
5. What patterns exist for model inheritance/composition (mixins, abstract
   bases) in SQLModel — does it support the kind of base resource hierarchy
   application uses?
6. How do teams handle the validation-bypass pattern (template expressions
   that need to skip type checking) in SQLModel/Pydantic?

## Relationship to Existing Research

No overlap with existing research topics.

## Why This Matters

Every data model in application flows through SQLModel. Understanding its
capabilities, limitations, and the trade-offs of the unified-model approach
is necessary for working on any domain's models, migrations, or API schemas.
