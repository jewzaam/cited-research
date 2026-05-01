# Reference 05 — Decision-aid gap (single composite "go / no-go" score)

Source numbers refer to [`citations.md`](../citations.md).

## What this dimension covers

Whether any tool answers *"should I set up tonight, given my targets and equipment?"* with a single multi-factor score, vs. presenting raw weather/seeing/transparency tables for the user to interpret. The hypothesis: the gap is real, with no tool fully integrating seeing + transparency + cloud + targets + equipment + particulates into one number.

## Decision-format taxonomy

| Format | Tools | Critique |
|---|---|---|
| **Raw multi-row table, color-coded per cell** | Astrospheric [27], Clear Outside [9][148], Clear Dark Sky [11][12], Good to Stargaze [15] | User synthesizes; high info density but cognitive load is high in driveway use |
| **Categorical traffic-light per time block** | Scope Nights (3-tier) [13][14] | Good for fast scanning; coarse; inputs limited (no seeing/transparency from a meteorological model) |
| **Single composite percentage (limited inputs)** | Sky Tonight Stargazing Index [138][139] | Combines moon + cloud + Bortle + visibility window; **no seeing or transparency**; methodology not disclosed |
| **Single composite 0-100 score with target-type modifier** | StarCast (LightCast) [136][137] | **Closest to a comprehensive composite found.** Six variables (cloud, moon, Bortle, humidity/visibility, seeing, dew-point spread); target modifier (MW / DSO / Planetary / Wide Field). No equipment-aware modifier. |
| **Per-target geometry score (not conditions)** | Telescopius visibility/season scores [38], Astrophotography Planner iOS [142] | Useful for target-vs-night, but does not integrate weather conditions into a recommendation |
| **Equipment-aware visibility filter (not a score)** | DSO Planner [143] | Filters target list by aperture/conditions/magnitude; produces a list, not a score |
| **AI/heuristic recommendation** | Astrospheric ensemble cloud (AI spectral nudging on GDPS) [4]; Ouranos AI features [144] | Model-accuracy enhancements to underlying signals, not a final go/no-go recommendation layer |

## Detailed gap assessment

### What no tool combines into a single score

A truly equipment-aware composite would integrate:
- Seeing (atmospheric scintillation, FWHM)
- Transparency (atmospheric extinction)
- Cloud cover (multi-layer)
- Sky darkness (Bortle / moon phase / horizon altitude)
- Target catalog (specific DSO / Milky Way / Solar-system / Wide-field)
- **User equipment** (focal length, sensor, filter type — narrowband vs broadband)
- Particulates (smoke, pollen, dust, AQI)
- Dew-point gap (equipment-protection signal)

**No tool found integrates all eight.** The closest is StarCast (six atmospheric variables + target type), missing equipment specs and particulates.

### Why this matters

Astrospheric — the highest-quality *data* tool — explicitly does not produce a nightly composite. AstroBackyard's review confirms: "Astrospheric has no simple Yes/No answer to tell you if conditions are good" [27]. This is an architectural choice: Astrospheric leaves synthesis to the user. For a hobbyist deciding *now* whether to set up the rig, that synthesis cost is real.

### Counter-evidence considered

- **Astrospheric Smoke Score** [4][7] is a *domain-specific* single number (column-integrated PM2.5 → f-AQI mapping). It does not aggregate seeing/transparency/cloud/moon — only smoke. This refines but does not refute the gap.
- **Astrospheric AI ensemble cloud forecast** uses spectral nudging on GDPS — but this is a model-accuracy enhancement, not a recommendation layer [4].
- **Sky Tonight's Stargazing Index** is a true composite percentage but with thin inputs (moon + cloud + Bortle + visibility window) and no seeing/transparency from a meteorological model [138][139].
- **StarCast (LightCast suite)** covers six atmospheric variables and adds target-type modifiers — clearly the deepest decision-aid found in this research [136][137]. But it does not accept user equipment (aperture, sensor, focal length, filter type) and does not integrate particulates other than via humidity/visibility proxies. The product is also new (March 2026 PetaPixel coverage), with longer-term stability/funding unknown.

## Conclusion

The decision-aid gap is **real but narrower than initially assumed.** StarCast in particular substantially closes the atmospheric-conditions composite-score gap as of late March 2026. Two genuine remaining gaps for an indie new entrant:

1. **Equipment-aware modifier** — adjusting the score by the user's specific rig (aperture, sensor, narrowband vs broadband filter, target category mismatched to equipment).
2. **Particulate-aware modifier** — integrating Astrospheric-grade smoke + missing pollen/dust/AQI signals into the same composite.

Either by itself is differentiation; both together is a defensible niche.

## Gaps and limitations

- StarCast was discovered late in this research (March 2026 launch); product traction, long-term stability, and platform reach (mobile rollout pace) are unknown.
- Astrospheric may have added or be planning a composite-score feature in the latest app version not reflected on indexed pages — cannot rule out.
- "Equipment-aware modifier" is partly speculative — no formal user study confirms hobbyists want or would adopt one.
