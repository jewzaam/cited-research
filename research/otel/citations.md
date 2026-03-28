# Citations

All sources visited in-session via WebSearch/WebFetch. Each entry records the URL,
access context, and specific data extracted.

---

## [1] OpenTelemetry — Logs Concept
- **URL:** https://opentelemetry.io/docs/concepts/signals/logs/
- **Type:** Official OTEL documentation
- **Data extracted:** Logs Bridge API concept — not for direct application use; bridges existing logging libraries into the OTEL data model. Automatic trace/log correlation.

## [2] OpenTelemetry Blog — Logs Collection (2023)
- **URL:** https://opentelemetry.io/blog/2023/logs-collection/
- **Type:** Official OTEL blog
- **Data extracted:** `LoggingHandler` code example, bridge pattern explanation, `LoggerProvider` + `BatchLogRecordProcessor` + `ConsoleLogRecordExporter` setup.

## [3] OpenTelemetry Python SDK — _logs module
- **URL:** https://opentelemetry-python.readthedocs.io/en/stable/sdk/_logs.html
- **Type:** Official Python SDK docs (readthedocs)
- **Data extracted:** Experimental status of `opentelemetry.sdk._logs`, `LogRecord` class parameters, `ReadableLogRecord` and `ReadWriteLogRecord` variants.

## [4] OpenTelemetry — Zero-Code Python Logs Example
- **URL:** https://opentelemetry.io/docs/zero-code/python/logs-example/
- **Type:** Official OTEL documentation
- **Data extracted:** Auto-instrumentation no longer requires `OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true` as of Python SDK 1.40.0. SpanID appended to logged events.

## [5] opentelemetry-instrumentation-logging (contrib)
- **URL:** https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/logging/logging.html
- **Type:** Official Python contrib docs
- **Data extracted:** `OTEL_PYTHON_LOG_CORRELATION=true` enables trace context injection. Default log format with `otelTraceID`, `otelSpanID`, `otelServiceName`, `otelTraceSampled` placeholders. Replaces deprecated handler in SDK.

## [6] OpenTelemetry — Logs Data Model Specification
- **URL:** https://opentelemetry.io/docs/specs/otel/logs/data-model/
- **Type:** Official OTEL specification
- **Data extracted:** Top-level fields: Timestamp, ObservedTimestamp, TraceId, SpanId, TraceFlags, SeverityText, SeverityNumber, Body, Attributes, Resource. SeverityNumber semantics. Body supports AnyValue. TraceId is 16 random bytes.

## [7] OpenTelemetry — Stdout Log Exporter Specification
- **URL:** https://opentelemetry.io/docs/specs/otel/logs/sdk_exporters/stdout/
- **Type:** Official OTEL specification
- **Data extracted:** ConsoleLogRecordExporter outputs to stdout/console. Intended for debugging/learning, not production. Output format not standardized.

## [8] OpenTelemetry Python — Exporters
- **URL:** https://opentelemetry.io/docs/languages/python/exporters/
- **Type:** Official OTEL documentation
- **Data extracted:** Package installation patterns. OTLP exporters emit data without loss of information from the OTEL data model.

## [9] OpenTelemetry Python — OTLP Exporter Docs
- **URL:** https://opentelemetry-python.readthedocs.io/en/latest/exporter/otlp/otlp.html
- **Type:** Official Python SDK docs
- **Data extracted:** gRPC exporter `OTLPLogExporter` from `opentelemetry.exporter.otlp.proto.grpc._log_exporter`. Default port 4317.

## [10] OpenTelemetry Python — OTLP HTTP Log Exporter Source
- **URL:** https://opentelemetry-python.readthedocs.io/en/latest/_modules/opentelemetry/exporter/otlp/proto/http/_log_exporter.html
- **Type:** Official Python SDK source docs
- **Data extracted:** HTTP exporter from `opentelemetry.exporter.otlp.proto.http._log_exporter`. Default port 4318. HTTP requires `/v1/logs` path suffix.

## [11] OpenTelemetry — OTLP File Exporter Specification
- **URL:** https://opentelemetry.io/docs/specs/otel/protocol/file-exporter/
- **Type:** Official OTEL specification
- **Data extracted:** Serialization to OTLP JSON format. Use cases include FaaS and Kubernetes log scraping from stdout. Files must contain one type of data. Early/placeholder stage.

## [12] OpenTelemetry — No Collector Deployment
- **URL:** https://opentelemetry.io/docs/collector/deploy/other/no-collector/
- **Type:** Official OTEL documentation
- **Data extracted:** Applications can export directly to OTLP-compatible backends without a Collector.

## [13] OpenTelemetry — OTLP Exporter Configuration
- **URL:** https://opentelemetry.io/docs/languages/sdk-configuration/otlp-exporter/
- **Type:** Official OTEL documentation
- **Data extracted:** Environment variables: `OTEL_EXPORTER_OTLP_ENDPOINT`, `OTEL_EXPORTER_OTLP_LOGS_ENDPOINT`, `OTEL_EXPORTER_OTLP_PROTOCOL`, `OTEL_LOGS_EXPORTER`, etc. Default endpoints 4317 (gRPC), 4318 (HTTP). SDK auto-appends `/v1/logs` for HTTP. Wire formats: grpc, http/protobuf, http/json.

## [14] OpenTelemetry — Python Zero-Code Configuration
- **URL:** https://opentelemetry.io/docs/zero-code/python/configuration/
- **Type:** Official OTEL documentation
- **Data extracted:** Python-specific env vars: `OTEL_PYTHON_LOG_CORRELATION`, `OTEL_PYTHON_LOG_FORMAT`, `OTEL_PYTHON_LOG_LEVEL`.

## [15] pypi.org — opentelemetry-exporter-jaeger (deprecated)
- **URL:** https://pypi.org/project/opentelemetry-exporter-jaeger/
- **Type:** PyPI package page
- **Data extracted:** Jaeger exporter deprecated; use OTLP instead. Support ended July 2023.

## [16] GitHub — cluster-logging-operator
- **URL:** https://github.com/openshift/cluster-logging-operator
- **Type:** GitHub repository
- **Data extracted:** CLO provides APIs to control collection/forwarding of logs. Does not collect logs itself — starts, configures, monitors components. Three log types: application, infrastructure, audit.

## [17] Red Hat Docs — OCP 4.14 Logging
- **URL:** https://docs.redhat.com/en/documentation/openshift_container_platform/4.14/html/logging/cluster-logging
- **Type:** Official Red Hat documentation
- **Data extracted:** Collector is a DaemonSet deploying pods to each node. Three log categories: application, infrastructure, audit.

## [18] Red Hat Docs — OpenShift Logging 6.0 Upgrading
- **URL:** https://docs.redhat.com/en/documentation/red_hat_openshift_logging/6.0/html-single/upgrading_logging/index
- **Type:** Official Red Hat documentation
- **Data extracted:** Fluentd deprecated in 5.6, removed in 6.0. Vector is the only supported collector. API changed from `logging.openshift.io` to `observability.openshift.io`.

## [19] Red Hat Docs — OpenShift Logging 6.1 Configuring
- **URL:** https://docs.redhat.com/en/documentation/red_hat_openshift_logging/6.1/html-single/configuring_logging/index
- **Type:** Official Red Hat documentation
- **Data extracted:** Supported output types: azureMonitor, cloudwatch, elasticsearch, googleCloudLogging, http, kafka, loki, lokistack, otlp, splunk, syslog. OTLP output is Technology Preview.

## [20] Red Hat Docs — OpenShift Logging 6.1 LokiStack OTLP
- **URL:** https://docs.redhat.com/en/documentation/red_hat_openshift_logging/6.1/html/configuring_logging/configuring-lokistack-otlp
- **Type:** Official Red Hat documentation
- **Data extracted:** OpenTelemetryCollector CR can receive OTLP and forward to LokiStack. Default OTLP attribute mappings applied automatically in `openshift-logging` mode.

## [21] Red Hat Docs — OpenShift Logging 6.2 Log Forwarding
- **URL:** https://docs.redhat.com/en/documentation/red_hat_openshift_logging/6.2/html/configuring_logging/configuring-log-forwarding
- **Type:** Official Red Hat documentation
- **Data extracted:** OTLP output is Technology Preview, requires annotation. OTLP uses OpenTelemetry data model (not ViaQ). OTLP ingestion with LokiStack requires Logging Operator + Loki Operator + COO.

## [22] Red Hat Docs — OpenShift Logging 6.3 Log Forwarding
- **URL:** https://docs.redhat.com/en/documentation/red_hat_openshift_logging/6.3/html/configuring_logging/configuring-log-forwarding
- **Type:** Official Red Hat documentation
- **Data extracted:** CLF supports HTTP and syslog receiver inputs. `lokiStack.dataModel` can be set to `Otel`. Default data model is ViaQ but will change to OpenTelemetry in future releases.

## [23] Red Hat Docs — OpenShift Logging 6.3 OpenTelemetry Data Model
- **URL:** https://docs.redhat.com/en/documentation/red_hat_openshift_logging/6.3/html/configuring_logging/opentelemetry-data-model
- **Type:** Official Red Hat documentation
- **Data extracted:** OTEL data model defines resources with attributes (container_name, cluster_id, pod_name, namespace, deployment). OTLP queries filter by labels instead of JSON parsing — better performance.

## [24] Red Hat Docs — OCP 4.16 Red Hat build of OpenTelemetry
- **URL:** https://docs.redhat.com/en/documentation/openshift_container_platform/4.16/html-single/red_hat_build_of_opentelemetry/index
- **Type:** Official Red Hat documentation
- **Data extracted:** Operator uses CRD. Deployment modes: Deployment, DaemonSet, StatefulSet, Sidecar. Filelog Receiver reached GA. Sidecar injection annotation.

## [25] Red Hat Docs — OCP 4.17 Red Hat build of OpenTelemetry
- **URL:** https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html-single/red_hat_build_of_opentelemetry/index
- **Type:** Official Red Hat documentation
- **Data extracted:** Red Hat build of OpenTelemetry 3.6.1 via Operator 0.127.0. Sidecar injection for auto-instrumentation.

## [26] Red Hat Docs — OCP 4.12 Configuring the Collector
- **URL:** https://docs.redhat.com/en/documentation/openshift_container_platform/4.12/html/red_hat_build_of_opentelemetry/configuring-the-collector
- **Type:** Official Red Hat documentation
- **Data extracted:** Deployment modes: deployment, daemonset, statefulset, sidecar. DaemonSet for node-level scraping (Filelog Receiver). Sidecar for in-container file access via shared volume.

## [27] Red Hat Docs — OCP 4.19 Forwarding Telemetry Data
- **URL:** https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/red_hat_build_of_opentelemetry/otel-forwarding-telemetry-data
- **Type:** Official Red Hat documentation
- **Data extracted:** OTEL Collector can forward logs to LokiStack in `openshift-logging` tenants mode. Prerequisites: OTEL Operator + Loki Operator + supported LokiStack.

## [28] Red Hat Blog — OpenShift as OTLP Native Platform
- **URL:** https://www.redhat.com/en/blog/red-hat-openshift-opentelemetry-otlp-native-platform
- **Type:** Red Hat blog
- **Data extracted:** Architecture: OTEL Collector as centralized collection layer forwarding to Tempo (traces), Prometheus (metrics), Loki (logs). DaemonSet with FileLog receiver scrapes `/var/log/pods/*`.

## [29] Red Hat Developer — Auto-instrumentation with OpenTelemetry (Feb 2026)
- **URL:** https://developers.redhat.com/articles/2026/02/25/how-use-auto-instrumentation-opentelemetry
- **Type:** Red Hat Developer article
- **Data extracted:** Guide for auto-instrumentation without code changes on OpenShift.

## [30] OpenTelemetry — Logs Specification
- **URL:** https://opentelemetry.io/docs/specs/otel/logs/
- **Type:** Official OTEL specification
- **Data extracted:** Two workflows: direct-to-collector (OTLP, recommended, simplest) and file/stdout (fallback). Stdout requires all fields encoded into logs and parsed by collector.

## [31] OpenTelemetry — Trace Context in Non-OTLP Log Formats
- **URL:** https://opentelemetry.io/docs/specs/otel/compatibility/logging_trace_context/
- **Type:** Official OTEL specification
- **Data extracted:** For structured non-OTLP formats, trace_id and span_id should be top-level JSON fields.

## [32] OpenTelemetry — Kubernetes Collector Components
- **URL:** https://opentelemetry.io/docs/platforms/kubernetes/collector/components/
- **Type:** Official OTEL documentation
- **Data extracted:** Filelog Receiver collects stdout/stderr by tailing `/var/log/pods/*/*/*.log`. k8sattributesprocessor enriches telemetry with pod metadata. Collector guarantees consistent attribute names across signals.

## [33] OpenTelemetry — Kubernetes Getting Started
- **URL:** https://opentelemetry.io/docs/platforms/kubernetes/getting-started/
- **Type:** Official OTEL documentation
- **Data extracted:** Recommended pattern: DaemonSet for node-level telemetry + Deployment for cluster-level data.

## [34] OpenTelemetry — Collector Scaling
- **URL:** https://opentelemetry.io/docs/collector/scaling/
- **Type:** Official OTEL documentation
- **Data extracted:** Sidecar better for gRPC load balancing and fault isolation. Running k8sattributesprocessor as sidecar on 10k pods is expensive.

## [35] OpenTelemetry — Collector Deployment
- **URL:** https://opentelemetry.io/docs/collector/deploy/
- **Type:** Official OTEL documentation
- **Data extracted:** DaemonSet vs sidecar trade-offs. DaemonSet has larger blast radius; sidecar has higher resource cost.

## [36] OpenTelemetry Blog — Collector Survey 2026
- **URL:** https://opentelemetry.io/blog/2026/otel-collector-follow-up-survey-analysis/
- **Type:** Official OTEL blog
- **Data extracted:** Kubernetes deployment modes: 58% gateway, 50% DaemonSet, 23% sidecar, 14% StatefulSet.

## [37] OpenTelemetry — Python Operator Auto-instrumentation
- **URL:** https://opentelemetry.io/docs/zero-code/python/operator/
- **Type:** Official OTEL documentation
- **Data extracted:** Annotation `instrumentation.opentelemetry.io/inject-python: "true"` enables auto-instrumentation. Default protocol: http/protobuf. Python logs auto-instrumentation disabled by default.

## [38] OpenTelemetry — Best Practices (Collector)
- **URL:** https://opentelemetry.io/docs/platforms/kubernetes/getting-started/
- **Type:** Official OTEL documentation
- **Data extracted:** Best practice to send telemetry to Collector rather than directly to backend. Collector simplifies secret management, decouples export problems from apps.
- **Note:** Quote also appears on the Kubernetes Operator automatic instrumentation page.

## [39] Red Hat Docs — OCP 4.10 JSON Logging
- **URL:** https://docs.redhat.com/en/documentation/openshift_container_platform/4.10/html/logging/cluster-logging-enabling-json-logging
- **Type:** Official Red Hat documentation
- **Data extracted:** `parse: json` in ClusterLogForwarder parses JSON strings into structured objects. Requires `structuredTypeKey` or `structuredTypeName` for Elasticsearch.

## [40] OpenTelemetry Blog — Collecting OTel-Compliant Java Logs from Files (2024)
- **URL:** https://opentelemetry.io/blog/2024/collecting-otel-compliant-java-logs-from-files/
- **Type:** Official OTEL blog
- **Data extracted:** OTLP JSON format is verbose but offers contextualized logs correlatable with traces and metrics.
