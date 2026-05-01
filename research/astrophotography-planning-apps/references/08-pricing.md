# Reference 08 — Pricing & monetization benchmarks

Source numbers refer to [`citations.md`](../citations.md). All prices in USD as confirmed April 2026 unless noted.

## What this dimension covers

What hobbyists actually pay for astrophotography planning apps; the price ceiling for a sustainable indie app; the spread of monetization models (one-time vs subscription vs donation vs hardware-tied).

## Pricing matrix (April 2026)

| App | Price | Model | Last confirmed | Cite |
|---|---|---|---|---|
| Astrospheric (free tier) | $0 | Freemium | Apr 2026 | [2] |
| **Astrospheric Pro** | **$2.99/mo or $29.99/yr + tax** | Subscription | Apr 2026 | [2] |
| Clear Outside | $0 | Free (retailer-backed) | Apr 2026 | [9][10] |
| Good to Stargaze (Value) | $0.99/mo or $6.49/yr | Tiered subscription | Apr 2026 | [16] |
| Good to Stargaze (Hobbyist 7-day) | $3.99/mo or $25.99/yr | Tiered subscription | Apr 2026 | [16] |
| Good to Stargaze (Professional 15-day) | $6.99/mo or $54.99/yr | Tiered subscription | Apr 2026 | [16] |
| Telescopius | $0 (donations) | Patreon-supported | Apr 2026 | [38][45][46][176] |
| Stellarium Desktop | $0 | Free OSS (GPL) | Apr 2026 | [47] |
| Stellarium Web | $0 | Free | Apr 2026 | [55][177] |
| Stellarium Mobile Plus (iOS) | $13.99 | One-time | Apr 2026 | [53] |
| **SkySafari 8 Basic** | $4.99 sale / $6.99 list | One-time | Apr 2026 | [56] |
| **SkySafari 8 Plus** | $17.99 sale / $29.99 list | One-time | Apr 2026 | [56] |
| **SkySafari 8 Pro** | $39.99 sale / $49.99 list | One-time | Apr 2026 | [56] |
| PhotoPills (iOS) | $10.99 | One-time | Apr 2026 | [85] |
| TPE (iOS) | $9.99 | One-time | 2024–2025 | [90] |
| TPE 3D (iOS) | (separate one-time; price not extracted) | One-time | — | [91] |
| PlanIt Pro (iOS) | $9.99 base + optional $5.99/yr 3D sub | One-time + optional sub | Apr 2026 | [94] |
| PlanIt Pro (Android) | ~$4.99 | One-time | (older snippet) | [95] |
| AstroPlanner | $45 | One-time (shareware) | 2024–2025 | [64] |
| N.I.N.A. | $0 | Free / OSS (MPL 2.0) | Apr 2026 | [102] |
| **Sequence Generator Pro** | **$149 first year + $59/yr renewal** (perpetual fallback if you don't renew) | Subscription with perpetual fallback | Apr 2026 | [110] |
| Voyager (Base) | ~129 EUR + ~29 EUR/yr renewal (vendor does not publish a public-storefront price; user-reported) | Perpetual + annual support | 2023–2024 | [173][174] |
| **Voyager Advanced (RoboTarget)** | Pricing not publicly disclosed at fetch time | Perpetual + annual support | — | [115] |
| **ASIAIR Plus (hardware)** | ~$349 retail (256GB) | Hardware-tied (app free) | Apr 2026 | [178][179] |
| KStars / Ekos | $0 | Free / OSS (GPL-2.0+) | Apr 2026 | [76] |
| StellarMate OS (RPi image) | $69 | Commercial OS layer | Apr 2026 | [180] |
| Ouranos | ~$40/yr (user-reported, T4) | Subscription only | 2024–2025 | [144][145] |
| Scope Nights (iOS) | $6.99 | One-time | Apr 2026 | [13][181] |
| Sky Tonight Plus | $1.99/mo or $14.99/yr | Subscription | Apr 2026 | [138][140] |
| Sky Tonight Pro | $4.99/mo or $39.99/yr | Subscription | Apr 2026 | [138][140] |
| Cartes du Ciel | $0 | Free / OSS (GPLv2) | Apr 2026 | [70] |
| Xasteria Plus (iOS) | $0.99 | One-time | Apr 2026 | [25] |
| StarCast (web) | $0 | Free web | Mar 2026 | [136] |
| StarCast (iOS app) | $2.99/mo (7-day trial) | Subscription | Mar 2026 | [136] |

## Monetization-model summary

- **Free / donation:** Telescopius, Clear Outside, all OSS desktop suites.
- **One-time purchase ($5–$15):** PhotoPills, TPE, Stellarium Mobile Plus, SkySafari Basic/Plus, Scope Nights, Xasteria Plus.
- **One-time purchase ($30–$50):** SkySafari 8 Plus list, AstroPlanner, SkySafari 8 Pro list.
- **Subscription, low ($1–$3/mo or ~$15–$30/yr):** Astrospheric Pro, Sky Tonight Plus, StarCast, Good to Stargaze low tier.
- **Subscription, mid ($4–$7/mo or ~$30–$55/yr):** Good to Stargaze mid/high tiers, Sky Tonight Pro, Ouranos.
- **Capture-suite annual ($60–$150):** SGP, Voyager.
- **Hardware-tied:** ASIAIR (~$350+).

## Hypothesis check: "free → ~$30/yr is typical for hobbyist apps"

**Confirmed for the planning/weather-app layer.** The clearest data point is Astrospheric Pro at $29.99/yr [2] — the price anchor for dedicated astronomy weather. SkySafari 8 Plus list at $29.99 (planning/visual) sits at the same anchor [56]. Sky Tonight Pro at $39.99/yr is slightly above [140].

**Higher tiers exist for capture/automation tools** ($59-$149/yr for SGP, ~150 EUR + renewal for Voyager) — but those are professional-imaging-suite users, not the hobbyist-planning audience.

**Free-tool gravity is heavy.** Clear Outside is free and retailer-backed. NINA, KStars, Stellarium are free OSS. Telescopius is free with donation-only revenue (~$2,415/mo Patreon gross [46] for ~30K+ users [186]). An indie new entrant cannot match these on price; it has to differentiate on capability.

## Conclusion

For an indie planning-app new entrant: realistic ceiling is **$30/yr subscription for general hobbyists**, with a stretch to $50-$60/yr if the differentiation is genuine and equipment/audience-specific. Above that, you compete with capture-suite tier where you don't belong as a planning tool.

## Gaps and limitations

- Voyager Advanced exact pricing (whether the beta €299 campaign is still active or a new list price applies) unconfirmed at fetch.
- Ouranos $40/yr is user-reported, not vendor-confirmed; App Store listing should be re-fetched.
- TPE 3D price not extracted at fetch; App Store listing returns it but content was not retrieved.
- Good to Stargaze pricing is from a 2023 archive in places; current App Store may differ slightly.
- PhotoPills Android price not separately verified.
