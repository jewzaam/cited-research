Research `Tines` as a workflow orchestration platform for a personal AI-assisted engineering assistant. Produce a citation-backed analysis.

### Context — What We Need

I run a personal assistant (PA) backed by Claude Code that handles scheduled engineering tasks: email review, GitHub PR monitoring, JIRA comment checks, meeting transcript mining, PIA approval polling. The PA currently uses sandboxed `claude -p` subprocesses launched by a bash script for background tasks. Custom CLI tools handle domain logic: `gws` (Google Workspace CLI), `gh` (GitHub CLI), `calendar-fetcher`, `meet-summarize-query`.

I am evaluating whether a workflow engine should replace or complement the current bash-based task scheduler. This is for **personal use on a home workstation** (Fedora Linux, Podman available). Not enterprise deployment.

I already evaluated n8n hands-on. The analysis at ~/source/cited-research/research/n8n/ is the benchmark for depth and structure. I also have an internal comparison spreadsheet (stale, use as context not authority) that evaluated: Temporal, ActivePieces, Serverless Workflow, Argo Workflows, Cadence, Windmill, Kestra, Prefect, n8n, Hatchet, Workato, Apache Airflow. Key data from that sheet for `Tines`:

**From internal comparison (stale — verify against current sources):**
- Check the sheet data provided below for `Tines`'s row entries on: HA, integrations, license, hosted/local, durable execution, MCP integration, REST API, deployment, secrets, pauseability, primary use case, workflow language, debugging, logging.

### Requirements (ranked by importance)

1. **Shell script / CLI execution** — must run arbitrary CLI commands (`gws gmail +triage`, `gh pr list`, custom Python scripts). Domain logic lives in existing tools. This is the #1 non-negotiable.
2. **Credential isolation** — the PA (an LLM) must never hold credentials. The engine manages secrets. PA triggers workflows by ID/webhook without accessing auth.
3. **Self-hosted on a single workstation** — Fedora Linux, Podman, no Kubernetes. Low resource footprint (runs alongside dev tools).
4. **API-driven management** — create, update, trigger, monitor workflows via REST API.
5. **Scheduling** — cron-style triggers (daily, every 30 min, weekly Monday).
6. **Execution history** — what ran, when, what failed, with per-step detail.
7. **Retry and error handling** — automatic retry with backoff on transient failures.
8. **Webhook triggers** — HTTP-triggered workflow execution.
9. **Licensing** — report the license. OSI-approved preferred. Flag restrictions but don't block on this.
10. **AI/LLM integration** — nice to have, not required. The PA is the LLM layer; the engine just runs deterministic pipelines.

### Dimensions to Cover

Cover each dimension below. Be specific — "yes" is not an answer; show how.

1. **What it is** — one paragraph. What it does, who made it, architecture overview.
2. **Licensing** — license type, OSI compliance, personal use implications.
3. **Self-hosting** — deployment method (Docker/Podman/binary), resource requirements (idle RAM, recommended specs), single-host viability.
4. **CLI/Script execution** — can it run shell commands? How (native node, container exec, subprocess)? Can it capture stdout/stderr and pass output to the next step?
5. **Credential management** — how secrets are stored (encrypted? at rest?). Can an API user trigger workflows that use credentials without seeing them?
6. **Scheduling** — cron support, interval triggers, timezone handling.
7. **API for workflow management** — CRUD operations on workflows, trigger execution, query execution status, list executions. REST or gRPC?
8. **Webhook support** — can external callers trigger workflows via HTTP? Auth options.
9. **Execution history and debugging** — is execution data persisted? Per-step input/output inspection? Retention policy?
10. **Retry and error handling** — built-in retry? Configurable backoff? Dead letter queues? Error notification hooks?
11. **AI/LLM integration** — native LLM nodes? MCP support? Or just "run a script"?
12. **Community and maturity** — GitHub stars, project age, release cadence, contributor count, notable adopters.
13. **Limitations and gaps** — what doesn't it do well relative to our requirements?
14. **Comparison to n8n** — direct comparison on each dimension. Stronger, weaker, or equivalent. Reference the n8n analysis at ~/source/cited-research/research/n8n/.
15. **Verdict** — given the requirements above, is this worth evaluating hands-on? One paragraph.

### Internal Comparison Sheet Data (stale — verify)

| Dimension | Temporal | ActivePieces | Windmill | Kestra | Prefect | Hatchet |
|-----------|----------|-------------|----------|--------|---------|---------|
| HA | Yes | Yes | Yes | Yes | Yes | Yes |
| Integrations | Code (Activities/SDKs) | Hundreds (Pieces) | Hundreds (scripts) | Hundreds (plugins) | Hundreds (Collections) | Code (Steps/SDKs) |
| License | MIT | MIT | AGPL-3.0 | Apache-2.0 | Apache-2.0 | Apache-2.0 |
| Hosted/Local | Both | Both | Both | Both | Both | Both |
| Durable Execution | Yes (event sourcing) | Yes (DB) | Yes (DB) | Yes (DB + queue) | Yes (DB) | Yes (event sourcing) |
| MCP Integration | Yes | Yes | Yes | Yes | Yes | Yes |
| REST API | Yes (gRPC primary) | Yes | Yes | Yes | Yes | No |
| Deployment | Platform agnostic | Docker/K8s | Docker/K8s | Docker/K8s | Platform agnostic | Docker/K8s |
| Secrets | Workers fetch; Payload Codec for E2E encryption | Built-in encrypted | Built-in | External secret managers | Built-in Blocks | Workers fetch from external |
| Pauseability | Yes (timers/signals) | Yes (delay/approval) | Yes (approval/sleep) | Yes (wait/approval) | Yes | Yes (timers/signals) |
| Primary Use Case | Long-running stateful business logic | No-code iPaaS | Internal tools, cron, dev workflows | Data orchestration, ETL | Data engineering, ML pipelines | Distributed task queues |
| Workflow Language | Code (Go, Java, Python, TS) | Declarative (visual/JSON) | Code (Python, TS, Go) + UI | Declarative (YAML) | Code (Python) | Code (Python, Go, TS) |
| Debugging | Local replay, history viewer | UI test runs, execution history | UI logs, local CLI testing | UI execution topology, logs | UI observability, local Python | UI history viewer |
| Logging | SDK + workflow history | Run history, step logs in UI | Centralized in UI | Centralized in UI | Centralized in UI | SDK + workflow history |

Note: Inngest and Tines are not in the internal sheet — research from scratch.

### Output

Follow cited-research conventions. Write to the research output directory. Every factual claim must trace to a visited web source.
