# Citations

All sources used in the LLMeem / External Epistemic Memory research, numbered sequentially.

---

**[1]** Thomasson, Ben. "LLMeem — External Epistemic Memory." *llmeem.ai*, 2026.
<https://llmeem.ai/>
**Tier:** 3
Primary source for all EEM architecture details, benchmark claims, CLI documentation, and theoretical framing. Self-published project site by the author; no peer review.

**[2]** Thomasson, Ben. "ftl-reasons: Reason Maintenance System — automatic belief retraction and dependency-directed backtracking (Doyle 1979)." *GitHub*, 2024–2026.
<https://github.com/benthomasson/ftl-reasons>
**Tier:** 4
Open-source repository implementing the BMS. Python, SQLite-backed, 419 commits, 211 tests, 0 stars, 1 fork. PyPI version 0.47.0. License not specified on GitHub.

**[3]** Doyle, Jon. "A Truth Maintenance System." *Artificial Intelligence*, vol. 12, no. 3, pp. 231–272, 1979.
DOI: 10.1016/0004-3702(79)90008-0.
<https://www.sciencedirect.com/science/article/abs/pii/0004370279900080>
**Tier:** 1
Foundational TMS paper defining justification-based truth maintenance, SL justifications, IN/OUT propagation, non-monotonic reasoning. 1,976+ citations.

**[4]** de Kleer, Johan. "An Assumption-Based TMS." *Artificial Intelligence*, vol. 28, pp. 127–162, 1986.
DOI: 10.1016/0004-3702(86)90080-9.
<https://www.sciencedirect.com/science/article/abs/pii/0004370286900809>
**Tier:** 1
ATMS architecture using assumption sets rather than justifications. Enables multiple contexts and efficient context switching.

**[5]** Alchourrón, Carlos; Gärdenfors, Peter; Makinson, David. "On the Logic of Theory Change: Partial Meet Contraction and Revision Functions." *Journal of Symbolic Logic*, vol. 50, pp. 510–530, 1985.
<https://en.wikipedia.org/wiki/Belief_revision>
**Tier:** 1
AGM belief revision postulates: expansion, revision, contraction. Still forms core of belief revision theory. 4,000+ citations.

**[6]** McCarthy, John; Hayes, Patrick J. "Some Philosophical Problems from the Standpoint of Artificial Intelligence." *Machine Intelligence 4*, Edinburgh University Press, pp. 463–502, 1969.
<https://plato.stanford.edu/entries/frame-problem/>
**Tier:** 1
Introduced frame problem and situation calculus. Technical frame problem solved by end of 1980s; epistemological version remains open.

**[7]** Tulving, Endel. "Episodic and Semantic Memory." In *Organization of Memory*, pp. 381–403. Academic Press, 1972.
<https://psycnet.apa.org/record/1973-08477-007>
**Tier:** 1
Foundational distinction between episodic memory (temporally-dated events) and semantic memory (general knowledge/mental thesaurus). 9,000+ citations.

**[8]** Stanford Encyclopedia of Philosophy. "Logic of Belief Revision."
<https://plato.stanford.edu/entries/logic-belief-revision/>
**Tier:** 1
Comprehensive overview of AGM theory including formal postulates, recovery postulate controversy, iterated revision difficulties, Gärdenfors impossibility theorem.

**[9]** Snorkel AI. "The Self-Critique Paradox: Why AI Verification Fails Where It's Needed Most." *Snorkel AI Blog*, December 2025.
<https://snorkel.ai/blog/the-self-critique-paradox-why-ai-verification-fails-where-its-needed-most/>
**Tier:** 3
50 hard visual reasoning tasks, 2 frontier models, 5 iterations. Easy tasks: Claude Sonnet 4.5 dropped 98.1%→56.9%. Hard tasks: 0%→60%. "Critique is for debugging, not polishing."

**[10]** Yang, Zhe; Zhang, Yichang; Wang, Yudong; Xu, Ziyao; Lin, Junyang; Sui, Zhifang. "Confidence v.s. Critique: A Decomposition of Self-Correction Capability for LLMs." *arXiv:2412.19513*, December 2024.
<https://arxiv.org/abs/2412.19513>
**Tier:** 1
Decomposes self-correction into confidence (preserving correct answers) and critique (fixing wrong answers). Trade-off: improving one can decline the other.

**[11]** Anthropic. "Introducing the Model Context Protocol." *Anthropic News*, November 2024.
<https://www.anthropic.com/news/model-context-protocol>
**Tier:** 2
MCP as open standard for connecting AI to external data. Client-server architecture, USB-C analogy. Connectivity protocol, not knowledge representation.

**[12]** Model Context Protocol. "What is the Model Context Protocol (MCP)?" *modelcontextprotocol.io*, 2024–2026.
<https://modelcontextprotocol.io/>
**Tier:** 2
Official MCP specification. Tools, resources, prompts. Standardized protocol replacing N×M integrations.

**[13]** Flynt, Jeffrey. "Structured Belief State and the First Precision-Aware Benchmark for LLM Memory Retrieval." *arXiv:2605.11325v2*, May 2026.
<https://arxiv.org/html/2605.11325>
**Tier:** 2
PrecisionMemBench: 89 cases. Comparison systems (Mem0, Zep, Hindsight) achieve 0.05–0.08 mean retrieval precision. Tenure: 89/89 passes, precision 1.0, sub-15ms. "Memory is state management, not search."

**[14]** Miteski, Stefan. "Memory as Metabolism: A Design for Companion Knowledge Systems." *arXiv:2604.12034v1*, April 2026.
<https://arxiv.org/html/2604.12034v1>
**Tier:** 2
Companion memory framework with mirror/compensate principle. References TMS for minority-hypothesis retention. AGM entrenchment → memory gravity. Vision paper, no implementation.

**[15]** 1up.ai. "Why LLMs Fail at Confidence Scoring." *1up.ai Blog*, February 2026.
<https://1up.ai/blog/why-llms-suck-at-confidence-scoring/>
**Tier:** 3
No built-in calibration, overconfidence by design, no ground truth awareness, no training to admit uncertainty. Token-level confidence ≠ answer-level reliability.

**[16]** Thomasson, Ben. "eem-expert: Expert Knowledge Base for External Epistemic Memory." *GitHub*, 2026.
<https://github.com/benthomasson/eem-expert>
**Tier:** 4
MIT license. 49 beliefs (19 premises, 30 derived), 0 nogoods, max derivation depth 3. Built with ftl-reasons 0.40.0.

**[17]** Thomasson, Ben. "ftl-beliefs: CLI tool for tracking claims and contradictions across multi-agent LLM systems." *PyPI*, 2026.
<https://pypi.org/project/ftl-beliefs/>
**Tier:** 4
Version 0.2.0. MIT license. 54 downloads/month. Simpler tool using markdown files (beliefs.md, nogoods.md).

**[18]** Thomasson, Ben. "ftl-reasons." *PyPI*, 2026.
<https://pypi.org/project/ftl-reasons/>
**Tier:** 4
Version 0.47.0. 321 downloads/month. Dependencies include langchain-anthropic, sentence-transformers, mcp.

**[19]** "expert.ftl2.com — Public Belief Registry."
<https://expert.ftl2.com/public/eem-expert/beliefs>
**Tier:** 4
Live belief registry. ~45 visible beliefs, all IN status. HTML/Markdown/JSON export. Topic search. Demonstrates belief structure with OBSERVATION and DERIVED types.

**[20]** ResearchGate. Martins, João. "A beginner's guide to belief revision and truth maintenance systems." 1990.
<https://www.researchgate.net/publication/24293777_A_beginner's_guide_to_belief_revision_and_truth_maintenance_systems>
**Tier:** 2
Overview of JTMS architecture, belief revision vs TMS comparison. Doyle built first domain-independent JTMS.

**[21]** NASA Technical Reports. "A beginner's guide to belief revision and truth maintenance systems." NTRS 19930006101, 1993.
<https://ntrs.nasa.gov/citations/19930006101>
**Tier:** 1
NASA perspective on TMS applications and technical implementation.

**[22]** *Artificial Intelligence* (arXiv preprint). "Why LLMs Hallucinate on Structured Knowledge." *arXiv:2605.26362*, 2026.
<https://arxiv.org/html/2605.26362>
**Tier:** 2
Structural Shortcut Reliance (SSR) and Semantic Alignment Score (SAS) Drift. MetaQA-1hop: 5–22% hallucination. WikiTableQuestions: 80–88% hallucination.

**[23]** GPTKB authors. "GPTKB: Building Very Large Knowledge Bases from Language Models." *arXiv:2411.04920v1*, 2024.
<https://arxiv.org/html/2411.04920v1>
**Tier:** 2
105M triples from GPT-4o-mini: 22.5% true, 57.5% plausible, 19% false, 1% implausible. Person-class: 26% false rate.

**[24]** Springer. "Propositional Truth Maintenance Systems: Classification and Complexity." *Annals of Mathematics and Artificial Intelligence*, 1992.
<https://link.springer.com/article/10.1007/BF01530952>
**Tier:** 1
Clause Maintenance System computation is Σ₂ᵖ-complete. First AI problem proven at this complexity level.

**[25]** Huang, Jie et al. "Large Language Models Cannot Self-Correct Reasoning Yet." *ICLR 2024*, Google DeepMind.
<https://arxiv.org/pdf/2310.01798>
**Tier:** 1
GPT-4 on GSM8K: 95.5%→91.5%→89.0% through intrinsic self-correction rounds. Self-correction without external feedback degrades reasoning.

**[26]** Kuznetsova et al. "Expert Personas Improve LLM Alignment but Damage Accuracy." *arXiv:2603.18507v1*, March 2026.
<https://arxiv.org/html/2603.18507v1>
**Tier:** 2
MMLU: 71.6%→66.3% with expert persona. Llama-3.1-8B: 68.4%→46.3% (−22.1 points). Social Sciences: 77.3%→21.8%.

**[27]** *MDPI Information*. "LLM Judge Bias and Instability in Pairwise Evaluation." vol. 16, no. 8, 2025.
<https://www.mdpi.com/2078-2489/16/8/652>
**Tier:** 2
48.4% of verdicts reversed under mirrored response order (positional bias).

**[28]** Medium. "The Illusion of Confidence: Why Asking Your LLM 'Are You Sure?' Is a Terrible Idea." October 2025.
<https://medium.com/data-science-collective/the-illusion-of-confidence-why-asking-your-llm-are-you-sure-is-a-terrible-idea-84eb5859fc26>
**Tier:** 3
Models consistently overconfident, especially when incorrect. Mean confidence difference between correct and incorrect: 0.6–5.4%.

**[29]** SQ Magazine. "LLM Hallucination Statistics 2026." 2026.
<https://sqmagazine.co.uk/llm-hallucination-statistics/>
**Tier:** 3
Hallucination rates by domain: Legal 58–88%, Medical 43–64%, Code up to 99%. Best model (grok-4): 15%, worst: 52%.

**[30]** *arXiv*. "When Can We Trust LLM Graders? Calibrating Confidence." *arXiv:2603.29559*, 2026.
<https://arxiv.org/html/2603.29559>
**Tier:** 2
86% of predictions exceed 0.8 confidence. ECE averages 0.166 for self-reported confidence. SFT produces calibrated confidence; RL/DPO induces sharpening.

**[31]** *Nature Scientific Reports*. "Belief Rule Base Combinatorial Explosion." 2023.
<https://www.nature.com/articles/s41598-023-27498-3>
**Tier:** 1
Rules increase exponentially with attributes and reference levels in belief rule base systems.

**[32]** Kloia. "Knowledge Base vs Knowledge Graph for LLM Systems (2026 Guide)." April 2026.
<https://www.kloia.com/blog/knowledge-base-vs-knowledge-graph-llm>
**Tier:** 3
NeurIPS 2025 workshop: KG + agentic retrieval improved multi-hop QA over pure vector RAG and static GraphRAG.

**[33]** Phyvant. "RAG vs. Knowledge Graphs for Enterprise AI: What Actually Works." January 2026.
<https://phyvant.com/blog/rag-vs-knowledge-graphs-what-actually-works>
**Tier:** 3
Pure RAG fails on relationship-heavy queries. Pure KG misses document-level details. Combination handles what neither can alone.

**[34]** *Nature Scientific Reports*. "Vector RAG vs Graph RAG Performance." 2025.
<https://www.nature.com/articles/s41598-025-21222-z>
**Tier:** 1
Vector RAG: 0% on schema-bound queries. Graph RAG: 90%+. Query-type dependent performance.

**[35]** RAGFlow. "RAG Review 2025: From RAG to Context." 2025.
<https://ragflow.io/blog/rag-review-2025-from-rag-to-context>
**Tier:** 3
GraphRAG 13.4% lower accuracy than vanilla RAG on Natural Questions. Time-sensitive queries: 16.6% accuracy drop with GraphRAG.

**[36]** Mem0. "RAG vs AI Memory." 2026.
<https://mem0.ai/blog/rag-vs-ai-memory>
**Tier:** 3
Observational memory 84.23% vs RAG 80.05% on LongMemEval. 10x token cost reduction via prompt caching.

**[37]** *arXiv*. "Memori Architecture." *arXiv:2603.19935*, 2026.
<https://arxiv.org/html/2603.19935>
**Tier:** 2
81.95% accuracy with 1,294 tokens/query via semantic triples and conversation summaries.

**[38]** Jentic. "The MCP Tool Trap." 2026.
<https://jentic.com/blog/the-mcp-tool-trap>
**Tier:** 3
MCP is protocol not knowledge layer. Tool connectivity ≠ knowledge representation. Critique of using MCP as universal schema.

**[39]** *arXiv*. "A-MEM: Agentic Memory for LLM Agents." *arXiv:2502.12110v1*, 2025.
<https://arxiv.org/html/2502.12110v1>
**Tier:** 2
Zettelkasten-based dynamic memory. Multi-hop reasoning F1 capped at 45.85. Temporal reasoning best F1: 17.55.

**[40]** *arXiv*. "Large Language Models Hallucination: A Comprehensive Survey." *arXiv:2510.06265v2*, 2025.
<https://arxiv.org/html/2510.06265v2>
**Tier:** 2
Sycophantic behavior, capability misalignment, knowledge conflict, domain knowledge deficiency, outdated knowledge, long-tail knowledge as hallucination causes.

**[41]** *Towards Data Science*. "Your 1M Context Window LLM Is Less Powerful Than You Think." 2025.
<https://towardsdatascience.com/your-1m-context-window-llm-is-less-powerful-than-you-think/>
**Tier:** 3
Lost in the middle problem: 30%+ accuracy drops for mid-window positioned information.

**[42]** O'Reilly. "When Context Collapses: Teaching Agents to Detect and Recover from Lost Memory." 2026.
<https://www.oreilly.com/radar/when-context-collapses-teaching-agents-to-detect-and-recover-from-lost-memory/>
**Tier:** 3
Context compaction: 12,847→1,526 tokens (88% reduction). After 2–3 compactions, agents behave as if session just started.

**[43]** *arXiv*. "ZebraLogic: Scaling Limits of LLMs for Logical Reasoning." *arXiv:2502.01100v1*, 2025.
<https://arxiv.org/html/2502.01100v1>
**Tier:** 2
LLMs exhibit "curse of complexity" in non-monotonic reasoning. Persists even with larger models and increased inference-time computation.

**[44]** *arXiv*. "Are LLMs Classical or Nonmonotonic Reasoners?" *arXiv:2406.06590*, 2024.
<https://arxiv.org/abs/2406.06590>
**Tier:** 2
LLMs fail to maintain stable beliefs when adding supporting or unrelated information. Consistent reasoning remains elusive.

**[45]** Thomasson, Ben. *GitHub Profile: benthomasson*.
<https://github.com/benthomasson>
**Tier:** 4
Senior Principal Software Engineer at Red Hat. 847 repositories, 74 followers. Organizations: network-automation, ftl-ai. Ansible ecosystem contributor.

**[46]** Thomasson, Ben. *LinkedIn Profile*.
<https://www.linkedin.com/in/ben-thomasson/>
**Tier:** 4
715 followers, Raleigh NC. Multiple roles at Ansible by Red Hat over ~13 years. Recently left Red Hat.

**[47]** Thomasson, Ben. "ftl2: AI-first Python automation using the Ansible module ecosystem." *GitHub*, 2025–2026.
<https://github.com/benthomasson/ftl2>
**Tier:** 4
Apache-2.0 license. 2–21x faster than ansible-playbook. Uses "reason" fields in policy enforcement. 0 stars.

**[48]** GoodData. "From RAG to GraphRAG: Knowledge Graphs, Ontologies and Smarter AI." October 2025.
<https://www.gooddata.ai/blog/from-rag-to-graphrag-knowledge-graphs-ontologies-and-smarter-ai/>
**Tier:** 3
GraphRAG combines unstructured text with structured knowledge graph for more informed answers.

**[49]** *arXiv*. "BeliefMem: Agent Memory Under Partial Observability." *arXiv:2605.05583v1*, May 2026.
<https://arxiv.org/html/2605.05583v1>
**Tier:** 2
Noisy-OR belief aggregation. Maintains probability of candidate conclusions. POMDP framework for agent belief state.

**[50]** *PMC*. "Interdependence of episodic and semantic memory." *Neuropsychologia*, 2010.
<https://pmc.ncbi.nlm.nih.gov/articles/PMC2952732/>
**Tier:** 1
Tulving's interdependence argument: episodic and semantic memory interact for normal function.

**[51]** *JMIR Medical Informatics*. "Benchmarking LLM Confidence in Clinical Question Answering." 2025.
<https://medinform.jmir.org/2025/1/e66917>
**Tier:** 1
Inverse correlation: worse-performing models show higher confidence (r=−0.40, P=.001). GPT-4o: 74% accuracy/63% confidence. Qwen2-7B: 46% accuracy/76% confidence.

**[52]** *arXiv*. "Neuro-Symbolic AI Limitations." *arXiv:2502.11269v1*, 2025.
<https://arxiv.org/html/2502.11269v1>
**Tier:** 2
No consensus architecture. Scalability problems. Neural components may relearn mechanistic parts yielding redundant models.

**[53]** Wikipedia. "Model Context Protocol." 2025.
<https://en.wikipedia.org/wiki/Model_Context_Protocol>
**Tier:** 3
MCP as open-source standard for connecting AI applications to external systems.

**[54]** Salfati Group. "Graph RAG: 85% enterprises adopting hybrid RAG by 2026." 2025.
<https://salfati.group/topics/graph-rag>
**Tier:** 3
Neither RAG nor KG consistently outperforms the other. Hybrid becoming standard.
