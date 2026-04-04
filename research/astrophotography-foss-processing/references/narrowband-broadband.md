# Narrowband and Broadband Processing Techniques

Dimension 6: Processing different filter data using FOSS tools.

All sources cited to [citations.md](../citations.md).

---

## Broadband Processing (LRGB)

### Overview

LRGB uses four channels: Luminance (detail), Red, Green, Blue (color) [43]. Siril's `rgbcomp` command accepts up to 8 input images [43].

### Workflow in Siril

1. Stack each filter (L, R, G, B) independently using monochrome preprocessing scripts [40]
2. Apply linear-match equalization before combining [43]
3. Assemble using RGB Composition tool [43]
4. Apply Photometric Color Calibration (PCC) or SPCC on the combined image [78]

### Color Calibration

**PCC (Photometric Color Calibration)** [78]:
- Requires plate-solved, linear (pre-stretch) image
- Uses star photometry to balance R/G/B channels

**SPCC (Spectrophotometric Color Calibration)** — new in Siril 1.4 [3][78]:
- Uses Gaia DR3 spectral data + sensor QE curves + filter transmittance curves
- More accurate than PCC, especially for narrowband-enhanced broadband
- Requires local or remote SPCC catalog (v1.4.2 adds caching) [2]

---

## Narrowband Palettes

### Channel Assignments

| Palette | Red Channel | Green Channel | Blue Channel | Use Case |
|---------|-------------|---------------|-------------|----------|
| **SHO (Hubble)** | SII | Ha | OIII | Full three-filter narrowband [53][99] |
| **HOO (Bicolor)** | Ha | OIII | OIII | Two-filter narrowband [44][59] |
| **Modified SHO** | Ha | 0.9×OIII + 0.1×Ha | OIII | Softer green channel [53] |

### SHO (Hubble Palette) in Siril

Classic SHO PixelMath [99]:

```
R = SII
G = Ha
B = OIII
```

The classic mapping produces heavy green dominance from Ha emission [99].

**Modified SHO** (Astrowheep) [53] — replaces the G channel to reduce green dominance:

```
R = Ha
G = 0.9 * OIII + 0.1 * Ha
B = OIII
```

Note: The Astrowheep modification also maps R=Ha instead of R=SII, making it usable with only Ha+OIII data (no SII filter required) [53].

Full SHO requires a monochrome camera with three separate filters (Ha, OIII, SII) [99]. OSC cameras with dual-narrowband filters (L-eXtreme, L-eNhance) can only capture Ha + OIII natively — SII requires a separate filter or synthetic approximation [104].

### HOO (Bicolor) in Siril

Siril PixelMath [44][59]:

```
R = Ha
G = OIII
B = OIII
```

Produces natural-looking emission nebulae with warm Ha reds and cool OIII blues/teals [59].

---

## OSC Dual-Narrowband Processing

OSC (one-shot color) cameras with dual-narrowband filters require channel extraction [94][104]:

### Siril OSC_Extract_HaOIII Script [94]

1. Script extracts Ha from red CFA pixels, OIII from combined green+blue CFA pixels
2. Outputs: `Ha_result.fit` and `OIII_result.fit`
3. Available in Image Processing → Extraction → Split CFA Channels (manual path)

### Post-Extraction Workflow [104]

After running OSC_Extract_HaOIII:
1. Register and stack Ha and OIII sequences separately
2. Apply GraXpert gradient removal to each
3. Combine using PixelMath (HOO or modified SHO)
4. StarNet star removal on starless layer
5. Stretch with GHS or Veralux [97]
6. Recompose stars

### Synthetic SII from OSC Data

Full SHO from OSC dual-band data is possible via synthetic SII approximation. The x-bit-astro-imaging blog (2024) demonstrates creating "every synthetic narrowband palette" from OSC RGB data without PixInsight. Quality is debated in the community [104].

---

## Combining Narrowband with Broadband

### Ha-Enhanced RGB

Adding Ha data to broadband RGB strengthens nebula emission [49][50]:

**Method 1 — Max blend** [49]:
```
R = max(Red, Q * Ha)
```
Where Q = 1.5 (adjustable). Simple, preserves whichever signal is stronger. 13-minute tutorial by Alexander Curry [49].

**Method 2 — Continuum subtraction** [50]:
```
Ha_pure = Ha - Q * (Red - median(Red))
```
Then blend Ha_pure into red channel. Removes stellar continuum from narrowband, isolating pure emission signal [50][96].

Deep Space Astro provides a Python script for automated continuum subtraction in Siril [96].

### Starless Processing for Blending

Best practice for narrowband+broadband combination [49][53]:
1. Remove stars from both datasets using StarNet V2
2. Blend narrowband into broadband on starless images
3. Recompose stars from one dataset only (avoids doubling)

---

## Processing JWST/Hubble Archive Narrowband Data

### JWST Filter Notation [20][67]

JWST uses F-number notation: F090W (wide), F200M (medium), F335N (narrow).
- **W** = wide band (broadband equivalent)
- **M** = medium band
- **N** = narrow band (e.g., F187N = Paschen-alpha, F470N = H₂)

### Workflow with FOSS Tools [67][75]

1. Download Stage 2 `_i2d.fits` from MAST [20]
2. Open in SAO DS9 (free) [67] or Siril [75]
3. Assign narrowband filters to color channels based on wavelength
4. Adjust scale, contrast, and color balance
5. Export as color composite

The Isolated Planets Archive tutorial [67] is the most current free-tool-specific resource for JWST narrowband processing (May 2025). PIXLS.US thread [75] covers Siril-specific handling, noting JWST FITS cubes require the "allow different sizes" option.

---

## Stretching Techniques in Siril

### Generalized Hyperbolic Stretch (GHS) [45]

Non-linear stretch that provides fine control over where in the tonal range the stretch is applied. Preferred over simple histogram stretch for deep sky [45].

### Veralux Scripts [97]

Community-contributed stretching scripts available in the official siril-scripts repository [97]. Includes Hypermetric Stretch variant. Discussed on AstroBin forums and Cloudy Nights [58].

---

## Gaps and Limitations

- **Siril-only SHO tutorials sparse**: Most monochrome SHO tutorials lean on PixInsight for combination; Siril-only SHO resources are less prevalent [53].
- **SII from OSC quality disputed**: Synthetic SII from dual-band data is a workaround with community-debated quality [104].
- **SPCC coverage thin**: SPCC was introduced December 2025 (Siril 1.4.0) [3]; tutorial coverage is still emerging [95].
- **Telescope.Live paywall**: Some narrowband tutorials may require subscription [49].
- **Siril readthedocs 403**: SPCC and extraction documentation was inaccessible to fetchers [78].
