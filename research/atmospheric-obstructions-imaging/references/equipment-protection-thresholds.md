# Equipment-protection thresholds

**Dimension scope:** when atmospheric particulates (especially pollen and
dust) are high enough to advise against deploying expensive optics at all,
distinct from the data-quality question of "is the sky transparent."

See [citations.md](../citations.md) for full source details.

## Why this is a separate dimension

The traditional astrophotography weather forecast asks "is the sky clear and
transparent?" Equipment protection asks a different question: "even if the
sky is fine, will deployment damage my optics?"

Pine pollen at 5,000+ grains/m³ does not just degrade transparency — it
physically coats and contaminates corrector plates, refractor objectives,
and Newtonian secondaries [76, 78, 80]. Cleaning a contaminated optical
surface risks scratching coatings; some users report skipping deployment
entirely during peak NC pollen weeks [83].

## Vendor and observatory positions

| Source | Position | Notes |
|---|---|---|
| **Astro-Physics (refractors)** [78] | Conservative: under heavy dewing in dusty/pollen conditions, "normally, this will not degrade the image quality" | Recommends Purosol cleaner as escalation for pollen [79] |
| **Baader Planetarium** [80] | Aggressive: pollen contains "very aggressive ethereal oils which can indeed penetrate into the coating layers" | Strongest vendor-level coating-attack mechanism claim |
| **Arkansas Sky Observatories (ASO)** [76] | Most aggressive: pollen is "the number one most damaging factor of telescope lenses, corrector plates and mirrors" | Source of widely-quoted "5–7 minute contamination window" claim — INACCESSIBLE for re-verification (403); discovery agent extraction only |
| **PlaneWave** [81] | Warranty explicitly excludes "damage resulting from weather or poor environmental control including dust/sand and pollen" | Direct documentation that vendors do not cover this damage |
| **Celestron** [82] | Warranty excludes coating blemishes from "wear and tear or abuse under various environmental conditions" | Less explicit, but environmental damage falls under exclusion |
| **Sky & Telescope** [84] | Mainstream: dust tolerance high; pollen and fingerprints are exceptions requiring escalated cleaning | Authoritative practitioner resource |

The vendor positions span from "you can image through pollen with proper
care" (Astro-Physics) to "the oils chemically attack coatings" (Baader).
Both views are held by reputable vendors. **No vendor publishes a numerical
deployment threshold.**

## Optical-surface-specific risk by instrument type

- **Schmidt-Cassegrain (SCT) corrector plate** — Most exposed; sealed cell
  but front-facing. Cleaning a contaminated plate is the primary repair-cost
  vector. Pollen-induced damage is the dominant Cloudy Nights "ruined my
  scope" narrative [83, 85].
- **Refractor objective** — Less exposed at sky angle but more delicate
  multi-element coatings. Astro-Physics specifies coatings "become part of
  the glass and cannot be removed" [78] — damage is permanent (vs. mirrors,
  which can be re-aluminized).
- **Newtonian secondary mirror** — Less exposed because not at the top of
  the tube, but contamination travels via wind. Cleaning risk is similar.
- **Camera sensor windows** — Sealed; not directly exposed unless the
  scope's tube is open. Lower risk vector.

## Mitigation hardware

| Hardware | Function | Source |
|---|---|---|
| **Dew shield** | Reduces solid-angle exposure of corrector to atmospheric pollen/dust during deployment | [82, 83] (Celestron, ASO) |
| **Metal dust cap on dew shield** | Blocks deposition during inter-imaging pauses and transport | AstroZap (vendor product) |
| **Dew heater** | Prevents dew from "gluing" pollen/dust to surface (the dew + pollen combination is hardest to clean) | All vendors |
| **Filter wheel barrier** | Protects camera sensor side; not optic side | Standard equipment |

The dew-shield + cap strategy is the universal recommendation. **No
quantitative pollen-reduction factor** has been published for any dew shield
geometry.

## NC-specific quantitative context

NC DEQ [41] and NC State Climate Office data (per discovery agent) cite
**5,219 grains/m³ on April 1, 2024** as the all-time-high NC pollen count
at the Raleigh station. "Very high" is conventionally above ~1,500 grains/m³.
2026 season had a 1,522 grains/m³ reading on March 24.

NC pine pollen onset can be predicted via the GDD model from NC State
Extension [42]:

- 300 GDD onset, 636 GDD peak, base 55 °F, accumulate from Feb 1.
- This brackets the equipment-risk window deterministically given temperature.

Cloudy Nights NC users report the air "looks like a yellow fog" during peak
[83] and explicitly skip deployment for "a month or so."

## Saharan dust deposition (separate equipment risk)

Saharan dust transport to the Caribbean delivers **~50 Tg/yr** to the
region [108]. PM2.5 during major Saharan dust events in
Florida/Caribbean reaches "unhealthy" AQI levels. Dust particles are silica
— **abrasive if wiped**, same cleaning-risk mechanism as pollen spicules
but without the chemical (ethereal-oil) component.

**No published study translates SAL-event PM2.5 to an equipment-relevant
optical-surface deposition rate.**

## Wildfire smoke creosote / tar deposition

**No source found specifically addresses wildfire smoke deposition on
telescope optics.** The physical analog is tar/VOC film deposits (cigarette
tar on glass), which would require a solvent-based cleaner (IPA or Purosol)
and pose coating-adhesion risk during removal. Inferred, not sourced.

Professional observatory closures during wildfire events (Keck, Palomar,
Kitt Peak) are well-documented in news but relate to **staff safety and
fire risk**, not optics protection from smoke deposition.

## Counter-perspectives

The Dim6 counter agent could not complete due to a mid-task rate limit. The
counter-perspective space is partially covered by:

- **Astro-Physics (vendor)** [78]: most conservative position — pollen is
  not generally a session-killer with proper care. This is the strongest
  counter-argument to the ASO "5–7 minutes" framing, from a higher-tier
  source.
- **Cloudy Nights "Fear the pollen?" thread** [from Dim6 Discovery, not
  separately cited]: explicit debate among NC users; some image through
  peak pollen with no observed damage using dew shield + post-night
  cleaning.
- **Pollen settles overnight (partially)** [51, 52]: pine pollen specifically
  has high settling velocity (2.1 cm/s [50]); ground deposition is real but
  rate decreases substantially after sunset.

The community consensus appears to be: **dew shield + cap is mandatory; per-night
gentle cleaning is sufficient for most exposures; deployment-avoidance is
prudent during the 1–2 week peak pine pollen weeks in NC, less so for routine
"high" pollen days.**

## Insurance / warranty

- **PlaneWave** explicitly excludes pollen/dust damage from warranty [81].
- **Celestron** warranty exclusion covers environmental damage broadly [82].
- **Takahashi** warranty excludes "misuse, abuse, acts of God, normal wear and
  tear" (Dim6 Discovery extraction).
- **No standard astronomical equipment insurance** confirmed to cover
  contamination damage. Homeowners riders may apply but no source enumerates
  this.

## Recommended app decision logic for equipment protection

Surface a separate "equipment-protection" alert distinct from the transparency
forecast:

1. **Pollen risk alert**: trigger when pollen count >1,500 grains/m³ with
   "Pine" as a named contributor. Display:
   - Recommendation: dew shield + cap mandatory; consider deferring
     deployment for SCT/exposed-corrector setups.
   - For NC users: include NC State GDD model [42] for season context
     ("we are 320 GDD into the pine pollen season; peak ~636 GDD").
2. **Dust deposition alert**: trigger during AOML SAL outbreak season for
   SE-US users [66] when CAMS dust AOD [33] exceeds a threshold (no published
   value — start at 0.3 AOD). Display: silica abrasion risk; clean before
   subsequent imaging session.
3. **Wildfire smoke alert**: surface as transparency degradation (primary)
   and equipment-soiling (secondary, lower-confidence).

## Gaps and limitations

- **The 5–7 minute corrector contamination window** [76] is the single most
  cited quantitative claim in the equipment-protection space. It traces to
  one Tier 3 source (Arkansas Sky Observatories) with no measurement
  methodology cited. The page returned 403 in our re-fetch, so we could not
  re-verify even the original wording. Treat with caution.
- **No peer-reviewed materials science study** on pine pollen vs telescope
  AR/dielectric coating degradation found. The Baader "ethereal oils penetrate
  coating layers" claim [80] is vendor-level only.
- **No vendor publishes a deployment-threshold pollen count.**
- **Wildfire smoke deposition on optics is an undocumented gap.**
- **Insurance coverage for contamination damage is unconfirmed.**
- **Deployment-avoidance behavior is real but unstandardized**: forum reports
  range from "skip a day" to "skip a month."
