# Kubernetes deployment patterns for browser-TTY workloads

## Dimension scope

How browser-TTY tools are deployed on Kubernetes: published Helm charts, multi-tenant patterns (Argo CD ApplicationSet), persistent home-directory shapes, liveness/readiness probes for WebSocket daemons, and known footguns. The brief noted the public web is thin here; this reference flags sparse areas explicitly.

Source numbers refer to [`citations.md`](../citations.md).

## Published Helm charts

| Tool | Helm chart status | Source |
|---|---|---|
| ttyd | No upstream chart. Operator pattern instead: **CloudTTY** wraps ttyd in a Kubernetes operator with its own Helm chart [26, 27] | [26, 27] |
| gotty (sorenisanerd) | No upstream Helm chart. Raw manifests only. | discovery sub-agent |
| wetty | No upstream Helm chart. Raw manifests only. | discovery sub-agent |
| code-server | In-tree at `ci/helm-chart/values.yaml` [23, 24]; install docs reference it briefly [24] | [23, 24] |

### CloudTTY (ttyd-based operator)

CloudTTY is the closest thing to a purpose-built Kubernetes pattern for a ttyd-backed browser shell [26].

- Install:
  ```bash
  helm repo add cloudtty https://cloudtty.github.io/cloudtty
  helm repo update
  helm install cloudtty-operator --version <V> cloudtty/cloudtty
  ```
  The README's quickstart references `0.5.0` [26], but the actual latest release is **0.8.9 (2025-01-27)** [27]. The README is stale.
- CRD: `cloudshell.cloudtty.io/v1alpha1`, kind `CloudShell`. Each CloudShell spawns a pod running ttyd ("the ttyd binary inside the container also comes from ttyd project") [26].
- Network exposure modes: NodePort (default), ClusterIP, Ingress, Istio VirtualService [26]. LoadBalancer is not listed.
- Persistence: no shell-state persistence story in the README. Jobs are ephemeral with TTL [26].

CloudTTY's design center is "open a shell to kubectl-against this cluster," not "persistent coding sandbox per user." It is a useful reference for the ttyd-in-CRD pattern but does not solve the PVC-backed `$HOME` requirement directly.

### code-server Helm chart

In-tree at `coder/code-server/ci/helm-chart/` [23]. Defaults from `values.yaml` [23]:

```yaml
persistence:
  enabled: true
  size: 10Gi
  accessMode: ReadWriteOnce
  storageClass: ""        # unset → cluster default
  existingClaim: ""       # unset → chart creates a PVC

ingress:
  enabled: false
  ingressClassName: ""

image:
  repository: codercom/code-server
  tag: 4.121.0
  pullPolicy: Always
```

Resource limits and requests are commented out by default [23]. This is fine for a homelab but means a code-server pod without explicit limits will draw whatever the node permits — with the documented 1 GB RAM floor [19].

The `existingClaim` field is the seam for per-user PVCs: an Argo CD ApplicationSet (below) can parameterize this with a per-user PVC name and let each operator's Application point to its own PVC.

## Argo CD ApplicationSet for multi-tenant sandboxes

The natural "one Application per operator" pattern uses Argo CD's **ApplicationSet List generator** [32]:

```yaml
generators:
  - list:
      elements:
      - cluster: engineering-dev
        url: https://kubernetes.default.svc
template:
  metadata:
    name: '{{.cluster}}-guestbook'
  spec:
    destination:
      server: '{{.url}}'
```

Each element becomes Go template variables (`{{.cluster}}`, `{{.url}}`) in the template, producing one Application per element [32]. For 12 sandboxes, the list contains 12 elements parameterizing operator name, PVC name, ingress hostname.

The discovery-agent counter-perspective flagged ApplicationSet multi-tenancy as having known anti-patterns: mixing infrastructure apps with developer apps in one ApplicationSet, and self-service Application creation requiring access to the `argocd` namespace (which is a bottleneck for true tenant self-service). For ~12 named operators in a homelab where the operator authors the ApplicationSet themselves, these concerns are manageable — the homelab is not the multi-tenant SaaS scenario those anti-patterns target.

## Persistent home directory patterns

The code-server Helm chart defaults to `persistence.enabled: true` with a `ReadWriteOnce` PVC of 10 Gi [23], mounted into `/home/coder` (per code-server convention).

Footguns specific to this pattern (sourced from discovery sub-agent observation, partially verifiable):

1. **PVC ownership.** Mounting a PVC on cloud providers sets ownership to root, but code-server runs as user `coder`. Explicit `chown` via `initContainer` or `securityContext.fsGroup` is needed. On k3s with local-path provisioner, default ownership behavior is more lenient but still worth verifying per node.
2. **`accessMode: ReadWriteOnce`** is correct for one-pod-per-user. ReadWriteMany (NFS, Longhorn, etc.) is only needed if you want to share dotfiles across sandboxes — which the brief does not require.
3. **PVC orphaning on pod recreate.** If the sandbox is deleted and re-created via a different Application, the PVC may not rebind without explicit `existingClaim` referencing the old PVC name.

For ttyd-based sandboxes (CloudTTY or a hand-rolled Pod), the persistence story is whatever the operator authors — CloudTTY itself does not provide one [26].

## Liveness/readiness probes for WebSocket daemons

No tool-specific probe documentation found in-session for ttyd, gotty, or wetty. For a WebSocket daemon, the conventional patterns are:

- `tcpSocket` probe on the listen port — minimal viable check that the process is bound. Cannot detect a hung WebSocket handler.
- `httpGet` probe on the daemon's HTTP root — most browser-TTY tools serve the HTML page on `/`, so an HTTP 200 on `/` is a reasonable readiness signal. This does not test the WebSocket upgrade path.
- `exec` probe running `wget -q -O- http://localhost:<port>/` from inside the container.

code-server exposes the same shape: HTTP `/` returns the IDE bundle when authenticated (or a login page when not). A probe shape of `httpGet /healthz` is documented in community Helm charts but not as a code-server-native endpoint.

**This is a sparse area on the public web.** Beyond generic Kubernetes probe patterns, tool-specific guidance is not published.

## Ingress and WebSocket behavior

### Traefik (k3s default ingress)

Traefik v3 supports WebSocket and WSS **out of the box** [29]. No special annotations, headers, or middlewares required for a single-pod backend. The IngressRoute YAML is the minimum:

```yaml
apiVersion: traefik.io/v1alpha1
kind: IngressRoute
metadata:
  name: sandbox
spec:
  entryPoints: [web]
  routes:
    - match: Host(`sandbox.example.com`)
      kind: Rule
      services:
        - name: sandbox
          port: 7681     # ttyd default
```

For WSS, add `tls: {}` and use `websecure`.

A real footgun on k3s: the k3s upgrade path that bumps Traefik from v2 to v3 introduces breaking changes (`defaultRuleSyntax`, removed middlewares). Customizing via `HelmChartConfig` in `/var/lib/rancher/k3s/server/manifests/` is the supported path. The discovery sub-agent flagged this as a footgun, but it is unrelated to the access-layer choice — it is a k3s operator concern.

### Tailscale Operator

The Tailscale Operator can expose any Kubernetes Service to the tailnet via `ingressClassName: tailscale` on a standard Ingress resource [28]. Prerequisites [28]:

- HTTPS and MagicDNS enabled on the tailnet.
- TLS hostname defaults to `<ingress-name>-<namespace>`; customize via `tls.hosts` (first label only).
- Certificate provisioning is **lazy on first connect**: "the first connection might be slow or even time out" [28]. This is a documented quirk, not a bug — workaround is to warm the certificate by hitting the URL once after creation.

This satisfies the brief's "single URL per sandbox, no per-device tooling" requirement directly: each per-operator sandbox gets its own Ingress with its own MagicDNS hostname, and any device on the tailnet can hit the URL.

### nginx-ingress (Kubernetes maintained)

**Important context for 2026:** `kubernetes/ingress-nginx` was **archived 2026-03-24** [30]. The project recommends Gateway API implementations as the migration path. Existing Helm charts and images remain available but receive no further updates [30]. For a new homelab deployment in May 2026, nginx-ingress should not be selected.

For reference, the historical WebSocket footgun on nginx-ingress is real: any `Ingress` add/modify/delete causes a config reload that drops active WebSocket connections [31]. The issue (#2461) was closed without resolution as part of the repo archival [31]. Operators on existing nginx-ingress deployments inherit this behavior.

## Known footguns

| Footgun | Source / verification |
|---|---|
| nginx-ingress drops WebSockets on any Ingress reload | [31]; verified |
| nginx-ingress 60-second default `proxy-read-timeout` requires `nginx.ingress.kubernetes.io/proxy-read-timeout` (not `ingress.kubernetes.io/proxy-read-timeout`) — silent annotation prefix bug | discovery agent; partially verified by repo activity |
| k3s Traefik v2 → v3 upgrade is breaking | discovery agent; partially verified |
| CloudTTY README references chart 0.5.0 while latest is 0.8.9 | [26, 27]; verified |
| code-server CVE-2025-47269 — affected versions <4.99.4 | [21]; verified |
| code-server Helm chart `image.tag: 4.121.0` defaults to current at chart build time — keep chart in sync with app version | [23]; verified |
| Tailscale Operator first-connect cert provisioning timeout | [28]; verified |
| `ingress.kubernetes.io/proxy-read-timeout` (wrong prefix) silently ignored | discovery agent; not verified directly in-session |
| Alpine vs Debian — Alpine images lack bash by default, breaking interactive tools that assume readline | well-known but not cited in-session |

## Gaps and Limitations

- Tool-specific liveness/readiness probe shapes are not documented in upstream repos. Community Helm charts vary in their probe choices.
- The `openclaw-rocks/openclaw-operator` third-party Kubernetes operator surfaced by the OpenClaw discovery agent was not profiled for this dimension — it is a candidate for a future revisit if OpenClaw becomes interesting.
- ApplicationSet anti-patterns (mixed infra+dev apps, control-plane flooding) were cited from a Codefresh blog by a sub-agent but not fetched directly in this session.
- No first-party benchmark exists for any of the four tools' idle RAM in a Kubernetes Pod. Operators relying on these numbers should measure locally.
- The PID-pressure failure mode (one pod's forks exhausting the node's PID pool, evicting other pods) is real but not specific to browser-TTY tools — it applies to any code-execution workload. The `podPidsLimit` mitigation requires explicit kubelet configuration, which is not k3s default in older versions.
