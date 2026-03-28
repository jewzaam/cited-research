# AI-Generated vs Human-Written Test Effectiveness

Covers: Studies comparing bug-finding rates between AI-generated and
human-written tests. See `../citations.md` for full source details.

---

## Direct Comparison Data

### Bug Detection Rates [13]

| Metric | AI-Generated | Human-Written | Ratio |
|--------|-------------|---------------|-------|
| Bug detection rate | ~80% | ~90% | 0.89x |
| Code coverage | 75% | 60% | 1.25x |
| First-pass accuracy | 85% | 95% | 0.89x |
| Time to write | 60% of human time | Baseline | 0.60x |

**Caveat:** These figures from the JUnit/Mockito study [13] appeared in search
summaries. The exact methodology and confidence intervals could not be verified
via direct page visit.

### Test Usability [8]

| Context | AI Passing Rate |
|---------|----------------|
| With existing test suite | 45.28% |
| Without existing test suite | 7.55% |

Human-written tests (the baseline in the study) had near-100% passing rates by
design, since they were already part of the project test suite [8].

### Code Quality Issues [9]

| Metric | AI-Generated PRs | Human PRs | Ratio |
|--------|------------------|-----------|-------|
| Total issues per PR | 10.83 | 6.45 | 1.68x |
| Critical issues | 1.4x more | Baseline | 1.4x |
| Logic/correctness errors | 1.75x more | Baseline | 1.75x |
| Security findings | 1.57x more | Baseline | 1.57x |
| XSS vulnerabilities | 2.74x more | Baseline | 2.74x |
| Excessive I/O | ~8x more | Baseline | ~8x |
| Spelling errors | Baseline | 1.76x more | 0.57x |
| Testability issues | Baseline | 1.32x more | 0.76x |

Study covered 470 GitHub PRs (320 AI-co-authored, 150 human-only) [9].

---

## Where AI Tests Excel

1. **Speed:** 40% less time to generate tests [13]
2. **Coverage breadth:** 75% vs 60% code coverage [13]
3. **Spelling/naming:** Fewer spelling errors in AI code [9]
4. **Testability:** AI code has fewer testability issues [9]
5. **Boilerplate:** AI excels at generating standard test structures

## Where AI Tests Fall Short

1. **Bug detection:** ~80% vs ~90% for humans [13]
2. **Complex logic:** Weak on complex business logic [13]
3. **Edge cases:** Systematically misses boundary conditions [8][13][19]
4. **First-pass correctness:** 85% vs 95% [13]
5. **Usability without context:** 92.45% failing/broken/empty without existing
   test suite [8]
6. **Security:** 1.57-2.74x more security vulnerabilities [9]
7. **Logic correctness:** 1.75x more logic errors [9]

---

## The Productivity Paradox

The CodeRabbit report [9] frames the core tension: "If AI code is 1.7 times
more likely to have bugs, and those bugs require human time to find and fix, the
productivity gain depends entirely on whether the time saved writing the code
exceeds the time spent reviewing and debugging it."

Pull requests per author increased 20% year-over-year with AI, but incidents
per pull request increased 23.5% [9].

---

## Gaps and Limitations

- The direct bug detection comparison (80% vs 90%) comes from a single study
  [13] and could not be independently verified
- CodeRabbit data [9] covers open-source PRs only -- enterprise patterns may
  differ
- No study measures long-term maintenance burden of AI-generated vs
  human-written tests
- Head-to-head studies on the same codebase with the same developers are rare
