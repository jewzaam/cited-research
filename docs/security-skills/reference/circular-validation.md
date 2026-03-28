# Circular Validation Risk

Covers: The risks of AI writing both code and tests, creating self-confirming
feedback loops. See `../citations.md` for full source details.

---

## The Core Problem

When AI generates both implementation code and its tests, it creates a closed
feedback loop where the code serves as both subject and specification [6][7][23].

- "When AI analyzes implementation code to generate tests, it creates a closed
  feedback loop. These tests aren't validating that software meets business
  needs -- they're simply confirming the code does exactly what it was written
  to do, including any bugs or misinterpretations" [6]
- "When a human writes tests, they bring an understanding of intent: what the
  code *should* do, not just what it *does*. When AI writes tests from code
  alone, it has no independent source of truth" [7]

---

## The Self-Referential Validation Loop [23]

```
AI generates code --> AI reviews code --> humans approve output
```

Both steps rely on the same underlying model limitations. Errors may go
undetected because the reviewer shares the generator's blind spots [23].

A named risk pattern: "code can look right and pass the unit tests and still be
wrong" [23].

---

## Documented Cases

### Doodledapp Converter (February 2026) [7]

- AI tested Solidity converter against 17 real-world contracts
- All 17 tests passed on first run
- Tests never compared output against original input
- Roundtrip testing only proved idempotency, not correctness
- "If the converter silently drops a modifier, flattens an expression, or loses
  a data location, the first pass bakes that error into the 'normalized'
  output. The second pass converts the already-broken version and produces the
  same broken result" [7]
- Resolution: "The AI could not be both the test writer and the source of
  truth. The original contracts had to be the reference point" [7]

### Tautological Unit Test Postmortem [19]

- Production incident: well-covered endpoint returned silently incorrect data
- Generated tests "duplicated the implementation's assumptions rather than
  challenging them"
- The suite "looked comprehensive when it was actually blind to the real
  failure mode"

### Payments Service Postmortem [20]

- Rounding change in helper function went undetected
- All tests kept passing
- Model's mocking strategies hid state mutations

---

## Why Circular Validation Is Structurally Difficult to Detect

1. **Metrics reinforce false confidence:** Coverage rises, assertion counts
   grow, CI stays green [19]
2. **Surface plausibility:** Generated tests have "clear names, readable setup,
   and plausible fixtures" [19]
3. **Review cognitive bias:** "When you skim a test suite and see good coverage
   numbers and descriptive test names, it's natural to assume edge cases are
   handled" [19]
4. **Scale compounds risk:** With AI accounting for 42% of committed code [12],
   the volume of unverified circular validation grows

---

## Mitigations

### Structural Mitigations

| Mitigation | How It Breaks the Loop | Source |
|-----------|----------------------|--------|
| Derive tests from requirements, not code | Independent specification source | [6][7] |
| Mutation testing | Tests that survive mutations expose circular assumptions | [2][10] |
| Property-based testing | Tests invariants, not specific outputs | [11][17][18] |
| Separate generation and validation | AI writes, humans validate intent | [7][22] |
| Blackbox integration tests | No access to implementation details | [19] |

### Process Mitigations

- "Keep a 'human-in-the-loop.' No tool, no process, nothing can replace the
  critical judgment of an experienced developer" [23]
- "Label all AI-generated or AI-assisted code in PRs with tags like
  [AI-Generated]. This adds transparency and triggers a different review
  mindset" [23]
- Treat AI-written tests as "drafts rather than proofs" [19]
- Review checklist: "does a test validate behavior or implementation? Does it
  cover negative and edge cases? Can the assertion be satisfied by a wrong but
  convenient implementation?" [19]

---

## The Verification Debt Problem [12]

- 96% of developers don't fully trust AI-generated code
- Fewer than half review before committing
- 38% say reviewing AI code requires *more* effort than human code
- This creates "verification debt" -- a growing backlog of unverified code that
  looks correct

---

## Gaps and Limitations

- No controlled study quantifies the frequency of circular validation in
  production codebases
- The Doodledapp case [7] is a single smart contract domain example; broader
  domain coverage is lacking
- No research measures how often AI-generated tests would have caught a bug
  that human-written tests miss (reverse comparison)
