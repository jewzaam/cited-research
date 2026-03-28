# Reference: OTEL Collector on OpenShift — Architecture

Covers deployment options and trade-offs for the OTEL Collector on OpenShift.
All citations reference [../citations.md](../citations.md).

---

## Red Hat Build of OpenTelemetry

Red Hat provides a supported distribution of the OTEL Collector via the "Red Hat build
of OpenTelemetry" operator [24]:

> "The Red Hat build of OpenTelemetry Operator uses a custom resource definition (CRD)
> file that defines the architecture and configuration settings to be used when creating
> and deploying the Red Hat build of OpenTelemetry resources." [24]

Installation: install operator → create namespace → create `OpenTelemetryCollector` CR [24].

## Deployment Modes

| Mode | Description | Use Case |
|---|---|---|
| Deployment | Standard deployment (default) | Gateway/aggregation layer |
| DaemonSet | One pod per node | Node-level log/metric collection |
| StatefulSet | Stateful deployment | Persistent processing state |
| Sidecar | One pod per application pod | Per-pod collection, in-container file access |

[24][26]

### DaemonSet

> "If you need to scrape telemetry data from every node, for example by using the
> Collector's Filelog Receiver to read container logs, use the DaemonSet deployment
> mode." [26]

The DaemonSet Collector scrapes pod logs from `/var/log/pods/*` [28].

### Sidecar

> "If you need access to log files inside a container, inject the Collector as a
> sidecar, and use the Collector's Filelog Receiver and a shared volume such as
> emptyDir." [26]

Injection triggered by annotation: `sidecar.opentelemetry.io/inject: "true"` [24].

## DaemonSet vs Sidecar Trade-offs

| Factor | DaemonSet | Sidecar |
|---|---|---|
| Resource efficiency | Better (one per node) | Worse (one per pod) |
| Blast radius | Larger (node-wide) | Smaller (single pod) |
| gRPC load balancing | Needs gRPC-specific LB | Natural per-pod balancing |
| Fault isolation | Lower | Higher |
| k8sattributesprocessor cost | One API call set per node | One per pod — expensive at scale |
| Popularity (2026 survey) | 50% | 23% |

[34][35][36]

> "When the number of nodes is low and the number of pods is high, Sidecars might make
> more sense, as you'll get a better load balancing for the gRPC connections among
> Collector layers without needing a gRPC-specific load balancer." [34]

> "If you're running as a sidecar with the k8sattributesprocessor on 10k pods, that's
> 10k API calls made to the K8s API. That's expensive." [34]

## Collector Capabilities

The Collector can [35]:

| Capability | Details |
|---|---|
| Receive OTLP | gRPC on 4317, HTTP on 4318 |
| Export to stdout | `debug` exporter |
| Export to files | OTLP JSON format |
| Export via OTLP | Forward to other collectors or backends |
| Export to Loki | Via `openshift-logging` tenants mode |

## Forwarding to LokiStack

The OTEL Collector can forward logs to a LokiStack instance [27]:

> "You can deploy the OpenTelemetry Collector to forward logs to a LokiStack instance
> by using the openshift-logging tenants mode." [27]

Prerequisites: OTEL Operator + Loki Operator + supported LokiStack instance [27].

LokiStack automatically applies default OTLP attribute mappings in `openshift-logging`
mode [20]:

> "When you set the Loki Operator to the openshift-logging mode, it automatically
> applies a default set of attribute mappings that align specific OTLP attributes with
> stream labels and structured metadata of Loki." [20]

## Filelog Receiver

The Filelog Receiver tails and parses logs from files [32]:

> "The Filelog Receiver collects Kubernetes logs and application logs written to
> stdout/stderr [...] by tailing the logs Kubernetes writes to
> `/var/log/pods/*/*/*.log`." [32]

- Reached GA in the Red Hat build [24]
- Can be used as sidecar container or DaemonSet [24]
- Container parser operator simplifies configuration [32]

## k8sattributesprocessor

> "The Kubernetes Attributes Processor automatically discovers Kubernetes pods, extracts
> their metadata, and adds the extracted metadata to spans, metrics, and logs as resource
> attributes. It is one of the most important components for a collector running in
> Kubernetes." [32]

> "The Collector guarantees that logs, traces and metrics have precisely the same
> attribute names and values describing the Kubernetes Pod that they come from. This
> enables exact and unambiguous correlation of the signals by the Pod in the backend." [32]

## Gaps and Limitations

- OTLP output from the CLF (Vector-based) is Technology Preview [19][21]
- The OTEL Collector → LokiStack path requires both the OTEL Operator and Loki
  Operator [27]
- Sidecar mode with k8sattributesprocessor is prohibitively expensive at scale [34]
- No direct OTLP receiver input into the ClusterLogForwarder [22]
