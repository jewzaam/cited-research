# Citations

All sources visited in-session via WebSearch or WebFetch. Numbered sequentially.

## Official Documentation

[1] Anthropic. "Pricing." platform.claude.com. Accessed 2026-05-07.
https://platform.claude.com/docs/en/about-claude/pricing
Data extracted: Claude model pricing (Haiku 4.5 $1/$5, Sonnet 4.6 $3/$15, Opus 4.7 $5/$25 per MTok), prompt caching multipliers (0.1x for reads), batch API 50% discount. Tier 2.

[2] Anthropic. "Model configuration." code.claude.com. Accessed 2026-05-07.
https://code.claude.com/docs/en/model-config
Data extracted: ANTHROPIC_DEFAULT_*_MODEL env vars, CLAUDE_CODE_SUBAGENT_MODEL, ANTHROPIC_CUSTOM_MODEL_OPTION, modelOverrides, model aliases (sonnet/opus/haiku), gateway requirements. Tier 2.

[3] Anthropic. "Create custom subagents." code.claude.com. Accessed 2026-05-07.
https://code.claude.com/docs/en/sub-agents
Data extracted: Subagent model resolution order (env var > per-invocation > frontmatter > parent), model field accepts aliases or full Anthropic model IDs, built-in subagent defaults. Tier 2.

[4] DeepSeek. "Models & Pricing." api-docs.deepseek.com. Accessed 2026-05-07.
https://api-docs.deepseek.com/quick_start/pricing
Data extracted: V4-Flash $0.14/$0.28/MTok, cache hit $0.0028/MTok, 1M context, 384K max output, tool call support. Tier 2.

[5] Google. "Gemini Developer API pricing." ai.google.dev. Accessed 2026-05-07.
https://ai.google.dev/gemini-api/docs/pricing
Data extracted: Gemini 2.5 Flash $0.30/$2.50/MTok, Flash-Lite $0.10/$0.40, batch 50% discount, context caching pricing. Tier 2.

[6] DeepSeek. "Rate Limit." api-docs.deepseek.com. Accessed 2026-05-07.
https://api-docs.deepseek.com/quick_start/rate_limit
Data extracted: Dynamic concurrency-based limiting, no fixed RPM/TPM, HTTP 429 on overload, 10-minute inference timeout. Tier 2.

[7] Google. "Rate limits." ai.google.dev. Accessed 2026-05-07.
https://ai.google.dev/gemini-api/docs/rate-limits
Data extracted: Free tier Flash 15 RPM/1,500 RPD, Flash-Lite 30 RPM/1,500 RPD, project-level quotas. Tier 2.

[8] OpenAI. "Pricing." developers.openai.com. Accessed 2026-05-07.
https://developers.openai.com/api/docs/pricing
Data extracted: GPT-4.1-mini no longer listed; current models are gpt-5.5/5.4 series. Tier 2.

[9] Anthropic. "OpenAI SDK compatibility." platform.claude.com. Accessed 2026-05-07.
https://platform.claude.com/docs/en/api/openai-sdk
Data extracted: Compatibility layer limitations (strict parameter ignored, no prompt caching, system message hoisting). Tier 2.

## GitHub Issues

[10] GitHub. "Support custom model aliases for subagent spawning via Task tool." anthropics/claude-code#34821. Accessed 2026-05-07.
https://github.com/anthropics/claude-code/issues/34821
Data extracted: Task/Agent tool model parameter restricted to sonnet/opus/haiku enum, closed as NOT PLANNED, no extension mechanism, workaround via claude-alias-patch. Tier 3.

[11] GitHub. "Subagent model routing is broken." anthropics/claude-code#43869.
https://github.com/anthropics/claude-code/issues/43869
Data extracted: All subagents resolve to parent model regardless of config (OPEN). Tier 3.

[12] GitHub. "BUG: Cowork Agent tool model parameter silently ignored." anthropics/claude-code#47488.
https://github.com/anthropics/claude-code/issues/47488
Data extracted: CLAUDE_CODE_SUBAGENT_MODEL hardcoded override in Cowork (OPEN). Tier 3.

[13] GitHub. "BUG: Claude Code intermittently ignores selected custom model." anthropics/claude-code#18025.
https://github.com/anthropics/claude-code/issues/18025
Data extracted: Custom models fall back to Anthropic model IDs during tool use (closed NOT PLANNED). Tier 3.

## Academic Papers

[14] Garg et al. "Correlated Errors in Large Language Models." arXiv:2506.07962, 2025.
https://arxiv.org/html/2506.07962
Data extracted: 349 models on HuggingFace, 71 on Helm; error agreement 60% (Helm) vs 33% random; 42.3% (HF) vs 12.7% random; more capable models have MORE correlated errors (p<0.001). Tier 1.

[15] Panickssery et al. "How Independent are Large Language Models? Behavioral Entanglement." arXiv:2604.07650, 2026.
https://arxiv.org/html/2604.07650
Data extracted: 18 models, 6 families (GPT, Claude, Qwen, Llama, Gemini, DeepSeek); Llama highest BEI (0.0446); de-entangled reweighting +4.5% over majority voting; judge bias Spearman 0.64-0.71. Tier 1.

[16] "Multi-Agent Code Verification via Information Theory." arXiv:2511.16708, 2025.
https://arxiv.org/html/2511.16708
Data extracted: Single agent 32.8% accuracy; best 2-agent pair 79.3%; 4 agents 72.4%; diminishing returns (+14.9, +13.5, +11.2 pp per agent); 99 hand-curated samples. Tier 1.

[17] "Cross-Model Disagreement as Correctness Signal." arXiv:2603.25450, 2026.
https://arxiv.org/abs/2603.25450
Data extracted: Cross-model perplexity achieves 0.75 AUROC vs 0.59 for within-model entropy. Tier 1. (From analysis agent, not directly fetched.)

[18] "Consensus is Not Verification." arXiv:2603.06612, 2026.
https://arxiv.org/html/2603.06612
Data extracted: At 25x inference cost, polling yields no consistent accuracy gains on truthfulness; models predict what other models say better than they identify truth. Tier 1. (From analysis agent, not directly fetched.)

[19] "How Accurately Do Large Language Models Understand Code?" arXiv:2504.04372, 2025.
https://arxiv.org/html/2504.04372v1
Data extracted: Semantic-preserving mutations cause 78% failure rate in fault localization. Tier 1. (From analysis agent.)

[20] "When Small Models Are Right for Wrong Reasons." arXiv:2601.00513, 2026.
https://arxiv.org/html/2601.00513v1
Data extracted: 50-69% of correct answers from small LMs contain flawed reasoning; standard accuracy metrics miss this. Tier 1. (From discovery agent.)

[21] "A Survey of Bugs in AI-Generated Code." arXiv:2512.05239, 2025.
https://arxiv.org/html/2512.05239v1
Data extracted: 60% of AI code faults are semantic errors (compile but produce wrong results). Tier 1. (From analysis agent.)

[22] "MoE-RBench: Towards Building Reliable Language Models." arXiv:2406.11353, 2024.
https://arxiv.org/html/2406.11353v1
Data extracted: MoE vs dense reliability comparison, task-dependent scaling. Tier 1. (From discovery agent.)

[23] "A Deep Dive Into LLM Code Generation Mistakes." arXiv:2411.01414, 2024.
https://arxiv.org/html/2411.01414v1
Data extracted: GPT-4 and Gemini make same 7 error categories; functional bugs consistent across LLMs. Tier 1. (From counter-discovery agent.)

[24] "Don't Always Pick the Highest-Performing Model." arXiv:2602.08003, 2026.
https://arxiv.org/html/2602.08003
Data extracted: Error correlation MEDMCQA rho=0.55, within-family rho=0.7-0.8, cross-family rho=0.4-0.5; diminishing ensemble returns at ~45% single-agent accuracy. Tier 1. (From counter-discovery agent.)

## Industry Sources

[25] TokenMix. "Structured Output and JSON Mode Guide 2026." tokenmix.ai. Accessed 2026-05-07.
https://tokenmix.ai/blog/structured-output-json-guide
Data extracted: Parse failure rates: OpenAI <0.1% (500K calls), Anthropic <0.2% (300K calls), Gemini <0.3%, DeepSeek 5-12%; token overhead per approach. Tier 3.

[26] Anthropic. "Detecting and preventing distillation attacks." anthropic.com, 2026-02.
https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks
Data extracted: 150,000+ exchanges through ~24,000 fraudulent accounts distilling Claude's capabilities. Tier 2. (From analysis agent.)

[27] CNBC. "Anthropic says Chinese AI firms used fraudulent accounts to distill Claude." 2026-02-24.
https://www.cnbc.com/2026/02/24/anthropic-openai-china-firms-distillation-deepseek.html
Data extracted: Corroboration of distillation campaign targeting reasoning capabilities. Tier 3. (From analysis agent.)

[28] HuggingFace. "Qwen2.5-72B identifies as Claude." Discussion thread.
https://huggingface.co/Qwen/Qwen2.5-72B-Instruct/discussions/2
Data extracted: Qwen 2.5-72B responds "I'm Claude, made by Anthropic" when asked about identity. Tier 4.

[29] Morpheus LLM. "Context Rot." morphllm.com. Accessed via discovery agent.
https://www.morphllm.com/context-rot
Data extracted: 18 frontier models tested, all show degradation with increased context; 30%+ mid-window accuracy drops. Tier 3. (Not directly fetched.)

[30] Datadog. "State of AI Engineering." datadoghq.com. Accessed via discovery agent.
https://www.datadoghq.com/state-of-ai-engineering/
Data extracted: Feb 2026 5% error rate (60% from rate limits); Mar 2026 2% (33% from rate limits); 8.4M total rate limit errors. Tier 2. (Not directly fetched.)

[31] Docker. "Local LLM Tool Calling: A Practical Evaluation." docker.com, 2024.
https://www.docker.com/blog/local-llm-tool-calling-a-practical-evaluation/
Data extracted: Claude 3 Haiku 0.933 F1 at 3.56s; GPT-4 0.974 F1 at ~5s; Qwen 3 14B 0.971 F1 at ~142s. Tier 3. (Not directly fetched.)

[32] InsiderLLM. "LLM Benchmarks Lie." insiderllm.com. Accessed via discovery agent.
https://insiderllm.com/blog/llm-benchmarks-lie-local-ai/
Data extracted: Model scoring 94% HumanEval solves only 23% of real engineering tasks. Tier 3. (Not directly fetched.)

[33] Artificial Analysis. "DeepSeek V4 Flash." artificialanalysis.ai. Accessed via discovery agent.
https://artificialanalysis.ai/models/deepseek-v4-flash
Data extracted: TTFT 1.06-1.14s, 74-150 t/s throughput across providers. Tier 3. (Not directly fetched.)

[34] OpenRouter. "Pricing." openrouter.ai. Accessed via discovery agent.
https://openrouter.ai/pricing
Data extracted: 5.5% fee on credit purchases, BYOK option. Tier 2. (Not directly fetched.)

[35] OpenRouter. "API Rate Limits." openrouter.ai. Accessed via discovery agent.
https://openrouter.ai/docs/api/reference/limits
Data extracted: Free tier 20 RPM/50 RPD; paid: $1 = 1 concurrent RPS, max 500. Tier 2. (Not directly fetched.)

[36] Together AI. "Rate limits." docs.together.ai. Accessed via discovery agent.
https://docs.together.ai/docs/rate-limits
Data extracted: Dynamic per-model rate limits, not fixed. Tier 2. (Not directly fetched.)

[37] Together AI. "Pricing." together.ai. Accessed via discovery agent.
https://www.together.ai/pricing
Data extracted: Serverless pricing, $25 free credit for new users. Tier 2. (Not directly fetched.)

[38] DeepInfra. "Pricing." deepinfra.com. Accessed via discovery agent.
https://deepinfra.com/pricing
Data extracted: 200 concurrent requests per model, auto-scaling. Tier 2. (Not directly fetched.)

[39] Alibaba Cloud. "Model Studio model pricing." alibabacloud.com. Accessed via discovery agent.
https://www.alibabacloud.com/help/en/model-studio/model-pricing
Data extracted: 1M input + 1M output tokens free (90 days, Singapore only), batch 50% discount. Tier 2. (Not directly fetched.)

[40] Mistral AI. "Codestral 25.01." mistral.ai. Accessed via discovery agent.
https://mistral.ai/news/codestral-2501
Data extracted: HumanEval 86.6%, FIM 95.3%, 22B params, 32K context (25.01 version). Tier 2. (Not directly fetched.)

[41] Mistral AI. "Codestral 25.08." mistral.ai. Accessed via discovery agent.
https://mistral.ai/news/codestral-25-08
Data extracted: 256K context, $0.30/$0.90 per MTok. Tier 2. (Not directly fetched.)

[42] Qwen. "Qwen3 Coder Next." qwen.ai. Accessed via discovery agent.
https://qwen.ai/blog?id=qwen3-coder-next
Data extracted: SWE-bench Verified 70.6%, SWE-bench Pro 44.3%, 262K context, 80B/3B MoE. Tier 2. (Not directly fetched.)

[43] HuggingFace. "DeepSeek-V4-Flash." Model card. Accessed via discovery agent.
https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash
Data extracted: 284B total/13B activated, V4 Pro SWE-bench 80.6%. Tier 2. (Not directly fetched.)

[44] OpenAI. "GPT-4.1." openai.com. Accessed via discovery agent.
https://openai.com/index/gpt-4-1/
Data extracted: 21% improvement on code correctness, 54.6% SWE-bench Verified. Tier 2. (Not directly fetched.)

[45] OpenRouter. "Outages February 17 and 19, 2026." openrouter.ai. Accessed via counter-discovery agent.
https://openrouter.ai/announcements/openrouter-outages-on-february-17-and-19-2026
Data extracted: 38-minute outages, 80-90% failure rates at peak, caching layer root cause. Tier 2. (Not directly fetched.)

[46] IsDown. "Together AI Status." isdown.app. Accessed via counter-discovery agent.
https://isdown.app/status/together-ai
Data extracted: 764 outages/incidents since March 2025, average resolution 66 minutes. Tier 3. (Not directly fetched.)

[47] Helicone. "LLM API Reliability Comparison." helicone.ai. Accessed via discovery agent.
https://www.helicone.ai/blog/the-complete-llm-model-comparison-guide
Data extracted: ~99.3% average LLM API uptime (5+ hours downtime/month), 7x worse than traditional cloud. Tier 3. (Not directly fetched.)

[48] IntoAI. "The Price Reversal Phenomenon." intoai.pub. Accessed via counter-discovery agent.
https://www.intoai.pub/p/price-reversal-phenomenon
Data extracted: 1 in 5 comparisons cheaper model costs more; Gemini 3 Flash $643 vs GPT-5.2 $527 despite 78% lower per-token price. Tier 3. (Not directly fetched.)

[49] Dstreefkerk. "Agentic Architecture Playbook 2026." GitHub Pages. Accessed via discovery agent.
https://dstreefkerk.github.io/2026-02-agentic-architecture-playbook-patterns-for-reliable-llm-workflows/
Data extracted: 99% per-step reliability compounds to 90.4% over 10 steps. Tier 3. (Not directly fetched.)

[50] OpenRouter. "Claude Code Integration." openrouter.ai. Accessed via multi-engine search.
https://openrouter.ai/docs/guides/coding-agents/claude-code-integration
Data extracted: CLAUDE_CODE_SUBAGENT_MODEL configuration for OpenRouter. Tier 2. (Not directly fetched.)

[51] ACM Computing Surveys. "Auditing Shared Training Data." dl.acm.org. Accessed via analysis agent.
https://dl.acm.org/doi/10.1145/3774897
Data extracted: GPT-4o showed ~0.89 standard deviations above mean memorization signals. Tier 1. (Not directly fetched.)

[52] Z.AI. "GLM-4.7." docs.z.ai. Accessed via discovery agent.
https://docs.z.ai/guides/llm/glm-4.7
Data extracted: 73.8% SWE-bench, 84.9% LiveCodeBench, 358B params, 203K context. Tier 2. (Not directly fetched.)

[53] Gemini API Free Tier Analysis. blog.laozhang.ai. Accessed via discovery agent.
https://blog.laozhang.ai/en/posts/gemini-api-free-tier
Data extracted: December 2025 50-80% rate limit reduction details. Tier 3. (Not directly fetched.)

[54] CodeRabbit. "State of AI vs Human Code Generation Report." coderabbit.ai. Accessed via analysis agent.
https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report
Data extracted: AI code 1.7x more issues than human, 75% more logic errors. Tier 3. (Not directly fetched.)

[55] IEEE Spectrum. "AI Coding Degrades." spectrum.ieee.org. Accessed via analysis agent.
https://spectrum.ieee.org/ai-coding-degrades
Data extracted: Silent failures in AI-generated code, production degradation patterns. Tier 2. (Not directly fetched.)
