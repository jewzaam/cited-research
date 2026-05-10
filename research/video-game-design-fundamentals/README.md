# Video game design and development fundamentals (indie/mobile, 1–2 person team with AI augmentation)

**Question:** What are the fundamentals of video game design and development, and what drives game success — for a solo or duo team using agentic AI augmentation?

**Last revised:** 2026-05-10. Full deliverable in [`analysis.md`](analysis.md). Sources in [`citations.md`](citations.md). Per-dimension detail in [`references/`](references/). Independent audit in [`audit/`](audit/).

---

## TL;DR

The honest summary: **most indie games fail, AI lowers the cost of features but not the cost of judgment, and the difference between hits and comparable flops is dominated by quality + luck + sustained marketing — not by following success patterns extracted from outliers.**

Plan financially around the median: a Steam indie game grosses **$249** in 2025; **79%** of 2024 Steam releases were classified "Limited" (failed to hit Valve's undisclosed sales/engagement thresholds); **83%** of mobile games fail within 3 years; sponsored Twitch streams have **median ROI of -95%**.

AI augmentation makes the cost curve more favorable for cost-per-feature work (boilerplate code, asset concepting, marketing copy first drafts), but does not change which decisions matter. The METR randomized controlled trial found experienced developers **took 19% longer with AI** despite predicting a 24% speedup beforehand and self-reporting a 20% speedup afterward.

## The numbers that frame everything

| Metric | Value | Source |
|---|---|---|
| Median 2025 Steam indie gross | **$249** ($174 net after Valve's 30% cut) | [42] |
| Steam games earning under $1K lifetime | **66%** | [42] |
| Steam games earning over $1M lifetime | **0.5%** | [42] |
| 2024 Steam releases classified "Limited" | **79%** | [77] |
| Mobile games failing within 3 years | **83%** | [73] |
| Median mobile D28 retention | **~0.85%** | [17] |
| Sponsored Twitch stream median ROI | **-95%** | [68] |
| Indie financial viability rate (2024 Steam) | **~0.5%** | [60] |
| Mobile games with no reported dark patterns | **10.76%** | [14] |
| AI productivity in METR RCT (n=16) | **-19%** (despite +20% self-perception) | [29] |
| 7,000 wishlists | Approximate Steam Popular Upcoming threshold | [47] |

## Decision framework

**1. Pick a quality threshold, not a sales target.** The strongest predictor of wishlist-to-sales conversion is the launch review score. Aim for "Very Positive" (≥80%) at minimum, "Overwhelmingly Positive" (≥95%, 500+ reviews) for the strongest algorithmic and conversion advantages. Quality is the entry filter.

**2. Build the cheapest viable first project.** First-game average gross is $120K, third-game $209K. There is a real experience effect, but only if you survive long enough to make a second and third game. Many do not. Plan financially around the median ($249), not the marketed averages.

**3. Use AI for cost-per-feature, not cost-per-decision.** Boilerplate, scaffolding, asset concepting, marketing copy first drafts, localization first drafts. *Not* fun-finding, balance, narrative cohesion, or community trust. Track your own time, not your perception of speed.

**4. Use the prototype/vertical-slice distinction explicitly.**
- *Prototype* = "should you make this?" Disposable. Fast. Cheap.
- *Vertical slice* = "can you make this?" 3–5 minutes of polished gameplay covering all core systems at near-shipping quality.
Don't polish prototypes. Don't treat vertical slices as throwaway.

**5. Choose your platform business model deliberately.**
- **Premium PC (Steam):** $5–20 price, no F2P obligations. Discoverability is the gate.
- **Premium mobile:** $3–10 price. Caps revenue per user but avoids whale-acquisition arms race.
- **F2P mobile:** Whale-dependent (top 10% of payers ≈ 64% of revenue). Dark patterns are nearly required to compete (96.8% of "dark" mobile games are F2P). Structurally unviable for tiny teams without franchise scale.

**6. Disclose AI use; license your AI tools.** Steam disclosure is mandatory for player-facing AI assets. Use commercial-license tools (Suno Pro, ElevenLabs Music, properly licensed image generators). The downside risk of undisclosed AI use is now larger than the upside from speed.

**7. Treat "make games you love and they will come" as dangerous advice.** It generalizes from outliers. The default outcome is poverty. Marketing must be planned from the start, not bolted on at launch. ~25% of total time on marketing is the practitioner-data norm (Tower of Guns: 983 of 3,850 hours).

**8. Plan for a 2–3× timeline overrun.** Documented case data: Last Humble Bee 9→27 months, Tower of Guns ~20 months, Stardew Valley ~5 years (intentional). The "average indie dev time is 18 months" figure is folklore.

## What this document is not

- **Not a prediction model.** Comparable-quality games show 500× revenue differences attributable to chance. You cannot reliably control for that gap.
- **Not a checklist for hits.** Survivorship bias contaminates almost all "patterns from successes" advice. Treat practitioner playbooks as approximations, not recipes.
- **Not specific to any one engine, genre, or platform.** Where a finding is engine- or genre-specific (e.g., game feel as Swink defined it), the document marks the scope.

## Where to read further

- [`analysis.md`](analysis.md) — full deliverable with cross-dimensional synthesis, methodology, reflection pass, and gap-acknowledgment.
- [`references/core-design-fundamentals.md`](references/core-design-fundamentals.md)
- [`references/player-psychology-engagement.md`](references/player-psychology-engagement.md)
- [`references/production-process-tiny-teams.md`](references/production-process-tiny-teams.md)
- [`references/disciplines-solo-duo-with-ai.md`](references/disciplines-solo-duo-with-ai.md)
- [`references/commercial-success-indie-mobile.md`](references/commercial-success-indie-mobile.md)
- [`references/critical-cultural-success.md`](references/critical-cultural-success.md)
- [`references/failure-modes-indie-mobile.md`](references/failure-modes-indie-mobile.md)
- [`citations.md`](citations.md) — all sources, numbered, with extracted data and source-tier ratings.
- [`audit/`](audit/) — independent citation audit and consistency review (Phase 4 outputs).
