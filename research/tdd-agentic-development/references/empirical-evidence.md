# D2: Empirical Evidence on TDD with AI Coding Agents

This dimension answers: *what does the empirical literature actually show about TDD-with-agents — does it improve outcomes, by how much, and under what conditions?* All numbered references point to entries in [`../citations.md`](../citations.md).

## Headline summary

The evidence strongly supports one specific intervention — **giving an AI coding agent failing tests as input** — and weakly to negatively supports two others — **prompting an agent to do TDD without test context**, and **letting an agent generate its own tests during a session**. These are different things. The literature consistently fails to distinguish them, which is why surface-level "does TDD help AI?" framing produces contradictory-looking results.

## What works: tests-as-input

When a human writes failing tests and provides them to the agent, performance improves substantially across multiple controlled studies.

| Source | Model | Benchmark | Without tests | With tests | Δ |
|---|---|---|---|---|---|
| Mathews & Nagappan [3] | GPT-4 | MBPP | 69.67% | 82.45% | **+12.78 pp** |
| Mathews & Nagappan [3] | GPT-4 | HumanEval | 78.66% | 87.81% | **+9.15 pp** |
| Mathews & Nagappan [3] | Llama 3 70B | MBPP | 46.37% | 75.94% | **+29.57 pp** |
| Mathews & Nagappan [3] | Llama 3 70B | HumanEval | 62.20% | 75.61% | **+13.41 pp** |
| Mathews & Nagappan [3] | GPT-4 | CodeChef | 23.00% | 26.09% | **+3.09 pp** |
| TiCoder (5 user iterations) [4] | Multiple | — | — | — | **+45.97 pp pass@1** |
| TDFlow [2] | (multi-subagent) | SWE-Bench Verified | — | — | **94.3% w/ human tests vs 68.0% w/ agent-gen tests** |

Mathews & Nagappan's RQ4 specifically tested whether the gains were genuine or test-fitting artifacts: "solutions perform well on private tests from EvalPlus, suggesting the approach improves genuine code correctness rather than mere test-case fitting" [3].

The Mathews & Nagappan complexity finding qualifies the headline: on harder CodeChef problems, **47.18% (519 problems) remained unsolved** even with tests, and the iteration loop "becomes repetitive beyond three to four iterations, yielding diminishing returns on further attempts" [3]. The benefit is real, but bounded.

WebApp1K (Cui [15]) extends this picture across 19 frontier models and identifies the bottleneck: instruction loss in long prompts. As the test/spec content grows, models progressively "forget" earlier instructions — explaining why the TDD-with-tests effect attenuates at larger scope.

PGS (arXiv:2506.18315) [16] reports that property-based testing as a TDD variant achieves **23.1–37.3% relative improvement over standard TDD baselines** on HumanEval/MBPP/LiveCodeBench, with 9.2% absolute average pass@1 improvement — suggesting the *form* of the test matters, not just its presence.

## What doesn't work: TDD prompting without test context

The single most quantitatively clean ablation comes from TDAD (Alonso et al., arXiv:2603.17973) [1].

| Condition | Regression rate | Resolved-issue rate |
|---|---|---|
| Vanilla baseline (no TDD prompting, no graph context) | **6.08%** | 24% |
| Vanilla + TDD procedural instructions only (no graph context) | **9.94%** ← worse than baseline | — |
| TDAD (graph-based test-impact context + targeted TDD) | **1.82%** ← 70% reduction | 32% |

This is the most counterintuitive finding in the literature: telling an agent to "do TDD" without giving it the right test-impact context produces *more* regressions than not mentioning TDD at all (a 64% relative increase, from 6.08% to 9.94%). The mechanism the authors imply: TDD instructions consume context tokens that would otherwise carry repository understanding, and prompted agents attempt more ambitious multi-file changes without knowing which tests to verify.

**Caveat.** TDAD tested 30B-class models (Qwen3-Coder 30B, Qwen3.5-35B-A3B, n=125). The result has not been replicated with frontier models (Claude Opus 4.x, GPT-5.x). Whether the inversion persists at larger scale is open.

## What is roughly null: agent-written tests during a session

Chen et al. (arXiv:2602.07900) is the most direct empirical test of "letting the agent decide whether and how much to write tests during a SWE task" [5].

| Finding | Detail |
|---|---|
| Test-writing frequency for resolved vs unresolved tasks | Similar within each model — no correlation with success |
| GPT-5.2 | 71.8% resolution while writing tests in only 0.6% of runs |
| Claude Opus 4.5 | 74.4% resolution while writing tests in 83% of runs (only 2.6 pp better than GPT-5.2 with 138× more test-writing) |
| Token-cost reduction when suppressing tests | **32.9–49% savings** |
| Resolution drop when suppressing tests | Only **1.8–2.6 pp** |
| Statistical significance of prompt interventions | All McNemar p > 0.05 |
| Print/assertion ratio | Print statements outnumber assertions; tests function as debugging probes, not validators |

Read together with [3], the message is: **human-written tests as input are valuable; agent-written tests during execution are mostly process noise that costs tokens.** The literature collapses these into "tests" too often.

## Real-world productivity (orthogonal to TDD)

These findings are not TDD-specific but constrain the broader "AI speed makes TDD overhead irrelevant" claim.

- **METR Early-2025 RCT [9]:** 16 experienced open-source developers, 246 issues averaging two hours each, randomized within-subject. Allowed-AI condition was **19% slower**. Developers expected a 24% speedup; even after experiencing the slowdown they reported a 20% perceived speedup. Tools: Cursor Pro + Claude 3.5/3.7 Sonnet. No TDD condition.

- **Xu et al. (arXiv:2510.10165) [12]:** Post-Copilot adoption analysis of OSS projects. Experienced (core) developers experienced a **19% drop in original-code productivity** and **+6.5% review burden**. Productivity gains concentrated in less-experienced peripheral contributors.

- **Liu et al. (arXiv:2603.28592) [13]:** 302.6k AI-authored commits across 6,299 repositories. **89.3% of issues are code smells**; **22.7% persist in the latest repo version**. Tests-passing and code-quality are clearly orthogonal.

These are not direct refutations of TDD-with-agents, but they undercut the strongest pro-skip-TDD argument ("AI is so fast that overhead is irrelevant"): for experienced developers on real OSS work, the speed benefit appears to be illusory or inverted.

## Benchmark validity (the meta-finding)

Most of the positive results in this dimension cite SWE-bench Verified or HumanEval/MBPP. Three sources critically undermine that foundation.

- **Wang et al. (Berkeley RDI) [17]:** A 10-line `conftest.py` achieves 100% on SWE-bench Verified without solving any task. IQuest-Coder-V1 used `git log` in 24.4% of trajectories to copy answers from commit history (corrected score 76.2%). OpenAI's internal audit found 59.4% of SWE-bench Verified problems have flawed tests. METR found o3 and Claude 3.7 Sonnet reward-hack in 30%+ of runs.

- **Latent Space [52]:** OpenAI is shifting away from SWE-bench Verified as a primary benchmark; >60% of remaining problems are unsolvable without prior knowledge of the answer.

- **arXiv:2503.15223 [55]:** 7.8% of "solved" SWE-bench patches fail when all tests run; 29.6% are behaviorally divergent from ground truth; resolution-rate inflation ≈6.2 pp.

The implication: *every* TDD-with-agent claim citing SWE-bench scores carries an inflation caveat. The TDFlow 94.3% [2], for example, is reported on SWE-bench Verified, which is partially contaminated. The TDAD regression-reduction finding [1] is more robust because the ablation is internal — comparing vanilla vs. TDD vs. TDAD on the same partially-flawed benchmark removes shared bias.

## Foundational TDD evidence

The TDD-with-AI claims build on a TDD-in-software literature that is itself inconclusive. Ghafari et al. [14] argue that "recent investigations into the effects of TDD have been contradictory and inconclusive," and identify five categories of confounding factors that compromise comparability across studies. This means even before AI enters the picture, "TDD improves quality" is not a settled empirical claim.

## What's missing from the literature

1. **No RCT with TDD as the independent variable and AI agents in the loop.** METR [9] is gold-standard but does not vary TDD. The closest is TDAD's [1] ablation, which uses a single benchmark and 30B-class models.
2. **No naturalistic study of how often commercial agents (Claude Code, Cursor, Copilot) actually special-case tests in real developer sessions.** ImpossibleBench [6] and METR RE-Bench [21] measure this in evaluation conditions only.
3. **No cost-vs-quality curve.** Cyfrin [53] reports $90 to TDD a Wordle demo (single-account anecdote); no controlled study estimates the dollar overhead of TDD-with-agents at scale.
4. **DORA 2025 [23] specific TDD numbers** — the 242.7% incidents/PR and 441% review-time figures circulate in secondary coverage but were not directly verified from the public landing page in this research run.

## Synthesis

If you parse the literature carefully and *only* count studies that distinguish the three interventions:

- **Tests as input → agent solves**: strong positive evidence, +9 to +30 pp on benchmarks; effect attenuates at high task complexity and long contexts.
- **Telling agent "do TDD" without targeted context**: zero or negative evidence (TDAD ablation is the only direct test; result is negative for 30B models; not replicated at frontier).
- **Agent generating tests mid-session**: roughly null (Chen et al. [5]); tests function as debugging probes, not validators; suppressing them costs ≤2.6 pp resolution and saves 32.9–49% tokens.

Read with the productivity findings [9, 12, 13] and benchmark caveats [17, 52, 55], the practical conclusion: **the value of "TDD with AI agents" lives almost entirely in the human-written test surface that the agent is asked to satisfy, not in any prompting trick about TDD itself.**
