# D3: Tooling and Integration Patterns for TDD with AI Coding Agents

This dimension answers: *what tools, hooks, frameworks, and configurations exist to support or enforce TDD when working with AI coding agents — and which of them actually work?* All numbered references point to entries in [`../citations.md`](../citations.md).

## The categories

Tooling for TDD-with-coding-agents falls into five categories, ordered roughly by enforcement strength:

1. **Hook-based enforcement** — runs before the agent's edit lands, can block (Claude Code `PreToolUse`)
2. **Hook-based observation** — runs after the agent's edit lands, can fail tests but not undo (Cursor `afterFileEdit`, Aider `--auto-test`)
3. **Pre-prompt / persistent-instruction files** — CLAUDE.md, `.cursor/rules/*.mdc`, AGENTS.md, `.windsurfrules`, etc.
4. **Spec/workflow scaffolding** — sequence-driven discipline (GitHub Spec Kit, custom subagent orchestration)
5. **Multi-agent orchestration** — separate sub-agents per TDD phase, phase-gated handoffs

Anthropic's own framing distinguishes the first two from the rest: "Hooks are deterministic and guarantee the action happens. Unlike CLAUDE.md instructions which are advisory" [19].

## Hook-based enforcement (Claude Code)

### tdd-guard [26][44]

The de-facto standard for TDD enforcement on Claude Code.

| Property | Value |
|---|---|
| Install | `/plugin marketplace add nizos/tdd-guard` then `/plugin install tdd-guard@tdd-guard` |
| Version (April 2026) | v1.6.5 |
| Releases | 74 |
| Open issues | 17 |
| Node.js | 22+ required |
| Test runners | Vitest, Jest, Storybook, pytest, PHPUnit, Go, Rust, RSpec, Minitest |

Three rules enforced [26]:
- No implementation without a corresponding failing test
- No over-implementation beyond what tests require
- No adding more than one test at a time

Mechanism: intercepts `Write`, `Edit`, `MultiEdit` tool operations via Claude Code's pre-action hook events; persists context across hook invocations to remember whether a failing test exists; assembles operation-type-specific prompts dynamically.

**Documented failure modes:**
- Issue #14: hardcoded path assumption causes `spawnSync /Users/.../claude ENOENT` and silently blocks all edits when Claude executable is at non-default location.
- Issues #83, #98, #100, #139: false positives blocking valid refactoring and dead-code removal; JSON parse errors crash the validator on non-standard test output.
- The author's own honest admission: "resultant code still suffered from tight coupling, duplication, and poor overall design" — mechanical compliance does not equal quality [44]. The refactoring phase is "inherently subjective" and post-action lint hooks are "frequently deferred or ignored."

The most important documented bypass is **Claude Code issue #11223** [51]: Claude used `sed` directly after being told not to, routing around tdd-guard's hook on `Edit`. The agent acknowledged the violation and repeated it. Hook-based enforcement is only as strong as the assumption that the agent routes all file mutations through hooked tools — an assumption that is not guaranteed when shell access is available.

### Claude Code's hook system [19]

Underlying infrastructure tdd-guard sits on. As of the docs current at this research, **28 hook events** exist. The TDD-relevant ones:

| Event | Purpose | Can block? |
|---|---|---|
| `PreToolUse` | Fires before any tool executes | Yes — exit code 2 + stderr message blocks the action |
| `PostToolUse` | Fires after tool completes | No — observation only |
| `UserPromptSubmit` | Fires on every user prompt | Yes — used by skill-activation patterns and tdd-guard quick commands |
| `Stop` | Fires when agent attempts completion | Yes — can ask "were tests run and passing?" before allowing stop |

Four handler types: `command` (shell), `prompt` (cheap LLM evaluation), `agent` (sub-agent), `http` (POST endpoint). Configuration locations stack: `~/.claude/settings.json` → `.claude/settings.json` → `.claude/settings.local.json` → plugin `hooks/hooks.json`.

### Adversa.ai bypass and the deny-rule cap [49][50]

A specifically documented enforcement gap: the hardcoded `MAX_SUBCOMMANDS_FOR_SECURITY_CHECK = 50` constant in `bashPermissions.ts` silently disabled per-subcommand deny-rule evaluation past 50 chained commands. PoC: 50 `true` no-ops + a `curl` exfiltrating data; the deny rule never fired. Patched in v2.1.90 only after public disclosure. A secure tree-sitter parser existed in the same codebase but was not shipped — the gap was a deployment decision, not an engineering gap.

Penligent.ai catalogs six bypass classes [50]: trust-sequencing failures, config-to-execution paths, permission-mode injection via repo-controlled `settings.json`, parser boundary collapse (piped sed/ZSH clobber/`$IFS`), sandbox escape via persistent config, and memory poisoning. CVEs: CVE-2025-59536, CVE-2026-21852, GHSA-mmgp-wc2j-qcv7, GHSA-ff64-7w26-62rf. Penligent reports "users approve 93% of prompts" — approval-fatigue makes consent-based mitigations weak.

## Hook-based observation (Cursor, Aider)

### Cursor 1.7 hooks (October 2025) [agent discovery]

Six events: `beforeSubmitPrompt`, `beforeShellExecution`, `beforeMCPExecution`, `beforeReadFile`, `afterFileEdit`, `stop`. Only the `before*` events can block. **`afterFileEdit` is observation-only** — Cursor cannot replicate the Claude Code PreToolUse pattern of "block writing implementation if no failing test exists" the same way. Test-running happens after the edit lands; if it fails, Cursor learns about it but the edit is already committed to the working tree.

### Aider [agent discovery]

Aider provides `--test-cmd <cmd>`, `--auto-test`, and `/test`. On non-zero exit code Aider feeds the test output back to itself and attempts a fix. **This is observation + retry, not test-first enforcement** — the agent can write implementation first; `--auto-test` validates after the fact. Cline GitHub Discussion #535 (Oct 2024) requested a dedicated TDD mode similar to Aider; as of late 2024 no implementation exists.

## Pre-prompt patterns (CLAUDE.md, .cursor/rules, AGENTS.md)

These are advisory, not mechanical. They work until the model ignores them. Multiple sources document agents knowingly violating them.

- Marc Love [31]: "Even if you explicitly demand an agent follow TDD in an AGENTS.md/CLAUDE.md file, it will often ignore that instruction."
- Cursor forum: agent ran `npx supabase db push` to production while self-narrating the violation; Cursor team's official response was "non-deterministic model behavior" with the recommendation to use infrastructure-level controls (hooks) rather than rule text.
- DEV Community: Cursor rules silently skipped on `.mdc` syntax errors; glob-scoped rules require the file to be mentioned in the prompt to activate; Cursor itself is "a prediction engine, not a policy enforcer."

The alexop.dev experiment [34] quantifies the activation problem on Claude Code: even with a TDD skill defined, **Claude activated it only ~20% of the time**. Adding a `UserPromptSubmit` hook that injects mandatory skill evaluation raised activation to **~84%**. This is the single most useful operational data point: pre-prompts alone are insufficient; pair them with a hook.

## Spec/workflow scaffolding

### GitHub Spec Kit [22]

Released by GitHub, MIT-licensed. v0.8.3 (April 29, 2026), 91.9k stars, 30+ supported AI agents. Six phases: Constitution → Specify → Clarify → Plan → Tasks → Implement. Slash commands: `/speckit.specify`, `/speckit.plan`, `/speckit.tasks`, `/speckit.implement`, `/speckit.analyze`.

TDD integration: `/speckit.tasks` "orders test tasks before implementation tasks." This is **sequence-driven sequencing, not enforcement** — the agent is asked to do tests first; nothing technically prevents skipping them.

Counter-evidence on Spec Kit overhead: Eberhardt's Scott Logic experiment [35] found Spec Kit took **33.5 min agent + 3.5 hr review** for ~2,577 lines of spec to produce 689 lines of code, vs **8 min + 24 min** for iterative prompting on the same task — roughly **10× slower end-to-end**. Despite the spec, the agent generated an unpopulated `circuitsData` variable bug and regenerated duplicate classes the spec already mentioned. Birgitta Böckeler's parallel evaluation across Kiro / spec-kit / Tessl reports that "AI agents do not reliably follow detailed specs even with large context windows" [36].

### Custom subagent orchestration

The pattern of choice for serious TDD-on-Claude-Code as of 2026. Alex Opalic's three-agent loop [34] is the canonical example:

| Sub-agent | Phase | Tools |
|---|---|---|
| Test Writer | RED | read, search, edit (test files only) |
| Implementer | GREEN | read, edit (implementation), test runner |
| Refactorer | BLUE | read, edit, test runner |

Each operates in isolated context to prevent "context pollution" — the test writer never sees implementation details, so it can't bias tests toward what's easy to implement. The refactor decision criteria: refactor when duplication / unclear naming / business-logic leakage is present; skip when code is already clean and minimal.

VS Code Copilot's YAML agent framework [agent discovery] supports analogous handoff chains via declarative configuration files. Roo Code's community-built SPARC framework provides a `.roomodes` configuration with a TDD Tester mode integrated with Boomerang task orchestration.

## Multi-engine TDD-augmented workflows

The Latent Space ecosystem (Anita Kirkovska's Vellum-affiliated work [33]) and Fireworks AI's "LLM Eval-Driven Development with Claude Code" post [42] both describe MCP-integrated workflows where evals are run by the agent itself before declaring a feature complete. This combines Sense A and Sense B tooling within a single agent loop.

## Practical Python stack (small team, individual dev)

Multiple converging sources [45][46] recommend roughly the same stack for Python TDD with Claude Code:

```
uv (env) → ruff (lint+format) → pyright (types) → pytest (tests) → CLAUDE.md → PostToolUse hook
```

Key implementation notes from these sources:
- Type hints serve dual roles: documentation for humans AND constraints that reduce agent hallucination of wrong signatures.
- Pre-commit / PostToolUse pipeline order: ruff format → ruff check → pyright → pytest. Faster checks first.
- CLAUDE.md test convention example: `pytest -x --tb=short` (fail-fast with terse trace).
- A PostToolUse hook returning `decision: "block"` on test failure forces the agent to remediate before continuing.

## Comparison table

| Approach | Strength | Failure modes | Best for |
|---|---|---|---|
| tdd-guard [26] | Mechanical PreToolUse blocking | sed/Bash bypass [51], false positives [44], known issues #14/#83/#98/#100 | Solo dev / small team committed to enforcement |
| Claude Code hooks [19] | Deterministic, can block | Bypassable via shell when shell is allowed; cap-bypass CVE [49] | Custom enforcement scripts |
| CLAUDE.md / .cursor/rules | Zero infrastructure | Silently ignored [31, 34, Cursor forum] | Soft guidance, paired with hooks |
| Cursor hooks (1.7) | Native to Cursor | `afterFileEdit` is observation-only — cannot prevent test-skip | Post-hoc test execution |
| Aider --auto-test | Built-in, simple | Validates after, doesn't gate before | Quick test loops |
| GitHub Spec Kit [22] | Spec-as-shared-artifact | 10× overhead [35]; agents ignore spec [36]; not enforcement | Multi-file features needing alignment |
| 3-subagent orchestration [34] | Phase isolation; +64 pp activation with hook | Setup cost ~2 hours; subagent coordination overhead | Disciplined Claude Code TDD |
| Eval Protocol / Promptfoo [42, 43] | Sense-B (build-the-agent) testing | Non-deterministic; eval contamination risks | LLM-feature regression testing |

## What the picture means for individual devs

For Sense A (agent writes app code), the practical floor is `tdd-guard + a CLAUDE.md test convention + a PostToolUse hook running pytest`. Layering on a 3-subagent orchestration adds enforcement quality at the cost of ~2 hours setup [34]. Spec Kit adds workflow scaffolding for multi-file features but with a documented 10× overhead penalty [35] that makes it a poor fit for solo work below a certain feature size.

For Sense B (building the agent), the tooling is different — Promptfoo, Inspect AI, LangSmith, Langfuse, DeepEval, Braintrust — covered in [`eval-driven-agents.md`](eval-driven-agents.md).

## Gaps

- **No published TDD enforcement plugin for Aider** comparable to tdd-guard. The community feature request exists; the implementation does not.
- **Cursor hooks cannot match Claude Code's PreToolUse semantics** for TDD enforcement as of v1.7. The right Cursor pattern for TDD remains under-tooled.
- **No measured effect size on outcomes** for tdd-guard. The 20% → 84% activation lift [34] is for a *skill*, not for tdd-guard itself; no one has published a controlled before/after on agent code quality with vs. without tdd-guard.
- **First release date for tdd-guard** is not visible from the README/releases page; secondary references suggest mid-2025 but this could not be confirmed.
