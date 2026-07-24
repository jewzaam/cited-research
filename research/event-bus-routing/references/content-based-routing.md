# Content-Based Routing & Filtering

Covers broker-side filtering, application-side routing, filter DSLs, and the CloudEvents filtering specification. Sources in [citations.md](../citations.md).

## Filtering by Broker

| Broker | Broker-Side Filtering | Mechanism | Limitation |
|--------|----------------------|-----------|------------|
| **NATS** | Yes — first-class | Subject hierarchies + wildcards [30] | Limited to subject naming; no payload inspection |
| **RabbitMQ 4.2** | Yes — Bloom + SQL | Two-stage: chunk-level Bloom → per-message SQL [29] | AMQP 1.0 only; publishers must annotate messages |
| **MQTT 5** | Partial — topic filters | Topic wildcards (# and +), shared subscriptions [39] | No payload-level filtering at broker |
| **Kafka** | No | KAFKA-6020 unresolved since 2017 [37] | All filtering is application-side |
| **Redis Streams** | No | Consumer groups only | Application-side filtering required |

## NATS Subject-Based Routing

NATS subject hierarchies enable content-based routing through naming conventions rather than payload inspection [30]:
- Wildcards: `*` matches single token, `>` matches remainder of subject [30]
- JetStream streams capture messages matching subject patterns [35]
- Filtered consumers: `FilterSubject` and `FilterSubjects` provide independent views over stored data [35]
- Subject mapping transforms subjects at stream ingress, mirror, and source [NATS docs]

One stream holds data; multiple consumers filter their delivery — avoids message duplication across "queues" [34].

**Anti-pattern:** >300 disjoint filters per consumer causes indexing/matching slowness and instability [7].

## RabbitMQ Bloom + SQL Filtering

Introduced in RabbitMQ 4.2 for streams [29]:

| Mode | Rate (10M messages, 10 matching) | Improvement |
|------|----------------------------------|-------------|
| SQL filter only | 404,645 msgs/sec | Baseline |
| Bloom + SQL filter | 4,868,549 msgs/sec | ~12x |

SQL syntax supports: equality, arithmetic, IN clauses, UTC(), boolean operators, access to message properties and application properties [29]. Benchmark ran on single Erlang scheduler thread — rates are per-thread [29].

**Trade-off:** Publishers must annotate messages with `x-stream-filter-value` for Bloom stage [29]. Bloom filters operate at chunk granularity — consumers may receive unwanted messages within chunks and must filter locally [40].

## Kafka: Application-Side Only

KAFKA-6020 (broker-side filtering) has been open since 2017 with 12 votes and 29 watchers, still unresolved [37]. Kafka's filtering approaches are all application-level:

- **Headers**: Routing without payload deserialization [33]. Best practice: headers for routing metadata, payload for business logic [33]
- **Kafka Streams**: `filter()`, `filterNot()`, `branch()` for predicate-based routing [32]. Limited to fixed predicates; dynamic routing requires Processor API [32]
- **TopicNameExtractor** (KIP-303, Kafka 2.0+): Runtime topic selection based on record content [32]. Output topics must be pre-created [32]

Solace positions this gap as fundamental: "Kafka was built for high-throughput log storage, not for operational event routing" [36].

## MQTT 5 Filtering

- **Topic wildcards**: `#` (multi-level) and `+` (single-level) [39]
- **Shared subscriptions**: `$share/GROUP/TOPIC` for load balancing — round-robin distribution across group members [39]
- **No payload-level broker filtering**: Content filtering is client-side

**Anti-pattern:** Subscribing to `#` (catch-all) and filtering client-side wastes network — broker-side topic design reduces load 70–80% [counter agent].

## CloudEvents Filtering Specification

CloudEvents Subscriptions spec (approved June 2024) defines vendor-neutral filtering [31]:

- **Six required dialects**: exact, prefix, suffix, all, any, not
- **One optional dialect**: SQL (references CESQL spec)
- Conjunctive top-level logic — all filters must pass
- 64KB size limit forces linking over embedding [counter agent]

**Adoption concern:** Spec approved June 2024 — still early adoption phase [counter agent]. Implementation prevalence across brokers/platforms unclear.

## Content-Based Router Pattern Risks

The canonical EIP pattern [38] carries maintenance risk:
- Router becomes "point of frequent maintenance" [38]
- Routing function risks becoming "dumping ground" for miscellaneous logic [38]
- When routing rules exceed simple predicates (time windows, regional checks, multi-attribute Boolean logic), application logic becomes necessary [counter agent]

## Hybrid Approach Required

Even with broker-side filtering (especially probabilistic methods like Bloom filters), client-side filtering remains necessary as a second stage [40]. The performance case for broker-side filtering is strongest at low selectivity: e.g., 10 matching messages from 10M requires processing all 10M application-side vs only 10 with broker-side filtering [29].

## Decision Framework

| Routing Need | Recommended Approach |
|-------------|---------------------|
| Route by message category/type | NATS subjects or MQTT topics (broker-side) |
| Complex SQL-like predicates | RabbitMQ 4.2 SQL filtering [29] |
| Dynamic routing based on content | Kafka Streams + TopicNameExtractor [32] |
| Protocol-agnostic filtering spec | CloudEvents filtering [31] |
| Cross-protocol unified filtering | Redpanda Connect Bloblang [15] |
| Header-based routing without deserialization | Kafka headers [33] |

## Gaps and Limitations

- No published benchmarks comparing NATS consumer filtering vs RabbitMQ Bloom+SQL at same scale
- CloudEvents filtering implementation maturity across brokers unknown
- Kafka KAFKA-6020 shows no signs of resolution despite years of demand [37]
- MQTT 5 `?key=value` subscription filter syntax: broker implementation status unclear
