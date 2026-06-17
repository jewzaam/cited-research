# Practical Value: Context7 Coverage for the Developer's Stack

## Direct Verification Results

Libraries verified by querying context7.com directly on 2026-06-17:

| Library | Indexed? | Tokens | Snippets | Trust Score | Last Updated |
|---------|----------|--------|----------|-------------|-------------|
| Django | Yes [19] | 2,151,957 | 24,330 | 8.8 | 2 weeks ago |
| FastAPI | Yes [20] | 127,807 | 2,124 | 9.9 | 10 hours ago |
| Go (golang) | Yes [21] | 2,447,540 | 13,367 | 8.3 | 1 week ago |
| React | Yes [22] | 800,029 | 7,143 | 10 | 3 hours ago |
| Next.js | Yes [22] | 527,972 | 5,907 | 10 | 4 hours ago |
| Docker Compose | Yes | — | — | — | — |
| Anthropic SDK Go | Yes [24] | 22,128 | 132 | 8.8 | 4 weeks ago |
| Ansible AAP 2.5 | Yes [23] | 683,224 | 10,310 | 10 | 1 month ago |

## Libraries Not Found

| Library | Status | Impact |
|---------|--------|--------|
| pytest | Not found in search | Medium — pytest docs are stable; training data likely sufficient |
| click | Not found in search | Low — CLI framework with stable API |
| pip | Not found (uv indexed instead) | Low — pip usage is well-known |
| Podman | Not found | Medium — container runtime alternative to Docker |
| Kubernetes client-go | Not found | High — Go K8s client is complex, version-specific |
| Kubernetes client-python | Not found | High — Python K8s client changes across versions |
| Helm (core CLI/SDK) | Not found (charts indexed, not Helm itself) | Medium — Helm CLI is fairly stable |

**Important caveat**: "Not found" means the discovery agent's search did not surface these libraries. They may exist under different names or paths. The library browser at context7.com/libraries uses dynamic content that could not be fully enumerated [3].

## Coverage Assessment by Domain

### Strong Coverage (verified)

- **Python web frameworks**: Django (trust 8.8, 2.1M tokens) and FastAPI (trust 9.9, 127K tokens) are extensively indexed with high trust scores [19][20].
- **Frontend**: React (trust 10, 800K tokens) and Next.js (trust 10, 527K tokens) are top-tier with near-real-time updates [22].
- **Go language**: Go standard library/docs indexed with 2.4M tokens [21].
- **Ansible**: Red Hat AAP 2.5 docs indexed with trust score 10 [23].
- **Claude/Anthropic SDK**: Go SDK indexed (trust 8.8, 22K tokens — relatively small) [24].

### Weak or Missing Coverage (unverified)

- **Kubernetes client libraries**: Neither client-go nor client-python found. K8s docs are available generically but not the programmatic client libraries that change significantly across versions.
- **Core Python tooling**: pytest, click, pip — these are stable enough that training data may suffice, but also stable enough that they should be trivial for Context7 to index.
- **Podman**: Not found. Docker Compose is indexed but Podman is absent — notable for a developer who uses both.
- **Helm**: Only Helm charts are indexed, not Helm itself.

### Libraries Where Context7 Adds Most Value

Based on refresh frequency and API churn rate:

1. **FastAPI** — Fast-moving framework, frequent breaking changes between versions. Context7 updates every 10 hours. High value.
2. **React/Next.js** — Active development, frequent API additions (Server Components, App Router). Updates within hours. High value.
3. **Anthropic SDK** — Rapidly evolving API surface. Context7 has the Go SDK but coverage is thin (132 snippets). Medium value.
4. **Django** — Stable framework but major version transitions (4.x→5.x) create API differences. Medium value.

### Libraries Where Context7 Adds Least Value

1. **Go standard library** — Very stable, well-documented in training data. Low incremental value from Context7.
2. **pytest, click, pip** — Stable APIs unlikely to hallucinate. Not indexed anyway.
3. **Ansible** — Indexed but updated only monthly. For AAP-specific questions, the developer's local knowledgebase likely contains more targeted information.

## Competitor Accuracy Context

| Tool | Accuracy/Hallucination | Source |
|------|----------------------|--------|
| Context7 | 65% accuracy; 63.4% hallucination on bleeding-edge [2][11] | Vendor benchmark [11] |
| Deepcon | 90% accuracy (vendor claim) [11] | Vendor benchmark |
| Nia | 52.1% hallucination (vendor claim) [11] | Vendor benchmark |
| No MCP context | 0% accuracy on same test [11] | Independent verification |

All competitor benchmarks are vendor-reported and should be treated with skepticism [11]. The 0% baseline without any MCP context validates that documentation injection helps, regardless of which tool provides it [11].

## Gaps and Limitations

1. Cannot definitively confirm absence of libraries — search may miss existing entries under different names or paths.
2. Token counts and trust scores are point-in-time snapshots from 2026-06-17 and will change.
3. Anthropic SDK Go coverage is thin (132 snippets vs Django's 24,330) — may not be sufficient for complex SDK questions.
4. No verification of documentation quality for the specific libraries — only trust scores and snippet counts.
