# Content Sanitization and Filtering

Dimension covering techniques for stripping or neutralizing prompt injection payloads in fetched text before it reaches an LLM. Sources referenced via `[N]` — see [citations.md](../citations.md) for full entries.

## Overview

Content sanitization for LLM inputs is fundamentally harder than traditional input validation because attacks are expressed in natural language with no finite set of dangerous characters [5]. Unlike SQL injection where parameterized queries provide a deterministic boundary, LLM prompt injection payloads share the same medium (natural language) as legitimate content [23].

## Techniques

### Spotlighting

Spotlighting [2] is a family of three prompt engineering techniques developed by Microsoft that help LLMs distinguish system instructions from untrusted external content:

| Technique | How It Works | ASR Reduction | Task Impact |
|-----------|-------------|---------------|-------------|
| **Delimiting** | Special tokens mark boundaries around untrusted input (e.g., `<<` and `>>`) | ~50% reduction on GPT-3.5-Turbo (from ~60% to ~30%) | Minimal |
| **Datamarking** | Interleaves special character throughout text, replacing whitespace (e.g., "In^this^manner") | GPT-3.5-Turbo: 3.1% (summarization), 8.0% (Q&A); text-davinci-003: 0.0% | None on SQuAD, SuperGLUE, IMDB |
| **Encoding** | Transforms text using Base64 or similar algorithms | 0.0% or near-zero ASR | GPT-4: minimal; GPT-3.5-Turbo: "very detrimental" |

Datamarking is recommended as the practical baseline — ASR varies by task (3.1% on summarization, 8.0% on Q&A for GPT-3.5-Turbo). Encoding provides superior protection but requires high-capacity models (GPT-4+) [2]. Delimiting alone is discouraged — attackers who learn the system prompt can insert matching delimiters [2].

Microsoft has deployed Spotlighting in production as part of their defense-in-depth strategy [6].

### DataFilter

DataFilter [29] is a test-time, model-agnostic filter that strips injected instructions while preserving benign content. It achieved 0.4% average ASR across evaluated attacks. Key properties:
- Operates at inference time without model retraining
- Architecture-independent — works across different LLMs
- Identifies and removes directives that attempt to override original instructions [29]

### Input Pattern Matching

OWASP recommends pattern-based filtering as one layer of defense [5]:

**Regex patterns for common injection phrases:**
- `ignore\s+(all\s+)?previous\s+instructions?`
- `you\s+are\s+now\s+(in\s+)?developer\s+mode`
- `reveal\s+prompt` or `system\s+override`

**Additional input processing:**
- Fuzzy matching for typoglycemia variants (scrambled words like "ignroe" for "ignore")
- Character repetition normalization
- Length limitation (10,000 character cap recommended)
- Encoding attempt detection [5]

### Remote Content Sanitization

For external/fetched content specifically, OWASP recommends [5]:
- Strip injection patterns from external sources
- Filter code comments and documentation
- Sanitize markup in web content
- Validate and decode suspicious encodings

### Input Preprocessing Techniques

The tldrsec taxonomy [30] identifies two additional preprocessing approaches:

- **Paraphrasing**: Rephrase inputs to disrupt adversarial tokens while preserving legitimate instructions. Trade-off: can degrade model performance.
- **Retokenization**: Break tokens into smaller components (e.g., "studying" → "study"+"ing") to disrupt adversarial token combinations.

### Structured Output Formatting (JSON)

OpenClaw [25] demonstrated that forcing untrusted content through JSON-structured output (extracting sender, subject, body summary, action items) "strips the persuasive framing" of injection attempts. Applied alone, JSON formatting reduced ASR to 14.18% (from baseline). Combined with agent isolation, ASR dropped to 0% [25].

## Output Filtering

Output-side filtering catches deviations that input filtering misses [5]:

**Output validation patterns:**
- `SYSTEM\s*[:]\s*You\s+are` (prompt leakage detection)
- `API[_\s]KEY[:=]\s*\w+` (credential exposure)
- `instructions?[:]\s*\d+\.` (instruction enumeration)

Response length thresholds and suspicious pattern blocking provide additional signals [5].

## Classifier-Based Detection as Filtering

Dedicated classifier models can function as pre-processing filters. See [detection-monitoring.md](detection-monitoring.md) for detailed coverage of DeBERTa [14], Meta Prompt Guard [15], and other classifiers. The distinction from pure pattern matching: classifiers use learned representations rather than handcrafted rules, but face their own generalization limitations.

## Limitations

1. **Natural language is the attack surface.** Unlike SQL injection, there is no syntax/data boundary to enforce — attacks and legitimate content share the same medium [23].
2. **Adaptive attackers bypass patterns.** Obfuscation via Unicode hiding, Base64 encoding, HTML markup, emoji smuggling (100% evasion rate against tested guardrails), and bidirectional text all defeat pattern-based filtering [22].
3. **Sanitization degrades content.** Aggressive filtering can strip legitimate content, creating a security/utility trade-off. Paraphrasing and retokenization both risk degrading model performance [30].
4. **No finite blocklist is possible.** Unlike traditional injection where dangerous characters are enumerable, prompt injection payloads can be expressed in infinite natural language variations [5].
5. **Encoding-based defenses require capable models.** Encoding (Base64 spotlighting) provides strong protection but causes "very detrimental" task performance on smaller models [2].

## Gaps and Limitations

- **No published comparison of sanitization techniques against adaptive attacks.** Most ASR numbers come from fixed attack datasets, not adversarial optimization.
- **Multilingual sanitization** is underexplored. Pattern-matching approaches designed for English fail against injection in other languages.
- **Combined sanitization + detection pipelines** lack systematic evaluation of interaction effects between layers.
