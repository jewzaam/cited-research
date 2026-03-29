# Detection and Monitoring

Dimension covering tools and techniques for detecting prompt injection attempts in already-fetched content. Sources referenced via `[N]` — see [citations.md](../citations.md) for full entries.

## Overview

Detection operates after content has been fetched but before (or during/after) it is processed by the target LLM. Approaches range from lightweight heuristic pattern matching to fine-tuned classifier models to LLM-as-judge systems. The critical finding across the literature: **no single detection method is sufficient**, and reported accuracy numbers are often inflated relative to real-world performance [10] [22].

## Classifier-Based Detection

### ProtectAI DeBERTa Classifier

The most widely-adopted open-source prompt injection classifier [14]:

| Property | Value |
|----------|-------|
| Base model | microsoft/deberta-v3-base |
| Parameters | 0.2B |
| Classification | Binary (injection / no injection) |
| Max input | 512 tokens |
| F1 (in-distribution) | 0.9998 |
| Accuracy | 0.9999 |
| Training data | ~30% injections, ~70% normal prompts, 12 datasets |
| License | Apache 2.0 |
| Monthly downloads | ~104,000 |

**Critical caveat:** These metrics are in-distribution only. Performance on novel injection techniques, different text styles, or domain-specific prompts may degrade significantly [14]. The v2 model exists with potential improvements.

### Meta Prompt Guard (86M)

Meta's classifier uniquely distinguishes jailbreaks from injections [15]:

| Label | Threat Model | Example |
|-------|-------------|---------|
| JAILBREAK | User overriding safety | "Ignore previous instructions..." |
| INJECTION | Third-party embedded commands | Instructions hidden in fetched content |
| BENIGN | Normal content | Regular queries |

**Performance by evaluation context:**

| Context | TPR | FPR | AUC |
|---------|-----|-----|-----|
| In-distribution (jailbreak) | 99.9% | 0.4% | 0.997 |
| In-distribution (injection) | 99.5% | 0.8% | 1.000 |
| Out-of-distribution jailbreak | 97.5% | 3.9% | 0.975 |
| Multilingual jailbreak | 91.5% | 5.3% | 0.959 |
| CyberSecEval indirect injections | 71.4% | 1.0% | 0.966 |

The 71.4% TPR on CyberSecEval indirect injections is the most relevant number for agentic workflows fetching external content — significantly lower than the headline 99.9% [15].

### Guardrail Bypass Reality

Hackett et al. [22] systematically tested bypass techniques against production classifiers:

| Guardrail System | PI Bypass ASR | Jailbreak Bypass ASR |
|-----------------|---------------|---------------------|
| Vijil Prompt Injection | 87.95% | 91.67% |
| ProtectAI v1 | 77.32% | 51.39% |
| Azure Prompt Shield | 71.98% | 60.15% |
| Meta Prompt Guard | 70.44% | 73.08% |
| NeMo Guard Jailbreak | — | 72.54% |
| ProtectAI v2 | 20.26% | — |

**Most effective bypass techniques:**
- Emoji smuggling: **100% evasion** across both attack types [22]
- Unicode tag smuggling: 90.15% PI / 81.79% jailbreak [22]
- TextFooler (adversarial ML): 46.27% PI / 48.46% jailbreak [22]

Key insight: "disparities between what detectors flag versus what LLMs comprehend" enable attacks that bypass filters while remaining functional prompts [22].

## LLM-as-Judge Detection

### PromptArmor Preprocessing

PromptArmor [9] uses an LLM (GPT-4.1 or GPT-4o) as a preprocessing guardrail to detect and remove injections before the backend LLM processes data:

| Metric | GPT-4.1 | GPT-4o |
|--------|---------|--------|
| FPR | 0.56% | 0.07% |
| FNR | 0.13% | 0.23% |

Evaluated on AgentDojo with 629 adversarial scenarios across 4 agent types [9]. Near-0% ASR after deployment.

**Limitations:** Small models (0.6B parameters) show fundamental trade-offs between security and utility; effectiveness depends on careful prompt design [9].

## Score-Based Detection

### Cloudflare WAF Integration

Cloudflare provides score-based prompt injection detection integrated with their WAF [20]:

- **Score range:** 1-99 (lower = higher risk — counterintuitive)
- **Thresholds:** Strict (<50), Moderate (<30), Conservative (<20)
- **Actions:** Block, Managed Challenge, or Log
- **Combinable signals:** Bot scores, PII detection, endpoint targeting [20]

No published false positive/negative rates. Threshold tuning requires trial-and-observation [20].

## Canary Tokens

### Vigil Implementation

Vigil-LLM implements canary tokens with two detection modes [19]:

1. **Prompt leakage detection:** A 16-character hex token is prepended to prompts. If the token appears in the LLM's response, attackers manipulated the model to reveal instructions [19]
2. **Goal hijacking detection:** Token is added with instructions to include it in every response. If the token is absent, original instructions were bypassed [19]

Canary tokens are detection-only — they identify that an attack occurred but cannot prevent it.

### Multi-Layer Canary Usage

Rebuff [28] incorporates canary tokens as one of four defense layers (alongside heuristics, LLM detection, and VectorDB similarity). The tldrsec taxonomy [30] lists canary tokens as a distinct defense category.

## Observability and Monitoring

### Datadog LLM Observability

Datadog provides production monitoring capabilities [24]:

- **Request scanning:** Key phrases from known jailbreaks, encoded content, suspicious links
- **Semantic analysis:** LLM-based similarity checking against known jailbreak corpus
- **Chain tracing:** Full trace inspection to identify how "an innocuous user prompt may have mutated subsequent system prompts" [24]
- **RAG monitoring:** Detect "when unexpected information is generated from embeddings" [24]
- **Vector DB correlation:** Audit logs reveal how potentially poisoned data was written
- **PII scanning:** Default rules for email addresses, IPs via Sensitive Data Scanner
- **AI Guard:** Real-time protection with prompt protection, tool protection, anomaly detection [24]

### Output Behavioral Heuristics

OWASP and the broader literature identify output-side signals [5] [30]:
- Token entropy deviation from expected patterns
- Response length anomalies
- Semantic drift from query intent
- Role confusion detection (LLM claiming to be "system" or "admin")
- Instruction-following language inconsistent with query intent [21]

## Multi-Layer Defense Effectiveness

Ramakrishnan & Balaji [21] combined three detection/defense layers:

1. **Content filtering with embedding analysis:** Anomaly detection on retrieved passages comparing against benign/malicious reference sets
2. **Hierarchical system prompt guardrails:** Explicit boundaries, privilege separation, meta-directives alerting to adversarial content
3. **Multi-stage response verification:** Behavioral consistency checking + specialized classifier

**Results across 7 LLMs, 847 adversarial test cases:**
- ASR: 73.2% → 8.7% (88.1% mitigation) [21]
- Task performance: 94.3% retention [21]
- Latency overhead: ~2.1% [21]

## Gaps and Limitations

- **In-distribution vs. real-world gap is severe.** DeBERTa's F1=0.9998 is misleading for deployment decisions. CyberSecEval shows 71.4% TPR for indirect injections [15], and bypass research shows 65-88% evasion rates [22].
- **Adaptive attacks defeat static classifiers.** Emoji smuggling alone achieves 100% evasion [22]. Any published defense can be studied and targeted.
- **Detection ≠ prevention.** All detection approaches are probabilistic. Canary tokens detect after the fact. Classifiers have false negatives. No detection system provides deterministic guarantees.
- **Latency and cost.** LLM-as-judge (PromptArmor) adds API call overhead per request. Classifier models add inference latency. Production systems must balance detection thoroughness against response time.
- **Multilingual gap.** Performance degrades on non-English content — Meta Prompt Guard TPR drops ~6 percentage points on multilingual jailbreaks (97.5% → 91.5% vs. English OOD baseline) [15].
