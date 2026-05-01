# Satellite Imagery and Nowcasting

**Dimension covered:** Observed-now cloud cover from satellite (GOES ABI L2 cloud products) and nowcasting from MRMS / HRRR-Smoke. AWS S3 access via NOAA Open Data Dissemination. Cadence, latency, accuracy, and limitations relative to NWP forecast.

Sources: [`citations.md`](../citations.md).

## Headline finding

**For the next 0–3 hours over the Southeast US, satellite-observed cloud (GOES-19 ABI L2 Clear Sky Mask at 5-min CONUS cadence) beats NWP cloud forecasts.** Beyond ~3 hours, optical-flow extrapolation degrades and NWP takes over.

**Critical 2025 update [151]:** GOES-19 became operational GOES-East on April 7, 2025, replacing GOES-16. Real-time SE US data should be sourced from `noaa-goes19` AWS S3 bucket. The user's planning topic (`ap-topics1.md`) names GOES-16 — that is now historical.

But satellite cloud products have substantial blind spots: **GOES-16 ABI Clear Sky Mask daytime clear-sky accuracy is only 66.6%** (1 in 3 clear pixels misclassified as cloudy) [161], and the 1.378 µm cirrus band is **daytime-only** [163], [164] — thin cirrus invisible to nighttime satellite is exactly what astrophotographers care about most for transparency.

## GOES-East status as of April 2026

| Satellite | Position | Operational role | S3 bucket |
|---|---|---|---|
| GOES-19 | 75.2°W | **Operational GOES-East since April 7, 2025** [151] | `noaa-goes19` |
| GOES-16 | (drift / backup) | Demoted to backup | `noaa-goes16` (historical only) |
| GOES-18 | ~137.2°W | Operational GOES-West | `noaa-goes18` |
| GOES-17 | (decommissioned) | (Was GOES-West; replaced by GOES-18) | `noaa-goes17` (historical) |

For SE US real-time cloud monitoring, **use `noaa-goes19`** [149], [151].

## ABI scan cadence (Mode 6, operational since April 2, 2019)

| Sector | Cadence | Cite |
|---|---|---|
| Full Disk | every 10 min | [152] |
| CONUS | **every 5 min** | [152] |
| Mesoscale (one of two domains) | every 60 sec | [152] |
| Mesoscale (single domain) | every 30 sec | [152] |

GOES-16 used Mode 6A; GOES-17 used Mode 6M. GOES-19 inherits the same operational scan strategy.

## ABI Level 2 cloud products

| Product | Acronym | Resolution | Cadence (CONUS) | DOI | Archive Start | Cite |
|---|---|---|---|---|---|---|
| Clear Sky Mask | ACM | 2 km | 5 min | 10.7289/V5SF2TGP | 2017-04-19 | [153] |
| Cloud Top Phase | ACTP | 2 km | 5 min | 10.7289/V5NP22QW | 2017-05-16 | [154] |
| Cloud Top Height | ACHA | 2 km (upgraded 2023-03-24; was 10 km) | 5 min | 10.7289/V5HX19ZQ | 2017-05-16 | [155] |
| Cloud Top Temperature | ACHT | 2 km (inferred from ACHA upgrade) | 5 min | (not retrieved) | (not retrieved) | (gap) |

### ACM (Clear Sky Mask)
- 4-class output: clear / probably clear / probably cloudy / cloudy [156].
- Uses 9 of 16 ABI spectral bands.
- Valid day and night.
- Algorithm: bi-spectral IR + visible reflectance combination.

### ACTP (Cloud Top Phase)
- Phase categories: warm liquid water (T>273 K), supercooled liquid water (T<273 K), mixed phase, ice phase, plus clear sky and unknown [157].

### ACHA (Cloud Top Height)
- Retrieves height, temperature, and pressure simultaneously from ABI IR bands [157].
- Resolution upgraded to 2 km on March 24, 2023 (was 10 km Full Disk/CONUS, 4 km Mesoscale) [155].

### Caveat: experimental vs operational status
NOAA STAR pages [156], [157] carry a caveat that products are "experimental use only and not delivered on an operational (24/7) basis." NCEI archival records do **not** carry this caveat — the archive is operational; the STAR visualization/experimental server is not. For an app, the AWS S3 archival data via NODD is the operational path.

## AWS S3 access (NOAA Open Data Dissemination)

| Aspect | Detail | Cite |
|---|---|---|
| Region | us-east-1 | [149], [150] |
| Authentication | None — `--no-sign-request` works for anonymous access | [149], [150] |
| Path template | `<ProductPrefix>/<Year>/<DayOfYear>/<Hour>/<Filename>.nc` | [150] |
| Filename pattern | `OR_ABI-L2-ACMC-M6_G19_s<start>_e<end>_c<creation>.nc` (M6 = Mode 6, G19 = GOES-19) | [150] |
| Format | NetCDF4 | [153]–[155] |
| SNS notification | `arn:aws:sns:us-east-1:123901341784:NewGOES19Object` | [149] |

### Product prefix examples
- `ABI-L2-ACMC` — Clear Sky Mask, CONUS sector
- `ABI-L2-ACMF` — Clear Sky Mask, Full Disk
- `ABI-L2-ACMM1` / `ABI-L2-ACMM2` — Clear Sky Mask, Mesoscale (1 or 2)
- `ABI-L2-ACHAC` — Cloud Top Height, CONUS
- `ABI-L2-ACTPM1` — Cloud Top Phase, Mesoscale 1

The fixed S3 path structure makes it trivially scriptable: for "current cloud over SE US right now," fetch the most recent ACMC file in the past 5 minutes, parse the NetCDF, extract the cloud mask for the user's lat/lon.

### Egress costs
GOES S3 buckets are free to access. Egress to **AWS-internal services in us-east-1** (e.g., Lambda, EC2 in us-east-1) is **free**. Egress to the public internet is billed at standard AWS rates (~$0.09/GB). For an indie astrophotography app deploying serverless, hosting the satellite-processing function in us-east-1 keeps egress costs at zero.

## Documented ABI cloud-product accuracy and limitations

### Tzallas et al. 2020 — ACM vs CALIPSO [161]
- Overall ACM accuracy: **86.0%**.
- Cloud detection: 90.9%.
- **Clear-sky detection: only 74.8%** (1 in 4 clear pixels misclassified as cloudy).
- **Daytime clear-sky drops to 66.6%** — 1 in 3 clear pixels misclassified as cloudy.
- Nighttime cloud detection: 85.8%; nighttime clear: 82.5%.
- Most missed clouds (false negatives) have tops within 2 km AGL, peaking near 1 km — these are boundary-layer clouds most likely to obscure telescope seeing.
- Performance degrades north of 36°N in winter daytime.

For an SE US astrophotography app at 32–36°N latitude, the daytime false-cloudy rate is operationally significant: the ACM may report partly cloudy when it's actually clear. This drives toward **using ACM as a "definitely cloudy" filter** rather than a "definitely clear" filter — false-cloudy is more common than false-clear, so ACM-reported cloudy is moderately reliable, while ACM-reported clear is less so.

### Sherwood et al. 2004 — convective cloud top height bias [162]
- GOES-8 thermal IR underestimates deep convective cloud tops by **~1 km on average** vs CRYSTAL-FACE CPL lidar.
- Up to 2 km low for the tallest cells.
- Physical cause: sub-cloud-top emission through cloud gaps inflates brightness temperature, lowering the inferred height.
- The bias is fundamental to IR retrieval, not instrument-specific — applies to GOES-19 ACHA.

### Thin cirrus blind spot at night [163], [164]
- The ABI 1.378 µm "cirrus" band operates exclusively on **solar backscatter** and is limited to daytime (SZA < 80°).
- At night, GOES reverts to thermal IR for cirrus detection; optically thin cirrus (optical depth < ~0.3) has minimal thermal contrast against the upper troposphere and is frequently missed.
- For astrophotography, thin cirrus invisible to nighttime satellite is the most damaging scenario: stars appear, the satellite says clear, but veil cirrus kills transparency.

### Nighttime IR false-cloud over coastal regions [165]
- Miller et al. 2022 (Earth and Space Science): bi-spectral 11–3.9 µm BTD overstates low cloud at night where cool ocean upwelling lies beneath warm moist atmosphere — common over coastal regions.
- Day/Night Band ground truth confirms IR false alarm.
- Direct relevance for Carolina coastal sites where Gulf Stream / coastal upwelling combines with humid atmosphere.

### ASOS vs satellite definitional incompatibility [167]
- ASOS automated ceiling sensors report only clouds **below 12,600 ft AGL**.
- Overcast at 15,000 ft is reported as "clear sky" by ASOS.
- Documented case: NC/SC, ASOS reported clear while satellite imagery showed obvious overcast.
- Implications:
  1. An app comparing satellite-clear to ASOS-clear to "validate" the satellite will find spurious disagreements that are definitional, not physical.
  2. ASOS cannot serve as ground-truth to calibrate satellite cloud masks for cirrus-heavy days.

### Geometric incompatibility ground vs satellite [166]
- Ground-based fractional sky cover from a 160° FOV systematically overestimates satellite nadir cloud fraction by **>50%** for individual measurements.
- Cause: oblique perspective sees cloud sides; nadir view sees only cloud tops.
- For an app cross-checking satellite cloud against user-reported / all-sky-camera sky cover, the geometric bias must be acknowledged.

## MRMS (Multi-Radar Multi-Sensor)

| Aspect | Detail | Cite |
|---|---|---|
| Spatial resolution | 1 km | [158] |
| Temporal resolution | 2 min | [158] |
| Vertical levels | 33 | [158] |
| Domain | CONUS + Alaska + Hawaii + Caribbean + Guam (with Mexican/Caribbean radar connections) | [158] |
| Operational since | 2014 | [158] |
| Number of products | 100+ | [158] |
| S3 bucket | `noaa-mrms-pds` (us-east-1, no auth) | [159] |
| SNS topic | `arn:aws:sns:us-east-1:123901341784:NewMRMSObject` | [159] |

### Latency caveats
**Zhang et al. 2016 [168]** (BAMS): MRMS QPE has Pass 1 latency of 20 minutes and Pass 2 latency of 60 minutes; "not as useful during flash flood warning operations." For amateur astrophotography:
- MRMS QPE measures **precipitation, not cloud cover** — it is a downstream signal, not a direct cloud-cover input.
- The reflectivity mosaic (separate from QPE) updates every 2 minutes.
- Western US has terrain blockage gaps; SE US coverage is good.

For a cloud-cover-focused astrophotography app, MRMS is useful as **secondary precipitation context** (storm detection, frontal boundaries), not as a primary cloud-cover source.

## HRRR-Smoke

| Aspect | Detail | Cite |
|---|---|---|
| Operational since | 2020 | (Dim 9 Discovery findings) |
| Coupling | HRRR (parent NWP model) | [21], [22] |
| Inputs | VIIRS / MODIS fire hot-spot detections + Fire Radiative Power | (Dim 9 Discovery findings) |
| Spatial resolution | 3 km | (Dim 9 Discovery findings) |
| Domains | CONUS + Alaska | (Dim 9 Discovery findings) |
| Forecast horizon | "up to 48 hours" per NWS tutorial materials | (Dim 9 Discovery findings) |
| Update cadence | (HRRR updates hourly; HRRR-Smoke cadence assumed same but not directly verified) | (Dim 9 Discovery findings) |
| S3 access | HRRR data is in `noaa-hrrr-bdp-pds` [160]; HRRR-Smoke as separate sub-product not directly verified in registry text | [160] |

For SE US astrophotography, HRRR-Smoke is relevant for transparency forecasting during wildfire season — Canadian / western US wildfire smoke aerosols can degrade transparency over the Carolinas at high altitude even on cloud-free nights. Astrospheric explicitly incorporates HRRR-Smoke / RAP-Smoke into its transparency forecast [124].

## Optical-flow nowcasting limits
**CloudCast 2024 [95]:**
- Optical-flow satellite cloud nowcasting has a skillful window of ~3 hours.
- Beyond that, it cannot create or dissipate clouds, only advect existing pixels.
- For amateur astrophotography planning (sessions 3–8 hours away), pure satellite extrapolation is **no more skilled than, and eventually inferior to, NWP**.
- The right architectural pattern: **satellite for now and the next 0–3 hours; NWP for 3+ hours.**

## Practical architecture for SE US astrophotography app

| Lead time | Source | Cadence | Purpose |
|---|---|---|---|
| Now | All-sky camera (user device) + GOES-19 mesoscale | 30 sec / 60 sec | Visual confirmation, real-time abort decisions |
| 0–30 min | GOES-19 ABI ACM (CONUS) | 5 min | Observed cloud mask; "is it clear right now?" |
| 30 min – 3 h | GOES-19 ABI ACM + persistence/optical-flow extrapolation | 5 min | Beats NWP at this horizon [82], [95] |
| 3 – 6 h | HRRR (CONUS) hourly + persistence cross-check | Hourly | Convection-allowing; FH0–2 spin-up caveat [78] |
| 6 – 18 h | HRRR (CONUS) hourly | Hourly | Standard NWP |
| 18 – 48 h | HRRR Extended (00/06/12/18 Z) or NAM | Hourly | Convective overforecast caveat for SE US [79] |
| 2 – 5 days | ECMWF IFS HRES (or via Open-Meteo ECMWF endpoint) | 4×/day | Highest medium-range skill [86] |
| 5 – 10 days | ECMWF ENS or GFS GEFS | 4×/day | Probabilistic outlook |

## Recommended app integration for satellite

1. Subscribe to GOES-19 SNS topic for new-object notifications [149].
2. Filter to ACMC product (Clear Sky Mask, CONUS sector) for SE US users.
3. On notification, fetch the latest ACMC NetCDF from `noaa-goes19/ABI-L2-ACMC/<Y>/<DOY>/<HH>/`.
4. Extract cloud-mask value for user lat/lon (apply 4-class → 2-class clear/cloudy logic per app preference).
5. Store the result with timestamp; expose to app UI as "current cloud (observed)."
6. For 0–3 h forecast: apply optical-flow extrapolation (open-source: pyresample + OFA / pysteps) to ACMC frames.
7. For 3+ h forecast: switch to HRRR via Open-Meteo or NOMADS.
8. Apply confidence flags: lower confidence at night for thin cirrus; lower confidence at coastal sites at night per [165]; daytime ACM lower confidence per [161].

## Gaps and limitations

- **GOES-19 specific cloud product validation** (vs the GOES-16 ACM Tzallas 2020 study [161]) was not found — ACM accuracy on the new satellite may differ. Tzallas-style validation was done on GOES-16; transferability to GOES-19 is plausible but unverified.
- **ECM (Enterprise Cloud Mask)** vs ACM in the current S3 bucket is unresolved. A 2022 NCEI/NESDIS document references ECM as an upgrade replacing ACM — whether `noaa-goes19/ABI-L2-ACMC` uses ACM or ECM is not confirmed.
- **HRRR-Smoke S3 sub-path** in `noaa-hrrr-bdp-pds` was not directly verified [160]. The NOAA HRRR-Smoke website returned 403.
- **MRMS reflectivity-mosaic latency** (vs QPE latency) was not explicitly stated in fetched sources [168]. The 2-minute analysis update is the cycle time; actual wall-clock latency from radar observation to S3 availability is not documented.
- **ACHT (Cloud Top Temperature)** DOI, archive start, and post-upgrade resolution were not fully retrieved (NCEI metadata for ACHT specifically was not separately fetched).
- **GOES-18 CONUS coverage of Southeast US**: GOES-18 is GOES-West at ~137°W. CONUS sector is shared, but the SE US is at the edge of GOES-18's optimal viewing geometry. GOES-19 (75.2°W) provides better geometric angle for SE US — confirmed.
- **HRRR-Smoke operational status in 2026:** model became operational in 2020; whether it remains a standalone product vs integrated into RRFS (the planned HRRR successor) is unverified [47], [48].
- **AWS egress costs for high-cadence GOES pulls**: bucket access is free; egress to non-AWS infrastructure is $0.09/GB. A consumer app pulling 5-min CONUS ACMC frames and serving them to user devices outside AWS would face egress cost — concrete numbers depend on payload size per frame, not measured here.
