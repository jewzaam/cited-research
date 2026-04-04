# Public Domain Deep Sky Data Sources

Dimension 1: Where to obtain free raw deep sky imaging data for processing practice.

All sources cited to [citations.md](../citations.md).

---

## Institutional Science Archives

| Archive | URL | Data Types | Formats | Registration | Calibration Frames |
|---------|-----|-----------|---------|-------------|-------------------|
| MAST (STScI) | archive.stsci.edu [19] | JWST, Hubble (all instruments) | FITS (4 processing levels) | None for public data | Yes — all calibration products archived [20] |
| ESA Hubble (eHST) | hst.esac.esa.int [21] | Mirrors MAST HST data | FITS | None for public data | Yes |
| ESASky | sky.esa.int [22] | Hubble, Herschel, XMM-Newton, Gaia, Planck | FITS | None | 500,000+ images |
| ESA/Hubble Education | esahubble.org [23] | Curated educational datasets | PSD + FITS | None | N/A (curated) |
| NOIRLab | astroarchive.noirlab.edu [24] | 40+ telescope/instrument combos | .fits.fz (compressed) | None for public | Yes (alongside science data) |
| SDSS DR18 | sdss.org/dr18 [25] | Photometric + spectroscopic survey | FITS | None | Calibrated frames provided |
| ESO Archive | archive.eso.org [26] | VLT, La Silla (~20M files) | FITS | Registration required | After 1-year proprietary period. CC-BY |
| Chandra CDA | cxc.harvard.edu/cda [27] | X-ray data | FITS | None | N/A |
| Chandra OpenFITS | chandra.harvard.edu/photo/openFITS [28] | Curated X-ray sets | FITS | None | With tutorials |

### JWST Data Access Detail

JWST data is available through MAST in four processing stages [20]:

1. **Stage 0 (Raw)** — spacecraft output converted to FITS
2. **Stage 1** — count-rate images with detector corrections
3. **Stage 2** — fully calibrated individual exposures
4. **Stage 3** — combined final products per observing mode

Search interfaces: MAST Portal, MAST JWST Search, MAST API (programmatic), exo.MAST (exoplanet-focused) [20].

For astrophotography processing, Stage 2 `_i2d.fits` files are the typical starting point — already calibrated, ready for background extraction and color mapping [52].

---

## Remote Observatory / Commercial with Free Tiers

| Source | URL | Free Offering | Formats | Calibration |
|--------|-----|---------------|---------|-------------|
| Telescope Live | telescope.live [32] | Curated sample datasets (no signup for samples) | FITS | Yes — Calibration Frame Archive |
| Deep Sky West | deepskywest.com | Free tier: calibrated masters only | FITS | Masters only (not individual raws) |

Telescope Live hosts 122,000+ images (7,000+ hours of observations) from professional dark-site telescopes [32]. Full archive requires subscription; free tier scope needs direct verification.

---

## Community / Amateur Data Sources

| Source | URL | What's Available | Formats | Calibration |
|--------|-----|-----------------|---------|-------------|
| MOANA Project | erellaz.com [29] | Deep-sky broadband + narrowband (Ha, OIII, SII) | Raw FITS | Not specified |
| AstroBackyard | astrobackyard.com [30] | 7 stacked nebula images | TIFF | N/A (pre-stacked) |
| AstroBackyard DSS Files | astrobackyard.com [31] | Practice data for DSS tutorial | Various | Yes |
| Matt Dieterich | mattdieterich.com [37] | Professional observatory data | Calibrated/stacked | N/A |
| Light Vortex Astronomy | lightvortexastronomy.com [34] | Pre-processed 32-bit FITS (Drizzled 2×) | FITS | N/A (pre-processed) |
| Astropix.com | astropix.com [35] | Canon CR2 raws (M31, M42, M45, M13) | CR2 | N/A |
| PhotographingSpace | photographingspace.com [36] | Hubble archive tutorials + shared data | FITS | N/A |
| Cloudy Nights Thread | cloudynights.com [33] | CR2 raws (M31, M42, M45, M46/47, M13) ~1 GB | CR2 | Darks + bias included |

### MOANA Project Detail

The MOANA Project [29] is among the most compelling free datasets found:

- **Telescope**: 254mm (10-inch) at Dark Sky Observatory, Fort Davis, TX
- **Camera**: ASI 1600MM (upgraded to QHY268M)
- **Resolution**: 0.591 arcsec/pixel, FOV 45′ × 35′
- **Filters**: Baader CMOS-optimized RGB + 6.5nm narrowband (Ha, OIII, SII)
- **License**: Creative Commons with attribution
- **Coverage**: Deep-sky objects, exoplanet transits, supernovae follow-up, asteroid light curves, comets

Project concluded January 2024 but archive remains accessible [29].

---

## Gaps and Limitations

- **Calibration frame availability varies**: Institutional archives (MAST, ESO) include full calibration products, but community sources often provide only stacked or pre-calibrated data [30][37].
- **Community hosting fragility**: Cloudy Nights external links and Google Drive shares age out over time [33][34][35].
- **AstroBin raw repository**: AstroBin is primarily for finished images; raw data sharing is community-driven and fragmented across forum posts.
- **SDSS is survey data**: Better suited for catalog work than traditional deep-sky processing [25].
- **MOANA longevity unconfirmed**: Archive appears accessible but the project concluded in 2024 [29].
