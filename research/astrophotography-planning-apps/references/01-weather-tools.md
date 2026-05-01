# Reference 01 — Weather-focused astrophotography tools

Source numbers refer to [`citations.md`](../citations.md).

## What this dimension covers

Inventory of dedicated weather-focused astrophotography apps and websites: pricing, platforms, underlying weather data sources, signals exposed, and how each presents its conclusion (raw table, color grid, traffic light, or single composite score).

## Tool-by-tool table

| Tool | Coverage | Platforms | Pricing (Apr 2026) | Decision format | Particulate signal | Cite |
|---|---|---|---|---|---|---|
| **Astrospheric** | Continental US + Canada only | iOS, Android, Web | Free; Pro **$2.99/mo or $29.99/yr** | Color-coded multi-row table; **no nightly composite score**; per-row coloring; "Smoke Score" is a domain-specific single number | **Smoke / column-integrated PM2.5 only** (no pollen, no Saharan dust as separate signal) | [1][2][3][4][27] |
| **Clear Outside** | Worldwide | iOS, Android, Web (free) | Free | Color-coded grid per cell; cloud at 3 layers + seeing + transparency + Bortle estimate; "Est. Sky Quality" header is light-pollution Bortle, not a nightly score | None | [9][10][148][215] |
| **Clear Dark Sky** | North America (~6,100 fixed locations) | Web; iCSC iOS viewer | Free | Color band per cell (cloud / transparency / seeing / darkness); user finds the column where all rows are dark blue | Smoke row sourced from FireSmoke.ca / Environment Canada FIREWORK; developer warns "any value other than 'no smoke' means enough to affect transparency" | [11][12][155][156] |
| **Scope Nights** | Global | iOS only | $6.99 one-time | Weighted algorithm → traffic-light (green/amber/red) per 3-/6-hour block; no continuous score; no seeing/transparency from a meteorological model | None | [13][14][181][182] |
| **Good to Stargaze** | Likely global | iOS (visionOS), Android | Tiered: Value $0.99/mo or $6.49/yr; Hobbyist $3.99/mo or $25.99/yr (7-day); Professional $6.99/mo or $54.99/yr (15-day) | Color-coded tiles per factor with user-customizable thresholds; no aggregate nightly verdict | None | [15][16][214] |
| **7Timer!** | Global (~1.5M points; 0.001° precision) | Web; consumed via Xasteria | Free, no API key, **non-commercial only** | Raw graphical/tabular ASTRO chart | None | [17][18][19] |
| **Meteoblue Astronomy** | Global | Web (free 3-day); paid for 7-day | Tiered; free 3-day seeing; `point+` subscription required for 7-day; **5,000 free API calls/year non-commercial** | Seeing Index 1 & 2 (1–5 scale); cloud at 0–4 / 4–8 / 8–15 km; "bad layers" turbulence visualization; no aggregate score | AOD550 in underlying API; consumer astronomy page surfacing not confirmed | [20][21][22][23][33][213] |
| **Xasteria / Xasteria Plus** | Global (via 7Timer) | iOS only | Plus: $0.99 one-time | Aggregator/portal of 7Timer + Clear Outside + Meteoblue + Astrospheric — raw multi-source data; no composite | None directly; links out to Astrospheric | [24][25][26] |
| **Sky Tonight** | Global | iOS, Android, Huawei | Freemium; Plus $1.99/mo or $14.99/yr; Pro $4.99/mo or $39.99/yr | **"Stargazing Index" percentage** combining sunset, moon phase, cloud cover, light pollution Bortle, visibility window — but **no seeing or transparency from a meteorological model** | None | [138][139][140][141] |
| **Ouranos** | Global | iOS, Android (PWA/TWA) | Subscription ~$40/yr (user-reported, not vendor-confirmed); 14-day forecast paid | "Sky Quality Index" updated every 15 min; methodology not publicly disclosed | None confirmed in documentation | [144][145][146] |
| **StarCast (LightCast)** | Global | Web (free); iOS app | Free web; iOS app **$2.99/month** with 7-day trial | **Composite 0–100 score** integrating cloud + moon + Bortle + humidity/visibility + atmospheric seeing + dew-point spread; **target-type modifiers** (Milky Way / DSO / Planetary / Wide Field); tier breakpoints 0–34 / 35–54 / 55–74 / 75–100 | None | [136][137] |

## Key findings

1. **Astrospheric is the clear North-American leader.** Highest user ratings (iOS 4.77/5; Android 4.06/5) [34][35]; the only mainstream app exposing column-integrated smoke / PM2.5 [4][5]; Pro at $29.99/yr is the price anchor for the category [2]. Coverage is its hard limit — continental US + Canada only [1][27].
2. **No app produces a seriously equipment-aware composite score.** Sky Tonight's index integrates only moon + cloud + Bortle + visibility window; StarCast adds seeing, dew point, and target-type modifier (closest to a comprehensive composite found) but does not accept user equipment specs (focal length, sensor, filter type) [136]. Astrospheric explicitly does not produce a nightly composite — multiple T3 reviewers confirm "no simple Yes/No answer" [27].
3. **Clear Outside has no seeing or transparency from a meteorological model.** Despite worldwide coverage and a strong free-app value proposition, this is a documented gap relative to Astrospheric and Meteoblue [9][215][27].
4. **7Timer is the underlying free engine for many.** Xasteria, AstroWeather (PL), and several smaller frontends consume it [17][18][24][26]. Free, no key, non-commercial — a real foundation for an indie tool.

## Source-quality notes

- All pricing for Astrospheric, Sky Tonight, Good to Stargaze, Scope Nights, SkySafari, and StarCast is direct vendor (T2) — confirmed within ±48h of fetch.
- 7Timer's GFS-based seeing model has peer-reviewed validation (Ye 2011, PASP 123:113) [19].
- The Astrospheric "Smoke Score" methodology is partly inferred — the public smoke page confirms column-integrated PM2.5 and 6-hour refresh [4] but does not disclose the f-AQI mapping mathematics; the f-AQI relationship is sourced from the FAQ [7].

## Gaps and limitations

- Meteoblue's seeing index lacks published peer-reviewed validation (a 2019 plan to publish was not found completed in this research).
- Astrospheric's Pro Feature Table page [3] was not deeply fetched; the per-feature comparison between free and Pro is partly inferred from third-party reviews.
- Ouranos's "Sky Quality Index" methodology is not publicly disclosed; integration of aerosols is unconfirmed.
- StarCast pricing and feature scope sourced from a March 2026 PetaPixel article [137] and the vendor page [136]; longer-term stability of the product is unknown.
