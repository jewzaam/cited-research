# Reference: OpenShift Logging Stack Compatibility

Covers how the OpenShift Logging Operator collects and forwards logs, and its
relationship with OpenTelemetry. All citations reference [../citations.md](../citations.md).

---

## Cluster Logging Operator (CLO)

The CLO provides APIs to control collection and forwarding of logs from all pods and
nodes in a cluster [16]:

> "The Cluster Logging Operator (CLO) provides a set of APIs to control collection and
> forwarding of logs from all pods and nodes in a cluster. This includes application
> logs (from regular pods), infrastructure logs (from system pods and node logs), and
> audit logs." [16]

The CLO does not collect logs itself — it configures and manages the components that
do [16].

## Log Collector: Vector

| Fact | Detail | Source |
|---|---|---|
| Fluentd deprecated | Logging 5.6 | [18] |
| Fluentd removed | Logging 6.0 | [18] |
| Vector is the only supported collector | Logging 6.x | [18] |
| Collector deployment model | DaemonSet — one pod per node | [17] |

> "The Fluentd log collector implementation has been removed, and Vector is now the
> supported collection service." [18]

## How Logs Are Collected

The collector (Vector) runs as a DaemonSet, deploying pods to each OpenShift node.
It reads container logs from `/var/log/containers` (json-file log driver) or from
journald [17].

Three log categories [17]:

| Category | Sources |
|---|---|
| Application | User pods (all namespaces except system) |
| Infrastructure | `openshift-*`, `kube-*`, `default` namespaces + journald |
| Audit | auditd, kube-apiserver, openshift-apiserver |

## Expected Log Format

The logging stack collects **whatever containers write to stdout/stderr**. It supports
both plain text and JSON structured logging [39].

JSON parsing is configurable via the ClusterLogForwarder [39]:
> "You can use JSON logging to configure the Log Forwarding API to parse JSON strings
> into a structured object and forward them to either OpenShift Container Platform
> Logging-managed Elasticsearch or any other third-party system."

When `parse: json` is enabled, the JSON content is placed into a `structured` field
without modifying the original `message` field [39].

For Elasticsearch, `structuredTypeKey` or `structuredTypeName` is required to control
index creation [39].

## ClusterLogForwarder

In Logging 6.x, the API changed [18]:
- API group: `logging.openshift.io` → `observability.openshift.io`
- `ClusterLogForwarder` and `ClusterLogging` merged into a single `ClusterLogForwarder` resource

The CR structure includes `spec.outputs`, `spec.inputs`, `spec.filters`, `spec.pipelines`,
and `spec.serviceAccount` [22].

Receiver inputs supported: HTTP (audit logs) and syslog (journal format infrastructure
logs) [22].

## Supported Output Backends

| Output Type | Notes |
|---|---|
| `azureMonitor` | Azure Monitor Logs |
| `cloudwatch` | AWS CloudWatch |
| `elasticsearch` | Elasticsearch / OpenSearch |
| `googleCloudLogging` | GCP Cloud Logging |
| `http` | Generic HTTP endpoint |
| `kafka` | Apache Kafka |
| `loki` | Loki (direct) |
| `lokistack` | LokiStack (managed by Loki Operator) |
| `otlp` | OpenTelemetry Protocol (**Technology Preview**) |
| `splunk` | Splunk |
| `syslog` | Syslog |

[19]

## OTLP Support

OTLP output in the ClusterLogForwarder is **Technology Preview** across Logging
6.1–6.4 [19][21]:

> "The OpenTelemetry Protocol (OTLP) output log forwarder is a Technology Preview
> feature only. Technology Preview features are not supported with Red Hat production
> service level agreements (SLAs)." [19]

Requires annotation: `observability.openshift.io/tech-preview-otlp-output: "enabled"` [19]

The OTLP output uses the **OpenTelemetry data model** (not ViaQ) and adheres to
OpenTelemetry Semantic Conventions [21].

LokiStack supports OTLP data ingestion via `lokiStack.dataModel: Otel` [22]:
> "The dataModel field is optional and left unset by default, which allows the CLO
> to automatically select a data model. Currently, the CLO defaults to the ViaQ model
> when the field is unset, but this will change in future releases." [22]

OTLP ingestion with LokiStack requires: Logging Operator + Loki Operator + Cluster
Observability Operator (COO) [21].

## Red Hat OpenTelemetry Operator

Red Hat provides the "Red Hat build of OpenTelemetry" operator separately [24]:
- Uses a CRD (`OpenTelemetryCollector`) to deploy Collector instances
- Deployment modes: Deployment, DaemonSet, StatefulSet, Sidecar [24]
- Filelog Receiver reached GA [24]
- Current version: 3.6.1 via Operator 0.127.0 (OCP 4.17) [25]

The two operators converge at the OTLP protocol [20]:
- Logging Operator (Vector) can output OTLP (Tech Preview)
- OTEL Collector can receive OTLP and forward to LokiStack

> "You can create an OpenTelemetryCollector custom resource (CR) object that receives
> logs via OTLP and forwards them to the Loki logging backend in the openshift-logging
> namespace." [20]

## OTEL Data Model on OpenShift

The OpenTelemetry data model defines resources with attributes [23]:
- `container_name`, `cluster_id`, `pod_name`, `namespace`, `deployment`
- Grouped under the resource object to reduce repetition

> "With OTLP, users can filter queries directly by labels rather than using JSON
> parsing, improving the speed and efficiency of queries." [23]

## Gaps and Limitations

- OTLP output from CLF is **Technology Preview**, not GA [19][21]
- Default data model is still ViaQ — OTEL model is opt-in [22]
- OTLP ingestion path requires three operators (Logging + Loki + COO) [21]
- HTTP and syslog are the only receiver input types for CLF — no direct OTLP
  receiver input into the CLF [22]
