# Internal Consistency Review — Visual TOM Research

**Review Date:** 2026-04-15  
**Reviewer:** Independent consistency auditor (no context from research conversation)  
**Scope:** All markdown files in `/home/nmalik/source/cited-research/research/visual-tom/`

## Executive Summary

This review checked numerical consistency, citation accuracy, formula validity, completeness, contradictions, estimation transparency, caveat honesty, and cross-reference validity across the Visual TOM research deliverable and its supporting reference files.

**Overall Grade: PASS with MINOR issues**

- 7 MINOR issues identified (primarily rounding inconsistencies and one missing estimation marker)
- 0 CRITICAL issues
- 0 MODERATE issues
- All citations spot-checked (50%+ coverage) traced correctly to citations.md
- No contradictions found between files
- Caveats and limitations clearly stated
- Cross-references validated

---

## Issue Summary

| Severity | Count | Description |
|---|---|---|
| CRITICAL | 0 | None found |
| MODERATE | 0 | None found |
| MINOR | 7 | Rounding inconsistencies, missing estimation marker |
| VERIFIED | 45+ | Items confirmed consistent |

---

## Issues Found

### ISSUE-001: Profit Margin Rounding Inconsistency

**Severity:** MINOR  
**Status:** OPEN

**Location:**
- visual-tom-analysis.md, line 235: "€4,246,840 (31.59% margin)"
- visual-tom-analysis.md, line 274: "31.6% profit margin"
- README.md, line 11: "31.6% net margin"
- company-market.md, line 29: "31.59%"

**Issue:** The profit margin is reported as both 31.59% and 31.6% across files. Both values calculate correctly from the source data (€4,246,840 / €13,442,236 = 0.31592 = 31.59%), but inconsistent rounding creates ambiguity.

**Expected:** Consistent rounding to either 31.59% (more precise) or 31.6% (rounded) across all files.

**Actual:** Mixed usage of both values.

**Recommendation:** Standardize on 31.6% throughout for readability, or consistently use 31.59% if precision is important.

---

### ISSUE-002: Revenue Value Rounding Inconsistency

**Severity:** MINOR  
**Status:** OPEN

**Location:**
- visual-tom-analysis.md, line 13: "€13.4M revenue"
- visual-tom-analysis.md, line 234: "€13,442,236"
- README.md, line 3: "€13.4M revenue"
- README.md, line 11: "€13.4M"
- company-market.md, line 26: "€13,442,236"

**Issue:** Revenue is presented as "€13.4M" in summary contexts and "€13,442,236" in detailed tables. Both are correct, but the rounded version (€13.4M) drops the 442K, which represents 3.3% of the total revenue.

**Expected:** Consistency in whether summaries use €13.4M or €13.44M.

**Actual:** Abbreviated to €13.4M in executive summaries, full precision in detailed tables.

**Assessment:** ACCEPTABLE — this is a reasonable summary/detail distinction, but borderline. €13.44M would be more accurate while maintaining readability.

---

### ISSUE-003: Net Profit Value Rounding Inconsistency

**Severity:** MINOR  
**Status:** OPEN

**Location:**
- visual-tom-analysis.md, line 13: "€4.2M net profit"
- visual-tom-analysis.md, line 235: "€4,246,840"
- README.md, line 11: (not listed in abbreviated form)
- company-market.md, line 27: "€4,246,840"

**Issue:** Net profit is presented as "€4.2M" in the executive summary but €4,246,840 in detailed sections. The abbreviation drops 246K (5.8% of the actual value).

**Expected:** Either €4.2M or €4.25M for consistency.

**Actual:** €4.2M in summaries, full value in tables.

**Assessment:** ACCEPTABLE with caveat — €4.25M would be more representative.

---

### ISSUE-004: Employee Count Presentation

**Severity:** MINOR  
**Status:** OPEN

**Location:**
- visual-tom-analysis.md, line 236: "20-49 (SME category)"
- README.md, line 12: "20-49"
- company-market.md, line 38: "20-49 (SME category)"

**Issue:** The deliverable consistently uses the "20-49" range from the French government registry [19], which is the most authoritative source. However, the reference file company-market.md (line 32) notes discrepancies with third-party estimates (54 from RocketReach, 20 from Datanyze) but does not provide a reconciliation.

**Expected:** Consistent use of 20-49 with acknowledgment of third-party variance.

**Actual:** Consistent use achieved. Third-party variance is noted in the reference file but not propagated to the main deliverable.

**Assessment:** PASS — the deliverable correctly prioritizes Tier 1 source. The discrepancy note in the reference file is appropriate context.

---

### ISSUE-005: Performance Capacity Discrepancy Flag

**Severity:** MINOR  
**Status:** OPEN

**Location:**
- visual-tom-analysis.md, line 179: "These marketing figures significantly exceed the documented safe limit (50,000/day) from the technical runbook [11]. The discrepancy may reflect different measurement methodologies or conditions, but no published reconciliation exists."
- product-overview.md, line 115: "⚠ These figures appear on the marketing page and may represent theoretical capacity under specific conditions rather than the conservative 'safe' limit of 50,000/day documented in the runbook [11]."

**Issue:** The discrepancy between marketing claims (780K-1.06M executions/day) and documented safe limits (50K/day) is flagged in both files. However, neither file provides a hypothesis about what might cause a 15-20x difference.

**Expected:** Either acceptance of the discrepancy as stated, or speculation on potential causes (e.g., "burst capacity vs sustained throughput", "different hardware configurations", "multi-server architecture").

**Actual:** Discrepancy noted without speculation.

**Assessment:** ACCEPTABLE — it is better to state the discrepancy without inventing explanations. The caveat is clear.

---

### ISSUE-006: TCO Savings Claim Range

**Severity:** MINOR  
**Status:** OPEN

**Location:**
- visual-tom-analysis.md, line 221: "30-50% TCO savings"
- pricing-licensing.md, line 48: "30% up to 50% savings"

**Issue:** The phrasing differs slightly ("30-50%" vs "30% up to 50%"), but both convey the same range.

**Expected:** Identical phrasing for consistency.

**Actual:** Semantically equivalent but syntactically different.

**Assessment:** PASS — no substantive inconsistency.

---

### ISSUE-007: Missing Estimation Marker on Specific Linux Distributions

**Severity:** MINOR  
**Status:** OPEN

**Location:**
- product-overview.md, line 129: "Specific minimum versions for Linux distributions (RHEL, SUSE, Ubuntu) are not enumerated in the runbook — only a kernel version minimum is given [11]"
- platform-integration.md, line 121: "Specific Linux distributions (RHEL, SUSE, Ubuntu, Debian) and their minimum supported versions are not enumerated — only kernel version ≥ 2.4.20 specified [11]"

**Issue:** Both files correctly note that specific Linux distribution versions are not documented. However, no estimation or interpolation is attempted (which is correct), but the gap is stated as a limitation rather than with an explicit "not documented" marker in the main deliverable.

**Expected:** The limitation is stated in reference files and acknowledged as a gap. No estimation should be made.

**Actual:** Correctly handled — no false precision introduced.

**Assessment:** PASS — proper handling of incomplete data.

---

## Citation Accuracy Check

**Sample:** 50%+ of citations in visual-tom-analysis.md were spot-checked against citations.md.

| Citation | Claim in Deliverable | Entry in citations.md | Status |
|---|---|---|---|
| [1] | Platform capabilities, 780K/1.06M executions, cloud support | Product overview, deployment options, performance specs | ✓ PASS |
| [2] | Three acquisition models, 20% maintenance | Perpetual/Subscription/SaaS, 20% annual maintenance | ✓ PASS |
| [3] | Founded 1990, Montrouge HQ | 30+ years, HQ address | ✓ PASS |
| [4] | Named customers across 11 sectors | Customer logos, AP-HP, SNCF, Sanofi, etc. | ✓ PASS |
| [5] | 650+ certified colleagues, 20+ service centers | Exactly matches | ✓ PASS |
| [8] | 30+ migrations, 1.5M+ jobs, 50K+ servers | Exactly matches | ✓ PASS |
| [9] | MFT protocols, storage types, French sovereignty | Protocols, cloud storage, French alternative | ✓ PASS |
| [10] | Hierarchical model, 10 resource types, SNL | Architectural details confirmed | ✓ PASS |
| [11] | OS support table, performance limits, 50K safe daily | OS table, 100K max jobs, 50K safe daily | ✓ PASS |
| [12] | Five module families, SSL/TLS, HA config | Module families, ports, HA, security | ✓ PASS |
| [13] | SAP versions v4.5-v6.40, four modules | Exactly matches | ✓ PASS |
| [14] | REST API v6.6.1a+, port 30002, token auth | Exactly matches | ✓ PASS |
| [16] | Gartner MQ 2024, Niche Player, 13 vendors | Exactly matches | ✓ PASS |
| [17] | EMA Radar 2025, 10 vendors, Dan Twing | Exactly matches | ✓ PASS |
| [18] | 2018 vulnerability, vtmanager/bdaemon, v5.7.4 | Buffer overflows, ports, no CVE | ✓ PASS |
| [19] | FY2024 revenue €13,442,236, profit €4,246,840, 20-49 employees | Exactly matches | ✓ PASS |
| [20] | 21 repositories, Apache-2.0, AbsyssLab | Exactly matches | ✓ PASS |
| [21] | ServiceNow connector, PowerShell 7.0+/Python 3.10+, v7.2.1f+ | Exactly matches | ✓ PASS |
| [25] | 4.9/5.0, NPS 94, 9 reviews | Exactly matches including small sample caveat | ✓ PASS |

**Result:** All spot-checked citations trace correctly to citations.md with accurate data extraction.

---

## Formula Validity Check

### Formula 1: Profit Margin Calculation

**Claim:** 31.59% profit margin (company-market.md, line 29)

**Calculation:**
- Net profit: €4,246,840
- Revenue: €13,442,236
- Margin = (4,246,840 / 13,442,236) × 100 = 31.592%

**Verification:** ✓ PASS — rounds to 31.59% or 31.6%

### Formula 2: Performance Discrepancy Ratio

**Claim:** Marketing figures (780K-1.06M) "significantly exceed" documented safe limit (50K)

**Calculation:**
- Lower marketing claim: 780,000 / 50,000 = 15.6x
- Upper marketing claim: 1,064,000 / 50,000 = 21.3x

**Verification:** ✓ PASS — "significantly exceed" is substantiated (15-21x difference)

---

## Completeness Check

All major factual claims in visual-tom-analysis.md were traced to reference files and citations:

| Claim | Reference File | Citation |
|---|---|---|
| Product identity, architecture | product-overview.md | [1][3][10][12] |
| OS support breadth | product-overview.md, platform-integration.md | [11] |
| Job scheduling capabilities | features-capabilities.md | [10] |
| MFT Gateway/Portal | features-capabilities.md | [9] |
| SAP integration | platform-integration.md | [13] |
| REST API details | features-capabilities.md, platform-integration.md | [14] |
| Pricing models | pricing-licensing.md | [2] |
| Gartner/EMA positioning | competitive-positioning.md | [16][17] |
| Financial data | company-market.md | [19] |
| Customer list | company-market.md | [4] |
| Partner ecosystem | company-market.md | [5][6][7] |
| Migration track record | competitive-positioning.md | [8] |
| Security features | security-compliance.md | [12] |
| 2018 vulnerabilities | security-compliance.md | [18] |

**Result:** ✓ PASS — all major claims trace to reference files and citations.

**Orphan Claims:** None identified. All substantive claims have citation backing.

---

## Contradiction Check

**Files cross-checked:**
- visual-tom-analysis.md vs. all reference files
- All reference files vs. each other
- README.md vs. visual-tom-analysis.md

**Contradictions found:** NONE

**Near-misses resolved:**
- Employee count: Deliverable prioritizes Tier 1 source (20-49) over third-party estimates (54, 20). Reference file notes discrepancy appropriately.
- Revenue: Tier 1 source (€13.4M) prioritized over third-party estimates ($8M, $5.4M). Discrepancy noted in company-market.md line 32.
- Performance capacity: Discrepancy between marketing (780K-1.06M) and documentation (50K safe daily) is explicitly flagged as unreconciled in both visual-tom-analysis.md and product-overview.md.

---

## Contradiction Transparency Check

### Source Disagreement 1: Revenue Estimates

**Files:** company-market.md, line 32-33

**Handling:** "Revenue figures vary by source: €13.4M from French government registry [19], $8M from RocketReach, $5.4M from Datanyze. The French government registry (Tier 1) is the most authoritative source."

**Assessment:** ✓ PASS — disagreement surfaced with rationale for selection.

### Source Disagreement 2: Employee Count

**Files:** company-market.md, line 36-42

**Handling:** Tier 1 source (20-49) vs. Tier 3 estimates (54, 20) shown in table with explicit note: "The official French classification (20-49 employees) from a Tier 1 source is the most reliable figure."

**Assessment:** ✓ PASS — disagreement surfaced with rationale for selection.

### Source Disagreement 3: Performance Capacity

**Files:** visual-tom-analysis.md line 179, product-overview.md line 115

**Handling:** Marketing claims (780K-1.06M) vs. documented safe limits (50K) explicitly flagged as unreconciled: "The discrepancy may reflect different measurement methodologies or conditions, but no published reconciliation exists."

**Assessment:** ✓ PASS — disagreement surfaced transparently without forcing a resolution.

---

## Estimation Markers Check

All derived or interpolated values were checked for proper marking.

| Value | Context | Marker | File | Status |
|---|---|---|---|---|
| 31.59% margin | Calculated from revenue/profit | (Calculated from [19]) | company-market.md | ✓ PASS |
| 15-20x capacity difference | Calculated from 780K-1.06M vs 50K | Ratio implied, not stated as est. | visual-tom-analysis.md | MINOR — could be explicit |
| "30+ migrations" | Direct from source | Not an estimate | competitive-positioning.md | ✓ PASS |
| "1.5M+ jobs" | Direct from source | Not an estimate | competitive-positioning.md | ✓ PASS |
| "650+ certified colleagues" | Direct from source | Not an estimate | company-market.md | ✓ PASS |

**Result:** PASS with one minor observation — the 15-21x performance discrepancy is a derived ratio but presented as implied rather than explicitly marked as calculated. This is acceptable because the underlying numbers are cited.

---

## Caveat Honesty Check

All files were reviewed for clear statement of limitations and gaps.

### visual-tom-analysis.md Section 10: "Key Considerations for Evaluation"

**Strengths:** 7 items listed with citations  
**Risks:** 7 items listed with citations and caveats  
**Information Gaps:** 5 items explicitly called out

**Assessment:** ✓ PASS — balanced presentation with clear acknowledgment of unknowns.

### Warning Markers (⚠) Throughout Files

| Warning | File | Line | Assessment |
|---|---|---|---|
| AI/LLM claims unsubstantiated | visual-tom-analysis.md | 124, 286 | ✓ Clear |
| Small review sample (9 reviews) | visual-tom-analysis.md | 289 | ✓ Clear |
| Performance discrepancy unreconciled | visual-tom-analysis.md, product-overview.md | 179, 115 | ✓ Clear |
| PDF unreadable | citations.md | 64, 66 | ✓ Clear |
| PARTIAL access (403 errors) | citations.md | 44, 48, 62 | ✓ Clear |
| No CVE assigned | security-compliance.md | 112 | ✓ Clear |
| Compliance certs not found | security-compliance.md | 136 | ✓ Clear with caveat |

**Assessment:** ✓ PASS — limitations stated clearly and honestly.

---

## Cross-Reference Link Check

Internal markdown links were validated against the actual directory structure.

| Link | Source File | Target | Status |
|---|---|---|---|
| `[citations.md](citations.md)` | visual-tom-analysis.md line 5 | ../citations.md (relative) | ✓ VALID |
| `[references/](references/)` | visual-tom-analysis.md line 5 | ../references/ (relative) | ✓ VALID |
| `[audit/](audit/)` | visual-tom-analysis.md line 7, 320 | ../audit/ (relative) | ✓ VALID |
| `[../citations.md](../citations.md)` | All reference files | ../../citations.md (relative) | ✓ VALID |
| `[references/product-overview.md](references/product-overview.md)` | README.md line 41 | Valid path | ✓ VALID |
| `[references/features-capabilities.md](references/features-capabilities.md)` | README.md line 42 | Valid path | ✓ VALID |
| `[references/platform-integration.md](references/platform-integration.md)` | README.md line 43 | Valid path | ✓ VALID |
| `[references/pricing-licensing.md](references/pricing-licensing.md)` | README.md line 44 | Valid path | ✓ VALID |
| `[references/competitive-positioning.md](references/competitive-positioning.md)` | README.md line 45 | Valid path | ✓ VALID |
| `[references/company-market.md](references/company-market.md)` | README.md line 46 | Valid path | ✓ VALID |
| `[references/security-compliance.md](references/security-compliance.md)` | README.md line 47 | Valid path | ✓ VALID |
| `[audit/citation-audit.md](audit/citation-audit.md)` | README.md line 48 | Valid path | ✓ VALID |
| `[audit/consistency-review.md](audit/consistency-review.md)` | README.md line 49 | Valid path | ✓ VALID |

**Result:** ✓ PASS — all internal links resolve correctly.

---

## Items Verified as Consistent

The following items were verified across multiple files and found to be numerically and factually consistent:

1. **Founded date:** February 26, 1990 — consistent across [3][19]
2. **Revenue FY2024:** €13,442,236 — consistent across deliverable and references
3. **Net profit FY2024:** €4,246,840 — consistent across deliverable and references
4. **Employee count:** 20-49 (Tier 1 source prioritized) — consistent
5. **Gartner MQ 2024:** Niche Player — consistent across [16] and all files
6. **EMA Radar 2025:** 10 vendors — consistent across [17] and all files
7. **Gartner Peer Insights:** 4.9/5.0, NPS 94, 9 reviews — consistent
8. **Migration track record:** 30+ migrations, 50K+ servers, 1.5M+ jobs — consistent across [8]
9. **Partner network:** 650+ certified colleagues, 20+ service centers — consistent across [5]
10. **SAP version support:** v4.5 through v6.40 — consistent across [13]
11. **REST API introduction:** v6.6.1a+ — consistent across [14]
12. **Performance limits:** 100K max jobs, 50K safe daily — consistent across [11]
13. **Default ports:** 30000, 30001, 30002, 30004 — consistent across [12][14][18]
14. **HA refresh interval:** 10 seconds — consistent across [12]
15. **Perpetual license maintenance:** 20% annual — consistent across [2]
16. **Licensing models:** Perpetual, Subscription, SaaS — consistent across [2]
17. **Editions:** Starter, Performance, Ultimate — consistent across [1][2]
18. **Pricing metrics:** Agents, Executions, Processes — consistent across [1][2]
19. **2018 vulnerability:** v5.7.4, vtmanager/bdaemon, no CVE — consistent across [18]
20. **MFT protocols:** FTP, SFTP, FTPS (PESIT/AS2 in dev) — consistent across [9]
21. **Cloud storage:** AWS S3, Azure Blob, GCS, Scaleway, Alibaba — consistent across [9]
22. **SAP modules:** R/3, BW, BO, DS — consistent across [13]
23. **OS families supported:** 12+ families including z/OS, IBM i, GCOS — consistent across [11]
24. **Hierarchical model:** Domain > Environment > Application > Job — consistent across [10]
25. **Resource types:** 10 types — consistent across [10]
26. **Submit unit modes:** 4 modes — consistent across [10]
27. **Hardware requirements:** 1.5 GHz/2 GB (Unix), 3 GHz/2 GB (Windows) — consistent across [11]
28. **Database:** PostgreSQL — consistent across [11]
29. **Java prerequisite:** ≥ 1.6 — consistent across [11]
30. **Server components:** VT-SES, VT-SDS, VT-SBU — consistent across [10][12]
31. **Agent components:** VT-CS, VT-CN — consistent across [10][12]
32. **GUI component:** VT-XVI — consistent across [10][12]
33. **Module families:** 5 families — consistent across [12]
34. **HA modes:** R (replication), S (auto-switch) — consistent across [12]
35. **Notification channels:** Email, SMS, WhatsApp, Teams, Slack — consistent across [1]
36. **OEM partners:** 4 (CGI, Atos, Accenture, Sopra Banking) — consistent across [6]
37. **Integrator partners:** 24 named — consistent across [5]
38. **Outsourcer partners:** 15 named — consistent across [7]
39. **Customer sectors:** 11 sectors — consistent across [4]
40. **GitHub repositories:** 21, Apache-2.0, AbsyssLab — consistent across [20]
41. **ServiceNow connector requirements:** v7.2.1f+, PowerShell 7.0+/Python 3.10+ — consistent across [21]
42. **TCO savings claim:** 30-50% — consistent across [8][26]
43. **Customer loyalty claim:** 97% for 12+ years — consistent across [1]
44. **Migration satisfaction:** 100% — consistent across [8]
45. **Visual IT Operations suite:** 3 products (TOM, BAM, IT Messenger) — consistent across [3]

---

## Recommendations

### Priority 1: Standardize Rounding

**Issue:** Profit margin reported as both 31.59% and 31.6%

**Action:** Choose one precision level and apply consistently:
- Option A: Use 31.6% throughout (more readable)
- Option B: Use 31.59% throughout (more precise)

**Affected files:** visual-tom-analysis.md, README.md

---

### Priority 2: Revenue Abbreviation Clarification

**Issue:** Revenue abbreviated from €13,442,236 to €13.4M (drops €442K, which is 3.3% of total)

**Action:** Consider using €13.44M in summaries to maintain accuracy while keeping readability.

**Affected files:** visual-tom-analysis.md, README.md

---

### Priority 3: Net Profit Abbreviation Clarification

**Issue:** Net profit abbreviated from €4,246,840 to €4.2M (drops €246K, which is 5.8% of total)

**Action:** Consider using €4.25M in summaries.

**Affected files:** visual-tom-analysis.md

---

## Final Assessment

**Overall Grade: PASS with MINOR issues**

The Visual TOM research deliverable and supporting files demonstrate strong internal consistency with only minor rounding inconsistencies. All citations trace correctly to citations.md, no contradictions were found between files, and limitations are stated clearly and honestly.

The 7 MINOR issues identified are primarily stylistic (rounding precision choices) rather than factual errors. The research methodology is sound, the multi-tier sourcing is applied correctly, and the deliverable accurately reflects the underlying reference data.

**Strengths:**
- Citation accuracy: 100% of spot-checked citations (50%+ coverage) traced correctly
- No contradictions between files
- Transparent handling of source disagreements with rationale
- Clear limitation statements with ⚠ markers
- All cross-references validate
- Formulas calculate correctly
- No orphan claims — all facts trace to citations

**Areas for improvement:**
- Standardize rounding precision across files (profit margin: 31.59% vs 31.6%)
- Consider more precise revenue/profit abbreviations (€13.44M vs €13.4M)

**Recommendation:** Address MINOR rounding inconsistencies for polish, but the deliverable is publication-ready in its current state.

---

**Review completed:** 2026-04-15  
**Files reviewed:** 10 markdown files (1 deliverable, 1 README, 1 citations, 7 references)  
**Citation coverage:** 50%+ spot-checked  
**Cross-references validated:** 100%
