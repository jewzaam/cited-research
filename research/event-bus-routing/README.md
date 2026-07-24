# Event Bus Routing: Multi-Protocol, Self-Hosted, Python/Go

**Last revised:** 2026-07-24

## What This Answers

Which brokers, bridges, and libraries to use for multi-protocol event routing (MQTT ↔ Kafka and others) with content-based filtering in self-hosted / on-prem / disconnected environments, using Python (primary) and Go (secondary).

## Key Findings

| Layer | Recommendation | Why |
|-------|---------------|-----|
| **MQTT broker** | EMQX (scale) or Mosquitto (edge) | EMQX: 100M connections, SQL rule engine. Mosquitto: lightweight, <5K devices |
| **Event backbone** | Kafka (if replay needed) or NATS JetStream (if simplicity prioritized) | Kafka: de facto standard but 56% of clusters run at ≤1 MB/s. NATS: single binary, sub-ms latency |
| **Multi-protocol bridge** | Redpanda Connect | 225+ connectors, single 128 MiB binary, Apache 2.0, declarative YAML |
| **Python framework** | FastStream | Unified API across Kafka, RabbitMQ, NATS, Redis, MQTT with Pydantic validation |
| **Python Kafka client** | confluent-kafka-python | C-backed, near-Java performance; aiokafka for async-native only |
| **Python stream processing** | Quix Streams | Faust replacement, commercially backed, DataFrame API |
| **Go Kafka client** | franz-go | Pure Go, 2.5x faster producing vs Sarama, Kafka 0.8.0–4.2+ |
| **Go messaging framework** | Watermill | 12 pub/sub implementations, HTTP handler pattern |
| **Content filtering** | NATS subjects (native) or RabbitMQ 4.2 SQL (advanced) | Kafka lacks broker-side filtering (KAFKA-6020 open since 2017) |

## Quick Decision Framework

1. **Clients are devices?** → MQTT (EMQX for scale, Mosquitto for edge)
2. **Need event replay?** → Kafka (but only if >10K msgs/day)
3. **Service-to-service pub/sub?** → NATS JetStream
4. **Task queues with acks?** → RabbitMQ
5. **Bridge protocols?** → Redpanda Connect
6. **Python routing services?** → FastStream (multi-broker) or confluent-kafka-python (Kafka-only)
7. **Go routing services?** → franz-go (Kafka) or Watermill (multi-protocol)
8. **Throughput >10K msgs/sec?** → Consider Go over Python for the routing layer

## Critical Caveats

- **Python is 7–15x slower than Go** for event processing — viable below ~10K msgs/sec for I/O-bound work
- **Faust is dead** — abandoned by Robinhood 2020, community fork inactive. Use Quix Streams
- **Sarama (Go Kafka) is broken** — data loss, ordering failures. Use franz-go
- **Cross-protocol ordering is hard** — weakest guarantee wins when bridging
- **Disconnected operation** (store-and-forward) poorly documented across all solutions

## Files

- [analysis.md](analysis.md) — Full analysis with methodology and 81 citations
- [citations.md](citations.md) — All sources with URLs, tiers, and extraction notes
- [references/broker-landscape.md](references/broker-landscape.md) — Broker comparison data
- [references/multi-protocol-bridging.md](references/multi-protocol-bridging.md) — Bridging solutions
- [references/integration-frameworks.md](references/integration-frameworks.md) — Framework comparison
- [references/content-based-routing.md](references/content-based-routing.md) — Filtering approaches
- [references/python-ecosystem.md](references/python-ecosystem.md) — Python libraries and performance
- [references/go-ecosystem.md](references/go-ecosystem.md) — Go libraries and concurrency
- [audit/citation-audit.md](audit/citation-audit.md) — Independent citation verification
- [audit/consistency-review.md](audit/consistency-review.md) — Cross-file consistency check
