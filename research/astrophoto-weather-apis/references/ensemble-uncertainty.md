# Ensemble Forecasts and Uncertainty Signals

**Dimension covered:** Probabilistic cloud-cover forecasting via ensembles. Ensemble systems (GEFS, ECMWF ENS, HREF, ICON-EPS, MOGREPS, NAEFS), API access patterns for probabilistic cloud products, and calibration / skill scoring.

Sources: [`citations.md`](../citations.md).

## Headline finding

**Surfacing "70% chance of clear" requires per-member ensemble cloud cover and post-processing — neither is fully available from free public APIs as a packaged product.**

- **Per-member access** is available via Open-Meteo Ensemble API (free, non-commercial) for ICON-EPS, GFS Ensemble (31 members), and ECMWF IFS (51 members) [103]. Cloud cover is exposed per member.
- **Probability product (`cloud_cover_probability`) is NOT exposed** by Open-Meteo. GitHub issue #349 proposes the syntax but is unimplemented [104]. The workaround is client-side: count members with cloud cover ≤ threshold, divide by total.
- **ECMWF Open Data ENS** provides per-member TCC (and LCC/MCC/HCC) at 0.25° free under CC-BY-4.0 [7], [99], [102] — but no `type=ep` probability product for cloud exceedances exists in the current open-data tier (probability products cover precipitation and wind gusts).
- **Cloud cover ensembles are demonstrably worse-calibrated** than temperature/precipitation ensembles. Raw ECMWF cloud cover ENS is "clearly underdispersive" [106], and standard EMOS post-processing fails for cloud cover where it succeeds for other variables [107].

## Ensemble systems comparison

| System | Operator | Members | Resolution | Horizon | Cadence | API cloud variable access | Cite |
|---|---|---|---|---|---|---|---|
| GEFS v12 | NOAA NCEP | 31 (1 control + 30 perturbed) | 25 km | 16 days (35-day extended) | 4×/day | Per-member TCDC via NOMADS / AWS / Herbie | [40], [41] |
| ECMWF ENS | ECMWF | 51 (1 control + 50 perturbed); 101 for extended-range | 9 km (since June 2023) | 360 h (15 days) at 00/12 Z; 144 h at 06/18 Z | 4×/day | Per-member TCC/LCC/MCC/HCC via `ecmwf-opendata` (0.25° free) | [28], [99], [101], [102] |
| HREF | NOAA NCEP | (multi-member: HRRR + ARW + FV3) | ~3 km convection-allowing | 48 h | 00/12 Z (CONUS, HI, Guam); 06/18 Z (AK, PR) | SPC ensemble viewer (graphics); no machine API | [25], [26] |
| ICON-EPS | DWD | 40 | 40 km global / 20 km EU | 180 h (00/12 Z extended); 120 h std; 30 h short runs | 8×/day every 3 h | Open-Meteo Ensemble API (`dwd_icon_eps`) | [35] |
| MOGREPS-G | UK Met Office | 18 | 20 km | 198 h (246 h post-Jan 2026) | 4×/day | AWS Open Data; via Open-Meteo `uk_mo_global_deterministic_10km` (deterministic only — ensemble exposure unconfirmed) | [36], [38] |
| MOGREPS-UK | UK Met Office | 18 | 2.2 km | 126 h | 24×/day | AWS Open Data NetCDF (UK only) | [37] |
| NAEFS | NOAA + Environment Canada | 40 + 2 control (20 GFS + 20 GEM) | 1°×1° (downscaled to 2.5 km CONUS) | 384 h | 2×/day (00/12 Z) | Mean/mode/SD/percentiles (10/50/90); embedded in NWS probabilistic products | [39] |
| GFS Ensemble (Open-Meteo) | NOAA NCEP via Open-Meteo | 31 | (varies) | 7 days hourly (Open-Meteo limit) | 4×/day | `cloud_cover` per member at hourly cadence | [103] |

## Deriving "70% chance of clear" from raw ensemble

Canonical method ([105]):
1. Select a cloud-cover threshold representing "effectively clear" for astrophotography. Operational practice in astrophoto tools suggests TCC ≤ 20% (10–25% range). For thin-cirrus-sensitive imaging, TCC ≤ 10%.
2. For each forecast hour and target lat/lon, retrieve all ensemble members' cloud cover values.
3. Count members with TCC ≤ threshold: `k`.
4. Divide by total member count: `P(clear) = k / N`.
5. **Granularity:** GEFSv12 (31 members) yields probabilities in multiples of ~3.2%; ECMWF ENS (51 members) yields multiples of ~2%.
6. The raw fraction is **not yet calibrated** — see "Calibration problems" below.

Open-Meteo's existing `precipitation_probability` formula uses this exact pattern [105]. Cloud cover probability is not implemented but follows the same logic — a developer can derive it client-side by querying the Ensemble API for all members' `cloud_cover` and applying a threshold.

## Calibration problems specific to cloud cover

### Raw ensembles are underdispersive
**Hemri, Haiden & Pappenberger 2016 [106]** (MWR, peer-reviewed): Raw ECMWF cloud cover ensemble is "clearly underdispersive" at day 3; U-shaped PIT histograms at days 1 and 4. Cloud cover ensemble skill is **"worse than ensemble forecasts of other weather variables."** The discrete/ordinal nature of oktas (9 values: 0–8) makes the standard Gaussian EMOS parametric family inapplicable.

This is **not** a case where temperature/precipitation post-processing carries over. Cloud cover requires fundamentally different methods.

### Standard post-processing fails for spatial coherence
**Dai & Hemri 2021 [107]** (MWR): Univariate post-processing destroys spatial dependence structure of cloud cover. Standard EMOS + ensemble copula coupling (ECC) fails for cloud cover where it succeeds for temperature. Producing spatially realistic cloud scenario maps requires conditional GAN — substantially more complex than typical post-processing.

### Skill drops below persistence at day 3
**Haiden et al. 2015 [86]** (ECMWF Newsletter 143): ECMWF HRES cloud cover skill drops below persistence at approximately **day 3** — earlier than skill loss for temperature, geopotential, wind, or precipitation. Cited repeatedly across the literature as the canonical NWP cloud skill ceiling.

### Cloud cover is bimodal — intermediate probabilities are sparse
Cloud cover has a strong bimodal distribution: more than 60% of observations cluster at 0 or 8 oktas (fully clear or fully overcast). Reliability diagrams for probabilistic cloud forecasts naturally cluster at 0% and 100% probability, with few reliable intermediate probability estimates — the exact regime where "70% chance of clear" would need to live.

This is a **physical property of the atmosphere**, not a calibration artifact, and cannot be fully resolved by post-processing.

### Systematic biases by cloud regime
**Jakob 1999 [108]** (J. Climate): ECMWF reanalysis systematic biases include 10–15% underestimation of extratropical ocean cloud, 10–15% overestimation of trade cumulus, and 15% underestimation of subtropical stratocumulus — biases structural enough to survive into operational forecasts.

**Frontiers 2023 [175]:** ECMWF temperature forecast error correlates with cloud cover error at r = 0.85–0.95 — confirming that cloud misrepresentation is not a fringe issue but propagates broadly into surface forecasts.

### NWP cloud parameterization at peak performance
**BAMS DoD Workshop 2024 [169]:** "NWP microphysical schemes may have reached peak performance at two moments." Subgrid cloud fraction estimation via RH thresholds is "fundamentally inadequate."

**Lamb 2026 [172]** (JAMES): double-moment microphysics shows persistent systematic biases with "relatively minimal benefit" from further sophistication.

## Ensemble post-processing for cloud cover (state of the art)

For developers wanting calibrated cloud cover probability:
- EMOS (Ensemble Model Output Statistics) extended to bounded variables — treats cloud cover as classification, applies parametric distributions or ML classifiers.
- Spatial coherence requires Ensemble Copula Coupling (ECC) after univariate calibration — but standard ECC fails for cloud per [107].
- Conditional GAN (Dai & Hemri 2021 [107]) produces spatially realistic cloud scenarios but requires substantial training infrastructure.
- DWD applies statistical post-processing to ICON-EPS in operational products [35], but the calibrated cloud-cover product is not exposed via a public API.

**No astronomy-targeted weather app reviewed produces a calibrated, reliability-diagram-tested P(clear) from ensemble post-processing.** Astrospheric's "cloud ensemble" [109] shows per-model percentages with color-coded agreement but does not output a calibrated probability number — and the underlying models (RDPS + ICON + GFS + NBM) are not even drawn from an ensemble system per se but from independent deterministic models.

This is an open product gap.

## Practical recommendations for an astrophoto app

1. **For "tonight: yes/no" decisions (1–24 h ahead):** Use deterministic HRRR / GFS / ECMWF cloud cover with HRRR's spin-up caveat (FH0–2). Avoid relying on ensemble probability at this horizon — single-model deterministic skill is what dominates.
2. **For "this week: which night is best?" decisions (1–7 days ahead):** Pull per-member ECMWF ENS via `ecmwf-opendata` (free, CC-BY-4.0). Compute per-hour P(TCC ≤ 20%) client-side. Display as confidence interval, not point probability — and **document explicitly that probabilities cluster at 0 and 100** (intermediate values are sparse).
3. **For uncertainty visualization:** Display per-member cloud cover as a fan/spaghetti plot. This is more honest about ensemble underdispersion than a single probability number.
4. **Avoid surfacing "70% chance of clear" as a calibrated forecast** without measuring reliability against observed clear-sky frequencies for the user's location and time of year. If the app does surface it, label it clearly as "raw ensemble fraction" or similar.
5. **For SE US specifically:** ECMWF ENS at 9 km (since June 2023) is the highest-resolution global ensemble and the best general-purpose probabilistic source. GEFS at 25 km is coarser but free and accessible via NOAA Open Data.

## Gaps and limitations

- **Brier Skill Scores specifically for total cloud cover from GEFSv12 or ECMWF ENS** were not extracted from peer-reviewed sources. Rasp & Lerch 2018 (MWR) and Scheuerer & Möller (MWR) are candidate papers but were paywalled in this research.
- **HREF current member count** post-2021 upgrade (which added HRRR and FV3) was not definitively confirmed in accessible sources [25], [26]. The pre-2021 member count of 10 may no longer be current.
- **ECMWF ENS open data TCC date of addition** is "recent" per multiple search results but the specific date and whether all 50 perturbed members' TCC are exposed (vs only ensemble mean) was not confirmed [7].
- **Open-Meteo `cloud_cover_probability` implementation timeline:** GitHub issue #349 [104] is open without committed timeline. Workaround (per-member query + client-side threshold) is straightforward but adds API calls.
- **NAEFS calibrated cloud cover output** was not confirmed; NAEFS exposes calibrated temperature/precipitation/wind probabilities via NWS, but cloud cover specifically was not verified [39].
- **MOGREPS-G cloud cover variable availability** on AWS Open Data NetCDF was not confirmed in the registry text [38].
- **ICON-EPS regional verification for SE US** vs GEFSv12 (40 km vs 25 km) was not found — no published comparison study.
- **AIFS in Open-Meteo Ensemble API** — whether AIFS exposes ensemble members or only deterministic output was not confirmed.
- The "70% chance of clear" calibration question is identified as an open research/product gap, not solved by available APIs.
