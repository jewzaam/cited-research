# Claude Code Integration Mechanics

How to configure Claude Code to use non-Anthropic models for subagent verification tasks. This is the most critical dimension because the integration mechanism determines whether this entire research direction is viable within Claude Code.

## Answer: Not Viable as Native Subagents Today

Non-Anthropic models cannot be used as native Claude Code subagents through any supported mechanism [2][3][10].

## Model Configuration Methods

Claude Code provides several model configuration mechanisms [2]:

| Method | Scope | What It Controls |
|---|---|---|
| `ANTHROPIC_DEFAULT_*_MODEL` | Per-alias | What opus/sonnet/haiku aliases resolve to |
| `CLAUDE_CODE_SUBAGENT_MODEL` | Subagents | Default model for subagents without explicit model |
| `ANTHROPIC_CUSTOM_MODEL_OPTION` | Session | Adds one custom entry to /model picker |
| `modelOverrides` in settings.json | Per-version | Maps Anthropic model IDs to provider strings |
| `ANTHROPIC_MODEL` | Session | Per-session model override |

## Subagent Model Resolution Order

From official documentation [3]:

1. `CLAUDE_CODE_SUBAGENT_MODEL` environment variable
2. Per-invocation `model` parameter from Agent tool
3. Subagent definition's `model` frontmatter field
4. Main conversation's model

The `model` field in frontmatter accepts: aliases (`sonnet`, `opus`, `haiku`), full Anthropic model IDs (e.g., `claude-opus-4-7`), or `inherit` [3]. These are **Anthropic model IDs only** — no mechanism exists to specify non-Anthropic models.

## Critical Limitations

### Hardcoded Model Aliases

The Agent tool's model parameter and subagent frontmatter accept only Anthropic model identifiers [10]. GitHub issue #34821 requested custom model aliases and was **closed as NOT PLANNED** [10]. No extension mechanism (plugin, hook, or MCP) can extend the model alias registry [10].

Related issues, all unaddressed: #2480 (19 upvotes), #12386, #5456, #4377 [10].

### Active Bugs in Model Routing

- **#43869** (OPEN): All subagents resolve to parent model regardless of configuration [11]
- **#47488** (OPEN): Agent tool model parameter silently ignored in Cowork mode [12]
- **#18025** (CLOSED NOT PLANNED): Custom models intermittently fall back to Anthropic model IDs during tool use [13]

### API Format Requirement

Claude Code requires one of three API formats [2]:
- Anthropic Messages API (`/v1/messages`)
- Bedrock InvokeModel
- Vertex rawPredict

This is **not OpenAI chat completions format**. The gateway must forward `anthropic-beta` and `anthropic-version` headers [2]. Gateway model discovery (`CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1`) only adds models whose ID matches known Anthropic patterns [2].

## Integration Paths (Ranked by Viability)

### Path A: External Verification Harness (Recommended)

Run verification as a separate process outside Claude Code subagents.

Architecture:
1. Claude Code runs normally with Anthropic models for all subagent work
2. A SubagentStop hook captures subagent outputs [3]
3. External script sends outputs to any verification LLM via its native API
4. Results written to a file the main Claude Code session reads

**Confidence: 0.85.** Uses only supported features. Works with any model that has an API. No Claude Code features lost. Verification is truly independent.

**Limitations**: Not integrated into Claude Code's conversation flow. Requires maintaining a separate service. Hook output limited to stdout/stderr.

### Path B: Alias Hijacking via LiteLLM Proxy (Fragile)

1. Set `ANTHROPIC_DEFAULT_HAIKU_MODEL` to a custom string
2. Point `ANTHROPIC_BASE_URL` at a LiteLLM proxy
3. Proxy translates Anthropic Messages format to target model's API
4. Subagents requesting "haiku" route to the non-Anthropic model

**Confidence: 0.35.** Theoretically possible but:
- Two open bugs affect model routing (#43869, #47488) [11][12]
- LiteLLM had a supply chain attack (PyPI versions 1.82.7-1.82.8 compromised) [2]
- Translation is inherently lossy for Anthropic-specific features
- Only 3 alias slots available, and Claude has no awareness of actual model selected [10]

### Path C: Direct Non-Anthropic Subagent (Not Viable)

Explicitly rejected by Anthropic [10]. No mechanism exists.

## Features Lost When Routing Through Translation

| Feature | Impact |
|---|---|
| Extended thinking / adaptive reasoning | Requires Anthropic-specific thinking blocks |
| Effort levels | Anthropic-proprietary, meaningless for other models |
| Prompt caching | Anthropic's cache_control mechanism has no equivalent |
| Tool use format | Anthropic uses tool_use/tool_result blocks, not OpenAI function_call |
| anthropic-beta features | Fail silently |
| Model capability detection | Claude Code matches model ID against known patterns [2] |

## Practical Workaround for Today

The community workaround [10]: hijack the 3 built-in aliases via `ANTHROPIC_DEFAULT_*_MODEL` env vars to point to non-Anthropic models behind a LiteLLM or similar proxy. A community project (claude-alias-patch) patches 6 locations in cli.js to register additional aliases, but requires manual re-patching on updates.

The most practical approach: run non-Anthropic verification **outside** the subagent system entirely, or prioritize deterministic verification (tests, linters, type checkers) which provides truly independent error detection without LLM integration friction.

## Gaps and Limitations

- Whether the per-invocation `model` parameter from the Agent tool accepts full model IDs (like frontmatter does) could not be confirmed — the tools-reference page does not expose the parameter schema
- Anthropic's position on future non-Anthropic model support is unclear — "closed as not planned" may indicate a temporary or permanent stance
- LiteLLM proxy compatibility with specific model features (thinking blocks, tool streaming) is untested
