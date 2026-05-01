# Reference 10 — Mobile vs. desktop UX

Source numbers refer to [`citations.md`](../citations.md).

## What this dimension covers

Astrophotographers do final go/no-go in the driveway on a phone. Tools that fail the mobile experience lose at this critical decision point even with rich data. This dimension categorizes each tool by mobile presence and quality.

## UX category matrix

| Tool | Category | iOS rating | Android rating | Night mode | Offline | Cite |
|---|---|---|---|---|---|---|
| **Astrospheric** | Mobile-equivalent | 4.77/5 (~390 ratings) | 4.06/5 (~680 ratings) | OS-level only (no built-in red mode confirmed) | Forecast requires internet | [34][35][201] |
| **Clear Outside** | Mobile-equivalent (web + mobile parity) | ~3/5 | (not surfaced) | None confirmed | Not confirmed | [9][10] |
| **Telescopius** | Mobile-secondary (PWA wrapped in TWA, not native) | 3.6/5 | low downloads | Not mentioned | Limited (PWA needs connectivity) | [40][41] |
| **Stellarium Mobile Plus** | Mobile-equivalent (native iOS + Android) | 4.0/5 (~8.3K reviews) | (free tier + paid Plus) | **Built-in red night mode** | YES — 2.5M stars / 2.9M DSOs / 10K asteroids offline | [52][53][200] |
| **SkySafari 8 (Plus / Pro)** | Mobile-first (iOS + Android + macOS) | "new standard for mobile astronomy" framing | (sale 40% off Android Plus) | **Five UI color themes incl. night vision** | **CRITICAL:** late-2025 user report: Android requires Google Play connectivity on launch even with downloaded data files; offline regression vs SS7 — single-thread evidence; persistence in 2026 builds unverified | [56][57][58][61] |
| **PhotoPills** | Mobile-first (iOS since 2013, Android added 2017; no desktop) | ~4.7/5 | ~4.5/5 (~6.4K reviews) | Night AR planning; no dedicated red-mode UI | Partial (planning works offline; map tiles need pre-cache) | [85][86][87][210] |
| **NINA** | Desktop-only (Windows-only); LAN companion via Touch-N-Stars (third-party, free, OSS, iOS+Android) | (companion app) | (companion app) | N/A (desktop) | LAN-required | [102][135][208] |
| **KStars / Ekos** | Desktop-only for full features (Linux/macOS/Windows); KStars Lite Android only (limited); **no iOS** | — | KStars Lite (limited) | Not confirmed for mobile | Desktop yes; Lite unclear | [76][206][207] |
| **ASIAIR App** | Hardware-tied (iOS + Android native; ZWO hardware required) | (paired with hardware) | (paired with hardware) | Not surfaced | Operates on local WiFi from ASIAIR — internet not required for session | [203][204][124] |
| **AstroPlanner** | Desktop-only (macOS + Windows; no mobile) | — | — | N/A | N/A | [63] |
| **Cartes du Ciel** | Desktop-only (Windows/Linux/macOS; no first-party mobile) | — | — | N/A (desktop) | N/A | [70] |
| **Sequence Generator Pro** | Desktop-only (Windows); RDP-only mobile workaround | — | — | N/A | N/A | [110] |
| **Voyager** | Desktop-only core + responsive Web Dashboard for mobile | — | — | Not confirmed for Web Dashboard | Web Dashboard requires LAN to Voyager PC | [205] |
| **Sky Tonight** | Mobile-first (iOS + Android) | 4.76/5 (~70K) | 4.6/5 (~78K reviews; 10M+ installs) | Red night mode (buried 2+ taps in settings) | **Excellent offline** | [138][140][141][202] |
| **Ouranos** | Mobile-first (iOS + Android, PWA/TWA) | 4.5/5 | (TWA) | Not confirmed | Not confirmed | [144][145][146] |
| **Good to Stargaze** | Mobile-secondary (iOS exists but reportedly unmaintained; developer redirects to mobile web) | (declining) | (limited) | Not confirmed | Partial | [16][214] |
| **Scope Nights** | Mobile-first (iOS only — no Android) | — | N/A | Not surfaced | Not confirmed | [13][181][182] |

## Critical UX findings

1. **The mobile-first / mobile-equivalent leaders are PhotoPills, SkySafari 8 Pro (with the Android offline caveat), Sky Tonight, and Astrospheric.** These four all have native apps with sustained engagement signals.
2. **The capture/automation suites (NINA, KStars, SGP, Voyager, Cartes du Ciel) are desktop-only.** Voyager's responsive Web Dashboard is the best mobile story among them [205]; NINA's Touch-N-Stars is functional but requires a NINA running PC on the LAN [135][208]; KStars/Ekos has *no* iOS support at all [206][207].
3. **The driveway use case is best served by Astrospheric or Sky Tonight + Telescopius (or a similar combo).** No single mobile tool answers "should I set up tonight, given my targets and equipment?" comprehensively today — the user runs at least two apps.
4. **PWA/TWA architecture is a quality penalty.** Telescopius and Ouranos both ship as PWA-wrapped apps; both have lower ratings (3.6/5 and 4.5/5 respectively) and persistent platform-edge bugs vs. fully native peers [40][41][145].
5. **Red / night-vision mode is a basic feature, but several tools lack a built-in implementation.** Stellarium Mobile Plus and SkySafari 8 explicitly support it; Sky Tonight has it but buried [200][58][202]; Astrospheric likely relies on OS-level color filters [34]; Clear Outside has none confirmed.
6. **Offline capability is uneven.** SkySafari 8 Android's offline regression (if confirmed in current builds) is a critical field-usability problem. Stellarium Mobile Plus's offline data set is a real differentiator. Most weather forecast apps require connectivity by nature (forecast data can't be pre-fetched indefinitely).

## Implications

- An indie new entrant **must ship native iOS and Android (or at least an excellent PWA with offline-friendly architecture)** — desktop-only is not credible for a planning tool in 2026.
- **Red/night-vision mode is table stakes**, not a differentiator.
- **Offline-friendly design is a moat.** Even partial offline (cached forecast snapshot, target list, equipment profile) outperforms apps that hard-fail when signal drops.
- **Ratings and review velocity are the only public engagement signals.** They lag actual usage but are what an indie app must compete against.

## Gaps and limitations

- Astrospheric built-in red night mode status is unconfirmed — the official app pages do not explicitly state it.
- SkySafari 8 Android offline regression is a single Cloudy Nights thread's evidence; persistence in 2026 builds is not confirmed.
- Touch-N-Stars internet-vs-LAN scope: confirmed LAN-only in current docs; remote-internet support is unconfirmed.
- Good to Stargaze's official maintenance status is inferred from user-review patterns, not a developer announcement.
- KStars Lite Android feature delta vs desktop Ekos is not enumerated in this research.
