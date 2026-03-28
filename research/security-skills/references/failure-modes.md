# Failure Modes of AI-Generated Tests

Covers: Known patterns where AI-generated tests fail to provide genuine
verification. See `../citations.md` for full source details.

---

## Taxonomy of Failure Modes

### 1. Tautological Assertions

Tests that assert what the code does rather than what it should do. The AI reads
the implementation and generates assertions that mirror its logic [5][6][7][19].

- The model "patterned tests after the code it saw, producing assertions that
  mirrored internal transformations" [19]
- "If your code has a bug that silently drops a modifier, the AI sees code that
  drops modifiers and writes a test confirming modifiers get dropped" [7]
- Even proper review may fail to detect these because the tests "look
  convincing: clear names, readable setup, and plausible fixtures" [19]

### 2. Testing Implementation, Not Behavior

Tests coupled to internal implementation details rather than external behavior
[5][6][19][20].

- Model defaults to "mocking strategies that hid state mutations. It stubbed
  internal helpers instead of exercising them, so tests could never catch a bug
  inside those helpers" [20]
- Generated tests assert on "specific return values constructed inside the test
  rather than the externally observable effects of the function" [19]

### 3. Missing Edge Cases and Boundary Conditions

AI-generated tests systematically undertest boundaries [8][13][24].

- "AI often tests the simple case. What about nulls, errors, edge conditions?
  AI might miss these unless you specifically tell it to check them" [24]
- Copilot "weak in terms of complex business logic and handling boundary
  conditions" [13]
- Model "refrains from proposing more intrusive test strategies like
  property-based tests or fuzzing unless prompted" [19]

### 4. Tests That Pass by Construction

Tests where the assertion is guaranteed to pass regardless of code behavior
[7][24][27].

- Roundtrip testing that "only proved idempotency: the converter produces
  consistent output. It never proved correctness: the converter produces the
  right output" [7]
- `assertTrue(true)` is "useless" [24]
- Some test suites achieve "100% coverage but only 4% mutation score" [27]

### 5. Happy Path Bias

Systematic preference for simple, positive test cases [8][13][19].

- The model "tends to replicate the most frequent, simplest patterns it sees
  in training data and prefers deterministic, single-case examples" [19]
- "It preferred simple equality assertions over property checks" [19]
- Without existing test suite context, 92.45% of Copilot-generated tests are
  "failing, broken, or empty" [8]

### 6. Mimicry Without Understanding

Passing tests that structurally copy existing tests without testing new behavior
[8].

- "Manual inspection of passing tests With-Context reveals that some passing
  tests appear to 'mimic' tests in their direct test context" [8]

### 7. Hallucinated APIs and Non-Existent Dependencies

Tests that reference APIs or packages that don't exist [25].

- "19.7% of packages suggested by AI coding assistants didn't actually exist"
  [25]

### 8. Weak or Missing Assertions

Tests that execute code but don't meaningfully check results [24].

- "A test without asserts is pointless -- AI often forgets to actually check
  the result" [24]
- "assertNotNull(result) is better than nothing, but doesn't prove the result
  is correct" [24]

---

## Root Causes

| Cause | Effect | Sources |
|-------|--------|---------|
| Pattern completion from training data | Canonical test structures without reasoning about invariants | [5][19] |
| No access to requirements/intent | Tests validate implementation, not specification | [6][7] |
| Preference for deterministic examples | Shallow inputs, simple assertions | [19] |
| Training on buggy public code | Reproduces flawed patterns | [21] |
| No adversarial thinking | Missing negative tests, error paths | [19][24] |

---

## Gaps and Limitations

- Most documented failure modes come from practitioner blog posts, not
  controlled studies. The taxonomy is observational rather than empirically
  validated at scale.
- Quantified rates of each failure mode across different LLMs are not available
  in the sources found.
- The relationship between prompt engineering quality and failure mode frequency
  is under-studied in the available literature.
