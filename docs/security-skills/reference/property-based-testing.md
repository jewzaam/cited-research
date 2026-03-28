# Property-Based Testing as Complement to AI-Generated Tests

Covers: How Hypothesis (Python) and fast-check (JS/TS) address weaknesses in
AI-generated example-based tests. See `../citations.md` for full source details.

---

## Why Property-Based Testing Complements AI-Generated Tests

AI-generated tests share a structural weakness: they produce **specific
examples** drawn from patterns in training data [19]. Property-based testing
(PBT) addresses this by testing **invariants across automatically generated
input spaces** [17][18].

| AI Example-Based Tests | Property-Based Tests |
|----------------------|---------------------|
| Specific inputs and outputs | Randomized inputs |
| Derived from code patterns | Derived from invariants/properties |
| Happy path bias [19] | Biased toward edge cases [18] |
| Fixed assertions | Property verification |
| Tests what code does | Tests what code should guarantee |

"Property-based tests complement normal unit tests, but they don't replace
them -- firstly because in most situations you won't be able to define a
property that is sufficient to ensure that your code works" [17]

---

## Hypothesis (Python) [17]

### Key Features

- **@given decorator:** Core API for declaring strategies and running tests
  across hundreds of generated values including edge cases
- **Strategies:** Broad range of data generators -- booleans, integers, floats,
  text, lists, dicts, dates, plus composable custom strategies
- **Shrinking:** When a failure is found, Hypothesis reduces the failing input
  to the **simplest example** that still fails. "Bottom-up" shrinking -- if
  any component is replaced with a simpler example, the result becomes simpler.
  Described as "among the best in the world"
- **Stateful testing:** `RuleBasedStateMachine` generates sequences of
  operations and verifies invariants hold after each step
- **Example caching:** Failed examples are saved across runs -- once a bug is
  found, Hypothesis will not forget it
- **Pytest integration:** Works out of the box

### How It Addresses AI Test Weaknesses

| AI Test Weakness | Hypothesis Mitigation |
|-----------------|----------------------|
| Happy path bias | Generates edge cases automatically |
| Specific input fixation | Randomized input generation |
| Missing boundary values | Biased toward edge cases (0, empty, negative) |
| Tautological assertions | Properties test invariants, not specific values |
| No adversarial inputs | Shrinking finds minimal failing examples |

---

## fast-check (JavaScript/TypeScript) [18]

### Key Features

- **TypeScript-first:** Strong types throughout
- **Biased generation:** Small values (0, [], "", undefined) generated early;
  larger values later for coverage
- **Shrinking:** Via `map`/`chain` operations that preserve shrinkability
- **Determinism:** Seed-based reproducibility for all test runs
- **Model-based testing:** Test UI, APIs, or state machines
- **Race condition detection:** Shuffle promise/async resolution order
- **Preconditions:** `fc.pre(...)` for filtering invalid inputs inside
  predicates
- **`fc.gen()`:** Generate random values within existing test predicates
- **Test runner agnostic:** Works with any runner; dedicated integrations for
  Jest (`@fast-check/jest`) and Vitest (`@fast-check/vitest`)
- **Trusted by:** jest, jasmine, fp-ts, ramda, js-yaml, query-string

### How It Addresses AI Test Weaknesses

| AI Test Weakness | fast-check Mitigation |
|-----------------|----------------------|
| Deterministic inputs | Seed-based randomization |
| No concurrent testing | Race condition detection |
| Model/state blindness | Model-based testing |
| Single-path coverage | Broad input space exploration |

---

## AI Agents Writing Property-Based Tests [11]

Anthropic's research demonstrates the combination of AI and PBT:

- AI agent autonomously writes PBTs for existing code using Hypothesis
- Agent discovers properties by reading type annotations, docstrings, function
  names, and comments
- Evaluated across 100 popular Python packages
- Of 984 bug reports: 56% valid bugs, 32% worth reporting to maintainers
- Found bugs in NumPy, SciPy, Pandas
- "LLMs are particularly good at identifying properties that should be true
  about a given block of code from context" [11]

This suggests a practical workflow:
1. Let AI generate example-based tests for speed
2. Let AI generate PBTs for robustness
3. Use mutation testing to verify both
4. Human reviews all for intent alignment

---

## Practical Integration

### Python Stack

```
pytest + Hypothesis + mutmut (or cosmic-ray)
```

- Hypothesis generates diverse inputs including edge cases
- mutmut/cosmic-ray verifies the test suite's fault detection capability
- pytest orchestrates all tests

### JavaScript/TypeScript Stack

```
Jest/Vitest + fast-check + Stryker
```

- fast-check generates diverse inputs with race condition detection
- Stryker verifies mutation coverage
- Jest/Vitest runs all tests

---

## Gaps and Limitations

- PBT requires developers to **think about properties**, which is the hard part
  AI could help with [11] but humans must validate
- Coverage of PBT research specifically applied to AI-generated test suites is
  limited (only Anthropic study [11] directly addresses this)
- Property discovery is itself a challenge -- not all behaviors reduce to clean
  properties
- PBT execution time can be significant for complex strategies
