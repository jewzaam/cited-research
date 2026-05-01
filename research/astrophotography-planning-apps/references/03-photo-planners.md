# Reference 03 — Photography-oriented night planners

Source numbers refer to [`citations.md`](../citations.md).

## What this dimension covers

Photography-first ephemeris/planning apps (PhotoPills, TPE, PlanIt Pro, Sun Surveyor, LightTrac) — what they're good at and where they hard-stop relative to deep-sky imaging.

## Findings per tool

### PhotoPills
- **Pricing:** $10.99 one-time iOS [85]. Cross-platform (iOS + Android).
- **Strengths:** Milky Way galactic-core positioning (AR overlay on live camera), MW rise/set timing, golden/blue hour, sun/moon AR, NPF rule, star-trail planning, FOV calculator (lens-centric) [82][83][84].
- **Hard stop for deep-sky:** No DSO catalog. No telescope FOV framing against specific nebulae/galaxies. No mount/equipment profiles. No session sequencing for DSO targets [82][83][86][87].
- **Mobile UX:** Mobile-first since 2013; portrait-only on phones; partial offline (planning works offline; map tiles need pre-cache) [86][87].
- **Note:** ~$1M ARR estimated by Crunchbase [185]. Price-anchored as a one-time purchase — explicitly bucking the subscription wave [183]. Not an AP tool — landscape/Milky-Way audience.

### The Photographer's Ephemeris (TPE / TPE 3D)
- **Pricing:** TPE iOS $9.99 one-time [90]; TPE 3D separate purchase (price not extracted) [91][92].
- **Strengths:** TPE 3D's terrain + sun/moon/MW visualization is best-in-class for landscape composition [92][88].
- **Hard stop:** No DSO catalog; no telescope FOV.
- **Note:** Skyfire (aurora) deprecated for new purchases February 2025 [89] — a signal of feature triage / focus narrowing.

### PlanIt Pro for Photographers
- **Pricing:** iOS $9.99 base + optional $5.99/year 3D feature subscription [94]; Android ~$4.99 [95] (older snippet — verify).
- **Differentiators over PhotoPills:** Bortle Dark Sky Scale integration (unique among this group), VR viewfinder mode, 3D terrain + city landmarks [100][96].
- **"Nebulae azimuth/elevation" feature is positional only** — not a DSO catalog with magnitude filtering or imaging-FOV planning. Confirmed via multiple reviews [99][100].
- **Hard stop:** Same as PhotoPills/TPE — landscape/wide-field oriented; no telescope FOV; no equipment profiles.
- **Notes:** Steeper learning curve than PhotoPills; PhotoPills preferred for field AR use [96][100].

### Sun Surveyor
- **Pricing:** $9.99 [98] (free Lite version available).
- **Scope:** AR sun/moon paths, golden/blue hour, shadow length, moon phase/supermoon, MW positioning [97][98].
- **Hard stop:** No DSO catalog, no telescope features. Solar/lunar specialist with basic MW.

### LightTrac
- **Pricing:** $9.99 iOS [99] (older listing; current status uncertain).
- **Scope:** Sun/moon elevation/azimuth on map, shadow length. **No Milky Way or star-trail planning** in any reviewed source.
- **Status:** Most reviews are 2010–2014; effectively in maintenance/stale mode. Probably irrelevant for active 2026 use.

## Cross-cutting findings

1. **None of the photography-oriented planners offer:** DSO catalogs, telescope FOV framing against object angular size, equipment profiles (focal length + sensor), mount-aware planning, or session sequencing. Multiple T3 reviewers redirect deep-sky users to astronomy-native tools (Telescopius, Stellarium, SkySafari Pro, AstroPlanner) [86][87][96][99][100].
2. **PhotoPills and PlanIt Pro are the two with the deepest astrophotography-adjacent overlap.** Even so, their "astrophotography" support is explicitly Milky Way / wide field [86][96][100].
3. **For deep-sky imaging, this entire category is out of scope.** A dedicated astrophotography planner does not compete with PhotoPills — different audience, different equipment class. PhotoPills is best understood as a *complement* (for sun/moon timing, framing constraints, golden-hour blend) rather than a competitor.

## Gaps and limitations

- TPE 3D price not retrieved at fetch time.
- LightTrac maintenance/availability status unverified for April 2026.
- PhotoPills's Night AR specifically — whether it overlays any named DSO markers (even Messier objects) — not confirmed; likely just galactic band/core based on reviews.
- Whether PhotoPills' FOV calculator accepts telescope focal lengths and astronomy sensor sizes (vs DSLR/mirrorless lens parameters only) — unconfirmed.
