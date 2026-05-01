# DeepSeek V4 — Self-Host Economics Reference

Scope: hardware footprint, throughput, KV-cache/FLOPs efficiency, framework support, quantization headroom, and break-even economics for self-hosting DeepSeek-V4-Pro and DeepSeek-V4-Flash. Each claim is tagged with the source file it derives from. Where the evidence is V3-era and only directionally applicable to V4, that is flagged inline.

---

## 1. Weight File Sizes and Native Precision

- **V4-Pro weights on Hugging Face: 865 GB** (simon-willison-deepseek-v4.md). The model card separately reports "862B parameters" as the on-disk size figure (hf-deepseek-v4-pro-modelcard.md). These are two different things — disk footprint in GB versus parameter count — and must not be conflated. The architectural parameter count is **1.6T total / 49B activated** (hf-deepseek-v4-pro-modelcard.md, hf-blog-deepseekv4.md, simon-willison-deepseek-v4.md).
- **V4-Flash weights on Hugging Face: 160 GB** (simon-willison-deepseek-v4.md). Model card lists "158B params" as the size figure (hf-deepseek-v4-flash-modelcard.md). Architectural count: **284B total / 13B activated** (hf-deepseek-v4-flash-modelcard.md, hf-blog-deepseekv4.md).
- **Native precision: FP4 + FP8 mixed**. MoE expert parameters in FP4, most other parameters in FP8 (hf-deepseek-v4-pro-modelcard.md, hf-deepseek-v4-flash-modelcard.md). Tensor types declared on the Pro card: BF16, I64, F32, F8_E8M0, F8_E4M3, I8 (hf-deepseek-v4-pro-modelcard.md). NVIDIA refers to the same format as **MXFP4** (nvidia-blackwell-v4.md).

Implication: V4 is the first DeepSeek release that ships with experts already at the minimum practical FP4 precision. There is no FP16/BF16 expert checkpoint to "downsize from."

## 2. Minimum Hardware (vLLM Day-0 Statement)

vLLM's V4 day-0 blog states the supported GPU configurations explicitly (vllm-blog-v4.md):

- **DeepSeek-V4-Pro: "runnable on 8xB200 or 8xB300"**
- **DeepSeek-V4-Flash: "runnable on 4xB200 or 4xB300"**

Targets: NVIDIA Hopper and Blackwell architectures (vllm-blog-v4.md).

Caveat — "8xH100 runs V4-Pro" is **not** a claim made by vLLM, NVIDIA, LMSYS/SGLang, or HuggingFace in any of the fetched sources. Treat that as a community claim, unverified here. The closest vendor-published Hopper datapoint is LMSYS's **V4-Flash on H200 with TP=4** (lmsys-blog-v4.md), not Pro on H100.

The wavespeed-vram.md article was reviewed but its numbers (671B / 37B active, 8xH100/A100 setups, 1.34 TB BF16 weights) are **V3.2 specs reused on a V4-titled URL** and explicitly should not be cited as V4 hardware data (wavespeed-vram.md self-flags this).

## 3. Concrete Throughput Numbers

Single-batch decode, 30K-token prefixes, 4K output sequence length (lmsys-blog-v4.md):

- **V4-Flash, H200, TP=4: 266 tok/s at 4K context, 240 tok/s at 900K context** — ~10% degradation across a 225× context-length scaling.
- **V4-Pro, B200, TP=8: 199 tok/s at 4K, 180 tok/s at 900K** — same ~10% degradation pattern.
- **V4-Pro, GB200 NVL72: ">150 tokens/sec/user"** at 1K/1K ISL/OSL with MXFP4 (nvidia-blackwell-v4.md).

The two Pro numbers (199 t/s on B200 TP=8 vs >150 t/s/user on GB200 NVL72) are not directly comparable: different test configs, different ISL/OSL, different precision treatment. They are consistent in the same order of magnitude.

## 4. KV Cache and FLOPs Efficiency

At 1M-token context (vllm-blog-v4.md, hf-blog-deepseekv4.md, hf-deepseek-v4-pro-modelcard.md, simon-willison-deepseek-v4.md):

- **V4-Pro KV cache: 9.62 GiB** vs V3.2's **83.9 GiB** — **8.7× reduction** per sequence (vllm-blog-v4.md). HF blog phrases it as "10% of V3.2's KV cache" for V4-Pro and "7% of V3.2's KV cache" for V4-Flash (hf-blog-deepseekv4.md).
- **V4-Pro inference FLOPs at 1M: 27% of V3.2** per single token (hf-deepseek-v4-pro-modelcard.md, hf-blog-deepseekv4.md).
- **V4-Flash inference FLOPs at 1M: 10% of V3.2** per single token (hf-blog-deepseekv4.md, simon-willison-deepseek-v4.md).

Note: the modelcard and the HF blog disagree on the V4-Pro KV-cache ratio (10% vs 8.7×/~11.5%). Both are within rounding distance of the same underlying figure (9.62 / 83.9 = 11.47%).

Architectural source of the savings: hybrid attention with three layer types — sliding-window, c4a (~1/4 compression), c128a (~1/128 compression) (vllm-blog-v4.md, hf-blog-deepseekv4.md). FP8 for most KV entries; BF16 only for RoPE dimensions (hf-blog-deepseekv4.md).

## 5. Inference Framework Support (Day-0)

- **vLLM**: yes, day-0 PR (vllm-blog-v4.md). Single + multinode recipes including prefill/decode disaggregation scaling to "100+ GPUs" per NVIDIA (nvidia-blackwell-v4.md).
- **SGLang**: yes, day-0. LMSYS describes V4 as having required novel systems work and ships three tuned NVIDIA recipes — low-latency, balanced, max-throughput (nvidia-blackwell-v4.md, lmsys-blog-v4.md).
- **NVIDIA NIM**: "Available to download on day-0 with NVIDIA NIM" for self-hosted deployment (nvidia-blackwell-v4.md).
- **Huawei Ascend**: via vllm-ascend plugin (vllm-blog-v4.md). Cambricon via vllm-mlu (vllm-blog-v4.md).
- **TensorRT-LLM**: **NOT confirmed** for V4 in NVIDIA's own day-0 blog (nvidia-blackwell-v4.md explicitly flags this as a gap). Do not assume support.
- **AMD ROCm**: **NOT confirmed**. LMSYS lists "AMD" among hardware targets at the architecture level (lmsys-blog-v4.md), but no specific ROCm framework readiness statement is in the fetched data.

## 6. Quantization Regression Risk

- V4 ships natively in **FP4 (experts) + FP8 (rest)** (hf-deepseek-v4-pro-modelcard.md, hf-deepseek-v4-flash-modelcard.md). Experts are already at the floor of practical precision used in vendor deployments.
- The V3-era reference (arxiv-quantization-2505.md, paper 2505.02390): **Q4 quantization maintains little performance degradation versus FP8** for DeepSeek-R1 and DeepSeek-V3. Sub-Q4 (Q3) shows significant regression unless using their dynamic DQ3_K_M variant.
- **V3-era data, not V4 data.** The paper explicitly studies R1 and V3 — V4 did not exist when it was published. The directional finding (Q4 ≈ FP8) does not transfer cleanly: V4 already begins at FP4 for the largest weight class, so any further compression of expert weights with GGUF Q3/Q2 would represent a steeper cliff than the V3-era Q4-from-FP8 step studied in the paper. **No fetched source quantitatively measures sub-FP4 quality loss on V4.**

## 7. Practical Viability for Individuals / Small Teams

- **V4-Pro**: 8×B200 or 8×B300 NVLink-class hardware (vllm-blog-v4.md). This is hyperscaler / well-funded-startup hardware. **Not practical for individuals.** Simon Willison observes that Pro "could require streaming active experts from disk" outside that envelope (simon-willison-deepseek-v4.md) — workable in principle but throughput-destroying.
- **V4-Flash**: 4×B200 or 4×B300 per vLLM (vllm-blog-v4.md), or single-host H200 TP=4 per LMSYS's actual benchmark (lmsys-blog-v4.md). This is reachable for well-funded small teams (single H200 server) but still well above prosumer hardware.
- Willison speculates "Flash model might run on 128GB hardware with quantization" (simon-willison-deepseek-v4.md). This is speculation, not a measured result. **No fetched source benchmarks V4-Flash on consumer multi-GPU rigs.** Any sub-160GB deployment would require GGUF quantization below the native FP4+FP8 mix, which puts it in the unmeasured-quality-cliff zone called out in §6.

## 8. Cost per Million Tokens — Self-Host vs API

API reference pricing (simon-willison-deepseek-v4.md):

- V4-Flash: **$0.14 input / $0.28 output** per 1M tokens
- V4-Pro: **$1.74 input / $3.48 output** per 1M tokens

Self-host cost calculation requires three inputs not present in this dataset:

1. GPU-hour rental rate for B200 / B300 / H200 instances (cloud or colo)
2. Actual sustained tokens/sec/dollar — which depends on batch size, ISL/OSL, and parallelism choice. The fetched throughput numbers (lmsys-blog-v4.md) are **single-batch decode**, which is a worst-case-for-cost scenario. Production batched throughput would be higher per dollar.
3. Utilization assumptions — break-even is sensitive to whether the rented hardware is saturated.

**Do not fabricate $/MTok self-host figures.** None of the fetched files provides the per-GPU-hour pricing or the production-batched throughput needed to compute it honestly. The qualitative direction is unambiguous: at $0.14/$0.28 per 1M tokens, V4-Flash API is cheap enough that self-hosting only pencils out for very high sustained volume, regulatory constraints (data residency, no third-party API), or research/development workloads where weight access matters more than economics.

A separately surfaced datapoint from the AA Intelligence Index — referenced indirectly via startupfortune-15x.md, which itself returned **HTTP 403 and could not be verified directly** — claims V4-Pro costs **~$1,071** to run the Intelligence Index benchmark suite versus V3.2's lower figure. This is reproduced here only as a flag for follow-up; do not cite startupfortune-15x.md as a primary source.

---

## Data Gaps and V3-vs-V4 Flags

- **wavespeed-vram.md**: V3.2-spec content under a V4 URL. Do not use for V4 hardware sizing.
- **arxiv-quantization-2505.md**: V3/R1 only. Directionally informative, not V4-measured.
- **startupfortune-15x.md**: HTTP 403, unverified.
- **TensorRT-LLM V4 support**: not confirmed in any fetched source.
- **AMD ROCm V4 support**: not confirmed at framework level (only listed as a hardware target by LMSYS).
- **Sub-FP4 quantization quality on V4**: not measured in any fetched source.
- **GPU-hour rental rates**: not in this dataset; required input for any $/MTok self-host calculation.
- **Production-batched throughput**: not in this dataset; LMSYS numbers are single-batch decode only.
