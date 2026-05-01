# Pricing and Licensing

**Dimension covered:** Free vs paid tiers, request quotas, attribution requirements, and commercial-use restrictions across the providers reviewed in [`provider-matrix.md`](provider-matrix.md). Practical viability for an indie / open-source astrophotography app polling many user locations.

Sources: [`citations.md`](../citations.md).

## Headline finding

For an indie astrophotography app, four providers can sustain non-trivial usage:
- **NOAA NWS** — free, public domain, no key, but production-unreliable per its own developer community [67], [68], [69], [70], [71].
- **MET Norway** — free, attribution required, strict User-Agent + caching ToS [60], [61], [62].
- **ECMWF Open Data** — free, CC-BY-4.0, no key required, full real-time catalogue open since October 1 2025 [7], [63].
- **Open-Meteo non-commercial tier** — free 10K/day, but legal ambiguity around what counts as commercial (donations, app-store distribution, ads) [49], [51], [52].

Commercial use of any of the above requires **either** Open-Meteo paid subscription ($29/mo and up) [51], **or** WeatherAPI.com / Visual Crossing free tiers (which permit commercial use), **or** self-hosting Open-Meteo (impractically expensive at indie scale per [74]).

## Free-tier comparison table

| Provider | Free quota | API key? | Commercial use on free tier? | Attribution required? | Cite |
|---|---|---|---|---|---|
| NOAA NWS | No published numeric limit; soft 429 throttling; alerts ≥30s | No (User-Agent required) | Yes — public domain (cannot claim copyright/imply endorsement/modify-as-official) | Not legally required (trademark protected) | [67], [6] |
| Open-Meteo | 600/min, 5,000/hr, 10,000/day, 300,000/month | No | **No** — strictly non-commercial; ads/subs/app-store revenue triggers commercial gate | Yes (CC-BY 4.0) | [49], [50], [51] |
| OpenWeatherMap | 60/min, 1M/month (general APIs); One Call 3.0 separate at 1,000/day | Yes (free issue) | Yes, with attribution | **Mandatory on-screen "Weather data © OpenWeather"** (ODbL, hidden footer credit insufficient) | [53], [54] |
| Tomorrow.io | 500/day, 25/hr, 3/sec | Yes | Status unconfirmed (ToS not directly fetched) | Unconfirmed | [57] |
| Meteomatics | 500/day, 50/min, 10 parallel | Yes | **No — explicitly "non-commercial = private projects only"** | Unspecified | [66] |
| Visual Crossing | 1,000 records/day | Yes | **Yes (commercial permitted on free tier)** | Required at Metered/Professional, not at Corporate | [58], [59] |
| MET Norway | No numeric quota; >20 req/sec is "heavy traffic" | No (User-Agent must contain contact info) | Yes (NLOD 2.0 + CC-BY 4.0 dual license) | Yes (suggested: "Data from MET Norway") | [60], [61] |
| ECMWF Open Data | 500 simultaneous connections | No | Yes (CC-BY-4.0) | Yes | [7], [63] |
| WeatherAPI.com | 100,000/month (with attribution); hard cap (no auto-overage) | Yes | Yes (all tiers) | Mandatory on free; recommended on paid | [64], [65] |

## Paid-tier comparison table

| Provider | Lowest paid tier | Quota | Commercial-use mechanics | Cite |
|---|---|---|---|---|
| Open-Meteo Standard | $29/month | 1,000,000 calls/month | Lifts non-commercial gate | [51] |
| OpenWeatherMap Startup | (price not on public page) | 600 calls/min, 10M/month | All tiers commercial | [53] |
| Tomorrow.io | Custom-sales | (not published) | Custom enterprise | [57] |
| Meteomatics | Custom-sales (industry-tailored) | 1,800+ parameters | Custom; 14-day trial | [66] |
| Visual Crossing Metered | $0.0001/record beyond free | Unlimited records/month | Pay-as-you-go beyond 1K/day | [58] |
| Visual Crossing Professional | Subscription | 10M records/month | Up to 10K records/query | [58] |
| WeatherAPI Starter | $7/month (or $75/year) | 3,000,000/month | All tiers commercial | [64] |
| WeatherAPI Pro+ | $25/month (or $270/year) | 5,000,000/month | All tiers commercial | [64] |
| WeatherAPI Business | $65/month (or $702/year) | 10,000,000/month | All tiers commercial | [64] |

## Per-location math at indie scale

Assuming one location polled hourly (24 calls/day per location):

| Provider/tier | Locations supportable on free tier |
|---|---|
| Open-Meteo non-commercial | ~417 (10,000 / 24) |
| OpenWeatherMap general API | ~1,388 (1M/month / 24/day / 30) |
| Tomorrow.io | ~20 (500 / 24) |
| Meteomatics | ~20 (500 / 24) |
| Visual Crossing | ~41 (1,000 / 24) |
| WeatherAPI.com | ~138 (100K/month / 24/day / 30) |
| MET Norway | unbounded by quota; bounded by ToS-friendly behavior |
| NWS | unbounded by quota; bounded by infrastructure stability |
| ECMWF Open Data | unbounded by quota; bounded by 500 concurrent connections + GRIB processing throughput |

For an app polling many user-registered dark-sky sites, **Open-Meteo non-commercial is the highest-leverage free tier among multi-layer-cloud providers** (~417 locations hourly), but its non-commercial restriction sharply limits monetization. WeatherAPI.com (~138 locations) and OWM general API (~1,388 locations) are the highest-leverage commercial-friendly free tiers — but expose only aggregate cloud cover.

## Documented "free tier turned hostile" patterns [75], [76]

The pattern of free-tier eliminations is industry-wide and historical:
- **Weather Underground** API discontinued (well documented prior to 2018).
- **Yahoo Weather API** retired in 2019.
- **Dark Sky** acquired by Apple 2020; API shutdown March 31, 2023; no migration path provided [76].
- **AccuWeather Core Weather API** replaced perpetual free with 14-day trial on September 9, 2025 [75].
- **OpenWeatherMap API 2.5** discontinued June 2024; 3.0 requires credit card on file even for free tier (community trust/privacy critique noted).

For a 2026 astrophotography app, the implication: **single-vendor dependency on a free tier is structurally fragile**. The architecturally robust pattern is multi-provider abstraction with Open-Meteo / NWS / MET Norway / ECMWF Open Data as the redundant base, plus WeatherAPI.com or Visual Crossing as commercial-friendly fallbacks.

## Documented free-tier enforcement issues

### OpenWeatherMap key suspension [55], [56]
- Free-tier 60-rpm limit triggers email-then-suspension when exceeded; suspension duration "several hours to several days randomly."
- Open-source apps with embedded keys are structurally vulnerable: any user of the published code can exhaust the developer's quota [55].
- 3.0 API requires credit card even for free tier (developer community treats this as a trust/privacy barrier).

### Open-Meteo non-commercial ambiguity [49], [52]
- ToS defers to Creative Commons for "non-commercial" definition.
- App-store distribution (with platform's 15–30% revenue cut), donations, and freemium models are not addressed.
- GitHub issue #417 [52] (developer asking whether donations = commercial) was closed without disclosed resolution.
- IP-based limits [73]: 600/min, 5,000/hr, 10,000/day are per-IP. Open-Meteo creator explicitly acknowledged this "is not ideal for shared hosting services like Cloudflare Workers" — a CF Worker shared-IP deployment aggregates many users' quotas to one limit.

### MET Norway User-Agent strictness [60], [62]
- User-Agent must contain a contact email or website link. Generic / fake User-Agent strings trigger 403; deliberate ToS violations result in **permanent ban with no upgrade path**.
- Coordinates with >4 decimal places trigger 403.
- Mobile push polling limited to once per 10 minutes.
- Browser-side JavaScript cannot set custom User-Agent — ruling out client-side calls.

### NOAA NWS production unreliability [68], [69], [70], [71]
- CDN cache served forecasts up to **981 hours (41 days) stale** in one documented case [69]. Cause: Akamai cached corrupted backend data; only fixed by replacing the backend service.
- Browsers got fresh data while API clients hit cache (architectural divergence in cache key handling) [68], [69].
- August 31, 2024: NWS blocked Linode and DigitalOcean IPv6 entirely after Akamai security filter change [70] — affected developers with compliant usage for weeks.
- NWS rate-limit blocks return **HTTP 403 (not 429)** [71]; standard 429-retry logic fails silently. Thresholds undocumented.
- Apple WeatherKit had a parallel confirmed bug returning current conditions 2+ hours stale with no fix ETA [72].

### Self-hosting Open-Meteo is not cheaper than the paid API [74]
- Self-hosting requires **500 GB+ storage** and **2 TB+/day bandwidth**.
- At typical cloud egress rates ($0.08–0.15/GB), 2 TB/day inbound costs $4,800–9,000/month — vastly more than the $29/month Standard subscription.
- AGPLv3 license additionally requires commercial source disclosure.
- Self-hosting is cost-justified only at billions of API calls/month.

## License attribution requirements

| Provider | License | Required attribution text | Display location |
|---|---|---|---|
| NWS | US public domain (17 USC §403) | None legally required (trademark protects logo/brand) | N/A | [67] |
| Open-Meteo | CC-BY 4.0 | Credit Open-Meteo as source | Required wherever data displayed | [49] |
| OpenWeatherMap | ODbL | "Weather data © OpenWeather" + logo | **On-screen** wherever data is displayed (footer in legal page is **insufficient**) | [54] |
| MET Norway | NLOD 2.0 + CC-BY 4.0 | "Data from MET Norway" with link | Where feasible; not allowed to imply official MET Norway / NRK / Yr origin | [61] |
| ECMWF Open Data | CC-BY 4.0 | "Adapted from '[Dataset]' by ECMWF, licensed under CC BY 4.0" + link | Standard CC-BY | [63] |
| Visual Crossing (Metered/Pro) | Commercial license | "Weather Data Provided by Visual Crossing" + link | Wherever displayed (Corporate/Enterprise: not required) | [59] |
| WeatherAPI.com (Free) | Commercial license | Credit WeatherAPI.com by name or logo | Mandatory on free tier; recommended on paid | [65] |

## Practical recommendation for an indie SE US astrophotography app

For the user's stated goal (SE US, hobbyist or small-paid-tier app):

1. **Primary forecast feed:** Open-Meteo non-commercial if the app stays donation/non-monetized; otherwise WeatherAPI.com Free (100K/month, commercial OK with attribution).
2. **Layered cloud verification:** MET Norway as a free, no-key cross-check (with proper User-Agent + caching).
3. **Medium-range outlook:** ECMWF Open Data via `ecmwf-opendata` Python client (GRIB2 processing required).
4. **Real-time observation overlay:** GOES-19 ABI ACM via `noaa-goes19` AWS S3 bucket (free, no auth) — see [`satellite-nowcasting.md`](satellite-nowcasting.md).
5. **Commercial path (if app monetizes):** Open-Meteo Standard ($29/month, 1M calls) is cheapest sustainable commercial option. WeatherAPI.com Starter ($7/month, 3M calls) is cheaper still per call — but cloud cover is single aggregate only [10].

## Gaps and limitations

- OpenWeatherMap and Tomorrow.io paid tier prices are not publicly listed beyond quota tiers; both direct enterprise inquiries to sales [53], [57].
- WeatherAPI.com free tier quota of 100,000 calls/month was confirmed from the official pricing page in this research; some third-party sources cite 1,000,000 — discrepancy flagged for Phase 4 verification [64].
- Tomorrow.io free-tier commercial-use status was not confirmed; ToS page returned 403 in this research.
- The non-commercial / commercial line for Open-Meteo when distributing through Apple App Store / Google Play (which take revenue cuts even from free apps) is unresolved [52].
- ECMWF Open Data 9 km HRES tier: planned for 2026 per October 2025 announcement [63]; whether this has launched at deliverable time was not re-checked.
- NWS API key rollout: NWS has announced intent to replace User-Agent with API keys; transition timeline not announced as of research date.
- No formal SLA exists on any free tier; production-grade apps must architect for graceful degradation.
