# Disciplines and the solo/duo workflow with AI augmentation

What this dimension covers: which game-development disciplines a solo or duo team must cover, where AI agents take meaningful load (code, art, audio, copy, marketing), and where human judgment remains load-bearing. Source numbers refer to entries in [`../citations.md`](../citations.md).

## The disciplines a solo dev must personally cover

A solo developer must address: **programming, 2D/3D art and animation, game design (systems, balance, level design), audio (music, SFX, voice), narrative/writing, QA/playtesting, marketing (Steam page, social media, trailers), community management, business/legal/admin, and project management.** A duo splits these but rarely cleanly — most duos pair "designer-programmer + artist-musician" or similar.

The Mirabello Tower of Guns data [23] is the cleanest measured allocation for a solo dev: ~25% of total time on marketing alone (983 of 3,850 hours). Practitioner advice (Cliff Harris [82]) recommends 12 months / 40+ patches of post-launch support, which extends the workload well past launch.

## AI tool adoption — the actual rates

Three sources, three different numbers, all credible:

| Source | Population | Adoption figure |
|---|---|---|
| GDC 2025 State of the Industry [32] | n=3,000+ developers, ±2% MoE | **36% personally use generative AI tools** |
| Stack Overflow 2025 Developer Survey [31] | tens of thousands of developers (general software) | **84% use or plan to use AI tools** (up from 76% in 2024) |
| Google Cloud / Harris Poll [33] | n=615 game developers, 5 countries | **90% report using AI in workflows** |

The wide spread reflects survey-design differences. GDC asked about "personally use generative AI" — narrow. Google Cloud asked about "AI in workflows" — broad enough to include autocomplete and analytics. The honest synthesis: **roughly a third of game developers personally use generative AI tools as of mid-2025**; broader "AI touches my workflow somewhere" rates are much higher.

By role, GDC 2025 [32] found the highest personal-use rates in **business/finance (51%), production/leadership (41%), community/marketing/PR (39%)** — the disciplines where text generation has the clearest fit. Creative and engineering roles trailed.

## Where AI takes meaningful load

### Programming

Primary tools (early 2026): GitHub Copilot, Cursor, Claude Code. Cursor and Claude Code are the most-discussed by indie devs. Stack Overflow 2025 [31] reports Claude Code at ~10% adoption among surveyed developers.

**The METR finding [29] is the most rigorous productivity data available:** randomized controlled trial, n=16 experienced open-source developers, 246 issues, Cursor Pro + Claude 3.5/3.7 Sonnet. Developers using AI tools **took 19% longer**, despite predicting 24% speedup beforehand and self-reporting 20% speedup afterward. Caveat: experienced developers, mature codebases — greenfield indie work may behave differently.

The qualitative picture: AI is most useful for boilerplate, scaffolding, learning unfamiliar APIs, and one-off scripts. It is least useful for debugging novel issues in custom systems and for systems where the human has more domain knowledge than the model. The Sept 2025 academic synthesis [36] confirms: "Code generation limited to relatively simple tasks."

### 2D and 3D art

Common tools: Midjourney (concepting, mood boards), Stable Diffusion (local, customizable), Leonardo.ai (character consistency attempts), Meshy AI (3D asset generation), Adobe Firefly, Blockade Labs Skybox AI (360° environments).

The honest workflow per practitioner reports: AI is a starting point, not a finished asset. The 5-stage pipeline — concept → base generation → refinement → texture/material work → integration — requires substantial human work at stages 3–5 (mesh cleanup, UV mapping, polygon optimization, style guide enforcement). Hand-finishing is not optional for production assets.

Style and character consistency is the hardest open problem. Midjourney's character reference parameter works ~70% of the time for simple portrait-to-portrait transfers; ~40% when poses, lighting, or scene context change substantially. Diffusion models are fundamentally probabilistic — 100% character consistency is nearly impossible without ControlNet or fine-tuned LoRAs.

### Audio

Primary tools: Suno (music, $10/mo Pro with commercial license), ElevenLabs Music (launched Aug 2025; built on licensed training data — Merlin Network, Kobalt Music Group), Beatoven.ai, SOUNDRAW, SFXR (free retro SFX).

Suno settled its Warner Music lawsuit September 2025; Pro and Premier subscribers ($10–30/mo) have full commercial licensing rights for generated content, including game soundtracks. ElevenLabs Music is trained on licensed data and offers commercial rights from day one — making it more developer-friendly for production integration.

The boundary: AI handles **background and ambient audio** competently. AI fails at **branded, memorable "hero" music** and signature jingles. "AI music is competent but rarely surprising. It follows genre conventions well but doesn't break them in interesting ways" — a recurring practitioner observation.

### Marketing and community

ChatGPT/Claude for Steam descriptions, social posts, trailer scripts. CapCut for trailer editing with AI auto-captions. AI-generated copy is a starting point that requires editing for tone and platform conventions.

The harder problem: **community trust is not AI-augmentable.** Players are sensitive to AI presence in creative work; when a community detects undisclosed AI use, the reaction is severe (see "Player rejection" below).

## Where human judgment remains load-bearing

Per Alharthi 2025 [30] and the Sept 2025 synthesis [36]:

- **Fun-finding and game feel.** AI cannot determine whether a mechanic is fun. Quote: "AI recognizes patterns and predicts likely outputs, but it doesn't grasp the cascading effects of a single tweak on balance, readability, or emotional tone."
- **Narrative cohesion across long arcs.** AI dialogue systems struggle with character consistency, factual accuracy, and thematic throughlines. The arXiv 2509.04239 study (separately surfaced in the discovery pool) found consistency errors in factual details and timeline logic in AI-co-created game narratives.
- **Style and tonal coherence across asset sets.** "Gameslop" — visually incoherent assets generated from different prompts/models — is a recognized industry problem. Speed gains on individual assets are offset by the labor cost of enforcing coherence.
- **Difficulty balance and systems design.** AI generates game states but cannot reason about long-horizon systems interactions.
- **Curation and taste.** The role shifts from authorship to filtering. Filtering AI outputs requires sophisticated taste — itself a non-trivial skill that novice developers may lack.

## Player rejection of AI assets — documented commercial damage

The discovery pool documented multiple cases:

- **Jurassic World Evolution 3 (Frontier Developments, 2025) [41]:** AI-generated scientist portraits removed pre-launch after wishlist deletions and player protest. Documented quote from a Steam user: "Just removed the game from my wishlist."
- **Neverness to Everness (Hotta Studio, 2025):** Players identified AI poster copying *Weathering with You*. Streamer Ironmouse pulled sponsorship. Voice actor threatened to quit.
- **"Hardest" (Eero Laine, 2026):** Developer voluntarily deleted free game from Steam after player feedback called it "soulless"; developer agreed.

GDC 2026 follow-up survey indicated **52% of game industry professionals believe generative AI has a negative impact on the industry** — up from 30% in 2025 [34]. Only 7% view it positively (down from 13%).

## Legal and platform compliance — real exposure

- **Steam disclosure policy [38]:** mandatory disclosure for all player-facing AI assets (pre-generated and live). January 2026 rewrite exempted efficiency tools (used in dev only) from disclosure. ~8,000 games disclosed AI use by mid-2025; one in five new releases.
- **Andersen v. Stability AI [39]:** August 2024 ruling allowed all copyright claims to proceed. Trial set September 2026. Court accepted plausibility that the model "compressed 100,000 GB of images into a 2 GB file." Indie devs cannot build proprietary training datasets the way large studios can.
- **Copyright unprotectability:** in the US, AI-only-generated content is ineligible for copyright. A competitor could legally copy and redistribute uncopyrightable AI assets from a game.
- **SAG-AFTRA video game strike [37]:** July 26, 2024 to July 9, 2025 (11 months). Settled at **95.04% ratification.** Established consent and disclosure requirements for AI digital replicas. Affected ~2,600 voice actors and motion-capture artists.
- **RIAA v. Suno and Udio (June 2024):** Udio settled with UMG and Warner by November 2025. Using AI voices trained on real performer recordings exposes developers to similar liability chains.

## What this means for solo and duo teams

**Reasonable use cases for AI augmentation in tiny indie/mobile teams:**

1. Boilerplate code, build scripts, scaffolding, simple gameplay scripting where the developer fully understands the output.
2. Concept art and mood boards (not finished assets).
3. Background and ambient music with paid commercial-license tools (Suno Pro, ElevenLabs Music) — not signature themes.
4. Marketing copy and social media drafts (always edited for tone).
5. Localization first drafts (always reviewed by the human or a hired translator).
6. Test data generation, dialogue placeholder content.

**Use cases where AI is a likely net-negative for indie teams:**

1. Production-quality character art — coherence problems, player rejection risk, copyright exposure.
2. Voice acting via AI — legal exposure post-SAG-AFTRA, trust collapse if discovered.
3. Code in domains where the developer cannot evaluate the output (Godot maintainers report being overwhelmed by AI-generated PRs whose authors cannot debug them).
4. Game design / balance / fun-finding decisions.
5. Community engagement.

**Compliance baseline for using AI assets:**

1. Disclose on Steam if any player-facing AI assets remain in the shipped game.
2. Use AI tools with explicitly licensed training data (ElevenLabs Music) where possible.
3. Document the human creative-control trail to retain copyright protection for AI-assisted work.
4. Avoid AI voices unless using a tool with explicit performer-consent licensing.

## Gaps and limitations

- **No controlled comparison** of AI-augmented vs. non-augmented solo game-dev outcomes (timeline, quality, sales).
- **No published postmortem** of an AI-augmented indie game that shipped and failed specifically due to AI workflow problems. The closest are ongoing controversies (Neverness to Everness) and qualitative friction reports.
- **The 90% Google Cloud adoption figure** [33] should be discounted by survey design — commissioned, broad definition, recruited panel.
- **Steam, Apple App Store, and Google Play AI policies** are evolving rapidly. Current text may not reflect 2026 enforcement.
- **Player sentiment about AI in games** is changing fast in both directions. The 52% negative figure is current as of GDC 2026 but could shift.
- **No solo-dev-specific AI productivity study** has been published. METR's experienced-OSS-developer finding [29] is the best available proxy.
