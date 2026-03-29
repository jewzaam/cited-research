# Prompt Injection Defenses for LLM Agents That Fetch External Web Content

## Research Question

What approaches exist — in academic research, open-source tooling, and production systems — for defending LLM-based agents against prompt injection when they must ingest untrusted external content (web pages, documents, API responses)? This analysis focuses on agentic workflows where fetched content is passed to sub-agents for analysis, not end-user-facing chatbots.

**Out of scope:** Jailbreaking/alignment attacks on the model itself, training-time poisoning, prompt injection in user-provided input (focus is on third-party content fetched by the agent).

## Methodology

Research conducted via web search and page fetching across academic papers (arXiv, USENIX, ICLR), vendor documentation (OpenAI, Anthropic, Microsoft, NVIDIA, Google DeepMind), industry guidance (OWASP), and open-source repositories. 34 sources cited, each visited in-session. Two independent review agents audited the output: a citation audit verifying claims against source content, and a consistency review checking cross-file agreement.

## Key Findings

### 1. No defense provides deterministic guarantees against prompt injection in agentic systems

Every major vendor and research group acknowledges this explicitly:
- NVIDIA: "cannot be effectively mitigated" at the LLM level [23]
- Anthropic: "No browser agent is immune to prompt injection" [13]
- Microsoft: indirect prompt injection is "an inherent risk" [6]
- The Design Patterns paper consortium: "general-purpose agents can provide meaningful and reliable safety guarantees" remains unlikely [1]

The fundamental reason: LLMs have no instruction-data boundary. Unlike SQL injection (solved by parameterized queries), prompt injection payloads share the same medium — natural language — as legitimate content [23] [5].

### 2. Architectural defenses are more reliable than detection-based defenses

The most promising results come from constraining agent capabilities rather than detecting injection payloads:

| Defense Type | Best Published ASR | Approach | Caveat |
|-------------|-------------------|----------|--------|
| Type-directed separation [7] | 0% | Eliminate freeform text between agents | Severe utility loss on text-heavy tasks |
| OpenClaw isolation [25] | 0% | Split reader/actor agents + JSON formatting | No adaptive attack testing |
| CaMeL [4] | Provable | Capability-based security with data flow tracking | Research prototype, user policy burden |
| Progent manual policies [8] | 0% | Fine-grained tool call constraints via DSL | Manual policy creation required |
| PromptArmor [9] | ~0% | LLM-as-judge preprocessing | Adds API call overhead per request |
| Multi-layer framework [21] | 8.7% | Embedding analysis + prompts + verification | English only, static attacks |
| Anthropic (Opus 4.5) [13] | 1% | RL training + classifiers + red teaming | Browser agent specific |

Meanwhile, detection-based guardrails are routinely bypassed at 70-88% ASR using character injection and adversarial ML techniques [22]. Emoji smuggling alone achieves 100% evasion across all tested systems [22].

### 3. Security and utility are in fundamental tension

The 0% ASR defenses achieve their guarantees by restricting what agents can do. The trade-off is starkest in type-directed separation [7]: bug-fixing utility drops from 49.7% to 14.6% when freeform text is eliminated. CaMeL loses 7 percentage points of task completion (77% vs. 84%) [4]. The multi-layer framework achieves a better balance — 8.7% ASR with 94.3% task retention — but does not reach 0% [21].

### 4. Text-to-text tasks are the hardest open problem

When the agent's purpose is to produce text from text (summarization, translation, content analysis), there is no structural boundary to enforce. CaMeL, type-directed separation, and JSON formatting cannot help because the output must be freeform text [4] [12]. No published defense addresses this case with provable security.

---

## Defense Landscape

### Content Sanitization and Filtering

Techniques for neutralizing injection payloads before they reach the LLM. Full analysis: [references/content-sanitization.md](references/content-sanitization.md).

**Spotlighting** [2] (Microsoft) provides the strongest empirically validated sanitization approach. Three techniques — delimiting, datamarking, and encoding — help LLMs distinguish instructions from data. Datamarking reduces ASR from ~50% to 3-8% on GPT-3.5-Turbo (3.1% summarization, 8.0% Q&A) with no measurable task performance impact. Encoding achieves 0% ASR on GPT-4 but severely degrades performance on smaller models [2]. Microsoft has deployed Spotlighting in production [6].

**DataFilter** [29] strips injected instructions while preserving benign content at the token level, achieving 0.4% ASR as a model-agnostic, test-time filter.

**Pattern matching** (regex for "ignore previous instructions" and similar) [5] catches only the simplest attacks. Adaptive attackers use Unicode hiding, Base64 encoding, emoji smuggling, and multilingual payloads to bypass any fixed pattern set [22].

**JSON formatting** of untrusted content strips persuasive framing. OpenClaw showed this reduces ASR to 14.18% when used alone [25].

### Architectural Defenses

Structural approaches that constrain what a compromised agent can do. Full analysis: [references/architectural-defenses.md](references/architectural-defenses.md).

**Six design patterns** formalized by Beurer-Kellner et al. [1] (IBM/Invariant Labs/ETH Zurich/Google/Microsoft consortium):

1. **Action-Selector** — LLM translates requests to predefined tool calls; no feedback from tool outputs influences decision-making. "Immune to prompt injections" for this constrained case [1].
2. **Plan-Then-Execute** — Fixed action plan before execution; tool outputs cannot influence action selection (but can corrupt action parameters) [1].
3. **LLM Map-Reduce** — Isolated sub-agents process individual documents; malicious input affects only its agent instance [1].
4. **Dual LLM** — Privileged LLM (tools, trusted) + quarantined LLM (no tools, untrusted content). Outputs handled symbolically via orchestrator [1].
5. **Code-Then-Execute** — Agent generates formal code that calls tools and spawns unprivileged LLMs [1].
6. **Context-Minimization** — Removes unnecessary context over multiple interactions [1].

**CaMeL** [4] (Google DeepMind) implements the Dual LLM pattern with capability-based security and data flow tracking via a custom Python interpreter. 77% task completion with provable security on AgentDojo [4]. Simon Willison calls it "the first credible prompt injection mitigation" because security comes from system design, not AI detection [12].

**Instruction Hierarchy** [3] (OpenAI) trains models to enforce System > User > Image/Audio > Tool priority ordering. Improves system prompt extraction defense by 63% and generalizes to unseen attacks (+30% on jailbreaks) despite no jailbreak training data [3].

**Type-directed privilege separation** [7] restricts inter-agent data to integers, floats, booleans, and pre-approved enums. Achieves 0% ASR across all tested scenarios but suffers severe utility loss on text-heavy tasks (−35 points on bug fixing) [7].

**Progent** [8] introduces a JSON Schema DSL for fine-grained privilege policies. Manual policies provably achieve 0% ASR on some benchmarks; automatic policies reach 2.2% on AgentDojo [8].

### Domain and URL Allowlisting

Approaches to constraining which sources agents can fetch. Full analysis: [references/url-allowlisting.md](references/url-allowlisting.md).

The consensus is **deny-by-default** with enforcement at the network/proxy layer, not via system prompt instructions [16] [17] [23]:

- **OpenAI Codex** implements tiered access: off by default, optional allowlist (~60 common domains), HTTP method restriction (GET/HEAD/OPTIONS only for non-allowlisted) [17]
- **LoginRadius architecture** describes multi-layer enforcement: infrastructure (egress firewalls), gateway (API validation), authentication (scoped tokens), with identity-bound logging [16]
- **MCP security** focuses on SSRF prevention (block private IPs, validate redirects, use egress proxies like Smokescreen) and scope minimization [18]

Key limitation: allowlists cannot address injection within allowed domains. A legitimate website can contain injected content. Allowlisting reduces attack surface but does not eliminate the injection problem.

### Detection and Monitoring

Tools for identifying injection attempts in fetched content. Full analysis: [references/detection-monitoring.md](references/detection-monitoring.md).

**Classifier models:**
- ProtectAI DeBERTa [14]: F1=0.9998 in-distribution, but bypassed at 77% ASR by adversarial techniques [22]
- Meta Prompt Guard [15]: 99.9% TPR on jailbreaks in-distribution, but drops to 71.4% on CyberSecEval indirect injections — the scenario most relevant to agentic content fetching
- PromptArmor [9]: LLM-as-judge achieving FPR 0.56% and FNR 0.13% on AgentDojo, but requires API call overhead per request

**Score-based detection:** Cloudflare integrates prompt injection scoring (1-99) into their WAF with configurable thresholds [20].

**Canary tokens:** Vigil-LLM [19] implements two modes — detecting prompt leakage (canary appears in output) and goal hijacking (canary absent from output). Detection-only, not prevention.

**Observability:** Datadog provides chain tracing, semantic similarity checking against known jailbreaks, RAG monitoring, and vector DB audit correlation [24].

**Critical reality check:** Hackett et al. [22] systematically bypassed six production guardrail systems at 70-88% ASR. Emoji smuggling achieved 100% evasion. The gap between in-distribution metrics and adversarial robustness is severe.

### Open-Source Tools and Frameworks

Existing libraries implementing the above defenses. Full analysis: [references/oss-tools-frameworks.md](references/oss-tools-frameworks.md).

**Production-ready detection tools:**
- **LLM Guard** [27]: 15 input + 21 output scanners, MIT license, pip-installable
- **NeMo Guardrails** [26]: 5 rail types with Colang DSL, Apache 2.0, LangChain integration
- **Meta Prompt Guard** [15]: 86M parameter classifier, multilingual (9 languages), fine-tunable

**Research prototypes (architecturally stronger):**
- **CaMeL** [4]: Capability-based architecture, open-source, provable security
- **Progent** [8]: Policy DSL for tool call constraints
- **DataFilter** [29]: Model-agnostic content filtering

**Key gap:** The most architecturally sound defenses (CaMeL, Progent) are research prototypes. The most production-ready tools (LLM Guard, NeMo Guardrails) rely on detection, which is routinely bypassed [22].

### Limitations and Open Problems

What the research says about fundamental difficulty. Full analysis: [references/limitations-open-problems.md](references/limitations-open-problems.md).

**Fundamental barriers:**
1. No instruction-data boundary exists in transformer architecture [23]
2. Capability paradox: more capable models are potentially more vulnerable
3. Power-law scaling: attackers with sufficient resources can eventually bypass defenses [5]
4. Adaptive attacks consistently defeat published defenses [10] [22]

**Open research problems:**
1. Text-to-text attacks (no structural defense possible) [4] [12]
2. Standardized adaptive attack evaluation framework [10]
3. Benchmark fragmentation (AgentDojo vs. CyberSecEval vs. TensorTrust vs. others)
4. Multilingual robustness (TPR degrades ~6 percentage points, from 97.5% to 91.5%) [15]
5. Defense composition effects (how do layers interact?) [1]
6. User policy burden (too hard for non-experts) [12]
7. Production deployment data (most numbers are from benchmarks) [13]

---

## Decision Framework for Agentic Workflows

### If your agents fetch external content, apply defenses in this order:

**Layer 1: Reduce blast radius (architectural)**
- Constrain agent capabilities to the minimum required (Action-Selector or Plan-Then-Execute patterns) [1]
- Separate privileged operations from untrusted content processing (Dual LLM, agent isolation) [1] [4] [25]
- Enforce least-privilege tool access (Progent-style policies) [8]
- Require human approval for high-impact actions [6] [13]

**Layer 2: Restrict attack surface (network)**
- Deny-by-default URL allowlisting at the proxy/firewall layer [16] [17]
- HTTP method restriction (read-only for non-allowlisted domains) [17]
- SSRF prevention (block private IPs, validate redirects) [18]

**Layer 3: Sanitize content (preprocessing)**
- Apply Spotlighting (datamarking recommended as baseline) [2]
- Force structured output (JSON) for untrusted content before passing to privileged agents [25]
- Strip known injection patterns as a cheap first filter [5]

**Layer 4: Detect and monitor (probabilistic)**
- Run classifier-based detection (Meta Prompt Guard for injection/jailbreak distinction) [15]
- Deploy canary tokens for leakage/hijacking detection [19]
- Instrument chain tracing and output monitoring [24]
- Set up alerting for anomalous patterns [5] [24]

**Layer 5: Verify outputs (post-processing)**
- Validate tool calls against user permissions [5] [31]
- Check output consistency with query intent [21]
- Monitor for credential exposure and data exfiltration patterns [5]

### What you cannot currently defend against:

- **Text-to-text injection** where the agent must produce freeform text from untrusted input [4] [12]
- **Sophisticated adaptive attacks** by motivated adversaries who study your defense stack [10] [22]
- **Novel injection techniques** not represented in classifier training data [14] [15]
- **Multilingual injection** with high reliability [15]

---

## Source Summary

| Category | Sources | Key Papers |
|----------|---------|------------|
| Architectural patterns | [1] [4] [7] [8] [25] | Design Patterns [1], CaMeL [4] |
| Content sanitization | [2] [5] [29] | Spotlighting [2], DataFilter [29] |
| Detection/classification | [14] [15] [20] [22] | DeBERTa [14], Prompt Guard [15], Bypass study [22] |
| URL/domain control | [16] [17] [18] | OpenAI Codex [17], MCP Security [18] |
| Monitoring | [19] [24] | Vigil canary tokens [19], Datadog [24] |
| Industry guidance | [5] [6] [13] [23] [31] | OWASP [5], Microsoft [6], Anthropic [13] |
| Evaluation/limitations | [3] [10] [21] | Instruction Hierarchy [3], Critical Evaluation [10] |
| Catalogs/reviews | [11] [12] [26] [27] [28] [30] | tldrsec [30], Willison [11] [12] |

All citations with full URLs, author information, and extraction notes: [citations.md](citations.md).
