# Reference: Python Logging + OTEL Integration

Covers how the Python standard `logging` module integrates with OpenTelemetry.
All citations reference [../citations.md](../citations.md).

---

## The Bridge Pattern

OpenTelemetry's Logs API is a **bridge API** — it is not meant for direct application
use. Unlike the Traces and Metrics APIs, there is no user-facing Logs API. Instead,
application developers continue using their existing logging library (Python's `logging`),
and the OTEL SDK bridges those log records into the OTEL data model [1].

> "There is a logs bridge API; however, it is different from the Traces and Metrics API,
> because it's not used by application developers to create logs." [1]

## LoggingHandler

The `LoggingHandler` is a `logging.Handler` subclass that bridges Python's `logging`
module into the OTEL log pipeline [2][3].

| Component | Import Path | Package |
|---|---|---|
| `LoggerProvider` | `opentelemetry.sdk._logs` | `opentelemetry-sdk` |
| `LoggingHandler` | `opentelemetry.sdk._logs` (deprecated) or `opentelemetry.instrumentation.logging` | `opentelemetry-sdk` / `opentelemetry-instrumentation-logging` |
| `BatchLogRecordProcessor` | `opentelemetry.sdk._logs.export` | `opentelemetry-sdk` |
| `ConsoleLogRecordExporter` | `opentelemetry.sdk._logs.export` | `opentelemetry-sdk` |
| `set_logger_provider` | `opentelemetry._logs` | `opentelemetry-api` |

As of Python SDK 1.40.0, the `opentelemetry-instrumentation-logging` contrib package
provides the handler and replaces the deprecated one in `opentelemetry-sdk` [4][5].

> "Prior to OpenTelemetry Python 1.40.0 you had to enable log instrumentation with
> `export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true`. This is no longer
> required." [4]

The `_logs` module is explicitly marked experimental [3]:
> "OpenTelemetry Python logs are in an experimental state, and the APIs within
> `opentelemetry.sdk._logs` are subject to change in minor/patch releases with no
> backward compatibility guarantees."

## Bridging Existing Code

Once the `LoggingHandler` is attached to Python's root logger (or any specific logger),
all standard `logging.getLogger(__name__).info(...)` calls are automatically captured
and converted to OTEL LogRecords. **No modification to existing logging statements is
required** [2].

```python
import logging
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor, ConsoleLogRecordExporter
from opentelemetry._logs import set_logger_provider

provider = LoggerProvider()
provider.add_log_record_processor(BatchLogRecordProcessor(ConsoleLogRecordExporter()))
set_logger_provider(provider)

handler = LoggingHandler(level=logging.INFO, logger_provider=provider)
logging.getLogger().addHandler(handler)

# Existing code works unchanged:
logger = logging.getLogger(__name__)
logger.info("This is now captured by OTEL")
```
[2]

## Log-Trace Correlation

Two distinct mechanisms exist:

### 1. Automatic correlation in OTEL LogRecords
The SDK automatically appends the SpanID and TraceID of the current active Span to
any logged events [4]:
> "The Span Event and the Log both have the same SpanID. The logging SDK appends the
> SpanID of the current Span to any logged events."

### 2. Format-string injection for non-OTEL outputs
For injecting trace context into Python log format strings (e.g., for stdout), set
`OTEL_PYTHON_LOG_CORRELATION=true` [5]. This registers a custom log record factory
adding these attributes to Python LogRecords:

| Attribute | Description |
|---|---|
| `otelTraceID` | 32-character hex string |
| `otelSpanID` | 16-character hex string |
| `otelServiceName` | Service name from OTEL resource |
| `otelTraceSampled` | Whether the trace is sampled |

Default format when correlation is enabled [5]:
```
%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d]
[trace_id=%(otelTraceID)s span_id=%(otelSpanID)s
resource.service.name=%(otelServiceName)s
trace_sampled=%(otelTraceSampled)s] - %(message)s
```

## Required Packages

| Package | Purpose |
|---|---|
| `opentelemetry-api` | API definitions, `set_logger_provider` |
| `opentelemetry-sdk` | SDK: `LoggerProvider`, processors, console exporter |
| `opentelemetry-instrumentation-logging` | Auto-instrumentation handler (contrib) |
| `opentelemetry-exporter-otlp` | Umbrella: installs gRPC + HTTP OTLP exporters |
| `opentelemetry-exporter-otlp-proto-grpc` | gRPC-specific OTLP exporter |
| `opentelemetry-exporter-otlp-proto-http` | HTTP-specific OTLP exporter |

[4][5][8]

## OTEL Logs Data Model vs Python LogRecord

The OTEL Logs data model defines these top-level fields [6]:

| Field | Type | Notes |
|---|---|---|
| `Timestamp` | nanoseconds | When the event occurred |
| `ObservedTimestamp` | nanoseconds | When the event was observed |
| `TraceId` | 16 random bytes | W3C trace context |
| `SpanId` | 8 random bytes | W3C trace context |
| `TraceFlags` | W3C flags | Sampling flag |
| `SeverityText` | string | e.g., "INFO", "ERROR" |
| `SeverityNumber` | integer | Lower = less severe |
| `Body` | AnyValue | Log message body |
| `Attributes` | key-value map | Structured metadata |
| `Resource` | key-value map | Entity producing telemetry |

The Python SDK's `LogRecord` accepts matching parameters: `timestamp`,
`observed_timestamp`, `trace_id`, `span_id`, `trace_flags`, `severity_text`,
`severity_number`, `body`, `attributes` [3].

## Gaps and Limitations

- The `opentelemetry.sdk._logs` module remains **experimental** — breaking changes
  possible in minor releases [3]
- The `opentelemetry-instrumentation-logging` package is the current recommended
  path but is relatively new (post-1.40.0) [4][5]
- Python logs auto-instrumentation via the Kubernetes operator is **disabled by
  default** and must be explicitly enabled [37]
