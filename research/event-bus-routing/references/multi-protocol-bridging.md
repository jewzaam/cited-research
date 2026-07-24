# Multi-Protocol Bridging

Covers solutions for routing between MQTT, Kafka, NATS, and other protocols in self-hosted environments. Sources in [citations.md](../citations.md).

## Solution Landscape

| Solution | Protocols | Direction | License | Approach |
|----------|-----------|-----------|---------|----------|
| **Redpanda Connect** | 225+ connectors (MQTT, Kafka, NATS, AMQP, HTTP, DBs) | Bidirectional | Apache 2.0 (99%+) | Declarative YAML pipelines |
| **EMQX Enterprise** | MQTT ↔ Kafka, Pulsar, others | Bidirectional | Commercial | Built-in rule engine |
| **NATS Server** | MQTT ↔ NATS | Bidirectional (QoS 0 for NATS→MQTT) | Apache 2.0 | Native protocol translation |
| **Kafka Connect** | 700+ connectors | Source/Sink | Apache 2.0 | JVM-based connector framework |
| **Strimzi MQTT Bridge** | MQTT → Kafka only | Unidirectional | Apache 2.0 | Lightweight bridge |
| **Custom code** | Any | Any | N/A | Application-level bridging |

## Redpanda Connect (formerly Benthos)

Strongest candidate for universal multi-protocol routing [15][16][19]:

- **225 connectors** spanning MQTT, Kafka, NATS, AMQP 0.9/1.0, HTTP, WebSocket, databases, object storage [15]
- **Single 128 MiB binary**, starts in ~140ms, scales from IoT devices (100 millicores) to 50 Gbps [15]
- **Bloblang** mapping language for transformations — simpler than Kafka Connect SMTs but non-Turing-complete (no loops, recursion, cross-message state) [28][69]
- **YAML-based declarative pipelines**: input → pipeline → output [19]
- **At-least-once delivery** via in-process transaction model [16]
- Apache 2.0 licensed (99%+ of connectors) [15]

**Limitations:** No stateful processing (windowing, joins, aggregations) — positioned as "middle ground" between collectors (Vector/FluentD) and stream processors (Flink) [69]. Ecosystem fragmentation post-Redpanda acquisition (repository split, Bento fork) [28]. Configuration complexity emerges in production despite "simple YAML" marketing [counter agent].

## EMQX Kafka Integration

Production-grade MQTT↔Kafka bridging with enterprise features [17]:

- **Bidirectional**: Kafka Sink (MQTT → Kafka) and Kafka Source (Kafka → MQTT) [17]
- **SQL rule engine**: Dynamic topic selection (e.g., `device-${payload.device}`) without custom code [17]
- **Performance tuning**: Configurable batching (up to 896 KB), sync/async writes, compression [17]
- **Authentication**: None, AWS IAM, OAuth 2.0, Basic Auth, Kerberos [17]
- **Buffer modes**: Memory, Disk (survives restarts), Hybrid [17]

**Limitation:** Commercial license — not open source [17]. Requires enterprise subscription for production use.

## NATS Native MQTT

MQTT v3.1.1 built into NATS Server since v2.2 [18]:

- **Topic mapping**: MQTT `/` → NATS `.`, wildcard translation (`#` → `>`, `+` → `*`) [18]
- **QoS support**: 0, 1, and 2 for MQTT clients [18]
- **Cross-protocol delivery**: MQTT subscriptions become NATS subscriptions cluster-wide [18]
- **JetStream required** for any MQTT client (persistence for sessions/retained messages) [18]

**Critical limitation:** NATS-originated messages delivered to MQTT subscribers are **always QoS 0** [18]. Retained messages in clusters are "best-effort" — not immediately consistent [18].

## Kafka Connect

700+ connector ecosystem but significant operational challenges [24][25]:

- **Silent failures**: Connectors show RUNNING while streaming has stopped ("half-dead task" state) [24]
- **Configuration complexity**: 10,000 forum posts analyzed — configuration as root cause of most issues [25]
- **Resource overhead**: JVM-based, requires dedicated Connect workers (2 CPUs, 4GB RAM typical) [19]
- **SMT limitations**: "Really simple stateless transformations" — complex logic requires Kafka Streams [28]
- **Confluent MQTT Proxy deprecated** in v7.9 [23]

## Cross-Protocol Ordering Conflicts

MQTT ordering applies within single client/topic/QoS only [26]. Kafka guarantees per-partition ordering. When bridging, the weakest guarantee wins — or worse, reordering violates both protocols' assumptions [counter agent]. Protocol bridging creates "domino effect" of complexity: persistent messages, out-of-order delivery requiring de-duplication, smart middleware violating the end-to-end principle [27].

## Anti-Patterns

1. **The complexity domino**: Each bridge adds latency, failure modes, and configuration surface [27]
2. **"If reliability is important on the business level, do it on the business level"** — generic reliability layers handle only generic logic [27]
3. **MQTT-Kafka architectural mismatch**: Kafka clients too heavy for IoT edge, topic scalability breaks with per-device topics [counter agent]

## Decision Framework

| Scenario | Recommended Solution |
|----------|---------------------|
| MQTT ↔ Kafka with filtering, open source | Redpanda Connect [15] |
| MQTT ↔ Kafka, enterprise with SQL rules | EMQX Enterprise [17] |
| MQTT ↔ NATS, lightweight | NATS native MQTT [18] |
| Kafka ↔ databases/APIs, existing ecosystem | Kafka Connect (with operational investment) [25] |
| Simple MQTT → Kafka, minimal | Strimzi MQTT Bridge [22] |
| Multi-hop (MQTT → Kafka → NATS) | Redpanda Connect or custom code |

## Gaps and Limitations

- No head-to-head benchmark comparing Redpanda Connect vs EMQX vs NATS for MQTT↔Kafka throughput
- NATS MQTT support limited to v3.1.1 — no MQTT 5 features [18]
- Redpanda Connect performance claims (50 Gbps) are vendor-stated, not independently verified [15]
- Disconnected/air-gapped operation (store-and-forward when upstream brokers unreachable) poorly documented across all solutions
