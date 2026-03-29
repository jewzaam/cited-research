# Citations

All sources visited in-session via WebSearch and/or WebFetch. Each entry records the specific data extracted.

**[1]** Beurer-Kellner, Luca; Buesser, Beat; Creţu, Ana-Maria; Debenedetti, Edoardo; Dobos, Daniel; Fabian, Daniel; Fischer, Marc; Froelicher, David; Grosse, Kathrin; Naeff, Daniel; Ozoani, Ezinwanne; Paverd, Andrew; Tramèr, Florian; Volhejn, Václav. "Design Patterns for Securing LLM Agents against Prompt Injections." arXiv:2506.08837v1, 2025.
<https://arxiv.org/html/2506.08837v1>
Data extracted: Six architectural design patterns (Action-Selector, Plan-Then-Execute, LLM Map-Reduce, Dual LLM, Code-Then-Execute, Context-Minimization), security properties and capability constraints of each, threat model framework.

**[2]** Hines, Keegan; Lopez, Gary; Hall, Matthew; Zarfati, Federico; Zunger, Yonatan; Kıcıman, Emre. "Spotlighting: Defending Against Indirect Prompt Injection Attacks for Large Language Models." Microsoft, arXiv:2403.14720v1, 2024.
<https://arxiv.org/html/2403.14720v1>
Data extracted: Three spotlighting techniques (delimiting, datamarking, encoding), ASR reduction metrics per technique and per model (GPT-3.5-Turbo, GPT-4, text-davinci-003), task performance impact on SQuAD/SuperGLUE/IMDB.

**[3]** Wallace, Eric; Xiao, Kai; Leike, Reimar; Weng, Lilian; Heidecke, Johannes; Beutel, Alex. "The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions." OpenAI, arXiv:2404.13208v1, 2024.
<https://arxiv.org/html/2404.13208v1>
Data extracted: Four-tier trust ordering (System > User > Image/Audio > Tool), SFT+RLHF training methodology, 63% improvement on system prompt extraction, 30%+ generalization to unseen attacks (jailbreaks), over-refusal limitations.

**[4]** Debenedetti, Edoardo; Shumailov, Ilia; Fan, Tianqi; Hayes, Jamie; Carlini, Nicholas; Fabian, Daniel; Kern, Christoph; Shi, Chongyang; Terzis, Andreas; Tramèr, Florian. "CaMeL: Defeating Prompt Injections by Design." Google DeepMind, arXiv:2503.18813, 2025.
<https://arxiv.org/abs/2503.18813>
Data extracted: Capability-based security architecture with data flow tracking, 77% task completion with provable security on AgentDojo (vs. 84% undefended), open-source implementation.

**[5]** "LLM Prompt Injection Prevention Cheat Sheet." OWASP, 2025.
<https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html>
Data extracted: Complete defense catalog (input validation, structured prompts, output monitoring, human-in-the-loop, Best-of-N mitigation, remote content sanitization, agent-specific defenses, least privilege), regex patterns for detection, layered pipeline architecture, attack type taxonomy.

**[6]** "How Microsoft Defends Against Indirect Prompt Injection Attacks." Microsoft MSRC Blog, July 2025.
<https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks>
Data extracted: Three-layer defense (prevention via Spotlighting, detection via Prompt Shields, impact mitigation via data governance/human-in-the-loop), 800+ participant Adaptive Prompt Injection Challenge producing 370,000+ prompt dataset.

**[7]** Jacob, Dennis; Alghamdi, Emad; Hu, Zhanhao; Alomair, Basel; Wagner, David. "Better Privilege Separation for Agents by Restricting Data Types." UC Berkeley, arXiv:2509.25926v1, 2025.
<https://arxiv.org/html/2509.25926v1>
Data extracted: Type-directed privilege separation using integers/floats/booleans/enums only, Q-Agent/P-Agent decomposition, 0% ASR across 3 case studies (shopping 31.7%→0%, calendar 63%→0%, bug fixing 94.3%→0%), utility trade-off (14.6% vs 49.7% in bug fixing).

**[8]** Shi, Tianneng; He, Jingxuan; Wang, Zhun; Wu, Linyu; Li, Hongwei; Guo, Wenbo; Song, Dawn. "Progent: Programmable Privilege Control for LLM Agents." UC Berkeley/UC Santa Barbara, arXiv:2504.11703v1, 2025.
<https://arxiv.org/html/2504.11703v1>
Data extracted: JSON Schema-based DSL for privilege policies, 41.2%→2.2% ASR reduction on AgentDojo, 70.3%→7.3% on ASB, zero ASR on EHRAgent poisoning attacks with manual policies, limitations (cannot defend within least-privilege bounds).

**[9]** PromptArmor team. "Simple yet Effective Prompt Injection Defenses." arXiv:2507.15219v1, 2025.
<https://arxiv.org/html/2507.15219v1>
Data extracted: Modular preprocessing guardrail, FPR 0.56% and FNR 0.13% with GPT-4.1 on AgentDojo (629 adversarial scenarios), near-0% ASR after deployment. Limitations: small models show fundamental security/utility trade-offs.

**[10]** Jia, Yuqi; Shao, Zedian; Liu, Yupei; Jia, Jinyuan; Song, Dawn; Gong, Neil Zhenqiang. "A Critical Evaluation of Defenses against Prompt Injection Attacks." arXiv:2505.18333, 2025.
<https://arxiv.org/abs/2505.18333>
Data extracted: Principled evaluation framework (effectiveness + utility), finding that "existing defenses are not as successful as previously reported" when tested against adaptive attacks. Code available at PIEval.

**[11]** Willison, Simon. "Prompt injection design patterns." simonwillison.net, June 13, 2025.
<https://simonwillison.net/2025/Jun/13/prompt-injection-design-patterns/>
Data extracted: Expert commentary on the 6 design patterns paper, practical significance assessment, security skepticism about format constraints, connection to CaMeL and Dual LLM origin.

**[12]** Willison, Simon. "CaMeL offers a promising new direction for mitigating prompt injection attacks." simonwillison.net, April 11, 2025.
<https://simonwillison.net/2025/Apr/11/camel/>
Data extracted: Assessment of CaMeL as "first credible prompt injection mitigation," data flow vulnerability analysis, user policy burden concerns, comparison to Dual LLM pattern.

**[13]** "Prompt Injection Defenses for Browser Use." Anthropic Research, 2025.
<https://www.anthropic.com/research/prompt-injection-defenses>
Data extracted: Three defense layers (RL-based training, content classifiers, human red teaming), 1% ASR with Claude Opus 4.5 on adaptive Best-of-N attacks, explicit acknowledgment that "no browser agent is immune."

**[14]** ProtectAI. "deberta-v3-base-prompt-injection." Hugging Face, 2024.
<https://huggingface.co/protectai/deberta-v3-base-prompt-injection>
Data extracted: DeBERTa-v3-base fine-tuned classifier, F1=0.9998, accuracy=0.9999, 0.2B parameters, 512 token limit, Apache 2.0 license, training on ~30% injections + ~70% normal prompts across 12 datasets. Caveat: in-distribution metrics only.

**[15]** Meta. "Prompt-Guard-86M." Hugging Face, 2024.
<https://huggingface.co/meta-llama/Prompt-Guard-86M>
Data extracted: mDeBERTa-based 3-class classifier (BENIGN/INJECTION/JAILBREAK), 86M parameters, multilingual (9 languages), TPR 99.9% jailbreak / 99.5% injection in-distribution, 71.4% TPR on CyberSecEval indirect injections, 3-5% FPR without fine-tuning.

**[16]** "Enforcing Outbound HTTP Allowlists for AI Agents." LoginRadius Engineering Blog, 2025.
<https://www.loginradius.com/blog/engineering/enforce-outbound-http-allowlists-ai-agents>
Data extracted: Deny-by-default framework, identity-bound enforcement, multi-layer architecture (infrastructure + gateway), scoped authentication with short-lived tokens, delegation-aware governance, zero-trust outbound model.

**[17]** "Codex Cloud: Internet Access." OpenAI Developer Documentation, 2025.
<https://developers.openai.com/codex/cloud/internet-access>
Data extracted: Binary on/off internet access model, three allowlist strategies (none, common dependencies ~60 domains, unrestricted), HTTP method restriction (GET/HEAD/OPTIONS only for non-allowlisted), explicit prompt injection risk warning with example.

**[18]** "Security Best Practices." Model Context Protocol Documentation, 2025.
<https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices>
Data extracted: SSRF prevention (block private IPs, validate redirects, use egress proxies like Smokescreen), confused deputy problem with OAuth, session hijacking mitigations, scope minimization, local MCP server compromise vectors.

**[19]** Vigil-LLM. "Canary Tokens Documentation." GitHub, 2024.
<https://github.com/deadbits/vigil-llm/blob/main/docs/canarytokens.md>
Data extracted: Two detection modes (prompt leakage: canary appears in output; goal hijacking: canary absent from output), 16-character hex token generation, API-based add/check workflow.

**[20]** "AI Security for Apps: Prompt Injection." Cloudflare Developer Documentation, 2025.
<https://developers.cloudflare.com/waf/detections/ai-security-for-apps/prompt-injection/>
Data extracted: Score-based detection (1-99, lower = higher risk), three threshold tiers (strict <50, moderate <30, conservative <20), WAF integration via custom rules, combinable with bot scores and PII detection.

**[21]** Ramakrishnan, Badrinath; Balaji, Akshaya. "Securing AI Agents Against Prompt Injection Attacks: A Comprehensive Benchmark and Defense Framework." arXiv:2511.15759v1, 2025.
<https://arxiv.org/html/2511.15759v1>
Data extracted: Three-layer defense (embedding analysis, hierarchical prompts, multi-stage response verification), 73.2%→8.7% ASR (88.1% mitigation), 94.3% task retention, 2.1% latency overhead, tested across 7 LLMs (GPT-4, Claude 2.1, PaLM 2, Llama 2 70B, Mistral 7B, Vicuna 13B, GPT-3.5-turbo), 847 adversarial test cases.

**[22]** Hackett, William; Birch, Lewis; Trawicki, Stefan; Suri, Neeraj; Garraghan, Peter. "Bypassing Prompt Injection Detection in LLM Guardrails." Mindgard/Lancaster University, arXiv:2504.11168v1, 2025.
<https://arxiv.org/html/2504.11168v1>
Data extracted: Bypass ASRs — Vijil 87.95%/91.67%, ProtectAI v1 77.32%/51.39%, Azure Prompt Shield 71.98%/60.15%, Meta Prompt Guard 70.44%/73.08%, NeMo Guard 72.54%, ProtectAI v2 20.26%. Emoji smuggling achieved 100% evasion. 12 character injection + 8 adversarial ML techniques tested.

**[23]** "Securing LLM Systems Against Prompt Injection." NVIDIA AI Red Team Blog, 2023.
<https://developer.nvidia.com/blog/securing-llm-systems-against-prompt-injection/>
Data extracted: Treat all LLM output as potentially malicious, parameterize external service calls, apply least-privilege across all prompt contributors, acknowledgment that injection "cannot be effectively mitigated" at LLM level.

**[24]** "Monitor LLM Prompt Injection Attacks." Datadog Blog, 2024.
<https://www.datadoghq.com/blog/monitor-llm-prompt-injection-attacks/>
Data extracted: Prompt/output scanning for key phrases and encodings, semantic similarity checking against known jailbreaks, chain tracing for mutation detection, RAG-specific monitoring, vector DB audit log correlation, PII detection via Sensitive Data Scanner.

**[25]** Cheng, Darren; Tsao, Wen-Kwang. "Agent Privilege Separation in OpenClaw." TrendAI Lab, arXiv:2603.13424, 2026.
<https://arxiv.org/html/2603.13424>
Data extracted: 0% ASR with full pipeline (agent isolation + JSON formatting) on 649-attack benchmark, 0.31% with isolation alone (323× improvement), tool partitioning (reader vs. actor agents), JSON structured output strips persuasive framing (ASR 14.18% alone).

**[26]** "NeMo Guardrails." NVIDIA, GitHub, 2024.
<https://github.com/NVIDIA/NeMo-Guardrails>
Data extracted: 5 rail types (input/dialog/retrieval/execution/output), Colang DSL, Apache 2.0 license, integrations with LangChain and third-party tools (ActiveFence, PolicyAI, AlignScore).

**[27]** ProtectAI. "LLM Guard." GitHub, 2024.
<https://github.com/protectai/llm-guard>
Data extracted: 15 input scanners + 21 output scanners, MIT license, includes PromptInjection scanner using DeBERTa model, pip-installable with API server option.

**[28]** ProtectAI. "Rebuff: Prompt Injection Detector Framework." GitHub, 2023.
<https://github.com/protectai/rebuff>
Data extracted: 4-layer defense (heuristics, LLM-based detection, VectorDB similarity, canary tokens), self-hardening design, explicitly described as "still a prototype."

**[29]** Wang, Yizhu; Chen, Sizhe; Alkhudair, Raghad; Alomair, Basel; Wagner, David. "DataFilter: Defending Against Prompt Injection." 2024.
<https://arxiv.org/pdf/2510.19207>
Data extracted: Test-time model-agnostic filter achieving 0.4% average ASR, strips injected instructions while preserving benign content, advancement beyond PromptArmor.

**[30]** McCarthy, Rami. "Prompt Injection Defenses." tldrsec, GitHub, 2024-2025.
<https://github.com/tldrsec/prompt-injection-defenses>
Data extracted: Complete defense taxonomy (blast radius reduction, input preprocessing, guardrails/overseers, taint tracking, secure threads/dual LLM, ensemble decisions, prompt engineering, robustness/fine-tuning, preflight testing), tool comparison, critical gap assessment.

**[31]** "OWASP AI Agent Security Cheat Sheet." OWASP, 2025.
<https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html>
Data extracted: Per-tool permission scoping, trust level separation, minimum tool sets, agent-specific threat model. (From discovery agent search snippets; full page not fetched.)

**[32]** "Prompt Defense." Lakera Guard Documentation, 2025.
<https://docs.lakera.ai/docs/prompt-defense>
Data extracted: Detection of prompt injections and jailbreaks, 100+ language support. Note: no quantified accuracy or latency metrics available in current documentation.

**[33]** "NVIDIA Blog: Securing Agentic AI — How Semantic Prompt Injections Bypass AI Guardrails." NVIDIA, 2025.
<https://developer.nvidia.com/blog/securing-agentic-ai-how-semantic-prompt-injections-bypass-ai-guardrails/>
Data extracted: Semantic injection techniques bypassing guardrails in agentic AI. (From discovery agent; full page not fetched separately.)

**[34]** "OpenAI Codex Instruction Hierarchy Challenge Dataset." OpenAI, March 2026.
<https://openai.com/index/instruction-hierarchy-challenge/>
Data extracted: IH-Challenge dataset for RL training, 15% benchmark improvement, Python-based grading, public on HuggingFace. (From discovery agent; 403 on direct fetch.)
**Access:** Could not fetch directly (403); data from search snippets and related sources [3].
