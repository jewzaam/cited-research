# Documented Incidents Where AI-Generated Tests Masked Real Bugs

Covers: Specific cases where AI-generated test suites created false confidence,
allowing bugs to reach production or go undetected. See `../citations.md` for
full source details.

---

## Incident 1: Doodledapp Solidity Converter [7]

- **Date:** February 2026
- **Domain:** Smart contract (Solidity) code converter
- **What happened:** AI-powered testing loop validated converter against 17
  real-world contracts. All tests passed on first run. Tests never compared
  output against original input -- only confirmed the converter runs without
  errors.
- **Root cause:** Roundtrip testing proved idempotency, not correctness. If
  the converter silently drops a modifier, the first pass bakes that error into
  the "normalized" output. The second pass converts the already-broken version
  and produces the same broken result.
- **Quote:** "When you point an AI at your code and say 'write tests for this,'
  it reads the implementation and generates assertions that the implementation
  satisfies. If your code has a bug that silently drops a modifier, the AI sees
  code that drops modifiers and writes a test confirming modifiers get dropped."
- **Resolution:** Original contracts made the reference point. AI could not be
  both test writer and source of truth.
- **Discussion:** Hacker News (item 47060041)
- **Source quality:** First-party incident report from the affected team.

## Incident 2: Tautological Unit Test Production Incident [19]

- **Domain:** Medium-sized service with AI-scaffolded unit tests
- **What happened:** Test suite grew quickly with green CI. Production incident
  occurred when a well-covered endpoint returned silently incorrect data.
- **Root cause:** Generated tests duplicated implementation assumptions. The
  model patterned tests after the code, producing assertions that mirrored
  internal transformations, making the suite "blind to the real failure mode."
- **Key behavioral patterns:**
  - Model defaults to happy path
  - Adds straightforward mocks
  - Avoids edge cases
  - Prefers deterministic, shallow inputs
  - Uses simple equality assertions over property checks
- **Resolution:** Changed review checklist to treat generated tests as draft
  artifacts. Introduced property-based tests and blackbox integration tests.
- **Source quality:** Practitioner blog post (DEV Community). Author identity
  and specific project details are limited.

## Incident 3: Payments Service Regression [20]

- **Domain:** Small payments service with AI-generated unit and integration
  tests
- **What happened:** Suite looked green locally and in CI while missing several
  regressions that reached production. A rounding change in a helper function
  went undetected -- all tests kept passing.
- **Root cause:** Model defaulted to mocking strategies that hid state
  mutations. Stubbed internal helpers instead of exercising them, so tests
  could never catch bugs inside those helpers.
- **Resolution:** Not specified in the available source.
- **Source quality:** Practitioner blog post (DEV Community). Limited detail on
  resolution.

---

## Broader Industry Evidence

### CodeRabbit Report [9]

- "This year also brought several high-visibility incidents, postmortems, and
  anecdotal stories pointing to AI-written changes as a contributing factor --
  and these weren't fringe cases or misuses"
- AI-generated code "often omits null checks, early returns, guardrails, and
  comprehensive exception logic -- issues tightly tied to real-world outages"
- AI PRs have 1.7x more issues, 1.4x more critical issues

### Sonar Verification Gap [12]

- 42% of committed code is AI-generated
- 96% of developers don't fully trust it
- Fewer than half review before committing
- "Verification debt" -- a growing backlog of unverified code
- 88% cite negative impacts on technical debt

### AI Code Issue Rate Increase

- Pull requests per author increased 20% year-over-year with AI [9]
- Incidents per pull request increased 23.5% [9]
- This suggests AI accelerates both output and incident rate

---

## Pattern Analysis

All three documented incidents share structural similarities:

| Pattern | Incident 1 | Incident 2 | Incident 3 |
|---------|-----------|-----------|-----------|
| Tests passed initially | Yes | Yes | Yes |
| CI was green | Yes | Yes | Yes |
| Coverage appeared adequate | Yes | Yes | Yes |
| Bug involved subtle logic | Yes (dropped modifiers) | Yes (incorrect data) | Yes (rounding) |
| Tests mirrored implementation | Yes | Yes | Yes (via mocking) |
| Missing independent oracle | Yes | Yes | Yes |
| Detected by production failure | Yes (implied) | Yes | Yes |

---

## Gaps and Limitations

- All three incidents are from practitioner blog posts, not formal incident
  reports with root cause analysis
- No incidents from large enterprises are publicly documented (though
  CodeRabbit [9] references "high-visibility incidents" without specifics)
- Selection bias: incidents where AI tests *did* catch bugs are less likely to
  be written about
- The DEV Community posts [19][20] have limited author/project detail, making
  independent verification difficult
- No quantified estimate of how often this pattern occurs across the industry
