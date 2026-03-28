# Best Practices for Reviewing AI-Generated Tests

Covers: Practitioner guidance and frameworks for reviewing AI-generated test
code. See `../citations.md` for full source details.

---

## Core Principle

Treat AI-generated tests as **first drafts, not finished artifacts** [19][24].

"AI usually nails the syntax, but code that compiles doesn't mean the test
logic is sound or it tests anything useful" [24].

---

## Review Checklist

### Behavioral Validation

- [ ] Does the test validate **behavior** or **implementation**? [19]
- [ ] Can the assertion be satisfied by a wrong but convenient implementation?
      [19]
- [ ] Does the test compare against an **independent source of truth** (not the
      code under test)? [6][7]
- [ ] Does at least one test per feature operate as a **black-box** test without
      mocking primary inputs? [19]

### Assertion Quality

- [ ] Are assertions **meaningful**, not just `assertNotNull` or
      `assertTrue(true)`? [24]
- [ ] Do assertions check **specific values** that would change if the code
      were wrong? [19]
- [ ] Are there assertions for both **positive and negative** cases? [24]
- [ ] Would a mutation in the code under test cause at least one assertion to
      fail? (mentally apply mutation testing) [2][27]

### Edge Case Coverage

- [ ] Are **null/empty/zero** inputs tested? [24]
- [ ] Are **boundary conditions** covered (off-by-one, max values)? [13]
- [ ] Are **error paths** and exception cases tested? [24]
- [ ] Are **negative inputs** and invalid states tested? [19]

### Test Independence

- [ ] Does the test stand on its own, or does it merely **mimic** adjacent
      tests? [8]
- [ ] Are fixtures **independently constructed**, not derived from the
      implementation? [19]
- [ ] Are mocks used appropriately, or do they **hide state mutations**? [20]

### Technical Quality

- [ ] Does the test reference **real APIs** (not hallucinated)? [25]
- [ ] Are all **dependencies available** and correctly versioned? [25]
- [ ] Does the test **actually execute** the code path it claims to test? [24]
- [ ] Is the test **deterministic** (no flaky timing, no external
      dependencies)? [24]

---

## Process Recommendations

### Before Generating

1. Write **acceptance criteria** before asking AI to generate tests [6]
2. Provide **requirements context**, not just implementation code [7]
3. Specify **edge cases explicitly** in the prompt [19]
4. Ask for **property-based tests** alongside example-based tests [11][17]

### During Review

5. Run **mutation testing** on AI-generated test suites [2][27]
6. Check coverage reports for **uncovered branches**, not just line counts [4]
7. Verify tests **fail when they should** -- break the code intentionally and
   confirm the test catches it [14][15][16]
8. Look for **test smells**: Duplicated Asserts, Empty Tests [8]

### After Merging

9. Monitor **mutation scores** over time, not just coverage [4][27]
10. Track **production incidents** in code covered by AI-generated tests [19]
11. Re-evaluate when **requirements change** -- AI tests coupled to old
    implementation may pass but miss regressions [20]

---

## Organizational Standards

### Code Review Standards for AI-Generated Code [22][25]

- Require **requirement fulfillment** check: does the code/test implement
  acceptance criteria?
- Enforce **testable design**: dependencies should be injectable
- Mandate **comprehensive test suite**: unit, integration, and E2E
- Shift human review focus to **"why"** rather than syntax [25]

### Governance [12]

- 42% of committed code is AI-generated, expected to reach 65% by 2027
- "Trust but verify" policy: all AI code reviewed as if human-written, with
  extra scrutiny [22]
- Some teams require AI-suggested code to be accompanied by AI-generated tests,
  with human reviewer approving **both** [22]
- Label AI-generated code with tags like `[AI-Generated]` in PRs [23]

### Quality Gates

- Set minimum mutation score thresholds for AI-generated test suites [2]
- "Sonar way for AI Code" requires at least 80% coverage for new code, limits
  duplication to 3% [12]
- Run static analysis before manual review to catch basic errors [24]

---

## Anti-Patterns to Watch For

| Anti-Pattern | Why It's Dangerous | Detection |
|-------------|-------------------|-----------|
| Accepting green CI without review | Circular validation | Process audit |
| Counting test methods as quality metric | Quantity != quality | Mutation score |
| Reviewing only the diff, not the test logic | Surface-level review | Behavioral check |
| Trusting coverage numbers alone | 100% coverage / 4% mutation [27] | Mutation testing |
| Mocking everything | Hides real behavior | Mock audit |

---

## Gaps and Limitations

- No empirical study measures the effectiveness of these review practices at
  catching AI-specific test failures
- Checklist items are aggregated from practitioner blogs, not validated through
  controlled experiments
- The organizational overhead of thorough review may negate productivity gains
  from AI test generation [9][12]
