# Real-world incidence vs lab demonstration

This file evaluates the question added as the 8th dimension during planning: are there *any* confirmed in-the-wild memory poisoning incidents in production agent systems, or only research-lab demonstrations?

See [citations.md](../citations.md) for source details.

## The honest answer

**There are no publicly confirmed cases of successful memory poisoning via prompt injection in a production enterprise agent system causing measurable harm.**

What exists:

| Category | Count | Best example | Source |
|---|---|---|---|
| Real-world deployment of memory-poisoning *attempts* | 50 (over 60 days, 31 companies) | Microsoft AI Recommendation Poisoning | [15] |
| Authorized researcher PoCs against live consumer AI products | several | SpAIware (ChatGPT), Gemini Memory, Claude (per OWASP) | [20], [21], [13] |
| Lab demonstrations against benchmark agents | many | AgentPoison, MemoryGraft, MINJA, eTAMP | [1], [7], [38], [3] |
| Confirmed production memory-poisoning incident with documented harm | **0 publicly disclosed** | — | — |
| Formal framework codification | 2 | OWASP ASI06, MITRE ATLAS AML.T0080 | [12], per discovery |

## Microsoft AI Recommendation Poisoning — close but not quite

Microsoft's February 2026 finding [15] is the strongest "real-world" data point. Over 60 days of reviewing AI-related URLs in email traffic, Microsoft Defender researchers identified **"50 distinct examples of prompt-based attempts directly aimed to influence AI assistant memory for promotional purposes. These attempts originated from 31 different companies and spanned more than a dozen industries"** [15].

Three critical caveats:

1. **Microsoft observed the attempts, not the successes.** The blog documents the URLs/buttons in the wild but does not claim to have confirmed successful memory writes against real users. The distinction is: 50 confirmed attempts sent vs. 0 (or unknown) confirmed successful poisoning of production user memory.

2. **The attack class is narrower than full memory poisoning.** It is promotional spam via clickable URL-embedded prompts targeting Copilot-style assistant memories — not adversarial corruption of a RAG vector store, not data exfiltration, not system compromise. Whether it counts as "memory poisoning" in the OWASP ASI06 sense depends on how strictly the term is scoped.

3. **Mitigations have reversed some behaviors.** Microsoft notes (verbatim): "In multiple cases, previously reported behaviors could no longer be reproduced." Persistence is not guaranteed and degrades as defenses deploy.

If the question is "have any companies maliciously deployed memory-poisoning attempts in the wild?", the answer is yes — 31 companies in 60 days. If the question is "has any production agent system been measurably harmed by memory poisoning?", the answer is no documented case.

## What the demonstrations are

The "real-world demonstrations" cited by OWASP and others are authorized researcher disclosures:

- **SpAIware** (Rehberger 2024 [20]): ChatGPT macOS app. Authorized disclosure, BSides Vancouver Island. OpenAI patched in v1.2024.247.
- **Gemini Memory Attack** (Rehberger Feb 2025 [21]): Authorized disclosure to Google December 2024. Google's response: "an abuse-related risk with low likelihood and low impact." This is the example OWASP cites for ASI06 [13].
- **Claude memory attack** (April 2026, per discovery agent threat-taxonomy unfetched): mentioned as "one snippet" but no primary source URL was surfaced.
- **Unit 42 Bedrock attack** [19]: Authorized PoC by Palo Alto researchers in a deliberately weakened Bedrock configuration (Guardrails disabled).

These are **authorized researcher demonstrations against production consumer/cloud AI products**, not unauthorized malicious exploitation in enterprise production contexts.

## The McKinsey Lilli incident — different attack class

The McKinsey Lilli RAG breach (March 2026, per discovery real-world-incidence agent, unfetched primary) is a genuine production breach, but the primary attack vector was **SQL injection** on 22 unauthenticated API endpoints, not memory poisoning via prompt injection. CodeWall's autonomous agent gained read access to 3.68M RAG document chunks via SQL injection. Whether write access was *exercised* (vs merely *demonstrated as possible*) against the corpus is unclear from the discovery agent's report.

This is relevant evidence that RAG knowledge bases can be compromised in production — but it is a category error to cite it as a "memory poisoning incident."

## Lab claims that should not be cited as production data

The ASR figures from topics5.md should be qualified:

| Claim | Source | Lab or production? |
|---|---|---|
| "19.5% on GPT-OSS-120B, 32.5% on GPT-5-mini" | eTAMP [3] | **Lab** — controlled (Visual)WebArena benchmark |
| "Up to 8x under UI friction" | eTAMP [3] | **Lab** — Chaos Monkey perturbations are simulated, not production |
| "AgentPoison >80% ASR at <0.1% poison rate" | [1] | **Lab** — and the 80% is ASR-r retrieval, end-to-end is ~58% |
| "MINJA >95% ISR" | [38, per discovery] | **Lab** — and the realistic-memory dilution found in [4] (testing a different attack on the same model class) suggests similar effects likely apply, though MINJA itself was not re-tested |

**Fabricated or unverified numbers found during research** (do not cite):

- "$45M crypto Step Finance breach" via memory-poisoned trading agent: **fabricated** per real-world counter-discovery agent's verification — KuCoin blog presents hypothetical scenario as if real.
- "CVE-2025-64439 LangGraph RCE memory poisoning": **fabricated** — no NVD entry, used in an educational writeup as fictional.
- "88% of organizations faced a confirmed or suspected incident" attributed to Beam AI: **unverifiable**, no traceable primary source.
- "380 memory poisoning incidents": **unverifiable**, no traceable primary source.

These are exactly the kinds of plausible-looking numbers that propagate through AI-security marketing content without anyone tracing them to a primary source.

## Threat reports (2026) on observed attacks

Per discovery real-world-incidence agent (unfetched primaries):
- IBM X-Force, CrowdStrike, Check Point, Darktrace 2026 threat reports document AI-enabled attacks (300,000+ ChatGPT credentials exposed via infostealers; prompt injection used against GenAI tools at 90+ organizations per IBM X-Force).
- **None** of these reports specifically confirms memory poisoning / RAG poisoning as an observed attack class in production.

The closest is IBM X-Force's prompt-injection-against-GenAI finding, which is not decomposed by attack subtype.

## Bug bounties and CVE disclosures

Per The Register [22] and discovery real-world-incidence agent:
- Anthropic, Google, GitHub paid bug bounties for prompt injection vulnerabilities in GitHub Actions integrations ($100/$1,337/$500). None involved persistent memory poisoning specifically. None resulted in CVE assignment.
- Huntr (AI/ML bug bounty platform): no confirmed memory-poisoning reports with production impact surfaced.

## Implication for threat assessment

The pattern is the same one Bruce Schneier and others have flagged for many emerging threat classes: **abundant demonstrated attacks, abundant vendor warnings, abundant framework codification — and zero confirmed production incidents with disclosed harm**.

This does not mean the threat is fake. The Microsoft empirical data [15] confirms motivated actors are deploying attempts. SpAIware [20] confirms the underlying mechanism works on real consumer products. The OWASP framework codification [12] is a legitimate prospective risk-management response.

But it does mean that **citing the lab ASR figures (32.5%, >80%, etc.) as if they describe the production threat landscape is misleading**. The lab figures describe what happens when attackers have white-box access to embedders, write access to knowledge bases, and stripped-down test corpora. Production deployments differ on every one of those axes.

The honest threat statement is: "demonstrated mechanism, attempts observed in the wild, no confirmed successful production exploitation with disclosed harm to date."

## Gaps and limitations

- IBM Think Insights [28] — the canonical "not seen in the wild" source for Morris-II — returned 403 in this session. The "not in the wild" claim rests on a discovery search snippet.
- The McKinsey Lilli breach details depend on discovery agent reports of CodeWall and BankInfoSecurity coverage; primary sources were not fetched in this session.
- AVID, MITRE ATLAS, OWASP AI Exchange were referenced by discovery but their incident registries were not directly queried for confirmed memory poisoning entries.
- The DEF CON / Black Hat 2026 incident database queries were not run.
- "Industry survey" claims (e.g., the 88% figure) could not be traced to primary sources and may be fabricated.
