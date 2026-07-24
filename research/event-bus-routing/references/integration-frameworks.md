# Integration Frameworks

Covers what plays the Apache Camel role in Python and Go — frameworks that handle routing, filtering, and multi-connector patterns. Sources in [citations.md](../citations.md).

## Landscape Summary

| Framework | Language | Brokers | Stars | License | Status |
|-----------|----------|---------|-------|---------|--------|
| **FastStream** | Python | Kafka, RabbitMQ, NATS, Redis, MQTT | — | Apache 2.0 | Production/Stable |
| **Watermill** | Go | 12 pub/sub implementations | 9.8K | MIT | Production-ready |
| **Redpanda Connect** | Go (standalone) | 225+ connectors | — | Apache 2.0 | Active |
| **Nameko** | Python | RabbitMQ (AMQP) | 4.8K | Apache 2.0 | Active |
| **Kombu** | Python | 8 backends (RabbitMQ, Redis, SQS...) | 3.1K | BSD-3 | Active |
| **Camel-K** | JVM (polyglot) | 300+ components | — | Apache 2.0 | Active but complex |
| **PyPipeline** | Python | N/A | 34 | GPL-3.0 | Inactive (2016) |

## Python: No Mature Camel Equivalent

Python lacks a single framework equivalent to Apache Camel [integration discovery agent]. The ecosystem splits into:

1. **FastStream** — closest to a unified routing framework, covering 5 brokers with a single API [41][42][78]
2. **Kombu** — AMQP abstraction powering Celery, pattern-based routing via routing keys, 8 broker backends [77]
3. **Nameko** — microservices framework with RPC/events over RabbitMQ, topic-based routing [75]
4. **Custom asyncio patterns** — `asyncio.Queue` + handlers scales for simpler cases [counter agent]

**FastStream** is the standout for multi-protocol routing [41]:
- Unified `@broker.subscriber`/`@broker.publisher` API across Kafka, RabbitMQ, NATS, Redis, MQTT
- Broker-specific features accessible (Kafka partitions/groups, RabbitMQ exchanges/RPC, NATS JetStream)
- Pydantic validation, dependency injection, AsyncAPI auto-generation
- In-memory testing utilities
- Production/Stable status on PyPI

**Counter-perspective:** Simple Python patterns often suffice. A minimal event bus using `collections.defaultdict` is ~15 lines. For I/O-bound workloads, Celery is overkill — 2.5GB for 50 concurrent tasks while async alternatives use 80MB [counter agent]. One team spent a week removing a RabbitMQ library to write "simple AMQP classes" after hitting inflexibility [counter agent].

## Go: Watermill Dominates

**Watermill** (MIT, 9.8K stars) provides infrastructure-agnostic pub/sub [64][65]:
- 12 official transports: Kafka, AMQP, Redis, GCP Pub/Sub, NATS, SQL, etc.
- Router follows HTTP handler pattern: `func(*Message) ([]*Message, error)` [65]
- Middleware for retry, poison queue, throttling, metrics, tracing [64]
- Hundreds of thousands msgs/sec throughput [discovery agent]

**Limitation:** No built-in content-based routing — topic-based only [65]. Content filtering requires handler/middleware logic. Default deduplicator doesn't support distributed operations [79]. GoChannel pub/sub isn't persistent — messages to topics with no subscribers are discarded [79]. Deadlocks documented as common pattern requiring pprof debugging [79]. Bootstrapped project without VC backing [counter agent].

**Counter-perspective:** Go channels handle most routing without frameworks. All standard concurrent patterns (fan-out, fan-in, pipeline, tee, rate limiting) built with channels, goroutines, `sync.WaitGroup`, and `context` [72]. "Share memory by communicating" via channels appears vindicated by lack of Go integration framework ecosystem comparable to JVM [counter agent].

## Camel-K: Complex and Resource-Heavy

100 integrations = 100 JVM pods = massive CPU/RAM consumption [80]. Users question whether consolidating routes into fewer pods is possible [80]. Infrastructure "extremely complex" with "confusing" status reporting [81]. Python language support in Camel Quarkus is Preview status, JVM-only, used for expression evaluation within routes — not for writing routes [integration discovery agent].

## The Framework vs Library Decision

| Favors Libraries/Simple Code | Favors Framework |
|------------------------------|------------------|
| Simple integrations | Complex multi-protocol routing |
| Small teams | Large scale requiring standardization |
| Agile/iterative delivery | Need for commercial support |
| I/O-bound workloads | Standardization across many teams |

Framework value proposition emerges when: (1) complex workflow primitives needed (chaining, fan-out, chords), (2) standardization across many teams required, (3) commercial support needed [counter agent].

## Gaps and Limitations

- FastStream performance ceiling not well-documented — abstraction overhead unknown [Python discovery agent]
- No head-to-head benchmark: FastStream vs native clients
- Watermill production case studies at scale are sparse
- PyPipeline (only Python EIP DSL) is effectively abandoned [74]
- Camel-K maturity unclear — some critique may be dated [counter agent]
