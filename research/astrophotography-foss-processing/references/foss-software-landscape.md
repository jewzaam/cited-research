# Free Open Source Software for Astrophotography (2026)

Dimension 2: Modern FOSS tools for deep sky image processing.

All sources cited to [citations.md](../citations.md).

---

## Core Processing Stack

These three tools form the dominant FOSS deep sky processing pipeline in 2025–2026:

### Siril

| Attribute | Detail |
|-----------|--------|
| **Current version** | 1.4.2 (2026-02-18) [2] |
| **License** | GPL v3 [1] |
| **Platforms** | Windows, macOS (Intel + Apple Silicon), Linux [2] |
| **Repository** | gitlab.com/free-astro/siril [5] |
| **Publication** | JOSS peer-reviewed paper (2024) [6] |

Key features [1][2][3][4]:
- Full calibration/registration/stacking pipeline
- Generalized Hyperbolic Stretch (GHS) [4] (pre-dates v1.4)
- Native StarNet integration [41]

New in v1.4.x [2][3]:
- Proper HST Drizzle algorithm + Bayer Drizzle [3]
- Spectrophotometric Color Calibration (SPCC) using Gaia DR3 [3][78]
- GraXpert integration [7]
- Python scripting system [3]
- PixelMath for narrowband combination [44]
- Astrometric plate solving with distortion correction [79]
- 24 official tutorials (difficulty 0–5) [4]

v1.4.2 specifics: GPU manager improvements, remote SPCC catalog caching, experimental Windows UCRT64 build raising file limit from ~2,048 to 8,192 [2].

### GraXpert

| Attribute | Detail |
|-----------|--------|
| **Current version** | 3.0.2 stable (2024-05-03); 3.1.0rc2 in development [8] |
| **License** | BSD-3-Clause [7] |
| **Platforms** | Windows, macOS (ARM64 + AMD64), Linux [7] |
| **Repository** | github.com/Steffenhir/GraXpert [8] |

Key features [7][8]:
- AI-based background gradient extraction (CNN foreground/background separation)
- AI denoising for linear images (v3.0.0+) [8]
- AI stellar deconvolution (v3.1.0rc2) [8]
- AI object deconvolution for nebulae/galaxies (v3.1.0rc1) [8]
- Traditional methods: RBF, Splines, Kriging [7]
- GPU acceleration: DirectML (Windows), CUDA 12 (Linux), CoreML (macOS) [8]
- Also available as PyPI package `graxpert` [7]
- Discord community at discord.gg/DarkMatters [7]

### StarNet V2

| Attribute | Detail |
|-----------|--------|
| **CLI version** | 2.0.0 [9] |
| **PI plugin version** | 2.1.2-0127 [9] |
| **Source** | github.com/nekitmm/starnet [10] |
| **Platforms** | Windows, macOS, Linux [9] |

Key features [9][10][66]:
- Neural network star removal (convolutional residual encoder-decoder)
- Single-step processing; CLI batch mode available
- Requires AVX-capable CPU [9]
- Input: 16-bit TIF [66]
- Output: starless image in same directory
- Integrated natively into Siril [41][42]
- Linear mode checkbox for processing pre-stretch data

---

## Stacking Tools

### DeepSkyStacker (DSS)

| Attribute | Detail |
|-----------|--------|
| **Current version** | 6.1.0 (2025) [13] |
| **License** | BSD 3-Clause [14] |
| **Platforms** | Windows, Linux, macOS 13.4+ (new in v6.1.0) [13] |

Key features [13][74]:
- Stacking with calibration frames (dark, flat, bias)
- Star detection via Gaussian curve fitting, triangle pattern matching for alignment [74]
- Methods: Average, Median, Kappa-Sigma, Median Kappa-Sigma, Auto Adaptive Weighted Average [74]
- Comet stacking (star-aligned, comet-aligned, hybrid) [74]
- Recommended: 15+ calibration frames per type, Kappa-Sigma clipping for satellite removal [64]

### ASTAP

| Attribute | Detail |
|-----------|--------|
| **Status** | Active (changelog entries through mid-2025) [15] |
| **License** | Free (license type unclear — freeware with open-source components) [15] |
| **Platforms** | Windows, Linux, macOS [15] |

Key features [15]:
- Native astrometric solver using H17/H18 star catalogs
- Image stacking with calibration frames
- FITS viewer and photometry
- Integrates as plate solver with NINA, SGP, APT, Voyager, CCDCiel

---

## Capture and Control

### KStars / EKOS / INDI

| Attribute | Detail |
|-----------|--------|
| **KStars version** | 3.8.1 (2026-02-02) [11] |
| **License** | GPL v2+ [11] |
| **Platforms** | Linux, macOS, Windows; KStars Lite for Android [11] |

EKOS handles: camera control, autofocus, autoguiding, polar alignment, plate solving, filter wheels, dome control. INDI provides hardware abstraction with hundreds of device drivers [11][17].

### PHD2

| Attribute | Detail |
|-----------|--------|
| **Current version** | 2.6.14 (2025-12-09) [12] |
| **License** | BSD [12] |
| **Platforms** | Windows, macOS, Linux [12] |

Multi-star guiding, Guiding Assistant, drift alignment, comet tracking. ASCOM and INDI support [12].

### NINA

| Attribute | Detail |
|-----------|--------|
| **Current version** | 3.2 (2025-11-12) [16] |
| **License** | Mozilla Public License 2.0 [16] |
| **Platforms** | Windows only [16] |

Full imaging sequence automation, plate solving, autoguiding integration, plugin ecosystem [16].

---

## Supporting Tools

| Tool | Purpose | License | Platform |
|------|---------|---------|----------|
| GIMP | Final image editing | GPL | All [105] |
| Astrometry.net | Blind plate solving | Open source | Web + local [18] |
| SAO DS9 | FITS viewer / JWST processing | Open source | All [67] |
| StellarSolver | Local plate solver library | Open source | All [79] |

---

## PixInsight Comparison

No FOSS equivalent matches PixInsight's full feature set. Siril is the closest alternative and has narrowed the gap significantly with v1.4 (SPCC, Drizzle, Python scripting) [105]. Community benchmarks show Siril CLI is faster than PixInsight WBPP for stacking on Apple Silicon hardware [4]. PixInsight ($275 one-time) offers more advanced masking and a larger tutorial ecosystem [105].

---

## Gaps and Limitations

- **ASTAP license ambiguity**: Official distribution is freeware; GitHub repos may be unofficial forks [15].
- **StarNet V2 license**: Source on GitHub but explicit license terms not confirmed on download page [9][10].
- **GIMP astronomy plugins**: gimp-plugin-astronomy suite targets GIMP 2.10; GIMP 3 compatibility unconfirmed.
- **DSS Linux/macOS**: Cross-platform support is new in v6.1.0 and may have rough edges [13].
- **GraXpert onnxruntime issues**: Known compatibility problems on certain Windows 10 systems [8].
