# Reference 04 — Capture-software-integrated planning

Source numbers refer to [`citations.md`](../citations.md).

## What this dimension covers

For each major capture/automation suite, what *planning* is built in vs. outsourced: target lists, multi-night scheduling, weather hooks (forecast vs. binary safety monitor), framing/FOV, integration with external planners.

## Tool-by-tool comparison

### N.I.N.A. (Nighttime Imaging 'N' Astronomy)
- **License / pricing:** Free, **Mozilla Public License 2.0** [102]. Windows-only.
- **Source:** [https://github.com/isbeorn/nina](https://github.com/isbeorn/nina) [107]; canonical plugin template [108]; manifest registry rejects closed-source plugins [109].
- **Target list:** Single target per Advanced Sequencer block in base; load from internal catalog, Framing Assistant, or planetarium (Stellarium, CdC, TheSkyX, HNSKY) [106]. **Multi-night scheduling via the Target Scheduler plugin** (tcpalmer; free third-party) — SQLite project DB, per-filter exposure plans, cross-night frame tracking [103].
- **Weather (forecast):** Read-only Weather driver with OpenWeatherMap / TheWeatherCompany / Weather Underground (API key required); displays temperature, humidity, dew point, wind, cloud cover, pressure [104][131].
- **Safety:** Separate ASCOM Safety Monitor slot for binary safe/unsafe (SkyAlert, Boltwood, CloudWatcher, etc.) [104][130]. Forecast data is *not* autonomously interpreted as safety — that requires a sensor or external interpreter [104].
- **Framing / FOV:** Full Framing Assistant with DSS/SkyView overlays; Telescopius CSV (1.11+) and observing-list import [105][42].
- **Mobile companion:** Touch-N-Stars (iOS + Android, free, open source; LAN-required; needs NINA Advanced API plugin) [135][208].

### Sequence Generator Pro (SGP)
- **License / pricing:** Commercial. **$149 first year + $59/year renewal**; 3-machine default install (4/5/6 upgrades available); after first-year purchase, *subscription is not required* — perpetual fallback to last-licensed version [110][175].
- **Target list:** Explicit target list per sequence file with active checkbox, start/end times, per-target exposure plan [111]. **No cross-night progress database** — frequently-cited gap vs. NINA + Target Scheduler [132].
- **Weather (forecast):** Safety Monitor only (binary ASCOM safe/unsafe), Boltwood II support, Observing Conditions Hub for personal weather stations; **no built-in forecast API integration** [114]. Automatic sequence pause/recovery on unsafe.
- **Framing / FOV:** Basic altitude chart; mosaic tool with prior-image framing [112].
- **External planner integration:** Telescopius URL import (paste observing-list URL; auto-populates per-target start/end times based on visibility); AstroPlanner and Starry Night import [113].
- **API:** Documented HTTP API (SOAP/JSON/XML/JSV/CSV) for external apps to trigger captures and equipment control. Note: the API help page returned 404 at this fetch — see [110] vendor product page for current pricing/license.

### KStars / Ekos
- **License / pricing:** Free, GPL-2.0-or-later (KDE) [76]. Linux/macOS/Windows. StellarMate hardware/OS commercial layer at $69 image price [180].
- **Target list:** Ekos Scheduler job queue with per-target constraints (min altitude, moon separation, twilight, artificial horizon) [75].
- **Multi-night scheduling: native and persistent.** Scheduler runs across nights, monitors conditions, starts/shuts the observatory automatically, resumes incomplete jobs next night [75].
- **Weather:** INDI weather drivers feed continuous data with three-state model (Ok / Warning / Alert). Standalone INDI Safety Monitor aggregates multiple weather/auxiliary devices. Soft-shutdown on Alert preserves connections [75].
- **Mosaic / framing:** Built-in planetarium with FOV overlay; Telescopius mosaic CSV import via `importMosaic` source-level function [76].
- **API:** Full D-Bus interface (Ekos + Scheduler) — any D-Bus-capable language (Python etc.) can drive the suite [77][78][79].

### ASIAIR / ASIAIR Plus (ZWO)
- **License / pricing:** Hardware-tied. **App is free; hardware required (~$349 standalone for ASIAIR Plus 256GB at retail dealer)** [178][179].
- **Target list:** Plan mode supports multi-target lists with grouped exposures per target; built-in DSO catalog; ephemeris display per night [124].
- **Multi-night scheduling: limited.** Plan-mode tracks completion within a run; resume requires manually re-opening the saved plan next night; no automated cross-night progress carry-forward [126][127].
- **Weather / safety:** **No native weather station integration; no ASCOM safety monitor support** (closed ecosystem). Significant gap for unattended remote operation [124][134].
- **Framing / FOV:** In-app framing with plate solving; mosaic via Telescopius CSV paste workflow [125].
- **Open-source posture:** Closed; ZWO has had GPL-violation issues with INDI/Siril/astrometry.net components — source releases obtained only after community pressure [128][129].

### Voyager (Base + Voyager Advanced with RoboTarget)
- **License / pricing:** Closed source, commercial. Base ~129 EUR one-time + ~29 EUR/yr renewal (per [173][174]; vendor does not publish a public storefront price). Voyager Advanced page does not list price publicly at fetch time [115].
- **Target list:** Base uses **DragScript** (visual drag-and-drop scripting) — manual specification [117][118]. Advanced adds **RoboTarget** — database-driven scheduler with unlimited targets, per-filter exposure quotas, constraints, priority weighting; Gantt-chart preview [115][121].
- **Multi-night scheduling:** RoboTarget tracks cumulative frames per filter across sessions; will not re-image already-captured data [121].
- **Weather / safety:** Distinguishes display from action. Safety monitor via ASCOM Boltwood/CloudWatcher; on unsafe, DragScript Emergency Suspend (park, close, wait); on safe, Emergency Resume [118][119][123].
- **Framing / FOV:** **RoboClip Web** — online Aladin-Lite-based framing tool integrated into Voyager workflow; stores frames with RA/Dec; transfers directly to DragScript / sequences / RoboTarget. Telescopius mosaic CSV import (Shift+click workflow) [122].
- **API / mobile:** JSON-RPC over TCP/WebSocket Application Server API [116]; **Web Dashboard is responsive (mobile/tablet)** for full equipment control over LAN [205].

## Cross-cutting findings

1. **The capture suites all separate "weather forecast" from "safety monitor."** None autonomously interprets a forecast to decide whether to start; they all rely on a binary safe/unsafe sensor or a manually scripted condition. This is the single most consistent gap across the category.
2. **Multi-night intelligent scheduling is the hardest distinguisher.** KStars/Ekos and NINA + Target Scheduler are best-in-class; Voyager Advanced (RoboTarget) is close. SGP and ASIAIR fall short for unattended multi-night runs [75][103][121][124].
3. **Open-source posture splits cleanly:** OSS hosts (NINA MPL 2.0, KStars GPL-2.0+) plus their plugin/D-Bus extension surfaces are highly contributable; Voyager and SGP are closed but with documented APIs; ASIAIR is closed and locks the developer out [102][76][116][110][128].
4. **Mobile control is a documented gap for NINA and SGP.** NINA gains a phone surface only via Touch-N-Stars [135] + Advanced API plugin (LAN only); SGP has no mobile, users resort to Windows RDP. Voyager's responsive Web Dashboard is the best mobile story among Windows-based suites [205].

## Gaps and limitations

- SGP API documentation page returned 404 at fetch; technical surface description sourced from vendor help references and third-party docs.
- Voyager Advanced exact pricing not publicly listed; the ~129 EUR base / ~29 EUR renewal figures are from forum/wiki sources [173][174].
- ASIAIR firmware updates 2025-2026 — whether ZWO has added any safety-monitor surface is unconfirmed.
- NINA Target Scheduler plugin's own weather awareness (does it consume forecast data, or rely entirely on safety-monitor signal?) — not documented in fetched material.
