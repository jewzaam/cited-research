# DeepSeek V4 — License, Weights Provenance, and Export-Control Posture

Reference compiled 2026-04-30. Covers the V4-Pro and V4-Flash weight releases, the shift away from the prior DeepSeek License, US federal/state restrictions in force as of April 2026, EU AI Act GPAI obligations, and outstanding distillation-IP risk.

## 1. V4 License Status: MIT (with one open question)

Both V4 weight releases ship under the MIT License according to the Hugging Face model cards.

- The V4-Pro card states: "The repository and model weights are licensed under the MIT License." [HF V4-Pro card]
- The V4-Flash card lists `License: MIT` in its metadata block and contains no Attachment-A-style appendix in the fetched body. [HF V4-Flash card]

This is a material shift from prior DeepSeek releases. The V3 LICENSE-MODEL file was the custom "DeepSeek License Agreement" Version 1.0 (dated October 23, 2023), which carried two provisions absent from MIT:

1. **Attachment A — use-based prohibitions**, including: "military use in any way"; exploiting or harming minors; generating false information intended to harm others; automated decisions adversely impacting legal rights; discrimination on protected characteristics; and harassment, defamation, or unauthorized privacy violations. Derivative works had to carry these restrictions forward in downstream legal agreements. [DeepSeek V3 LICENSE-MODEL]
2. **PRC governing law** with exclusive jurisdiction in Hangzhou courts. [DeepSeek V3 LICENSE-MODEL]

A pure MIT release removes both. Black Duck's prior analysis — that the V3-era model weights were not OSI-compliant open source because of the use-based restrictions — applied to the V3 license and does not apply to V4 if the MIT designation is unmodified. [Black Duck]

### Highest-priority confirmation gap: Is V4's MIT "clean"?

The fetched HF model card text declares MIT but does not include the full LICENSE file body. A direct fetch of the V4 repository's `LICENSE` (or `LICENSE-MODEL`) file is needed to confirm there is no appended Attachment A or other use-restriction rider. Until that confirmation is in hand, treat the "clean MIT" reading as probable but not verified. [HF V4-Pro card; DeepSeek V3 LICENSE-MODEL — gap noted in fetched analysis]

## 2. Redistribution Rights Under MIT

Assuming the V4 license is unmodified MIT:

- Permits commercial use, redistribution, fine-tuning, and creation of derivative works.
- Sole obligation is to retain the MIT copyright notice and permission text in copies or substantial portions of the software.
- No revenue caps, no MAU thresholds, no field-of-use clauses, no patent grant or retaliation language.

Comparison points used by enterprise legal teams:

- **Llama 4 community license** carries a 700M monthly-active-user cap above which a separate license is required, plus a competing-model clause restricting using Llama outputs to train rival models.
- **Apache 2.0** adds an explicit patent grant and patent-retaliation termination, which MIT lacks.
- **DeepSeek License v1.0 (V3 era)** added Attachment A use restrictions and PRC jurisdiction, which MIT lacks.

For a self-hoster, MIT is the most permissive of the four. For a redistributor pushing weights downstream, MIT is the simplest to comply with — copy the notice and you are done. [HF V4-Pro card; DeepSeek V3 LICENSE-MODEL]

## 3. US Export Controls — Inbound Use

There is currently no US export-control rule that prohibits a US person from downloading or running DeepSeek V4 weights from Hugging Face.

- The Biden-era BIS AI Diffusion Rule (effective January 13, 2025) created ECCN 4E091 covering closed-weight AI models trained with more than 10²⁶ operations, with associated end-use and end-user controls.
- The Trump administration rescinded the AI Diffusion Rule effective May 13, 2025. ECCN 4E091 was effectively suspended at that point.
- A replacement rule has been promised but, per the trackers consulted, has not been finalized as of April 2026.
- Current BIS guidance focuses on chip export enforcement, not on inbound model-weight downloads. [Akin Gump tracker — fetch failed (HTTP 403); summary derived from agent search snippets]

Note that the Akin Gump source returned HTTP 403 in this session; the rescission date and replacement-rule status above come from the cached agent summary and should be reconfirmed against a working source (e.g., the Federal Register notice or BIS press release) before relying on them in legal advice.

## 4. US Federal and State Restrictions

Restrictions in force as of April 2026 cover government devices and government contractors, not private individuals or non-government enterprises.

### Federal (statute)

- **FY2026 NDAA, P.L. 119-60, Section 1532** (signed December 18, 2025): within 30 days of enactment, DoD must execute "exclusion and removal of AI developed by DeepSeek, High Flyer, or associated entities from DOD systems." The restriction extends to contractors — it prohibits using DeepSeek/High Flyer/affiliates "with respect to the performance of a contract with" DoD. Limited waivers exist for research, national security analysis, and mission-critical functions. [Crowell client alert]
- **Section 6604 (Intelligence Authorization Act)**, included with the FY2026 NDAA: identical restrictions applied to the Intelligence Community. [Crowell client alert]
- **H.R.1121 — "No DeepSeek on Government Devices Act"** (119th Congress, introduced February 7, 2025 by Gottheimer/LaHood): would direct OMB to require removal from federal IT, with exceptions for national security and research. Status as of April 2026: introduced, not enacted. The Congress.gov page returned HTTP 403 in this session, so the status comes from cached agent summaries. [HR 1121 — fetch failed]

### State (executive orders)

Per the GovTech tracker dated February 13, 2025, three states had banned DeepSeek on state-issued devices:

- **Texas** — January 31, 2025 (Gov. Abbott, alongside RedNote, Webull, Tiger Brokers, Moomoo, Lemon8).
- **New York** — February 10, 2025 (Gov. Hochul, citing foreign surveillance and data-harvesting concerns).
- **Virginia** — February 11, 2025 (Gov. Youngkin: "a threat to the security and safety").

The article carries an editor's note that more states would be added. [GovTech]

### Scope

All of the above target government devices, government employees acting in their official capacity, or contractors performing on government contracts. None of them prohibit private individuals, academic researchers (outside of state-funded device usage), or non-government enterprises from running V4 weights.

## 5. EU AI Act — GPAI Obligations

Chapter V General-Purpose AI rules took effect August 2, 2025. The systemic-risk threshold is 10²⁵ floating-point operations; models above this are presumptively "high impact capabilities." [Pinsent Masons]

GPAI provider obligations apply to all GPAI models:

- Maintain technical documentation accessible to regulators.
- Adopt EU-compliant copyright policies allowing rightsholders to opt out of training use.
- Publish summaries of training content.

Systemic-risk GPAI providers additionally owe adversarial testing and evaluation, systemic-risk assessment and mitigation, incident reporting, and cybersecurity protections. [Pinsent Masons]

The Commission has acknowledged DeepSeek raises a threshold-design question, quoting: "Large numbers of models are likely trained with compute resources above the threshold, while DeepSeek has shown that frontier capabilities can also be reached with less compute." The AI Office said it would issue clarifications drawing on the Joint Research Centre. No formal enforcement actions against DeepSeek have been announced; the Commission is "monitoring market developments." [Pinsent Masons]

For self-hosters of open weights: deploying V4 internally does not, by itself, make a downstream user a GPAI "provider" under Chapter V. GPAI obligations attach to the entity that places the model on the EU market or puts it into service under its own name. A purely internal or non-EU-market deployment would not trigger them; a redeployment-as-a-service offered into the EU likely would.

## 6. Distillation Allegations and Downstream IP Risk

A White House OSTP statement in April 2026 alleged "industrial-scale" distillation by DeepSeek from US frontier models, per agent reports — this source was not directly fetched in this session and should be confirmed against the OSTP release before being relied on. If proven in a court or settlement, the allegation creates a downstream IP risk for V4 fine-tunes, since derivative liability could in principle reach parties that knowingly built on tainted weights. Legal-press coverage (Winston & Strawn, prior Anthropic statements) referenced in agent reports treats this as an open litigation risk rather than a settled one.

This risk exists independently of the MIT designation: an MIT grant from DeepSeek does not warrant non-infringement of third-party IP, and the standard MIT disclaimer of warranties shifts that exposure to the downstream user.

## 7. Practical Recommendation by Audience

- **Individuals and non-government small teams (US/EU)**: V4 weights are legally usable under the MIT designation on the model cards. Confirm the LICENSE file matches MIT before redistribution. [HF V4-Pro card; HF V4-Flash card]
- **DoD employees and contractors**: barred from using DeepSeek tools "with respect to the performance of a contract with" DoD per NDAA Section 1532. Limited waivers for research, national security analysis, and mission-critical functions. [Crowell]
- **US Intelligence Community**: same bar under Section 6604. [Crowell]
- **State employees in TX, NY, VA (and any later-adding states)**: barred on state-issued devices per executive order. [GovTech]
- **EU GPAI providers**: comply with Chapter V documentation, copyright opt-out, and training-data summary obligations; if above 10²⁵ FLOPs, add systemic-risk obligations. [Pinsent Masons]
- **Anyone redistributing V4 derivatives**: confirm the LICENSE file is unmodified MIT before relying on the simpler obligations; if any Attachment A appears, the V3-era restrictions return.

## Sources

- Hugging Face — DeepSeek-V4-Pro model card: https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro
- Hugging Face — DeepSeek-V4-Flash model card: https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash
- DeepSeek V3 LICENSE-MODEL: https://github.com/deepseek-ai/DeepSeek-V3/blob/main/LICENSE-MODEL
- Black Duck — DeepSeek License analysis: https://www.blackduck.com/blog/deepseek-license.html
- Crowell — FY2026 NDAA client alert: https://www.crowell.com/en/insights/client-alerts/the-fy-2026-national-defense-authorization-act
- GovTech — state ban tracker: https://www.govtech.com/biz/data/wheres-deepseek-banned-the-states-blocking-chinese-made-ai
- Pinsent Masons — EU AI Act GPAI / DeepSeek: https://www.pinsentmasons.com/out-law/analysis/eu-ai-act-gpai-deepseek-review
- MIT Technology Review — Why DeepSeek's V4 matters: https://www.technologyreview.com/2026/04/24/1136422/why-deepseeks-v4-matters/
- Akin Gump — BIS rescission tracker (FETCH FAILED HTTP 403): https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/bis-rescinds-ai-diffusion-rule-and-issues-new-guidance
- Congress.gov — H.R.1121 (FETCH FAILED HTTP 403): https://www.congress.gov/bill/119th-congress/house-bill/1121

## Confirmation Gaps (priority order)

1. **HIGHEST PRIORITY — V4 MIT cleanliness.** Direct fetch of the LICENSE file in the V4-Pro and V4-Flash repositories needed to confirm no Attachment A or use-restriction rider is appended. The HF model card text states MIT but the full file body was not extracted.
2. BIS rescission and replacement-rule status — Akin Gump source returned 403; reconfirm against Federal Register or BIS press release.
3. H.R.1121 status — Congress.gov returned 403; reconfirm against Congress.gov or GovTrack.
4. White House OSTP April 2026 distillation statement — not directly fetched; locate the original release before citing.
