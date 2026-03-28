# Reference: OTEL Data Export Options for Python

Covers the available exporters for Python OpenTelemetry logs.
All citations reference [../citations.md](../citations.md).

---

## Console/Stdout Exporter

The `ConsoleLogRecordExporter` outputs log records to stdout [7].

> "The 'Standard output' LogRecord Exporter is a LogRecord Exporter which outputs
> the logs to stdout/console. This exporter is intended for debugging and learning
> purposes. It is not recommended for production use. The output format is not
> standardized and can change at any time." [7]

- Import: `from opentelemetry.sdk._logs.export import ConsoleLogRecordExporter`
- The older name `ConsoleLogExporter` is deprecated [7]
- Output is human-readable but unstandardized — not suitable for machine parsing

## OTLP Exporter (gRPC)

| Property | Value |
|---|---|
| Package | `opentelemetry-exporter-otlp-proto-grpc` |
| Import | `from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter` |
| Default port | 4317 |
| Path suffix | None (gRPC handles routing) |
| Protocol value | `grpc` |

[9][13]

## OTLP Exporter (HTTP)

| Property | Value |
|---|---|
| Package | `opentelemetry-exporter-otlp-proto-http` |
| Import | `from opentelemetry.exporter.otlp.proto.http._log_exporter import OTLPLogExporter` |
| Default port | 4318 |
| Path suffix | `/v1/logs` (auto-appended by SDK when using base endpoint) |
| Protocol value | `http/protobuf` or `http/json` |

[10][13]

> "For HTTP (4318), include the path `/v1/traces`, `/v1/metrics`, or `/v1/logs`.
> For gRPC (4317), do not include the path." [10]

## Umbrella Package

`opentelemetry-exporter-otlp` installs both gRPC and HTTP exporters [8].

## File Exporter

The OTLP File Exporter specification exists but is in an early stage [11]. It describes
serialization to OTLP JSON format. **There is no dedicated `FileLogExporter` class in
the Python SDK.**

Use cases from the spec [11]:
- FaaS environments where OTLP network export is unavailable
- Kubernetes environments where "logs are often scraped from the stdout pod file"

Files must contain exactly one signal type (traces, metrics, or logs) [11].

## Direct Export Without a Collector

Applications can export directly to any OTLP-compatible backend without using a
Collector [12]:

> "The most direct deployment pattern doesn't use a Collector at all. In this approach,
> applications instrumented with an OpenTelemetry SDK export telemetry signals (traces,
> metrics, and logs) straight to a backend." [12]

The dedicated `opentelemetry-exporter-jaeger` package is deprecated as of July 2023;
use OTLP instead [15].

## Environment Variables

| Variable | Purpose | Default |
|---|---|---|
| `OTEL_EXPORTER_OTLP_ENDPOINT` | Base endpoint for all signals | `localhost:4317` (gRPC) / `localhost:4318` (HTTP) |
| `OTEL_EXPORTER_OTLP_LOGS_ENDPOINT` | Per-signal override for logs | — |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | Wire format: `grpc`, `http/protobuf`, `http/json` | SDK-dependent |
| `OTEL_EXPORTER_OTLP_LOGS_PROTOCOL` | Logs-specific protocol override | — |
| `OTEL_EXPORTER_OTLP_HEADERS` | Key-value headers for all signals | — |
| `OTEL_EXPORTER_OTLP_LOGS_HEADERS` | Logs-specific headers | — |
| `OTEL_EXPORTER_OTLP_TIMEOUT` | Timeout in milliseconds | — |
| `OTEL_EXPORTER_OTLP_INSECURE` | Disable TLS for gRPC | `false` |
| `OTEL_EXPORTER_OTLP_CERTIFICATE` | TLS certificate path | — |
| `OTEL_LOGS_EXPORTER` | Select logs exporter (`otlp`, `console`) | `otlp` |

[13]

Python-specific environment variables [14]:

| Variable | Purpose |
|---|---|
| `OTEL_PYTHON_LOG_CORRELATION` | Enable trace context injection into log records |
| `OTEL_PYTHON_LOG_FORMAT` | Custom log format string |
| `OTEL_PYTHON_LOG_LEVEL` | Minimum log level for OTEL handler |

## OTLP Wire Formats

Three supported formats [13]:

| Format | Description |
|---|---|
| `grpc` | Protobuf-encoded data using gRPC wire format over HTTP/2 |
| `http/protobuf` | Protobuf-encoded data over HTTP |
| `http/json` | JSON-encoded data over HTTP |

> "OpenTelemetry Protocol (OTLP) exporters are designed with the OpenTelemetry data
> model in mind, emitting OTel data without any loss of information." [8]

## Gaps and Limitations

- No production-ready file exporter in the Python SDK — the spec exists but
  implementation is early-stage [11]
- ConsoleLogRecordExporter output format is unstandardized and can change [7]
- The deprecated `ConsoleLogExporter` name may still appear in older tutorials
