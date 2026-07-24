# Event Bus Routing: Multi-Protocol, Self-Hosted, Python/Go

A citation-backed analysis of the current state of event bus routing with filtering for greenfield platforms using Python (primary) and Go (secondary), targeting self-hosted / on-prem / disconnected environments.

**Last revised:** 2026-07-24

## Methodology

Research conducted 2026-07-24 using 12 parallel discovery and counter-discovery agents across 6 dimensions, supplemented by multi-engine search (DuckDuckGo) and deep-read of 30+ key sources via WebFetch. Counter-perspectives actively sought for each dimension. All claims cite web sources visited in-session. Full source list in [citations.md](citations.md); per-dimension data in [references/](references/).

---

## 1. Problem Framing

The task: route messages between MQTT devices, Kafka streams, and potentially other protocols, with content-based filtering, in self-hosted environments that may be disconnected. Schema is controlled (transformation deprioritized). Cloud-managed solutions excluded.

This is a multi-axis problem:

1. **Which brokers** serve which roles?
2. **How to bridge** between them?
3. **Where does filtering happen** — broker-side or application-side?
4. **What frameworks/libraries** exist in Python and Go?

The Camel/Fuse mental model from Java — one framework handling everything — does not translate directly. Python and Go ecosystems favor composable libraries over monolithic frameworks, and some routing is better pushed to broker infrastructure than application code.

## 2. Broker Landscape

### Summary Table

| Broker | Sweet Spot | Throughput | Latency | Self-Hosted Ops |
|--------|-----------|-----------|---------|-----------------|
| Kafka | Event log, replay, analytics | Hundreds MB/s/broker [1] | 5–10ms [1] | Moderate–High (6–7 node min) [3] |
| NATS JetStream | Service-to-service, request/reply | Tens of millions msgs/sec/node [1] | Sub-ms [1] | Low (single binary) [1] |
| RabbitMQ | Task queues, complex routing | ~40K msgs/sec (classic); Streams 1M+ [10] | Low | Moderate (mature tooling) [14] |
| EMQX | IoT device management at scale | 100M connections (23-node) [8] | MQTT-optimized | Moderate [8] |
| Mosquitto | Edge/gateway, <5K devices | ~1K connections [8] | Low | Very Low [8] |
| Redis Streams | Lightweight, Redis already deployed | 10K–100K msgs/day | Sub-ms | Low (if Redis exists) |

### Key Findings

**Kafka is the de facto standard** [2] but overkill for most: 56% of clusters run at ≤1 MB/s [3]. Self-managing costs ~$300K/yr [3]. Avoid for <10K msgs/day, fire-and-forget, or request-reply patterns [5].

**NATS is operationally simplest** — single binary, no external dependencies, first-class request/reply [1]. But: proprietary protocol creates lock-in [6], >100K consumers causes excessive Raft traffic [7], >300 disjoint filters per consumer causes instability [7].

**RabbitMQ is underrated** — active development (4.1 in Feb 2026, 4.2 with SQL filtering) [14][29], native multi-protocol (AMQP, MQTT, STOMP), and most projects don't need Kafka's throughput [10].

**For MQTT at scale, EMQX over Mosquitto** — Mosquitto is single-threaded, ~1K connections [8]. EMQX handles 100M connections with SQL rule engine and native Kafka bridging [8][17].

**Running multiple brokers is legitimate:** "NATS for service mesh, Kafka for CDC/analytics/event logs, MQTT for field devices — with bridging at defined boundaries" [1].

## 3. Multi-Protocol Bridging

### Solution Comparison

| Solution | Protocols | License | Key Strength | Key Weakness |
|----------|-----------|---------|-------------|-------------|
| **Redpanda Connect** | 225+ connectors [15] | Apache 2.0 | Single binary, declarative YAML | No stateful processing [69] |
| **EMQX Enterprise** | MQTT ↔ Kafka [17] | Commercial | SQL rule engine, bidirectional | Not open source |
| **NATS native MQTT** | MQTT ↔ NATS [18] | Apache 2.0 | Zero additional components | NATS→MQTT always QoS 0 [18] |
| **Kafka Connect** | 700+ connectors | Apache 2.0 | Ecosystem breadth | Silent failures, JVM overhead [24][25] |

### Redpanda Connect: Best Universal Router

Redpanda Connect (formerly Benthos) is the strongest candidate for self-hosted multi-protocol routing [15][16]:
- 225 connectors (MQTT, Kafka, NATS, AMQP, HTTP, databases, object storage) [15]
- Single 128 MiB binary, starts in ~140ms [15]
- Bloblang mapping language for filtering and transformation [19]
- Apache 2.0 licensed [15]
- At-least-once delivery via in-process transactions [16]

**Limitations are real:** Bloblang is non-Turing-complete — no loops, recursion, or cross-message state [28][69]. No windowing, joins, or aggregations without external systems [69]. It's a "middle ground" between collectors and stream processors [69]. Configuration complexity emerges in production despite "simple YAML" marketing [counter agent].

### Cross-Protocol Ordering Is Hard

MQTT ordering applies within single client/topic/QoS [26]. Kafka guarantees per-partition. When bridging, the weakest guarantee wins — or worse, creates reordering violating both protocols' assumptions [counter agent]. Protocol bridging creates "domino effect" of complexity [27].

### NATS MQTT Bridging: Elegant but Limited

NATS translates MQTT topics to subjects automatically (/ → .) [18]. MQTT v3.1.1 supported since v2.2 with QoS 0/1/2 [18]. But **NATS-originated messages delivered to MQTT subscribers are always QoS 0** [18] and retained messages in clusters are "best-effort" [18]. No MQTT 5 support [18].

## 4. Content-Based Routing & Filtering

### Broker-Side vs Application-Side

| Approach | When to Use | Performance Impact |
|----------|-------------|-------------------|
| Broker-side (NATS subjects, RabbitMQ SQL) | High selectivity, known patterns | RabbitMQ: 12x improvement at 0.0001% selectivity [29] |
| Application-side (Kafka Streams, custom) | Complex business logic, dynamic rules | Full message stream consumed |
| Hybrid | Most production systems | Broker pre-filters, app refines |

**RabbitMQ 4.2 is the leader** in broker-side filtering: two-stage Bloom + SQL filtering achieves 4.87M msgs/sec (12x over SQL-only) [29]. Kafka still lacks broker-side filtering entirely (KAFKA-6020 open since 2017) [37].

**NATS subject hierarchies** provide the most natural content-based routing — design subject names to encode routing dimensions [30]. Filtered consumers provide independent views without message duplication [35].

**CloudEvents filtering spec** (approved June 2024) defines vendor-neutral filtering with six required dialects, but adoption is still early [31].

**Counter-perspective:** Content-based routers become "point of frequent maintenance" and risk becoming a "dumping ground" for miscellaneous logic [38]. When rules exceed simple predicates, application logic becomes necessary anyway [counter agent].

## 5. Python Libraries & Frameworks

### For Multi-Protocol Routing: FastStream

**FastStream** is the standout for Python multi-protocol event routing [41][42]:
- Unified API across Kafka (AIOKafka & Confluent), RabbitMQ, NATS, Redis, MQTT [41]
- Pydantic validation, dependency injection, AsyncAPI auto-generation [41]
- Production/Stable status on PyPI [41]
- Decorator-based pub/sub: `@broker.subscriber("topic")` / `@broker.publisher("topic")` [41]

**Unknown:** Abstraction layer performance overhead vs native clients. No published benchmarks [Python discovery agent].

### For Kafka Specifically

Use **confluent-kafka-python** for production — C-backed via librdkafka, "near Java client" performance [43][52]. Use **aiokafka** only if native asyncio integration is critical and you accept its reliability caveats (silent consumer stops, compression latency spikes) [counter agent]. confluent-kafka-python v2.13.0b1 adds asyncio interfaces [54].

**kafka-python is deprecated** — avoid for new projects [43].

### For Kafka Stream Processing

**Quix Streams** replaces Faust [47][48]:
- Pure Python, Streaming DataFrame API, RocksDB state [47]
- McLaren F1 engineering origins, commercial backing [47]
- v3.15.0+ with `join_asof()` [47]

**Faust is dead** — abandoned by Robinhood ~Oct 2020 after memory leaks (10MB/s), consumer death cascades, event loss [46]. Community fork classified "inactive" [46].

**Bytewax stalling** — last OSS release Nov 2024, waxctl CLI archived March 2025 [49].

### Python Performance Reality

Python is 7–15x slower than Go for event processing [55][56]. GIL creates throughput ceiling with P99 latency explosions at high thread counts [58]. But: below 1,000 req/s the gap is negligible, and for I/O-bound workloads where the bottleneck is external systems, Python's gap narrows significantly [counter agent]. C-backed clients (confluent-kafka-python) achieve near-Java performance [43].

**Practical threshold:** If routing throughput stays below ~10K msgs/sec and work is I/O-bound, Python is viable. Above that, consider Go for the routing layer specifically.

## 6. Go Libraries & Frameworks

### Kafka: franz-go

**franz-go** is the consensus leading Go Kafka client [59][60][61]:
- Pure Go, no CGO, feature-complete through Kafka 4.2+ [59]
- 2.5x faster producing, 1.5x faster consuming vs Sarama [62]
- Production adoption at Mux and WarpStream [71][62]

**Sarama explicitly avoided** — Alibaba Cloud recommends against it [68], WarpStream documents ordering failures and incorrect idempotent producer implementation [62], data loss in v1.27–1.30 [68].

### Messaging Framework: Watermill

**Watermill** (9.8K stars, MIT) for multi-protocol messaging [64][65]:
- 12 official transports (Kafka, AMQP, Redis, NATS, SQL, etc.) [64]
- HTTP handler–style router pattern [65]
- No built-in content-based routing — topic-based only [65]

**Limitations:** Deadlocks documented as common [79], GoChannel not persistent [79], no distributed dedup [79].

### For Most Routing: Go Channels Suffice

Go's concurrency primitives (channels, goroutines, `select`) handle fan-out, fan-in, pipeline, tee, and rate limiting without external dependencies [72]. "Share memory by communicating" — the Go philosophy naturally maps to event-driven patterns [72].

### Go Performance Caveats

GC pauses: 7–38ms measured at Pusher [70]. Goroutine panic cascades require defensive wrappers on every goroutine [counter agent]. For ultra-low-latency (<10ms guaranteed), Go's GC is a structural limitation — Rust cited as alternative [counter agent].

## 7. Decision Framework

### Step 1: Do You Need Multiple Brokers?

| If... | Then... |
|-------|---------|
| Devices send MQTT + backend needs event log | MQTT broker + Kafka, bridged |
| Services only talk to each other | NATS alone may suffice |
| Task queue + pub/sub | RabbitMQ handles both |
| Redis already deployed, moderate scale | Redis Streams |

### Step 2: How to Bridge?

| If... | Then... |
|-------|---------|
| Multi-protocol, self-hosted, open source | **Redpanda Connect** [15] |
| MQTT ↔ Kafka with SQL-level filtering rules | EMQX Enterprise (commercial) [17] |
| MQTT ↔ NATS, minimal components | NATS native MQTT [18] |
| Already invested in Kafka Connect ecosystem | Keep Kafka Connect (with operational investment) |

### Step 3: Where Does Filtering Happen?

| If... | Then... |
|-------|---------|
| Filtering is by message category/type | Encode in NATS subjects or MQTT topics |
| Complex SQL-like predicates | RabbitMQ 4.2 SQL filtering [29] |
| Kafka, dynamic routing needed | Kafka Streams + TopicNameExtractor [32] |
| Cross-protocol unified filtering | Redpanda Connect Bloblang [15] |

### Step 4: Which Language for the Routing Layer?

| If... | Then... |
|-------|---------|
| <10K msgs/sec, I/O-bound, team knows Python | Python + FastStream [41] |
| >10K msgs/sec, latency-sensitive | Go + franz-go [59] or Watermill [64] |
| Need standalone routing process | Redpanda Connect (Go binary, no code) [15] |
| Ultra-low-latency (<10ms guaranteed) | Consider Rust [counter agent] |

## 8. Recommended Architecture for the Stated Requirements

Given: greenfield, Python-primary, Go-secondary, multi-protocol (MQTT ↔ Kafka required), content-based filtering, self-hosted, disconnected-capable.

**Proposed stack:**

1. **MQTT broker:** EMQX (open-source edition) for device-facing MQTT 5 with built-in rule engine, or Mosquitto for edge/gateway nodes
2. **Event backbone:** Kafka (if replay/event sourcing needed) or NATS JetStream (if operational simplicity prioritized)
3. **Bridge layer:** Redpanda Connect — declarative YAML routing between MQTT, Kafka, NATS with Bloblang filtering [15]
4. **Application framework:** FastStream for Python services consuming/producing across multiple brokers [41]; franz-go for Go services needing Kafka throughput [59]
5. **Stream processing (if needed):** Quix Streams for Python Kafka processing [48]; Watermill for Go multi-protocol processing [64]

**What this stack doesn't solve:** Disconnected/air-gapped store-and-forward, complex stateful event processing (windowing, joins — needs Flink or custom code), guaranteed cross-protocol ordering.

## 9. Gaps and Limitations

1. **No head-to-head benchmarks** across bridging solutions (Redpanda Connect vs EMQX vs NATS) under identical conditions
2. **Disconnected operation** (store-and-forward when upstream brokers unreachable) poorly documented across all solutions
3. **FastStream abstraction overhead** unknown — no published benchmarks vs native clients
4. **CloudEvents filtering** still early adoption despite spec approval [31]
5. **Cross-protocol ordering** remains fundamentally hard with no clean solution [26][27]
6. **Python performance** data from web framework benchmarks, not message routing specifically [55][56]
7. **Redpanda Connect 50 Gbps claim** is vendor-stated, not independently verified [15]
8. **Some "2025/2026" blog sources** may contain SEO-driven content with lower reliability (Medium, dev.to articles) — cross-referenced where possible

**Two independent review agents will audit this document:** one checks every cited URL against source content, the other checks numerical and logical consistency.
