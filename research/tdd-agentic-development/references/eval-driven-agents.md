# D4: Eval-Driven Development for Building AI Agents

This dimension answers: *what does test-first / eval-first development look like when you are building the AI agent itself, not when an agent is writing code for you?* All numbered references point to entries in [`../citations.md`](../citations.md).

## The premise

When the system under test is a deterministic function of inputs, classical TDD applies. When the system is a non-deterministic LLM-based agent, classical TDD breaks down — assertions like `assert response == expected_string` are flaky even at temperature=0; outputs vary in form while remaining semantically equivalent. The replacement is **eval-driven development (EDD)**: define a structured eval set first, then iterate on the prompt, scaffold, model, or fine-tune until the agent passes evals at acceptable thresholds.

## Two definitions of EDD

There is no single canonical definition. Two converge with similar shape but different emphases.

### EDDOps (Xia et al., arXiv:2411.13768) [8]

The most formal academic treatment. The paper positions evaluation as "a continuous, governing function rather than a terminal checkpoint" and unifies offline (development-time) and online (runtime) evaluation in a closed feedback loop. Explicit contrast with TDD/BDD: "Unlike TDD and BDD, which are primarily applied in pre-deployment phases and assume relatively stable specifications and deterministic test outcomes, EDDOps must address the non-deterministic behavior and post-deployment evolution characteristic of LLM agents."

The paper's case study (Tax Assistant for Australia) demonstrates the loop: evaluation plans built from tax-regulation requirements → DeepEval test cases → systematic offline evaluation → iterative improvements driven by results.

### Anthropic's recommendation [18]

The official Anthropic engineering blog explicitly endorses EDD: "We recommend practicing eval-driven development: build evals to define planned capabilities before agents can fulfill them, then iterate until the agent performs well."

The 8-step roadmap [18]:

| Step | What |
|---|---|
| 0 | Start with 20-50 simple tasks from real failures, not hundreds |
| 1 | Convert manual checks and user-reported failures into test cases |
| 2 | Write unambiguous tasks with reference solutions two domain experts grade identically |
| 3 | Build balanced sets testing both when behaviors should and shouldn't occur |
| 4 | Create eval harnesses with stable, isolated environments starting from clean states |
| 5 | Design graders thoughtfully — favor deterministic checks; avoid overly rigid step sequences |
| 6 | Examine transcripts to verify graders work and failures are fair |
| 7 | Watch for eval saturation; introduce harder problems |
| 8 | Maintain dedicated teams owning eval suites as living artifacts |

### The community manifesto

evaldriven.org [24] distills the position to three components — dataset, grader, harness — and one axiom: "Build evals first. Code is generated. Evals are engineered."

## The metrics that matter

Anthropic's pass@k vs pass^k distinction [18] is the cleanest way to think about non-determinism:

- **pass@k** measures the likelihood that an agent gets at least one correct solution in k attempts. Higher k → higher score.
- **pass^k** measures the probability that all k trials succeed. Higher k → lower score.

Worked illustration: at k=1 they're identical. At k=10, pass@k approaches 100% while pass^k can fall to 0% [18]. Choose pass@k when you only need the agent to succeed at least sometimes (research, exploration); choose pass^k when consistency is the actual requirement (production user-facing agent).

## The grader taxonomy [18]

| Grader type | Methods | Strengths | Weaknesses |
|---|---|---|---|
| **Code-based** | String matching, binary tests, static analysis, outcome verification, tool-call verification, transcript analysis | Fast, low cost, objective, reproducible | Brittle to valid variations, limited nuance |
| **Model-based (LLM-as-judge)** | Rubric scoring, NL assertions, pairwise comparison, multi-judge consensus | Flexible, handles open-ended tasks | Non-deterministic, higher cost, requires calibration |
| **Human** | SME review, crowdsourced judgment, spot-checking, A/B testing | Gold-standard quality | Expensive, slow, expert-dependent |

Anthropic's "Swiss Cheese Model" framing [18]: "no single evaluation layer catches every issue. With multiple methods combined, failures that slip through one layer are caught by another."

## The practitioner counterpoint

Hamel Husain — among the most cited practitioners in this space — explicitly disagrees with the strong form of EDD. From the FAQ co-authored with Shreya Shankar [30]:

> "You can't anticipate what will break. A better approach is to start with error analysis. Write evaluators for errors you discover, not errors you imagine."

He calls naive EDD an approach that "creates more problems than it solves" because LLMs have "infinite surface area for potential failures." His recommended sequencing inverts the canonical EDD ordering:

1. Build the agent at minimum useful quality
2. Manually review 20-50 outputs after significant changes
3. Identify *real* failure patterns from traces
4. Build evals only for observed failures

Husain allows EDD as appropriate "for specific, well-defined constraints where you know exactly what success looks like" — guardrails like "never mention competitors," not behavioral correctness in general [30].

His original post "Your AI Product Needs Evals" [29] establishes the broader framing: a 3-level hierarchy of evals (Level 1 unit tests with quick assertions; Level 2 human and model evaluation; Level 3 A/B testing with real users) and the "whack-a-mole" pattern that emerges when teams skip evaluation infrastructure.

The disagreement matters but is not as deep as it sounds. Husain's "error analysis first" runs the same EDD loop, just delayed by one bootstrap iteration. Anthropic's [18] step 0 — "start with 20-50 simple tasks from *real failures*" — encodes the same insight: don't try to enumerate failures upfront.

## The tooling landscape

| Tool | Maintainer | Best for | Notable feature |
|---|---|---|---|
| **OpenAI Evals** | OpenAI | Benchmark-style eval registry | Completion Function Protocol for tool-using agents |
| **Anthropic Cookbook / building_evals** | Anthropic | Hands-on grader implementation | Code-level recipes for code/human/model graders |
| **Inspect AI** [25] | UK AI Safety Institute | Government-grade research evaluation | ReAct, Deep Agent, multi-agent composition; Docker/K8s/Modal sandboxing; 200+ pre-built evals (GAIA, SWE-Bench) |
| **LangSmith** | LangChain | Datasets + traces + multi-turn evals | UI baseline comparison; pytest + GitHub Actions CI integration |
| **Langfuse** | Langfuse | Open-source LangSmith alternative | Top-down funnel regression detection (macro → baseline → item-level) |
| **Promptfoo** [43] | Ian Webster / Promptfoo Inc. | CLI-first declarative YAML, CI-native | 3-tier capability model; `--repeat 3` for variance; trajectory:step-count assertion |
| **DeepEval** | Confident AI | pytest-native, 50+ metrics | `@observe` tracing, 3-layer agent evaluation (reasoning/action/execution) |
| **Braintrust** | Braintrust | Observability + evals + business metrics | Eval gates blocking releases; closed-loop production-trace → dataset updates |

## Trajectory evaluation is the defining 2024-2026 advance

The shift from output evaluation to *trajectory* evaluation — evaluating intermediate steps, tool calls, plan quality — is what separates 2024-2026 agent eval practice from earlier LLM eval practice. Multiple independent sources (Braintrust, Langfuse, DeepEval, OpenAI, Promptfoo [43]) converge on this without coordinating, suggesting genuine field consensus. The single-output-correctness frame inherited from MMLU/HumanEval is insufficient when an agent's mistake at message 50 in a multi-turn flow doesn't show up in the final response.

## Applied EDD: the Fireworks example [42]

Fireworks AI's August 2025 walkthrough is the cleanest practitioner application of EDD-with-Claude-Code: write evals defining desired behavior before writing the agent, then have Claude Code iterate against them. MCP integration carries eval results back to the agent loop. This is TDD-the-feel-of for a non-deterministic system.

## What eval-driven dev does NOT solve

The literature on eval limitations is substantial and recent.

- **Contamination is pervasive.** Microsoft MMLU-CF (ACL 2025) [63]: GPT-4o drops 14.6 pp (88.0% → 73.4%) on a contamination-free version of the same benchmark. SWE-bench effectively retired by OpenAI [52]; Berkeley RDI [17] showed a 10-line conftest.py achieves 100% without solving any task; OpenAI's audit found 59.4% of SWE-bench Verified problems had flawed tests. SWE-Rebench (decontaminated) showed one Chinese model fall from 35% to 18% [62].

- **LLM-as-judge is biased.** The CALM framework (ICLR 2025) [57] documents 12 distinct bias types in judge models. Fallacy-Oversight bias scores 0.566–0.832 across frontier models; position-swap causes >10% accuracy shifts; multilingual Fleiss' Kappa ≈ 0.3.

- **Benchmarks don't measure reliability.** Vendrow et al. [58] found that on more than half of popular benchmarks, any reported model error is more likely to be a benchmark label error than a model failure. Claude 3.5 Sonnet has a documented systematic rounding error on prime-adjacent values that benchmark accuracy masked entirely.

- **Agent evals miss structural failures.** The widely cited 1.9M-row database wipe (2024) [59] is the canonical case: the agent executed correct SQL, passed every behavioral test, and caused catastrophic damage because evals never tested environment-confusion scenarios. The MAST taxonomy (Berkeley) [60] catalogs 14 distinct multi-agent system failure modes that are undetectable at the individual-agent level.

- **The philosophical limit.** "You cannot test your way into trustworthiness when the system's behavior changes every time it runs" [61]. An eval gives you a probability distribution over one slice of input space at one point in time. It does not give you a specification.

## Synthesis

EDD is meaningful and worth doing for any non-trivial AI-backed feature, but the strong claim — *if your evals pass, your agent is good* — is empirically unsupported. The gap between eval performance and production behavior is documented and growing. Practical conclusion for individual devs and small teams: build evals continuously from observed failures (Husain's pattern [30]), use both deterministic and LLM-judge graders in a Swiss-cheese arrangement [18], measure trajectory not just output, and treat the eval suite as a living artifact whose primary job is to **detect regressions** rather than prove correctness.

## Gaps

- **No longitudinal study correlating eval suite scores with production outcome metrics.** This is the single biggest gap in the literature.
- **No source provides a sizing rule** (e.g., "use EDD when feature touches an LLM and has >X expected query volume; skip otherwise"). The line between "worth the harness investment" and "not worth it" is uncharted for small teams.
- **Eval contamination as it specifically applies to coding agents** is documented for benchmarks (SWE-bench [52]) but not for in-house eval sets. Whether internal evals leak into model training via inference logging or RLHF feedback loops is plausibly worrying but not empirically measured.
