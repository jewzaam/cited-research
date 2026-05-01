# Reference 02 — Planning / target-selection tools

Source numbers refer to [`citations.md`](../citations.md).

## What this dimension covers

Dedicated DSO / planetarium / target-selection tools and how they compare on catalog size, FOV/framing, mosaic planning, observability windows, weather integration, telescope control, and capture-software hand-off.

## Tool-by-tool summary

### Telescopius
- **Platform:** Web + iOS/Android (PWA/TWA wrapped, not native) [38][40][41].
- **Pricing:** Free; donation-supported via Patreon (~519–646 patrons, ~$2,415/month gross — order-of-magnitude estimate from [46]); self-described "not a money-making machine" [45][46].
- **Strengths:** Equipment-aware target filtering (telescope/camera/mount profiles); FOV/mosaic simulator on DSS imagery; CSV export consumed by NINA and SGP [38][39][42].
- **Weather:** Built-in cloud + seeing forecast page; specific provider not confirmed [38][39].
- **Mobile UX:** Mobile app is a TWA-wrapped PWA, not native. iOS rating 3.6/5 with persistent login bugs reported on newer iPhones / current iOS [40][41].

### Stellarium (Desktop)
- **Platform:** Windows / macOS / Linux; v26.1 as of 2026 [47].
- **Pricing:** Free, GPL-2.0+ open source [47][51].
- **Catalog:** Default 600K+ stars; extended addons to ~220M; 80K+ DSOs [47].
- **FOV/Framing:** Oculars plugin (one entry per fixed focal length — zooms require multiple entries); Mosaic Camera plugin added in 25.2 (June 2025) overlays multi-panel grids and exports J2000 RA/Dec per panel [48].
- **Weather:** None built in.
- **Telescope control:** ASCOM (native since 0.19.3) and INDI; HTTP RemoteControl plugin for headless automation [49]; ECMAScript scripting engine [50].
- **Capture-software hand-off:** Coordinate push to NINA / SGP / TheSkyX / HNSKY / CdC. No native CSV export.

### Stellarium Mobile Plus
- **Platform:** iOS, Android (Stellarium Labs) [52].
- **Pricing:** $13.99 one-time iOS [53] (Android free tier + paid Plus).
- **Catalog (Plus, online):** 1.4B Gaia DR2 stars; 3M DSOs; 10K asteroids. Offline mode reduced to 2.5M stars / 2.9M DSOs / 10K asteroids [52].
- **Plus features:** Telescope control, ocular display, observability calendar, event calendar, 3D planet views [52].
- **Limitations for AP:** Single ocular configuration at a time (vs desktop multi-config); no mosaic planning.
- **Mobile UX:** Built-in red night mode [200]; reviewers say falls short of SkySafari Pro for astrophotography control specifically [54][53].

### Stellarium Web
- **Platform:** Browser (free) [55].
- **Status:** Subset of desktop; described as beta. No FOV/framing, no telescope control (browser sandbox).

### SkySafari 8 (Plus / Pro)
- **Platform:** iOS [58], Android [56]; macOS asserted by the vendor product page [57] but a Mac App Store listing was not retrieved at fetch — treat macOS support as vendor-claimed.
- **Pricing (April 2026, sale):** Basic $4.99/$6.99 list; Plus $17.99/$29.99 list; Pro $39.99/$49.99 list. Plus 8 on Android marked 40% off at fetch [56].
- **Pro catalog:** 100M+ stars (Gaia + Hipparcos); 780K DSOs; 3M galaxies (PGC); 750K solar-system objects; 20K Abell/Zwicky clusters [57].
- **Astrophotography (Pro only):** Native ASCOM Alpaca camera control, plate solving (StarPX remote for premium), AstroBin import [57].
- **Weather:** Pro includes "Observing Conditions" with hourly seeing index and sky quality (signal source not disclosed) [57].
- **Mobile UX:** Five UI color themes including night vision [58]. **Critical caveat:** late-2025 forum report that SkySafari 8 Android requires Google Play connectivity on launch even with downloaded data files — offline regression vs SkySafari 7 [61]. This is single-thread evidence; persistence in 2026 builds unverified.

### AstroPlanner
- **Platform:** macOS 10.14+ and Windows 8.1+ (no mobile) [63].
- **Pricing:** $45 one-time (shareware); $25 upgrade from v1.x [64][65].
- **Catalog:** 100+ astronomical catalogs, 1M+ objects (full install ~2GB) [63].
- **FOV:** Field-of-view tab with telescope/eyepiece/sensor profiles [66].
- **Weather:** None [63][66].
- **Capture-software hand-off:** None native; designed as planning/logging app [66][67].
- **Status:** Version currency uncertain — purchase page had template placeholders; the "2011-2026" copyright footer may not indicate active development [63][64].

### Cartes du Ciel (SkyChart)
- **Platform:** Windows / macOS / Linux; free, GPLv2 [68][72].
- **Version:** 4.2.1 stable; 4.3 beta build dated 2026-04-20 on SourceForge confirms active development [70].
- **FOV/Framing:** Object Browser imports observing/mosaic/frame lists; Telescopius mosaic format imports [68][71].
- **Telescope control:** ASCOM, INDI, Alpaca; CCDciel companion capture app in same suite [68][71].
- **Automation surface:** TCP/IP server on port 3292 (127.0.0.1 default) for external automation [69].

### KStars + Ekos
- **Platform:** Windows / macOS / Linux (free, KDE / GPL-2.0-or-later) [73][76].
- **Catalog:** Default mag-8 stars; extended catalogs to ~100M (mag 16); ~10K NGC/IC DSOs; downloadable Messier, Abell PN; custom catalog import [73].
- **Strength:** All-in-one — KStars planetarium + Ekos capture/scheduling. Full equipment control via INDI [74].
- **Telescopius integration:** `importMosaic` function in KStars source for mosaic CSV (user-facing workflow needs verification) [76].
- **Mobile:** "KStars Lite" Android only (limited feature set); no iOS [206].
- **Automation surface:** D-Bus interfaces for Ekos and Scheduler — full external scriptability in any D-Bus-capable language [77][78][79].

### Sky & Telescope Interactive Sky Chart
- Web-only, free, naked-eye DSOs only [80]. Not a serious astrophotography planning tool; included for completeness.

## Cross-cutting findings

1. **Telescopius dominates DSO planning workflow for hobbyist astrophotographers** because of its FOV simulation, equipment-aware filtering, and clean CSV hand-off to NINA/SGP/ASIAIR/Voyager. Free price + donation model is a key competitive moat — no indie new entrant easily competes on price [38][39][42].
2. **Stellarium is a planetarium first, planning tool second.** Strong as a visual reference and plugin host; weaker for guided AP target selection vs Telescopius. The Mosaic Camera plugin (25.2, June 2025) closes a long-standing gap [48].
3. **SkySafari 8 Pro made a serious AP push** with native Alpaca camera control, plate solving, and AstroBin import in version 8 [57]. It's positioned as "the new standard for mobile astronomy" [58] but the offline regression on Android, if real, undermines field reliability [61].
4. **AstroPlanner is the riskiest active product** — pricing/page templating quirks suggest possible quiet maintenance mode [64].

## Gaps and limitations

- Telescopius weather page data provider not confirmed (likely Astrospheric or Meteoblue based on reviewer mentions).
- SkySafari 8 Pro Alpaca camera-control compatibility list not confirmed.
- KStars `importMosaic` user-facing workflow stability in v3.7.6+ unconfirmed.
- AstroPlanner's last release date unconfirmed; assume risk of staleness until verified.
