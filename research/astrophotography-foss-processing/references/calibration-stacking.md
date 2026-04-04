# Calibration and Stacking Fundamentals

Dimension 5: Theory and practice behind calibration frames and image stacking.

All sources cited to [citations.md](../citations.md).

---

## Calibration Frames

The calibration equation [100][69]:

```
calibrated_light = (raw_light - master_dark) / master_flat
```

Where master_dark already includes bias subtraction, and master_flat is normalized.

### Frame Types

| Frame | How to Capture | What It Corrects | Key Constraints |
|-------|---------------|-----------------|-----------------|
| **Bias/Offset** | Shortest exposure, lens capped | Read-out pedestal voltage, fixed ADC offset | No thermal signal, no photons [100] |
| **Dark** | Same exposure, ISO/gain, temperature as lights; lens capped | Thermal dark current, hot pixels, amp glow, fixed pattern noise | Must match light parameters exactly [100] |
| **Flat** | Short exposure of uniform field (twilight, light panel) | Vignetting, dust motes, pixel-to-pixel QE variation | Histogram peak at 1/3–1/2 full scale [100] |
| **Flat dark** | Dark at flat-frame exposure time | Dark current in flat frames themselves | Short exposure = primarily read noise |

### Master Frame Best Practices

Recommended frame counts [100]:

| Frame Type | Minimum | Recommended |
|-----------|---------|-------------|
| Bias | 30 | 50–100 |
| Dark | 15 | 30–50 |
| Flat | 15 | 30–50 per filter/config |
| Flat dark | 50 | 100–200 |

Integration method for masters: average with sigma-clipping rejection. Bias and dark masters must NOT have normalization applied. Flat masters use multiplicative normalization [100].

Critical: always use ≥ as many bias frames as dark frames to prevent read-noise amplification in bias-subtracted darks [100].

---

## Stacking Algorithms

### Core Methods

| Method | How It Works | SNR Behavior | Best For |
|--------|-------------|-------------|----------|
| **Sum** | Adds all pixel values | SNR ∝ √N | Maximum dynamic range |
| **Average (mean)** | Sum ÷ N | SNR ∝ √N, best preservation | Clean data, no artifacts |
| **Median** | Middle value of sorted stack | ~25% SNR penalty vs mean [65] | Quick outlier rejection |
| **Kappa-sigma clipping** | Iterative: reject beyond mean ± κ×σ | Near-mean SNR | General purpose, ≥10 frames [65] |
| **Winsorized sigma** | Replace extremes at percentile limits | Similar to kappa-sigma | Alternative to kappa-sigma |
| **Linear fit clipping** | Fit y=ax+b, reject outliers | Best for gradient variation | Large stacks (25+ frames) |

Sigma-clipped average consistently outperforms median [65]: median causes posterization artifacts on 14-bit data, while sigma-clipped average produces smoother intensity transitions. Tone-mapping provides approximately 40× improvement in intensity precision for faint signal [65].

### Siril Stacking Implementation [76]

Five combination methods: Sum, Mean, Median, Minimum, Maximum.

Five rejection algorithms:
1. **Percentile clipping** — best for ≤6 frames
2. **Sigma clipping** — iterative kappa-sigma
3. **MAD clipping** — uses Median Absolute Deviation (more robust for skewed distributions)
4. **Linear fit clipping** — Siril implementation of PixInsight algorithm
5. **Winsorized sigma clipping**

Normalization: IKSS (Iteratively K-Sigma Clipped Scale and Shift) estimators by default. Fast normalization (median+MAD) available for long sequences. Multiplicative normalization preferred when flats are in the pipeline [76].

### DeepSkyStacker Implementation [74]

Star detection: Gaussian curve fit, max radius 50 pixels, minimum 8 common stars [74].

Alignment: Triangle pattern matching by side-distance ratios [74].

Quality scoring: star roundness, FWHM, sky background level; auto-rejects elongated stars [74].

Methods: Average, Median, Kappa-Sigma, Median Kappa-Sigma, Auto Adaptive Weighted Average [74].

Recommended settings: default threshold 10%, Kappa-Sigma clipping for satellite removal, 15+ calibration frames per type [64].

---

## Dithering

Random small telescope slew (5–20 pixels) between sub-exposures [101].

**Why it matters**: Fixed-pattern noise (hot pixels, column banding, amp glow) lands on different sensor locations in each frame. Sigma-clipping rejects those as outliers [101].

- Minimum effective stack with dithering: ~6 frames (for sigma-clipping statistical power) [101]
- Also breaks walking noise from guiding periodicity [101]
- Without dithering, hot pixels survive even aggressive rejection algorithms

---

## Registration (Alignment)

### Star-Based Registration

Siril Global Star Alignment [79]:
- Triangle similarity matching (based on Michael Richmond's "match" program)
- RANSAC outlier rejection for projection matrix computation
- Max 2000 stars detected per frame by default
- Two-pass variant: reference frame selection by star quality metrics

### Plate Solving

Two categories [18]:
- **Local solvers** (ASTAP, PlateSolve2/3): Use local star catalog + known approximate FOV. Fast but need starting hint [15]
- **Blind solvers** (Astrometry.net): No prior required. Geometric hash (quads of 4 stars), translation/rotation/scale invariant. 99.9% success rate [18]

---

## Drizzle (Super-Resolution Stacking)

**Original paper**: Fruchter & Hook (2002), PASP 114:144 — "Variable-Pixel Linear Reconstruction" [68].

How it works: Each input pixel is shrunk to a "droplet" smaller than the output grid. Flux is distributed proportionally across overlapping output pixels. With dithered input, droplets sample different subpixel positions, reconstructing sub-pixel information [68].

**Requirements** [68][77]:
1. Imaging train is undersampled (pixel scale > seeing)
2. Sufficient dithered frames
3. Sub-pixel diversity in offsets

**Siril implementation** [77]: Applied during registration (not stacking). Scale 0.1–2.0. For Bayer cameras, input must NOT be debayered before drizzle registration.

**Trade-off**: Improved resolution at cost of increased noise. No benefit for oversampled or well-sampled systems [68].

---

## SNR Theory

The CCD equation [69]:

```
SNR = S / √(S + n_pix × (sky + dark_current × t + RON²))
```

Where:
- S = source electrons (flux × QE × t) [69]
- sky = sky background electrons/pixel/second
- dark_current = thermal electrons/pixel/second
- RON = read-out noise (electrons per read)
- n_pix = pixels summed over PSF

**Stacking benefit** (average combine): SNR improves by √N [70][102]:
- 4 frames → 2× SNR
- 9 frames → 3× SNR
- 100 frames → 10× SNR

When read-noise dominated (short exposures): each added frame buys proportionally more. When sky-limited (long exposures): gain comes purely from averaging shot noise [69][70].

---

## Processing Without Calibration Frames

When calibration frames are unavailable (archive data, smart telescopes) [64]:

| Problem | Workaround |
|---------|-----------|
| Hot/cold pixels | Sigma-clipping + dithering [64] |
| Vignetting/dust | GraXpert gradient removal [7] |
| Amp glow (CMOS) | Cannot be fully corrected post-capture |
| Fixed-pattern noise | Partially addressed by sigma rejection |

DSS workaround: Kappa-Sigma (κ=2, 5 iterations) with dithered data eliminates most hot pixels even without darks [64].

For pre-calibrated archive data (MAST Stage 2+), calibration is already applied — processing starts at background extraction [20].

---

## Gaps and Limitations

- **CMOS vs CCD dark scaling**: CMOS amp glow cannot be reliably scaled across exposure times. No dedicated technical paper on this mechanism was located.
- **Siril readthedocs 403**: Full stacking/registration parameter documentation was inaccessible to web fetchers (AI crawler blocking). Data sourced from search snippets [76][77][79].
- **Weighted average stacking**: Per-frame weighting by FWHM/SNR is mentioned in DSS and APP but not deeply documented from these sources.
