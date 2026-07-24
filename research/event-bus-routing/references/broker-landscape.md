# Broker Landscape (2025–2026)

Covers positioning, protocol strengths, self-hosted viability, and multi-protocol interop for the major message brokers. Sources in [citations.md](../citations.md).

## Broker Comparison

| Broker | Throughput | Latency | Persistence | Self-Hosted Viability | Multi-Protocol |
|--------|-----------|---------|-------------|----------------------|----------------|
| **Apache Kafka** | Hundreds MB/s per broker [1] | 5–10ms single publish [1] | Distributed commit log, replay [1] | Moderate — 6–7 node minimum, 300+ config knobs [3] | Kafka protocol only; Connect for sinks/sources |
| **NATS JetStream** | Tens of millions msgs/sec/node [1] | Sub-millisecond [1] | JetStream adds durable streams [1] | High — single binary, no external deps [1] | Native MQTT v3.1.1 [18] |
| **RabbitMQ** | ~40K msgs/sec (classic); Streams 1M+ [10] | Low (task queue optimized) | Quorum queues, streams [14] | High — mature tooling, Docker/K8s [14] | AMQP, MQTT, STOMP native |
| **EMQX** | 100M concurrent connections (23-node) [8] | MQTT-optimized | Retained messages, session persistence | High — Docker, K8s, bare-metal [8] | MQTT 5, MQTT-SN, MQTT over QUIC [8] |
| **Mosquitto** | ~1K connections before packet loss [8] | Low (lightweight) | File-backed, single-threaded [8] | High for edge — minimal resources | MQTT only |
| **Redis Streams** | 10K–100K msgs/day typical [1] | Sub-millisecond (in-memory) | Append-only log with consumer groups | High if Redis already deployed | Redis protocol only |
| **Apache Pulsar** | 1M–2.6M msgs/sec [discovery agent] | Variable | Tiered storage (BookKeeper + S3) | Low — 3 distributed systems required | Pulsar protocol; Kafka protocol adapter |

## Kafka: Dominant but Often Overkill

Kafka holds the de facto standard position [2] but 56% of all clusters run at ≤1 MB/s (~390 msgs/sec at 2.5 KB events) [3]. Self-managing 3-AZ Kafka costs ~$300K/yr; managed ~$50K/yr; equivalent S3 storage <$5K/yr [3]. Only ~9% of organizations have enterprise-wide streaming adoption [3].

Kafka 4.0 (March 2025) removed ZooKeeper completely — KRaft is now the only coordination mechanism [discovery agent]. The Kafka protocol has become a de facto standard, with Redpanda, WarpStream, Azure Event Hubs all building protocol compatibility [2].

**When Kafka is overkill:** <10K msgs/day, fire-and-forget notifications, request-reply patterns, simple batch processing, two-service architectures [5]. "Most teams don't technically outgrow Kafka. They outgrow the operational cost of running it" [3].

## NATS JetStream: Simplest Operations, Protocol Lock-In Risk

Single binary, Go, clustered with Raft, no external dependencies [1]. First-class request/reply — `nc.Request(subject, data, timeout)` provides RPC-like ergonomics [1]. Core NATS is pure fire-and-forget; JetStream (since v2.2) adds persistence [1].

**Limitations:** Proprietary protocol incompatible with Kafka/AMQP, creating high migration costs [6]. >100K consumers causes excessive Raft traffic [7]. >300 disjoint filters per consumer causes instability [7]. Go GC bottlenecks under extreme load [6]. Rarely mentioned in mainstream adoption discussions — niche verticals (finance, telecom, industrial) [6].

## RabbitMQ: Quiet Persistence

RabbitMQ 4.1 (February 2026) delivered quorum queue improvements [14]. RabbitMQ 4.2 introduced broker-side SQL filtering — a capability Kafka still lacks [29]. Native multi-protocol: AMQP, MQTT, STOMP [discovery agent].

Expert recommendation: "Start with RabbitMQ or even Redis Streams and migrate to Kafka only when concrete scaling requirements demand it" [counter agent, citing Jeff Delaney]. For most projects operating at <10K msgs/day, RabbitMQ's throughput ceiling is irrelevant [counter agent].

## MQTT Brokers: EMQX for Scale, Mosquitto for Edge

EMQX supports MQTT 5.0, MQTT-SN, MQTT over QUIC, and built-in SQL rule engine for real-time transformation [8]. Mosquitto is single-threaded, suitable for 1K–5K clients on modest hardware, no clustering [8]. HiveMQ supports 200M concurrent connections with enterprise features [8].

**MQTT scaling challenge:** Broker workload grows n² as devices increase — 2 clients = 4 transmissions, 100K devices = exponential load [counter agent]. Session state becomes nightmare with CleanSession=false at scale [counter agent].

## Pulsar: Near Zero Traction

Kai Waehner observes "zero traction in the market" for Pulsar [2]. StreamNative (primary vendor) has pivoted to Kafka protocol support [2]. Architecture requires three distributed systems (ZooKeeper/etcd + BookKeeper + Broker), making self-hosted deployment complex [discovery agent].

## Market Data

Global message broker market: $1.98B (2024) → $4.4B (2033) at 10% CAGR [11]. Cloud-based solutions hold 62% market share (2024), growing 2x rate of on-premises [11].

## Decision Flow

1. Clients are actual devices → MQTT [1]
2. Need replay of past events with partitioned ordering → Kafka [1]
3. Service-to-service pub/sub or request/reply without long replay → NATS [1]
4. Task queue with acknowledgments → RabbitMQ [counter agent]
5. Already running Redis, moderate scale → Redis Streams [counter agent]

Running multiple brokers is legitimate: "NATS for service mesh, Kafka for CDC/analytics/event logs, MQTT for field devices — with bridging at defined boundaries" [1].

## Gaps and Limitations

- Benchmark data varies across sources; no single standardized test covers all brokers
- Market share numbers are directional, not precise — sources vary by 2x on market size estimates
- Pulsar assessment may be unfairly negative given Waehner's Kafka-adjacent position [2]
- Redis Streams production case studies are sparse at enterprise scale
