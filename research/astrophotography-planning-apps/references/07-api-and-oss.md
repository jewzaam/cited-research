# Reference 07 — API surface, ecosystem, and open-source posture

Source numbers refer to [`citations.md`](../citations.md).

## What this dimension covers

For each tool: license model (closed/SaaS, freemium with closed core, OSS — under what license), public API availability (endpoint, auth, rate limits, terms), plugin/extension architecture, and underlying weather APIs that are themselves directly usable. Goal: map the build-new vs. contribute-to-existing decision surface.

## License + API matrix

| Tool | License | Public API | Plugin SDK | Source repo |
|---|---|---|---|---|
| **Astrospheric** | Closed SaaS, US/Canada-only | YES — REST; **gated to Pro subscription**; 100 credits/day refreshed at midnight UTC; cloud-cover call costs 5 credits | No | None public | [8][162] |
| **Clear Outside** | Closed; free retailer-backed | **No public API documented** | No | None public | [9][10][215] |
| **Telescopius** | Closed, freemium-by-donation | YES — `api.telescopius.com`; **Patreon-gated** (key from user settings); free-tier for personal use announced via Patreon (status as of April 2026 ambiguous) | No | None public | [43][44][163] |
| **PhotoPills** | Closed commercial | **No public API**; consumer-only product | No | None public | [172] |
| **AstroBin** | Open source — **AGPL-3.0-or-later** | YES — read-only REST/XML+JSON; key by request; commercial use allowed with key | No | [https://github.com/astrobin/astrobin](https://github.com/astrobin/astrobin) | [159][160][161] |
| **N.I.N.A.** | Open source — **MPL 2.0** ("Incompatible With Secondary Licenses" — limits GPL-family compat); Copyright © 2019-2025 Stefan Berg & contributors | Plugin SDK only (no network API); plugins via C# MEF interfaces | YES — official template; manifest registry rejects closed-source plugins | [https://github.com/isbeorn/nina](https://github.com/isbeorn/nina) | [102][107][108][109] |
| **KStars / Ekos** | Open source — **GPL-2.0-or-later** | YES — full D-Bus interface (Ekos modules + Scheduler); any D-Bus-capable language can drive it | Modular Ekos (no separate plugin SDK in NINA sense) | [https://github.com/KDE/kstars](https://github.com/KDE/kstars) | [76][77][78][79] |
| **Stellarium** | Open source — **GPL-2.0 or later** | YES — HTTP RemoteControl plugin API | YES — compiled C++ plugins + ECMAScript scripting engine | [https://github.com/Stellarium/stellarium](https://github.com/Stellarium/stellarium) | [49][50][51] |
| **Stellarium Mobile Plus** | Closed (Stellarium Labs commercializes) | No | No | (closed; based on OSS Stellarium core) | [52] |
| **Sequence Generator Pro** | Closed commercial | YES — documented HTTP API (SOAP/JSON/XML/JSV/CSV); REST-style | No formal SDK; API is the integration path | None public | [110] |
| **Voyager** | Closed commercial | YES — **JSON-RPC over TCP/IP and WebSocket** (Application Server API); Developer Plugin (separate purchase) extends DragScript variable passing | YES — plugins page; Developer Plugin sold separately | None public | [116][117][120] |
| **ASIAIR** | Closed proprietary; **GPL-violation history** with INDI/Siril/astrometry.net components — sources released only under community pressure | **No public API** | No | None public; partial component forks under pressure | [128][129] |
| **AstroPlanner** | Closed shareware | No | No | None public | [65] |
| **Cartes du Ciel** | Open source — **GPLv2** | YES — TCP/IP server on port 3292 (127.0.0.1 default); ASCOM + INDI compliant | Limited (ASCOM/INDI is the integration surface) | SourceForge | [70][68][69] |
| **SkySafari** | Closed commercial | No public API; SkySafari 7+ Pro consumes ASCOM Alpaca + INDI as a *client* | No | None public | [56][57] |

## Underlying weather APIs (directly usable for an indie tool)

| API | License/cost | Coverage | Auth | Notes |
|---|---|---|---|---|
| **NWS api.weather.gov** | Free, US-government public domain | US only | None (no API key) | OpenAPI v3.0 spec; ~30s/request cadence guidance; firewall-rate-limited [164] |
| **MET Norway api.met.no** | **CC-BY 4.0 + NLOD 2.0**; commercial use allowed with attribution | Global | None; User-Agent with contact info expected | Service rate-limits enforced; "Credit should be given to The Norwegian Meteorological Institute" [165][166] |
| **ECMWF Open Data** | **CC-BY-4.0** | Global; rolling ~2-3 day window of real-time IFS+AIFS | None for open subset | Replicated on AWS/Azure/GCP; Python `ecmwf-opendata` client; MARS request language [167][168] |
| **Open-Meteo** | **AGPL-3.0** (self-host); free non-commercial via hosted API | Global | None for free non-commercial | Up to 16-day hourly; SDKs in Python/TS/Swift/Kotlin/Java; commercial use requires paid plan [169][170] |
| **7Timer** | **Free, non-commercial only**; no key | Global, ~1.5M points, 0.001° precision | None | GFS-based; ASTRO product gives cloud + seeing + transparency + humidity + wind + temp [17][18][19] |
| **Meteoblue weather APIs** | Tiered; **5,000 free calls/year non-commercial**; commercial paid | Global | API key | Astronomy seeing endpoints (Index 1 + Index 2, jet-stream layers, 3-layer cloud) [22][23] |
| **NASA POWER** | Free, US gov | Global | None | Solar/met data; daily/monthly/annual/climatology [171] |
| **AirNow API** | Free, US-government public domain | US-focused | API key | Wildfire smoke + AQI + PM2.5 (basis for any urban-AQI integration) |

## Build-new vs. contribute-to-existing surface

**Highest-leverage contribution targets** (if the goal is to fill the gaps identified in [Reference 05](05-decision-aid-gap.md) and [Reference 06](06-particulate-integration.md)):

1. **N.I.N.A.** — MPL 2.0, plugin SDK, manifest registry. A "DecisionScore" plugin that consumes existing weather/safety drivers and outputs a composite score per night is mechanically possible. Plugin must be open source [109]. Reach: Windows astrophotographers — significant audience but constrained by NINA's Windows-only scope.
2. **KStars / Ekos** — GPL-2.0+, D-Bus surface, modular. A Scheduler enhancement that integrates a multi-factor score is structurally feasible. Cross-platform reach. Higher contribution-friction (KDE governance) but feasible.
3. **Stellarium plugin** — C++ + ECMAScript scripting; could host a planning panel that surfaces weather/score from external API. Reach is broad (planetarium audience), AP-specificity is lower than NINA/Ekos.

**Closed but API-accessible** (build a thin layer on top, not contribute):

- **Astrospheric** has a credit-gated REST API requiring Pro subscription [8]. Anything built on it inherits Astrospheric's coverage limit (US + Canada) and depends on Astrospheric's pricing/terms. Acceptable for a North-American-only product; deal-breaker for a global audience.
- **Voyager** API and plugins surface allow companion-app development, not core capture-suite extension [116][120]. Best fit if the goal is a remote-imaging companion, not a planning tool.
- **SGP** API allows triggering captures and equipment control [110] — same companion pattern as Voyager.

**Closed and not API-accessible** (cannot integrate practically):

- **PhotoPills, Clear Outside, ASIAIR, AstroPlanner.** Treat as out-of-scope for integration; competitors only.

## Conclusion

The ecosystem is **more open than a casual look suggests** for the capture-suite/planetarium layer (NINA, KStars, Stellarium are all OSS with documented extension surfaces). The weather-tool layer is split: Astrospheric and Telescopius have APIs but gate them behind paid tiers; Clear Outside has no public API; the underlying primary weather sources (NWS, MET Norway, ECMWF Open Data, 7Timer, Open-Meteo, Meteoblue free tier) are themselves directly usable by an indie developer.

A **"thin decision layer over existing data providers"** strategy is technically viable. Whether it's a *good* business is the question taken up in [Reference 09 — Market viability](09-market-viability.md).

## Gaps and limitations

- Telescopius free-tier API status as of April 2026 is unconfirmed; the announcement [163] predates today and no follow-up confirmation was found.
- ASIAIR's compliance with GPL terms post-2024 is contested; the source-release situation may have evolved [128][129].
- Meteoblue's astronomy seeing API has no peer-reviewed validation found; users should not assume scientific calibration.
- AirNow API is widely available but documentation page was not fetched in this research; cite tier and rate limits not confirmed.
