# Source conflict resolution

**Dimension scope:** when AirNow, PurpleAir, OpenAQ, and competing pollen
APIs disagree on the same metric for the same time and place — by 2–3× or
more — what should the app do? Includes EPA correction equations, sensor
calibration biases, and fusion vs. surface-disagreement strategies.

See [citations.md](../citations.md) for full source details.

## The PurpleAir → EPA equivalence equation

The standard correction (Barkjohn et al. 2021 [18]):

```
PM2.5_corrected = 0.524 × PA_cf_1 − 0.0862 × RH + 5.75
```

- Inputs: `PA_cf_1` (CF=1 channel-averaged PurpleAir reading), RH in %.
- Reduces RMSE from 8 µg/m³ to 3 µg/m³ at typical US ambient
  concentrations [18].
- Calibration set: 50 sensors, 16 states, 39 sites — **only 3 rural sites**
  [18].
- Stated boundary: validity at >60 µg/m³ or <−12 °C is uncertain [18].

This is the equation deployed on the AirNow Fire & Smoke Map [57].

## The dust failure (the most actionable counter-finding)

Jaffe et al. 2023 [19], peer-reviewed: the corrected PurpleAir data are
accurate in smoke (slope 0.99 at Keeler CA) and urban (slope 1.00) but
**too low by factor 5–6 in dust** (slope 5.6 at Keeler CA).

**Implication for an app**: applying Barkjohn uniformly during a Saharan
dust event will display PM2.5 ~1/5 of the actual value. A user in NC during
mid-July might see "PurpleAir says 4 µg/m³" when the true surface PM2.5 is
20 µg/m³, with no warning.

**Mitigation**: detect aerosol type (dust vs smoke vs urban) before applying
correction. Possible signals:

- CAMS dust AOD [33] active in the region → suspect dust → apply different
  multiplier or fall back to AirNow regulatory data [23].
- Active wildfire detection [56] within plume distance → suspect smoke →
  apply piecewise correction at high concentrations.
- Neither active → urban/routine → apply Barkjohn directly.

## High-concentration smoke breakdown

The Barkjohn equation [18] was derived primarily from urban ambient. For
extreme smoke (>300 µg/m³) [22]:

- Only 5 of 15 smoke-impacted sites met EPA performance targets at hourly
  averages.
- Standard equation underestimates above 300 µg/m³.
- A piecewise quadratic correction has been proposed for >300 µg/m³ but
  introduces a positive bias at 150–300 µg/m³.
- The two correction approaches **give opposite error directions** at the
  concentration levels where accurate data matter most.

## Plantower hardware revision

A silent hardware change to the PMS5003 around June 2021 [20] introduces a
~3 µg/m³ low bias for concentrations <16 µg/m³. **More than 10% of the
PurpleAir outdoor network is affected without per-sensor flag.**

For an astrophotography app, the 5–15 µg/m³ band is exactly where the
"excellent" vs "good" transparency distinction lives — this is the wrong
place to have a silent cohort-level bias.

## High-RH bias

Plantower sensors over-estimate at RH > 65–70% due to hygroscopic particle
growth [20, 21]. The Barkjohn correction includes a humidity term but at
very high concentrations + high RH, the correction's behavior is
"unclear" [21].

## OpenAQ pass-through behavior

Per OpenAQ documentation and discovery agent extraction [26]: data shared
"without modification (other than standardizing format)." No QA/QC at
ingestion. Sensor type metadata exists but is inconsistently populated.

A 2025 PMC study (per Dim8 counter agent) documented an OpenAQ EEA adapter
bug where stale `value_datetime_inserted` caused most hourly readings to
be discarded silently — German/Estonian station coverage dropped from
hourly to ~2 readings per day. **Infrastructure-level data loss is a
real risk that no automated check would catch.**

## NowCast vs raw temporal alignment

AirNow's NowCast [25]:

- 12-hour weighted average with weight = 1 − (range/max), minimum 0.5.
- Approaches 12-hour average when stable; approaches 3-hour average when
  rapidly changing.
- Updated August 2013 to be more responsive to wildfire events.

When comparing AirNow (NowCast-derived) to PurpleAir (raw 2-min averages),
the temporal-averaging mismatch alone produces apparent disagreement that
has nothing to do with sensor error. **Always align time windows before
comparing values across sources.**

## FRM/FEM regulatory monitor heterogeneity

Even within the "regulatory" tier, there is non-trivial divergence [from Dim8
Discovery citing MDPI 2073-4433/15/8/978]:

- **More than 50% of FEM monitors have FEM/FRM ratios > 1.1.**
- **~30% have FEM/FRM > 1.2.**
- Mean positive bias of FEM vs FRM is ~22%.

**Implication**: even before considering low-cost sensors, the regulatory
"ground truth" itself is heterogeneous. A 22% inter-monitor bias is
comparable to the scale of PurpleAir vs AirNow divergence often blamed
entirely on the low-cost sensor.

## Pollen API agreement (or lack thereof)

**No peer-reviewed head-to-head accuracy study compares Tomorrow.io,
Ambee, and Google Pollen.** Independent accuracy findings are weak:

- 2025 PMC study [48]: AccuWeather concordance with automated pollen
  monitors 7% (grass) – 56% (mold). The Weather Channel: 29% (grass) – 34%
  (ragweed). **No statistically significant association** in Fisher exact
  tests.
- 2024 Healio survey of public pollen websites in 5 US cities [105]:
  uniformly low accuracy.

**The implication**: fusing Ambee + Tomorrow.io + Google Pollen does not
average toward truth. It averages multiple poor forecasts.

The sources of disagreement are fundamental [42, 44]:

1. No standardized pollen measurement network (Hirst/Burkard manual stations
   are sparse and slow to report).
2. Most APIs extrapolate via models from sparse counter data.
3. Different APIs use incompatible taxonomic aggregations.
4. Timing of counts vs forecast periods differs.

## Spatial fusion methods

For PM2.5 specifically, peer-reviewed methods exist [from Dim8 Discovery]:

| Method | Strengths | Weaknesses |
|---|---|---|
| **Kriging (Bayesian / detrended)** [101] | Best linear unbiased estimate; quantifies uncertainty | Requires statistical stationarity (violated near point sources) |
| **IDW / Modified IDW** [103] | Simple, fast, no stationarity assumption | No uncertainty estimate; modified IDW reduces MAPE/RMSE 10–12% over standard |
| **Optimum Linear Data Fusion** [102] | Hybrid sensor + station fusion with uncertainty | Complex implementation |
| **Conflict-weighted fusion** [104] | Lower weight to sources that disagree most | Requires pairwise conflict measurement |
| **Bayesian multi-source** [101] | Theoretical framework with uncertainty quantification | Independent-error assumption often violated |

**Critical caveat from spatial statistics** [from Dim8 Counter agent
extraction]: ignoring spatial autocorrelation artificially narrows confidence
intervals. **Fused estimates can appear more certain than the underlying data
supports.** A "confident" fused AQI with a tight uncertainty band is likely
overstating predictive reliability.

## Recommended app architecture for source conflict

Three options, in order of recommended-ness:

### Option A: Surface disagreement, do not fuse

When AirNow regulatory and corrected PurpleAir disagree by >50%, display
**both values with provenance**, e.g.:

> Surface PM2.5: AirNow (regulatory) reads 8 µg/m³, PurpleAir (corrected)
> reads 22 µg/m³. CAMS dust AOD is elevated — PurpleAir may underestimate
> by 5× during dust events.

This pushes interpretation to the user but is honest about uncertainty.

### Option B: Hierarchical fallback

1. If AirNow station within 25 km, use AirNow.
2. Else if EPA-corrected PurpleAir sensors within 10 km with A/B agreement,
   use median of available.
3. Else use OpenAQ aggregator (with sensor-type filter to exclude low-cost
   if possible).
4. Else use CAMS gridded reanalysis [33] (low spatial resolution caveat).

### Option C: Bayesian fusion (research-grade)

Implement a per-source error model with conflict-weighted fusion [104] and
present the posterior with uncertainty band. Most rigorous; highest
implementation cost; carries spatial-statistics overconfidence risk.

**Recommendation**: ship Option B in v1, add Option A "show disagreement
when present" as v1.1, defer Option C indefinitely.

## What to surface to the user

For an astrophotography planning context:

1. **Single primary number** for the user's "is tonight worth it?" question
   (use the Option B hierarchy).
2. **A confidence/uncertainty indicator** if sources disagree materially.
3. **Aerosol-type context**: if dust or smoke is active, flag that the
   PurpleAir correction may be wrong.
4. **Avoid presenting fused estimates as if they were measurements** —
   distinguish observed values from interpolated/modeled ones.

## Gaps and limitations

- The PurpleAir A/B channel agreement threshold (5 µg/m³ absolute or 70%
  relative) is a community standard; the specific thresholds were not
  re-fetched and rely on Dim8 Discovery agent extraction.
- The FEM/FRM 22% mean positive bias claim is from a single MDPI 2024 paper
  (per Dim8 Discovery); the breakdown by FEM instrument class was not
  retrieved.
- The CAMS organic-matter 3× overestimation in North America (per Dim2
  Counter agent) is from a 2024 ESSD preprint and would need direct
  verification before integrating CAMS at face value.
- No peer-reviewed paper found provides head-to-head accuracy comparison
  of Tomorrow.io, Ambee, Google Pollen — the disagreement-resolution
  framework for pollen rests on inference from poor accuracy of consumer
  apps generally [48].
