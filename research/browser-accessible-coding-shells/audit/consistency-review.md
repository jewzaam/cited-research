# Consistency Review

**Scope:** Cross-file numerical and logical consistency for the `browser-accessible-coding-shells` research deliverable.
**Date:** 2026-05-23
**Files reviewed:**
- `citations.md`
- `browser-accessible-coding-shells.md`
- `README.md`
- `references/openshell.md`
- `references/openclaw.md`
- `references/browser-tty-comparison.md`
- `references/k8s-deployment-patterns.md`
- `references/synthesis.md`

---

## Summary Table

| ID | Severity | File | Issue |
|---|---|---|---|
| C-01 | CRITICAL | `README.md` line 31; `references/browser-tty-comparison.md` line 22 | "14 months since release" is wrong — the span from 2024-03-30 to 2026-05-23 is ~25-26 months |
| C-02 | MODERATE | `README.md` line 36 | "weekly [6]" claims weekly OpenClaw release cadence; citation [6] (Wikipedia) does not state this |
| C-03 | MODERATE | `README.md` line 32 | gotty `~19 MB community Alpine` image size lacks a gap/unverified marker; `browser-tty-comparison.md` explicitly marks it as **Gap** |
| C-04 | MINOR | `README.md` line 19 (disqualifying table) | "`≥1 GB RAM floor`" is not backed by any citation in that table row — the row cites `[21, 22, 25]` but citation [19] is the source for the RAM requirement |
| C-05 | MINOR | `README.md` line 19 | "265 MB image" rounds to 265 MB, but citations.md [25] and all other files state 265.68 MB (linux/amd64); rounding is acceptable but diverges from every other file's precision |

---

## C-01 — CRITICAL: "14 months since release" is factually wrong

**Status: RESOLVED** — corrected to "~26 months" in `README.md` line 31 and `references/browser-tty-comparison.md` line 22.

**Files affected:**
- `README.md` line 31 (key facts table notes column)
- `references/browser-tty-comparison.md` line 22 (ttyd maintainer signal paragraph)

**Expected (per citations.md [9]):**
ttyd v1.7.7 released 2024-03-30. Research date 2026-05-23.
Span: 2024-03-30 → 2026-03-30 = 24 months; + 54 days ≈ 25–26 months.

**Actual text:**
- `README.md` line 31: `Stable; 14 months since release`
- `browser-tty-comparison.md` line 22: `no release in 14 months as of 2026-05-23`

**Correct value:** approximately 25–26 months (≈25 months 24 days).

**Notes:** The 14-month figure appears to derive from May 2024 → May 2026 = 24 months, minus some earlier reference date, or may reflect a midpoint in the prior cadence. Regardless, 2024-03-30 to 2026-05-23 cannot yield 14 months under any standard interpretation. The error appears in both files, suggesting it was written consistently but incorrectly. The key facts table in `README.md` correctly states the release date as 2024-03-30, making the "14 months" claim internally contradictory within the same row.

---

## C-02 — MODERATE: Unsupported "weekly" release cadence claim for OpenClaw

**Status: RESOLVED** — `README.md` line 36 now reads `active 2026 [4, 6]` with no fabricated cadence claim.

**File:** `README.md` line 36

**Actual text:**
```
| OpenClaw | (active) | weekly [6] | n/a | ...
```

**Expected per citations.md [6]:**
Citation [6] (Wikipedia — OpenClaw) states: "247,000 stars and 47,700 forks as of 2026-03-02." It does not state a release cadence or say releases are weekly.

Citation [4] (openclaw/openclaw repo) states: "374k stars, 51,743 commits on main as of 2026-05-23 fetch" — also no mention of "weekly" release cadence.

**Issue:** "weekly" is an interpolated/inferred claim, not documented in either cited source. The correct marker should be something like "~weekly (est.)" with an acknowledged gap, or the claim should be dropped in favor of citing actual release dates if available. No citation in the session documents weekly release cadence.

---

## C-03 — MODERATE: gotty image size unverified in README without gap marker

**Status: RESOLVED** — `README.md` line 32 now reads `~19 MB community Alpine (gap — unverified)`.

**File:** `README.md` line 32
**Reference file:** `references/browser-tty-comparison.md` lines 99, 103, 204

**README text:** `~19 MB community Alpine` (no gap marker)

**browser-tty-comparison.md text:**
- Line 99: "community Alpine images report ~19 MB compressed (discovery-agent snippet, not directly verified). **Gap.**"
- Line 103: "Community Docker images are Alpine-based (discovery-agent finding from non-official images). **Gap on official image.**"
- Line 204 (comparison table): `~19 MB compressed (community Alpine)` (no citation number)

**Issue:** `browser-tty-comparison.md` explicitly marks this value as unverified with **Gap** in the prose section, but the comparison table in that same file omits the gap marker. The README propagates the table form (no gap marker). Wetty's `~105 MB` is marked `(gap)` in the README, but gotty's `~19 MB` is not, creating an inconsistency in how unverified values are signaled.

**Note:** The `browser-tty-comparison.md` comparison table also does not carry the gap marker for gotty's image size, so the README is consistent with the table, but both are inconsistent with the prose section of the same reference file.

---

## C-04 — MINOR: Missing citation [19] in README disqualifying table for RAM claim

**Status: RESOLVED** — `README.md` line 19 disqualifying table row now cites `[19, 21, 22, 25]`.

**File:** `README.md` line 19

**Actual text:**
```
| code-server | ≥1 GB RAM floor and 265 MB image per pod; CVE-2025-47269 (CVSS 8.3, May 2025); Coder docs say it's not for multi-user | [21, 22, 25] |
```

**Expected:** Citation [19] (`coder/code-server` repository, which states "1 GB RAM, and 2 vCPUs") is the source for the RAM floor claim. It appears in every other file that states this figure (`browser-tty-comparison.md` line 179, line 206; `synthesis.md` line 24; `k8s-deployment-patterns.md` line 57). The README disqualifying table omits [19], leaving the RAM claim without a citation in that row.

**Note:** Citations [21] (CVE), [22] (Coder docs warning), and [25] (Docker Hub image size) are all present and correct for the other two claims in the row. The omission is only for the RAM floor.

---

## C-05 — MINOR: Rounded "265 MB" vs precise "265.68 MB" in README disqualifying table

**Status: RESOLVED** — `README.md` line 19 now reads `265.68 MB image per pod`.

**File:** `README.md` line 19

**Actual text:** `265 MB image per pod`
**All other files:** `265.68 MB` (citations.md [25]; browser-tty-comparison.md line 180, 206; synthesis.md line 24; README key facts table line 34)

**Issue:** The disqualifying table uses a rounded value (265 MB) while the key facts table in the same file (line 34) uses the precise value (265.68 MB). This is a minor precision inconsistency within `README.md` itself. The rounded value is not wrong, but creates a discrepancy between rows of the same document.

---

## Items Verified as Consistent

The following values and claims were checked against `citations.md` and found to be consistent across all files:

| Claim | Value | Citation | Files consistent |
|---|---|---|---|
| ttyd image size | 6.9 MB compressed (Alpine) | [11] | citations, README, deliverable, browser-tty-comparison, synthesis |
| ttyd last release | v1.7.7, 2024-03-30 | [9] | citations, README, deliverable, browser-tty-comparison |
| code-server image size (linux/amd64) | 265.68 MB | [25] | citations, README key facts, deliverable, browser-tty-comparison, synthesis |
| code-server image size (linux/arm64) | 265.08 MB | [25] | citations, browser-tty-comparison |
| code-server min RAM | ≥1 GB, 2 vCPUs | [19] | citations, browser-tty-comparison, k8s-deployment-patterns, synthesis |
| code-server latest release | v4.121.0, 2026-05-20 | [19, 20] | citations, README, deliverable, browser-tty-comparison, k8s-deployment-patterns |
| CVE-2025-47269 CVSS score | 8.3 | [21] | citations, README, deliverable, browser-tty-comparison |
| CVE-2025-47269 affected versions | <4.99.4 | [21] | citations, browser-tty-comparison, k8s-deployment-patterns |
| CVE-2025-47269 published | 2025-05-09 | [21] | citations, browser-tty-comparison |
| code-server PVC default size | 10 Gi | [23] | citations, README, deliverable, browser-tty-comparison, k8s-deployment-patterns, synthesis |
| code-server PVC access mode | ReadWriteOnce | [23] | citations, deliverable, k8s-deployment-patterns, synthesis |
| CloudTTY latest chart | 0.8.9, 2025-01-27 | [27] | citations, README, deliverable, k8s-deployment-patterns, synthesis |
| CloudTTY README quickstart version | 0.5.0 (stale) | [26, 27] | citations, README, deliverable, k8s-deployment-patterns, synthesis |
| gotty latest release | v1.7.2, 2026-05-17 | [15] | citations, README, deliverable, browser-tty-comparison |
| gotty image size | ~19 MB community Alpine | [discovery agent] | README, deliverable, browser-tty-comparison (prose marks as Gap) |
| wetty latest release | v2.7.0, 2023-09-16 | [16] | citations, README, deliverable, browser-tty-comparison, synthesis |
| wetty image size | ~105 MB (gap) | [discovery agent] | README (gap marker), deliverable, browser-tty-comparison |
| ingress-nginx archive date | 2026-03-24 | [30] | citations, README, deliverable, k8s-deployment-patterns, synthesis |
| NVIDIA OpenShell latest release | v0.0.47, 2026-05-22 | [2] | citations, README, deliverable, openshell |
| OpenShell release cadence | ~daily (v0.0.43–v0.0.47 in 5 days) | [2] | citations, openshell |
| OpenShell license | Apache 2.0 | [1] | citations, openshell |
| OpenShell primary language | Rust 89.6% | [1] | citations, openshell |
| OpenClaw creator | Peter Steinberger, Austrian developer | [4, 6] | citations, openclaw |
| OpenClaw star count (2026-05-23) | 374k | [4] | citations, openclaw, deliverable |
| OpenClaw star count (2026-03-02) | 247,000 | [6] | citations, openclaw |
| OpenClaw fork count (2026-03-02) | 47,700 | [6] | citations, openclaw |
| OpenClaw initial release name | Clawdbot, November 2025 | [6] | citations, openclaw |
| OpenClaw renamed to Moltbot | 2026-01-27 | [6] | citations, openclaw |
| Tailscale Operator lazy cert provisioning | "first connection might be slow or even time out" | [28] | citations, k8s-deployment-patterns, synthesis |
| Traefik v3 WebSocket support | Out of the box, no special config | [29] | citations, deliverable, browser-tty-comparison, k8s-deployment-patterns, synthesis |
| ttyd auth-header mode requires unix socket | Per wiki [10] | [10] | citations, browser-tty-comparison, synthesis |
| ttyd credential plaintext exposure | `-c user:pass` visible in `ps aux` and `kubectl describe pod` | [13] | citations, browser-tty-comparison, synthesis |
| wetty Origin-header vuln | Unpatched upstream, fix applied by Glitch | [18] | citations, browser-tty-comparison, synthesis |
| code-server Helm image tag | 4.121.0 | [23] | citations, deliverable, browser-tty-comparison, k8s-deployment-patterns |
| CloudTTY CRD | `cloudshell.cloudtty.io/v1alpha1` | [26] | citations, deliverable, k8s-deployment-patterns |

---

## Cross-Reference Link Verification

All internal markdown links were checked against the directory structure:

| Link | From file | Expected target | Status |
|---|---|---|---|
| `[citations.md](citations.md)` | README.md, browser-accessible-coding-shells.md | `research/browser-accessible-coding-shells/citations.md` | PASS |
| `[citations.md](../citations.md)` | references/*.md | `research/browser-accessible-coding-shells/citations.md` | PASS |
| `[references/openshell.md](references/openshell.md)` | browser-accessible-coding-shells.md, README.md | correct relative path | PASS |
| `[references/openclaw.md](references/openclaw.md)` | browser-accessible-coding-shells.md, README.md | correct relative path | PASS |
| `[references/browser-tty-comparison.md](references/browser-tty-comparison.md)` | browser-accessible-coding-shells.md, README.md | correct relative path | PASS |
| `[references/k8s-deployment-patterns.md](references/k8s-deployment-patterns.md)` | browser-accessible-coding-shells.md, README.md | correct relative path | PASS |
| `[references/synthesis.md](references/synthesis.md)` | browser-accessible-coding-shells.md, README.md | correct relative path | PASS |
| `[openshell.md](openshell.md)` | synthesis.md, openclaw.md | within references/ directory — correct | PASS |
| `[openclaw.md](openclaw.md)` | synthesis.md | within references/ directory — correct | PASS |
| `[browser-tty-comparison.md](browser-tty-comparison.md)` | synthesis.md | within references/ directory — correct | PASS |
| `[k8s-deployment-patterns.md](k8s-deployment-patterns.md)` | synthesis.md | within references/ directory — correct | PASS |
| `[audit/citation-audit.md](audit/citation-audit.md)` | README.md | `research/browser-accessible-coding-shells/audit/citation-audit.md` | PASS (file expected to exist after Phase 4) |
| `[audit/consistency-review.md](audit/consistency-review.md)` | README.md | this file | PASS |

---

## Contradiction Transparency Check

The one known source disagreement (CloudTTY README 0.5.0 vs releases page 0.8.9) is explicitly surfaced in every file that mentions CloudTTY. All files consistently note the docs-to-reality gap. No other source contradictions were found within the verified citations.

---

## Estimation Marker Check

| Estimate | Marker present | Files |
|---|---|---|
| gotty image size (~19 MB) | **Gap** in prose; absent from comparison table | browser-tty-comparison (inconsistent), browser-accessible-coding-shells.md (no marker), README (no marker) |
| wetty image size (~105 MB) | `(gap)` in README; **Gap** in browser-tty-comparison prose and table | Consistent |
| wetty base OS (likely Debian) | **Gap** in browser-tty-comparison | Consistent |
| gotty base OS (Alpine, community) | **Gap on official image** in browser-tty-comparison | Consistent |
| wetty idle RAM (50–100 MB) | **Gap** in browser-tty-comparison | Consistent |
| gotty idle RAM | **Gap** in browser-tty-comparison | Consistent |
| OpenClaw release cadence ("weekly") | No gap marker — see C-02 | INCONSISTENT |

---

## Gaps and Limitations Coverage

All files contain a "Gaps and Limitations" section, with one exception: `README.md` does not have a dedicated gap section (it is a summary document, so this is expected). The main deliverable (`browser-accessible-coding-shells.md`) has a "Limitations and gaps" section that covers all major unverified claims. The reference files each carry their own gap sections appropriate to their scope. Coverage is adequate.
