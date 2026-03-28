# Mutation Testing Tools

Covers: Capabilities and features of mutation testing tools that reveal weak
tests. See `../citations.md` for full source details.

---

## Overview

Mutation testing evaluates test suite quality by introducing small, targeted
changes (mutants) into source code and checking whether existing tests detect
them. If tests pass on mutated code, they are not adequately testing the affected
behavior [14][15][16][27].

Common mutation types: operator replacement (`+` to `-`), comparison changes
(`>` to `>=`), statement deletion, constant modification, boolean negation,
return value changes.

---

## Tool Comparison

| Feature | Stryker (JS/TS) [14] | mutmut (Python) [15] | Cosmic Ray (Python) [16] |
|---------|---------------------|---------------------|-------------------------|
| Language | JavaScript, TypeScript | Python 3 | Python 3 |
| Mutation approach | AST-based | AST-based | AST-based |
| Incremental mode | Yes | Yes (remembers prior work) | No (but distributed) |
| Distributed execution | No | No | Yes (HTTP-based workers) |
| Type checker integration | Yes (TypeScript checker) | Yes (mypy, pyrefly) | No |
| Test runner support | Jest, Vitest, Mocha | pytest | Configurable |
| Coverage integration | Built-in | Optional (coverage.py) | N/A |
| CI/Dashboard | Stryker Dashboard | No | No |
| Platform | Cross-platform | Linux/macOS/WSL (requires fork) | Cross-platform |
| Maintenance status | Active | Most actively maintained Python tool | Active (v8.4.4) |

---

## Stryker (JavaScript/TypeScript) [14]

- Supports JS, TS, React, Angular, Vue, Svelte, Node
- TypeScript checker plugin marks invalid mutants as `CompileError`, avoiding
  wasted time on type-error mutants
- Incremental mode tests only changed code since last run
- Identifies redundant and ineffective tests
- 2,722 GitHub stars
- Also available for .NET (Stryker.NET) and Scala
- By 2026, Stryker.NET uses ML to prune equivalent mutants, "reducing noise
  by 30%" (from search summary, primary source unverified)

## mutmut (Python) [15]

- Developed by Anders Hovmoller
- Focus on ease of use
- Remembers prior work for incremental testing
- Knows which tests to execute per mutant (speeds up runs)
- `mutmut browse` for interactive result exploration
- `mutmut apply <mutant>` writes mutant to disk for investigation
- Integrates with mypy/pyrefly to filter type-invalid mutants
- Supports coverage.py for line-level mutation targeting
- Pattern matching for selective mutation: `mutmut run "module.function*"`
- Requires fork() -- Linux/macOS/WSL only

## Cosmic Ray (Python) [16]

- Developed by Sixty North (Austin Bingham)
- AST manipulation via Python's built-in `ast` module
- HTTP-based distributed execution:
  - `cr-http-workers` clones git repo per worker
  - Each worker has isolated code copy
  - Linear scaling with worker count
  - Custom distributor plugins supported
- Docker-based distribution also supported
- Limitation: Python's AST library doesn't preserve formatting, making it
  impossible to dump AST back and get original file

---

## How Mutation Testing Exposes AI-Generated Test Weaknesses

The critical insight: **a test suite can achieve 100% code coverage but only 4%
mutation score** [27]. This directly exposes the weakness of AI-generated tests
that optimize for coverage metrics.

Mutation testing reveals:
- **Tautological assertions:** Mutant survives because the assertion doesn't
  actually test the mutated behavior
- **Missing edge cases:** Mutants in boundary conditions survive because no test
  exercises them
- **Weak assertions:** `assertNotNull` passes even when the value is wrong
- **Implementation coupling:** Tests break on refactoring but pass on logic
  errors

MuTAP [2] and Meta ACH [10] demonstrate that feeding mutation results back into
LLM test generation significantly improves test quality (93.57% mutation score
for MuTAP vs baseline LLM generation).

---

## Practical Considerations

- **Computational cost:** Mutation testing is expensive. Each mutant requires a
  full test suite run. Mitigations: incremental mode (Stryker, mutmut),
  distributed execution (Cosmic Ray), selective mutation by module/function.
- **Equivalent mutants:** Some mutations produce semantically identical code.
  These inflate the denominator and deflate mutation scores. Stryker.NET uses
  ML to prune these; mutmut uses type checkers.
- **Integration into CI:** Best applied to critical modules and high-value code
  rather than entire codebases [15].

---

## Gaps and Limitations

- No published study directly compares mutation scores of AI-generated vs
  human-written test suites using the same mutation tool on the same codebase
  (though MuTAP [2] compares against Pynguin)
- Equivalent mutant detection remains an unsolved problem across all tools
- Performance data for large codebases (>100K LOC) is sparse in the available
  sources
