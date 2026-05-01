# Citations

All sources used in this research, numbered for inline reference. Quality tiers
follow the cited-research methodology:

- **Tier 1**: Peer-reviewed paper, government/institutional report
- **Tier 2**: Manufacturer spec, established reference site, university publication
- **Tier 3**: Industry blog, conference talk, well-known practitioner
- **Tier 4**: Forum, personal blog, GitHub discussion, social media

Citations marked **(verified)** were directly fetched and quoted in-session.
Citations marked **(unverified)** were extracted by Phase 1 sub-agents from search
snippets but the full source content could not be re-fetched in-session (403,
PDF parse failure, paywall, or fetch budget). The Phase 4 audit grades each.

---

## Atmospheric extinction physics & observatory baselines

1. **Patat et al. 2011** — *Optical atmospheric extinction over Cerro Paranal*. A&A 527, A91. <https://www.aanda.org/articles/aa/full_html/2011/03/aa15537-10/aa15537-10.html> — **Tier 1, verified**. Decomposes extinction into Rayleigh, aerosol, ozone, telluric. Aerosol coefficient k₀ = 0.013 ± 0.002 mag/airmass at reference wavelength; Ångström exponent α = −1.38 ± 0.06; spectral 3300–8000 Å. Notes detectable El Chichón volcanic residual below 4000 Å decades after eruption.

2. **Buton et al. 2013** — *Atmospheric extinction properties above Mauna Kea from the Nearby SuperNova Factory*. A&A 549, A8. <https://www.aanda.org/articles/aa/full_html/2013/01/aa19834-12/aa19834-12.html> — **Tier 1, partial verification**. 4285 spectra from 478 nights at Mauna Kea, 2004–2011, spectral 3200–9700 Å. SNIFS on UH 2.2m. Discovery agent reported median V = 0.11, B = 0.19 mag/airmass; band-specific values not exposed in our re-fetch and are flagged as DRIFT pending direct verification.

3. **IAC observatory monitoring** — *Atmospheric extinction and AOD at the Canary Islands observatories*. <https://www.iac.es/en/observatorios-de-canarias/sky-quality/sky-quality-parameters/atmospheric-extinction-and-aerosol-optical-depth> — **Tier 1, verified**. Median V-band extinction at ORM = 0.130 mag/airmass (Carlsberg Meridian Telescope, 1984–2013). Photometric threshold 0.153 mag/airmass. ~20% of dust outbreaks reach observatory altitudes; July–August calimas dominate. AERONET sun photometers measure 340–1640 nm.

4. **Sky & Telescope** — *Transparency and atmospheric extinction*. <https://skyandtelescope.org/astronomy-resources/transparency-and-atmospheric-extinction/> — **Tier 2, unverified**. Practitioner-focused explainer of AOD-to-magnitude conversion (×1.086 factor), typical AOD ranges by region (eastern US ~0.2, hazy ≥0.5).

5. **Ångström exponent** — Wikipedia. <https://en.wikipedia.org/wiki/Angstrom_exponent> — **Tier 3, unverified**. Formula AOD(λ) = AOD(λ₀)(λ/λ₀)^(−α); typical α 0–0.5 (coarse mode/dust), 1.5–2.5 (fine mode urban/smoke).

6. **Bodhaine et al. 1999** — *On Rayleigh optical depth calculations*. <https://web.gps.caltech.edu/~vijay/Papers/Rayleigh_Scattering/Bodhaine-etal-99.pdf> — **Tier 1, unverified**. Definitive Rayleigh OD formula used in atmospheric extinction modeling.

7. **Hand & Malm 2007** — *Review of aerosol mass scattering efficiencies*. JGR. <https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2007jd008484> — **Tier 1, unverified**. Mass scattering efficiency: dry ammonium sulfate 2.5 ± 0.6 m²/g; nitrate 2.7 ± 0.5 m²/g, both at 550 nm. Foundational for PM2.5→extinction conversion.

8. **Stubbs & Vaz** (NIST/Harvard, OSTI) — *Comparison of MODTRAN5 atmospheric extinction predictions with narrowband astronomical flux observations*. <https://www.osti.gov/pages/servlets/purl/1784950> — **Tier 1, unverified**. Best-fit narrowband photometric extinction model (380–840 nm) at a dark site required zeroing the aerosol scattering term to match observations within 0.013 mag/airmass.

9. **Petržala & Kocifaj 2026** — *PM2.5 as a proxy for aerosol optical depth in night-sky-brightness applications*. MNRAS 548, stag712. <https://academic.oup.com/mnras/article/548/3/stag712/8654590> — **Tier 1, unverified**. Physics-based PM2.5→AOD model; achieves R = 0.998 under controlled conditions but raw empirical PM2.5/AOD R² is "well below 0.6" without humidity and PBL-height correction.

10. **Cinzano & Falchi 2021** — *Air pollution mitigation and night sky brightness*. Scientific Reports. <https://www.nature.com/articles/s41598-021-94241-1> — **Tier 1, unverified**. Reducing aerosol load decreases night sky brightness by tens of percent near light sources; second-order scatter ≤18%.

## PM2.5 / AOD coupling (and decoupling)

11. **Fu et al. 2022** — *Decoupling between PM2.5 concentrations and AOD at ground stations in China*. Frontiers in Environmental Science. <https://www.frontiersin.org/journals/environmental-science/articles/10.3389/fenvs.2022.979918/full> — **Tier 1, verified**. 19 stations, 2017–2019. Daily PM2.5/AOD R = 0.03–0.60 across sites. Specific humidity range 2.83–11.89 g/kg drives most of the decoupling. Predictive R: AOD-only 0.49, AOD+humidity 0.74, AOD+four met factors 0.81.

12. **ACP 2014** — *Surface-to-column representativeness of the PM2.5/AOD relationship in the contiguous US*. <https://acp.copernicus.org/articles/14/6049/2014/> — **Tier 1, unverified**. Seasonal phase inversion at ~half of US sites: AOD peaks summer, PM2.5 peaks winter.

13. **Jiang et al. 2024** — *Characteristics of daytime and nighttime AOD differences over China*. JGR Atmospheres. <https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2023JD039158> — **Tier 1, unverified**. Nighttime AOD below 1 km is 58.5% larger than daytime in model, driven almost entirely by hygroscopic growth (dry mass only 2.6% higher). CALIOP observations: 41.3% larger.

14. **Balmes 2021** — *Diurnal AOD variation at ARM SGP*. <https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2021EA001852> — **Tier 1, unverified**. Annual-mean day vs night AOD differs 1–3% but day-to-day spread reaches ±0.2.

15. **MDPI 2021** — *Variations in nocturnal residual layer height and effects on surface PM2.5*. <https://www.mdpi.com/2072-4292/13/22/4717> — **Tier 1, unverified**. Boundary layer collapse at sunset concentrates aerosol at surface without changing column AOD.

16. **Chew et al. 2016 (PMC)** — *Surface PM2.5 vs column AOD by altitude*. <https://pmc.ncbi.nlm.nih.gov/articles/PMC7398152/> — **Tier 1, unverified**. R² 0.29–0.54 for aerosol below 1.3 km; R² collapses to 0.03–0.21 above 1.3 km. 58% of aerosol scale-height measurements placed mass above 1.35 km.

17. **Zhu et al. 2024** — *Aerosol composition and the PM2.5/AOD ratio*. ACP. <https://acp.copernicus.org/articles/24/11565/2024/> — **Tier 1, unverified**. η (PM2.5 per unit AOD) varies 7.8 µg/m³ (Hawaii) to 504 µg/m³ (Mongolia); dust regions 3× sulfate regions.

## PurpleAir correction & sensor quality

18. **Barkjohn et al. 2021** — *US-wide correction for PM2.5 from PurpleAir*. AMT 14, 4617–4637. <https://amt.copernicus.org/articles/14/4617/2021/> — **Tier 1, verified**. Equation: `PM2.5 = 0.524 × PA_cf_1 − 0.0862 × RH + 5.75` (RH in %). RMSE 8 → 3 µg/m³. 50 sensors, 16 states, 39 sites. Limitations: only 3 rural sites, high-concentration validity uncertain, bias at T < −12 °C.

19. **Jaffe et al. 2023** — *Evaluation of EPA correction under smoke, dust, wintertime*. AMT 16, 1311–1322. <https://amt.copernicus.org/articles/16/1311/2023/> — **Tier 1, verified**. Corrected PAS data accurate in smoke (slope 0.99 at Keeler) and urban (slope 1.00) but **too low by factor 5–6 in dust** (slope 5.6 at Keeler). Published 13 March 2023.

20. **Searle et al. 2023** — *Plantower PMS5003 hardware revision*. Atmospheric Environment. <https://www.sciencedirect.com/science/article/abs/pii/S0021850223001210> — **Tier 1, unverified**. June 2021+ hardware variant biased low ~3 µg/m³ below 16 µg/m³. >10% of network affected.

21. **AMT 2024 high-RH PurpleAir correction** <https://amt.copernicus.org/articles/17/6735/2024/> — **Tier 1, unverified**. Models PurpleAir correction degradation under high-RH conditions; high-RH/high-concentration interaction "unclear."

22. **PurpleAir wildfire smoke evaluation 2022** (PMC) <https://pmc.ncbi.nlm.nih.gov/articles/PMC9784900/> — **Tier 1, unverified**. Only 5 of 15 smoke-impacted sites met EPA performance targets at 1-hour averages with corrected data. Correction breaks above 300 µg/m³.

## Air quality APIs

23. **AirNow API** — <https://docs.airnowapi.org/> — **Tier 1, verified (landing)**. Public US/Canada/Mexico API, 2,500+ monitoring stations, forecasts for 500+ cities, real-time observations, free public registration. Detailed rate limits/endpoint base URL not exposed on landing.

24. **AirNow webservices reference** — <https://docs.airnowapi.org/webservices> — **Tier 1, unverified**. Bbox observation, forecast, contour KML endpoints documented; reconstructed pattern `/aq/observation/bbox/`.

25. **AirNow NowCast forum** — <https://forum.airnowtech.org/t/the-nowcast-for-pm2-5-and-pm10/172> — **Tier 1, unverified**. NowCast = 12-hour weighted PM2.5 average; weight = 1−(range/max), min 0.5; updated August 2013 to be more responsive to wildfire events.

26. **OpenAQ API v3** — <https://docs.openaq.org/> — **Tier 2, verified (partial)**. v3 confirmed; X-API-Key auth; AirNow listed as a provider; per-location licenses (e.g., US Public Domain). Discovery agent reported 60 req/min, 2000 req/hr rate limits and pass-through ingestion (no QA/QC) — needs separate verification from rate-limits/terms subpages.

27. **EPA AQS Data Mart** — <https://aqs.epa.gov/aqsweb/documents/data_api.html> — **Tier 1, unverified**. FRM/FEM regulatory archive. Discovery agent reported 6+ month lag, 10 req/min recommended, query rows capped 2M; not real-time. PM2.5 FRM parameter code 88101.

28. **PurpleAir API** — <https://api.purpleair.com/> — **Tier 2, unverified**. Points-based pricing (1M free start, ~$0.01/sensor/day at 10-min poll cadence). Key fields `pm2.5_cf_1` (for Barkjohn input), `pm2.5_atm`, `pm2.5_alt`, `humidity`. A/B channel agreement is the standard QC.

29. **WAQI API** — <https://aqicn.org/api/> — **Tier 2, unverified**. Free token; 1000 req/sec default. **Hard license blocker**: data "cannot be sold or included in sold packages" — commercial app use requires separate agreement.

30. **IQAir AirVisual API** — <https://api-docs.iqair.com/> — **Tier 2, unverified**. Community tier free (city/station AQI only, no raw PM2.5); Startup/Enterprise paid for raw concentration. Default ToS restricts commercial use.

31. **Sensor.Community** — <https://github.com/opendata-stuttgart/meta/wiki/EN-APIs> — **Tier 3, unverified**. No-auth real-time JSON at `data.sensor.community/static/v2/data.json`; `airrohr/v1/filter/?box=` for geographic filtering. Plantower SDS011/PMS5003 sensors. Daily CSV archive 2015→present.

32. **EEA Air Quality Download Service** — <https://www.eea.europa.eu/en/datahub/datahubitem-view/778ef9f5-6293-4846-badd-56a29c70880d> — **Tier 1, unverified**. EU regulatory data; E1a verified annual, E2a near-real-time; Parquet format.

33. **CAMS Atmosphere Data Store** — <https://ads.atmosphere.copernicus.eu/> — **Tier 1, unverified**. Global PM2.5 reanalysis (EAC4, 2003–Dec 2024) and 5-day NRT forecast at ~40 km. Free with cdsapi Python client. CC-BY license.

34. **CAMS GFAS** — <https://ads.atmosphere.copernicus.eu/datasets/cams-global-fire-emissions-gfas> — **Tier 1, unverified**. Global fire emissions, 0.1° resolution, daily, CC-BY.

## Pollen data sources

35. **Google Pollen API coverage** — <https://developers.google.com/maps/documentation/pollen/coverage> — **Tier 1, verified**. **80 countries** (NOT 65+ as some secondary sources state). US tree species: maple, elm, cottonwood, alder, birch, ash, **pine**, oak, juniper. Reduced-coverage countries enumerated (grass-only in 13 countries; partial in Japan, Canada). No subspecies resolution.

36. **Google Pollen API billing** — <https://developers.google.com/maps/documentation/pollen/usage-and-billing> — **Tier 1, unverified**. Pay-as-you-go $10 CPM (per Maps Platform schedule); discovery agent noted free $200 monthly credit expired Feb 28 2025 — needs re-verification.

37. **Ambee Pollen API docs** — <https://docs.ambeedata.com/apis/pollen> — **Tier 2, verified**. Endpoints `/latest/`, `/history/`, `/forecast/`, `/forecast/v2/pollen/120hr/`. NA species: Oak, Cypress/Juniper/Cedar, Mulberry, Pine, Elm, Ash, Birch, Maple, Poplar/Cottonwood, Ragweed, Grass. **No Pinus species resolution for NA**. `x-api-key` auth.

38. **Ambee marketing page** — <https://www.getambee.com/api/pollen> — **Tier 3, unverified**. 100 free records/day; 150+ countries; 500m resolution; 7-year historical; "93% correlation with ground-truth" (vendor claim, not peer-reviewed).

39. **Atmospore** — <https://atmospore.com/api-docs>, <https://atmospore.com/plans> — **Tier 3, unverified**. Tiers: Starter €9/mo (500 calls/day), Professional €39/mo (5K), Enterprise €149/mo (50K). 7–14 day forecast. Smaller, newer provider.

40. **Tomorrow.io pollen** — <https://docs.tomorrow.io/reference/data-layers-pollen> and <https://support.tomorrow.io/hc/en-us/articles/31227084428052-Pollen-Premium-Layer> — **Tier 2, unverified**. Premium layer; sales contact required; doc page returns 403 to public.

41. **NC DEQ pollen monitoring** — <https://www.deq.nc.gov/about/divisions/air-quality/air-quality-monitoring/pollen-monitoring> — **Tier 1, verified**. Single station at 4403 Reedy Creek Road, Raleigh, NC. Operates late-Feb to mid-Nov, M–F. Reports trees/grasses/weeds. Live HTML page at `xapps.ncdenr.org/aq/ambient/Pollen.jsp`.

42. **NC State Extension — pine pollen GDD** — <https://content.ces.ncsu.edu/predicting-the-start-of-the-pine-pollen-season> — **Tier 1, verified**. Onset ≈300 GDD (Boyer 1978); peak ≈636 GDD (Baker & Langdon 1990). Base 55°F, accumulate from Feb 1. No published uncertainty range. Implementable from any weather API.

43. **NC State Forestry Extension — pine pollen** — <https://forestry.ces.ncsu.edu/news/pine-pollen-season/> — **Tier 1, unverified**. Pine pollen is the visible yellow-film species but not the main allergen (oak, birch, grass dominate allergens).

44. **AAAAI National Allergy Bureau** — <https://www.aaaai.org/global/nab-pollen-counts/counting-stations> — **Tier 1, unverified**. ~85 US stations using Burkard volumetric traps. **No public API**; data release by formal request.

45. **Open-Meteo Air Quality API** — <https://open-meteo.com/en/docs/air-quality-api> — **Tier 2, unverified**. Free non-commercial; **Europe-only pollen** (alder, birch, grass, mugwort, olive, ragweed). CAMS-backed. No North American pollen.

46. **CAMS pollen** — <https://atmosphere.copernicus.eu/how-cams-pollen-information-serves-local-level> — **Tier 1, unverified**. Europe-only, 6 species, 4-day forecast, 10 km resolution. Not viable for NC.

47. **SILAM (Finnish Met Inst.)** — <https://silam.fmi.fi/> — **Tier 1, unverified**. Open-source pollen transport model; covers Europe/N. Europe/SE Asia; no North America operational domain.

48. **Pollen forecast accuracy study** (PMC 2025) — <https://pmc.ncbi.nlm.nih.gov/articles/PMC12834900/> — **Tier 1, unverified**. AccuWeather: 7% concordance for grass, 33% for ragweed, 56% for mold. The Weather Channel: 29% grass, 34% ragweed. No statistically significant association in Fisher exact tests.

49. **Pollen apps validation** (PMC 2017) — <https://pmc.ncbi.nlm.nih.gov/articles/PMC5440733/> — **Tier 1, unverified**. 9 apps across 4 European cities; best 62.9% exact hit rate; worst <40%; calls for mandatory QC.

50. **Pinus taeda aerobiology** (Dantic & Franklin 2009) — <https://cdnsciencepub.com/doi/10.1139/X08-062> — **Tier 1, unverified, partial access**. Peak 1,480 grains/m³ during active shedding from plantation; settling velocity 2.1 cm/s.

51. **Pollen optical depth** (Noh et al. 2013, lidar) — <https://eurekalert.org/news-releases/469586> and <https://acp.copernicus.org/articles/13/7619/2013/acp-13-7619-2013.html> — **Tier 1, unverified**. Pollen can account for 25–97% of aerosol optical depth during spring daytime peak. Lidar shows pollen aloft collapses after 18:00 local time.

52. **Diurnal pollen variation** (Grewling et al., PMC) — <https://pmc.ncbi.nlm.nih.gov/articles/PMC5106497/> — **Tier 1, unverified**. Ragweed nighttime ground-level concentrations exceed daytime by >30%; birch day/night peaks nearly equal. Counters the "pollen settles overnight" assumption.

## Wildfire smoke forecasting

53. **HRRR-Smoke (NOAA GSL)** — <https://rapidrefresh.noaa.gov/hrrr/HRRRsmoke/> — **Tier 1, unverified (403 on re-fetch)**. Operational hourly 3 km CONUS smoke forecast. GRIB2 variables `MASSDEN` (8 m AGL near-surface, kg/m³) and `COLMD` (column total). Smoke from biomass burning only.

54. **NOAA NOMADS HRRR** — <https://nomads.ncep.noaa.gov/pub/data/nccf/com/hrrr/prod> — **Tier 1, unverified**. HRRR GRIB2 file pattern `hrrr.tCCz.wrfsfcfHH.grib2`; AWS S3 mirror at `noaa-hrrr-bdp-pds`.

55. **NOAA NESDIS HMS smoke polygons** — <https://www.ospo.noaa.gov/products/land/hms.html> — **Tier 1, unverified**. Light/medium/heavy density polygons; shapefile + GeoTIFF + KML at `satepsanone.nesdis.noaa.gov/pub/FIRE/web/HMS/Smoke_Polygons/`. Daily updates; no forecast horizon.

56. **NASA FIRMS API** — <https://firms.modaps.eosdis.nasa.gov/api/area/> — **Tier 1, verified**. URL pattern `/api/area/csv/[MAP_KEY]/[SOURCE]/[AREA_COORDINATES]/[DAY_RANGE]`. 8 sensor variants (MODIS, VIIRS SNPP/NOAA-20/NOAA-21, LANDSAT for US/CA). 5000 transactions / 10 min rate limit. Free MAP_KEY. 5-day max range per query.

57. **AirNow Fire & Smoke Map** — <https://fire.airnow.gov> — **Tier 1, unverified**. Composites HMS smoke layer + regulatory monitors + corrected PurpleAir; no separate documented API distinct from AirNow main API.

58. **Astrospheric smoke documentation** — <https://www.astrospheric.com/dynamiccontent/smoke.html> — **Tier 2, verified**. Existing astrophotography app explicitly states: "The smoke layer presented on Astrospheric integrates smoke and aerosols in the entire column of air above a particular point" and "The smoke forecast should not be used as an air quality forecast." Confirms competitor handling of column-vs-surface confound.

59. **ACP 2021 Williams Flats intercomparison** — <https://acp.copernicus.org/articles/21/14427/2021/> — **Tier 1, verified**. 12 forecasting systems (3 global + 9 regional) for Williams Flats fire (44,446 acres, WA, Aug 2019). All underpredicted AOD: NMB −87.4% to −4.3%; r ≤ 0.50 spatial correlation. FRP-based emissions 6.4× higher than hotspot-based. FRP-based models generally outperformed.

60. **CIMSS GOES nighttime smoke detection** — <https://cimss.ssec.wisc.edu/satellite-blog/archives/41707> — **Tier 1, unverified**. Nighttime smoke "not present at all in infrared imagery" — requires solar or lunar illumination.

61. **Camp Fire HRRR-Smoke evaluation** (Berkeley) — <https://vcresearch.berkeley.edu/news/new-study-evaluates-noaas-wildfire-smoke-forecasting-model> — **Tier 2, unverified**. HRRR-Smoke underpredicted Camp Fire PM2.5 by up to 70% during smoke-on-smoke satellite blindness.

62. **AirNow F&S Map data limitations** (LBL/EHS) — <https://ehs.lbl.gov/resource/wildfire-smoke-and-air-quality-resources/data-limitations-and-frequently-asked-questions/> — **Tier 1, unverified**. Sensors systematically underestimate dust events; correction makes it worse.

63. **NOAA HYSPLIT smoke forecast** — <https://www.arl.noaa.gov/hysplit/smoke-forecasting/> — **Tier 1, unverified**. 48 h PM2.5 transport shapefiles for CONUS/AK/HI.

64. **FireSmoke.ca / BlueSky-Canada** — <https://firesmoke.ca/data/> — **Tier 1, unverified**. NetCDF + KMZ forecasts, seasonal April–September; UBC.

65. **Yale Climate Connections smoke survey** — <https://yaleclimateconnections.org/2025/07/15-sources-of-wildfire-smoke-forecasts-for-north-america/> — **Tier 2, unverified**. Survey of 15 operational and experimental smoke products.

## Saharan dust transport

66. **NOAA AOML Saharan Air Layer** — <https://www.aoml.noaa.gov/saharan-air-layer/> — **Tier 1, verified**. SAL is "a mass of very dry, dusty air … 2 to 2.5-mile-thick … with the base starting about 1 mile above the surface." Active mid-June through mid-August (peak), declining after. Reaches Caribbean, Florida, Central America, Texas. Outbreaks every 3–5 days during peak. Tracked via GOES-16, Meteosat, polar-orbiting + GPS dropsondes.

67. **CAMS Saharan dust transport tracking** — <https://atmosphere.copernicus.eu/cams-tracks-ongoing-saharan-dust-transport-caribbean> — **Tier 1, unverified**. Confirms seasonal Caribbean dust transport tracked via CAMS dust AOD product.

68. **CAMS dust forecast** — <https://ads.atmosphere.copernicus.eu/api/v2> — **Tier 1, unverified**. CAMS Global Atmospheric Composition Forecasts; twice daily 00/12 UTC; 5-day horizon; ~40 km (~0.35°). Variable `composition_duaod550` (dust AOD at 550 nm). GRIB or NetCDF. Free with CDS API.

69. **NASA GEOS-FP** — <https://opendap.nccs.nasa.gov/dods/GEOS-5/fp/0.25_deg/assim> — **Tier 1, unverified**. 10-day aerosol forecast at 0.25° via OPeNDAP. Dust AOD a distinct variable.

70. **WMO Barcelona Dust Regional Center** — <https://dust.aemet.es/> — **Tier 1, unverified**. SDS-WAS node; MONARCH 72-hr regional dust forecast; THREDDS/OPeNDAP/WMS/WCS NetCDF. Public access embargoed >2 days for real-time forecasts (NRT requires institutional access).

71. **NASA Worldview / GIBS** — <https://nasa-gibs.github.io/gibs-api-docs/> — **Tier 1, unverified**. WMTS tiles for `MODIS_Terra_Aerosol`, `MODIS_Aqua_Aerosol`, MAIAC at 1 km. Imagery only, not numeric grid.

72. **ICAP-MME** — <https://www.nrlmry.navy.mil/aerosol/> — **Tier 2, unverified**. 9-model ensemble dust AOD, 6-hr to 120-hr; visualization confirmed, programmatic NetCDF download path unclear.

73. **AERONET** — <https://aeronet.gsfc.nasa.gov/> and web service <https://aeronet.gsfc.nasa.gov/cgi-bin/print_web_data_v3> — **Tier 1, unverified**. Ground-truth network. AOD at 500 nm (and 340–1640 nm), ~15 min cadence.

74. **NOAA NESDIS GOES-R AOD** — <https://www.star.nesdis.noaa.gov/goesr/product_aero_aod.php> — **Tier 1, unverified**. AOD from GOES-16/18 ABI; CONUS ~2 km nadir, near-real-time.

75. **EUMETSAT MSG Dust RGB** — <https://data.eumetsat.int/product/EO:EUM:DAT:MSG:DUST> — **Tier 2, unverified**. Qualitative thermal IR composite for dust visualization. Not quantitative AOD.

## Equipment-protection thresholds

76. **Arkansas Sky Observatories — Pollen alert** — <https://arksky.org/calendar/alerts/700-alert-pollen-and-your-telescope> — **Tier 3, INACCESSIBLE** (403 on re-fetch). Discovery agent extraction: claims "the number one most damaging factor" and "5–7 minute" contamination window claim, with pollen spicules and ethereal oils as mechanisms. **Source for the widely-quoted 5–7 minute claim — not independently verified by this run.**

77. **ASO — Protecting your telescope from pollen** — <http://arksky.org/aso-guides/aso-general-guides/701-protecting-your-telescope-from-pollen> — **Tier 3, unverified**. Companion guide; recommends dew shield + cap during deployment.

78. **Astro-Physics — Care of your refractor** — <https://astro-physics.info/tech_support/refractors/care-of-scope-instructions-9-4-2014.pdf> — **Tier 1 (vendor), unverified**. States that under heavy dewing in dusty/pollen-laden conditions, "normally, this will not degrade the image quality." Recommends Purosol cleaner as escalation for pollen.

79. **Astro-Physics — Cleaning instructions** — <https://astro-physics.info/tech_support/accessories/cleaningproducts/optcs-instructions.pdf> — **Tier 1 (vendor), unverified**. Pollen-specific cleaning workflow.

80. **Baader Planetarium — Cleaning and maintenance of optics** (Thomas Baader) — <https://www.baader-planetarium.com/en/downloads/dl/file/id/110/product/260/cleaning_and_maintenance_of_optics_a_short_instruction_guide.pdf> — **Tier 1 (vendor), unverified**. Claims pollen contains "very aggressive ethereal oils which can indeed penetrate into the coating layers." Strongest vendor-level coating-attack claim.

81. **PlaneWave service / warranty** — <https://planewave.com/services/> — **Tier 1 (vendor), unverified**. Explicitly excludes "damage resulting from weather or poor environmental control including dust/sand and pollen" from warranty.

82. **Celestron warranty** — <https://www.celestron.com/pages/warranty> — **Tier 1 (vendor), unverified**. Excludes coating blemishes from "wear and tear or abuse under various environmental conditions."

83. **Cloudy Nights "Pollen vs your telescope"** — <https://www.cloudynights.com/forums/topic/489697-pollen-vs-your-telescope/> — **Tier 4, unverified**. NC user: "the air looks like a yellow fog" — explicit deployment avoidance during peak pollen weeks.

84. **Sky & Telescope optics care** — <https://skyandtelescope.org/astronomy-resources/caring-for-your-optics/> — **Tier 2, unverified**. Mainstream guidance: dust tolerance high, pollen/fingerprints exception requiring escalated cleaning.

85. **Cloudy Nights "Ruined corrector with Zeiss cleaner"** — <https://www.cloudynights.com/forums/topic/654937-ruined-corrector-plate-coating-with-zeiss-lens-cleaner/> — **Tier 4, unverified**. Documented cleaning-induced damage incident.

## Volcanic / stratospheric

86. **USGS Pinatubo (Self et al.)** — <https://pubs.usgs.gov/pinatubo/self/> — **Tier 1, verified**. SO₂ injection: TOMS measured 20 ± 6 Mt (largest in 13 years of TOMS operation); other remote-sensing estimates 13.5–17 Mt; combined average ~17 Mt. Global stratospheric AOD 0.1–0.15 for 2 years; peak local 0.4 in late 1992. 3-year persistence above background. Visual effects: hazy whitish sun late 1991–early 1993. **No quantitative astronomical magnitude data** in the chapter — confirmed gap.

87. **Hunga Tonga water vapor** (Millán et al., Science) — <https://www.science.org/doi/10.1126/science.abq2299> — **Tier 1, unverified (paywall)**. ~146 Tg water vapor injected; +5% global stratospheric H₂O. MLS instrument.

88. **Hunga Tonga aerosol formation** (Zhu et al., PNAS) — <https://www.pnas.org/doi/10.1073/pnas.2219547120> — **Tier 1, unverified**. Aerosol growth 3× faster than typical due to humidification.

89. **Hunga Tonga at Paranal** (ESO Messenger 190) — <https://www.eso.org/sci/publications/messenger/archive/no.190-mar23/messenger-no190-58-61.pdf> — **Tier 1, INACCESSIBLE** (PDF parse failed, 403 on archive page). Discovery agent reported: VLT twilight calibration images showed sky brightness changes; aerosol layer persisted >12 months; sky had not returned to pre-eruption state one year later. **Direct astronomical-impact citation — could not re-verify in-session.**

90. **Hunga Tonga optical properties** — <https://acp.copernicus.org/articles/25/6353/2025/> — **Tier 1, unverified**. Particles ~2× larger than typical volcanic; spectral extinction 2022–2024.

91. **Stothers 2001 stellar SAOD** — <https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/2000JD900652> — **Tier 1, unverified**. Stellar photometry uncertainty for SAOD ±0.017; events below ~0.02 SAOD at detection floor.

92. **Solomon et al. 2011** — *Persistently variable background stratospheric aerosol layer*. Science. <https://www.science.org/doi/abs/10.1126/science.1206027> — **Tier 1, unverified**. Background SAOD is variable even absent major eruptions.

93. **CFHT Mauna Kea inversion** — <https://www.cfht.hawaii.edu/Instruments/ObservatoryManual/CFHT_ObservatoryManual_(Sec_2).html> — **Tier 1, unverified**. Confirms summit (4,205 m) sits above the trade-wind inversion layer (~4,500 ft), isolating it from VOG and lower atmospheric pollutants.

94. **IVHHN Vog Dashboard** — <https://vog.ivhhn.org/> — **Tier 1, unverified**. Real-time SO₂ (15-min) and PM2.5 at Hawaii stations. VOG capped at ~4,500 ft under trade winds.

95. **VMAP Hawaii vog forecast** — <http://mkwc.ifa.hawaii.edu/vmap/current/> — **Tier 2, unverified**. WRF + NAM NEST driven SO₂/sulfate forecast, 3 km statewide / 1 km Big Island. Web dashboard only.

96. **London VAAC QVA API** — <https://www.metoffice.gov.uk/services/transport/aviation/regulated/international-aviation/vaac/qva/qva-api> — **Tier 1, unverified**. Quantitative Volcanic Ash gridded forecasts; launched July 2025. Only VAAC with documented REST API.

97. **USGS HANS volcano API** — <https://volcanoes.usgs.gov/hans-public/api/volcano/> — **Tier 1, unverified**. JSON API exposing alert level (Normal/Advisory/Watch/Warning) and color code per US volcano.

98. **GloSSAC v2.23** — <https://www.earthdata.nasa.gov/data/projects/glossac> — **Tier 1, unverified**. Merged stratospheric aerosol climatology 1979–Dec 2024. Canonical historical SAOD record.

99. **Sentinel-5P TROPOMI SO₂** — <https://dataspace.copernicus.eu/explore-data/data-collections/sentinel-data/sentinel-5p> — **Tier 1, unverified**. SO₂ total column, ~13 × 24 km, daily global since July 2018. Free via Copernicus Data Space (OData/OpenSearch) or AWS Open Data S3.

100. **VAAC Skybrary** — <https://skybrary.aero/articles/volcanic-ash-advisory-centre-vaac> — **Tier 2, unverified**. Confirms VAAC mandate is aviation-operational, not ground-observer focused. Products in flight levels.

## Data fusion and conflict resolution

101. **Bayesian air quality fusion review** (PMC) — <https://pmc.ncbi.nlm.nih.gov/articles/PMC6295977/> — **Tier 1, unverified**. Bayesian kriging at 1 km² across Europe outperforms LUR and GWR for PM2.5.

102. **Optimum linear data fusion + kriging** (ScienceDirect) — <https://www.sciencedirect.com/science/article/pii/S0160412018326552> — **Tier 1, unverified**. Hybrid micro-sensor + EPA station fusion methodology.

103. **Modified IDW for PM2.5** — <https://www.mdpi.com/2073-4433/13/5/846> — **Tier 1, unverified**. Modified IDW reduces MAPE/RMSE 10–12% vs ordinary IDW.

104. **Multi-sensor conflict-weighted fusion** (arXiv) — <https://arxiv.org/abs/1803.04551> — **Tier 1, unverified**. Conflict-weighted fusion theory.

105. **Healio public pollen accuracy 2024** — <https://www.healio.com/news/allergy-asthma/20240510/public-websites-show-low-accuracy-in-predicting-pollen-counts-in-five-u-s-cities> — **Tier 2, unverified**. Public pollen websites show low accuracy vs NAB across 5 US cities.

## Foundational / context

106. **Cloudy Nights "Seeing and Transparency"** — <https://www.cloudynights.com/articles/articles/observing-skills/seeing-and-transparency-r1213/> — **Tier 4, unverified**. Practitioner article distinguishing transparency (aerosol/cirrus/humidity) from seeing (turbulence).

107. **Sky & Telescope "Seeing vs. Transparency"** — <https://skyandtelescope.org/astronomy-blogs/imaging-foundations-richard-wright/seeing-vs-transparency-difference/> — **Tier 2, unverified**. "Transparency is the limiting factor" for deep-sky imaging SNR; cirrus and humidity dominate over aerosol in practitioner experience.

108. **PMC: African dust deposition Atlantic estimates** — <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7340100/> — **Tier 1, unverified**. Reports African dust deposition rates including ~50 Tg/yr to the Caribbean.
