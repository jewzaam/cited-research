# Reference 06 — Pollen / smoke / dust / aerosol integration

Source numbers refer to [`citations.md`](../citations.md).

## What this dimension covers

Whether existing astrophotography tools surface particulate signals (tree pollen, wildfire smoke, Saharan dust, urban PM2.5). Hypothesis: no astro-weather tool does this comprehensively. The user's home region (NC) has severe pine pollen seasons that ruin imaging nights even at zero cloud cover.

## Tool-by-tool integration matrix

| Tool | Wildfire smoke | AOD/aerosol | Saharan dust | Pollen | Urban PM2.5 | Source |
|---|---|---|---|---|---|---|
| **Astrospheric** | **YES — integrated into transparency**, column-integrated PM2.5 from NOAA RAP via SmokeWx, 6-hour refresh, GOES every 30 min, NIFC fire data | YES — jet stream + AOD overlays | NO (not surfaced as separate dust signal — only generic smoke/PM2.5 column) | NO | Implicit only (RAP PM2.5 captures all wildfire-sourced PM2.5 but is not framed as AQI; vendor explicitly says "should not be used as an air quality forecast") | [1][4][5][6][7][147][149][211] |
| **Clear Dark Sky** | PARTIAL — smoke row from FireSmoke.ca / Environment Canada FIREWORK; developer warns it is "not well-calibrated" — "any value other than 'no smoke' means enough to affect transparency" | NO | NO | NO | NO | [11][12][155][156] |
| **Clear Outside** | NO | NO | NO | NO | NO | [9][215] |
| **Meteoblue Astronomy** | AMBIGUOUS — AOD550 in underlying API; consumer astronomy seeing page lists cloud layers, seeing index, jet stream — does not explicitly list AOD/smoke | AMBIGUOUS | NO | NO | NO | [20][21] |
| **Xasteria** | NO directly (links to Astrospheric externally) | NO | NO | NO | NO | [24][26] |
| **Ouranos** | NO | NO | NO | NO | NO | [144][145] |
| **Scope Nights** | NO | NO | NO | NO | NO | [13][14] |
| **Sky Tonight** | NO | NO | NO | NO | NO | [138][139] |
| **Good to Stargaze** | NO | NO | NO | NO | NO | [15][16] |
| **StarCast** | INDIRECT — humidity/visibility variable subsumes some particulate effects | NO direct | NO | NO | NO | [136][137] |
| **Telescopius** | NO | NO | NO | NO | NO | [38][39] |
| **Stellarium / SkySafari / planetariums** | N/A — not weather tools | | | | | |

## Astrospheric's smoke detail

The **only** mainstream astrophotography app with explicit particulate data is Astrospheric, and it covers only wildfire smoke:

- **Methodology:** "The smoke layer presented on Astrospheric integrates smoke and aerosols in the entire column of air above a particular point" — column-integrated, not surface-level [4].
- **Data source pipeline:** NOAA RAP PM2.5 model via Astrospheric's SmokeWx product; GOES satellite imagery refreshed every 30 minutes; fire location data from NIFC [5][7].
- **Refresh cadence:** "The smoke data on Astrospheric updates every 6 hours along with the rest of the forecast data" [4].
- **Smoke Score:** Encodes a forecast's worth of smoke into a single number mappable to f-AQI (fire-specific Air Quality Index) [7]. **Vendor explicitly warns: "the smoke forecast should not be used as an air quality forecast"** [4].
- **Transparency coupling:** Smoke is integrated into Astrospheric's transparency forecast by default — the only astronomy app to do so [4][6][27].

## What no tool surfaces

1. **Pine / oak / grass pollen** — extensively discussed in Cloudy Nights forums as an equipment-contamination hazard (sticky pine pollen on corrector plates) [150][153]. **Zero astrophotography planning apps** track pollen as an imaging or equipment-protection signal. Pollen.com, IQVIA, Tomorrow.io pollen API, and Ambee are all sources that exist; none are integrated in any astro tool found.
2. **Saharan dust transport** — Copernicus CAMS confirmed frequent storms across the Atlantic and over Europe in H1 2025 measurably degrading transparency [154]. NASA Worldview's AOD layer surfaces it [158]. **No astrophotography app** integrates Saharan dust as a separate forecast signal.
3. **Urban PM2.5 / chronic AQI** — AirNow, OpenAQ, PurpleAir crowdsourced data exists. **Astrospheric's column PM2.5 captures wildfire-sourced PM2.5 but is explicitly not an AQI tool** [4]. No app integrates EPA/AirNow urban PM2.5 for observing-session planning.

## Conclusion

The hypothesis is **strongly confirmed**. The particulate-integration gap is real and non-trivial. Astrospheric is the only meaningful incumbent and its coverage is wildfire-smoke-only. For a user in the Southeast US — pine pollen season (March-May), occasional Saharan dust events (summer), occasional Western wildfire smoke transport — no existing tool surfaces three out of four relevant particulate signals.

This is the strongest single differentiation hook surfaced in this research.

## Gaps and limitations

- Meteoblue's AOD550 surfacing on the consumer astronomy page was not directly verified; the API has it, the public seeing page may not display it.
- No evidence found of any developer publicly planning pollen integration; this gap appears to be unaddressed at the planning-discussion level too.
- Pollen-to-imaging-impact conversion (does a high pollen day actually degrade imaging vs. just contaminate optics?) is empirically real but not quantified in any peer-reviewed study found in this research.
- Astrospheric's RAP-PM2.5-derived column smoke is good for wildfire smoke but does not distinguish dust, biological aerosol (pollen), or generic urban PM2.5 — it's a single PM2.5 channel, not a multi-source classifier.
