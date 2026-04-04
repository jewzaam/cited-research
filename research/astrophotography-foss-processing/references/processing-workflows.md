# Processing Workflows

Dimension 3: End-to-end guides for processing deep sky images with FOSS tools.

All sources cited to [citations.md](../citations.md).

---

## The Dominant FOSS Pipeline (2025–2026)

The community-standard workflow chains multiple specialized FOSS tools [53][54][58]:

```
Siril (calibrate/stack) → GraXpert (gradient/denoise) → Siril (color calibrate/stretch) → StarNet (star removal) → GIMP (final editing) → Siril (star recomposition)
```

Variations exist at each step, but this sequence appears in the majority of community tutorials [53][54][57][58].

---

## Beginner Entry Points

### Official Siril Tutorials

Siril provides 24 tutorials at siril.org/tutorials/ [4], organized by difficulty (0–5):

| Tutorial | Difficulty | Key Content |
|----------|-----------|-------------|
| First Steps — Scripts | 0/5 | Automated preprocessing [38] |
| Seestar Processing | 0/5 | Smart telescope data [46] |
| Star Reduction Script | 1/5 | Automated star reduction [42] |
| Gradient Removal | 1/5 | Background extraction |
| Manual Preprocessing | 2/5 | Step-by-step GUI workflow [39] |
| StarNet Integration | 2/5 | Native star removal [41] |
| PixelMath | 3/5 | Narrowband combination [44] |
| GHS Transformations | 3/5 | Non-linear stretching [45] |
| RGB Composition | 3/5 | LRGB assembly [43] |
| pySiril Automation | 4/5 | Python scripting |

### Script-Driven Preprocessing

The recommended beginner path uses Siril's built-in scripts [40]:
1. Place files in named subdirectories: `lights/`, `darks/`, `flats/`, `biases/`
2. Select the appropriate script (DSLR, OSC, Mono, Narrowband)
3. Script handles: master dark/flat/bias creation → calibration → debayering → registration → stacking

Scripts are sensor-type aware with separate variants for DSLR/OSC, monochrome, and narrowband (Ha, OIII, dual-band) [40][94].

### Telescope.Live Beginner Series

Six-video series (39 minutes total) with Alexander Curry [47][72]:
- Intro to Siril (5 min) [47]
- Comprehensive manual preprocessing
- Plate solving + Photometric Color Calibration
- GraXpert gradient removal + denoising (Nik Szymanek) [48]
- GIMP post-processing enhancements
- Nebula Processing Master Class

### Deep Space Astro

Described as "the destination for all things astrophotography and Siril tutorials" [85]. Key content:
- "Siril 1.4 Beginner Tutorial: From Raw to Finished" with free practice data + PDF guide [61]
- Mosaic creation in Siril
- Workflow automation
- VeraLux stretching scripts
- SPCC walkthrough for Siril 1.4 [95]

---

## Complete Multi-Tool Workflows

### Astrowheep Narrowband Workflow [53]

1. **Stack** with Sirilic (Duo Ha/OIII mode, Winsorized/Sigma rejection)
2. **Plate solve** in Siril
3. **Noise reduce** (~40% modulation per channel)
4. **Combine** Ha + OIII via PixelMath: R=Ha, G=0.9×OIII+0.1×Ha, B=OIII
5. **Crop** dithering artifacts
6. **Remove gradients** with GraXpert (RBF)
7. **Remove stars** with StarNet (×2 upsampling) — original tutorial uses ImagesPlus [53]
8. **Stretch** with GHS (background) + Histogram (stars)
9. **Recombine** in GIMP (stars as "Screen" blend mode)
10. **Final tweaks** — curves, saturation, hue in GIMP

### Max Dobres FRAS Guides [54]

Most comprehensive published FOSS guides found. Free step-by-step at maxastro.co.uk [54]:
- Updated to Siril 1.4 (July 2025)
- Covers DSLRs, OSC astro cameras, smart telescopes (Seestar, Dwarf 3)
- Full Siril + GraXpert + GIMP pipeline
- Two published books on Amazon

### UnderSouthWestSkies Siril 1.4 Workflow [58]

December 2025 guide for L-eNhance OSC users:
- Siril 1.4 preprocessing
- GraXpert gradient removal + denoising on linear data
- Veralux stretching scripts [97]
- Channel normalization and mixing for narrowband

### Niall Bell Custom Scripts Workflow

Preprocessing script → PCC → background extraction → green noise removal → GraXpert noise reduction → StarNet star removal → stretch in Siril → export TIFF → starless editing in Affinity Photo → star recombination in Siril → final tweaks.

---

## LRGB Workflows

| Source | Tools | Level | Citation |
|--------|-------|-------|----------|
| Siril RGB Composition Tutorial | Siril only | Intermediate | [43] |
| Telescope.Live LRGB Galaxy | Siril + Affinity Photo | Intermediate | [51] |
| RemoteAstrophotography Guide | Siril (automation scripts) | Intermediate | [55] |
| Lonely Speck LRGB | Siril + Photoshop | Intermediate | [56] |
| PIXLS.US Community Workflow | Siril only | Intermediate | [62] |

The Siril `rgbcomp` command accepts up to 8 input images for LRGB assembly. A linear-match equalization step is applied before combining [43].

---

## Processing Archive Data (No Calibration Frames)

### JWST / Hubble Data

For space telescope data, processing starts at background extraction — calibration is already done [20][52]:
1. Download Stage 2 `_i2d.fits` from MAST Portal [20]
2. Open in Siril or SAO DS9 [67][75]
3. Assign narrowband filters to color channels
4. Background extraction → color mapping → stretching

Guides: Telescope.Live JWST guide [52], Isolated Planets Archive DS9 tutorial [67], PIXLS.US Siril+JWST thread [75], PhotographingSpace Hubble tutorials [36].

### Smart Telescope Data (Seestar, Dwarf)

Siril's Seestar script [46] handles pre-stacked FITS from these devices:
- Plate solving → registration with 1× Drizzle → stacking → SPCC → auto-stretch
- No separate calibration frames (on-device preprocessing handles them)

### No-Calibration Workarounds

When calibration frames are unavailable [64]:
- Sigma-clipping with dithered data removes most hot pixels
- GraXpert handles gradient residuals
- DSS Kappa-Sigma (κ=2, 5 iterations) combined with dithering eliminates hot pixels even without darks [64]

---

## Gaps and Limitations

- **FOSS-specific JWST tutorials are rare**: Most JWST processing tutorials use PixInsight or Photoshop for color mapping. Siril-specific archive processing tutorials are sparse [52][75].
- **Reddit coverage**: No consolidated workflow guides found on r/astrophotography — knowledge is distributed across posts.
- **Video-vs-text**: Many community workflows exist only as YouTube videos without written equivalents.
- **Telescope.Live paywall**: Some tutorials marked "[Free]" imply others require subscription [49].
