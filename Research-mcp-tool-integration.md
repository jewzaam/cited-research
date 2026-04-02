# Research Brief: Model Context Protocol (MCP) for Tool Integration

## Context

The application (the backend project) uses MCP servers as its primary tool
integration mechanism. The tool_manager module discovers, validates, and
executes tools from MCP servers via langchain-mcp-adapters. It has a plugin
architecture for tool providers (currently MCP only), a factory pattern for
provider instantiation with thread-safe registration, and per-tool rate
limiting with configurable strategies.

## Research Questions

1. What is the MCP specification — transports (stdio, SSE, streamable HTTP),
   tool schemas, resource types, prompts — and what version is current?
2. How does MCP compare to native function-calling / tool-use APIs offered
   by model providers (Anthropic, OpenAI)?
3. What MCP servers exist in the ecosystem, and what's the maturity curve
   (vendor-maintained vs community)?
4. What are production deployment patterns for MCP servers — lifecycle
   management, connection pooling, error handling, security boundaries?
5. How does langchain-mcp-adapters work, and what are its limitations
   compared to using the MCP SDK directly?
6. What patterns exist for rate limiting, access control, and auditing of
   MCP tool calls in multi-tenant or multi-agent systems?
7. What is the security model — how are MCP servers authenticated, what
   data can they access, and what are the known attack surfaces?

## Relationship to Existing Research

- **agent-sdk-vs-skills** — mentions MCP in context of Claude Agent SDK
- **personal-assistant** — evaluates MCP servers for specific integrations
- **todoist** — evaluates Todoist's MCP server
- **security-skills** — touches MCP permissions
- None of these deep-dive into MCP itself. This would be the canonical
  MCP reference.

## Why This Matters

MCP is how application extends its capabilities. Understanding the protocol, its
ecosystem, and production patterns is necessary for adding new tool providers,
debugging tool execution failures, or evaluating the plugin architecture.
