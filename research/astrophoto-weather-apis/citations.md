# Citations

All sources collected during research conducted in April 2026. Each entry
includes a Tier rating per the cited-research source quality framework
(1 = peer-reviewed/govt; 2 = manufacturer specs/established reference;
3 = industry blog/conference talk; 4 = forum/personal blog/social).

Where a source could not be directly fetched in-session (e.g., 403 errors,
paywalls), the entry notes the access status and the basis for the
extracted claim. Phase 4 verification is responsible for re-fetching cited
URLs and grading each claim against actual source content.

---

## Provider documentation (Dim 1)

**[1]** Open-Meteo. "Forecast API Documentation." n.d.
<https://open-meteo.com/en/docs>
**Tier:** 2
Parameters `cloud_cover_low` (0–3 km), `cloud_cover_mid` (3–8 km), `cloud_cover_high` (8 km+), `cloud_cover` (total); free tier; 7-day default forecast horizon, up to 16 days.

**[2]** Open-Meteo. "Forecast API — DWD ICON cloud cover from model levels." GitHub Issue #416.
<https://github.com/open-meteo/open-meteo/issues/416>
**Tier:** 4
Documents bug where pressure levels physically below terrain (1000 hPa, 975 hPa) were included in `cloudcover_low` calculations at elevated sites, producing 100% low cloud cover at clear-sky elevated locations.

**[3]** MET Norway. "Locationforecast 2.0 Data Model." n.d.
<https://docs.api.met.no/doc/locationforecast/datamodel.html>
**Tier:** 1
Parameters `cloud_area_fraction`, `cloud_area_fraction_high` (>5000 m), `cloud_area_fraction_medium` (2000–5000 m), `cloud_area_fraction_low` (<2000 m); instant percentage values; time steps 1-hour for first ~60h, 6-hour medium range; ~10 days horizon.

**[4]** MET Norway. "Locationforecast 2.0 Documentation." n.d.
<https://api.met.no/weatherapi/locationforecast/2.0/documentation>
**Tier:** 1
Endpoint URL structure, forecast horizon, cadence, JSON schema.

**[5]** weather.gov. "Gridpoint Frequently Asked Questions." weather-gov.github.io.
<https://weather-gov.github.io/api/gridpoints>
**Tier:** 1
NWS API gridpoints endpoint exposes only `skyCover` (single aggregate %); no separate low/mid/high cloud layer parameters; 4-decimal coordinate precision cap.

**[6]** weather.gov. "API General FAQs." weather-gov.github.io.
<https://weather-gov.github.io/api/general-faqs>
**Tier:** 1
NWS API requires User-Agent header; supports `Last-Modified`/`If-Modified-Since` 304 conditional requests; cache-busting query parameters trigger 400.

**[7]** ECMWF. "Open Data." n.d.
<https://www.ecmwf.int/en/forecasts/datasets/open-data>
**Tier:** 1
ECMWF Open Data covers LCC, MCC, HCC, TCC parameters; 0.25° resolution; 0–360 h horizon for 00Z/12Z (15 days), 0–144 h for 06Z/18Z; rolling ~2–3 day archive; CC-BY-4.0 license.

**[8]** ECMWF Confluence. "How are low, medium and high cloud cover defined?" page id 111155326.
<https://confluence.ecmwf.int/pages/viewpage.action?pageId=111155326>
**Tier:** 1
ECMWF defines LCC at sigma >0.8, MCC at sigma 0.45–0.8, HCC at sigma <0.45. Source uses dimensionless sigma values exactly. Pressure-level translations (e.g., "~850 hPa surface boundary, ~450 hPa MCC/HCC boundary") cited elsewhere in the documents are derivative (est., assuming 1013 hPa surface pressure) — not from the source page. Sigma-based, terrain-relative — not directly comparable to providers using fixed-pressure or fixed-altitude cutoffs.

**[9]** ECMWF Confluence. "ECMWF open data: real-time forecasts from IFS and AIFS."
<https://confluence.ecmwf.int/display/DAC/ECMWF+open+data:+real-time+forecasts+from+IFS+and+AIFS>
**Tier:** 1
Confirms parameter IDs and time-step schedule; rolling 12-run archive; details on `enfo` stream for ENS.

**[10]** OpenWeatherMap. "One Call API 3.0."
<https://openweathermap.org/api/one-call-3>
**Tier:** 2
Single aggregate `clouds` parameter (percentage); no separate low/mid/high cloud layer fields. API 2.5 deprecated June 2024; 3.0 current; 48h hourly + 8 daily horizon.

**[11]** Meteomatics. "Cloud Parameters."
<https://www.meteomatics.com/en/api/available-parameters/weather-parameter/clouds/>
**Tier:** 2
Parameters `low_cloud_cover`, `medium_cloud_cover`, `high_cloud_cover`, `total_cloud_cover`, `effective_cloud_cover`; altitude bands low 0–1800m AGL, medium 1800–6300m AGL, high >6300m AGL; units octas or percent.

**[12]** Meteomatics. "API Request Format."
<https://www.meteomatics.com/en/api/request/>
**Tier:** 2
URL format: `https://api.meteomatics.com/{validdatetime}/{parameters}/{location}/{format}`; commercial trial available.

**[13]** Tomorrow.io. "Core Data Layers."
<https://docs.tomorrow.io/reference/data-layers-core>
**Tier:** 2
Three cloud parameters: `cloudCover` (aggregate %), `cloudBase` (km), `cloudCeiling` (km). No `cloudCoverLow/Mid/High` fields documented.

**[14]** Visual Crossing. "Weather Data Documentation."
<https://www.visualcrossing.com/resources/documentation/weather-data/weather-data-documentation/>
**Tier:** 2
Field `cloudcover` is single aggregate percentage representing all-altitude cloud cover; daily values are mean of hourly. No layered cloud parameters.

**[15]** WMO. "International Cloud Atlas — Some Useful Concepts: Levels."
<https://cloudatlas.wmo.int/en/some-useful-concepts-levels.html>
**Tier:** 1
WMO altitude ranges are latitude-dependent: high cloud bases 3 km (polar), 5 km (temperate), 6 km (tropical); mid cloud tops 4 km (polar), 7 km (temperate), 8 km (tropical). Levels overlap.

**[16]** Pirate Weather. "Data Sources."
<https://docs.pirateweather.net/en/latest/DataSources/>
**Tier:** 2
Pirate Weather "currently" block can jump discontinuously between RTMA-RU analysis cycles; cloud cover is model-blend (HRRR + NBM + GFS depending on region).

**[17]** Open-Meteo. "ECMWF History API returning null for cloud_cover and weather_code." GitHub Issue #1135.
<https://github.com/open-meteo/open-meteo/issues/1135>
**Tier:** 4
Documents Open-Meteo ECMWF History API silently returning null for `cloud_cover` and `weather_code` from October 12–16, 2024 across all coordinates. Issue closed without disclosed resolution.

**[18]** meteoblue. "Weather Variables: Clouds."
<https://content.meteoblue.com/en/research-education/specifications/weather-variables/clouds>
**Tier:** 2
meteoblue defines mid-cloud as 2–7 km (temperate) per WMO; explicitly notes "measuring cloud cover is very difficult in practice."

---

## NWP model documentation (Dim 2)

**[19]** NOAA NCEP. "HRRR Subhourly GRIB2 Inventory."
<https://www.nco.ncep.noaa.gov/pmb/products/hrrr/hrrr.t00z.wrfsubhf00.grib2.shtml>
**Tier:** 1
HRRR `wrfsubhf` (subhourly) product: 15-minute output, FH00–FH18, no LCDC/MCDC/HCDC/TCDC variables. Inventory includes REFC, RETOP, VIL, VIS, DSWRF/VBDSF, precipitation types/rates, cloud ceiling/base/top heights, simulated GOES brightness temperatures.

**[20]** NOAA NCEP. "HRRR Surface GRIB2 Inventory."
<https://www.nco.ncep.noaa.gov/pmb/products/hrrr/hrrr.t00z.wrfsfcf00.grib2.shtml>
**Tier:** 1
HRRR hourly surface (`wrfsfcf`) product cloud variables: LCDC, MCDC, HCDC, TCDC (boundary layer + entire atmosphere), cloud ceiling height, cloud base/top.

**[21]** Dowell, D.C. et al. "The High-Resolution Rapid Refresh (HRRR): An Hourly Updating Convection-Allowing Forecast Model." *Weather and Forecasting*, vol. 37 no. 8, 2022. DOI:10.1175/WAF-D-21-0151.1.
<https://journals.ametsoc.org/view/journals/wefo/37/8/WAF-D-21-0151.1.xml>
**Tier:** 1
Authoritative HRRR system description: 3 km, hourly, CONUS-only, cloud-resolving / convection-allowing.

**[22]** NOAA. "High-Resolution Rapid Refresh (HRRR)." n.d.
<https://rapidrefresh.noaa.gov/hrrr/>
**Tier:** 1
HRRR overview page; 3 km, 18h forecast (48h on extended cycles 00/06/12/18Z), hourly cycles. **Access:** Returned 403 during research — claims confirmed via secondary sources.

**[23]** NOAA NCEP. "RAP GRIB2 Inventory."
<https://www.nco.ncep.noaa.gov/pmb/products/rap/rap.t00z.awp130pgrbf00.grib2.shtml>
**Tier:** 1
RAP cloud variables: LCDC, MCDC, HCDC, TCDC (boundary layer + entire atmosphere), cloud ceiling, cloud base, cloud top.

**[24]** NCEI. "Global Forecast System (GFS)."
<https://www.ncei.noaa.gov/products/weather-climate-models/global-forecast>
**Tier:** 1
GFS specs: ~13 km native (T1534), 0.25° / 0.5° / 1.0° output grids, 384h forecast (16 days), 4 runs/day at 00/06/12/18 UTC, 127 vertical levels.

**[25]** NCEP EMC. "HREF / HiResW."
<https://www.emc.ncep.noaa.gov/emc/pages/numerical_forecast_systems/href-hiresw.php>
**Tier:** 1
HREF: ~3 km convection-allowing ensemble; HRRR + ARW + FV3 members; 00/12 UTC CONUS runs (06/18 UTC for AK/PR); 48-hour horizon.

**[26]** NWS. "HREF Model Upgrade — December 2021."
<https://www.weather.gov/news/211205-href-model-upgrade>
**Tier:** 1
Upgrade added FV3 members and HRRR; forecast range extended to 48 hours.

**[27]** ECMWF. "New Model Cycle 41r2 Brings Higher Resolution." Newsletter 147.
<https://www.ecmwf.int/en/newsletter/147/meteorology/new-model-cycle-brings-higher-resolution>
**Tier:** 1
IFS HRES upgraded to 9 km horizontal resolution March 8, 2016 (Cycle 41r2); 137 vertical levels.

**[28]** ECMWF. "Model Upgrade Increases Skill and Unifies Medium-Range Resolutions." June 2023.
<https://www.ecmwf.int/en/about/media-centre/news/2023/model-upgrade-increases-skill-and-unifies-medium-range-resolutions>
**Tier:** 1
IFS Cycle 48r1 upgraded ENS resolution from 18 km to 9 km on June 27, 2023; extended-range ENS expanded from 51 to 101 members.

**[29]** ECMWF. "Implementation of IFS Cycle 47r3."
<https://confluence.ecmwf.int/display/FCST/Implementation+of+IFS+Cycle+47r3>
**Tier:** 1
Cycle 47r3 (October 2021) explicitly degraded total cloud cover; +3-4% global mean cloud increase, up to +15% locally — a documented regression acknowledged by ECMWF.

**[30]** ECMWF. "47r3 Impact on Surface Weather Representation."
<https://confluence.ecmwf.int/display/FCST/47r3+Impact+on+Surface+Weather+representation>
**Tier:** 1
Quantified TCC changes by latitude band and cloud type after 47r3.

**[31]** ECMWF. "ECMWF's AI Forecasts Become Operational." February 2025.
<https://www.ecmwf.int/en/about/media-centre/news/2025/ecmwfs-ai-forecasts-become-operational>
**Tier:** 1
AIFS Single v1.0 operational from February 25, 2025; 28 km grid spacing; 6-hour update cadence. Source mentions wind, temperature, precipitation types, surface solar radiation, and turbine-level wind speeds among outputs. The specific cloud-output variables (tcc, lcc, mcc, hcc) come from the AIFS Single v1 documentation [32], not this announcement page.

**[32]** Bouallègue, Z.B. et al. "ECMWF AIFS Single v1.0: Documentation Update." Newsletter 183.
<https://www.ecmwf.int/en/newsletter/183/news/operational-release-aifs-single-10>
**Tier:** 1
AIFS produces flat cloud cover distribution vs observed U-shape; under-predicts clear-sky and overcast extremes; attributed to MSE training as "an inherent limitation."

**[33]** Solcast. "Accuracy Analysis: ECMWF's AI Model for Solar Forecasting."
<https://solcast.com/blog/accuracy-analysis-ecmwfs-ai-model-for-solar-forecasting-performs-well>
**Tier:** 3
AIFS irradiance bias −8% vs IFS +2% vs GFS +5% — implies AIFS systematically over-predicts cloud opacity. Note: industry blog, methodology described but not peer-reviewed.

**[34]** DWD. "ICON Description."
<https://www.dwd.de/EN/research/weatherforecasting/num_modelling/01_num_weather_prediction_modells/icon_description.html>
**Tier:** 1
ICON Global: 13 km, 90 vertical levels, 180h horizon (00/12Z); ICON-EU: 6.5 km, 60 levels, 120h; ICON-D2: 2.2 km, 65 levels, 48h, 3-hour cadence.

**[35]** DWD. "ICON-EPS Documentation."
<https://www.dwd.de/EN/research/weatherforecasting/num_modelling/04_ensemble_methods/ensemble_prediction/ensemble_prediction_en.html>
**Tier:** 1
ICON-EPS: 40 members; 40 km globally, 20 km EU; 8 runs/day; 180h extended horizon at 00/12Z.

**[36]** Met Office. "MOGREPS Overview."
<https://www.metoffice.gov.uk/research/weather/ensemble-forecasting/mogreps>
**Tier:** 1
MOGREPS-G: 18 members, 20 km, ~7-day; MOGREPS-UK: 18 members, 2.2 km, 5-day, 24 runs/day.

**[37]** AWS Open Data. "MOGREPS-UK Ensemble." Registry of Open Data on AWS.
<https://registry.opendata.aws/met-office-uk-ensemble/>
**Tier:** 1
MOGREPS-UK: 2.2 km, 24 runs/day, 126-hour horizon, NetCDF on AWS; format changes from January 2026.

**[38]** AWS Open Data. "MOGREPS-G Ensemble."
<https://registry.opendata.aws/met-office-global-ensemble/>
**Tier:** 1
MOGREPS-G: 20 km grid, 4 runs/day, up to 198 hours (246h post-Jan 2026), 30-day archive.

**[39]** Wikipedia. "North American Ensemble Forecast System."
<https://en.wikipedia.org/wiki/North_American_Ensemble_Forecast_System>
**Tier:** 2
NAEFS: 40 perturbed members + 2 controls (NWS GFS + Environment Canada GEM), 2× daily, 16-day horizon. Outputs: mean, mode, SD, percentiles 10/50/90.

**[40]** NCEI. "GEFS." n.d.
<https://www.ncei.noaa.gov/products/weather-climate-models/global-ensemble-forecast>
**Tier:** 1
GEFS official product page; member counts, run cadence, forecast horizon, archive cutoff.

**[41]** NOAA UFS. "GEFSv12 Operational." September 2020.
<https://ufs.epic.noaa.gov/2020/09/gefsv12/>
**Tier:** 1
GEFSv12: 31 members (control + 30 perturbed), 25 km resolution, FV3 dynamical core, atmosphere-wave-aerosol coupling, 16-day forecast (35-day extended).

**[42]** Lam, R. et al. "Learning skillful medium-range global weather forecasting." Science 2023. arXiv preprint.
<https://arxiv.org/abs/2212.12794>
**Tier:** 1
GraphCast: 0.25° resolution, 10-day forecast in 6-hour steps, 227 target variables. Cloud cover NOT among output variables. Outperforms ECMWF HRES on 89.3% of tested variable/lead-time combinations.

**[43]** Bi, K. et al. "Pangu-Weather." arXiv:2211.02556.
<https://arxiv.org/abs/2211.02556>
**Tier:** 1
Pangu-Weather: 0.25°, 1–168h forecast, 69 variables (geopotential, humidity, wind, temperature at pressure levels). No cloud cover output.

**[44]** Pathak, J. et al. "FourCastNet." arXiv:2202.11214.
<https://arxiv.org/abs/2202.11214>
**Tier:** 1
FourCastNet: 0.25°, 73 ERA5 channels including TCWV (total column water vapor) but no cloud cover (LCDC/MCDC/HCDC).

**[45]** Bonavita, M. "On Some Limitations of Current Machine Learning Weather Prediction Models." *Geophysical Research Letters*, 2024.
<https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2023GL107377>
**Tier:** 1
Pangu-Weather, FourCastNet, GraphCast all heavily damp spectral modes above wavenumber ~60 at 12–24h forecasts; physically inconsistent at small scales.

**[46]** Olivetti, L. & Messori, G. "Data-driven medium-range weather prediction with a Resnet pretrained on climate simulations." *Geoscientific Model Development*, 2024.
<https://gmd.copernicus.org/articles/17/7915/2024/>
**Tier:** 1
GraphCast and Pangu-Weather exhibit "blurring" — progressive reversion toward climatology at longer leads. AI models underestimate 99th-percentile precipitation by 20–35% vs HRES 10–15%.

**[47]** GribStream. "RRFS replaces NAM/HiResW/HREF/NARRE." Blog.
<https://gribstream.com/blog/rrfs-replaces-nam-hiresw-href-narre-proposal>
**Tier:** 3
RRFS proposed 3 km CONUS replacement for NAM/HRRR/RAP/HREF, originally planned early 2026, delayed.

**[48]** LuckGrib. "UFS / RRFS Status." February 2026.
<https://luckgrib.com/tutorials/2026/02/08/ufs.html>
**Tier:** 3
RRFS planned specs: 3 km CONUS (2.5 km Hawaii/PR); hourly to 18h, 00/06/12/18Z to 84h; retirement timeline still in flux as of February 2026.

---

## Pricing and licensing (Dim 3)

**[49]** Open-Meteo. "Terms of Service."
<https://open-meteo.com/en/terms>
**Tier:** 1
Free tier strictly non-commercial (CC-BY 4.0 reference); apps with subscriptions or advertising are commercial; no SLA; blocking without notice for ToS violation.

**[50]** Open-Meteo. "Pricing."
<https://open-meteo.com/en/pricing>
**Tier:** 1
Free tier: 600/min, 5,000/hr, 10,000/day, 300,000/month. Commercial subscription required for ads/subscriptions/app-store revenue.

**[51]** Open-Meteo. "API Subscriptions for Commercial Use." Substack.
<https://openmeteo.substack.com/p/api-subscriptions-for-commercial>
**Tier:** 2
Commercial API subscription: $29/month (1M calls), Pro/Enterprise tiers above.

**[52]** Open-Meteo. "Donations and Commercial Use." GitHub Issue #417.
<https://github.com/open-meteo/open-meteo/issues/417>
**Tier:** 4
Developer asked whether donations to a free open-source app constitute commercial use; ToS does not address this; issue closed without disclosed resolution.

**[53]** OpenWeatherMap. "API Pricing."
<https://openweathermap.org/price>
**Tier:** 1
Free: 60 calls/min, 1M/month; Startup/Developer/Professional/Expert paid tiers (10M to 3B calls/month).

**[54]** OpenWeatherMap. "API Guide / License." n.d.
<https://openweathermap.org/guide>
**Tier:** 1
ODbL license; mandatory on-screen "Weather data © OpenWeather" attribution; share-alike if redistributing adapted database.

**[55]** OpenWeatherMap (Free Code Camp forum). "Weather App: API Key Got Blocked."
<https://forum.freecodecamp.org/t/weather-app-api-key-got-blocked/65030>
**Tier:** 4
Documents OWM blocking a free-tier key for exceeding 60 rpm limit; open-source key exposure risk for embedded keys.

**[56]** Home Assistant (GitHub). "OpenWeatherMap cloud cover inverted." Issue #119873.
<https://github.com/home-assistant/core/issues/119873>
**Tier:** 4
OWM cloud cover reportedly inverted in HA (0% = overcast, 100% = clear); closed as "not planned"; root cause (OWM API vs HA mapping) not confirmed.

**[57]** Tomorrow.io Support. "Free API Plan Rate Limits."
<https://support.tomorrow.io/hc/en-us/articles/20273728362644-Free-API-Plan-Rate-Limits>
**Tier:** 2
Free plan: 500 requests/day, 25/hr, 3/sec; resets midnight UTC. **Access:** Page returned 403 during research; numbers from search snippets and corroborating Tomorrow.io FAQ pages.

**[58]** Visual Crossing. "Pricing / Editions."
<https://www.visualcrossing.com/weather-data-editions/>
**Tier:** 1
Free 1,000 records/day; Metered $0.0001/record; Professional 10M records/month; Corporate unlimited fair use; commercial use permitted from free tier with attribution.

**[59]** Visual Crossing. "Service Terms."
<https://www.visualcrossing.com/weather-service-terms/>
**Tier:** 1
Attribution: "Weather Data Provided by Visual Crossing" required at Metered/Professional tiers; non-compete clause: app cannot directly compete with Visual Crossing offering.

**[60]** MET Norway. "Terms of Service."
<https://api.met.no/doc/TermsOfService>
**Tier:** 1
User-Agent must contain contact email/website; >20 req/sec is "heavy traffic"; permanent ban for ToS violations; mobile push polling limited to once per 10 min; coords with >4 decimal places trigger 403.

**[61]** MET Norway. "License."
<https://api.met.no/doc/License>
**Tier:** 1
Dual license NLOD 2.0 + CC-BY 4.0; commercial use permitted; attribution required.

**[62]** MET Norway. "FAQ."
<https://api.met.no/doc/FAQ>
**Tier:** 1
Generic User-Agent triggers 403 on Locationforecast 2.0; permanent ban for deliberate violations; browser JS cannot set custom User-Agent.

**[63]** ECMWF. "ECMWF makes its entire real-time catalogue open to all." October 2025.
<https://www.ecmwf.int/en/about/media-centre/news/2025/ecmwf-makes-its-entire-real-time-catalogue-open-all>
**Tier:** 1
Effective October 1, 2025: full real-time catalogue open under CC-BY-4.0; 25 km publicly accessible subset; 9 km HRES planned for 2026 with 2-hour latency.

**[64]** WeatherAPI.com. "Pricing."
<https://www.weatherapi.com/pricing.aspx>
**Tier:** 1
Free 100,000 calls/month with attribution; Starter $7/mo for 3M calls; Pro+ $25/mo for 5M; Business $65/mo for 10M; commercial use permitted on all tiers; data resale prohibited.

**[65]** WeatherAPI.com. "Terms of Service."
<https://www.weatherapi.com/terms.aspx>
**Tier:** 1
"You may access, view and make copies of the data in the API for your personal or commercial use"; one API key per application; mandatory free-tier attribution.

**[66]** Meteomatics. "Free API Account."
<https://www.meteomatics.com/en/weather-api/>
**Tier:** 1
Free basic: 500 queries/day, 50/min, 10 parallel queries; 10-day forecast; 15 basic parameters; "for non-commercial = private projects only."

**[67]** weather.gov. "Disclaimer."
<https://www.weather.gov/disclaimer>
**Tier:** 1
NWS data is US public domain (17 USC §403); commercial use permitted; cannot claim copyright, imply endorsement, or modify and present as official.

**[68]** GitHub. "weather-gov/api Discussion #224 — NWS/Akamai stale cache."
<https://github.com/weather-gov/api/discussions/224>
**Tier:** 4
NWS/Akamai CDN served forecasts up to 27h 47m stale for months; programmatic clients hit cached responses while browsers got fresh data.

**[69]** GitHub. "weather-gov/api Discussion #492 — 981h stale forecast."
<https://github.com/weather-gov/api/discussions/492>
**Tier:** 4
Forecast data up to 981 hours (41 days) stale served via CDN cache; structural divergence between browser and API client cache keys.

**[70]** GitHub. "weather-gov/api Discussion #763 — Linode/DigitalOcean blocked."
<https://github.com/weather-gov/api/discussions/763>
**Tier:** 4
August 31, 2024: NWS blocked Linode and DigitalOcean IPs entirely after Akamai IPv6 advertisement change; affected developers with compliant usage for weeks.

**[71]** GitHub. "weather-gov/api Discussion #772 — 403 not 429 for rate limits."
<https://github.com/weather-gov/api/discussions/772>
**Tier:** 4
NWS rate-limit blocks return HTTP 403 (not 429); standard 429-retry logic fails silently; thresholds undocumented.

**[72]** Apple Developer Forums. "WeatherKit returning stale data." Thread 726148.
<https://developer.apple.com/forums/thread/726148>
**Tier:** 4
Confirmed Apple bug: WeatherKit returned current conditions 2+ hours stale; apps showed clear skies during active rain; no fix ETA at time of report.

**[73]** Y Combinator HN. "Open-Meteo creator on IP-based limits." Item 46591888.
<https://news.ycombinator.com/item?id=46591888>
**Tier:** 4
Open-Meteo creator confirms 600/min, 5,000/hr, 10,000/day are IP-based; explicitly "not ideal for shared hosting services like Cloudflare Workers" — shared-IP deployments aggregate quota.

**[74]** Open-Meteo. "Self-hosted Open-Meteo." Brightcoding blog.
<https://blog.brightcoding.dev/2026/02/05/open-meteo-the-revolutionary-free-weather-api-developers-crave>
**Tier:** 3
Self-hosting requires 500 GB+ storage and 2 TB+/day bandwidth; AGPLv3 commercial-disclosure obligation; paid API ($29/mo) is the practical commercial path.

**[75]** Hacker News. "AccuWeather discontinues free Core Weather API." 2025 thread.
<https://news.ycombinator.com/item?id=44663003>
<https://alternativeto.net/news/2025/7/accuweather-to-end-free-core-weather-api-access-with-new-portal-launch/>
**Tier:** 3 / Tier 4
AccuWeather replaced perpetual free with 14-day trial on September 9, 2025. Pattern of free-tier eliminations: weather underground → Yahoo → DarkSky → AccuWeather.

**[76]** 9to5Mac. "Apple shuts down Dark Sky API on March 31, 2023." June 2021 announcement.
<https://9to5mac.com/2021/06/10/dark-sky-apple-acquisition-shutdown-date/>
**Tier:** 3
Apple acquired Dark Sky 2020; API shutdown March 31, 2023; no migration path provided.

---

## Southeast US accuracy (Dim 4)

**[77]** James, E.P. & Turner, D.D. "Sources of Error in HRRR Surface Solar Radiation Forecasts." *Monthly Weather Review*, ahead of print 2025. DOI:10.1175/MWR-D-25-0094.1.
<https://journals.ametsoc.org/view/journals/mwre/aop/MWR-D-25-0094.1/MWR-D-25-0094.1.xml>
**Tier:** 1
Excessive SW↓ at all 14 SURFRAD stations across CONUS; cause is insufficient cloud attenuation plus dry water-vapor bias; experimental fixes cut bias 80–84% in fall/winter, only 35% in summer. **Access:** Full text not directly fetched in-session; abstract and search snippets used.

**[78]** Griffin, S.M. et al. "Seasonal Analysis of Cloud Objects in the High-Resolution Rapid Refresh (HRRR) Model Using Object-Based Verification." *J. Applied Meteor. Climatol.*, vol. 56 no. 8, 2017. DOI:10.1175/JAMC-D-17-0004.1.
<https://journals.ametsoc.org/view/journals/apme/56/8/jamc-d-17-0004.1.xml>
<https://www.ssec.wisc.edu/~jasono/papers/griffin_jamc_aug2017.pdf>
**Tier:** 1
HRRR cloud objects via MODE/GOES verification: too many small objects at initialization (especially August), too few oversized objects by FH2 ("cloud spin-up"); summer skill degrades after 1 h vs January.

**[79]** Skinner, P.S. et al. "Object-Based Verification of HRRR Forecasts of Severe Weather." *Weather and Forecasting*, vol. 36 no. 3, 2021. DOI:10.1175/WAF-D-20-0203.1.
<https://journals.ametsoc.org/view/journals/wefo/36/3/WAF-D-20-0203.1.xml>
**Tier:** 1
Large-sample (1,400 forecasts) radar object verification of HRRR warm season 2019; HRRR overforecasts convective storm objects over southern and eastern US, **most pronounced in southeastern US**.

**[80]** Burlingame, B.M. et al. "An Investigation of HRRR Surface Energy Balance over Northern Alabama." *Weather and Forecasting*, vol. 34 no. 3, 2019. DOI:10.1175/WAF-D-18-0184.1.
<https://journals.ametsoc.org/view/journals/wefo/34/3/waf-d-18-0184_1.xml>
**Tier:** 1
HRRRv2 evaluation in northern Alabama (closest direct SE US published study found); surface energy balance, radiation biases, seasonal patterns.

**[81]** Mathiesen, P. & Kleissl, J. "Evaluation of numerical weather prediction for intra-day solar forecasting in the continental United States." *Solar Energy*, vol. 85 no. 5, 2011. DOI:10.1016/j.solener.2011.02.018.
<https://www.sciencedirect.com/science/article/abs/pii/S0038092X11000570>
**Tier:** 1
GFS/NAM/ECMWF vs SURFRAD CONUS solar forecasting; ECMWF best in cloudy conditions; raw GFS/NAM positive bias up to 150 W/m² in forecast-clear conditions; MOS-corrected GFS achieves best RMSE (~85 W/m²), beating ECMWF.

**[82]** Ye, Y. & Chen, X. "On the Reliability of Cloud Forecasts for Astronomers." *MNRAS*, vol. 428 no. 4, 2013. DOI:10.1093/mnras/sts288.
<https://academic.oup.com/mnras/article/428/4/3288/1000251>
<https://arxiv.org/abs/1011.3863>
**Tier:** 1
GFS for astronomy: cloud detection probability 30–90% across sites; "GFS can identify less than half" of convective clouds globally (~45% detection); persistence model "is best of all for τ < 6 h"; layer/convective cloud forecasts "less reliable than total cloud forecast."

**[83]** Henderson, J. et al. "Convective Initiation Skill in High-Resolution NWP via GOES-16." *MWR*, 2021.
<https://www.ssec.wisc.edu/~jasono/papers/henderson_mwr_apr2021.pdf>
**Tier:** 1
State-of-the-art high-resolution NWP struggles with non-linear convective initiation events; SE US isolated convection driven by surface heating and BL inhomogeneities is poorly forecast.

**[84]** Yin, J. & Porporato, A. "Diurnal cloud cycle biases in climate models." *Nature Communications*, 2017.
<https://pmc.ncbi.nlm.nih.gov/articles/PMC5741665/>
**Tier:** 1
Climate-model land cloud peaks too early in the morning by 4–6 hours. Note: CMIP5 climate models, not NWP — direct extrapolation requires caution.

**[85]** Lledó, L. et al. "Scale-dependent verification of precipitation and cloudiness." *ECMWF Newsletter 174*, Winter 2023.
<https://www.ecmwf.int/en/newsletter/174/earth-system-science/scale-dependent-verification-precipitation-and-cloudiness>
**Tier:** 2
ECMWF HRES cloud FSS is scale-dependent; high-res 4.5 km outperforms coarser only for small-scale structures, coarser wins for large frontal systems.

**[86]** Haiden, T. et al. "Skill of ECMWF Cloudiness Forecasts." *ECMWF Newsletter 143*, 2015.
<https://www.ecmwf.int/sites/default/files/elibrary/2015/17326-skill-ecmwf-cloudiness-forecasts.pdf>
**Tier:** 2
ECMWF HRES cloud cover skill drops below persistence at approximately day 3; skill is low relative to geopotential, temperature, wind, and precipitation. **Access:** PDF not fetched directly; day-3 threshold confirmed via secondary citations.

**[87]** Min, Q. et al. "HRRR vs NY State Mesonet — Cloud-Driven Bias." *JGR-Atmospheres*, 2021.
<https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2021JD034989>
**Tier:** 1
HRRR overcast/thick-cloud conditions during warm season are main driver of positive SW↓ and warm-T biases; frontal/convective cloud conditions worst.

**[88]** Patel, P. et al. "GFS winter diurnal temperature error and sky-cover dependence." *Geophysical Research Letters*, 2021.
<https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2021GL095101>
**Tier:** 1
GFS diurnal T error: at 25% sky cover condition, 1°C warm bias at night, 2°C cold bias daytime — implicates GFS cloud-timing errors.

**[89]** Hahn, A. et al. "Verification of cloudiness and radiation forecasts." *Meteorologische Zeitschrift*, vol. 25 no. 1, 2016.
<https://www.schweizerbart.de/papers/metz/detail/25/84588/Verification_of_cloudiness_and_radiation_forecasts>
**Tier:** 1
ECMWF underestimates persistent low stratus over Alpine lowlands "especially in late autumn and early winter."

**[90]** NSSL EWP. "Convective Initiation Timing between PHS and HRRR." May 2024.
<https://inside.nssl.noaa.gov/ewp/2024/05/23/convective-initiation-timing-between-the-phs-and-hrrr/>
**Tier:** 2
HRRR delays afternoon convective initiation by 1–2 hours in the Southeast; excessive CIN persistence through afternoon (17Z HRRR waits until 23Z vs PHS at 21–22Z).

---

## Sub-hourly resolution (Dim 5)

**[91]** Open-Meteo. "Sub-hourly (15-minutely) Weather Forecasts." Substack.
<https://openmeteo.substack.com/p/sub-hourly-15-minutely-weather-forecasts>
**Tier:** 2
`minutely_15` backed by HRRR for North America, ICON-D2 / AROME for Central Europe; cloud cover NOT in native variable list — interpolated from hourly when requested.

**[92]** Open-Meteo. "GFS / HRRR API."
<https://open-meteo.com/en/docs/gfs-api>
**Tier:** 2
HRRR-backed minutely_15 variables for North America explicitly exclude cloud_cover (interpolated only).

**[93]** MET Norway. "Nowcast 2.0 Documentation."
<https://api.met.no/weatherapi/nowcast/2.0/documentation>
**Tier:** 1
MET Norway Nowcast: covers Norway/Sweden/Finland/Denmark only; 5-min update cycle; 2-hour forecast window via radar optical-flow; 8 variables, no cloud cover fraction.

**[94]** MET Norway. "Nowcast 2.0 Data Model."
<https://docs.api.met.no/doc/nowcast/datamodel.html>
**Tier:** 1
Nowcast variables: weather_symbol, T2m, precipitation_amount, precipitation_rate, RH2m, wind direction, wind speed 10m, wind gust 10m. No `cloudAreaFraction`.

**[95]** Hatfield, S. et al. "CloudCast — Total Cloud Cover Nowcasting with Machine Learning." arXiv:2410.21329, 2024.
<https://arxiv.org/abs/2410.21329>
<https://arxiv.org/html/2410.21329v2>
**Tier:** 2
NWP MEPS achieves MAESS ~0.3 (flat across all lead times); ML CloudCast (CNN on satellite) achieves ~0.75 at 15-min lead; EXIM optical flow falls below persistence at 15-min mark; "small-scale nature of cloud formation" makes prediction challenging; ~3-hour skillful satellite-extrapolation horizon.

**[96]** Lyman, J. & Mahoney, R. "Cloud nowcasting verification over complex terrain." Mountain Scholar.
<https://mountainscholar.org/items/d541de64-666c-4ede-8d6f-1bc4ccfa0c9f>
**Tier:** 2
Wind-displacement nowcast methods cannot beat persistence over complex terrain (Utah/Wyoming); persistence leads by up to 10% CSI in winter.

**[97]** Chu, Y. et al. "Intra-hour solar irradiance forecasting." iScience.
<https://pmc.ncbi.nlm.nih.gov/articles/PMC8531863/>
**Tier:** 1
"Neither NWP or WRF methods have been adopted operationally for intra-hour horizons by solar power plant managers." NWP cadence inadequate for intra-hour forecasting; persistence outperforms NWP at sub-hourly horizons.

**[98]** wgrib2. "Time interpolation."
<https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/time_interpolation.html>
**Tier:** 1
HRRR sub-hourly fields between F+H and F+H+1 are produced via linear time interpolation; no new meteorological information enters at interpolated steps.

---

## Ensemble / uncertainty (Dim 6)

**[99]** ECMWF. "Set III — Ensemble Forecasts."
<https://www.ecmwf.int/en/forecasts/datasets/set-iii>
**Tier:** 1
ENS: 51 members (50 perturbed + 1 control), 0.1° resolution option, 4 daily runs; cloud cover variables tcc/lcc/mcc/hcc.

**[100]** ECMWF. "ECMWF Forecast User Guide §2.1.5.2 Clouds."
<https://confluence.ecmwf.int/pages/viewpage.action?pageId=462552686>
**Tier:** 1
TCC/HCC/MCC/LCC definitions; pressure-level boundaries; cloud overlap assumption; TCC ≤ HCC + MCC + LCC by maximum-overlap.

**[101]** dynamical.org. "ECMWF IFS ENS forecast 15-day 0.25 degree."
<https://dynamical.org/catalog/ecmwf-ifs-ens-forecast-15-day-0-25-degree/>
**Tier:** 2
ENS open data via dynamical: 51 members (control + 50 perturbed), 0.25° grid, 360-hour horizon; TCC available.

**[102]** ECMWF. "ecmwf-opendata Python client." GitHub.
<https://github.com/ecmwf/ecmwf-opendata>
**Tier:** 1
`stream="enfo"`, `type=cf|pf|em|es|ep`, `number=1–50`, step ranges; per-member ENS access via Python client; no API key required.

**[103]** Open-Meteo. "Ensemble API."
<https://open-meteo.com/en/docs/ensemble-api>
**Tier:** 2
Per-member time series for ICON-D2-EPS (20 members), ICON-EU-EPS (40), GFS Ensemble (31), ECMWF IFS (51). `cloud_cover`, `cloud_cover_low/mid/high` per member at hourly cadence (7 days).

**[104]** Open-Meteo. "Probability parameter for cloud cover." GitHub Issue #349.
<https://github.com/open-meteo/open-meteo/issues/349>
**Tier:** 4
Proposed `p~cloudcover~lesseq~20` parameter syntax for cloud cover threshold probabilities; issue open and unimplemented as of research date.

**[105]** Open-Meteo. "Precipitation probability formula." GitHub Discussion #708.
<https://github.com/open-meteo/open-meteo/discussions/708>
**Tier:** 4
`precipitation_probability` = (#members > threshold / total members) × 100; cloud cover probability not provided by API.

**[106]** Hemri, S., Haiden, T. & Pappenberger, F. "Discrete Postprocessing of Total Cloud Cover Ensemble Forecasts." *Monthly Weather Review*, vol. 144 no. 7, 2016. DOI:10.1175/MWR-D-15-0426.1.
<https://journals.ametsoc.org/view/journals/mwre/144/7/mwr-d-15-0426.1.xml>
**Tier:** 1
Raw ECMWF cloud cover ensemble is "clearly underdispersive" at day 3; U-shaped PIT histograms at days 1 and 4; cloud cover ensemble skill is "worse than ensemble forecasts of other weather variables"; discrete/ordinal okta nature makes standard EMOS inapplicable. **Access:** Full text returned 403; abstract and DOI confirmed via ResearchGate.

**[107]** Dai, Y. & Hemri, S. "Spatially Coherent Postprocessing of Cloud Cover Ensemble Forecasts." *Monthly Weather Review*, vol. 149 no. 12, 2021.
<https://journals.ametsoc.org/view/journals/mwre/149/12/MWR-D-21-0046.1.xml>
**Tier:** 1
Univariate post-processing destroys spatial dependence structure of cloud cover; standard EMOS+ECC fails; cGAN required for spatially realistic output.

**[108]** Jakob, C. "Cloud Cover in the ECMWF Reanalysis." *Journal of Climate*, vol. 12 no. 4, 1999.
<https://journals.ametsoc.org/view/journals/clim/12/4/1520-0442_1999_012_0947_cciter_2.0.co_2.xml>
**Tier:** 1
Systematic biases: extratropical ocean cloud underestimated 10–15%; trade cumulus overestimated 10–15%; subtropical stratocumulus underestimated 15%.

**[109]** Astrospheric. "Cloud Ensemble." Help page.
<https://www.astrospheric.com/dynamiccontent/ensemble.html>
**Tier:** 2
Cloud ensemble blends RDPS + ICON + GFS + NBM with per-model percentages and color-coded agreement display; no calibrated probability number output.

---

## Caching and rate-limit (Dim 7)

**[110]** weather.gov. "Gridpoints FAQ — caching."
<https://github.com/weather-gov/api/blob/master/gridpoints.md>
**Tier:** 1
NWS gridpoint endpoint returns Cache-Control + Last-Modified; supports `If-Modified-Since` 304 conditional requests; `updateTime` field as JSON-body fallback.

**[111]** Open-Meteo. "Model Updates / Metadata API."
<https://open-meteo.com/en/docs/model-updates>
**Tier:** 2
`last_run_availability_time`, `update_interval_seconds`; recommend +10 min wait after model update due to distributed-server eventual consistency; "minor delays are fairly common"; metadata API calls don't count toward quota.

**[112]** PyPI. "openmeteo-requests Python client."
<https://pypi.org/project/openmeteo-requests/>
**Tier:** 2
Recommended client config: `expire_after=3600`, `retries=5`, `backoff_factor=0.2`; uses `requests-cache` + SQLite.

**[113]** GitHub. "open-meteo-cache-api community Redis proxy."
<https://github.com/soleinjast/open-meteo-cache-api>
**Tier:** 4
5-minute TTL Redis shared cache pattern for Open-Meteo to avoid 429.

**[114]** Open-Meteo. "How to store weather forecast data." Substack.
<https://openmeteo.substack.com/p/how-to-store-weather-forecast-data>
**Tier:** 2
Time-series gridded files; 3D arrays per cell, 168h sequential storage; mmap-backed; 2 ms response, 0.4 ms consecutive.

**[115]** LuckGrib. "HRRR Extended."
<https://luckgrib.com/models/hrrr_extended/>
**Tier:** 3
HRRR Extended runs 00/06/12/18Z to 48h; data availability ~1h50m post-init.

**[116]** Hydroforecast. "When forecasts are issued and available."
<https://support.hydroforecast.com/article/191-when-forecasts-are-issued-and-available>
**Tier:** 3
HRRR availability lag ~1.5h; GFS lag ~5.25h to f384.

**[117]** Cloudflare. "Workers — Cache using fetch."
<https://developers.cloudflare.com/workers/examples/cache-using-fetch/>
**Tier:** 2
`cacheTtl`, `cacheEverything`, `cacheTtlByStatus` options; data-center-local cache; query-string normalization required.

**[118]** Cloudflare. "Workers Cache API runtime reference."
<https://developers.cloudflare.com/workers/runtime-apis/cache/>
**Tier:** 2
Cache.put/match/delete; data-center-local; no `ignoreSearch`; Vary:* rejected.

**[119]** Cloudflare. "Cache Rules — Settings."
<https://developers.cloudflare.com/cache/how-to/cache-rules/settings/>
**Tier:** 2
"Respect Strong ETags" toggle; query-string controls Enterprise-only.

**[120]** PirateWeather. "API documentation — rate limit headers."
<https://docs.pirateweather.net/en/latest/API/>
**Tier:** 2
Returns `Ratelimit-Limit`, `Ratelimit-Remaining`, `Ratelimit-Reset`, `X-Forecast-API-Calls`; monthly quota model.

**[121]** Xweather. "Rate limiting — getting started."
<https://www.xweather.com/docs/weather-api/getting-started/rate-limiting>
**Tier:** 2
7 `X-RateLimit-*` headers (Limit/Remaining/Reset × minute + period + Period-Type).

**[122]** PyPI. "requests-ratelimiter."
<https://github.com/JWCook/requests-ratelimiter>
**Tier:** 2
Session-level rate limiter; `Retry-After` header support; per-second/minute limits.

**[123]** Meteomatics. "Downscaling — terrain effects."
<https://www.meteomatics.com/en/api/downscaling/>
**Tier:** 2
9–10 km ECMWF grid produces 3–6°C temperature errors in Alpine valleys vs peaks; nearest grid cell represents area average not point.

---

## Astrophoto-specific aggregators (Dim 8)

**[124]** Astrospheric. "Astrospheric Help / About."
<https://www.astrospheric.com/dynamiccontent/astrospheric.html>
**Tier:** 2
Models: Canadian RDPS (primary, 6h cadence), GFS, NAM, RAP (smoke), NBM (1h, 36h horizon, blends 40+ models including HRRR/ECMWF). Variables: cloud, transparency, seeing (0–5, Allan Rahill CMC algorithm), temperature, wind, sun/moon/planet positions, ISS pass, wildfire smoke (AOD via GFS).

**[125]** Astrospheric. "Data Domain."
<https://www.astrospheric.com/DynamicContent/datadomain.html>
**Tier:** 2
RDPS coverage: continental US + Canada + partial Mexico (excludes Hawaii); NBM has smaller CONUS+Alaska sub-domain. Southeast US is within RDPS domain.

**[126]** Astrospheric. "API Info."
<https://www.astrospheric.com/DynamicContent/api_info.html>
**Tier:** 2
REST API at `https://astrosphericpublicaccess.azurewebsites.net/api/`; requires Pro membership; 100 credits/day; GetForecastData_V1 = 5 credits, GetSky_V1 = 1 credit; 81-hour forecast at lat/lon.

**[127]** Astrospheric. "Subscription / Pricing."
<https://www.astrospheric.com/dynamiccontent/subscription.html>
**Tier:** 2
Pro subscription $2.99/month or $29.99/year; auto-renew terms.

**[128]** Astrospheric. "FAQ."
<https://www.astrospheric.com/dynamiccontent/faq.html>
**Tier:** 2
Self-acknowledgement: "It will be wrong at times. Even the Cloud Ensemble will be wrong at times." 200 million predictions every 6 hours; worldwide expansion "prohibitively expensive."

**[129]** Clear Outside. "Forecast home page."
<https://clearoutside.com/>
**Tier:** 2
Powered by Meteosource Weather API (commercial aggregator); free; no API; embed widget; covers low/medium/high cloud + total obscuration, dew, fog, ISS, Bortle, magnitude limit; no seeing or transparency index.

**[130]** First Light Optics. "Clear Outside — Weather Forecasts for Astronomers." Blog.
<https://www.firstlightoptics.com/blog/clear-outside-weather-forecasts-for-astronomers.html>
**Tier:** 2
2022 attribution: aggregate of UK Met Office, Norwegian Met Office, NOAA. Current site footer says "Powered by Meteosource."

**[131]** meteoblue. "Astronomical Seeing — Help."
<https://content.meteoblue.com/en/private-customers/website-help/outdoor-and-sports/astronomy-seeing>
**Tier:** 2
Cloud cover bands 0–4 km, 4–8 km, 8–15 km ASL; Seeing Index 1 (turbulent layer integration), Index 2 (density/flicker); jet stream >35 m/s correlates with poor seeing; "experimental" label; free 3-day, paid 7-day.

**[132]** meteoblue. "NEMS model documentation."
<https://content.meteoblue.com/en/research-education/specifications/data-sources/weather-simulation-data/meteoblue-models>
**Tier:** 2
Proprietary NEMS model family; NEMS2/NEMS_E variant builds on ECMWF; standard NEMS builds on GFS; ingests GFS, ECMWF IFS, DWD ICON, AROME ARPEGE.

**[133]** meteoblue. "Business Solutions / API Pricing."
<https://content.meteoblue.com/en/business-solutions/weather-apis>
**Tier:** 2
Free, €1,200, €2,400, €4,800/year tiers; credit system (basic_1h forecast 8,000 credits/call; 200M credits = 25,000 calls); astronomy widget available.

**[134]** Wikipedia. "Clear Sky Chart."
<https://en.wikipedia.org/wiki/Clear_Sky_Chart>
**Tier:** 2
CMC GEM model (Allan Rahill processing); ECMWF added 2020 to some charts; Attilla Danko (deceased) maintained the site; 6,100+ fixed sites; 48-hour limit; cirrus-specific modeling.

**[135]** Clear Sky Chart. "Credits."
<https://www.cleardarksky.com/csk/credits.html>
**Tier:** 2
CMC authorship; Schaefer/Sugarman darkness algorithm + Cinzano light pollution atlas; web-only; static PNG charts.

**[136]** Clear Sky Chart. "Coverage."
<https://www.cleardarksky.com/csk/coverage.html>
**Tier:** 2
North America boundary; site count 6,100+; 9-mile radius per chart; 48-hour forecast cap; no arbitrary lat/lon lookup.

**[137]** Clear Sky Chart. "FAQ #5."
<https://www.cleardarksky.com/csk/faq/5.html>
**Tier:** 2
CSC explicitly unavailable outside North America.

**[138]** 7Timer. "Documentation."
<https://www.7timer.info/doc.php>
**Tier:** 2
Sole NWP source: GFS (~1.5 million geographic points globally; ~28 km native at equator since GFS is 0.25°, varying by latitude). PNG graphical API at `astro.php?lon=X&lat=Y`; JSON/XML API at `api.pl?lon=X&lat=Y&product=astro&output=json`; no auth; non-commercial only ("you can use or redistribute them as long as you are not using them for commercial purpose"). ASTRO product variables (per source): cloud cover, astronomical seeing, atmospheric transparency, precipitation chances, atmospheric instability (lifted index), relative humidity warnings, wind speed warnings. 3-day ASTRO forecast horizon.

**[139]** Cloudy Nights forum. "How accurate is Astrospheric?"
<https://www.cloudynights.com/forums/topic/900151-how-accurate-is-astrospheric/>
**Tier:** 4
User reports Astrospheric wrong in both directions; CMC-RDPS lake-effect cloud failures over Ontario reported. **Access:** Returned 403; content from Google snippets.

**[140]** Cloudy Nights forum. "Clear Sky Chart inaccurate."
<https://www.cloudynights.com/topic/595123-clear-sky-chart-inaccurate/>
**Tier:** 4
1.5h drive based on CSC "perfect" forecast met 100% cloud; 3-day rain event under "good" CSC. **Access:** 403; Google snippets.

**[141]** Cloudy Nights forum. "Accuracy of Clear Sky Chart website."
<https://www.cloudynights.com/forums/topic/729800-accuracy-of-clear-sky-chart-website/>
**Tier:** 4
Community accuracy reports for CSC: 80% accuracy <12h ahead; 76% accuracy at 36–48h; pixel-based grid concerns. **Access:** 403; Google snippets.

**[142]** Cloudy Nights forum. "7 forecasts all agree but the sky doesn't."
<https://cloudynights.com/topic/728618-arghhhh-7-forecasts-all-agree-but-the-sky-doesnt>
**Tier:** 4
Community thread documenting all seven major astronomy weather apps simultaneously wrong on same night.

**[143]** Hart, Phil. "Cloud forecasts for astronomers."
<https://philhart.com/content/cloud-forecasts-astronomers>
**Tier:** 3
Independent practitioner evaluation: 7Timer APanel "seeing appears to almost always forecast a worst case"; GFS "not quite as good in terms of resolution as the Canadian model."

**[144]** Telescope Boss. "Weather Apps Astrospheric vs Clear Outside."
<https://telescopeboss.com/weather-apps-for-astronomy-astrospheric-vs-clearoutside/>
**Tier:** 4
Astrospheric: "there are times it will tell me it is clear, but when I look, there are clouds"; Clear Outside biased toward cloudy.

**[145]** AstroBackyard. "Best Weather App for Astronomy."
<https://astrobackyard.com/best-weather-app-astronomy/>
**Tier:** 3
Practitioner workflow: GOES-16/Zoom Earth satellite loops as primary near-real-time go/no-go; Astrospheric for forecast; multi-tool comparison; Astrospheric top pick for North America.

**[146]** GitHub. "AstroWeather Home Assistant integration."
<https://github.com/mawinkler/astroweather>
**Tier:** 4
DIY integration built on Met.no + Open-Meteo rather than aggregators — demonstrates DIY parity is achievable.

**[147]** jaglab.org. "Astro Forecast — Open-Meteo-driven custom seeing index."
<https://jaglab.org/astro-forecast/>
**Tier:** 3
Custom tool using Open-Meteo API directly; derives seeing index from temperature/dew spread, wind, humidity — same variables aggregators use.

**[148]** SkippySky. "Disclaimer."
<http://www.skippysky.com.au/dont_blame_me.txt>
**Tier:** 4
GFS-based, free, freeware terms; 0.5° (older claim) or 0.25° resolution.

---

## Satellite imagery and nowcasting (Dim 9)

**[149]** AWS. "NOAA GOES on AWS." Registry of Open Data.
<https://registry.opendata.aws/noaa-goes/>
**Tier:** 1
Buckets: `noaa-goes16`, `noaa-goes17`, `noaa-goes18`, `noaa-goes19` in us-east-1; no AWS account required (`--no-sign-request`); SNS notification ARN for GOES-19: `arn:aws:sns:us-east-1:123901341784:NewGOES19Object`.

**[150]** GitHub. "AWS open-data-docs — NOAA GOES-16 README."
<https://github.com/awslabs/open-data-docs/blob/main/docs/noaa/noaa-goes16/README.md>
**Tier:** 1
S3 path template `<Product>/<Year>/<DOY>/<Hour>/<Filename>`; product prefixes ABI-L2-ACMC (CONUS Cloud Mask), ABI-L2-ACHAF (Full Disk Cloud Top Height), ABI-L2-ACTPM (Mesoscale Cloud Phase).

**[151]** NESDIS. "GOES-19 Now Operational as GOES-East." April 2025 news.
<https://www.nesdis.noaa.gov/news/noaas-goes-19-now-operational-goes-east-providing-critical-new-data-forecasters>
**Tier:** 1
GOES-19 became operational GOES-East on April 7, 2025 (75.2°W); GOES-16 demoted to backup. Real-time SE US data should be sourced from `noaa-goes19`.

**[152]** GOES-R Program. "ABI Scan Mode Info."
<https://www.goes-r.gov/users/abiScanModeInfo.html>
**Tier:** 1
Mode 6 (operational since April 2, 2019): Full Disk every 10 min, CONUS every 5 min, Mesoscale every 60 sec (or 30 sec single-domain).

**[153]** NCEI. "ABI Level 2 Clear Sky Mask metadata." DOI 10.7289/V5SF2TGP.
<https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C01503>
**Tier:** 1
ACM (Clear Sky Mask): 2 km resolution, NetCDF4, archive start April 19, 2017; output 4 classes (clear / probably clear / probably cloudy / cloudy).

**[154]** NCEI. "ABI Level 2 Cloud Top Phase metadata." DOI 10.7289/V5NP22QW.
<https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C01504>
**Tier:** 1
ACTP: 2 km, archive start May 16, 2017; phase categories warm liquid/supercooled/mixed/ice.

**[155]** NCEI. "ABI Level 2 Cloud Top Height metadata." DOI 10.7289/V5HX19ZQ.
<https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C01505>
**Tier:** 1
ACHA: upgraded to 2 km on March 24, 2023 (was 10 km Full Disk/CONUS, 4 km Mesoscale); archive start May 16, 2017.

**[156]** NOAA STAR. "Clear Sky Mask Algorithm Working Group."
<https://www.star.nesdis.noaa.gov/goesr/product_cp_clearskymask.php>
**Tier:** 1
ACM uses 9 of 16 ABI bands; CALIPSO validation; experimental-use caveat on STAR pages (NCEI archival is operational).

**[157]** NOAA STAR. "Cloud Top Properties."
<https://www.star.nesdis.noaa.gov/goesr/product_cp_cloud.php>
**Tier:** 1
Product acronyms ACHA (height/temp/pressure), ACTP (phase), DCOMP/NCOMP (microphysics).

**[158]** NSSL. "MRMS Project."
<https://www.nssl.noaa.gov/projects/mrms/>
**Tier:** 1
MRMS: 1 km × 2 min update cycle; 33 vertical levels; CONUS + Alaska + Hawaii + Caribbean + Guam; 100+ products; operational since 2014.

**[159]** AWS. "NOAA MRMS PDS." Registry of Open Data.
<https://registry.opendata.aws/noaa-mrms-pds/>
**Tier:** 1
Bucket `noaa-mrms-pds` in us-east-1; no auth; 2-min real-time delivery; SNS `arn:aws:sns:us-east-1:123901341784:NewMRMSObject`.

**[160]** AWS. "NOAA HRRR PDS." Registry of Open Data.
<https://registry.opendata.aws/noaa-hrrr-pds/>
**Tier:** 1
Bucket `noaa-hrrr-bdp-pds` in us-east-1; hourly updates; 3 km resolution; no AWS account required; HRRR-Smoke variables not separately confirmed in registry text.

**[161]** Tzallas, V. et al. "Performance Evaluation of the GOES-16 ACM Using CALIPSO." *Remote Sensing*, vol. 12 no. 10, 2020. DOI:10.3390/rs12101630.
<https://pmc.ncbi.nlm.nih.gov/articles/PMC8243760/>
<https://www.mdpi.com/2072-4292/12/10/1630>
**Tier:** 1
GOES-16 ACM vs CALIPSO: overall accuracy 86.0%; cloud detection 90.9%; clear-sky detection only 74.8%; **daytime clear-sky drops to 66.6%**; majority of missed clouds within 2 km AGL; performance degrades north of 36°N in winter daytime.

**[162]** Sherwood, S.C. et al. "Underestimation of deep convective cloud tops by thermal-infrared retrievals." *Geophysical Research Letters*, 2004. DOI:10.1029/2004GL019699.
<https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2004GL019699>
**Tier:** 1
GOES-8 thermal IR underestimates deep convective cloud tops by ~1 km on average vs CRYSTAL-FACE CPL lidar; up to 2 km low for tallest cells; sub-top emission mechanism applies to GOES-16/19 ACHA.

**[163]** Tan, Z. et al. "GOES-16 ABI thin cirrus over land." *J. Atmos. Ocean. Tech.*, vol. 39 no. 9, 2022.
<https://journals.ametsoc.org/view/journals/atot/39/9/JTECH-D-21-0160.1.xml>
**Tier:** 1
ABI 1.378 µm cirrus band is daytime-only (SZA < 80°); precipitable water variations cause misclassification of optically thin clouds.

**[164]** Stelzel, K. & Lindsey, D. "Maritime thin cirrus detection." *J. Atmos. Ocean. Tech.*, 2021.
<https://journals.ametsoc.org/view/journals/atot/38/6/JTECH-D-20-0130.1.xml>
**Tier:** 1
ABI 1.38 µm channel relies on solar scattering; nighttime detection is impossible by design.

**[165]** Miller, S.D. et al. "Day/Night Band confirms IR algorithm overstates nighttime low clouds." *Earth and Space Science*, 2022.
<https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/2021EA002137>
**Tier:** 1
Bi-spectral 11–3.9 µm BTD overstates low cloud at night where cool ocean upwelling lies beneath warm moist atmosphere; DNB ground truth confirms IR false alarm.

**[166]** Kassianov, E. et al. "Ground-based fractional sky cover vs satellite nadir." *J. Appl. Meteor. Climatol.*, 2005.
<https://journals.ametsoc.org/view/journals/apme/44/1/jam-2184.1.xml>
**Tier:** 1
160° FOV ground-based sky cover overestimates satellite nadir cloud fraction by >50% for individual retrievals; geometric incompatibility.

**[167]** AVWX Training. "ASOS automated ceiling reports."
<https://www.avwxtraining.com/post/what-you-need-to-know-about-automated-ceiling-reports>
**Tier:** 3
ASOS reports clouds only below 12,600 ft AGL; overcast at 15,000 ft reported as "clear sky." NC/SC documented case of satellite-clear / ASOS-overcast disagreement.

**[168]** Zhang, J. et al. "Multi-Radar Multi-Sensor (MRMS): Initial operating capabilities." *BAMS*, 2016.
<https://journals.ametsoc.org/view/journals/bams/97/4/bams-d-14-00174.1.xml>
**Tier:** 1
MRMS QPE Pass 1 latency 20 min, Pass 2 60 min; "not as useful during flash flood warning operations"; western US terrain blockage gaps.

---

## Counter-perspective sources (cross-cutting)

**[169]** Bonavita, M. et al. "Discussion of NWP cloud parameterization at peak performance." *BAMS DoD Workshop*, 2024.
<https://journals.ametsoc.org/view/journals/bams/105/6/BAMS-D-24-0077.1.xml>
**Tier:** 1
Some experts argue NWP microphysical schemes have "reached peak performance at two moments"; subgrid cloud fraction estimation via RH thresholds fundamentally inadequate.

**[170]** ECMWF. "Verifying high-resolution forecasts." Science blog 2023.
<https://www.ecmwf.int/en/about/media-centre/science-blog/2023/verifying-high-resolution-forecasts>
**Tier:** 1
Double-penalty problem at high resolution; FSS required for fair assessment; no cloud-specific quantitative improvement at km-scale.

**[171]** Bouallègue, Z.B. et al. "AIFS 1.1.0 update." Egusphere preprint 2025.
<https://egusphere.copernicus.org/preprints/2025/egusphere-2025-4716/>
**Tier:** 2
AIFS 1.1.0 acknowledges flat cloud cover distribution as inherent MSE-training limitation, structurally not fixable in deterministic training.

**[172]** Lamb, K. "Microphysical biases persist." *JAMES*, 2026.
<https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2025MS005341>
**Tier:** 1
Double-moment microphysics schemes show "systematic biases persist" and "greater microphysical sophistication appears to provide relatively minimal benefit."

**[173]** Han, J.-Y. et al. "WeatherReal benchmark." arXiv:2409.09371, 2024.
<https://arxiv.org/html/2409.09371v1>
**Tier:** 2
Total cloud cover has highest RMSE across all variables and models in WeatherReal benchmark; fewer (8,981 vs 12,901) QC'd observation stations available for cloud than temperature.

**[174]** WPC. "GFS QPF documentation — Arakawa-Schubert convective scheme."
<https://www.wpc.ncep.noaa.gov/research/model_qpf_files/Page324.htm>
**Tier:** 1
GFS Arakawa-Schubert "very susceptible to grid scale convective blow-ups" in moist/unstable airmasses; warm-season QPF bias ~1.6 (overforecast); peak convection too early (15Z / 11AM local).

**[175]** Frontiers. "Forecast error and cloud cover correlation."
<https://www.frontiersin.org/journals/earth-science/articles/10.3389/feart.2023.1099344/full>
**Tier:** 1
Frontiers 2023 study: ECMWF temperature forecast error correlates with cloud cover at r = 0.85–0.95, indicating persistent cloud cover misrepresentation drives downstream temperature errors.

---

## Notes on access

Sources marked with `**Access:**` notes were not directly fetched in-session (typically due to 403 errors, paywall walls, or sites that block AI crawlers). For these, the extracted claims rest on:
- Search-result snippets (used by Discovery agents)
- Secondary citations of the same primary work
- Abstract/metadata pages that *were* fetchable

Phase 4 verification is responsible for re-fetching cited URLs and grading
each claim against actual source content — INACCESSIBLE results are expected
in the audit per the cited-research methodology's 20–30% inaccessibility expectation.
