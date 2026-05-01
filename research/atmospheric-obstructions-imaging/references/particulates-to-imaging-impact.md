# Particulates → astronomical imaging impact

**Dimension scope:** the physics and empirical mappings that turn airborne
particulate metrics (PM2.5 µg/m³, AOD at 550 nm, pollen grains/m³) into
actionable signals for astrophotography — magnitude of additional extinction
per band, sky brightness change, and Bortle-equivalent shift.

See [citations.md](../citations.md) for full source details.

## The core conversion

The Beer-Lambert law applied to astronomical extinction:

```
Δm (mag/airmass) = 1.086 × τ
```

where `τ` is the optical depth and 1.086 = 2.5/ln(10) [4].

Total atmospheric extinction at zenith:

```
Δm = 1.086 × (τ_Rayleigh + τ_aerosol + τ_ozone) × airmass
```

Rayleigh scattering is wavelength-dependent (∝ λ⁻⁴) and dominates the blue
end. Aerosol extinction is the variable component for transparency planning.

## Wavelength dependence: the Ångström exponent

Aerosol AOD at one wavelength scales to another via [5]:

```
AOD(λ) = AOD(λ₀) × (λ/λ₀)^(−α)
```

where α (the Ångström exponent) characterizes the aerosol size mode:

- **Coarse mode (mineral dust, pollen)**: α ≈ 0–0.5 → near-flat across visible.
- **Fine mode (urban, smoke, sulfate/nitrate)**: α ≈ 1.5–2.5 → strong blue
  preference.
- **Volcanic stratospheric** (sulfate, large after Hunga Tonga): α ≈ 0.5–1.5.

**Worked example** (calculated, marked as derived):

For a fine-mode urban aerosol with α = 1.5 and AOD(550 nm) = 0.20, applying
AOD(λ) = AOD(550) × (λ/550)^(−1.5) and Δm = 1.086 × AOD:

| Band | Wavelength | AOD (est.) | Δm at zenith (mag, est.) |
|---|---|---|---|
| B | 440 nm | 0.280 | 0.30 |
| V | 550 nm | 0.200 | 0.22 |
| OIII | 500 nm | 0.231 | 0.25 |
| Ha | 656 nm | 0.154 | 0.17 |
| SII | 671 nm | 0.148 | 0.16 |

For a coarse-mode dust event with α = 0.2 and AOD(550 nm) = 0.20, all bands
see approximately equal additional extinction (~0.21–0.22 mag, est.).

**Practical consequence**: OIII filters at 500 nm see more extinction than
Ha at 656 nm during fine-mode aerosol events (urban PM2.5, smoke), but
nearly equal extinction during coarse-mode events (dust, pollen).

## Observatory baseline extinction (calibration anchors)

| Site | Elevation | V-band median | Source |
|---|---|---|---|
| **Cerro Paranal** (ESO VLT) | 2,635 m | k_aerosol₀ = 0.013 ± 0.002 mag/airmass at reference wavelength; α = −1.38 ± 0.06 [1]; total V around 0.15–0.16 mag/airmass | Patat et al. 2011 [1] |
| **Mauna Kea** (SNIFS data) | 4,205 m | V ≈ 0.11, B ≈ 0.19 (per discovery agent extraction; band values not exposed in re-fetch — flagged as DRIFT) | Buton et al. 2013 [2] |
| **ORM (La Palma)** | 2,396 m | V = 0.130 mag/airmass median (1984–2013) [3] | IAC monitoring [3] |

For comparison, a low-elevation observer at sea level under typical eastern
US summer conditions sees **roughly 2–3× the total extinction** of these
high-altitude observatory sites, with the additional component being mostly
aerosol and water vapor (not Rayleigh, which is column-dependent).

## PM2.5 → AOD: the unreliable bridge

The chain `PM2.5 → AOD → magnitude loss` accumulates two large uncertainties.

### Step 1 (PM2.5 → AOD): poorly correlated

- Daily PM2.5/AOD R = **0.03 to 0.60** across 19 stations in China [11].
- η = PM2.5 per unit AOD ranges **7.8 µg/m³ (Hawaii) to 504 µg/m³ (Mongolia)**
  globally, with dust regions ~3× sulfate regions [17] — a 65× span.
- Predictive R for PM2.5 from AOD: 0.49 (AOD only) → 0.74 (+ humidity) → 0.81
  (+ 4 met factors) [11].
- **Above 1.3 km altitude, the relationship breaks**: R² = 0.03–0.21 vs
  0.29–0.54 below; 58% of aerosol scale-height measurements place mass
  above 1.35 km [16].

### Step 2 (AOD → V-band extinction): site-dependent

- Stubbs & Vaz [8]: best-fit narrowband (380–840 nm) extinction modeling at a
  dark site **required zeroing the aerosol scattering term entirely** to
  match observations within 0.013 mag/airmass.
- IAC ORM [3]: at a high-altitude observatory, routine aerosol-driven V-band
  extinction is **<0.075 mag/airmass at 680 nm** outside calima events.

### The Petržala & Kocifaj 2026 model

A dedicated PM2.5-to-AOD model for night sky brightness [9]: achieves
R = 0.998 under controlled conditions, but raw empirical PM2.5/AOD R² is
"well below 0.6" without humidity and PBL-height correction. Three named
scatter sources:

1. Vertical distribution / PBL height
2. Coarse particle fraction (PM10–PM2.5)
3. Aerosol chemical composition affecting refractive index

**For an app, this means**: do not present a single PM2.5 → magnitude-loss
number to the user. Present the column AOD where available (AERONET [73],
CAMS [33], VIIRS) and a separately-flagged PM2.5 health signal.

## Sky brightness (forward scatter) effect

Aerosols redirect light-pollution photons downward via forward Mie scatter,
**increasing zenith sky brightness** even as they decrease direct stellar
flux [10]:

- Reducing aerosol load decreases night sky brightness by **tens of percent**
  near light sources [10].
- Second-order scatter contribution: ≤18% of total [10].

Two competing effects on imaging SNR:

1. **Direct extinction** (reduces target signal — reduces numerator).
2. **Sky background increase** (raises noise floor — increases denominator).

Both worsen SNR. The forward-scatter effect is stronger near cities; under
truly dark skies, direct extinction dominates.

**Narrowband filters reject most aerosol-scattered skyglow** because the
scattered light pollution is broadband; narrowband filters pass only the
target-line light. This means narrowband imaging is sensitive to aerosol
direct extinction but largely immune to aerosol-amplified skyglow. Net:
narrowband under aerosol load ≈ extinction-only impact, with Ha (656 nm)
moderately less affected than OIII (500 nm) under fine-mode aerosols [5].

## Volcanic stratospheric aerosol — magnitude scale

From Pinatubo 1991 case [86]:

- Globally averaged stratospheric AOD: **0.10–0.15 for 2 years** post-eruption.
- Peak local: **0.40** in late 1992.
- 3-year persistence above background.

Translated to extinction:

- Global avg AOD 0.12 → +0.13 mag/airmass at zenith (calculated, est.).
- Local peak 0.40 → +0.43 mag/airmass at zenith (calculated, est.); +0.86
  mag/airmass at airmass 2 (est.).

Hunga Tonga 2022 produced the largest stratospheric AOD perturbation since
Pinatubo — particles 2× larger than typical volcanic [90], aerosol formation
3× faster than typical due to humidification [88]. ESO Messenger 190 [89]
reports VLT/Paranal twilight calibration showed sky brightness change persisting
>12 months (extracted by discovery agent; could not be re-verified in-session
due to PDF parse failure).

## Pollen optical extinction

Pollen grains are large (10–100 µm) — geometric optics regime where
Q_ext → 2 (extinction cross-section ≈ 2× geometric cross-section).
Wavelength dependence is near-zero (α ≈ 0), so pollen affects all bands
roughly equally [from Dim5 Discovery citing AMT 2022 ragweed/birch/pine
scattering matrix study].

Single scattering albedo for studied pollen types (Olea, Fraxinus, Populus,
Salix): **0.038–0.058** [from Dim5 Discovery citing ScienceDirect 2023 cavity
ring-down spectroscopy study]. Strongly forward-peaked.

Lidar evidence [51]: pollen can account for 25–97% of aerosol optical depth
during spring daytime peak emission events. **However, this is a daytime
phenomenon — the column collapses after ~18:00 LT** for most pollen species
[51]. Implication: the atmospheric-transparency impact of pollen for night
imaging starting after astronomical twilight is small for SE US pine; more
significant for ragweed which has a non-trivial nighttime ground-level signal
[52].

**No paper found gives a direct grains/m³ → AOD or → magnitude conversion**
for pine pollen specifically. This is a real scientific gap.

## SQM / NELM / Bortle relationships

Sky Quality Meter (SQM) reads in mag/arcsec². Approximate Bortle mapping:

- Bortle 1 (pristine): SQM ≥ 21.7 mag/arcsec²
- Bortle 4 (rural/suburban transition): SQM ≈ 20.0
- Bortle 7 (suburban): SQM ≈ 18.5

(One Bortle class ≈ 0.9–1.0 SQM unit, scale non-uniform.)

NELM ≈ (SQM − 8.89)/2 + 0.5 for SQM > 20.5.

Aerosol effects on SQM are bidirectional: extinction dims stars (raises NELM
threshold), but forward scatter brightens background (lowers SQM). Both
worsen Bortle equivalent. A novel 2025 SQM aerosol-retrieval algorithm
[from Dim5 Discovery citing ScienceDirect 1309-1042/2025] enables AOD
inference from SQM at La Silla and Asiago, validated against MODIS.

**Counter-perspective** [from Dim5 Counter, citing Cloudy Nights and S&T]:
the amateur term "transparency" frequently means cirrus/humidity, not
aerosols. Practitioners report cirrus as the dominant transparency killer.
Routine urban PM2.5 (10–35 µg/m³) is rarely the rate-limiting factor in
actual observing reports.

## Recommended app decision logic

For a single-night transparency forecast:

1. Pull column AOD at 550 nm from AERONET nearest station [73] (15-min
   cadence) **OR** CAMS forecast [33] (~40 km, 5-day) **OR** VIIRS NRT
   [from Dim4 Discovery] (~6 km, daily).
2. Apply Ångström exponent assumption based on the dominant aerosol type
   that day:
   - Wildfire smoke active → α = 1.7 (fine-mode default) [5]
   - Saharan dust active → α = 0.3 (coarse-mode default) [5]
   - Routine urban → α = 1.5 (fine-mode default) [5]
3. Convert to per-band extinction via Δm = 1.086 × AOD(λ).
4. Display both V-band Δm (broadband planning) and Ha/OIII Δm (narrowband
   planning), with explicit Ångström-exponent caveat.
5. Surface column AOD as the primary number; demote PM2.5 to a secondary
   "surface air quality" indicator (it is a poor transparency proxy [11, 16]).

## Gaps and limitations

- **Buton 2013 V/B/R/I band-specific values** [2] could not be exposed in
  the in-session re-fetch summary — those numbers come from discovery-agent
  extraction and are flagged as DRIFT.
- **No paper found** quantifying Pinatubo or Hunga Tonga astronomical impact
  in standard photometric magnitudes (B/V/R band extinction increase) for
  amateur imaging conditions. The direct evidence is observatory-tier
  (Paranal, Mauna Kea) and not always directly reported in mag units.
- **Pollen → AOD conversion at the grains/m³ → 550-nm-AOD level** is not
  available in any paper found.
- **Hygroscopic growth correction f(RH)** for AOD inference (rather than
  surface visibility) is not validated for astronomical use in any source
  found.
- **Narrowband (Ha 656 nm vs OIII 500 nm) differential extinction** under
  smoke/dust has not been empirically validated in the amateur literature.
  The Ångström-exponent calculation is physics-correct but unsupported by a
  controlled study.
