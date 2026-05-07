# Failure Mode Diversity

Does using a different model family to verify Claude's output provide meaningful diversity of failure modes?

## Summary

Cross-model verification provides measurable but limited benefit. Error correlation between model pairs is significantly above random (60% vs 33% on Helm) [14], and more capable models show MORE correlated errors [14]. However, cross-family entanglement is lower than within-family [15], and cross-model disagreement detects confident errors better than self-evaluation (0.75 vs 0.59 AUROC) [17]. The two cheapest candidates (DeepSeek, Qwen) have documented Claude training contamination [26][28], undermining their diversity value.

## Quantitative Evidence

### Error Correlation

| Metric | Value | Source |
|---|---|---|
| Error agreement (Helm, both wrong) | 60% vs 33% random baseline | [14] |
| Error agreement (HuggingFace, both wrong) | 42.3% vs 12.7% random baseline | [14] |
| Within-family error correlation (rho) | 0.7-0.8 | [24] |
| Cross-family error correlation (rho) | 0.4-0.5 | [24] |
| Cross-model AUROC for error detection | 0.75 vs 0.59 self-evaluation | [17] |
| Polling at 25x cost vs single sample | No consistent accuracy gain | [18] |

349 models on HuggingFace and 71 on Helm were analyzed [14]. Nearly all model pairs (100% HF, 97.5% Helm) exceed random agreement expectations [14]. The regression analysis found that "pairs of models that are more accurate individually also have more correlated errors" — this held controlling for shared developers, architectures, and model sizes (p<0.001) [14].

### Multi-Agent Verification

| Configuration | Accuracy | Improvement |
|---|---|---|
| Single agent | 32.8% | Baseline |
| Best 2-agent pair (Correctness + Performance) | 79.3% | +46.5pp |
| Full 4-agent system | 72.4% | +39.6pp |

The best 2-agent pair outperformed the full 4-agent system [16]. Adding Security and Style agents added noise for general bug detection [16]. Diminishing returns: +14.9, +13.5, +11.2 percentage points per additional agent [16].

De-entangled reweighting (weighting verifiers by statistical independence) achieves up to 4.5% accuracy gain over majority voting [15].

### Behavioral Entanglement

18 models across 6 families studied (GPT, Claude, Qwen, Llama, Gemini, DeepSeek) [15]:
- Llama variants most entangled (BEI=0.0446, p<0.01)
- Cross-family entanglement exists but is lower than within-family
- Judge bias correlates with entanglement: Spearman 0.64 (GPT-4o-mini) and 0.71 (Llama3-based judges) between dependency and over-endorsement [15]

## Model Family Independence from Claude

### Gemini — Highest Independence

Google-trained with independent research infrastructure. Natively multimodal architecture differs fundamentally from Claude's text-centric Constitutional AI approach. Not implicated in distilling Claude — Google disclosed in February 2026 that attackers attempted to clone *Gemini*, positioning Google as victim [26]. Shared training data floor (Common Crawl, Wikipedia, GitHub) creates irreducible baseline correlation [51].

### GPT — Moderate Independence

OpenAI has independent research. GPT-4o showed strongest memorization signals in contamination studies (~0.89 standard deviations above mean) [51]. Shares heavy reliance on common web corpora with Claude.

### GLM-4.7 — High Independence

Zhipu AI (Chinese lab), dense Transformer architecture, independent training pipeline. Not implicated in Claude distillation. Open weights (MIT license).

### DeepSeek — Compromised Independence

Anthropic documented industrial-scale distillation: 150,000+ Claude exchanges through ~24,000 fraudulent accounts [26][27]. Campaign targeted reasoning capabilities, rubric-based grading, and censorship-safe response generation [26]. MoE architecture differs structurally, but training data contamination directly imports Claude's error patterns.

### Qwen — Compromised Independence

Qwen 2.5-72B identifies itself as "Claude, made by Anthropic" when asked about identity [28]. Community has created intentional distillations of Claude reasoning into Qwen models.

### Codestral/Mistral — High Independence

Mistral (French lab), independent architecture and training. Not implicated in Claude distillation.

## What Cross-Model Verification IS Good For

1. **Detecting confident errors** — the most dangerous failure mode. Cross-model perplexity achieves 0.75 AUROC compared to 0.59 for within-model entropy [17]. This is a 27% relative improvement and requires only a single forward pass from the verifier.

2. **Triage signal** — flagging outputs for human review without requiring ground truth labels.

3. **Mechanical/structural checks** — verification tasks that are more pattern-matching than reasoning (schema validation, file existence, format compliance) are less affected by correlated errors than reasoning-heavy tasks [20].

## What Cross-Model Verification Does NOT Provide

1. **Independent validation** — errors are correlated above random at 42-60% depending on benchmark [14]. Using a second model provides partial, not independent, error detection.

2. **Correction through consensus** — at 25x inference cost, polling yields no consistent accuracy gains on truthfulness benchmarks [18]. Models predict what other models will say better than they identify truth.

3. **Scale benefits** — marginal gains from additional models decrease: +14.9, +13.5, +11.2 pp per agent [16]. A carefully selected 2-agent pair outperforms a 4-agent system [16].

4. **Cheap diversity** — the cheapest alternatives (DeepSeek at $0.14/MTok, Qwen at $0.11/MTok) have documented Claude contamination [26][28]. The most independent option (Gemini at $0.30/MTok) costs 2-3x more.

## Gaps and Limitations

- No benchmark specifically measures cross-model verification effectiveness on code claim checking
- Error correlation data is from MCQ benchmarks, not code comprehension tasks specifically
- Within-Claude-family entanglement has not been directly measured (extrapolated from Llama family data)
- The 60% error agreement rate includes models of varying capability — the rate for frontier-only pairs may differ
- MoE vs dense architecture impact on code verification diversity is task-dependent and not well-characterized [22]
