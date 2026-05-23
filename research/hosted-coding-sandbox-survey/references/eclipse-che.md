# Eclipse Che (and OpenShift Dev Spaces)

Dimension: how Eclipse Che solves the four recurring problems on Kubernetes. Most architecturally analogous to a self-hosted k3s sandbox in this survey. Sources in [citations.md](../citations.md).

## Architecture orientation

"Che runs on three groups of components: Che server components [which] Manage User namespace and workspaces", the DevWorkspace operator that "Creates and controls the necessary Kubernetes objects to run User workspaces", and "User workspaces [which are] Container-based development environments, the IDE included" [43]. The central abstraction is the **DevWorkspace Custom Resource** — "Valid Kubernetes objects representing the User workspaces" [43] — managed by the DevWorkspace Operator (DWO).

The lesson worth importing: each workspace is a CR, reconciled by an operator, queryable via `kubectl get devworkspaces`. The operator-pattern split between "user dashboard transforms devfile→DevWorkspace CR" and "operator reconciles DevWorkspace CR→Deployment/PVC/Service" is exactly the right shape for a k3s-native homelab sandbox.

## Session persistence

`pvcStrategy` is set on the `CheCluster` CR at `spec.devEnvironments.storage.pvc.pvcStrategy` [46]. Three options [46]:
- **per-user** (default): "Use a single PVC for all workspaces created by a user."
- **per-workspace**: "Each workspace is given its own PVC."
- **ephemeral**: "Non-persistent storage; any local changes will be lost when the workspace is stopped."

(Note: discovery agent surfaced a fourth `common` strategy from older docs / GitHub issue #21185; the current page lists only the three above [46]. The `common` strategy historically prevented running more than one workspace concurrently, which is why `per-workspace` was added.)

User can override per-workspace via devfile or URL parameter [46]. Idle-timeout defaults (`secondsOfInactivityBeforeIdling`, `secondsOfRunBeforeIdling`) were expected on the running-at-scale doc but were not present there in this fetch [50] — those defaults remain unverified at primary source level.

## Browser access UX

A single **Traefik-based gateway** (`che-gateway`) terminates external traffic [45]. Three responsibilities baked into the same Deployment [45]:
- **Routing** (Traefik)
- **Authentication** (OAuth2 Proxy + OIDC)
- **Access control** (`kube-rbac-proxy` enforcing Kubernetes RBAC)

Gateway-managed access to: user dashboard, Che server, plugin registry, user workspaces [45]. The downstream-product (Red Hat OpenShift Dev Spaces) adds an additional gateway-RBAC check that "only the developer who creates the workspace can physically access it and its PVC with an IDE" (discovery agent finding).

Default browser editor — code-server / VS Code Web — replaced the deprecated Che-Theia. (Discovery agent finding; not re-fetched in this pass.)

For a homelab the gateway pattern is the most directly portable design: one Ingress, dynamic per-workspace routing config, OIDC at the gate. The kube-rbac-proxy pattern of "user must have K8s RBAC to access workspace" reuses cluster-native authz instead of inventing a separate access-control system.

## Multi-tenant isolation

**Namespace per user** is the default tenancy unit. Che server auto-provisions a namespace on first login, name templated from userid (discovery: 14 char userid + 6 char suffix); admins can pre-provision namespaces with required labels and disable auto-provisioning [44].

**Resource sync from `eclipse-che` to user namespaces** is bidirectional with a strong invariant: "If you make changes to a Kubernetes resource in an eclipse-che namespace, Che will immediately synchronize the changes across all users namespaces" and conversely "if a Kubernetes resource is modified in a user namespace, Che will immediately revert the changes" [44]. Sync source ConfigMaps/Secrets/PVCs are labeled `app.kubernetes.io/part-of: che.eclipse.org` + `app.kubernetes.io/component: workspaces-config` [44]. Annotation `che.eclipse.org/sync-retain-on-delete: "true"` preserves on source deletion [44]. The mount-control annotations `controller.devfile.io/watch-configmap: "false"` and `controller.devfile.io/mount-to-devworkspace: "false"` opt-out individual resources from auto-mount [44].

This central-to-namespace sync is a useful pattern for homelab: shared cluster credentials and per-tenant secrets handled by the same mechanism, with revert-on-tamper enforcing that user namespaces can't diverge from admin-blessed config.

**NetworkPolicies** address the K8s open-by-default east-west issue head-on: "By default, all Pods in a Kubernetes cluster can communicate with each other even if they are in different namespaces" [48]. Three canonical policies [48]:
- `allow-from-eclipse-che` — applied to user namespaces, allows Che namespace → user pods.
- `allow-from-openshift-apiserver` — apiserver → devworkspace-webhook-server.
- `allow-from-workspaces-namespaces` — user namespaces → `che-gateway` pod.

The implicit rule: no other namespace-to-namespace traffic. For a k3s build, this is the explicit network-policy bundle to crib.

## Credential injection

**Git PATs**: configured per-user via dashboard at `/dashboard/#/user-preferences?tab=personal-access-tokens`, OR applied manually as a K8s Secret in the user's namespace [49] with labels `app.kubernetes.io/component: scm-personal-access-token` + `app.kubernetes.io/part-of: che.eclipse.org`, annotations `che.eclipse.org/che-userid`, `scm-personal-access-token-name` (`github` | `gitlab` | `bitbucket-server` | `azure-devops`), `scm-url`, `scm-organization` (Azure DevOps only), and `stringData: token: <Content>` [49]. Purpose: "Mounting your access token as a Secret enables the Che Server to access the remote repository that is cloned during workspace creation, including access to the repository's /.che and /.vscode folders" [49].

**Generic secret/configmap automount** uses a label-and-annotation pattern that is the most portable Che design idea [47]:
- Labels required: `controller.devfile.io/mount-to-devworkspace: 'true'` + `controller.devfile.io/watch-secret: 'true'`
- Annotations: `mount-path` (default `/etc/secret/<Secret_name>`), `mount-as: file | subpath | env` (default `file`)

This is just labels + annotations on standard K8s Secrets/ConfigMaps. No CRD for secrets. A k8s-native homelab can adopt this verbatim by writing a small admission controller or reusing DWO itself.

**Auth**: OIDC. On plain K8s, Keycloak is the documented external provider — configured via OAuth client name/secret and identity provider URL pointing at a realm (discovery; not re-fetched).

**Known limitation surfaced in discovery**: GitLab OAuth tokens issued via Dev Spaces' integration expire after ~2 hours without refresh, breaking commits after the window. (Source not re-fetched in this pass.)

## Lessons for a k3s homelab

The strongest design ideas to import:
1. **Workspace as Custom Resource**, operator reconciliation.
2. **Namespace-per-user** as tenancy boundary with auto-provisioning template.
3. **Bidirectional sync from admin namespace** with revert-on-tamper semantics [44].
4. **Three explicit NetworkPolicies** to close the K8s default-open east-west [48].
5. **Single Traefik gateway** with Routing + OIDC + kube-rbac-proxy stacked in one Deployment [45].
6. **Label-driven secret/configmap automount** — no separate CRD, no custom secrets API [47].

## Gaps

- Default editor in current Che (code-server vs Microsoft VS Code Web build) not re-verified at primary source.
- Whether kube-rbac-proxy sidecars are actually shipped in user workspace pods today, or only at the gateway, not confirmed.
- Idle-timeout defaults not on the running-at-scale page [50]; remain unverified at primary source.
- Cred lifecycle on DevWorkspace deletion (GC of secrets in user namespace) not pulled in this pass.
- Single-host vs multi-host gateway routing details not on the gateway doc fetched here [45].
