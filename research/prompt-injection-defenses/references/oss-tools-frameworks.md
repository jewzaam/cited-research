# Open-Source Tools and Frameworks

Dimension covering existing libraries, MCP servers, and agent frameworks that implement prompt injection defenses. Sources referenced via `[N]` — see [citations.md](../citations.md) for full entries.

## Overview

The open-source landscape for prompt injection defense is active but immature. Most tools focus on detection (classifiers, pattern matching) rather than architectural prevention. No tool provides deterministic guarantees against injection in agentic workflows [30].

## Tool Comparison

| Tool | Approach | License | Key Metric | Status |
|------|----------|---------|------------|--------|
| LLM Guard [27] | Multi-scanner pipeline | MIT | 15 input + 21 output scanners | Active, ~104K monthly downloads (via DeBERTa model) |
| Rebuff [28] | 4-layer detection | — | Heuristics + LLM + VectorDB + canaries | Prototype ("cannot provide 100% protection") |
| NeMo Guardrails [26] | Programmable rails | Apache 2.0 | 5 rail types with Colang DSL | Active, 72-73% bypass ASR [22] |
| Meta Prompt Guard [15] | 3-class classifier | Llama 3.1 Community | 99.9% TPR in-dist, 71.4% indirect | Active, ~25K monthly downloads |
| DeBERTa PI Classifier [14] | Binary classifier | Apache 2.0 | F1=0.9998 in-dist | Active, ~104K monthly downloads |
| CaMeL [4] | Capability-based architecture | Open source | 77% task completion, provable security | Research prototype |
| Progent [8] | Policy DSL for tool control | — | 41.2%→2.2% ASR | Research prototype |
| DataFilter [29] | Test-time content filter | — | 0.4% ASR | Research prototype |
| Vigil-LLM [19] | Canary tokens + scanning | — | Two detection modes | Maintained |

## Detailed Tool Profiles

### LLM Guard (Protect AI)

The most comprehensive open-source toolkit [27]:

**Input scanners (15):** Anonymize, BanCode, BanCompetitors, BanSubstrings, BanTopics, Code, Gibberish, InvisibleText, Language, PromptInjection, Regex, Secrets, Sentiment, TokenLimit, Toxicity

**Output scanners (21):** BanCode, BanCompetitors, BanSubstrings, BanTopics, Bias, Code, Deanonymize, JSON, Language, LanguageSame, MaliciousURLs, NoRefusal, ReadingTime, FactualConsistency, Gibberish, Regex, Relevance, Sensitive, Sentiment, Toxicity, URLReachability

The PromptInjection scanner uses the DeBERTa model [14]. Deployment options include pip install, API server, and direct integration [27].

### NeMo Guardrails (NVIDIA)

Programmable guardrails middleware [26]:

**Five rail types:**
1. Input rails — Process/reject/modify user messages
2. Dialog rails — Influence LLM prompting and conversation flow
3. Retrieval rails — Filter chunks in RAG scenarios
4. Execution rails — Monitor custom action I/O
5. Output rails — Validate/modify LLM responses

Uses **Colang**, a Python-like DSL for modeling dialogue flows and guardrail logic. Integrates with LangChain, OpenAI GPT models, LLaMa-2, Falcon, Vicuna, and third-party tools (ActiveFence, PolicyAI, AlignScore) [26].

**Critical finding:** Research shows NeMo Guard Jailbreak Detect has 65.22% bypass ASR when attacked with adversarial ML evasion techniques [22]. This significantly undermines confidence in deployment for security-critical applications.

### Rebuff (Protect AI)

Four-layer defense architecture [28]:
1. **Heuristics:** Pattern matching for known injection phrases
2. **LLM-based detection:** Uses an LLM to evaluate whether input contains injection
3. **VectorDB similarity:** Compares against database of known injections
4. **Canary tokens:** Detects prompt leakage and goal hijacking

Explicitly described as "still a prototype" that "cannot provide 100% protection" [28]. Self-hardening design stores detected attacks to improve future detection.

### Meta Prompt Guard (86M)

Built on mDeBERTa-v3-base with multilingual support (9 languages) [15]:

- **Unique feature:** Distinguishes INJECTION from JAILBREAK labels, enabling different filtering strategies for third-party content (both) vs. user dialogue (jailbreak only)
- **Lightweight:** 86M backbone parameters, no GPU required
- **Practical deployment:** 3-5% FPR without fine-tuning; Meta recommends fine-tuning on application-specific data for production [15]
- **Integration:** Pipeline API, custom scoring functions for jailbreak and indirect injection separately

### CaMeL (Google DeepMind)

Architectural defense rather than detection tool [4]:

- Converts user commands into restricted Python code
- Tracks variable provenance through "capabilities" tags
- Enforces security policies based on source trust when tools are called
- Open-source via Google Research repository
- 77% task completion on AgentDojo with provable security guarantees [4]

Willison calls it "the first credible prompt injection mitigation" because security comes from system design, not AI-based detection [12].

### Progent

Policy-based privilege control [8]:

- JSON Schema DSL for fine-grained tool call constraints
- Policies evaluate in priority order (forbid > allow at equal priority)
- Parameter-level inspection (not just tool-level blocking)
- Manual policies achieve 0% ASR on some benchmarks [8]
- Cannot defend against attacks within least-privilege bounds [8]

## Commercial Tools (Notable)

| Tool | Approach | Key Claim |
|------|----------|-----------|
| Lakera Guard | Multi-language detection | 100+ languages, acquired by Check Point [32] |
| Cloudflare AI Security | WAF-integrated scoring | 1-99 score with configurable thresholds [20] |
| Microsoft Prompt Shields | Classifier + Spotlighting | Integrated with Azure AI Content Safety [6] |
| Datadog AI Guard | Observability + protection | Chain tracing, RAG monitoring, PII scanning [24] |

## Framework Integration Patterns

### As Preprocessing Pipeline

```
Fetched content → Sanitizer/Filter → Classifier → LLM
```
Used by: LLM Guard [27], PromptArmor [9], DataFilter [29]

### As Middleware

```
User request → Guardrails engine → LLM → Guardrails engine → Response
```
Used by: NeMo Guardrails [26], Guardrails AI (wraps Rebuff)

### As Architectural Constraint

```
Privileged LLM ←(structured data only)→ Quarantined LLM ← External content
```
Used by: CaMeL [4], type-directed separation [7], OpenClaw [25]

## Gaps and Limitations

- **No tool provides deterministic guarantees** for agentic workflows processing untrusted content [30].
- **Detection tools face the adaptive attacker problem.** Open-source models can be studied to craft evasion attacks [15] [22].
- **Prototype maturity.** The most architecturally sound tools (CaMeL, Progent, DataFilter) are research prototypes, not production-ready libraries.
- **Benchmark fragmentation.** AgentDojo, Open Prompt Injection, TensorTrust, CyberSecEval are used inconsistently across tools, making direct comparison difficult.
- **Latency and cost data is sparse.** LLM Guard claims lower CPU inference cost vs GPU [27], Lakera claims sub-50ms [32], but systematic comparisons across tools are absent.
- **MCP-specific defenses are nascent.** The MCP security documentation [18] focuses on OAuth and SSRF, not prompt injection in tool outputs.
