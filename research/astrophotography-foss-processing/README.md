# Astrophotography Processing with Free Open Source Software (2026)

How to process public domain deep sky imaging data using modern, free, open
source tools — with links to guides and YouTube tutorials.

## TL;DR

Three FOSS tools form the core pipeline:

| Tool | What It Does | Version |
|------|-------------|---------|
| **Siril** | Calibration, stacking, color calibration, stretching | 1.4.2 (Feb 2026) |
| **GraXpert** | AI gradient removal, denoising, deconvolution | 3.0.2 |
| **StarNet V2** | Neural network star removal | CLI 2.0.0 |

The standard workflow:
**Siril** (calibrate → stack) → **GraXpert** (gradient → denoise) → **Siril** (color calibrate → stretch) → **StarNet** (remove stars) → **GIMP** (final edit) → **Siril** (recompose stars)

## Quick Start Decision Framework

1. **Need data?** → MAST Portal (archive.stsci.edu) for JWST/Hubble, or
   Cloudy Nights practice files for amateur data with calibration frames
2. **First time?** → Install Siril + GraXpert + StarNet V2, follow Siril's
   "First Steps" tutorial (difficulty 0/5), watch Deep Space Astro's Siril 1.4
   beginner video
3. **Broadband (LRGB)?** → Stack per-filter in Siril, combine with `rgbcomp`,
   SPCC for color calibration
4. **Narrowband?** → Extract Ha/OIII with Siril scripts, combine via PixelMath
   (HOO: R=Ha, G=OIII, B=OIII)
5. **Archive data?** → Download Stage 2 FITS from MAST, skip calibration,
   start at background extraction

## Key YouTube Resources

| Channel | What They Cover |
|---------|----------------|
| **Nebula Photos** (Nico Carver) | Siril + GIMP workflows, narrowband, JWST data |
| **Deep Space Astro** | Siril-dedicated tutorials (beginner → advanced) |
| **Cuiv, The Lazy Geek** | Siril as PixInsight alternative, urban AP |
| **AstroBackyard** | DeepSkyStacker, StarNet++, software comparisons |

## Files in This Directory

| File | Content |
|------|---------|
| [astrophotography-foss-guide.md](astrophotography-foss-guide.md) | Full guide with methodology |
| [citations.md](citations.md) | All 105 sources, numbered and tiered |
| [references/public-data-sources.md](references/public-data-sources.md) | Where to get free data |
| [references/foss-software-landscape.md](references/foss-software-landscape.md) | Tool comparison and versions |
| [references/processing-workflows.md](references/processing-workflows.md) | End-to-end workflow guides |
| [references/youtube-tutorials.md](references/youtube-tutorials.md) | Video resources catalog |
| [references/calibration-stacking.md](references/calibration-stacking.md) | Calibration frame theory |
| [references/narrowband-broadband.md](references/narrowband-broadband.md) | Filter-specific techniques |
| [audit/citation-audit.md](audit/citation-audit.md) | Independent citation verification |
| [audit/consistency-review.md](audit/consistency-review.md) | Cross-file consistency check |
