# MCP Server Permissions

Dimension: How Model Context Protocol (MCP) tool access is controlled and secured in Claude Code.

See `../citations.md` for full source details.

---

## MCP Server Trust Model

- Claude Code allows users to configure MCP servers [1]
- The list of allowed MCP servers is configured in source code, as part of Claude Code settings engineers check into source control [1]
- Anthropic encourages writing your own MCP servers or using MCP servers from trusted providers [1]
- Anthropic does not manage or audit any MCP servers [1]
- First-time codebase runs and new MCP servers require trust verification [1]

## Permission Controls for MCP Tools

MCP tools follow the same permission system as built-in tools [4]:

- Can be added to `permissions.allow`: e.g., `"mcp__puppeteer__puppeteer_navigate"` [4]
- Can be added to `permissions.deny`: e.g., `"mcp__servername"` [4]
- Tools that make network requests require user approval by default [1]

## SDK-Level Controls

- `allowed_tools` and `disallowed_tools` apply to MCP tools the same as built-in tools [7]
- `canUseTool` callback enables runtime evaluation of MCP tool calls [7]
- For locked-down agents, pair `allowedTools` with `permissionMode: "dontAsk"` to deny unlisted tools outright [7]

## Remote MCP Server Security

- Native OAuth support for remote MCP servers -- authenticate once, no API keys to manage [22]
- Users should only connect to trusted servers and review requested permissions during auth [22]
- Recommendation: limit scopes when possible and deny access if requested permissions seem unnecessary [22]

## Enterprise Controls

Enterprise admins can deploy managed policy settings to enforce MCP server configurations across all users. [from search results]

The `--allowedTools` CLI flag can be used for session-specific MCP tool permissions. [4]

## Sandboxing MCP Servers

The sandbox runtime can sandbox MCP servers in addition to arbitrary processes and agents. [6]

`CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` strips credentials from subprocess environments including MCP stdio servers. [10]

## Known Security Issues

- `deny: ["mcp__servername"]` permission rules did not remove MCP server tools before sending to the model, allowing Claude to see and attempt blocked tools -- fixed [11]
- MCP tools added to Anthropic's reviewed MCP directory must adhere to security, safety, and compatibility standards [8], but most MCP servers are community-maintained and unaudited

## Gaps and Limitations

- Anthropic explicitly states it does not manage or audit MCP servers [1] -- security responsibility falls entirely on the user
- No built-in mechanism to verify MCP server integrity or authenticity beyond initial trust prompt
- Community MCP servers are a significant attack surface for prompt injection and data exfiltration
- OAuth-based remote MCP servers depend on the user correctly limiting scopes
