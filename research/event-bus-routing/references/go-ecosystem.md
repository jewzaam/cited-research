# Go Ecosystem

Covers Go libraries and frameworks for event routing: Kafka clients, messaging frameworks, MQTT/NATS clients, and concurrency patterns. Sources in [citations.md](../citations.md).

## Kafka Client Comparison

| Client | Performance | CGO | Maintenance | Status |
|--------|------------|-----|-------------|--------|
| **franz-go** | 2.5x faster producing, 1.5x faster consuming vs Sarama [62] | No (pure Go) | Active [59] | **Recommended** |
| **confluent-kafka-go** | High (librdkafka) | Yes | Active | CGO friction |
| **segmentio/kafka-go** | Moderate | No | Active | Less popular |
| **Sarama (IBM)** | Moderate | No | **Seeking new maintainer** [63] | **Avoid** |

**franz-go** consensus as leading Go Kafka client [59][60][61]:
- Feature-complete: Kafka 0.8.0 through 4.2+ [59]
- Pure Go, no CGO dependencies [59]
- Production adoption: Mux (CDN logs with Kafka transactions) [71], WarpStream [62]

**Sarama explicitly recommended against:**
- Alibaba Cloud: Cannot detect new partitions without restart, non-compliant protocol triggering mass duplicate consumption, data loss v1.27–1.30, LZ4 memory exhaustion [68]
- WarpStream: "Fails to maintain strict ordering," "does not implement idempotent producer correctly" [62]
- Shopify seeking new maintainer [63]

## Messaging Frameworks

### Watermill

Production-ready, infrastructure-agnostic pub/sub [64][65]:
- 12 official transports: Kafka, AMQP, Redis, GCP Pub/Sub, NATS, SQL, etc. [64]
- Router follows HTTP handler pattern: `func(*Message) ([]*Message, error)` [65]
- Middleware: retry, poison queue, throttling, metrics, tracing [64]
- 9.8K stars, MIT license, 516 commits [64]

**Limitations:** No built-in content-based routing [65]. Default deduplicator doesn't support distributed operations [79]. GoChannel pub/sub not persistent [79]. Deadlocks require pprof debugging [79]. Bootstrapped without VC backing [counter agent].

### Redpanda Connect (Benthos)

Standalone stream processor written in Go [15][16][69]:
- 225+ connectors, single binary [15]
- Bloblang for transformations [19]
- Stateless — no windowing, joins, aggregations [69]
- Bloblang non-Turing-complete, no cross-message state [69]

See [multi-protocol bridging](../references/multi-protocol-bridging.md) for full analysis.

## Protocol-Specific Clients

### MQTT
**Eclipse Paho Go** — most widely recommended [66]:
- MQTT v3.1/3.11 with full async operation
- MQTT v5 support available
- Alternatives: go-mqtt/mqtt (delivery guarantees), at-wat/mqtt-go (thread-safe, context-controlled)

### NATS
**nats.go** — official client [67]:
- Built-in JetStream support with new API (jetstream package)
- Requires nats-server ≥ 2.9.0
- Smaller, simpler interfaces vs legacy JetStreamContext

## Go Concurrency Advantages

Go's CSP model (communicating sequential processes) naturally maps to event-driven patterns [72]:

- **Pipeline pattern**: Stages connected by channels, goroutines per stage [72]
- **Fan-out/fan-in**: Parallelize independent work, combine results [72]
- **Worker pools**: Fixed workers processing from shared queue [72]
- **No GIL**: True parallelism without Python's threading constraints [counter agent]
- **Goroutines**: Lightweight (2–8 KB each), support 100K+ concurrent [counter agent]

Go channels + `select` provide message routing, distribution, merging, splitting, health monitoring without external dependencies [counter agent].

## Go Limitations

### GC Latency
7–38ms pauses measured in production at Pusher [70]. 10-second STW pauses reported with 64GB heaps [counter agent]. "For operations with hard deadline in milliseconds range, GC delay could already result in missing a deadline" [counter agent].

### Goroutine Hazards
Panics cascade across goroutines and crash entire applications unless every goroutine wraps with `defer`/`recover()` [counter agent]. Closing closed channels panics; unbuffered channels deadlock without receivers [counter agent]. Blue Matador required wrapper boilerplate on every single goroutine [counter agent].

### Rust Comparison
2x throughput (3,887 vs 2,001 req/s), 2–4x lower memory (50–80MB vs 100–320MB), zero-copy via pointer manipulation, deterministic latency without GC pauses [counter agent]. Relevant only for latency-critical workloads — Go remains adequate for typical message queue processing [counter agent].

## Decision Framework

| Need | Recommendation |
|------|---------------|
| Kafka client | franz-go [59] |
| Multi-protocol framework | Watermill [64] (or Redpanda Connect for standalone routing) |
| MQTT client | Eclipse Paho Go [66] |
| NATS client | nats.go [67] |
| Ultra-low-latency (<10ms) | Consider Rust instead [counter agent] |

## Gaps and Limitations

- Limited quantitative benchmarks comparing all Kafka clients head-to-head
- Watermill production case studies at enterprise scale sparse
- Benthos/Redpanda Connect community reaction to renaming not fully explored
- GC latency numbers from Pusher may be outdated (pre-Go 1.22 improvements) [70]
- Rust comparison data from generic web benchmarks, not message routing specifically
