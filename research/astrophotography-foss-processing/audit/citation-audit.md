# Citation Audit Report

Independent verification of claims against their cited sources. Performed by
a separate agent with no context from the research conversation.

## Summary

- Total citations checked: 35
- ACCURATE: 22
- INACCURATE: 3 → **Status: RESOLVED** (all 3 fixed post-audit)
- PARTIAL: 6
- UNVERIFIED: 4
- INACCESSIBLE: 5 (403/permission denied)

## Resolved Inaccuracies

### [3] GHS listed as v1.4.0 addition
**Original claim**: GHS grouped under "v1.4.x series added"
**Issue**: GHS predates v1.4.0 — it has its own tutorial [4] but is not in the 1.4.0 release notes
**Status: RESOLVED** — GHS moved to pre-existing features section, separated from v1.4.x additions

### [3] "Python scripting with built-in IDE"
**Original claim**: Siril has a "built-in IDE" for Python
**Issue**: 1.4.0 release notes say "complete Python scripting system" — no mention of IDE
**Status: RESOLVED** — Changed to "Python scripting system"

### [53] Astrowheep workflow StarNet attribution
**Original claim**: Step 7 used StarNet for star removal
**Issue**: Astrowheep tutorial uses ImagesPlus, not StarNet
**Status: RESOLVED** — Corrected to note ImagesPlus as the original tool

## Partial Matches

### [1] Siril GPL v3
**Claim**: "GPL v3 [1]"
**Rating**: PARTIAL
**Evidence**: Homepage metadata shows CC-BY (website content license). GPL v3 is the software license per GitLab repo and JOSS paper [6], not prominently stated on homepage.

### [7] GraXpert BSD-3-Clause and methods
**Claim**: "BSD-3-Clause", "RBF, Splines, Kriging"
**Rating**: PARTIAL
**Evidence**: Website confirms open source but doesn't state BSD-3-Clause. License confirmed on GitHub [8]. Methods not mentioned on homepage.

### [53] Astrowheep — ImagesPlus vs StarNet
**Claim**: StarNet for star removal in Astrowheep workflow
**Rating**: PARTIAL → RESOLVED
**Evidence**: Tutorial uses ImagesPlus, not StarNet. Fixed post-audit.

### [12] PHD2 version and license
**Claim**: "v2.6.14, BSD"
**Rating**: UNVERIFIED from homepage — details not prominent.

### [22] ESASky 500,000+ images
**Claim**: "500,000+ images"
**Rating**: UNVERIFIED — ESASky loads via JS, count not extractable.

### [30] AstroBackyard count
**Claim**: "7 stacked nebulae"
**Rating**: PARTIAL — count is 7 but includes Andromeda Galaxy (not technically a nebula).

## Inaccessible Sources (403)

- [13] deepskystacker.com
- [24] astroarchive.noirlab.edu
- [26] archive.eso.org
- [33] cloudynights.com forum thread
- [68] ui.adsabs.harvard.edu (Drizzle paper)
- [100] practicalastrophotography.com
- [101] skyandtelescope.org

## Accurate Confirmations (Key)

| Citation | Claim | Confirmed |
|----------|-------|-----------|
| [2] | Siril 1.4.2, 2026-02-18, GPU manager, UCRT64 8192 | Yes |
| [3] | Drizzle and SPCC in v1.4.0 | Yes |
| [4] | 24 tutorials, difficulty 0–5, Deep Space Astro + BorealisLite | Yes |
| [8] | GraXpert 3.0.2, v3.0.0 AI denoising, GPU accel | Yes |
| [9] | StarNet CLI 2.0.0, Win/Mac/Linux | Yes |
| [20] | JWST 4 processing stages | Yes |
| [29] | MOANA 254mm, 0.591″/px, CC license, concluded Jan 2024 | Yes |
| [43] | rgbcomp up to 8 inputs, linear-match | Yes |
| [49] | max(Red, Q*Ha), Q=1.5, Alexander Curry, 13 min, free | Yes |
| [50] | Continuum subtraction formula | Yes |
| [53] | Modified SHO: R=Ha, G=0.9×OIII+0.1×Ha, B=OIII | Yes |
| [61] | Deep Space Astro Siril 1.4 beginner tutorial, 2025-05-17 | Yes |
| [65] | Sigma-clip > median, 40× precision improvement | Yes |
| [72] | 6-video series, 39 minutes | Yes |
| [105] | PixInsight $275, Siril free, Photoshop $22.99/mo | Yes |
