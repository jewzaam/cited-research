# Python Ecosystem

Covers Python libraries and frameworks for event routing: Kafka clients, stream processing, MQTT clients, and async patterns. Sources in [citations.md](../citations.md).

## Kafka Client Comparison

| Client | Performance | Async | Maintenance | Best For |
|--------|------------|-------|-------------|----------|
| **confluent-kafka-python** | High — C-backed via librdkafka [43] | v2.13.0b1 adds asyncio [54] | Active, enterprise-backed [52] | Production, high-load |
| **aiokafka** | 45K msgs/sec async [45] | Native asyncio [53] | Active, aio-libs community [53] | AsyncIO applications |
| **kafka-python** | Moderate | No native async | **Deprecated** [43] | Avoid for new projects |

confluent-kafka-python rated "high (near Java client)" performance [43]. aiokafka benchmarked at 45K msgs/sec async vs confluent-kafka's 22K sync [45] — but aiokafka has documented reliability issues: silent consumer stops, >100% latency increase from compression defaults, corrupted messages on big-endian architectures [counter agent].

**Recommendation:** confluent-kafka-python for production reliability; aiokafka for async-native workloads where its limitations are acceptable [43].

## Stream Processing

| Framework | Status | Focus | State |
|-----------|--------|-------|-------|
| **Quix Streams** | Active, commercially backed [47][48] | Kafka-only | RocksDB state, DataFrame API |
| **faust-streaming** | **Inactive** per Snyk [46] | Kafka-only | Tables, windowing |
| **Bytewax** | **Stalling** — last OSS v0.21.1 (Nov 2024), waxctl archived [49] | Multi-source | Stateful operators |

**Quix Streams** — leading Faust replacement [47]:
- Origins in McLaren F1 engineering, enterprise backing [47]
- Streaming DataFrame API (pandas-like), RocksDB state, tumbling/hopping windows [47]
- v3.15.0+ with `join_asof()` for industrial data enrichment [47]
- Pure Python — no JVM, no cross-language bridging [47]
- Kafka-focused, not multi-protocol [47]

**Faust tragedy:** Abandoned by Robinhood ~Oct 2020 after pervasive reliability failures — progressive consumer death, memory leaks (10MB/s growth), loss of 644/300K events even with exactly-once [46]. Kapernikov evaluation: "quickly encountered situations where Faust crashed and couldn't recover" [46]. Community fork (faust-streaming) classified "inactive" [46].

**Bytewax:** Python+Rust hybrid, claims 1.5–8x faster dev than Flink, 7–25x less memory, 100K+ msgs/sec single-worker [49][50]. But waxctl CLI archived March 2025, no new releases since November 2024 — project trajectory unclear [49].

## Multi-Protocol Framework: FastStream

FastStream is the standout for multi-protocol Python event routing [41][42]:
- Unified API across Kafka (AIOKafka & Confluent), RabbitMQ, NATS, Redis, MQTT [41]
- Pydantic validation, dependency injection, AsyncAPI auto-generation [41]
- In-memory testing utilities [41]
- Production/Stable status [41]
- MQTT support recently added [42]

**Unknown:** Performance ceiling of abstraction layer, overhead vs native clients [Python discovery agent].

## MQTT Clients

| Client | Type | Status | Notes |
|--------|------|--------|-------|
| **asyncio-mqtt / aiomqtt** | Async wrapper for paho-mqtt | Active, recommended [51] | Windows requires SelectorEventLoop |
| **paho-mqtt** | Sync (with asyncio examples) | Active, official Eclipse | Includes native asyncio examples |
| **HBMQTT** | Async native | **Deprecated** [51] | Fork aMQTT under development |

## Python Performance Limitations

### GIL-Induced Throughput Ceiling

Academic research on edge AI event pipelines [58]:
- Single-core: 40.2% throughput drop beyond optimal thread count (39,738 → 23,771 TPS)
- Quad-core: 35.1% drop (19,833 → 12,877 TPS)
- P99 latency explosion: 2–4.8x increase at high thread counts
- Python 3.13 free-threading: 4x multi-core improvement but 21.8% single-core degradation [57]

### Performance Gap vs Go

| Metric | Python (FastAPI) | Go (Gin/Fiber) | Gap |
|--------|------------------|----------------|-----|
| Requests/sec | 12,500–24,800 | 95,000–214,000 | 7.6–8.6x [55] |
| P99 latency | 18.3 ms | 2.8 ms | 6.5x [55] |
| Memory (idle) | 40–52 MB | 8–12 MB | 4–5x [55] |
| Docker image | 180–350 MB | 8–15 MB | 12–22x [55] |

Migration case study: e-commerce Django → Go = 2,500 → 38,000 req/s (15x), 120ms → 4ms P99 [56].

### Async Library Overhead

aio_pika is 6x slower than synchronous pika (2.23s vs 0.37s for 10K messages) due to per-message `await` overhead [counter agent]. The "function coloring" problem: any synchronous library call within async context blocks the entire event loop — a constraint Go's goroutine model avoids [counter agent].

### Contextual Boundaries

Below 1,000 req/s, Python vs Go gap is negligible [counter agent]. For I/O-bound workloads where bottleneck is external systems, Python's performance gap narrows significantly [counter agent]. confluent-kafka-python (C-backed) achieves "near Java client" performance — the gap is in pure Python implementations [43].

## Gaps and Limitations

- No head-to-head benchmark: FastStream vs native clients under load
- Quix Streams blog URL returned 404 — relied on search snippets and secondary sources [47]
- Python 3.13 free-threading data from dev.to, not peer-reviewed [57]
- Performance gap numbers are from web framework benchmarks, not message routing specifically [55][56]
- confluent-kafka-python asyncio support (v2.13.0b1) is beta — production readiness unclear [54]
