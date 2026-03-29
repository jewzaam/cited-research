# Architectural Defenses

Dimension covering dual-LLM patterns, privilege separation, read-only agent boundaries, and input/output tagging. Sources referenced via `[N]` — see [citations.md](../citations.md) for full entries.

## Overview

Architectural defenses constrain what a compromised LLM can do, rather than trying to detect or filter injection payloads. The consensus across NVIDIA [23], OWASP [5] [31], and the academic literature [1] [4] [7] [8] is that **general-purpose agents cannot provide reliable safety guarantees** — effective security requires application-specific agents with constrained capabilities.

## The Six Design Patterns

Beurer-Kellner et al. [1] formalized six architectural patterns for securing LLM agents. The paper represents a consortium effort across IBM, Invariant Labs, ETH Zurich, Google, Microsoft, and others.

### 1. Action-Selector Pattern
- **Mechanism:** LLM translates natural language into one of several predefined tool calls — an "LLM-modulated switch statement" [1]
- **Security:** Prevents feedback from tool outputs back into agent decision-making. Agent is "immune to prompt injections" because untrusted data never influences response generation [1]
- **Constraint:** Agent can only select from hardcoded actions with template placeholders

### 2. Plan-Then-Execute Pattern
- **Mechanism:** Agent formulates a fixed action plan before execution. Tool outputs flow back but cannot influence which actions are taken [1]
- **Security:** Provides "control flow integrity protection" — injections in tool outputs cannot cause action deviation [1]
- **Constraint:** No dynamic action selection based on runtime data. As Willison notes [11]: "the `calendar.read()` output might corrupt the email body but won't change the recipient"

### 3. LLM Map-Reduce Pattern
- **Mechanism:** Isolated sub-agents independently process individual pieces of third-party data. Malicious input affects only its corresponding LLM instance [1]
- **Security:** Enforces "stricter isolation between agent workflow and tool outputs" [1]
- **Constraint:** Map agents have no tool access; reduce operations avoid LLMs or use constrained outputs (booleans, regex-validated results)

### 4. Dual LLM Pattern
- **Mechanism:** Privileged LLM with tools + quarantined LLM without tools. Outputs handled symbolically via orchestrator [1]
- **Security:** Quarantined LLM cannot "dereference values" — only the orchestrator can during function calls [1]
- **Origin:** Proposed by Simon Willison in April 2023 [12], formalized in this paper and influenced CaMeL [4]

### 5. Code-Then-Execute Pattern
- **Mechanism:** Agent writes formal code calling tools and spawning unprivileged LLMs. Generalizes plan-then-execute through explicit program generation [1]
- **Security:** Structured code separates untrusted data processing from control flow
- **Constraint:** Agent outputs must be executable code; untrusted data flows through designated LLM calls

### 6. Context-Minimization Pattern
- **Mechanism:** Removes unnecessary content from context over multiple interactions — user prompts are dropped after initial action selection [1]
- **Security:** Blocks user prompt injections from affecting later processing. Only guards against user input, not third-party data [1]

### Key Finding
No single pattern suffices. The authors recommend "combining multiple design patterns" tailored to specific threat models [1]. Simon Willison emphasizes this remains "the biggest challenge to responsibly deploying the kind of agentic systems everyone is so excited to build" [11].

## CaMeL (Google DeepMind)

CaMeL [4] is described by Willison as "the first credible prompt injection mitigation" [12] because it achieves security through **system design rather than AI-based detection.**

| Property | Detail |
|----------|--------|
| Architecture | Dual-LLM with custom Python interpreter for data flow tracking |
| Security model | Capability-based — enforces policies when tools are called |
| Key innovation | Extracts control and data flows from trusted queries; untrusted data cannot impact program flow [4] |
| AgentDojo results | 77% task completion with provable security (vs. 84% undefended) [4] |
| Open source | Yes, via Google Research repository |

**Limitations identified by Willison [12]:**
- Users must codify and maintain security policies independently
- Continuous approval prompts risk "user fatigue" and decision-making failures
- Data flow vulnerability: extracting data from untrusted sources (e.g., "Bob's email" from compromised meeting notes) creates tainted variables
- Traditional defenses that rely on model training fail ~1% of the time — "a failing grade" in application security [12]

## Instruction Hierarchy (OpenAI)

OpenAI trained GPT-3.5 Turbo to enforce a four-tier privilege ordering [3]:

| Priority | Level | Source |
|----------|-------|--------|
| 0 (Critical) | System Message | Application developers |
| 10 (High) | User Messages | End users |
| 20 (Medium) | Images/Audio | Multimodal inputs |
| 30 (Low) | Tool text | Web browsing, search, APIs |

**Training approach:** SFT + RLHF with two principles [3]:
- **Context Synthesis** (aligned instructions): Decompose composite requests across hierarchy levels
- **Context Ignorance** (misaligned instructions): Train models to respond "as if they never saw the lower-level instructions"

**Results:**
- System prompt extraction defense: +63% improvement [3]
- Jailbreak generalization: +30% despite zero jailbreak training data [3]
- Over-refusal: Some benign queries triggered refusals on two evaluations [3]

**Key limitation:** Treats all tool outputs as categorically misaligned, preventing legitimate instruction-following in third-party content [3].

## Type-Directed Privilege Separation

Jacob et al. [7] restrict data flow between agents to **integers, floats, booleans, and pre-approved enums only** — eliminating freeform text as a carrier for injected commands.

| Case Study | Model | Undefended ASR | Defended ASR | Utility Impact |
|------------|-------|---------------|-------------|----------------|
| Online Shopping | GPT-4o | 31.7% | 0% | 22.4% vs 21.8% (neutral) |
| Calendar Scheduler | GPT-4o | 63.0% | 0% | 91.0% vs 90.0% (neutral) |
| Bug Fixing | Claude Sonnet 4 | 94.3% | 0% | 14.6% vs 49.7% (−35 pts) |

The 35-point utility drop in bug fixing exemplifies the fundamental tension: tasks requiring natural language context suffer significantly when text is removed [7].

## Progent (Programmable Privilege Control)

Progent [8] introduces a JSON Schema-based DSL for fine-grained privilege policies over tool calls:

- **Mechanism:** Policies specify effect (allow/forbid), tool identifier, parameter conditions, fallback actions, and priority
- **Key property:** Constrains parameters, not just tools — e.g., a transfer tool can be restricted to specific recipients [8]
- **Results:** AgentDojo 41.2%→2.2% ASR; ASB 70.3%→7.3%; EHRAgent 0% with manual policies [8]
- **Limitation:** Cannot defend against preference manipulation within least-privilege bounds or text-only attacks [8]

## OpenClaw Agent Isolation

Cheng & Tsao [25] split agent operations between a reader agent (store_summary tool only) and an actor agent (send_email, get_pending_summary, store_result — never sees raw content):

- Full pipeline (isolation + JSON formatting): **0% ASR** on 649-attack benchmark [25]
- Isolation alone: **0.31% ASR** (323× improvement over baseline) [25]
- JSON formatting alone: 14.18% ASR [25]

## Microsoft Defense-in-Depth

Microsoft deploys a three-layer architecture in production [6]:

1. **Prevention:** Hardened system prompts + Spotlighting [2] with randomized delimiters
2. **Detection:** Prompt Shields — probabilistic classifier trained on known injection techniques across multiple languages, continuously updated [6]
3. **Impact Mitigation:** Data governance via sensitivity labels (Microsoft Purview), deterministic blocking of exfiltration techniques (markdown image injection), human-in-the-loop for sensitive operations [6]

Emerging research areas: TaskTracker (analyzes internal LLM states rather than textual inputs/outputs) and FIDES (information-flow control for deterministic injection prevention) [6].

## Anthropic Browser Agent Defenses

Anthropic employs three defense layers for browser-based agents [13]:

1. **RL-based training:** Claude encounters injections in simulated web content during training, receives rewards for correct identification and refusal
2. **Content classifiers:** Scan untrusted content entering context window for adversarial commands (hidden text, manipulated images, deceptive UI)
3. **Human red teaming:** Continuous probing by security researchers

Result: **1% ASR with Claude Opus 4.5** on adaptive Best-of-N attacks (100 attempts per environment) [13]. Explicitly states: "No browser agent is immune to prompt injection" [13].

## Gaps and Limitations

- **Utility-security trade-off is not well characterized.** CaMeL loses 7 percentage points, type-directed separation loses 35 points on complex tasks. No systematic framework exists for predicting utility cost.
- **Composition effects unknown.** How do multiple patterns interact when layered? The design patterns paper [1] recommends combining patterns but does not evaluate combinations.
- **User policy burden.** CaMeL and Progent both require users to write security policies — difficult even for security professionals [12].
- **No pattern addresses text-to-text attacks.** When the agent's job is to produce text from text (summarization, translation), there is no structural boundary to enforce [4] [12].
