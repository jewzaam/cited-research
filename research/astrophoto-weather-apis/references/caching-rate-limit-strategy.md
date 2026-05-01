# Caching and Rate-Limit Strategy

**Dimension covered:** Practical engineering patterns for an indie astrophotography app that polls many user locations against the providers reviewed in [`provider-matrix.md`](provider-matrix.md). HTTP cache headers, geographic grid caching, refresh strategy aligned to model run cycles, rate-limit handling, edge / CDN caching.

Sources: [`citations.md`](../citations.md).

## Headline findings

1. **NWS supports `Last-Modified` / `If-Modified-Since` 304 conditional requests** — but the same NWS infrastructure has documented multi-day stale-cache failures up to **981 hours (41 days)** [69], [110].
2. **Open-Meteo's free-tier limits are IP-based** (600/min, 5,000/hr, 10,000/day, 300,000/month) [50], [73] — incompatible with shared-IP hosts (Cloudflare Workers, shared VPS) where many users aggregate to one quota.
3. **HRRR data availability lags ~1.5 hours** behind initialization time; GFS lags ~3.5–5.25 hours [115], [116]. Refresh-on-model-run timing requires buffers, not deterministic schedules.
4. **Geographic grid snapping causes 3–6 °C errors** in complex terrain at 9–10 km grids [123]. For Appalachian / Blue Ridge sites, grid snapping is non-trivial.
5. **Self-hosting Open-Meteo is not cheaper than the paid subscription** at indie scale — bandwidth alone exceeds $4,800–9,000/month vs $29/month Standard [74].

## HTTP cache headers by provider

| Provider | `Cache-Control` | `ETag` | `Last-Modified` | `If-Modified-Since` 304 | Cache-busting prohibited? | Cite |
|---|---|---|---|---|---|---|
| NWS api.weather.gov | Yes (max-age=3600 documented for hourly forecasts) | Not documented | Yes | Yes (officially supported) | Yes (unknown query params trigger 400) | [110], [6] |
| Open-Meteo | Not documented in public docs (live HTTP inspection required) | Not documented | Not documented | Not documented | Unknown | [111], [112] |
| Pirate Weather | Yes (directive value not publicly documented) | Not documented | Not documented | Unknown | Unknown | [120] |
| Xweather | Returns 7 `X-RateLimit-*` headers (not Cache-Control) | Not documented | Not documented | Unknown | Unknown | [121] |

The NWS pattern is most directly usable: send `If-Modified-Since: <previous Last-Modified value>` and receive `304 Not Modified` if the gridded data has not been re-issued. For the JSON-body alternative, the `updateTime` field carries the same timestamp [110].

## Free-tier rate limits

| Provider | Limit | Mechanism | Cite |
|---|---|---|---|
| Open-Meteo | 600/min, 5,000/hr, 10,000/day, 300,000/month | IP-based (per-IP) | [50], [73] |
| NWS | No published numeric limit; soft 429 throttling; alerts ≥30s recommended; 403 (not 429) on rate-limit blocks | Per-IP / per-User-Agent (rate-limit blocks return **HTTP 403, not 429**) | [6], [71] |
| MET Norway | >20 req/sec is "heavy traffic" | User-Agent + per-IP | [60] |
| Tomorrow.io free | 500/day, 25/hr, 3/sec | Per-API-key | [57] |
| Visual Crossing free | 1,000 records/day | Per-API-key | [58] |
| WeatherAPI.com free | 100,000/month, hard cap (no auto-overage) | Per-API-key | [64] |
| OpenWeatherMap free | 60/min, 1M/month general; 1,000/day for One Call 3.0 | Per-API-key; suspension for breach | [53], [55] |

## Documented rate-limit gotchas

### NWS uses HTTP 403 for rate-limit blocks
**GitHub discussion #772 [71]:** NWS rate-limit blocks return HTTP 403 (not 429), making automated 429-retry logic fail silently. Standard exponential-backoff libraries that watch for 429 will not catch NWS rate-limiting.

### NWS blocked Linode and DigitalOcean entirely (August 2024)
**GitHub discussion #763 [70]:** August 31, 2024, NWS blocked Linode and DigitalOcean IPv6 ranges entirely after Akamai security filter classification change. Compliant developers were blocked for weeks. Resolution required forcing IPv4. Open-source developers using common cloud VPS providers are structurally exposed to this kind of infrastructure-classification block.

### Open-Meteo IP-based limits are incompatible with shared hosting
**HN item 46591888 [73]:** Open-Meteo creator confirms 600/min, 5,000/hr, 10,000/day are per-IP. Explicitly: "this is not ideal for shared hosting services like Cloudflare Workers." Apps deployed on Workers, shared VPS, or behind shared NAT aggregate quota to one IP.

### Open-Meteo opaque quota accounting
**GitHub issue #438 [for Dim 7 counter]:** Developer reports persistent 429 errors despite "far under" 10,000 calls/day, with even "a handful of website reloads" triggering the limit. The IP-basis calculation and reset boundaries are opaque.

### OpenWeatherMap suspends keys
**Free Code Camp forum [55]:** OWM blocks (not throttles) free-tier keys for limit breach. Suspension duration: "several hours to several days randomly." Open-source apps with embedded keys are structurally vulnerable — any user of the published code can exhaust the developer's quota.

### Apple WeatherKit returned stale data
**Apple Developer Forums thread 726148 [72]:** Confirmed Apple bug where WeatherKit returned current conditions 2+ hours stale. Apps showed clear skies during active rain. No fix ETA provided.

### NWS multi-day stale cache
**GitHub discussion #492 [69]:** Forecast data up to **981 hours (41 days) stale** served via Akamai CDN. Browsers vary headers and busted the cache; programmatic clients sent identical requests and always hit the cached entry. NWS's response was to *increase* max-age to protect origin servers — trading freshness for reliability.

### Apps deliberately cache to reduce per-call API costs
**Medium economics article (cited in Dim 7 counter):** Many production weather apps deliberately cache 30 min – several hours of stale data to reduce per-call API costs. Most do not disclose data age. "Accuracy takes a backseat when somebody decided how often to refresh that data based on API pricing."

## Model-run timing for fetch scheduling

| Model | Run times (UTC) | Availability lag (rough) | Practical fetch time | Cite |
|---|---|---|---|---|
| HRRR (standard) | Every hour | ~1.5 h post-init | T+2 h after top-of-hour with 10-min buffer | [115], [116], [111] |
| HRRR Extended (48 h) | 00, 06, 12, 18 Z | ~1h50m post-init | Same as standard for the extended cycles | [115] |
| GFS | 00, 06, 12, 18 Z | ~3.5 h to ~5.25 h to f384 | T+4 h after run hour | [116] |
| ECMWF Open Data | 00, 06, 12, 18 Z | ~7–9 h post-init | T+9 h with buffer | [7], [63] |
| MET Norway Locationforecast | (continuous) | Per `Expires` header | Honor `Expires` | [60] |

### Open-Meteo Metadata API
**Open-Meteo `update_interval_seconds` and `last_run_availability_time` [111]:** Provides per-model fields signaling when a new run is available. Recommended pattern: poll Metadata API (free, doesn't count toward quota), wait additional 10 min after `last_run_availability_time` updates, then fetch full forecast. This avoids fetching during the eventual-consistency window across Open-Meteo's distributed servers.

Open-Meteo's documentation explicitly states: **"Minor delays are fairly common."** Models flagged yellow at 20-min delay, red at multiple missed runs. A production app needs to handle missed/delayed runs gracefully.

### Refresh strategy (recommended)
1. **HRRR (CONUS, hourly):** Poll Open-Meteo Metadata API at T+2 h after top-of-hour. Fetch only if `last_run_availability_time` updated.
2. **GFS (global, 6-hourly):** Poll at T+4 h after 00/06/12/18 Z. Fetch only if metadata shows new run.
3. **ECMWF Open Data (4×/day):** Poll dissemination status; allow ~9 h buffer; download GRIB2 via `ecmwf-opendata` Python client.
4. **HydroForecast pattern [116]:** Add 30-min buffers and poll every 2 hours rather than at exact model-run times — implicitly acknowledges the brittleness of strict run-timed scheduling.

## Geographic grid caching

### Snapping precision per provider
| Provider | Native grid | Snap precision recommendation | Cite |
|---|---|---|---|
| NWS gridpoint | 2.5 km (forecast office WFO grids) | 4 decimal places (API enforced) | [6], [110] |
| Open-Meteo | Internal time-series grid | Round client-side to ~2 decimals (~1 km) for cache key | [114] |
| HRRR | 3 km | 3 km cell snap | [21] |
| GFS | 0.25° (~28 km) | 0.25° cell snap | [24] |
| ECMWF Open Data | 0.25° | 0.25° cell snap | [7] |

### Grid-snapping pitfall
**Meteomatics downscaling docs [123]:** 9–10 km ECMWF grid produces **3–6 °C temperature errors** in Alpine valleys vs peaks. The grid cell value represents area average, not specific coordinate. For SE US Appalachian / Blue Ridge sites where dark-sky observation occurs precisely because of terrain, the nearest grid cell may represent terrain 5–25 km away at different elevation.

For a cloud-cover app, this matters less than for temperature (cloud cover varies less sharply with terrain than temperature does), but for marginal sites in valley microclimates, grid snap can place the user on the wrong side of a ridge.

### NWS `/points` caching pattern
NWS issues forecasts on 2.5 km grids. The `/points/{lat},{lon}` endpoint returns the forecast office and grid XY for that coordinate. Many arbitrary coordinates resolve to the same grid cell. **Recommended pattern:**
1. Snap user lat/lon to 4 decimal places.
2. Cache the `/points` response indefinitely (grid assignments rarely change).
3. Use the returned `forecastGridData` URL as the stable cache key for forecast fetches.
4. Multiple users within the same 2.5 km square share one cached response.

## Rate-limit handling pattern

### Algorithm
```
delay = base_delay * (2 ^ attempt) * jitter_factor
where jitter_factor = random(0.5, 1.5)
cap delay at 30 seconds
max attempts = 5–7
```
Specific formula [Dim 7 Discovery]: `min(1000ms * 2^attempt, 30000ms)`.

### Retry-After header handling
- If `Retry-After` is present, use it as-is.
- Otherwise apply exponential backoff with jitter.
- For NWS specifically: watch for **HTTP 403 (not 429)** as the rate-limit signal [71].

### Python tooling
- **`requests-ratelimiter`** [122]: session-level rate limiter; `Retry-After` support; per-second/minute limits.
- **`openmeteo-requests` official client** [112]: uses `retry-requests` with `retries=5`, `backoff_factor=0.2`, `expire_after=3600`.

### Queue pattern for multi-location apps
- FIFO queue of location fetches.
- Single background worker drains at ≤ 1 req/sec.
- Naturally caps at 3,600/hr — well under Open-Meteo's 5,000/hr free-tier limit.
- Python: `asyncio.Queue` + semaphore, or `requests-ratelimiter` for sync.

## Edge / CDN caching

### Cloudflare Workers pattern
[117], [118], [119]:
```js
fetch(request, {
  cf: {
    cacheTtl: 3600,
    cacheEverything: true,
    cacheTtlByStatus: { "200-299": 3600, "500-599": 0 }
  }
})
```
- Cache is **data-center-local** — a miss at one PoP does not benefit another PoP. Suitable when most users cluster geographically.
- **Manual query-string normalization required** (no `ignoreSearch`). Pattern: strip volatile params, sort remaining ones, use normalized URL as cache key.
- "Respect Strong ETags" toggle passes provider ETag through for revalidation.
- Custom cache-key controls (excluding specific query params) require Enterprise plan.

### Architectural caveat
**CDN edge caching is architecturally incompatible with personalized per-coordinate forecasts** if the cache keys on path only — many lat/lon pairs collapse to one entry. Caching by snapped grid cell (or by NWS gridpoint URL) preserves per-location semantics.

### Workers + Open-Meteo IP-limit interaction [73]
A Cloudflare Worker shared-IP deployment **aggregates many users' quotas to one IP**, hitting Open-Meteo's 5,000/hr free-tier limit much faster than expected. This is the documented incompatibility between Open-Meteo's IP-based limits and shared-host architectures.

**Mitigation:** route through self-hosted Open-Meteo (expensive — see below), use commercial Open-Meteo paid tier, or front the API behind a serverless function with a stable per-deployment IP.

## Self-hosting Open-Meteo math
**Brightcoding analysis [74]:**
- Self-hosting requires **500 GB+ storage** (NVMe SSDs preferred) and **2 TB+/day bandwidth** for model data sync.
- At cloud egress pricing ($0.08–0.15/GB), 2 TB/day inbound costs **$4,800–9,000/month** — vastly more than the $29/month Standard subscription.
- AGPLv3 license adds source-disclosure obligation for commercial apps.
- Self-hosting is cost-justified only at billions of API calls/month.

For an indie astrophotography app, the paid Open-Meteo Standard subscription ($29/month, 1M calls) is the economically rational choice if the non-commercial gate matters.

## Practical caching architecture for an SE US astrophotography app

1. **For NWS:** Use `If-Modified-Since` 304 conditional requests. Cache `/points/{lat},{lon}` indefinitely. Cache forecast responses with the `Last-Modified` value as the cache key fingerprint.
2. **For Open-Meteo (non-commercial):** Use the official `openmeteo-requests` client with `requests-cache` SQLite backend, `expire_after=3600`. Snap lat/lon to ~2 decimals client-side for shared cache. Stay well under 5,000/hr by queuing.
3. **For ECMWF Open Data:** Use `ecmwf-opendata` Python client, fetch only the GRIB2 fields needed (LCC/MCC/HCC/TCC), cache locally for 6 h between runs.
4. **For GOES-19 ABI ACM:** Use AWS S3 `--no-sign-request`, cache locally for 5–10 minutes (matching CONUS scan cadence) — see [`satellite-nowcasting.md`](satellite-nowcasting.md).
5. **For all providers:** Honor returned `Cache-Control` / `Expires` headers, prefer 304 conditional requests where supported, expect ~20% inaccessibility per the cited-research methodology baseline.
6. **Avoid:** Cloudflare Workers for primary Open-Meteo proxy (IP-aggregation problem); aggressive sub-hour cloud-cover caching of NWP data (model output cadence is structurally hourly, sub-hour caches just serve interpolated/stale data).

## Gaps and limitations

- **Open-Meteo actual HTTP response headers** were not directly observed in this research. Whether Open-Meteo returns `Cache-Control` / `ETag` / `Last-Modified` and what specific values is unverified.
- **NWS exact `Cache-Control` directive values** (max-age, s-maxage, must-revalidate combination) were referenced but not directly observed.
- **Pirate Weather `Cache-Control` directive value** is not publicly documented [120].
- **HRRR coverage for specific SE US lat/lon** (e.g., Charlotte NC at 35.2°N, 80.8°W; Asheville NC at 35.6°N, 82.6°W) was asserted as CONUS but not verified via live Metadata API call.
- **Self-hosted Open-Meteo minimum viable variable set** for HRRR + GFS only (vs full global dataset) and its true storage footprint was not computed [74]. The 500 GB / 2 TB/day numbers reflect comprehensive deployment.
- **Cloudflare Workers free-tier `cacheEverything: true`** support: docs imply some cache controls are Enterprise-only [117], [119]; the exact tier boundary was not extracted.
- **`requests-ratelimiter` parsing of Open-Meteo rate-limit headers**: whether the library pre-emptively throttles based on response headers (vs reactively on 429) was not verified [122].
