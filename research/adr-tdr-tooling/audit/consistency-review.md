# Consistency Review Report: ADR/TDR Tooling Research

## Review Metadata

- **Date:** 2026-07-07
- **Deliverable:** /home/nmalik/source/cited-research/research/adr-tdr-tooling
- **Reviewer Context:** No access to original research conversation

## Summary

| Severity | Count |
|----------|-------|
| CRITICAL | 0 |
| MODERATE | 0 |
| MINOR | 2 (both RESOLVED) |

## Issues Found

### MINOR-1: Simplicity table ordering

**File:** analysis.md (Simplicity Analysis table)
**Status: RESOLVED**
**Issue:** adr-tool (~2 min setup) was ranked 5th below ADG (~3 min) at rank 4. Ordering should reflect setup time.
**Resolution:** Swapped ranks 4 and 5.

### MINOR-2: adr.zone tier classification

**File:** analysis.md (Tier 3: No Programmatic Access)
**Status: RESOLVED**
**Issue:** adr.zone listed under "No Programmatic Access" but described as having an API, which contradicts the tier label.
**Resolution:** Moved adr.zone out of the tier 3 table with a note about its intermediate position.

## Items Verified as Consistent

### Numerical Consistency

| Claim | README | analysis.md | Reference Files | citations.md | Verdict |
|-------|--------|-------------|-----------------|--------------|---------|
| Source count | 50 | "Fifty" | — | 50 entries ([1]-[50]) | PASS |
| Tool count | 36 | 36 | 36 (tool-landscape) | [1] "36 distinct" | PASS |
| Format families | 5 | — | 5 (format-ecosystem) | — | PASS |
| Active tools | — | 8 | 8 (tool-landscape) | — | PASS |
| adrs stars | — | 95 | 95 | [11] "95 stars" | PASS |
| adr-tools stars | — | ~5,600 | ~5,600 | [9] "~5,600" | PASS |
| ADG stars | — | — | 35 | [10] "35 stars" | PASS |
| Structured MADR stars | — | — | 9 | [12] "9 stars" | PASS |
| Cliff's Delta | — | 0.6364 | 0.6364 | [6] "0.6364" | PASS |
| p-value | — | 0.002 | 0.002 | [6] "p=0.002" | PASS |
| W statistic | — | 84.0 | 84.0 | [6] "W=84.0" | PASS |
| Study n | — | 33 | 33 | [6] "n=33" | PASS |
| Haiku accuracy drop | 63.5pp | 86.99%→23.44% | 86.99%→23.44% | [18] exact | PASS |
| Frontmatter fields | 10 required | 10 fields | 10 required | [3] "10 required" | PASS |

### Citation Accuracy (spot-check 25/50)

All checked citation numbers ([1]-[18], [22], [25], [29], [32], [39], [40], [44]) point to correct entries in citations.md. PASS.

### Cross-Reference Links

| Link | Source File | Target | Exists | Verdict |
|------|-----------|--------|--------|---------|
| `[analysis.md](analysis.md)` | README.md | analysis.md | Yes | PASS |
| `[citations.md](citations.md)` | README.md | citations.md | Yes | PASS |
| `[references/](references/)` | README.md | references/ | Yes | PASS |
| `[audit/](audit/)` | README.md | audit/ | Yes | PASS |
| `[citations](citations.md)` | analysis.md | citations.md | Yes | PASS |
| `[references/](references/)` | analysis.md | references/ | Yes | PASS |
| `[citations](../citations.md)` | all ref files | ../citations.md | Yes | PASS |

### Table Consistency

Format comparison matrix in format-ecosystem.md matches the source data from [4]. Agentic readiness tier tables in analysis.md match agentic-readiness.md. Tool landscape tables match across files. PASS.

### Contradiction Check

No conflicting facts found between files. Counter-perspectives are surfaced with citations to both sides (format restrictions [18] vs metadata benefits [5], simplicity [32] vs scale needs [25]). PASS.

### Caveat Honesty

Gaps and limitations sections present in all 5 reference files and analysis.md. Key caveats surfaced: no empirical validation of Structured MADR AI claims, MCP ecosystem nascent (2 tools), Agent Decision Records adoption unknown. PASS.

## Conclusion

No critical or moderate issues. Two minor ordering/classification issues found and resolved. Cross-file numerical consistency, citation accuracy, and link integrity all verified.
