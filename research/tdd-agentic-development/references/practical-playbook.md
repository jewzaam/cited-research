# D6: Practical Playbook for Individual Developers and Small Teams

This dimension answers: *given everything in D1–D5, what should an individual developer or small team actually do?* All numbered references point to entries in [`../citations.md`](../citations.md).

## The decision tree (at the situation level)

The practitioner literature converges on roughly this decision matrix:

| Situation | Recommended approach | Why |
|---|---|---|
| Bug fix with regression risk | TDD — write failing repro test first | Test serves as both correctness signal and regression guard; agent has clear hill to climb |
| Well-scoped single function | TDD — human writes test, agent implements | Strong empirical support [3]; effect size +9 to +30 pp |
| New feature, requirements fuzzy | Spec/plan first, then TDD per module | TDD doesn't answer "are we building the right thing?"; spec scoping does |
| Multi-file / multi-layer feature | Plan mode → tasks → TDD per task | Anthropic's own heuristic [19]; Spec Kit-style scaffolding optional but adds 10× overhead [35] |
| Refactoring existing code | TDD with characterization tests | Tests pin behavior before agent rewrites |
| Throwaway script / sandbox | Skip TDD; iterate with agent | Cost outweighs benefit; vibe-coding posture [37] is fine here |
| Production LLM-backed feature (Sense B) | Eval-driven (Husain pattern [30]: build → observe → eval failures) | Non-determinism breaks unit-test pass/fail; trajectory eval over output eval |
| Agent's own code (its prompt, its scaffold) | Eval-driven from day one [18, 24] | EDDOps process model [8]; pass^k consistency over pass@k |

Anthropic's own framing [19]: "Planning is most useful when you're uncertain about the approach, when the change modifies multiple files, or when you're unfamiliar with the code being modified. **If you could describe the diff in one sentence, skip the plan.**"

## The minimum useful Python TDD setup with Claude Code

Multiple converging sources [45, 46, 19] point to a remarkably consistent stack:

```
uv (env)
  ↓
ruff (lint + format)
  ↓
pyright (types)
  ↓
pytest (tests)
  ↓
CLAUDE.md (advisory conventions)
  ↓
PostToolUse hook (deterministic enforcement)
```

### CLAUDE.md test convention (concrete example)

```markdown
# Testing Conventions
- Always write a failing test BEFORE implementation.
- Tests must initially FAIL — confirm red before green.
- Run: pytest -x --tb=short
- Tests live in tests/, named test_*.py. Use pytest.raises for expected exceptions.
- Don't modify existing tests to make them pass; if a test is wrong, say so.
```

Keep it short. Anthropic explicitly warns: "If your CLAUDE.md is too long, Claude ignores half of it because important rules get lost in the noise" [19].

### PostToolUse hook (deterministic test gate)

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "pytest -x --tb=short"
          }
        ]
      }
    ]
  }
}
```

A non-zero exit code feeds back to Claude as "tests failed, fix them before continuing." This is the deterministic complement to the advisory CLAUDE.md content.

### tdd-guard if you want PreToolUse blocking [26]

```bash
/plugin marketplace add nizos/tdd-guard
/plugin install tdd-guard@tdd-guard
/tdd-guard:setup
```

Three rules: no implementation without failing test, no over-implementation, no multiple tests at once. Known limitations [44, 51]: bypassable via shell `sed`; false positives on refactoring (issues #83, #98, #100, #139). Worth using anyway because most agent runs don't actively try to bypass.

### The 3-subagent orchestration tier (when discipline matters)

For projects where TDD discipline genuinely matters, alexop.dev [34] documents a three-subagent pattern:

| Sub-agent | Phase | Tools |
|---|---|---|
| `tdd-test-writer` | RED | Read, Search, Edit (test files only) |
| `tdd-implementer` | GREEN | Read, Edit (impl), test runner |
| `tdd-refactorer` | BLUE | Read, Edit, test runner |

Plus a `UserPromptSubmit` hook injecting skill evaluation, which the author measured as raising activation from ~20% to ~84%. Setup cost: ~2 hours. The phase isolation prevents context pollution — the test writer cannot bias tests toward what's easy to implement because it never sees the implementation [34].

Refactor-decision criteria [34]:
- Refactor when: clear duplication, reusable logic, naming obscures intent, business logic in components
- Skip when: code already clean, refactor risks over-engineering, implementation minimal and focused

## TDD vs Spec-Driven Development vs Constraint-Driven — the 2026 picture

Three workflow paradigms exist concurrently. They're not mutually exclusive but they are pitched as alternatives.

### Spec-Driven (GitHub Spec Kit) [22, 35, 36]

**When it pays off:** multi-file features touching architectural surface; team alignment matters; the agent will be left running while a human is unavailable; you can absorb the markdown overhead.

**When it doesn't:** Eberhardt's Scott Logic experiment [35] is the cleanest data: Spec Kit took 10× longer than iterative prompting on a Formula-1 timing implementation, generated 2,577 lines of spec for 689 lines of code, and **still produced an unpopulated-variable bug**. Birgitta Böckeler [36]: "AI agents do not reliably follow detailed specs even with large context windows." Spec Kit gives you alignment artifacts; it does not enforce correctness.

### TDD (Sense A) [28, 32, 19]

**When it pays off:** scoped functions/modules; bug fixes; refactoring; situations where "did it work?" can be answered by an executable test. Strong empirical floor [3, 4, 2, 16].

**When it doesn't:** brand-new feature where you don't yet know what "done" looks like; LLM-output features where assertions are flaky; throwaway scripts.

### Constraint-Driven (types + linters) [45, 46]

**When it pays off:** Python projects where pyright + ruff catch agent errors at zero token cost; static analysis is a free first line of defense; type annotations measurably reduce hallucinated wrong signatures.

**When it doesn't:** behavioral correctness — types prove the function compiles, not that it does the right thing. Constraint-driven is best paired with TDD, not used as a replacement.

### Vibe Coding [37, 39, 40]

**When it pays off:** sandboxed personal projects, prototypes you'll throw away, learning a new framework. Karpathy's original framing was modest — "a way to give in to the vibes" for fun side projects, not for production. The risk surface is well-documented [40] for anything beyond that.

**When it doesn't:** anything with a user-facing surface, anything storing data, anything that touches production. The 7 documented incidents in [40] cover the full spectrum: API key exposures, auth bypasses, RCE, accidental DB deletions during code freezes.

The honest small-team approach: **don't pick one paradigm and apply it monolithically**. Match the situation. Most small teams already do this implicitly; making the matching explicit reduces the chance that vibe-coding posture leaks into production-critical code.

## Sense B: minimum useful eval setup for an LLM-backed feature

If you're building a feature whose output is generated by an LLM (chat, content generation, an agent doing its own work), the minimum useful setup [18, 30, 33, 43]:

1. **Capture 20-50 real failures** before building anything elaborate. Ship the agent at minimum useful quality first; collect production traces.
2. **Define one binary grader and one rubric grader per failure mode.** Code-based first ("does the response include the user's name?"); LLM-as-judge second for the open-ended dimensions.
3. **Run evals on every prompt change.** If you can't run them in CI, run them on a button-push before deploying. Husain & Shankar [30]: "no prompt change ships without a fresh eval run."
4. **Track pass^k, not just pass@k** for non-deterministic agents [18]. Consistency matters in production.
5. **Use Promptfoo [43] / Inspect AI [25] / DeepEval if you want CI integration**, or LangSmith/Langfuse if you want trace-and-eval combined. The choice of framework matters less than committing to running evals.

## "How would I prove this is worth doing?" — the meta-question

Several sources are honest about the absence of definitive proof:

- **No controlled study compares TDD vs no-TDD with AI agents on outcome metrics** that practitioners care about (production defect rate, time-to-correct, maintainability).
- **METR's RCT [9]** has TDD as a confound, not a treatment.
- **TDAD's ablation [1]** is the cleanest direct test and gives a paradoxical result: TDD prompting alone is *worse*; TDD with graph-derived test-impact context is *much better*. This means the practical question is less "should I TDD with my agent?" and more "do I have a way to point my agent at the right tests?"

For an individual dev, the heuristic that survives the literature is:

- If the test surface is human-curated and pointed at the change being made → TDD probably helps
- If the test surface is agent-generated during the session → it probably doesn't help and costs tokens
- If the test surface doesn't exist → write one before turning the agent loose; this alone captures most of the benefit

## A 90-minute starter kit (for a small Python project on Claude Code)

If you adopt nothing else:

1. **(15 min)** Add a `CLAUDE.md` with a 5-line testing convention.
2. **(15 min)** Add a `PostToolUse` hook that runs `pytest -x --tb=short` on every edit.
3. **(20 min)** Install tdd-guard via the plugin marketplace [26]. Accept the false-positive risk; you can disable it for specific tasks.
4. **(20 min)** Write a `pytest`-based test for the next thing you're going to ask the agent to implement. Confirm it fails.
5. **(20 min)** Ask the agent to make the test pass. Review the diff.

The test in step 4 is the load-bearing intervention. Steps 1-3 are scaffolding that makes step 4 reliably engaged across sessions. If you skip steps 1-3, your test will still help on this specific feature; if you skip step 4 and rely only on 1-3, the agent's verbal compliance is unreliable [31, 41] and you'll get performative TDD without the benefit.

## What this playbook does NOT promise

- **Faster shipping.** The METR RCT [9] suggests that under controlled conditions, AI tools made experienced developers slower, not faster. This may invert with smaller projects, less expert developers, or different task types — but the strong "AI plus discipline ships you faster than no discipline" claim is not empirically grounded.
- **Higher code quality automatically.** Liu et al. [13] found 89.3% of issues in AI-authored commits are code smells; 22.7% persist at the latest version of the repo. Tests passing and code quality are demonstrably orthogonal.
- **A fix for context loss.** TDD is friendly to context-window constraints (Gorman's argument [32]) but doesn't eliminate them. For long sessions, expect context pollution regardless of discipline.

## Synthesis: the one-sentence playbook

For agent-as-coder work: write the failing test yourself, then turn the agent loose with mechanical hooks ensuring tests run on every edit. For agent-as-product work: collect real failures first, build evals from them, never ship a prompt change without running the eval suite. Both halves of the playbook depend on a discipline that no tool can supply for you — deciding what "passing" means before you start.
