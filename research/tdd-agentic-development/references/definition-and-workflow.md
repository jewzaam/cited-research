# D1: Definition and Adapted Workflow

This dimension answers: *what does "TDD for agentic development" actually mean, and how is the workflow adapted from classical Kent-Beck-style TDD?* All numbered references point to entries in [`../citations.md`](../citations.md).

## The two senses of "TDD for agentic development"

The phrase is used in the literature to mean at least two distinct things, often without distinguishing them. Independent sources converge on this taxonomy.

### Sense A — Agent-as-coder (TDD-as-guardrail)

The human writes a failing test. The coding agent (Claude Code, Cursor, Aider, Codex, etc.) implements just enough code to make the test pass. The human reviews the green diff and triggers refactoring.

Simon Willison defines this as "red/green TDD" — "shorthand for the much longer 'use test driven development, write the tests first, confirm that the tests fail before you implement the change that gets them to pass'" [28]. He calls it "a *fantastic* fit for coding agents" because it prevents two distinct failure modes: code that doesn't actually work, and code that works but is unnecessary [28].

Tweag's Agentic Coding Handbook reframes the same workflow as "tests-as-prompts": the failing test serves dual purposes — the executable correctness check that classical TDD provides, and a natural-language specification the agent reads as the prompt [47]. This collapses "test writing" and "requirement specification" into a single artifact.

Jason Gorman makes the structural argument for why this fit is real and not coincidental: LLMs have effective context limits smaller than advertised maximums, and TDD's micro-iterative steps fit within those limits. "If the model's first change breaks the code, that broken code is now in its context" — frequent green-or-revert testing prevents context pollution [32].

### Sense B — Building-the-agent (eval-driven development)

The developer is not writing application code with an agent; the developer *is* building an LLM-powered agent. Tests as classically defined (binary pass/fail unit assertions) don't apply because outputs are non-deterministic.

The replacement is eval-driven development (EDD): define the eval set first, then iterate on the prompt, scaffold, model, or fine-tune until evals pass at acceptable thresholds.

The most formal definition is EDDOps (Xia et al., arXiv:2411.13768): "evaluation as a continuous, governing function rather than a terminal checkpoint," unifying offline (development-time) and online (runtime) evaluation in a closed feedback loop [8]. The paper explicitly contrasts this with TDD/BDD, which "are primarily applied in pre-deployment phases and assume relatively stable specifications and deterministic test outcomes."

Anthropic's official position is explicit: "We recommend practicing eval-driven development: build evals to define planned capabilities before agents can fulfill them, then iterate until the agent performs well" [18]. The post introduces pass@k vs. pass^k metrics for handling non-determinism: "At k=1, they're identical… By k=10, pass@k approaches 100% while pass^k falls to 0%" [18].

evaldriven.org's community manifesto distills the position: "Build evals first. Code is generated. Evals are engineered" [24].

### Why the distinction matters

Marc Love's January 2026 critique exposes definition drift directly: "Even if you explicitly demand an agent follow TDD in an AGENTS.md/CLAUDE.md file, it will often ignore that instruction" [31]. He argues TDD's friction is designed for *human* cognition. Telling a generative model to do TDD doesn't cause it to experience the cognitive feedback that drove the practice in the first place.

The "TDD for AI" frame can be incoherent if it bundles Sense A and Sense B without distinguishing them. The same word covers both "I write tests and the agent fills in code" (Sense A — guardrails for generation) and "I write evals and iterate on a non-deterministic agent" (Sense B — specifications for stochastic behavior). These are different practices with different success criteria.

## The adapted Red-Green-Refactor for agent-as-coder

The classical cycle adapts to agent-as-coder roughly as follows. Multiple practitioner sources converge on a similar shape.

| Phase | Classical TDD | Agentic adaptation |
|-------|--------------|-------------------|
| **Red** | Human writes a failing test capturing intended behavior | Human writes the test (or describes it precisely enough that the agent generates it under supervision); confirms it fails |
| **Green** | Human writes minimum code to pass | Agent generates implementation; tests run; loop continues until green |
| **Refactor** | Human refactors with tests as safety net | Agent or human refactors; tests must remain green; specialised "refactor" sub-agent or skill may apply discipline [34] |
| **Commit** | Human commits on green | "Commit on green, revert on red" Git discipline prevents broken state from polluting agent context [32] |

The non-trivial change is in *who* writes the test. TDFlow's empirical comparison is the cleanest data point: agents produce 94.3% pass on SWE-Bench Verified when given human-written reproduction tests, vs 68.0% when generating their own tests — a 26.3 pp gap [2]. The paper explicitly frames its envisioned operating model as "a human-LLM interactive system" where humans write tests and the LLM solves them.

## The five-stage Sense-B workflow (eval-driven for AI-backed features)

For features whose output *is* a model — a chatbot, a content generator, a multi-step agent — Anita Kirkovska's Latent Space framework is the canonical practitioner reference [33]:

1. **Planning / Speccing** — Define where AI adds value, map user journeys, assess data quality, identify technical risks.
2. **Experimentation** — Build an MVP (a simple prompt or orchestrated workflow); validate on small scale.
3. **Evaluation at scale** — Build test databases with product/domain experts. Run automated evals. Iterate: "create tests → run evals → make small change → check for regressions."
4. **Release management** — Decouple AI-system deployments from application releases; version control prompts; enable rollback and A/B testing.
5. **Observability** — Capture production edge cases via traces; feed back into the eval set.

Kirkovska's most operationally important observation: "Fixing a prompt for one test case can easily introduce regressions to other test cases" [33]. This is the LLM equivalent of test fragility. Without a regression eval suite, every prompt change risks silent breakage.

## Sense A and Sense B together

For an individual developer or small team, both senses can apply within the same project. Coding the regular application code uses Sense A (TDD with the agent as code generator). Building any LLM-powered feature *inside* that application uses Sense B (eval-first development of the model-backed piece). The handoff point is where deterministic tests stop being meaningful — typically at the boundary where LLM output enters the system. Beyond that boundary, evals and rubric/judge-based grading take over [18, 33].

## Gaps and limitations

- **No published source defines the boundary condition cleanly.** Where exactly Sense A workflow ends and Sense B workflow begins inside a hybrid codebase is uncharted in the practitioner literature.
- **The "tests-as-prompts" reframe has not been empirically validated.** Tweag [47] articulates it; no controlled study compares natural-language-prompt-only vs test-as-prompt agent output quality.
- **The third sense — using TDD to build the agent's *test harness* — also exists but was outside this dimension's scope.** It surfaced in discovery findings but the practitioner literature is too thin to support an independent treatment.
