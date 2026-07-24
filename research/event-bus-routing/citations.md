# Citations — Event Bus Routing

All sources visited in-session via WebSearch or WebFetch on 2026-07-24.

## Broker Landscape

[1] "NATS vs Kafka vs MQTT: Same Category, Very Different Jobs." HarrisonSec, 2025. https://harrisonsec.com/blog/nats-kafka-mqtt-same-category-different-jobs/ — Design axes comparison, latency data (NATS sub-ms, Kafka 5–10ms, Kafka-as-RPC 30–50ms), throughput (NATS tens of millions msgs/sec/node, Kafka hundreds MB/s/broker), decision flow. Tier 3.

[2] "The Data Streaming Landscape 2025." Kai Waehner, 2024-12-04. https://www.kai-waehner.de/blog/2024/12/04/the-data-streaming-landscape-2025/ — Kafka as de facto standard, Pulsar "zero traction," Flink becoming standard for stream processing, BYOC emerging via WarpStream. Qualitative field observations, no hard market share numbers. Tier 3.

[3] "Apache Kafka's 80 Percent Problem." Aiven blog, 2025. https://aiven.io/blog/apache-kafkas-80-percent-problem — 56% of clusters ≤1 MB/s, median ingest 9.81 MB/s across 4K services, cost analysis ($300K/yr self-managed vs $50K managed vs <$5K S3). Vendor blog but uses internal fleet data. Tier 2.

[4] "Kafka is Overkill for 80% of Projects — Prove Me Wrong." Medium/@techInFocus, 2025. https://medium.com/@techInFocus/kafka-is-overkill-for-80-of-projects-prove-me-wrong-0d966988b58d — Case studies of Kafka overuse (6-person fintech, enterprise cron-job scenario). Tier 4.

[5] "When NOT to Use Kafka: 5 Scenarios Where Simpler Wins." Conduktor, 2025. https://www.conduktor.io/blog/when-not-to-use-kafka — Decision criteria for when Kafka is inappropriate (<10K msgs/day, fire-and-forget, request-reply). Tier 3.

[6] "NATS: Technically Elegant, Clearly Limited Ceiling." RobustMQ, 2025. https://robustmq.com/en/Blogs/38 — NATS market ceiling argument, protocol lock-in, Go GC bottlenecks. Competitor perspective. Tier 3.

[7] "JetStream Anti-Patterns." Synadia blog, 2025. https://www.synadia.com/blog/jetstream-design-patterns-for-scale — Consumer info overuse, >100K consumer overhead, >300 disjoint filters instability. Official vendor docs. Tier 2.

[8] "Comparison of Open Source MQTT Brokers 2026." EMQX blog. https://www.emqx.com/en/blog/a-comprehensive-comparison-of-open-source-mqtt-brokers-in-2023 — EMQX 100M connections on 23-node cluster, Mosquitto ~1K connections before packet loss, HiveMQ 200M connections. Vendor comparison. Tier 2.

[9] "NATS JetStream vs RabbitMQ vs Apache Kafka on VPS — 2025 Benchmarks." onidel.com, 2025. https://onidel.com/blog/nats-jetstream-rabbitmq-kafka-2025-benchmarks — Standardized VPS benchmarks across three brokers. Tier 3.

[10] "Kafka vs RabbitMQ: 1M msgs/sec vs 40K [2026]." tech-insider.org, 2026. https://tech-insider.org/kafka-vs-rabbitmq-2026/ — Throughput comparison, RabbitMQ 4.1 improvements. Tier 3.

[11] "Message Broker Market 2025 To 2033." Business Research Insights. https://www.businessresearchinsights.com/market-reports/message-broker-market-113346 — Market size $1.98B (2024) → $4.4B (2033), 10% CAGR. Tier 2.

[12] "MQTT Broker Comparison." mqttt.com. https://mqttt.com/brokers/ — EMQX, HiveMQ, Mosquitto feature comparison. Tier 3.

[13] "Kafka vs RabbitMQ vs NATS vs SQS: Choosing the Right Message Broker." BackendBytes, 2025. https://backendbytes.com/articles/message-queue-comparison/ — Use case guidance. Tier 3.

[14] "Migrating from Classic Mirrored Queues to Quorum Queues in 2025." RabbitMQ blog, 2025-07-29. https://www.rabbitmq.com/blog/2025/07/29/latest-benefits-of-rmq-and-migrating-to-qq-along-the-way — RabbitMQ 4.1 active development. Tier 2.

## Multi-Protocol Bridging

[15] "Introducing Redpanda Connect." Redpanda blog. https://www.redpanda.com/blog/redpanda-connect — 225 connectors, Apache 2.0, single 128 MiB binary, starts ~140ms, scales from 100 millicores to 50 Gbps. Tier 2.

[16] Redpanda Connect GitHub repository. https://github.com/redpanda-data/connect — Source code, connector list, Bloblang documentation. Tier 1.

[17] "Stream MQTT Data into Apache Kafka." EMQX Enterprise Docs. https://docs.emqx.com/en/emqx/latest/data-integration/data-bridge-kafka.html — Bidirectional Kafka Sink/Source, SQL rule engine, dynamic topic mapping (device-${payload.device}), batching up to 896 KB, sync/async modes. Tier 2.

[18] "MQTT | NATS Docs." NATS.io. https://docs.nats.io/running-a-nats-service/configuration/mqtt — MQTT v3.1.1 support since v2.2, topic→subject mapping, QoS 0/1/2, JetStream required, NATS→MQTT always QoS 0, retained messages best-effort in clusters. Tier 1.

[19] "Migrating from Kafka Connect to Redpanda Connect." Platformatory, 2025. https://platformatory.io/blog/migrating-kafka-connect-to-redpanda/ — Bloblang vs SMTs, single YAML config, input→pipeline→output architecture, Go-based vs JVM. Tier 3.

[20] "Integrating MQTT Data from Mosquitto to Kafka." Cedalo, 2025. https://www.cedalo.com/blog/mqtt-to-kafka-integration — Mosquitto Pro Kafka bridge plugin. Tier 3.

[21] "MQTT Source Connector for Confluent Platform." Confluent docs. https://docs.confluent.io/kafka-connectors/mqtt/current/mqtt-source-connector/overview.html — Confluent MQTT Source Connector. Tier 2.

[22] Strimzi MQTT Bridge GitHub. https://github.com/strimzi/strimzi-mqtt-bridge — Apache 2.0, unidirectional MQTT→Kafka, MQTT 3.1.1, 50 stars. Tier 3.

[23] "MQTT Proxy for Confluent Platform (Deprecated)." Confluent docs. https://docs.confluent.io/platform/current/kafka-mqtt/index.html — Deprecated in v7.9. Tier 2.

[24] "Kafka Connect in Production Without Bad Surprises." Medium, 2025. https://medium.com/@maroinemlis/kafka-connect-not-working-youre-not-alone-077708ee959a — Silent "half-dead task" failures, zombie connector states. Tier 4.

[25] "The Real Problems with Apache Kafka: 10,000 Forum Posts Analyzed." Conduktor, 2025. https://www.conduktor.io/blog/apache-kafka-what-10-000-forum-posts-reveal — Configuration complexity as root cause, cryptic errors. Tier 3.

[26] "Understanding MQTT Message Ordering." HiveMQ blog. https://www.hivemq.com/blog/understanding-mqtt-message-ordering — Ordering only within single client/topic/QoS; cross-topic disorder, QoS mixing breaks ordering. Tier 2.

[27] "Anti-pattern: Advanced Messaging Systems." CedaNet. https://cedanet.com.au/antipatterns/advanced-messaging-systems.php — Protocol bridging as domino effect of complexity; 12 network hops with brokers vs 3 without. Tier 3.

[28] "Is Benthos the New Kafka Connect?" Streaming Data Tech, 2025. https://www.streamingdata.tech/p/is-benthos-the-new-kafka-connect — Benthos lacks stateful processing, Bloblang non-Turing-complete. Tier 3.

## Content-Based Routing & Filtering

[29] "Broker-Side SQL Filter Expressions." RabbitMQ blog, 2025-09-23. https://www.rabbitmq.com/blog/2025/09/23/sql-filter-expressions — Two-stage Bloom+SQL filtering, 4.87M msgs/sec (12x over SQL-only), introduced in RabbitMQ 4.2. Tier 2.

[30] "Subject-Based Messaging." NATS docs. https://docs.nats.io/nats-concepts/subjects — Subject hierarchies, wildcards (* single-token, > multi-token), location-transparent routing. Tier 1.

[31] "CloudEvents Subscriptions Spec." CNCF/CloudEvents. https://github.com/cloudevents/spec/blob/main/subscriptions/spec.md — Six required filter dialects (exact, prefix, suffix, all, any, not), optional SQL dialect, approved June 2024. Tier 1.

[32] "Putting Events in Their Place with Dynamic Routing." Confluent blog. https://www.confluent.io/blog/putting-events-in-their-place-with-dynamic-routing/ — TopicNameExtractor (KIP-303), runtime topic selection, enrichment-based routing. Tier 2.

[33] "Using Kafka Headers Effectively." Conduktor. https://www.conduktor.io/glossary/using-kafka-headers-effectively — Headers for routing without payload deserialization, best practices. Tier 3.

[34] "RabbitMQ-to-NATS JetStream Routing Patterns." Synadia blog. https://www.synadia.com/blog/rabbitmq-routing-patterns-in-nats-jetstream — Stream vs consumer filtering, domain-based stream boundaries. Tier 2.

[35] "JetStream Consumers." NATS docs. https://docs.nats.io/nats-concepts/jetstream/consumers — FilterSubject and FilterSubjects for consumer-level routing. Tier 1.

[36] "Beyond Kafka for Operational Use Cases: Flexible Event Filtering." Solace blog. https://solace.com/blog/beyond-kafka-4-dynamic-event-routing/ — Kafka lacks broker-side filtering, comparison to Solace native routing. Tier 3.

[37] KAFKA-6020: "Add broker side filter capability." Apache JIRA. https://issues.apache.org/jira/browse/kafka-6020 — Open since 2017, 12 votes, 29 watchers, unresolved. Tier 1.

[38] "Content-Based Router." Enterprise Integration Patterns (Hohpe & Woolf). https://www.enterpriseintegrationpatterns.com/patterns/messaging/ContentBasedRouter.html — Canonical EIP pattern definition, maintenance risk as "dumping ground." Tier 1.

[39] "MQTT 5 Shared Subscriptions." HiveMQ blog. https://www.hivemq.com/blog/mqtt5-essentials-part7-shared-subscriptions/ — $share/GROUP/TOPIC syntax, round-robin distribution, load balancing. Tier 2.

[40] "RabbitMQ Stream Filtering Internals." RabbitMQ blog, 2023-10-24. https://www.rabbitmq.com/blog/2023/10/24/stream-filtering-internals — Bloom filter mechanics at chunk level. Tier 2.

## Python Ecosystem

[41] "FastStream Documentation." AG2AI. https://faststream.ag2.ai/latest/ — Unified API across Kafka (AIOKafka & Confluent), RabbitMQ, NATS, Redis, MQTT. Pydantic validation, DI, AsyncAPI generation. Production/Stable status. Tier 2.

[42] FastStream GitHub repository. https://github.com/ag2ai/faststream — Multi-broker async framework, MQTT support added. Tier 2.

[43] "Choosing the best Kafka client for Python." Sulyak blog, 2025. https://blog.sulyak.info/post/choosing-the-best-kafka-client-for-python/ — confluent-kafka-python "high (near Java client)" performance, aiokafka "moderate," kafka-python deprecated. Qualitative, no benchmarks. Tier 3.

[44] "AIOKafka vs Confluent vs Kafka: Python Comparison 2025." DevEverest, 2025. https://deveverest.com/aiokafka-vs-confluent-vs-kafka/ — Performance benchmarks and production readiness comparison. Tier 3.

[45] kafka-client-benchmarks GitHub. https://github.com/abhishekray07/kafka-client-benchmarks — confluent-kafka 22K msgs/sec, aiokafka 45K msgs/sec async. Tier 3.

[46] "The Tragedy of Faust: Python's Stream Processing." Medium/Gang Tao. https://taogang.medium.com/the-past-and-present-of-stream-processing-17-the-tragedy-of-faust-pythons-stream-processing-3f4aaa2556c9 — Faust abandoned by Robinhood ~Oct 2020, progressive consumer death, memory leaks 10MB/s, 644/300K events lost. Tier 3.

[47] "Python-Native Ultra-Fast Streaming with Quix Streams." Medium/Gang Tao. https://taogang.medium.com/the-past-and-present-of-stream-processing-part-23-python-native-ultra-fast-streaming-with-quix-8fdc83946ab8 — McLaren F1 origins, Streaming DataFrame API, RocksDB state. Tier 3.

[48] Quix Streams GitHub repository. https://github.com/quixio/quix-streams — Pure Python Kafka streaming, DataFrame API, v3.15.0+ with join_asof(). Tier 2.

[49] "Bytewax — The Burned-Out Data Candle." Medium/Gang Tao. https://taogang.medium.com/the-past-and-present-of-stream-processing-part-20-bytewax-the-burned-out-data-candle-760223db6b64 — Last OSS v0.21.1 (Nov 2024), waxctl archived (Mar 2025). Tier 3.

[50] Bytewax GitHub repository. https://github.com/bytewax/bytewax — Python+Rust, Apache 2.0, stateful operators. Tier 2.

[51] "Comparison of Python MQTT clients." EMQX/Medium. https://emqx.medium.com/comparison-of-python-mqtt-clients-9ecc219a9e15 — HBMQTT deprecated, asyncio-mqtt recommended. Tier 3.

[52] confluent-kafka-python GitHub. https://github.com/confluentinc/confluent-kafka-python — Active maintenance, enterprise backing, C-backed via librdkafka. Tier 2.

[53] aiokafka GitHub. https://github.com/aio-libs/aiokafka — Pure Python asyncio Kafka client, maintained by aio-libs. Tier 2.

[54] "Kafka Client Updates: KIP-848, Python Asyncio, OAuth." Confluent blog, 2025. https://www.confluent.io/blog/kafka-client-updates-kip-848-oauth/ — confluent-kafka-python 2.13.0b1 adds asyncio interfaces. Tier 2.

[55] "Python vs Go for Backend Development in 2026." dev.to, 2026. https://dev.to/_d7eb1c1703182e3ce1782/python-vs-go-for-backend-development-in-2026-an-honest-comparison-3pno — Python 12.5–24.8K req/s vs Go 95–214K req/s (7.6–8.6x gap). Tier 4.

[56] "Python vs Go Microservices Performance Comparison 2026." Free Academy, 2026. https://freeacademy.ai/blog/python-vs-go-microservices-performance-comparison-2026 — E-commerce migration: 2,500 → 38,000 req/s (15x), 120ms → 4ms P99. Tier 4.

[57] "What Python's GIL Change Actually Means." dev.to, 2025. https://dev.to/naresh_007/what-pythons-gil-change-actually-means-in-real-systems-2aml — Python 3.13 free-threading: 4x multi-core improvement, 21.8% single-core degradation. Tier 4.

[58] "Edge AI Event Processing Under the GIL." arXiv:2601.10582v3. https://arxiv.org/html/2601.10582v3 — 40.2% throughput drop single-core, 35.1% quad-core beyond optimal thread count, 2–4.8x P99 latency explosion. Tier 1.

## Go Ecosystem

[59] franz-go GitHub repository. https://github.com/twmb/franz-go — Pure Go, Kafka 0.8.0–4.2+, feature-complete. Tier 2.

[60] "A brief comparison of mainstream Kafka clients in the Go community." SoByte, 2022. https://www.sobyte.net/post/2022-03/the-comparison-of-the-go-community-leading-kakfa-clients/ — franz-go vs Sarama vs kafka-go comparison. Tier 3.

[61] "franz-go vs sarama comparison." LibHunt. https://www.libhunt.com/compare-franz-go-vs-sarama — Side-by-side feature and performance comparison. Tier 3.

[62] "Tuning for Performance." WarpStream docs. https://docs.warpstream.com/warpstream/kafka/configure-kafka-client/tuning-for-performance — franz-go performance characteristics, Sarama "fails to maintain strict ordering," "does not implement idempotent producer correctly." Tier 2.

[63] Sarama GitHub repository (IBM). https://github.com/IBM/sarama — Shopify seeking new maintainer, known liveness/correctness issues. Tier 2.

[64] Watermill GitHub repository. https://github.com/ThreeDotsLabs/watermill — 9.8K stars, 12 official pub/sub implementations, MIT license. Tier 2.

[65] "Watermill Router." Watermill docs. https://watermill.io/docs/messages-router/ — HTTP handler pattern, middleware support, topic-based routing (no built-in content filtering). Tier 2.

[66] Eclipse Paho MQTT Go Client. https://github.com/eclipse-paho/paho.mqtt.golang — MQTT v3.1/3.11, full async, v5 available. Tier 2.

[67] nats.go GitHub repository. https://github.com/nats-io/nats.go — Official Go NATS client with JetStream. Tier 1.

[68] "Alibaba Cloud: Why Not Use Sarama." Alibaba Cloud Help. https://www.alibabacloud.com/help/en/apsaramq-for-kafka/cloud-message-queue-for-kafka/support/why-is-it-not-recommended-to-use-a-go-client-developed-with-the-sarama-library-to-send-and-subscribe-to-messages — Cannot detect new partitions without restart, data loss v1.27–1.30, LZ4 memory exhaustion. Tier 2.

[69] "Benthos: The Reliable Guardian of Ordinary Tasks." Medium/Gang Tao. https://taogang.medium.com/the-past-and-present-of-stream-processing-part-16-benthos-the-reliable-guardian-of-ordinary-5a8cdaefad0f — Stateless architecture, Bloblang non-Turing-complete, "middle ground" between collectors and stream processors. Tier 3.

[70] "Golang's Real-Time GC in Theory and Practice." Pusher blog. https://pusher.com/blog/golangs-real-time-gc-in-theory-and-practice/ — 7–38ms GC pauses measured in production. Tier 2.

[71] "Processing CDN logs with Kafka transactions." Mux blog. https://www.mux.com/blog/processing-cdn-logs-exactly-once-with-kafka-transactions — Real-world franz-go adoption and exactly-once semantics. Tier 3.

[72] "Go Concurrency Patterns: Pipelines and Cancellation." Official Go blog. https://go.dev/blog/pipelines — Pipeline pattern, fan-out/fan-in, cancellation via done channels. Tier 1.

[73] "Event-Driven Architecture and Message Design Anti-Patterns." Ben Morris, 2025. https://www.ben-morris.com/event-driven-architecture-and-message-design-anti-patterns-and-pitfalls — Chatty services, command-event confusion, entity-based event anti-patterns. Tier 3.

## Integration Frameworks

[74] PyPipeline GitHub repository. https://github.com/vaibhav-sinha/pypipeline — Python EIP DSL, GPL-3.0, ~34 stars, inactive since 2016. Tier 4.

[75] Nameko GitHub repository. https://github.com/nameko/nameko — Python microservices framework, RPC/events over RabbitMQ, Apache 2.0, 4.8K stars. Tier 2.

[76] "Watermill: Introducing Watermill." Three Dots Labs blog, 2018. https://threedots.tech/post/introducing-watermill/ — Design philosophy, infrastructure-agnostic event-driven development. Tier 3.

[77] Kombu GitHub repository. https://github.com/celery/kombu — AMQP abstraction powering Celery, 8 broker backends, BSD-3, 3.1K stars. Tier 2.

[78] "NATS Supported by FastStream." NATS blog. https://nats.io/blog/nats-supported-by-faststream/ — FastStream NATS JetStream integration. Tier 2.

[79] "Watermill Troubleshooting." Watermill docs. https://watermill.io/docs/troubleshooting/ — Deadlocks, GoChannel non-persistence, no consumer groups, no distributed dedup. Tier 2.

[80] "Camel-K issue #1196: 100 integrations = 100 JVM pods." Apache JIRA. https://github.com/apache/camel-k/issues/1196 — Camel-K resource consumption at scale. Tier 2.

[81] "Camel-K: A Critical Look." Kevin Boone. https://kevinboone.me/camelk.html — "Extremely complex" infrastructure, confusing status reporting, design compromises. Tier 3.
