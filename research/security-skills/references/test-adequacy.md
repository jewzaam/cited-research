# Test Adequacy Research

Covers: The relationship between coverage metrics and actual defect detection.
See `../citations.md` for full source details.

---

## The Coverage-Effectiveness Gap

### Key Finding: Coverage Is Not Strongly Correlated with Effectiveness [3]

Inozemtseva and Holmes (ICSE 2014, SIGSOFT Distinguished Paper Award):

- **Low to moderate correlation** between coverage and effectiveness when
  controlling for test suite size
- Stronger coverage criteria (branch, MC/DC) do **not** provide greater insight
  into suite effectiveness than weaker criteria (statement)
- **Moderate to very high correlation** between effectiveness and number of test
  methods (i.e., test suite size matters more than coverage percentage)
- Study used 5 large open-source Java projects (~100K LOC, 1000+ test methods)

### Statement Coverage Alone Is Weak [4]

Chen et al. (ASE 2020):

- Statement coverage alone detects only **10% of faults**
- Combining multiple control-flow criteria: **28%** vs **19%** for strongest
  single criterion
- Basic def/use pair coverage detects **79% of faults missed** by control-flow
  coverage
- Mutation score is **superior** to statement coverage for predicting test
  effectiveness after removing confounding effects

### The 100% Coverage / 4% Mutation Score Problem [27]

Codecov blog demonstrates a case where:

- Test suite achieves **100% code coverage**
- Mutation score is only **4%**
- This directly illustrates that high coverage can coexist with almost no fault
  detection capability

---

## Three Approaches to Test Adequacy [4]

| Approach | Focus | Example Criterion |
|----------|-------|-------------------|
| Structural | Coverage of program elements | Statement, branch, MC/DC |
| Fault-based | Fault detecting ability | Mutation score |
| Error-based | Error-prone points | Based on common fault patterns |

---

## Why This Matters for AI-Generated Tests

AI-generated tests tend to optimize for the most visible metric: code coverage.
This creates a dangerous alignment:

1. AI generates tests that increase line/branch coverage [13]
2. Teams see coverage numbers rise and gain confidence [19]
3. But coverage is weakly correlated with fault detection [3]
4. Mutation testing reveals the true gap [2][27]

The Sonar survey [12] found that 53% of developers report AI generates "code
that looks correct but isn't reliable" -- this extends directly to test code.

---

## Recommended Adequacy Criteria Hierarchy

Based on the research:

1. **Mutation score** — strongest predictor of fault detection [2][4]
2. **Test suite size** — moderate to high correlation with effectiveness [3]
3. **Number of meaningful assertions** — correlated with effectiveness (Zhang &
   Mesbah, FSE 2015, cited alongside [3])
4. **Branch/MC/DC coverage** — moderate correlation, diminishing returns [3]
5. **Statement coverage** — weakest predictor [4]

---

## Gaps and Limitations

- The Inozemtseva & Holmes study [3] uses Java projects -- generalizability to
  other languages is assumed but not proven
- No study directly measures coverage-to-fault-detection correlation
  specifically for AI-generated test suites
- Operational coverage (accounting for usage profiles) is a promising but
  under-studied alternative
- The 100%/4% example [27] is from a blog post, not a controlled study
