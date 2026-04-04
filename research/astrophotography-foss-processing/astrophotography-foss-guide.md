# Processing Public Domain Deep Sky Data with Free Open Source Software (2026)

A citation-backed guide to astrophotography image processing using modern FOSS
tools. Every factual claim traces to a web source visited in-session. Two
independent review agents audited this document — see
[audit/citation-audit.md](audit/citation-audit.md) and
[audit/consistency-review.md](audit/consistency-review.md).

---

## Table of Contents

1. [The FOSS Processing Stack](#1-the-foss-processing-stack)
2. [Where to Get Public Domain Data](#2-where-to-get-public-domain-data)
3. [End-to-End Processing Workflow](#3-end-to-end-processing-workflow)
4. [Calibration and Stacking Fundamentals](#4-calibration-and-stacking-fundamentals)
5. [Broadband (LRGB) Processing](#5-broadband-lrgb-processing)
6. [Narrowband Processing (SHO, HOO)](#6-narrowband-processing-sho-hoo)
7. [Processing Archive Data (JWST, Hubble)](#7-processing-archive-data-jwst-hubble)
8. [YouTube Learning Resources](#8-youtube-learning-resources)
9. [Limitations and Methodology](#9-limitations-and-methodology)

---

## 1. The FOSS Processing Stack

Three tools form the core of the modern FOSS deep sky pipeline:

| Tool | Version | Purpose | License | Platforms |
|------|---------|---------|---------|-----------|
| **Siril** | 1.4.2 (2026-02-18) [2] | Calibration, stacking, registration, color calibration, stretching | GPL v3 [1] | Win/Mac/Linux [2] |
| **GraXpert** | 3.0.2 (2024-05-03) [8] | AI gradient extraction, denoising, deconvolution | BSD-3-Clause [7] | Win/Mac/Linux [7] |
| **StarNet V2** | CLI 2.0.0 [9] | Neural network star removal | Open source [10] | Win/Mac/Linux [9] |

### Siril 1.4.x Highlights

Siril is the backbone of the FOSS pipeline. The v1.4.x series (December 2025 onward) added [2][3]:

- **Drizzle** — proper HST algorithm for super-resolution stacking [3]
- **SPCC** — Spectrophotometric Color Calibration using Gaia DR3 spectral data [3][78]
- **Python scripting** system [3]
- **Native StarNet integration** [41]
- **GraXpert integration** [7]
- **PixelMath** for narrowband channel combination [44]
- GPU manager improvements and UCRT64 Windows build (file limit raised to 8,192) [2]
- Peer-reviewed in the Journal of Open Source Software [6]

### GraXpert Capabilities

GraXpert uses CNN-based AI for [7][8]:
- **Background gradient extraction** — removes light pollution and vignetting artifacts
- **AI denoising** for linear images (v3.0.0+) [8]
- **AI stellar deconvolution** (v3.1.0rc2) [8]
- **AI object deconvolution** for nebulae/galaxies (v3.1.0rc1) [8]
- Traditional methods also available: RBF, Splines, Kriging [7]
- GPU acceleration on all platforms: DirectML (Windows), CUDA 12 (Linux), CoreML (macOS) [8]

### Supporting Tools

| Tool | Purpose | Citation |
|------|---------|----------|
| **DeepSkyStacker** (6.1.0) | Alternative stacker; now cross-platform. BSD 3-Clause [13][14] | [13] |
| **GIMP** | Final image editing (curves, saturation, layer compositing) [105] | [105] |
| **ASTAP** | Stacking + native plate solving [15] | [15] |
| **KStars/EKOS/INDI** | Telescope control + capture (Linux-native) [11] | [11] |
| **PHD2** (2.6.14) | Autoguiding. BSD [12] | [12] |
| **NINA** (3.2) | Imaging sequence automation (Windows). MPL 2.0 [16] | [16] |
| **SAO DS9** | FITS viewer, useful for JWST data [67] | [67] |

---

## 2. Where to Get Public Domain Data

### Professional Archives (Institutional)

| Archive | What's There | Access |
|---------|-------------|--------|
| **MAST Portal** (archive.stsci.edu) [19] | All JWST + Hubble data. 4 processing levels. FITS | No registration for public data |
| **ESASky** (sky.esa.int) [22] | 500,000+ images across ESA missions. FITS | No login |
| **NOIRLab** (astroarchive.noirlab.edu) [24] | 40+ ground telescopes. Compressed FITS | No account needed |
| **SDSS DR18** (sdss.org) [25] | Full-sky survey. Calibrated FITS frames | No registration |
| **ESO Archive** (archive.eso.org) [26] | VLT/La Silla. ~20M FITS files. CC-BY | Registration required |

For astrophotography processing, MAST's Stage 2 `_i2d.fits` files are the typical starting point — already calibrated, ready for background extraction and color mapping [20].

### Community Data for Practice

| Source | Content | Format | Calibration |
|--------|---------|--------|-------------|
| **MOANA Project** [29] | Deep sky broadband + narrowband (Ha/OIII/SII). 254mm scope, 0.591″/px | Raw FITS | Creative Commons |
| **Cloudy Nights thread** [33] | M31, M42, M45, M13 | Canon CR2 | Darks + bias included |
| **Astropix.com** [35] | M31, M42, M45, M13 | Canon CR2 | None |
| **AstroBackyard** [30][31] | 7 stacked nebulae + DSS practice files | TIFF/various | DSS files include cals |
| **Telescope Live** [32] | Curated samples from dark-site observatories | FITS | Full calibration archive |

See [references/public-data-sources.md](references/public-data-sources.md) for the complete inventory.

---

## 3. End-to-End Processing Workflow

### The Standard FOSS Pipeline

The community-dominant workflow in 2025–2026 [53][54][58]:

```
1. Siril        → Calibrate (darks, flats, bias)
2. Siril        → Register (align frames)
3. Siril        → Stack (sigma-clipped average)
4. GraXpert     → Remove gradients (AI background extraction)
5. GraXpert     → Denoise (AI, on linear data)
6. Siril        → Color calibrate (PCC or SPCC)
7. StarNet V2   → Remove stars (creates starless + star mask)
8. Siril        → Stretch (GHS or Veralux scripts)
9. GIMP         → Final editing (curves, saturation, layers)
10. Siril       → Recompose stars (blend star mask back)
```

### Beginner Quick Start

**Fastest path from zero to processed image:**

1. **Get data**: Download Cloudy Nights practice files [33] or AstroBackyard DSS practice data [31]
2. **Install**: Siril [1], GraXpert [7], StarNet V2 [9]
3. **Follow**: Siril "First Steps" tutorial (difficulty 0/5) [38] — place files in `lights/`, `darks/`, `flats/`, `biases/` subdirectories, run the built-in script
4. **Watch**: Deep Space Astro "Siril 1.4 Beginner Tutorial" [61] or Nico Carver's M31 Siril+GIMP video [82]
5. **Process**: GraXpert for gradient removal [7], StarNet for star removal [9], Siril GHS for stretching [45]

### Intermediate Multi-Tool Workflow (Astrowheep) [53]

1. Stack with Sirilic (Duo Ha/OIII mode, Winsorized/Sigma rejection)
2. Plate solve in Siril
3. Noise reduce at ~40% modulation per channel
4. Combine via PixelMath: R=Ha, G=0.9×OIII+0.1×Ha, B=OIII
5. Crop dithering artifacts
6. GraXpert RBF background extraction
7. StarNet star removal (×2 upsampling) — or ImagesPlus for star reduction [53]
8. GHS stretch (background) + Histogram (stars)
9. Recombine in GIMP (stars as "Screen" blend)
10. Final curves, saturation, hue in GIMP

See [references/processing-workflows.md](references/processing-workflows.md) for additional workflow variants.

---

## 4. Calibration and Stacking Fundamentals

### Why Calibration Matters

Calibration frames correct systematic sensor errors [100]:

| Frame | Captures | Corrects |
|-------|----------|----------|
| **Bias** | Read-out pedestal voltage | Fixed ADC offset |
| **Dark** | Thermal current + hot pixels + amp glow | Temperature-dependent noise |
| **Flat** | Vignetting + dust + QE variation | Optical path non-uniformity |

The math: `calibrated = (raw - master_dark) / master_flat` [100]

**Recommended counts**: 30–50 darks, 30–50 flats, 50–100 bias frames [100]. Use average with sigma-clipping rejection for master creation.

### Stacking Algorithms

| Method | When to Use | SNR vs Mean |
|--------|------------|-------------|
| **Sigma-clipped average** | General purpose, ≥10 frames | Near-optimal [65] |
| **Kappa-sigma clipping** | Satellite trails, artifacts | ~optimal with 3–5 iterations [65] |
| **Median** | Quick rejection, small stacks | ~25% penalty [65] |
| **MAD clipping** | Skewed distributions | More robust than sigma [76] |
| **Linear fit clipping** | Gradient variation across sequence | Best for 25+ frames [76] |

Sigma-clipped average consistently outperforms median [65]. Median causes posterization on 14-bit data; tone-mapping provides ~40× improvement in intensity precision [65].

### SNR and Stacking

SNR improves by √N when averaging N frames [70][102]:
- 4 frames → 2× SNR
- 9 frames → 3× SNR
- 100 frames → 10× SNR

### Dithering

Random 5–20 pixel slew between sub-exposures [101]. Combined with sigma-clipping, this removes hot pixels, column banding, and amp glow patterns without calibration frames [101]. Minimum effective stack: ~6 dithered frames [101].

### Drizzle

Variable-Pixel Linear Reconstruction [68]. Shrinks each input pixel to a "droplet" and distributes flux across a finer output grid. Requires: undersampled data, dithered frames, and sufficient sub-pixel diversity [68].

Siril implements drizzle during registration (scale 0.1–2.0). For Bayer cameras, input must NOT be debayered before drizzle [77].

See [references/calibration-stacking.md](references/calibration-stacking.md) for the full technical treatment.

---

## 5. Broadband (LRGB) Processing

### Workflow

1. Stack each filter (L, R, G, B) independently [40]
2. Apply linear-match equalization [43]
3. Assemble with Siril `rgbcomp` (accepts up to 8 inputs) [43]
4. Color calibrate with SPCC (Siril 1.4+) [78] or PCC

**SPCC** uses Gaia DR3 spectral data + sensor QE curves + filter transmittance curves for more accurate calibration than PCC [3][78]. Requires a plate-solved, linear image.

### Guides

| Source | Level | Tools | Citation |
|--------|-------|-------|----------|
| Siril RGB Composition Tutorial | Intermediate | Siril | [43] |
| Telescope.Live LRGB Galaxy | Intermediate | Siril + Affinity | [51] |
| Lonely Speck LRGB | Intermediate | Siril + Photoshop | [56] |
| PIXLS.US Community | Intermediate | Siril | [62] |

---

## 6. Narrowband Processing (SHO, HOO)

### Palette Channel Assignments

| Palette | R | G | B |
|---------|---|---|---|
| **SHO (Hubble)** | SII | Ha | OIII |
| **Modified SHO** | Ha | 0.9×OIII + 0.1×Ha | OIII [53] |
| **HOO (Bicolor)** | Ha | OIII | OIII [44][59] |

### HOO in Siril PixelMath [44]

```
R = Ha
G = OIII
B = OIII
```

### Ha-Enhanced RGB

**Max blend** [49]: `R = max(Red, Q * Ha)` where Q ≈ 1.5

**Continuum subtraction** [50]: `Ha_pure = Ha - Q * (Red - median(Red))` — isolates pure emission by removing stellar continuum.

### OSC Dual-Narrowband Extraction [94]

For cameras with L-eXtreme or L-eNhance filters:
1. Run Siril's `OSC_Extract_HaOIII` script [94]
2. Register and stack Ha and OIII separately
3. Combine via PixelMath [104]

### Starless Processing Strategy [49][53]

1. Remove stars from all channels using StarNet V2
2. Process nebula aggressively (stretch, color, contrast)
3. Recompose stars from a single dataset to avoid doubling
4. Stars at "Screen" blend mode in GIMP [53]

See [references/narrowband-broadband.md](references/narrowband-broadband.md) for the complete treatment.

---

## 7. Processing Archive Data (JWST, Hubble)

### JWST Data

JWST data is available at four processing stages through MAST [20]:

| Stage | Content | Use for AP |
|-------|---------|-----------|
| 0 | Raw spacecraft FITS | Rarely needed |
| 1 | Count-rate with detector corrections | Specialist use |
| **2** | **Fully calibrated individual exposures** | **Start here** |
| 3 | Combined final products | Ready to view |

**Workflow** [20][52][67]:
1. Search MAST Portal for your target
2. Download Stage 2 `_i2d.fits` files
3. Open in Siril [75] or SAO DS9 [67]
4. Assign narrowband filters to color channels (JWST uses F-number notation: F187N, F470N, etc.)
5. Background extraction → color mapping → stretching

### No-Calibration Processing

Archive data is already calibrated — no darks/flats/bias needed [20]. For community data without calibration frames:
- Sigma-clipping + dithering handles hot pixels [64]
- GraXpert handles gradient residuals [7]
- Amp glow (CMOS) cannot be fully corrected post-capture

### Smart Telescope Data (Seestar, Dwarf)

Siril's Seestar script [46] processes pre-stacked FITS: plate solve → register with Drizzle → stack → SPCC → auto-stretch.

---

## 8. YouTube Learning Resources

### Channels Focused on FOSS Tools

| Channel | Handle | Focus | Key Content |
|---------|--------|-------|-------------|
| **Nebula Photos** (Nico Carver) | @NebulaPhotos [81] | Siril + GIMP, narrowband, light-polluted skies | M31 Siril+GIMP [82], M31 DSS+GIMP [83], M42 DSS+GIMP [84], JWST processing |
| **Deep Space Astro** | YouTube + buymeacoffee [85] | Siril-dedicated tutorials | Siril 1.4 beginner [61], SPCC [95], mosaics, VeraLux, automation |
| **Cuiv, The Lazy Geek** | UC65vvpQDX5rymeqrYt-Bb1g [86] | Urban AP, FOSS alternatives | "Siril a Free Alternative to PixInsight" (2020) |

### Channels with Notable FOSS Content

| Channel | Handle | Relevant Videos |
|---------|--------|----------------|
| **AstroBackyard** (Trevor Jones) | @AstroBackyard [87] | DSS stacking [88][89], StarNet++ [90] |
| **BorealisLite** | Referenced by Siril [4] | Siril tutorials |
| **AstroOnBudget** (Jeremiah) | — | GraXpert denoising [73] |

### Specific Video URLs (Verified)

| Video | URL | Tools |
|-------|-----|-------|
| Nico Carver — M31 (Siril + GIMP) | youtu.be/ambUmZLOeSs [82] | Siril, GIMP |
| Nico Carver — M31 (DSS + GIMP) | youtu.be/K5b9PVwSB6Q [83] | DSS, GIMP |
| Nico Carver — M42 (DSS + GIMP) | youtu.be/fkldylli094 [84] | DSS, GIMP |
| AstroBackyard — DSS Stacking | youtube.com/watch?v=4DbUkgjf6gs [88] | DSS |
| AstroBackyard — DSS FITS | youtube.com/watch?v=ANZ9XwfMhXA [89] | DSS |
| Chuck Ayoub — StarNet++ | youtube.com/watch?v=Uayg_CMwzJo [90] | StarNet V2 |

### Tutorial Series

| Series | Source | Length | Level | Citation |
|--------|--------|--------|-------|----------|
| Siril + Telescope.Live Beginner | telescope.live [91] | 6 videos, 39 min | Beginner | [72] |
| Ha Enhancement with Siril | telescope.live [49] | 13 min | Intermediate | [49] |
| GraXpert Gradient/Denoising | telescope.live [48] | — | Beginner | [48] |
| Intro to SIRIL (NJAA) | classcentral.com [92] | — | Beginner | [92] |

See [references/youtube-tutorials.md](references/youtube-tutorials.md) for the complete catalog.

---

## 9. Limitations and Methodology

### Research Methodology

This document was produced using the cited-research methodology:
- **Phase 1**: Six parallel research agents searched across all dimensions
- **Phase 2**: Findings organized into reference files with inline citations
- **Phase 3**: Deliverable written with accountability clause
- **Phase 4**: Two independent verification agents audited citations and consistency

### Known Limitations

1. **YouTube video IDs partially unresolvable**: YouTube renders via JavaScript; specific watch URLs for Deep Space Astro and many Nico Carver videos could not be extracted. Channel handles and content themes are confirmed through secondary sources [81][85][86].

2. **Siril readthedocs blocked (403)**: Official documentation for stacking parameters, drizzle, SPCC, and registration was inaccessible to web fetchers (AI crawler blocking). Data sourced from search snippets and discovery agent findings [76][77][78][79].

3. **FOSS-specific JWST tutorials sparse**: Most JWST processing tutorials use PixInsight or Photoshop. Siril-specific archive processing guides are limited to community threads [75].

4. **StarNet V2 license ambiguity**: Source on GitHub [10] but explicit license terms not confirmed on the download page [9].

5. **GraXpert v3.1.0 not yet stable**: RC2 as of data collection. AI stellar and object deconvolution are release-candidate features [8].

6. **Telescope.Live paywall uncertainty**: Some tutorials confirmed free [49]; others may require subscription.

7. **MOANA Project longevity**: Archive appears accessible but the project concluded January 2024 [29].

### Source Quality Distribution

| Tier | Count | Examples |
|------|-------|---------|
| Tier 1 (institutional/peer-reviewed) | 14 | MAST, ESA, JOSS paper, Drizzle paper, ESO |
| Tier 2 (official docs/manufacturer) | 28 | Siril, GraXpert, StarNet, KStars, PHD2 |
| Tier 3 (established practitioner) | 48 | AstroBackyard, Telescope.Live, Nebula Photos |
| Tier 4 (forums/personal blogs) | 15 | Cloudy Nights, PIXLS.US, Stargazers Lounge |

---

*Generated By: Claude Code (Claude Opus 4.6)*
