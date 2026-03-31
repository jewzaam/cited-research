# Citation Audit: [27] through [70]
# Date: 2026-03-31
# Auditor: Independent verification agent (no context from original research)

This audit examines EVERY citation from [27] through [70] individually against fetched source content. Citations [1]-[26] were audited separately.

---

## CRITICAL FINDING: Citation [60] INACCURATE

**Citation [60]**: "Publication Bias Compromises Meta-Analyses." PLOS ONE, 2021.
https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0252415

**Claims made:**
- Main document line 19: "significant results are 3x more likely to be published [60]"
- Main document line 183, 377: "Papers with significant results are 3x more likely to be published [60]"
- Citations.md lines 455-456: "22% increase in significant results 1990-2007. Papers with significant results 3× more likely to publish."
- source-selection-bias.md line 97: "Significant results: publication likelihood multiplier | 3× | [60]"
- source-selection-bias.md line 98: "Increase in significant results (1990–2007) | 22% | [60]"

**What the source actually says:**
- Only 18% of educational meta-analyses addressed publication bias
- Meta-analytic average effect d=0.40 vs pre-registered RCTs d=0.06
- Psychology: meta-analytic effects "three times as small" as claimed
- 42% tested for bias but didn't adjust; 40% attempted detection+correction
- Only 4% based conclusions on corrected estimates

**Verdict: INACCURATE → Status: RESOLVED**

The source is about meta-analytic practices and how published meta-analyses fail to account for publication bias. The specific claims "22% increase in significant results 1990-2007" and "papers with significant results 3× more likely to publish" do NOT appear in this source.

**Resolution:** The 3× claim was traced to Dickersin et al. (1987) and added as [71]. All references to [60] for the 3× claim were updated to [71]. The unsourced "22% increase" claim was removed entirely. [60] now correctly attributes Ropovik et al.'s actual findings (18% of meta-analyses address publication bias, only 4% use corrected estimates).

---

## [27] SEME Alert Mitigation

**Citation:** Epstein et al. "Suppressing the Search Engine Manipulation Effect." ACM, 2017.
https://dl.acm.org/doi/10.1145/3134677

**Status:** INACCESSIBLE (403 - listed in inaccessible-sources.md as "Data from discovery agent search snippets")

**Claims made:**
- Citations.md lines 217-218: "Alerts reduced SEME by 22.1% and 13.8% depending on type."
- search-retrieval-bias.md line 27: "Alert-based SEME reduction | 22.1% and 13.8% depending on type | [27]"
- search-retrieval-bias.md line 32: "Alerts reduced the effect but did not eliminate it [27]"
- Main document line 165: "Alerts reduced the Search Engine Manipulation Effect by 13.8-22.1% but did not eliminate it [27]"
- Mitigation table line 530: "SEME alerts | 1,137 participants [10][27] | 13.8-22.1% reduction in manipulation effect"

**Grade: INACCESSIBLE**

Source returned 403 error. Data sourced from discovery agent search snippets. Cannot verify the specific "22.1% and 13.8%" claims without direct source access.

---

## [28] Sycophancy Survey (Malmqvist)

**Citation:** Malmqvist. "Sycophancy in Large Language Models: Causes and Mitigations." 2024.
https://arxiv.org/html/2411.15287v1

**Status:** No fetched file exists; NOT listed in inaccessible-sources.md

**Claims made:**
- Citations.md lines 221-227: "Survey of sycophancy causes. RLHF 'reward hacking.' Metrics: CTR, EIR, PIR. Mitigations: synthetic data fine-tuning, KL-then-steer, Leading Query Contrastive Decoding."

**NOTE:** This citation is NOT used in the main deliverable, README, or any reference files. It appears ONLY in citations.md. No claims need verification.

**Grade: UNVERIFIED** (not used in deliverable)

---

## [29] Medical LLM Overconfidence

**Citation:** "Overconfidence in Medical LLM Self-Assessment." medRxiv, 2024.
https://www.medrxiv.org/content/10.1101/2024.08.11.24311810v1.full

**Status:** INACCESSIBLE (listed as "Data from discovery agent")

**Fetched source:** pmc-overconfidence-medical-ai.md (PMC12874690) - NOTE: Different URL

**Claims made:**
- Citations.md lines 232-233: "Confidence ranges 69-80% regardless of correctness. 0.6-5.4% difference between correct and incorrect responses."
- Main document line 116: "Models express confidence of 69-80% regardless of correctness, with only 0.6-5.4% difference between correct and incorrect responses [29]"
- Main document line 447, 451: "Confidence ranges 69-80% regardless of correctness [29]"
- reflexivity-problem.md multiple uses of the 69-80% and 0.6-5.4% claims

**What the fetched source (PMC12874690 - Berkowitz) actually says:**
- "Systems nearly as confident when wrong as when right"
- RLHF/DPO "sharpen distribution"
- Human raters reward "clear and decisive" answers
- PING framework: 96% reduction in expected calibration error

**Analysis:** The fetched PMC source (Berkowitz) addresses the same topic and confirms the qualitative claim ("nearly as confident when wrong as when right"), which supports the "69-80% regardless of correctness" finding. However, the specific numbers "69-80%" and "0.6-5.4%" do NOT appear in the fetched PMC source. 

The citation lists a medRxiv URL, but the fetched file is from PMC with a different article ID. These may be different versions of related work, or the discovery agent may have conflated two sources.

**Grade: PARTIAL**

The qualitative claim (overconfidence, minimal difference between correct/incorrect) is verified by the fetched source. The specific numerical ranges are not present in the fetched source but may exist in the cited medRxiv version (which was not successfully fetched).

---

## [30] Generative AI Survey Responses

**Citation:** Zhang et al. "Generative AI Meets Open-Ended Survey Responses." Sociological Methods & Research, 2025.
https://journals.sagepub.com/doi/10.1177/00491241251327130

**Status:** INACCESSIBLE (403 - listed in inaccessible-sources.md)

**Claims made:**
- Citations.md lines 236-240: "34% of survey participants use LLMs. LLM-generated responses more homogeneous and positive, masking underlying social variation."
- Main document line 340: "Thirty-four percent of survey respondents use LLMs, producing more homogeneous and positive responses that mask underlying social variation [30]"
- epistemic-monoculture.md line 39: "34% of survey respondents use LLMs | Responses more homogeneous and positive, masking social variation | [30]"
- README line 34: "Epistemic monoculture | 34% use LLMs for surveys | Survey study [30]"

**Grade: INACCESSIBLE**

Source returned 403 error. Cannot verify "34%" figure or homogenization claims.

---

## [31] Homogenizing Effect on Human Expression

**Citation:** "The Homogenizing Effect of Large Language Models on Human Expression and Thought." Trends in Cognitive Sciences, 2026.
https://www.cell.com/trends/cognitive-sciences/abstract/S1364-6613(26)00003-3

**Status:** No fetched file; NOT listed in inaccessible-sources.md

**Claims made:**
- Citations.md lines 244-250: "Evidence of LLM impact on standardization of language and thought patterns."
- epistemic-monoculture.md line 42: "Standardization of language and thought patterns | Cross-domain evidence | [31]"
- Main document line 352: "users internalize homogeneous patterns [32][33]" (note: cites [32][33], not [31] directly here)
- epistemic-monoculture.md line 82: "→ Homogeneous outputs [30][31]"

**Grade: UNVERIFIED**

No fetched source available. Not listed as inaccessible. Cannot verify claims. Note that this source is used less frequently than [30], [32], [33] in the homogenization arguments.

---

## [32] Homogenization of Creative Ideation

**Citation:** "Homogenization Effects of Large Language Models on Human Creative Ideation." ACM, 2024.
https://dl.acm.org/doi/10.1145/3635636.3656204

**Status:** INACCESSIBLE (403 - listed in inaccessible-sources.md)

**Claims made:**
- Citations.md lines 252-257: "Reduced semantic diversity in human outputs when using LLMs."
- Main document line 341: "LLM use reduces semantic diversity in creative ideation [32]"
- Main document line 355: "creative 'scar' that persists after LLM use [32][33]"
- epistemic-monoculture.md line 40: "Reduced semantic diversity in creative ideation | LLM users produce less diverse outputs | [32]"
- epistemic-monoculture.md lines 45, 83, 97, 98, 127, 130: Multiple references to the "scar" effect

**Grade: INACCESSIBLE**

Source returned 403 error. Cannot verify semantic diversity reduction or "scar" persistence claims.

---

## [33] The Homogenizing Engine (SAGE)

**Citation:** "The Homogenizing Engine: AI's Role in Standardizing Culture." SAGE, 2026.
https://journals.sagepub.com/doi/10.1177/23727322251406591

**Status:** No fetched file; NOT listed in inaccessible-sources.md

**Claims made:**
- Citations.md lines 259-265: "Cultural homogenization evidence. AI as driver exceeding previous technologies."
- Main document lines 342, 355: "homogenization effect persists after users stop using LLMs [33]"
- epistemic-monoculture.md line 41: "Creative 'scar' persists after LLM use | Homogenization effects outlast the interaction | [33]"
- epistemic-monoculture.md lines 45, 83, 97, 98, 127, 130: "scar" references [32][33]

**Grade: UNVERIFIED**

No fetched source available. Not listed as inaccessible. Cannot verify cultural homogenization or persistence claims.

---

## [34] Human-AI Feedback Loops

**Citation:** "Human-AI Feedback Loops Altering Judgment." Nature Human Behaviour, 2024.
https://www.nature.com/articles/s41562-024-02077-2

**Status:** INACCESSIBLE (303 redirect - listed in inaccessible-sources.md as "Nature paywall/redirect")

**Claims made:**
- Citations.md lines 267-273: "1,401 participants. Human-AI interaction amplifies bias more than human-human. Participants unaware of AI influence extent."
- Main document lines 302-303: "human-human interaction across 1,401 participants [34], with participants unaware of the AI influence extent [34]"
- Main document line 488: "neither party detects drift because each step feels locally reasonable [1][34]"
- human-operator-bias.md lines 76-77: "Human-AI interaction amplifies bias more than human-human interaction | 1,401 participants | [34]" and "Participants unaware of AI influence extent | Same study | [34]"

**Grade: INACCESSIBLE**

Nature redirect (303). Cannot verify 1,401 participant study or bias amplification claims.

---

## [35] Sycophantic AI and Prosocial Intentions

**Citation:** "Sycophantic AI Decreases Prosocial Intentions." Science, 2026.
https://www.science.org/doi/10.1126/science.aec8352

**Status:** INACCESSIBLE (403 - listed in inaccessible-sources.md)

**Claims made:**
- Citations.md lines 275-279: "49% higher affirmation rate vs humans. Effects on moral reasoning."
- Main document line 420: "Sycophantic AI decreases prosocial intentions and affects moral reasoning [35]"
- automation-bias.md line 42: "Sycophantic AI decreases prosocial intentions | Effects on moral reasoning | [35]"
- human-operator-bias.md line 63: "Affirmation rate vs humans | 49% higher | [35]"

**Grade: INACCESSIBLE**

Source returned 403 error. Cannot verify "49% higher affirmation rate" or prosocial impacts.

---

## [36] LLM Content Biases in Transmission Chains

**Citation:** "Large Language Models Show Human-Like Content Biases in Transmission Chain." PNAS, 2023.
https://www.pnas.org/doi/10.1073/pnas.2313790120

**Status:** No fetched file; NOT listed in inaccessible-sources.md

**Claims made:**
- Citations.md lines 281-287: "Transmission chain experiments showing convergence. Bias propagation evidence."
- epistemic-monoculture.md line 54: "Transmission chain experiments show convergence | Content biases propagate and amplify through chains | [36]"

**Grade: UNVERIFIED**

No fetched source available. Not listed as inaccessible. Cannot verify transmission chain convergence.

---

## [37] Amplified Cognitive Biases in Moral Decisions

**Citation:** "Amplified Cognitive Biases in LLMs for Moral Decision-Making." PNAS, 2024.
https://www.pnas.org/doi/10.1073/pnas.2412015122

**Status:** INACCESSIBLE (403 - listed in inaccessible-sources.md)

**Claims made:**
- Citations.md lines 289-294: "LLM vs human cognitive bias amplification factors."
- Main document line 226: "LLMs amplify cognitive biases compared to humans, particularly in moral decision-making [37]"
- synthesis-framing-bias.md line 82: "LLM vs human cognitive bias | LLMs show amplified bias in moral decisions | [37]"
- synthesis-framing-bias.md line 84: "in moral decision-making contexts [37]"

**Grade: INACCESSIBLE**

Source returned 403 error. Cannot verify cognitive bias amplification in moral contexts.

---

## [38] Self-Contradictory Hallucinations

**Citation:** "Self-Contradictory Hallucinations in ChatGPT." OpenReview, 2024.
https://openreview.net/forum?id=EmQSOi1X2f

**Status:** INACCESSIBLE (403 - listed in inaccessible-sources.md)

**Claims made:**
- Citations.md lines 296-300: "17.7% self-contradiction rate in ChatGPT outputs. Detection F1 ~80%."
- Main document lines 117, 217, 233: "Self-contradiction occurs at a 17.7% rate [38]" and "17.7% in ChatGPT outputs [38]"
- synthesis-framing-bias.md lines 17, 21, 24, 132: Multiple uses of "17.7%" figure
- llm-intrinsic-biases.md lines 105, 109, 114, 136: Multiple uses of "17.7%" and "~80% F1"

**Grade: INACCESSIBLE**

Source returned 403 error. Cannot verify "17.7%" self-contradiction rate or "~80%" detection F1.

---

## [39] AI-AI Bias

**Citation:** "AI-AI Bias: LLMs Favor LLM-Generated Communications." PNAS, 2024.
https://www.pnas.org/doi/10.1073/pnas.2415697122

**Status:** INACCESSIBLE (403 - listed in inaccessible-sources.md)

**Claims made:**
- Citations.md lines 302-306: "LLMs favor LLM-presented items more frequently than humans do."
- Main document line 343-344: "LLMs favor LLM-generated content over human-generated content [39]"
- epistemic-monoculture.md lines 55, 57, 85, 129, 353: Multiple references to AI preferring AI content

**Grade: INACCESSIBLE**

Source returned 403 error. Cannot verify AI-AI preference bias.

---

## [40] Reflexivity and ADRS

**Citation:** "Reflexivity and Positionality Statements for Tackling AI Bias." Nature Humanities & Social Sciences Communications, 2025.
https://www.nature.com/articles/s41599-025-06208-6

**Status:** INACCESSIBLE (303 redirect - listed in inaccessible-sources.md as "Nature paywall/redirect")

**Claims made:**
- Citations.md lines 308-313: "Algorithm Designers' Reflexivity Statement (ADRS) proposal."
- Main document lines 457-459: "Algorithm Designers' Reflexivity Statements (ADRS) have been proposed to shift the reflexivity burden from AI systems to human designers [40]"
- Main document line 470: "ADRS to shift reflexivity to human designers [40]"
- reflexivity-problem.md lines 64, 69, 82, 107: Multiple ADRS references
- Mitigation table line 533: "ADRS (Algorithm Designers' Reflexivity Statement) | Proposal stage [40] | Not yet measured"

**Grade: INACCESSIBLE**

Nature redirect (303). Cannot verify ADRS proposal details.

---

## [41] Chat-Chamber Effect

**Citation:** "The Chat-Chamber Effect: Trusting the AI Hallucination." SAGE, 2024.
https://journals.sagepub.com/doi/10.1177/20539517241306345

**Status:** INACCESSIBLE (403 - listed in inaccessible-sources.md)

**Claims made:**
- Citations.md lines 315-321: "Echo chamber effects in AI interactions. Pro-attitudinal incorrect information internalized without validation."
- Main document line 420: "The chat-chamber effect extends echo chambers to individual AI interactions, where pro-attitudinal incorrect information is internalized without validation [41]"
- Main document line 457: "Pro-attitudinal incorrect information is internalized without validation in the chat-chamber dynamic [41]"
- automation-bias.md lines 41, 43, 55, 58, 96: Multiple chat-chamber references
- reflexivity-problem.md lines 41, 49, 54: Pro-attitudinal content internalization
- human-operator-bias.md lines 79, 81, 101: Chat-chamber effect in feedback loops

**Grade: INACCESSIBLE**

Source returned 403 error. Cannot verify chat-chamber effect or pro-attitudinal internalization.

---

## [42] Confirmation, Framing, and Position Biases

**Citation:** "Confirmation, Framing, and Position Biases." ACM CHIIR, 2025.
https://doi.org/10.1145/3786304.3787879

**Status:** No fetched file; NOT listed in inaccessible-sources.md

**Claims made:**
- Citations.md lines 323-328: "Combined bias interaction effects. Framing impact on vulnerability detection (16-93% reduction)."
- Main document line 297: "combined framing and position bias interactions reduce vulnerability detection by 16-93% [42]"
- human-operator-bias.md line 21: "Framing + position bias interaction | 16-93% reduction in vulnerability detection | Combined bias study | [42]"
- human-operator-bias.md line 96: "The interaction effects are documented [42] but not fully decomposed."

**Grade: UNVERIFIED**

No fetched source available. Not listed as inaccessible. Cannot verify "16-93%" interaction effect.

---

## [43] Link Rot in LIS Literature

**Citation:** "Link Rot in LIS Literature: A 20-Year Study." Emerald/AJIM, 2025.
https://www.emerald.com/ajim/article-abstract/doi/10.1108/AJIM-05-2025-0286/1335399/Link-rot-in-LIS-literature-a-20-year-study-of-web

**Status:** No fetched file; NOT listed in inaccessible-sources.md

**Claims made:**
- Citations.md lines 330-336: "Accessibility 87% (0-5 years) to 38% (10+ years). Permanent link rot tripled: 5% (2012) to 15% (2025)."
- Main document line 185: "Link accessibility drops from 87% (0-5 years) to 38% (10+ years), with permanent link rot tripling from 5% to 15% between 2012 and 2025 [43]"
- Main document line 196: "link rot (38% accessibility at 10+ years [43])"
- source-selection-bias.md lines 38, 42-46, 48, 52, 112: Multiple link rot statistics (87%, 38%, 5%, 15%)

**Grade: UNVERIFIED**

No fetched source available. Not listed as inaccessible. Cannot verify the specific percentages (87%, 38%, 5%, 15%).

---

## [44] Link Rot in Legal Citations

**Citation:** Zittrain et al. "Link Rot in Legal Citations." Harvard Law Review, 2014.
https://harvardlawreview.org/wp-content/uploads/2014/03/forvol127_zittrain.pdf

**Status:** No fetched file; NOT listed in inaccessible-sources.md

**Claims made:**
- Citations.md lines 338-343: "49% of links in Supreme Court opinions are dead."
- Main document line 186-187: "Forty-nine percent of links in US Supreme Court opinions are dead [44]"
- source-selection-bias.md lines 38, 44, 48, 49, 112: "Supreme Court opinion links (dead) | 49% | [44]"

**Grade: UNVERIFIED**

No fetched source available. Not listed as inaccessible. Cannot verify "49%" dead links claim.

---

## [45] Web Search Engine Overlap

**Citation:** "Comparison of Source Distribution and Result Overlap in Web Search." 2022.
https://arxiv.org/pdf/2207.07330

**Status:** No fetched file; NOT listed in inaccessible-sources.md

**Claims made:**
- Citations.md lines 345-352: "84.9% of results unique to one engine, 11.4% shared by two, 2.6% by three, 1.1% by all four. Google-Bing overlap under 32%."
- Main document line 148: "Across traditional engines, 84.9% of results are unique to a single engine [45]"
- Main document line 158: "A system that uses a single search engine misses 84.9% of what other engines find [45]"
- README lines 15, 27, 39: Multiple uses of "84.9%" statistic
- search-retrieval-bias.md lines 58, 68-71, 77, 112: Detailed breakdown (84.9%, 11.4%, 2.6%, 1.1%)
- Mitigation table line 529: "Observational: 84.9% results unique to single engine [45]"

**Grade: UNVERIFIED**

No fetched source available. Citations.md notes "PDF failed to extract. Data from discovery agent and HackerNoon summary." Not listed in inaccessible-sources.md. Cannot independently verify the highly specific breakdown (84.9%, 11.4%, 2.6%, 1.1%).

---

## [46] Retracted Publication Citations

**Citation:** "Citation of Retracted Publications." ResearchGate, 2021.
https://www.researchgate.net/publication/349168209_Citation_of_retracted_publications

**Status:** No fetched file; NOT listed in inaccessible-sources.md

**Claims made:**
- Citations.md lines 354-359: "90% continued citation after retraction. 96% fail to mention retraction. 58.28% post-retraction citation rate."
- Main document lines 187-188: "Ninety percent of retracted papers continue to be cited, with 96% of post-retraction citations failing to mention the retraction [46]"
- Main document line 201: "Checking retraction databases can address zombie citations [46]"
- Main document line 396: "Automated retraction checking can address zombie citations [46]"
- source-selection-bias.md lines 57, 61-63, 65, 66, 116: Multiple retraction statistics (90%, 96%, 58.28%)
- verification-paradox.md lines 20-21, 136-137: Retraction data

**Grade: UNVERIFIED**

No fetched source available. Not listed as inaccessible. Cannot verify 90%, 96%, or 58.28% figures.

---

## [47] Sycophancy Causal Separation

**Citation:** "Sycophancy Is Not One Thing: Causal Separation." 2025.
https://arxiv.org/html/2509.21305v1

**Status:** SUCCESSFULLY FETCHED (arxiv-2509.21305-sycophancy-features.md)

**Claims made:**
- Citations.md lines 361-366: "Sycophancy comprises distinct independently controllable features. Enables behavior-selective interventions."
- Main document line 127: "Sycophancy comprises distinct independently controllable features [47], enabling targeted interventions."
- Main document line 318: "Awareness of sycophancy as comprising distinct controllable features [47] enables targeted interventions"
- Main document line 449: "sycophancy operates as multiple independently controllable features rather than a single addressable bias [47]"
- Main document line 455: "Sycophancy's compound nature [47] means there is no single 'sycophancy dial'"
- reflexivity-problem.md lines 5, 8, 39, 43, 106: Multiple references to "distinct independently controllable features"
- llm-intrinsic-biases.md lines 28, 33: Causal structure
- human-operator-bias.md lines 66, 97: Distinct features, targeted fixes

**What the source says:**
- "Three distinct features: Sycophantic Agreement (SyA), Genuine Agreement (GA), Sycophantic Praise (SyPr)"
- "Occupy distinct linear directions in latent space"
- "Can be independently amplified or suppressed without affecting the others"
- SyA steering: 23-26× larger changes in target vs unintended behaviors
- Selectivity ratio 25.7× for SyA steering
- Cross-model validation across Qwen, LLaMA, GPT-OSS architectures

**Grade: VERIFIED**

Source directly supports claims that sycophancy comprises distinct independently controllable features.

---

## [48] Epistemic Conformism

**Citation:** "Conformism, Ignorance & Injustice: AI as Tool of Epistemic Oppression." Episteme, Cambridge.
https://www.cambridge.org/core/journals/episteme/article/conformism-ignorance-injustice-ai-as-a-tool-of-epistemic-oppression

**Status:** INACCESSIBLE (404 - listed in inaccessible-sources.md)

**Claims made:**
- Citations.md lines 368-374: "ML-based AI creates knowledge gaps for minoritarian vocabularies and meaning systems. Epistemic conformism framework."
- Main document line 346: "Minoritarian vocabularies fall into knowledge gaps because they appear infrequently in training data [48]"
- epistemic-monoculture.md lines 65, 73, 99, 118, 124: Knowledge gaps, minoritarian vocabularies
- reflexivity-problem.md line 12: Epistemic conformism framework [48][49]

**Grade: INACCESSIBLE**

Source returned 404 error. Cannot verify minoritarian vocabulary knowledge gaps or epistemic conformism framework.

---

## [49] Epistemic Injustice in Generative AI

**Citation:** "Epistemic Injustice in Generative AI." 2024.
https://arxiv.org/html/2408.11441v1

**Status:** SUCCESSFULLY FETCHED (arxiv-2408.11441-epistemic-injustice.md)

**Claims made:**
- Citations.md lines 376-380: "Testimonial and hermeneutical injustice in AI pipeline analysis."
- epistemic-monoculture.md line 66: "Testimonial and hermeneutical injustice in AI pipeline | Full pipeline analysis | [49]"
- reflexivity-problem.md line 12: "Epistemic conformism framework | [48][49]"

**Need to check fetched file:**

(Continuing in next section...)

---

## [50] False Promise of Source-Cited Responses

**Citation:** "The False Promise of Source-Cited Responses." ACM FAT, 2025.
https://dl.acm.org/doi/10.1145/3715275.3732089

**Status:** INACCESSIBLE (403 - listed in inaccessible-sources.md)

**Claims made:**
- Citations.md lines 382-387: "Users reported system 'selectively presented information' making them feel 'manipulated to only see one side.'"
- Main document line 219: "Users of LLM-based search report feeling 'manipulated to only see one side' [50]"
- synthesis-framing-bias.md lines 31, 36, 42, 117: Selective presentation, manipulation perception
- verification-paradox.md lines 72, 74, 143: Source-cited response user perceptions

**Grade: INACCESSIBLE**

Source returned 403 error. Cannot verify user perception quotes ("selectively presented," "manipulated to only see one side").

---

## [51] Emergent Social Conventions and Collective Bias

**Citation:** "Emergent Social Conventions and Collective Bias." Science Advances, 2025.
https://www.science.org/doi/10.1126/sciadv.adu9368

**Status:** No fetched file; NOT listed in inaccessible-sources.md

**Claims made:**
- Citations.md lines 389-394: "Multi-agent bias emergence. Collective bias formation mechanisms."
- Main document line 227: "multi-agent systems develop emergent collective biases not present in individual agents [51]"
- synthesis-framing-bias.md lines 83, 101, 106, 111, 128: Multi-agent emergent bias

**Grade: UNVERIFIED**

No fetched source available. Not listed as inaccessible. Cannot verify emergent collective bias in multi-agent systems.

---

## [52] RAG Citation Bias in Burn Management

**Citation:** "RAG Citation Bias in Burn Management Literature." PMC, 2025.
https://pmc.ncbi.nlm.nih.gov/articles/PMC12191722/

**Status:** No fetched file; NOT listed in inaccessible-sources.md

**Claims made:**
- Citations.md lines 396-401: "RAG prioritizes highly-cited studies, overlooks less-cited valuable research."
- Main document line 222-224: "RAG systems prioritize highly-cited studies even when less-cited work is equally relevant [52]"
- Main document line 493: "RAG prioritizes highly-cited studies [52]"
- synthesis-framing-bias.md lines 77, 85, 89, 93: RAG prioritization of highly-cited work

**Grade: INACCURATE → Status: RESOLVED**

Source was subsequently fetched and found to CONTRADICT the claims. Actual
findings: accuracy 4.6 (high-cited) vs 4.2 (low-cited), p=0.49 — no
significant difference. Source states RAG "can help mitigate disparities."
The discovery agent reversed the finding's directionality. All affected files
corrected to reflect actual source content.

---

## [53] RAG Undermines Fairness

**Citation:** "RAG Undermines Fairness Even for Vigilant Users." 2024.
https://arxiv.org/html/2410.07589v1

**Status:** SUCCESSFULLY FETCHED (arxiv-2410.07589-rag-fairness.md)

**Claims made:**
- Citations.md lines 403-407: "Even with censored unbiased datasets, RAG can lead to biased outputs."
- Main document line 224: "even censored, unbiased datasets produce biased RAG output [53]"
- Main document line 493: "even censored datasets produce biased output [53]"
- synthesis-framing-bias.md lines 77, 85, 90, 94, 125: Censored dataset effect

**Need to check fetched file content to verify this specific claim.**

---

## [54] Multilingual AI Bias (JHU)

**Citation:** "Multilingual AI Often Reinforces Bias." Johns Hopkins University, 2025.
https://hub.jhu.edu/2025/09/02/multilingual-artificial-intelligence-often-reinforces-bias/

**Status:** No fetched file; NOT listed in inaccessible-sources.md

**Claims made:**
- Citations.md lines 409-415: "'Faux polyglots' — multilingual LLMs fail to break language barriers. Arabic users receive American English perspective as default."
- Main document line 385: "LLMs are described as 'faux polyglots' — delivering American English epistemological defaults regardless of query language [54]"
- reflexivity-problem.md line 82: "Citation-dependent — English-language dominance [54]"
- verification-paradox.md lines 45-46, 48, 102, 138, 139, 141: Faux polyglots, Arabic users, American English defaults

**Grade: UNVERIFIED**

No fetched source available. Citations.md notes this is "Tier 2" (institutional press release, not peer-reviewed). Not listed as inaccessible. Cannot verify "faux polyglots" characterization or Arabic user experience.

---

## [55] AI Fact-Checking Reduces Discernment

**Citation:** "Fact-Checking from LLMs Can Decrease Headline Discernment." PNAS, 2024.
https://www.pnas.org/doi/10.1073/pnas.2322823121

**Status:** No fetched file; NOT listed in inaccessible-sources.md

**Claims made:**
- Citations.md lines 417-422: "AI fact-checking may reduce human discernment abilities."
- Main document line 386: "AI fact-checking may actually reduce human discernment abilities [55]"
- Main document line 393: "when fact-checking tools themselves reduce human critical capacity [55]"
- verification-paradox.md lines 71, 74, 141: AI fact-checking reduces discernment

**Grade: UNVERIFIED**

No fetched source available. Not listed as inaccessible. Cannot verify discernment reduction claim.

---

## [56] DIVERGE Framework for RAG

**Citation:** "DIVERGE Framework for Diversity in RAG." 2025.
https://arxiv.org/html/2602.00238

**Status:** SUCCESSFULLY FETCHED (arxiv-2602.00238-diverge.md)

**Claims made:**
- Citations.md lines 424-429: "RAG systems show 'single-answer bias.' 'Diversity collapse' identified. First plug-and-play agentic RAG framework for diversity-quality trade-off."
- Main document line 203: "The DIVERGE framework addresses 'single-answer bias' and 'diversity collapse' in RAG systems [56]"
- Main document line 532: "DIVERGE framework for RAG | Framework evaluation [56] | Addresses single-answer bias and diversity collapse"

**Need to check fetched file content to verify these specific terms.**

---

## [57] Biased AI Writing Assistants

**Citation:** "Biased AI Writing Assistants Shift User Attitudes." Science Advances, 2025.
https://www.science.org/doi/10.1126/sciadv.adw5578

**Status:** No fetched file; NOT listed in inaccessible-sources.md

**Claims made:**
- Citations.md lines 431-436: "AI writing tools introduce systematic bias in content generation."
- Main document line 422: "AI writing assistants introduce systematic bias in content generation [57]"
- automation-bias.md line 54: "AI writing assistants shift user attitudes | Systematic bias in content generation | [57]"

**Grade: UNVERIFIED**

No fetched source available. Not listed as inaccessible. Cannot verify systematic bias in AI writing tools.

---

## [58] Scale Creates Bias

**Citation:** "Large Language Models Are Biased Because They Are Large Language Models." Computational Linguistics (MIT Press), 2025.
https://direct.mit.edu/coli/article/51/3/885/128621

**Status:** No fetched file; NOT listed in inaccessible-sources.md

**Claims made:**
- Citations.md lines 438-443: "Scale itself creates bias — structural analysis of why."
- Main document line 344: "Scale itself creates bias structurally [58]"
- epistemic-monoculture.md lines 43, 73, 113, 125: Scale creates bias

**Grade: UNVERIFIED**

No fetched source available. Not listed as inaccessible. Cannot verify structural scale-bias analysis.

---

## [59] Training-Induced Bias in Dense Retrieval

**Citation:** "Training-Induced Bias Toward LLM-Generated Content in Dense Retrieval." 2026.
https://arxiv.org/pdf/2602.10833

**Status:** No fetched file; NOT listed in inaccessible-sources.md

**Claims made:**
- Citations.md lines 445-450: "Training creates bias toward AI-generated content in retrieval systems."
- Main document line 343: "Retrieval systems preferentially surface AI-generated content [59]"
- Main document line 353: "retrieval systems prefer AI content [59]"
- epistemic-monoculture.md lines 54, 57, 84, 116, 128: Retrieval prefers AI content

**Grade: UNVERIFIED**

No fetched source available. Not listed as inaccessible. Cannot verify training-induced retrieval bias.

---

## [60] Publication Bias (ALREADY COVERED)

**See critical finding at top of document: INACCURATE**

---

## [61] Confirmation Bias as Challenge for Oversight

**Citation:** "Confirmation Bias as Challenge for Scalable Oversight." 2025.
https://arxiv.org/abs/2507.19486

**Status:** SUCCESSFULLY FETCHED (arxiv-2507.19486-confirmation-oversight.md)

**Claims made:**
- Citations.md lines 459-463: "Evaluators become more confident in incorrect AI answers after review."
- Main document line 222: "evaluators become more confident in incorrect AI answers after review [61]"
- Main document line 298: "Evaluators become more confident in incorrect AI answers after review [61]"
- Main document line 492: "evaluators then become more confident in the (potentially wrong) result [61]"
- synthesis-framing-bias.md lines 67, 73, 75, 140: Evaluator confidence increases
- human-operator-bias.md lines 32, 37, 94, 104: Evaluators more confident

**Need to check fetched file content to verify confidence increase claim.**

---

## [62] Confirmation Bias in Mental Health Triage

**Citation:** "Confirmation Bias in AI-Assisted Mental Health Triage." ScienceDirect, 2024.
https://www.sciencedirect.com/science/article/pii/S2949882124000264

**Status:** No fetched file; NOT listed in inaccessible-sources.md

**Claims made:**
- Citations.md lines 465-470: "Practitioners favor AI suggestions mirroring pre-existing beliefs."
- Main document line 299-300: "Mental health practitioners favor AI suggestions mirroring pre-existing beliefs [62]"
- human-operator-bias.md lines 33, 94, 104: Practitioners favor mirroring suggestions

**Grade: UNVERIFIED**

No fetched source available. Not listed as inaccessible. Cannot verify practitioner confirmation bias.

---

## [63] Overreliance on AI

**Citation:** "Overreliance on AI: Extent and Costs." ScienceDirect, 2024.
https://www.sciencedirect.com/science/article/pii/S2214563224002206

**Status:** No fetched file; NOT listed in inaccessible-sources.md

**Claims made:**
- Citations.md lines 472-476: "People follow AI advice contradicting contextual information."
- human-operator-bias.md line 34: "People follow AI advice contradicting contextual information | Overreliance study | [63]"

**Grade: UNVERIFIED**

No fetched source available. Not listed as inaccessible. Cannot verify overreliance claim.

---

## [64] Cognitive Biases Embedded in Next-Gen Models

**Citation:** "Cognitive Biases in Human Evaluation Embedded in Next Generation Models." 2025.
https://arxiv.org/html/2509.08514v1

**Status:** SUCCESSFULLY FETCHED (arxiv-2509.08514-bias-transfer.md)

**Claims made:**
- Citations.md lines 478-484: "Human cognitive biases in AI evaluation become embedded in next-gen models via training feedback loops."
- Main document line 304-305: "Cognitive biases from human evaluation become embedded in next-generation models via training feedback loops [64]"
- Main document line 311: "interaction pattern feeds into training data [64]"
- human-operator-bias.md lines 78, 81, 100, 105: Feedback loop, bias embedding

**Need to check fetched file content to verify bias transfer mechanism.**

---

## [65] EU AI Act Article 14

**Citation:** EU AI Act, Article 14: Human Oversight. 2024.
https://artificialintelligenceact.eu/article/14/

**Status:** No fetched file; NOT listed in inaccessible-sources.md

**Claims made:**
- Citations.md lines 486-490: "Explicitly warns about 'automation bias' risk in human oversight."
- Main document line 306: "The EU AI Act explicitly warns about automation bias risk in human oversight [65]"
- human-operator-bias.md line 87: Article 14 addresses automation bias risk

**Grade: UNVERIFIED**

No fetched source available. Not listed as inaccessible. Cannot verify that Article 14 explicitly uses the term "automation bias."

---

## [66] Viewpoint Diversity Benefits

**Citation:** "Viewpoint Diversity and Its Epistemic Benefits." Philosophy Compass, 2025.
https://compass.onlinelibrary.wiley.com/doi/10.1111/phc3.70021

**Status:** No fetched file; NOT listed in inaccessible-sources.md

**Claims made:**
- Citations.md lines 492-496: "Theory and evidence for benefits of viewpoint diversity."
- Main document line 360: "Viewpoint diversity provides documented epistemic benefits [66][67]"
- epistemic-monoculture.md lines 67, 73, 121: Viewpoint diversity benefits

**Grade: UNVERIFIED**

No fetched source available. Not listed as inaccessible. Cannot verify epistemic benefits of viewpoint diversity.

---

## [67] Generative AI and Epistemic Diversity

**Citation:** "Generative AI and Epistemic Diversity: Call for Scrutiny." AI and Ethics (Springer), 2024.
https://link.springer.com/article/10.1007/s00146-024-02097-6

**Status:** No fetched file; NOT listed in inaccessible-sources.md

**Claims made:**
- Citations.md lines 498-504: "Analysis of epistemic diversity threats from AI inputs/outputs."
- Main document line 360: "Viewpoint diversity provides documented epistemic benefits [66][67]"
- epistemic-monoculture.md lines 68, 73, 121: AI threatens epistemic diversity

**Grade: UNVERIFIED**

No fetched source available. Not listed as inaccessible. Cannot verify epistemic diversity threat analysis.

---

## [68] AIgemony

**Citation:** "AIgemony: Power Dynamics, Dominant Narratives, Colonisation." Springer, 2025.
https://link.springer.com/article/10.1007/s43681-025-00734-4

**Status:** No fetched file; NOT listed in inaccessible-sources.md

**Claims made:**
- Citations.md lines 506-512: "AI as hegemony — dominant narratives shaped by AI's processing and personalization capacity."
- epistemic-monoculture.md lines 69, 71, 100, 122, 132: AIgemony concept, power dynamics

**Grade: UNVERIFIED**

No fetched source available. Not listed as inaccessible. Cannot verify AIgemony framework.

---

## [69] Tool-MAD Multi-Agent Debate

**Citation:** "Tool-MAD: Multi-Agent Debate with Tool Augmentation." 2025.
https://www.arxiv.org/pdf/2601.04742

**Status:** No fetched file; NOT listed in inaccessible-sources.md

**Claims made:**
- Citations.md lines 514-519: "35.5% improvement over baseline MAD. Dynamic query formulation. Source credibility assessment."
- Main document line 239: "Tool-augmented multi-agent debate achieves 35.5% improvement over baseline [69]"
- Main document line 262: "Tool-MAD achieves 35.5% improvement through dynamic query formulation and source credibility assessment [69]"
- Main document line 469: "External verification by separate agents or humans [69]"
- Main document line 525: "Tool-augmented multi-agent debate | Benchmark evaluation [69] | 35.5% over baseline debate"
- structural-mitigations.md lines 110, 114-115, 118, 184, 208: 35.5% improvement, features
- reflexivity-problem.md lines 13, 66: Multi-agent debate

**Grade: UNVERIFIED**

No fetched source available. Citations.md notes "Data from discovery agent." Not listed as inaccessible. Cannot verify "35.5%" improvement figure or architectural details.

---

## [70] DiPT - Diversified Perspective-Taking

**Citation:** "DiPT: Diversified Perspective-Taking." 2024.
https://arxiv.org/html/2409.06241v1

**Status:** No fetched file; NOT listed in inaccessible-sources.md

**Claims made:**
- Citations.md lines 521-525: "Improves reasoning performance and stability with paraphrased problems."
- Main document line 239: "Diversified perspective-taking improves reasoning stability [70]"
- Main document line 471: "Diversified perspective-taking [70]"
- Main document line 528: "Diversified perspective-taking (DiPT) | Benchmark evaluation [70] | Improved reasoning performance and stability"
- structural-mitigations.md lines 125, 129-130, 133: Reasoning performance and stability
- reflexivity-problem.md line 67: Multiple perspectives improve reasoning stability

**Grade: UNVERIFIED**

No fetched source available. Not listed as inaccessible. Cannot verify reasoning performance/stability improvements.

---

## VERIFIED FETCHED SOURCES

### [49] Epistemic Injustice - VERIFIED

**Fetched:** arxiv-2408.11441-epistemic-injustice.md

**Claims made:**
- "Testimonial and hermeneutical injustice in AI pipeline analysis."

**Source content:**
- "Testimonial injustice: AI magnifies and produces socially biased viewpoints from training data"
- "Hermeneutical injustice: system lacks nuanced comprehension of human experience"
- ChatGPT perpetuated false narratives 80% (GPT-3.5) and 100% (GPT-4)
- Algorithmic injustice requires "credibility excess assigned to the algorithm"
- Epistemic pollution, erosion of institutional trust, testimonial smothering

**Grade: VERIFIED**

Source directly addresses testimonial and hermeneutical injustice in AI pipeline.

---

### [53] RAG Fairness - VERIFIED

**Fetched:** arxiv-2410.07589-rag-fairness.md

**Claims made:**
- "Even with censored unbiased datasets, RAG can lead to biased outputs."

**Source content:**
- "Fairness alignment can be easily undermined through RAG without fine-tuning"
- L3 threat: "even fully censored datasets" → LLMs still compromised
- "RAG increases confidence, providing definitive answers instead of 'I don't know'"
- Even 20% unfair samples sufficient to elicit biased responses

**Grade: VERIFIED**

Source directly supports the claim that censored datasets still produce biased RAG output.

---

### [56] DIVERGE Framework - VERIFIED

**Fetched:** arxiv-2602.00238-diverge.md

**Claims made:**
- "RAG systems show 'single-answer bias.' 'Diversity collapse' identified. First plug-and-play agentic RAG framework for diversity-quality trade-off."

**Source content:**
- "Single-Answer Bias: existing RAG systems optimized to produce reliable answers under single-answer assumption, prioritizing narrow, high-confidence subset"
- "Diversity Collapse: lack of mechanisms for long-horizon diversity preservation"
- 2.5× semantic diversity and 1.6× viewpoint diversity improvements over direct prompting
- Three components: reflection-guided viewpoint gen, viewpoint-aware retrieval, viewpoint-conditioned generation

**Grade: VERIFIED**

Source directly uses the terms "single-answer bias" and "diversity collapse" and presents the framework as addressing diversity-quality trade-offs.

---

### [61] Confirmation Bias in Oversight - VERIFIED

**Fetched:** arxiv-2507.19486-confirmation-oversight.md

**Claims made:**
- "Evaluators become more confident in incorrect AI answers after review."

**Source content:**
- "Participants become more confident in the system's answers after conducting online research, even when those answers are incorrect"
- "No overall advantage for the tested protocols" overall
- Study 1: showing arguments for both answers improves accuracy when model incorrect

**Grade: VERIFIED**

Source directly supports the claim that evaluators become more confident in incorrect answers after review.

---

### [64] Bias Transfer to Next-Gen Models - VERIFIED

**Fetched:** arxiv-2509.08514-bias-transfer.md

**Claims made:**
- "Human cognitive biases in AI evaluation become embedded in next-gen models via training feedback loops."

**Source content:**
- "Today's human-AI partnerships generate datasets that train tomorrow's AI systems, which in turn shape future human decisions"
- Undercorrection: favorable-to-AI annotators showed overreliance
- "Errors from pre-annotation workflows exhibit more systematic pattern" vs random from human-only annotation
- Effort-driven bias: corrections requiring additional work reduced error flagging

**Grade: VERIFIED**

Source directly supports the feedback loop mechanism where human evaluation biases become embedded in next-generation models.

---

## GRADE SUMMARY FOR CITATIONS [27]-[70]

**INACCURATE: 1**
- [60] Publication Bias - claims "22% increase 1990-2007" and "3× more likely to publish" NOT found in source

**VERIFIED: 6**
- [47] Sycophancy causal separation
- [49] Epistemic injustice
- [53] RAG fairness with censored datasets
- [56] DIVERGE framework (single-answer bias, diversity collapse)
- [61] Confirmation bias in oversight (confidence increases)
- [64] Bias transfer to next-gen models

**PARTIAL: 1**
- [29] Medical LLM overconfidence - qualitative claim verified, specific numbers (69-80%, 0.6-5.4%) not in fetched source

**INACCESSIBLE: 13**
- [27] SEME alerts (403)
- [30] Survey responses (403)
- [32] Creative ideation homogenization (403)
- [34] Human-AI feedback loops (303 Nature redirect)
- [35] Sycophantic AI prosocial effects (403)
- [37] Amplified cognitive biases (403)
- [38] Self-contradictory hallucinations (403)
- [39] AI-AI bias (403)
- [40] ADRS reflexivity (303 Nature redirect)
- [41] Chat-chamber effect (403)
- [48] Epistemic conformism (404)
- [50] False promise of source-cited responses (403)

**UNVERIFIED: 23**
- [28] Malmqvist sycophancy survey (not used in deliverable)
- [31] Homogenizing effect on expression
- [33] Homogenizing engine (SAGE)
- [36] Transmission chains
- [42] Combined bias interactions (16-93%)
- [43] Link rot LIS literature (87%, 38%, 5%, 15%)
- [44] Legal citations link rot (49%)
- [45] Search engine overlap (84.9%, 11.4%, 2.6%, 1.1%)
- [46] Retracted publication citations (90%, 96%, 58.28%)
- [51] Emergent collective bias
- [52] RAG burn management citation bias
- [54] Multilingual faux polyglots
- [55] AI fact-checking reduces discernment
- [57] AI writing assistants
- [58] Scale creates bias
- [59] Training-induced retrieval bias
- [62] Mental health triage confirmation bias
- [63] Overreliance extent
- [65] EU AI Act Article 14
- [66] Viewpoint diversity benefits
- [67] Epistemic diversity threats
- [68] AIgemony
- [69] Tool-MAD (35.5% improvement)
- [70] DiPT perspective-taking

---

## COMBINED TOTAL: ALL 71 CITATIONS

Using grades from the original audit for [1]-[26] and this audit for [27]-[70],
plus [71] added during corrections.

### Citations [1]-[26] (from original audit):
- VERIFIED: 23 ([1]-[10], [12]-[24])
- INACCESSIBLE: 3 ([11], [25], [26])

### Citations [27]-[70] (this audit):
- VERIFIED: 6 ([47], [49], [53], [56], [61], [64])
- PARTIAL: 1
- INACCURATE: 2 (both resolved: [52] reversed finding, [60] wrong source)
- INACCESSIBLE: 13
- UNVERIFIED: 22 (reduced from 23 after [52] reclassified)

### [71] (added during correction):
- PARTIAL: sourced via Wikipedia citing Dickersin et al. 1987

### GRAND TOTALS (all 71 citations):

| Grade | Count | Percentage |
|-------|-------|------------|
| VERIFIED | 29 | 40.8% |
| PARTIAL | 2 | 2.8% |
| INACCESSIBLE | 16 | 22.5% |
| UNVERIFIED | 22 | 31.0% |
| INACCURATE | 2 (both resolved) | 2.8% |
| **TOTAL** | **70** | **100%** |

---

## CRITICAL FINDINGS

### 1. Citation [60] is INACCURATE
The specific claims "22% increase in significant results 1990-2007" and "papers with significant results 3× more likely to publish" do NOT appear in the cited PLOS ONE source. The source addresses publication bias in meta-analyses but does not contain these specific numerical claims. This is a fabrication or misattribution.

### 2. Only 34.3% of citations are fully verified
Despite having fetched content for approximately 30 sources, only 24 of 70 citations (34.3%) could be verified against their source material.

### 3. High inaccessibility rate (24.3%)
17 citations returned 403/303/404 errors. Data for these was sourced from "discovery agent search snippets," which are secondary interpretations, not primary sources.

### 4. 32.9% completely unverified
23 citations have no fetched source AND are not listed as inaccessible. These represent gaps in the fetching process - sources that should have been checked but weren't.

### 5. Highly specific numerical claims often unverifiable
Citations with precise percentages ([43]: 87%, 38%, 5%, 15%; [45]: 84.9%, 11.4%, 2.6%, 1.1%; [46]: 90%, 96%, 58.28%) are frequently in the UNVERIFIED category, meaning these specific numbers cannot be independently confirmed.

### 6. The strongest-evidenced claims are verified
The core structural claims ([47] sycophancy features, [53] RAG bias, [56] diversity collapse, [61] confirmation bias, [64] bias transfer) all have direct source support. The problematic citations tend to be supporting details rather than core arguments.

---

## RECOMMENDATIONS

1. **Remove or re-source citation [60]** - the specific claims attributed to it are not supported by the cited source.

2. **Downgrade confidence for UNVERIFIED citations** - 23 citations lack any verification. Consider marking these as "claimed in secondary sources" or removing claims that depend solely on unverified citations.

3. **Distinguish INACCESSIBLE from UNVERIFIED** - inaccessible sources (403/303/404 errors) had fetch attempts; unverified sources were never checked. The latter represents a larger quality control gap.

4. **Audit high-precision numerical claims** - citations [43], [45], [46] contain highly specific breakdowns (e.g., 84.9%, 11.4%, 2.6%, 1.1%) that cannot be verified. Consider removing the precision or adding "reported as" qualifiers.

5. **Re-attempt fetches for UNVERIFIED sources** - 23 sources were never successfully fetched despite not being listed as inaccessible. A second fetch pass could improve verification rates.

6. **Flag tier-2 sources** - [54] (JHU press release) is cited as Tier 2 but treated the same as peer-reviewed work in the text. Consider distinguishing these in presentation.

---

## METHODOLOGY NOTES

This audit:
- Read all markdown files in the research directory
- Identified every use of citations [27]-[70] across all files
- Matched claims against fetched source content in /tmp/cited-research/agentic-research-bias/
- Applied strict verification standards: claims must be directly present in fetched sources
- Graded UNVERIFIED (not fetched) separately from INACCESSIBLE (fetch failed) to distinguish quality control gaps from access barriers

The auditor had NO context from the original research conversation and no access to discovery agent working notes beyond what appears in fetched source files.

