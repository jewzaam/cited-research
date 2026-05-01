# Southeast US Forecast Accuracy

**Dimension covered:** Documented accuracy, biases, and skill of cloud-cover forecasts in the Southeast US (Carolinas / Piedmont / Blue Ridge). HRRR/GFS/ECMWF performance, terrain effects, summer convective forecast skill.

Sources: [`citations.md`](../citations.md).

## Headline finding

**No peer-reviewed cloud-forecast verification study targets the Carolinas/Piedmont/Blue Ridge specifically.** The closest direct evaluation is HRRRv2 in northern Alabama (Burlingame et al. 2019) [80]. Most quantitative skill assessment for SE US comes from CONUS-wide studies that include SE US implicitly (SURFRAD, USCRN, NY State Mesonet) plus the southeastern-specific finding in Skinner et al. 2021 [79] that **HRRR overforecasts convective storm objects most in the southeastern US**.

Three converging lines of evidence support a practical conclusion: **for SE US summer convective regimes, all major NWP models have low cloud-forecast skill, persistence beats short-horizon NWP, and HRRR has a documented "spin-up" defect in its first 1–2 forecast hours.**

## Confidence statement

This dimension's evidence base is **moderate, not strong**. Several key papers' full text was not directly fetched in-session (AMS journals returned 403 throughout; James & Turner 2025 was ahead-of-print). Where quantitative numbers are quoted, they are sourced from search snippets / abstracts or from secondary citations — Phase 4 verification is responsible for grading these against actual source content. The audit report should flag any claim where the source's exact wording does not entail the assertion as stated.

## Documented HRRR cloud biases

### Cloud underprediction → excessive surface shortwave (CONUS-wide)
**James & Turner 2025 [77]** (MWR ahead of print) — most directly relevant recent paper:
- Excessive SW↓ at all 14 SURFRAD stations across the lower US.
- Cause: insufficient cloud attenuation (not clear-sky aerosol errors); a dry water-vapor bias in initial conditions further reduces modeled cloud.
- Experimental fixes cut bias by 80–84% in fall/winter but **only 35% in summer**. Summer is the hardest regime.

For the Carolinas, summer is exactly the regime when afternoon convective cloud cover (and post-storm lingering cloudiness) is most common — the worst-modeled regime is the most common one.

### Cloud spin-up at FH0–2
**Griffin & Otkin 2017 [78]** (JAMC, MODE/GOES verification):
- HRRR contains "fewer cloud objects than observed except at 0-h analysis" — except at the analysis hour, cloud objects are systematically too few across all seasons.
- Summer (August) bias is compounded by a more pronounced diurnal cloud cycle that HRRR's convective scheme does not capture well.
- Object-based finding: too many small objects at initialization, transitioning to too few oversized objects by FH2.

This is a documented "cloud spin-up" pattern in HRRR's first forecast hours that complicates trust in fresh HRRR cycles.

### Convective initiation timing in SE US
**NSSL EWP 2024 [90]** (operational note):
- HRRR delays afternoon convective initiation by **1–2 hours** in the Southeast.
- Excessive CIN persistence through afternoon hours (e.g., 17Z HRRR waits until 23Z to fire convection vs PHS at 21–22 Z; observed even earlier).
- Direct relevance: an SE US astrophotography app polling HRRR for "is the afternoon storm done?" decisions will see clear skies forecast 1–2 hours before observed clearing.

### Convective object overforecasting in SE US
**Skinner et al. 2021 [79]** (Wea. Forecasting, 1,400-forecast warm-season sample):
- HRRR overforecasts convective storm objects over the southern and eastern US.
- **Most pronounced in the southeastern US**.
- At high reflectivity thresholds (35–40 dBZ) overforecasting is widespread.

This implies HRRR over-generates convective precipitation events in SE US — and the associated high cirrus anvils on convective days may also be over-forecast.

### Reconciling apparent contradiction: HRRR underforecasts cloud cover AND overforecasts convective storm objects in SE US

The papers above can read as contradictory — if HRRR underforecasts cloud cover [77], [78], [87], how can it simultaneously overforecast convective storm objects [79]? Both findings are true and refer to **different measurement frameworks**:

- **Cloud underforecasting** is measured against **surface shortwave radiation** (SURFRAD, USCRN) and **MODE/GOES cloud objects**. The error mode is missing or under-resolving stratiform / shallow convective / boundary-layer clouds — the diffuse, persistent cloud cover that attenuates solar radiation but does not produce strong radar reflectivity.
- **Convective object overforecasting** is measured against **radar reflectivity** at 35–40 dBZ thresholds. The error mode is generating spurious deep-convection cells where observation shows weaker or no convection.

The two are physically consistent: HRRR's convective parameterization is too eager to fire deep convection (Skinner) but also too poor at maintaining the diffuse cloud cover that radiation-based verification measures (James & Turner; Min et al.; Griffin & Otkin). For an SE US astrophotography app, the practical implication is: HRRR may simultaneously **(a)** clear the sky too aggressively in stratiform / boundary-layer regimes (good night forecast that turns out cloudy due to undercaptured low cloud) **and (b)** falsely fire convective cells on the radar-reflectivity output (bad night forecast that turns out clear). These are different error modes for different underlying weather regimes — both worth flagging in user-facing forecasts.

### NY State Mesonet validation
**Min et al. 2021 [87]** (JGR-Atmos):
- HRRRv3 with NY State Mesonet: overcast/thick clouds during warm season are the main driver of positive SW↓ and warm-T biases.
- Frontal/convective cloud conditions are worst.

Northeast / Mid-Atlantic mesonet evidence reinforces the SE-US pattern.

### Northern Alabama (closest SE US direct evaluation)
**Burlingame et al. 2019 [80]** (Wea. Forecasting):
- HRRRv2 evaluated in northern Alabama (closest direct SE US peer-reviewed evaluation found).
- Surface energy balance errors documented; specific cloud-fraction values require full text access (not directly fetched).

This study is the highest-relevance direct SE-US-adjacent peer-reviewed verification and should be re-fetched in Phase 4 audit for specific bias numbers.

## GFS Arakawa-Schubert convective failures
**WPC operational notes [174]**:
- Arakawa-Schubert scheme is "very susceptible to grid scale convective blow-ups when the airmass is very moist and unstable" — exactly the SE US summer regime.
- Triggers convection too early in the diurnal cycle (peak ~15 UTC / 11 AM local vs observed mid-afternoon).
- Warm-season precipitation overforecast bias of ~1.6.

**Patel et al. 2021 [88]** (GRL): GFS at 25% sky cover shows 1°C warm bias at night, 2°C cold bias during the day — implicates GFS cloud-timing errors as a driver of surface-temperature errors.

## ECMWF performance in CONUS / SE US

**No SE US-specific peer-reviewed ECMWF cloud verification study was found** in this research. The available evidence:

**Mathiesen & Kleissl 2011 [81]** (Solar Energy, peer-reviewed) is the strongest CONUS-relevant direct comparison:
- ECMWF best in cloudy conditions (smallest bias <50 W/m² MBE).
- Raw GFS/NAM positive bias up to 150 W/m² in forecast-clear conditions.
- After MOS correction, GFS achieves the **best CONUS RMSE (~85 W/m²)** — beating ECMWF.
- Caveat: 2009–2010 data, both models have been substantially upgraded since. The conclusion does not necessarily hold for current operational ECMWF/GFS but illustrates that ECMWF's global skill leadership does not automatically translate to CONUS cloud cover.

**ECMWF IFS Cycle 47r3 cloud regression [29], [30]:** Globally introduced +3–4% mean cloud cover (up to +15% locally) since October 2021. This regression has not been confirmed as fixed in subsequent cycles in accessible documentation.

**Lledó et al. ECMWF Newsletter 174 [85]**: cloud FSS is scale-dependent; high-resolution 4.5 km only outperforms coarser models for small-scale structures — coarser wins for large frontal systems.

## Persistence vs NWP for cloud (astronomy-specific)

**Ye & Chen 2013 [82]** (MNRAS — only peer-reviewed cloud-forecast study targeting astronomers):
- "The persistence model is best of all for τ < 6 h" for GFS cloud cover comparison — **but the paper qualifies this**: "this is not meaningful as the GFS model data are not available after approximately 4–5 h." In other words, the persistence-vs-GFS advantage at <6h is partly an **operational availability artifact** (GFS forecasts have a 4–5h post-initialization latency before they reach the user) rather than a pure skill comparison.
- GFS detects fewer than half of convective cloud events globally ("the GFS model can identify less than half of such cloud").
- For total cloud cover forecast accuracy: probability of <30% forecast error declines from 73% at 3 hours to 58% at 180 hours.
- GFS beats ISCCP climatology baseline up to ~120 hours.
- Regional biases: oceans systematically underestimated (–10.31% at 3h, –11.28% at 180h); land slight overestimation (+0.28% to +0.25%); high clouds overestimated 15–19%; low clouds underestimated off west coasts of major continents at mid-latitude.

**Implication (revised):** For lead times where GFS data is not yet available (the first ~4–5 hours after a forecast cycle initialized), persistence is the only signal — and persistence is the best you have. Once GFS data arrives, it beats persistence for total cloud cover. For the SE US user, this means observed-conditions sources (GOES-19 ABI ACM, all-sky cameras) cover the latency gap until the next NWP cycle is available; NWP takes over once it arrives. This validates the architectural choice of layering observation-based and forecast-based signals — but the strict claim "persistence beats NWP at <6h" is qualified by the operational availability of NWP data at that horizon.

## Diurnal cloud bias

**Yin & Porporato 2017 [84]** (Nature Communications):
- Climate models peak land cloud cover too early in the morning by 4–6 hours.
- Caveat: CMIP5 climate models, not NWP. Direct extrapolation requires caution.

NWP-specific diurnal cloud bias is documented in several sources (Griffin 2017 [78] for HRRR; WPC notes for GFS [174]) but no SE-US-specific diurnal study was found. The convective initiation delay in HRRR for SE US [90] is the closest documented diurnal effect.

## Convective initiation difficulty
**Henderson et al. 2021 [83]** (MWR): state-of-the-art high-resolution NWP struggles with non-linear convective initiation events. SE US isolated convection driven by surface heating and boundary-layer inhomogeneities is poorly forecast by all operational models — a regional regime where physics fundamentally limits forecast skill.

Cool-season precipitation forecasts are generally 35–55% more accurate than warm-season forecasts; warm-season PoP improves at only ~2%/decade — convective initiation timing and mode remain unsolved across all model resolutions (literature consensus per multiple sources cited in the BAMS DoD workshop [169]).

## Practical implications for SE US astrophotography

| Forecast horizon | What works for SE US | Why |
|---|---|---|
| Now / next 30 min | GOES-19 ABI ACM (5 min CONUS cadence) | Observed cloud, model-free [149], [152] |
| 30 min – 3 h | GOES-19 ACM + persistence/optical-flow extrapolation | Beats NWP at this horizon [82], [95] |
| 3 – 6 h | HRRR (for SE US dynamics, with caveats) + persistence cross-check | HRRR is convection-allowing but has spin-up issues at FH0-2 [78]; persistence still competitive [82] |
| 6 – 18 h | HRRR (CONUS) | 3 km, hourly cycles; CIs delayed 1-2 h in SE US [90] |
| 18 – 48 h | HRRR Extended (00/06/12/18 Z) — convective season caveat | HRRR overforecasts convective objects in SE US per [79] |
| 2 – 5 days | ECMWF IFS HRES | Highest medium-range skill globally [86] but no SE-US-specific verification |
| 5 – 10 days | ECMWF ENS / GFS GEFS for probabilistic | Skill near climatology; ensemble probability more useful than deterministic |

## Gaps and limitations

- **No SE-US-specific peer-reviewed cloud verification study** was found. The most directly relevant available studies are CONUS-wide (James & Turner 2025 [77]; Mathiesen & Kleissl 2011 [81]; SURFRAD-based and NY State Mesonet-based — [87]).
- **Burlingame et al. 2019 [80]** (HRRRv2 northern Alabama) is the geographically closest direct SE US peer-reviewed evaluation; full text was not fetched in-session.
- **NWS NDFD WFO-level sky cover verification portal** (sats.nws.noaa.gov/~verification/ndfd/) maintains GSP/RAH/ILM/MHX/CHS-specific Heidke Skill Scores and Fraction Correct numbers but was inaccessible at research time.
- **No CONUS or SE-US ECMWF cloud verification study more recent than Mathiesen & Kleissl 2011** [81] was found. ECMWF's own verification is Europe-centric.
- The convective initiation delay [90] is from an NSSL operational blog post (Tier 2), not from a peer-reviewed publication.
- The HRRRv2 (2019) and HRRRv3 (2018-2021) verification literature predates the current operational HRRRv4 — bias magnitudes may have changed.
- Several sources reporting bias values come from search snippets / abstracts (AMS journals returned 403 throughout the research). Phase 4 verification should re-fetch and grade specific quantitative claims against full-text source content.
- The NY State Mesonet study [87] is northeast / Mid-Atlantic, not SE US — applicability to SE US humid subtropical regime is inferred, not demonstrated.
- Climate-model diurnal cycle studies (Yin & Porporato 2017 [84]) do not directly address NWP behavior; the 4–6 h "too early" finding is for CMIP5, not HRRR/GFS.
