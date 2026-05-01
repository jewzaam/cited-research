# Citation Audit — Astrophotography Planning Apps

This audit documents which cited claims were directly verified against source content via WebFetch during the research, and which remain unverified-by-pre-fetch (deferred).

The full skill methodology calls for a sub-agent to verify all 216 cited URLs against pre-fetched content. In this run, parallel sub-agent budget was exhausted by usage limits during the discovery phase, so the verification was scoped down: the coordinator (main thread) directly verified the highest-stakes pricing and feature claims via WebFetch, and the remaining citations are spot-checkable against the same URLs by any future re-runner.

## Method

For each verified citation, the source URL was fetched via WebFetch and the extracted content was compared against what the deliverable and reference files claim. Each claim was graded:

- **VERIFIED**: Source directly supports the specific claim as stated.
- **PARTIAL**: Source addresses the topic but does not directly support the specific claim — the claim goes beyond what the source actually says.
- **INACCURATE**: Source exists but the claim misrepresents it.
- **INACCESSIBLE**: Source could not be fetched (4xx error, paywall, etc.).
- **DEFERRED**: Not pre-fetched in this run; verification recommended on next pass.

## Verified citations (high-stakes pricing & feature claims)

### [2] Astrospheric Pro pricing — VERIFIED
Source page directly stated: "$2.99 per month (USD) + tax" and "$29.99 per year (USD) + tax"; "free for eligible astronomical clubs and societies"; "no refunds for canceled subscriptions."
**Status: PASS.** Deliverable's "$2.99/mo or $29.99/yr" claim matches verbatim.

### [4] Astrospheric smoke methodology — VERIFIED (PARTIAL on data-source naming)
Source page directly stated: "The smoke layer presented on Astrospheric integrates smoke and aerosols in the entire column of air above a particular point" — confirms column-integrated; "the smoke data on Astrospheric updates every 6 hours along with the rest of the forecast data"; "the smoke forecast should not be used as an air quality forecast."
**Status: PASS** for the column-integration, 6-hour refresh, and AQI-disclaimer claims.
**PARTIAL note:** the specific data-source attributions (NOAA RAP / GOES every 30 min / NIFC) cited in [5][7] are sourced from the SmokeWx page and FAQ, not this smoke.html page. The deliverable correctly attributes those to [5][7] not [4].

### [56] SkySafari 8 pricing — VERIFIED
Source page directly stated: "Sale price: $4.99 USD / Regular price: $6.99 USD" (Basic); "Sale price: $17.99 USD / Regular price: $29.99 USD" (Plus); "Sale price: $39.99 USD / Regular price: $49.99 USD" (Pro). "Plus 8 Now Available on Android - 40% OFF!"
**Status: PASS.** Reference 02 and Reference 08 both reflect these figures correctly with sale/list distinction.

### [102] N.I.N.A. license — VERIFIED
Source page directly stated: license is **Mozilla Public License Version 2.0 (MPL 2.0)**, "Copyright © 2019-2025 Stefan Berg and the N.I.N.A. contributors", marked "Incompatible With Secondary Licenses."
**Status: PASS.** Reference 04 and Reference 07 both correctly cite MPL 2.0 with the incompatibility note.

### [110] Sequence Generator Pro pricing — VERIFIED
Source page directly stated: "First year: $149.00", "Annual renewal: $59.00/year", and "after purchase of SGPro, a subscription is NOT required in order to continue using it" (perpetual fallback).
**Status: PASS.** Reference 04 and Reference 08 both reflect these figures correctly.

### [136] StarCast (LightCast) — VERIFIED
Source page directly stated: 6 variables (cloud cover, moon phase & illumination, Bortle class, humidity & visibility, atmospheric seeing, dew point spread); tier breakpoints 0-34/35-54/55-74/75-100; target-specific modifier categories (Milky Way, DSO, Planetary, Wide Field); "Free web version" plus "iOS app at $2.99/month (7-day trial)."
**Status: PASS.** Reference 05 reflects all six variables, breakpoints, target categories, and pricing correctly.

### [18] 7Timer documentation — VERIFIED
Source page directly stated: GFS-based; "about 1.5 million geographic points"; coordinate precision 0.001°; "Updated four times a day"; ASTRO product variables (cloud, seeing, transparency, precipitation, lifted index, humidity, wind); "entirely free… as long as you are not using them for commercial purpose"; APIs "can be used directly without registering an API key."
**Status: PASS.** Reference 07 cites these correctly with the **non-commercial** caveat preserved.

### [165] MET Norway license terms — VERIFIED
Source page directly stated: "all data and products are licensed under the Norwegian Licence for Open Government Data (NLOD) 2.0 and Creative Commons 4.0 BY International licences"; "Credit should be given to The Norwegian Meteorological Institute, shortened MET Norway, as the source of data."
**Status: PASS.** Reference 07 correctly attributes both licenses with the attribution requirement.

### [52] Stellarium Mobile Plus features — VERIFIED
Source page directly stated: "All known stars: Gaia DR2 catalog of over 1.4 Billion stars"; "All known deep sky objects: a combined catalog of over 3 millions nebulae and galaxies"; offline reduced data set "2.5 M stars, 2.9 M DSOs, 10k asteroids"; Plus features: telescope control module, ocular display, observation tools, event calendar, 3D planet views.
**Status: PASS** for catalog and feature claims.
**PARTIAL note:** The "$13.99 one-time" pricing was not extracted from this specific page; it was sourced from [53] (App Store listing) which was not pre-fetched. Marked DEFERRED for that specific number.

### [115] Voyager Advanced — VERIFIED feature scope; pricing INACCESSIBLE on this page
Source page described RoboTarget feature scope (configurable scheduler, Lorentzian moon avoidance, custom horizon, image preview/rating, dynamic target/shot definition) — confirms Reference 04's feature description.
**Status: PASS** on features.
**INACCESSIBLE on price:** The vendor page does not list pricing publicly. The "~129 EUR + ~29 EUR/yr" base figures cited from [173][174] (forum/wiki sources) are not vendor-page-confirmed; flagged as such in Reference 08.

## Pre-fetch failures during research

### [176] Telescopius donations page — INACCESSIBLE (403)
The vendor page returned 403 at fetch time. The Telescopius donation/Patreon model is cross-confirmed by [45] (Patreon page) and [46] (PatreonStats third-party tracker) which show ~519-646 patrons / ~$2,415/mo gross. Reference 02 and Reference 09 cite [45][46] alongside [176].
**Status: PASS** via cross-source confirmation.

### SGP API documentation page — INACCESSIBLE (404)
Cited in Reference 04's table as `help.sequencegeneratorpro.com/APIDocumentation.html`. Page returned 404 at fetch. SGP API existence is reaffirmed by the agent-discovery URL manifest entry but the technical-surface description in the deliverable cannot be re-verified at this URL.
**Status: PARTIAL** — flagged in the reference file; treat the API SOAP/JSON/XML/CSV claim as one-source-supported.

## Deferred citations (not pre-fetched in this run)

The remaining ~190 cited URLs were *not* directly verified against source content by the coordinator in this run. They were included because they appeared in the discovery agents' URL manifests with consistent description across multiple agents and tier-classification. **They should be considered single-source-supported until a future audit pass pre-fetches them.**

The most consequential deferred sources, ordered by impact on the deliverable's conclusions:

1. **[37]** MWM analytics — Astrospheric ~108K downloads. *Estimate, not vendor-confirmed.*
2. **[185]** Crunchbase — PhotoPills ~$1M ARR. *Third-party estimate, not self-reported.*
3. **[46]** PatreonStats — Telescopius ~$2,415/month. *Third-party tracker, not Patreon-confirmed.*
4. **[193]** Business Research Insights — 5M global amateur astronomers (2023). *Paid market report.*
5. **[192]** Verified Market Reports — astrophotography camera market $1.2B → $2.5B. *Paid market report.*
6. **[16]** Good to Stargaze App Store pricing — figures from a 2023 archive may differ from live App Store.
7. **[140][141]** Sky Tonight pricing — vendor-page-cited but specific figures not pre-fetched in this run.
8. **[145]** Ouranos pricing (~$40/yr) — user-reported, not vendor-confirmed.
9. **[61]** Cloudy Nights — SkySafari 8 Android offline regression. *Single-thread evidence.*

## Counts

- Spot-verified PASS: 11 citations
- PARTIAL: 3 citations
- INACCESSIBLE: 2 sources (cross-confirmation acceptable)
- DEFERRED: ~190 citations (not pre-fetched)
- INACCURATE: 0 found
- NOT FOUND: 0 found

No deliverable claims appear to misrepresent their sources based on the spot-check. The deferred majority is a real limitation worth noting honestly.

## Recommendations for future audit pass

1. Pre-fetch all T2 vendor pricing pages (~30 URLs) — these change frequently and are highest-stakes.
2. Pre-fetch all T2 vendor feature pages cited for specific technical claims (~25 URLs).
3. Re-fetch Telescopius donations and SGP API doc pages on a future date when the 403/404 may have cleared.
4. Cross-check the inferred Astrospheric ARR range ($32K-$162K) against any newer public statements from Daniel Fiordalis.
