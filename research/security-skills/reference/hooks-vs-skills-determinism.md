# Hooks vs Skills: Deterministic vs Probabilistic Triggering

## Dimension

This reference file covers the fundamental architectural distinction between Claude Code hooks (deterministic) and skills (probabilistic/LLM-matched), with reliability implications for security enforcement.

## Hooks: Deterministic Execution

Hooks are "user-defined shell commands that execute at specific points in Claude Code's lifecycle" that "provide deterministic control over Claude Code's behavior, ensuring certain actions always happen rather than relying on the LLM to choose to run them" [1].

The official documentation explicitly frames hooks as the antithesis of LLM-dependent behavior: they fire on every matching event, regardless of what the LLM decides to do.

### Mechanism

1. An event fires (e.g., `PreToolUse` when Claude is about to call a tool)
2. Claude Code checks all configured hooks for that event
3. Hooks with matching `matcher` patterns execute
4. The matcher is a regex pattern matched against a specific field (tool name for PreToolUse/PostToolUse) [1]
5. Exit code determines outcome: 0 = proceed, 2 = block, other = non-blocking error [1]

### Key Property

Hooks operate **outside the LLM's reasoning chain**. As one analysis states: "Autonomous AI agents need deterministic control layers that operate outside the LLM's reasoning chain. The agent can be creative, adaptive, and autonomous in its problem-solving while hooks enforce the non-negotiable constraints" [23].

The gap this addresses: "A CLAUDE.md instruction says 'always run the linter.' The agent usually complies. A PostToolUse hook runs the linter after every file write, every single time, no exceptions. That gap between 'usually' and 'always' is where production systems fail" [23].

## Skills: LLM-Based Triggering

Skills use "pure LLM reasoning" for triggering — "no algorithmic routing or intent classification at the code level. Claude Code doesn't use embeddings, classifiers, or pattern matching to decide which skill to invoke" [3].

### Mechanism

1. Skill descriptions are loaded into context (subject to character budget) [2]
2. When a user prompt arrives, Claude's language model decides whether any skill is relevant
3. "The decision happens inside Claude's forward pass through the transformer, not in the application code" [3]
4. If Claude decides a skill is relevant, it invokes the Skill tool to load full instructions
5. Full skill content is then injected into the conversation context [2]

### Reliability Implications

The `description` field in SKILL.md frontmatter is the **sole trigger mechanism** for automatic invocation. Claude uses this description "to decide when to apply the skill" [2]. If the description doesn't match Claude's interpretation of the current task, the skill won't fire.

The official troubleshooting section acknowledges this reliability gap directly:
- "If Claude doesn't use your skill when expected: Check the description includes keywords users would naturally say... Try rephrasing your request to match the description more closely" [2]
- "If Claude uses your skill when you don't want it: Make the description more specific" [2]

A community developer created a `UserPromptSubmit` hook specifically to force skill evaluation because "Claude Code often ignores available skills entirely and proceeds with generic responses instead of leveraging specialized skill knowledge" [20].

### The `disable-model-invocation` Flag

Skills can be marked `disable-model-invocation: true` to prevent automatic LLM-triggered invocation, requiring explicit `/skill-name` invocation by the user [2]. This is the opposite of mandatory: it makes the skill manual-only.

There is **no `force-model-invocation` or `mandatory` flag** in the frontmatter specification [2]. No mechanism exists in Claude Code for skills that must always run.

## Comparison Table

| Property | Hooks | Skills |
|---|---|---|
| Trigger mechanism | Event + regex matcher | LLM description matching |
| Deterministic | Yes | No |
| Can block actions | Yes (exit 2) | No |
| Fires on subagent actions | Yes [1] | No (unless subagent loads skill) |
| Can be bypassed by LLM | No | Yes (LLM may not match description) |
| Can be made mandatory | Yes (configure and it always fires) | No (no mandatory flag exists) |
| Security suitability | Enforcement | Advisory guidance only |
| Official guidance | "ensuring certain actions always happen" [1] | "Claude uses this to decide when to apply" [2] |

## Implications for Security

For any security check that must run on every occurrence of an event (e.g., every `npm install`, every file write to sensitive paths), **hooks are the only viable mechanism**. Skills are advisory and probabilistic -- they should be used for guidance ("here's how to write secure code") but not for enforcement ("this check must run before every dependency addition").

## Citations

All citations reference `../citations.md`. Key sources: [1] Official hooks guide, [2] Official skills documentation, [3] Skills deep-dive analysis, [20] Mandatory skill activation workaround, [23] Deterministic control layer analysis.
