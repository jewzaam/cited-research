# Benchmarks and Evaluation Frameworks

Covers: Frameworks used to measure LLM test and code generation quality,
providing methodological context for other findings. See `../citations.md` for
full source details.

---

## EvalPlus Framework [1]

### Overview

EvalPlus is a code synthesis evaluation framework that rigorously benchmarks
the functional correctness of LLM-synthesized code by augmenting evaluation
datasets with automatically generated test cases.

- **Published:** NeurIPS 2023 (Main Conference Track), extended at COLM 2024
- **Authors:** Jiawei Liu, Chunqiu Steven Xia, Yuyao Wang, Lingming Zhang
- **Repository:** https://github.com/evalplus/evalplus
- **PyPI:** `pip install evalplus`

### Key Components

| Component | Description |
|-----------|-------------|
| HumanEval+ | HumanEval augmented by 80x test cases |
| HumanEval++-MINI | Distilled by 47x, similar effectiveness |
| MBPP+ | Analogous augmentation for MBPP benchmark |
| EvalPerf | Performance/efficiency evaluation |
| Leaderboard | Public ranking at evalplus.github.io |

### Test Generation Pipeline

1. **LLM-based seed generation:** ChatGPT proposes "interesting" or
   "corner-case" inputs, filtered via preconditions
2. **Type-aware mutation-based expansion:** Seeds mutated recursively in
   type-respecting fashion (flip booleans, add/remove list elements, perturb
   strings)
3. **Oracle-driven differential testing:** Solutions validated via agreement
   with reference outputs
4. **Test-suite reduction:** Greedy set-cover maintains 99% of coverage and
   bug-detecting power with ~16 tests/problem

### Impact on LLM Evaluation

- **pass@k reduction:** 19.3-28.9% across 26 LLMs
- **Ground-truth defects:** 18 defects (11%) in original HumanEval solutions
- **Ranking corrections:** Models mis-ranked on original HumanEval were
  correctly ranked on HumanEval+
- **Implication:** Prior code synthesis benchmarks undercount LLM failures due
  to insufficient tests -- the same problem that affects production AI tests

---

## Defects4J [4]

Referenced in Chen et al. (ASE 2020) for empirical evaluation of test adequacy
criteria. Contains real faults from Java projects.

- Used to demonstrate that mutation score is superior to statement coverage for
  predicting test effectiveness
- Baseline for comparing coverage-based, mutation-based, and random testing

---

## HumanEval and MBPP [1]

The original benchmarks that EvalPlus extends:

- **HumanEval:** 164 hand-crafted Python programming problems
  - Typically fewer than 10 tests per problem
  - Insufficient to detect non-trivial bugs
- **MBPP:** Mostly Basic Python Programming, 974 problems
  - Similar test insufficiency

Both benchmarks' limited test suites allow "non-trivial bugs to evade
detection, resulting in inflated pass@k scores" [1].

---

## Bug Taxonomy Benchmarks [21]

Gao et al.'s survey identifies bug patterns across:

- **CodeGen, PanGu-Coder, Codex** (related work): 333 bugs, 10 distinctive
  patterns: Misinterpretations, Syntax Error, Silly Mistake, Prompt-biased
  code, Missing Corner Case, Wrong Input Type, Hallucinated Object, Wrong
  Attribute, Incomplete Generation, Non-Prompted Consideration
- Key finding: "distributions of bug taxonomy are inconsistent between existing
  commonly used benchmarks and real-world projects"

---

## Why Benchmarks Matter for AI Test Trust

1. **Evaluation tools are only as good as their tests:** If the benchmark has
   weak tests, models that generate buggy code score well [1]
2. **The same dynamic applies to production:** AI-generated tests for
   production code have the same insufficiency risk as benchmark test suites
3. **EvalPlus demonstrates the solution:** Augmenting tests with mutation-based
   and LLM-generated inputs catches 19-29% more failures
4. **Meta-lesson:** The tools we use to evaluate AI code quality are themselves
   subject to the coverage-vs-effectiveness gap

---

## Gaps and Limitations

- EvalPlus focuses on Python; multi-language evaluation is less mature
- Benchmarks test algorithmic problems, not enterprise/business logic
- No benchmark specifically evaluates AI-generated *test* quality (they
  evaluate AI-generated *code* quality)
- The benchmark-to-production gap is acknowledged but not quantified
