# Reference: Practical Integration Pattern

Covers the recommended wiring for a Python app on OpenShift that uses OTEL and
ships logs to the OpenShift logging stack. All citations reference
[../citations.md](../citations.md).

---

## Two Fundamental Approaches

The OTEL specification defines two log collection workflows [30]:

### 1. Direct to Collector (OTLP) — Recommended

> "In the direct to collector workflow, logs are emitted directly from an application
> to a collector using a network protocol (e.g. OTLP). This workflow is simple to set
> up as it doesn't require any additional log forwarding components." [30]

> "If you want to get logs from your application ingested into an OpenTelemetry-compatible
> logs backend, the easiest and recommended way is using an OpenTelemetry protocol (OTLP)
> exporter." [30]

### 2. File / Stdout — Fallback

> "In the file or stdout workflow, logs are written to files or standout output. Another
> component (e.g. FluentBit) is responsible for reading / tailing the logs, parsing them
> to more structured format, and forwarding them a target." [30]

> "It requires that all log fields required down stream are encoded into the logs, and
> that the component reading the logs parse the data into the log data model." [30]

## Best Practice: Use a Collector

> "It is a best practice to send telemetry from containers to an OpenTelemetry Collector
> instead of directly to a backend. The Collector helps simplify secret management,
> decouples data export problems from your apps, and lets you add additional data to
> your telemetry." [38]

## Trace Context in Each Approach

### OTLP Approach
When using the OTEL SDK with OTLP export, trace context is **automatically correlated** [1]:
> "OpenTelemetry automatically correlates your logs and traces." [1]

TraceID and SpanID are first-class fields in the OTLP log record, requiring no parsing.

### Stdout Approach
For non-OTLP formats, trace_id and span_id must be recorded as top-level JSON fields [31]:
> "For structured formats, trace_id and span_id fields should be recorded as top-level
> fields in JSON structures." [31]

The stdout approach has a disadvantage [30]:
> "It requires that all log fields required down stream are encoded into the logs."

The log collector must then parse these fields, adding complexity and fragility.

## Recommended Kubernetes Architecture

The OTEL project recommends two Collector instances for Kubernetes [33]:
1. **DaemonSet** — node-level telemetry (logs, host metrics, container metrics)
2. **Deployment** — cluster-level data (events, cluster metrics)

The k8sattributesprocessor enriches telemetry with pod metadata, ensuring consistent
correlation across signals [32].

## OpenShift-Specific Architecture Options

### Option A: Structured JSON to Stdout + Logging Operator (Vector)

```
Python App (logging + OTEL correlation)
    → structured JSON to stdout
    → Vector (DaemonSet, managed by Logging Operator)
        → parse: json in ClusterLogForwarder
        → LokiStack
```

**How it works:**
- Python app uses `OTEL_PYTHON_LOG_CORRELATION=true` to inject trace_id/span_id
  into log format strings [5]
- App writes structured JSON to stdout with trace context as top-level fields
- Vector collects from `/var/log/containers` [17]
- ClusterLogForwarder with `parse: json` extracts structured fields [39]
- Forwarded to LokiStack or other backends

**Pros:**
- No additional operators needed beyond the Logging Operator
- Works with existing Logging Operator + LokiStack setup
- Simple deployment — no sidecar or additional DaemonSet

**Cons:**
- Trace context must be explicitly formatted into log output [31]
- Log collector must parse JSON — adds processing overhead and fragility [30]
- No automatic OTEL resource attributes (k8s metadata must come from Vector)
- OTEL data model fidelity is lost in the JSON → parse → forward pipeline [30]

### Option B: OTLP to OTEL Collector → LokiStack

```
Python App (OTEL SDK)
    → OTLP (gRPC/HTTP)
    → OTEL Collector (DaemonSet, managed by OTEL Operator)
        → k8sattributesprocessor enrichment
        → LokiStack OTLP endpoint
```

**How it works:**
- Python app uses `OTLPLogExporter` to send logs via OTLP [9][10]
- OTEL Collector receives on port 4317/4318 [13]
- k8sattributesprocessor adds pod metadata [32]
- Collector forwards to LokiStack OTLP endpoint [27]
- LokiStack in `openshift-logging` mode applies default attribute mappings [20]

**Pros:**
- Full OTEL data model fidelity — no lossy parsing [8]
- Automatic trace correlation — trace_id/span_id are native fields [1]
- k8sattributesprocessor ensures consistent metadata across all signals [32]
- Unified pipeline for logs, traces, and metrics
- Better query performance with OTLP labels vs JSON parsing [23]

**Cons:**
- Requires OTEL Operator + Loki Operator (+ COO for OTLP ingestion) [21][27]
- OTLP output from CLF is Technology Preview [19]
- Additional infrastructure (OTEL Collector DaemonSet)
- More operators to manage and upgrade

### Option C: Hybrid — Both Stdout and OTLP

```
Python App (OTEL SDK)
    ├→ structured JSON to stdout (for Logging Operator / legacy consumers)
    └→ OTLP to OTEL Collector (for full OTEL pipeline)
```

Use when migrating incrementally or when both pipelines are needed.

## Red Hat's Direction

Red Hat is positioning OpenShift as an "OTLP-native platform" [28]:
> "This architecture helps avoid vendor lock-in, and provides unified cross-signal
> capabilities for data collection, processing and forwarding to the observability
> backend." [28]

The default data model for LokiStack is currently ViaQ but **will change to
OpenTelemetry in future releases** [22].

Auto-instrumentation is available via the OTEL Operator [29][37]:
- Annotation: `instrumentation.opentelemetry.io/inject-python: "true"` [37]
- Default protocol: `http/protobuf` [37]
- Python logs auto-instrumentation is **disabled by default** [37]

## Decision Framework

| Factor | Stdout + Logging Op | OTLP + OTEL Collector |
|---|---|---|
| Operator complexity | Low (1 operator) | High (+ OTEL Op + Loki Op + COO) |
| Data model fidelity | Lossy (JSON parsing) | Full (native OTLP) |
| Trace correlation | Manual (format strings) | Automatic |
| Cross-signal correlation | Limited | Full (k8sattributes) |
| Maturity on OpenShift | GA | OTLP output is Tech Preview |
| Red Hat's future direction | Legacy (ViaQ) | Strategic (OTLP-native) |
| Infrastructure overhead | None (uses existing DaemonSet) | Additional DaemonSet |

## Gaps and Limitations

- The OTLP path through OpenShift logging is still maturing — OTLP output from
  the CLF is Technology Preview [19][21]
- Python logs auto-instrumentation must be explicitly enabled on the Kubernetes
  operator [37]
- No File Exporter in the Python SDK for writing OTLP JSON to stdout [11]
- The hybrid approach adds operational complexity with two parallel pipelines
