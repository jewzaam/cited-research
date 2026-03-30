# Internal Consistency Review
## Obsidian PA Integration Research

**Review Date:** 2026-03-30
**Reviewer:** Independent consistency verification agent
**Scope:** All markdown files in `/home/nmalik/source/cited-research/research/obsidian-pa-integration/`

---

## Summary Table

| Severity | Count | Category |
|---|---|---|
| CRITICAL | 0 | Contradictions, major numerical errors, missing required citations |
| MODERATE | 2 | Incomplete data extraction, arithmetic errors in metadata tables |
| MINOR | 1 | Missing license information for some plugins |
| VERIFIED | 47+ | Numerical consistency, citation accuracy, cross-references, formulas |

---

## Issues Found

### MODERATE-1: Source Accessibility Table Arithmetic Error

**File:** `obsidian-pa-integration.md`
**Line:** 178-183
**Issue Type:** Numerical inconsistency
**Status: RESOLVED** — Corrected to 13 search snippets, 1 dynamic page.

**Expected:**
```
| Status | Count |
|---|---|
| Fetched and verified | 22 |
| Referenced from search snippets (not fetched) | 13 |
| Dynamic page (content not extractable) | 1 |
| HTTP 403 | 1 |
```
Total: 22 + 13 + 1 + 1 = 37 ✓

**Actual:**
```
| Status | Count |
|---|---|
| Fetched and verified | 22 |
| Referenced from search snippets (not fetched) | 12 |
| Dynamic page (content not extractable) | 2 |
| HTTP 403 | 1 |
```
Total: 22 + 12 + 2 + 1 = 37 ✓ (arithmetic correct but components wrong)

**Analysis:**
Manual count of `citations.md` entries [23]-[37]:
- Citations with "Not fetched; data sourced from discovery agent search snippets": 13 ([23]-[27], [30]-[37])
- Citations with "Dynamic page; content not extractable": 1 ([28])
- Citations with "HTTP 403": 1 ([29])

The narrative text correctly identifies only [28] as a dynamic page that was not extractable. The table incorrectly shows "2" for dynamic pages and "12" for search snippets.

**Grade:** FAIL

---

### MODERATE-2: Plugin Count Citations Incomplete

**File:** `references/alternatives.md`
**Lines:** 23, 53
**Issue Type:** Citation accuracy / data extraction completeness
**Status: RESOLVED** — Updated citation [31] data extracted field to include plugin counts with note about search snippet sourcing.

**Claim:**
- "1500+ plugins" (Obsidian) - cited to [31]
- "150+ plugins" (Logseq) - cited to [31]

**Citation [31] Data Extracted Field:**
> "Obsidian local-first + Zettelkasten + AI plugins; Logseq open-source + block-based + querying; Notion cloud + collaboration."

**Analysis:**
The citation [31] data extracted field does not mention the specific plugin counts (1500+ and 150+). This creates one of three possible issues:
1. The data extraction in `citations.md` is incomplete (numbers were in the source but not recorded)
2. The citation in `alternatives.md` is incorrect (numbers came from a different source)
3. The numbers were inferred or estimated from discovery search snippets but not explicitly stated in [31]

Since [31] is marked "Not fetched; data sourced from discovery agent search snippets", the plugin counts may have been visible in search snippets but not included in the data extraction summary.

**Recommendation:** Either update the data extracted field in [31] to include the plugin counts, or verify the citation and add a note that these numbers are from search snippet context rather than the full article.

**Grade:** FAIL (citation trace incomplete)

---

### MINOR-1: Incomplete License Information in Plugin Table

**File:** `obsidian-pa-integration.md`
**Lines:** 144-151
**Issue Type:** Completeness
**Status: RESOLVED** — Added footnote to Required Plugins table explaining missing license data.

**Table "Required Plugins" shows:**
- `obsidian-local-rest-api`: MIT (✓)
- `obsidian-dataview`: — (missing)
- `Templater`: AGPLv3 (✓)
- `obsidian-periodic-notes`: — (missing)
- `obsidian-advanced-uri`: MIT (✓)
- `obsidian-git`: — (missing)

**Analysis:**
License information is provided for 3 out of 6 plugins. The citations.md file contains license data for some plugins but not others:
- [7] obsidian-dataview: no license mentioned
- [13] obsidian-periodic-notes: no license mentioned
- [17] obsidian-git: no license mentioned

**Explanation:** This is not an error per se—the research may not have extracted license information for these plugins. However, it creates an inconsistent table presentation where some rows show licenses and others show "—".

**Recommendation:** Either research and add the missing licenses, or add a footnote explaining that license information was not available in the sources reviewed.

**Grade:** PASS (with caveat: incomplete but not inconsistent)

---

## Items Verified as Consistent

### Numerical Consistency (23 verified)

1. ✓ **CLI command count:** "80+ commands" and "over 80 commands" used consistently across summary [line 7, 31], citations [line 8], alternatives [line 15, 29], obsidian-cli [line 11]
2. ✓ **Advanced URI stars:** "1.1k stars" consistent in summary [line 45, 150], citations [line 28], uri-scheme [line 80]
3. ✓ **Templater stars:** "4.7k stars" consistent in summary [line 73, 148], citations [line 53], templater-daily-notes [line 49]
4. ✓ **JSON Canvas stars:** "3.3k stars" consistent in citations [line 78], canvas [line 53]
5. ✓ **Node.js version:** "Node.js 22+" consistent in summary [line 37], citations [line 113]
6. ✓ **Notion rate limit:** "3 req/s" consistent in summary [line 119], citations [line 108], alternatives [line 17, 64]
7. ✓ **REST API port:** "127.0.0.1:27124" consistent across summary [line 51, 139], citations [line 33], local-rest-api [line 11, 65, 71]
8. ✓ **URI scheme actions:** "7 actions" consistent in summary [line 43], citations [line 23]
9. ✓ **Templater function modules:** "9 internal function modules" consistent in summary [line 73], citations [line 58]
10. ✓ **REST API endpoint groups:** "11 endpoint groups" consistent in summary [line 51], citations [line 33]
11. ✓ **Canvas node types:** "4 node types" consistent in summary [line 81], citations [line 73]
12. ✓ **Dataview query types:** "four query types" (LIST/TABLE/TASK/CALENDAR) consistent in summary [line 63], citations [line 48]
13. ✓ **Dataview query modes:** "4 query modes" (DQL/DataviewJS/inline/inline JS) correctly distinguished from query types in citations [line 38], dataview [line 52, 63]
14. ✓ **Obsidian version:** "v1.12.0" and "February 2026" consistent in summary [line 31, 189], obsidian-cli [line 11, 95]
15. ✓ **Total citations:** "37 citations" matches actual count in citations.md
16. ✓ **Notion size limits:** All consistent - "1000 blocks/request, 500KB payload, 2000 char rich text, 100 elements per array" in citations [line 108]
17. ✓ **Canvas color presets:** "1-6 (red, orange, yellow, green, cyan, purple)" consistent in summary [line 81], citations [line 73], canvas [line 49]
18. ✓ **Weekly note format:** "gggg-[W]ww" consistent in citations [line 68], templater-daily-notes [line 81]
19. ✓ **Monthly note format:** "YYYY-MM" consistent in citations [line 68], templater-daily-notes [line 82]
20. ✓ **Advanced URI version:** "v1.46.1" consistent in summary [line 45], citations [line 28], uri-scheme [line 80]
21. ✓ **Templater version:** "v2.18.1" consistent in summary [line 73], citations [line 53], templater-daily-notes [line 49]
22. ✓ **PyCanvas commit count:** "10 commits" consistent in citations [line 83], canvas [line 59, 94]
23. ✓ **Obsidian Sync version history:** "~1 year" in alternatives [line 76] (tilde correctly used as approximation marker)

### Citation Accuracy (24 spot-checked)

1. ✓ **[1]** CLI documentation - correctly cited for 80+ commands, requirements, setup
2. ✓ **[2]** CLI landing page - correctly cited for release date
3. ✓ **[4]** URI scheme - correctly cited for 7 actions, platform setup
4. ✓ **[5]** Advanced URI plugin - correctly cited for append/prepend modes
5. ✓ **[6]** REST API plugin - correctly cited for 11 endpoints, 127.0.0.1:27124, surgical edits
6. ✓ **[7]** Dataview - correctly cited for vault-as-database concept
7. ✓ **[8]** Dataview metadata - correctly cited for frontmatter and inline fields
8. ✓ **[9]** Dataview query types - correctly cited for LIST/TABLE/TASK/CALENDAR
9. ✓ **[10]** Templater - correctly cited for security warning, stars, license
10. ✓ **[11]** Templater intro - correctly cited for 9 function modules
11. ✓ **[12]** Templater settings - correctly cited for folder templates
12. ✓ **[13]** Periodic Notes - correctly cited for weekly/monthly formats
13. ✓ **[14]** JSON Canvas spec - correctly cited for node types, edges, colors
14. ✓ **[15]** JSON Canvas GitHub - correctly cited for MIT license, 3.3k stars
15. ✓ **[16]** PyCanvas - correctly cited for Python library
16. ✓ **[17]** Obsidian Git - correctly cited for mobile limitations
17. ✓ **[18]** Linux URI handler - correctly cited for .desktop file setup
18. ✓ **[19]** Auto-reload issue - correctly cited for no auto-reload behavior
19. ✓ **[20]** Steph Ango vault - correctly cited for CEO's vault structure
20. ✓ **[21]** Notion rate limits - correctly cited for 3 req/s
21. ✓ **[22]** Obsidian headless - correctly cited for Node.js 22+, npm install
22. ✓ **[28]** Sync troubleshoot - correctly marked as dynamic page with search snippet data
23. ✓ **[29]** Logseq CLI - correctly marked as HTTP 403 with search snippet data
24. ✓ **[31]** PKM comparison - correctly cited but data extraction incomplete (see MODERATE-2)

### Formula Validity and Derived Values

1. ✓ **Canvas layout example:** x-coordinates (0, 450, 900) with width 400 creates 50px gaps - geometrically valid
2. ✓ **Canvas example citation:** Correctly marked "Calculated from [14]" showing derivation
3. ✓ **Table arithmetic verification:** Integration Methods Matrix categories sum correctly
4. ✓ **Risk assessment:** Plugin risk levels (Low/Medium) are qualitative assessments, appropriately not given numerical citations

### Cross-Reference Links

1. ✓ **Summary to references:** All 10 reference file links use correct relative paths (`references/*.md`)
2. ✓ **References to citations:** All 10 reference files link back to citations with correct relative path (`../citations.md`)
3. ✓ **Summary to audit:** Links to `audit/citation-audit.md` and `audit/consistency-review.md` use correct paths
4. ✓ **Directory structure:** All links will resolve correctly given the actual file locations

### Terminology Consistency

1. ✓ **"Query types" vs "query modes":** Correctly distinguished in Dataview (types = LIST/TABLE/TASK/CALENDAR; modes = DQL/DataviewJS/inline/inline JS)
2. ✓ **"Binary files" vs "non-markdown":** Summary uses "binary files" [line 107], reference uses "Non-markdown (images, PDFs, Canvas)" [sync-conflicts line 40] - consistent (non-markdown files are binary in this context)
3. ✓ **"80+ commands" vs "over 80 commands":** Both forms used but semantically equivalent
4. ✓ **"PA" expansion:** Consistently defined as "personal assistant" in summary [line 5]

### Contradiction Check

1. ✓ **No contradictions found** between summary and reference files on:
   - Obsidian CLI requirements
   - Plugin capabilities
   - REST API endpoints
   - Sync conflict resolution strategies
   - Linux setup requirements
   - File format specifications

### Caveat and Limitation Honesty

1. ✓ **CLI newness flagged:** Summary correctly notes CLI is new (February 2026) and may have breaking changes [line 189]
2. ✓ **File watcher poorly documented:** Limitation correctly stated [line 190]
3. ✓ **REST API concurrent access:** Correctly flagged as "not documented" [line 191]
4. ✓ **Community plugin risk:** Correctly identified as "structural risk" [line 192]
5. ✓ **Dynamic page extraction:** Limitation transparently disclosed for [28] in both citations and summary
6. ✓ **HTTP 403 on npm:** Transparently disclosed for [29]
7. ✓ **Search snippet sourcing:** Citations [23]-[27], [30]-[37] all correctly marked as sourced from search snippets

### Source Transparency

1. ✓ **Tier assignments:** All 37 citations have tier ratings (2, 3, or 4)
2. ✓ **Access field consistency:** All 15 non-fetched sources have **Access:** field explaining status
3. ✓ **Data extracted completeness:** All citations include "Data extracted:" field (though some may be incomplete per MODERATE-2)

---

## Estimation and Interpolation Markers

**No unmarked estimates detected.** The only approximation marker found was the tilde (~) in "~1 year version history" for Obsidian Sync [alternatives line 76], which is correctly used.

The Canvas layout example includes "Calculated from [14]" which correctly marks it as derived rather than sourced.

---

## Methodology Assessment

The research correctly documents its own limitations:
- 37 total sources with transparency about access status
- 22 fetched and verified (correct count)
- Dynamic page and HTTP 403 errors transparently disclosed
- Search snippet sourcing explicitly noted for 13+ citations

The cited-research methodology is consistently applied with proper tier assignment and data extraction documentation.

---

## Recommendations

1. **REQUIRED:** Correct the Source Accessibility Table in `obsidian-pa-integration.md` line 178-183 to show 13 search snippets and 1 dynamic page (not 12 and 2).

2. **RECOMMENDED:** Update citation [31] data extracted field to include the plugin counts "1500+ for Obsidian, 150+ for Logseq" if those numbers were in the source, or add a note that they came from search snippet context.

3. **OPTIONAL:** Research and add license information for Dataview, Periodic Notes, and Git plugins to complete the Required Plugins table, or add a footnote explaining incomplete license data.

4. **OPTIONAL:** Consider adding a "Data completeness" indicator to the citation format when data extraction is known to be partial (e.g., for search snippet sources where only specific facts were extracted).

---

## Overall Assessment

**Grade: PASS with two moderate issues**

The research demonstrates strong internal consistency with 47+ verified items and only 3 issues identified. The issues found are:
- One arithmetic/counting error in a metadata table (easily corrected)
- One incomplete data extraction or incorrect citation (requires verification)
- One incomplete data collection (licenses) that doesn't affect core claims

The core technical claims, numerical data, citations, and cross-references are highly consistent. The research methodology is transparent about its limitations, and caveats are honestly stated.

**Confidence in findings:** High. The research is reliable for decision-making purposes with the noted caveats about dynamic page content and search snippet sourcing.
