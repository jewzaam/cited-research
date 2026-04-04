# Consistency Review Report

Independent cross-file consistency check. Performed by a separate agent with
no context from the research conversation.

## Summary

- Total checks performed: 28
- PASS: 23
- FAIL: 3 → **Status: RESOLVED** (all 3 fixed post-review)
- WARNING: 2 (minor, accepted)

## Resolved Failures

### FAIL 1: Modified SHO code block in narrowband-broadband.md
**Files**: narrowband-broadband.md vs astrophotography-foss-guide.md, processing-workflows.md
**Issue**: Code block showed R=SII (classic SHO) but table and other files said R=Ha (modified SHO per Astrowheep [53])
**Status: RESOLVED** — Separated classic SHO and modified SHO into distinct code blocks with clear labels

### FAIL 2: SNR stacking examples differ
**Files**: astrophotography-foss-guide.md (4/16/100) vs calibration-stacking.md (4/9/100)
**Issue**: Different example frame counts used for √N demonstration
**Status: RESOLVED** — Guide aligned to 4/9/100 matching reference file

### FAIL 3: Audit files referenced but missing
**Files**: README.md, astrophotography-foss-guide.md → audit/citation-audit.md, audit/consistency-review.md
**Issue**: Files did not exist at time of review
**Status: RESOLVED** — Audit files created (this file)

## Accepted Warnings

### WARNING 1: Continuum subtraction notation
**Files**: citations.md uses `med()`, main files use `median()`
**Assessment**: Notation difference only, mathematically identical. Accepted.

### WARNING 2: Cloudy Nights data targets
**Files**: Guide omits M46/47 present in citations.md and public-data-sources.md
**Assessment**: Omission in summary table, not a contradiction. Full list in reference file. Accepted.

## Passed Checks (28 total)

All version numbers (Siril 1.4.2, GraXpert 3.0.2, StarNet CLI 2.0.0, DSS 6.1.0, PHD2 2.6.14, NINA 3.2, KStars 3.8.1) are consistent across all files.

All license types (GPL v3, BSD-3-Clause, BSD, MPL 2.0) are consistent.

All platform claims are consistent.

HOO formula (R=Ha, G=OIII, B=OIII) identical across 4 files.

Ha-enhanced RGB formula (max(Red, Q*Ha), Q=1.5) consistent.

All 6 YouTube video URLs identical across guide, youtube-tutorials.md, and citations.md.

Citation count (105) matches: README claims 105, citations.md has [1]–[105], tier totals sum to 105.

MAST JWST 4 processing stages identical across 3 files.

MOANA Project details (254mm, 0.591″/px, CC, Fort Davis) identical across 3 files.

Drizzle parameters (0.1–2.0, no debayer before drizzle) identical across 3 files.

Standard pipeline step order consistent across README, guide, and processing-workflows.md.

Dithering parameters (5–20 px, ~6 frame minimum) consistent.

Calibration frame recommended counts consistent (guide shows recommended range; reference adds minimums — supplemental, not contradictory).
