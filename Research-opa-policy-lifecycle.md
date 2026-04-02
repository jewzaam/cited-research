# OPA Policy Lifecycle Management - Research Findings

## URL Manifest

| URL | Rationale | Data to extract | Source Tier |
|-----|-----------|-----------------|-------------|
| <https://www.openpolicyagent.org/docs/policy-testing> | Official OPA documentation on testing framework | Test framework syntax, opa test command flags, coverage reporting, mocking patterns | Tier 2 (Manufacturer) |
| <https://www.openpolicyagent.org/docs/management-bundles> | Official OPA documentation on bundle management | Bundle API protocol, distribution configuration, ETag caching, persistence, delta bundles | Tier 2 (Manufacturer) |
| <https://www.openpolicyagent.org/docs/cicd> | Official OPA documentation on CI/CD integration | CI/CD use cases, opa eval flags, integration patterns | Tier 2 (Manufacturer) |
| <https://www.openpolicyagent.org/docs/management-decision-logs> | Official OPA documentation on decision logging | Decision log format, audit capabilities, compliance monitoring | Tier 2 (Manufacturer) |
| <https://www.openpolicyagent.org/docs/latest/policy-language/> | Official OPA documentation on Rego language | Module structure, package organization, imports, modularization patterns | Tier 2 (Manufacturer) |
| <https://www.openpolicyagent.org/docs/latest/storage/> | Official OPA documentation on storage | Disk persistence, storage backends, bundle persistence behavior | Tier 2 (Manufacturer) |
| <https://www.conftest.dev/> | Official Conftest documentation | Conftest overview, policy testing use cases, integration patterns | Tier 2 (Manufacturer) |
| <https://github.com/open-policy-agent/conftest> | Official Conftest GitHub repository | GitHub Actions integration, outputters, implementation details | Tier 2 (Manufacturer) |
| <https://github.com/open-policy-agent/regal> | Official Regal linter GitHub repository | Linting rules, style guide enforcement, CI integration, language server features | Tier 2 (Manufacturer) |
| <https://docs.styra.com/regal> | Official Regal documentation | Rule categories, best practices, editor integration | Tier 2 (Manufacturer) |
| <https://docs.opal.ac/> | Official OPAL documentation | Real-time policy updates, architecture, client-server model | Tier 2 (Manufacturer) |
| <https://github.com/permitio/opal> | Official OPAL GitHub repository | OPAL implementation details, GitOps integration, production usage | Tier 2 (Manufacturer) |
| <https://docs.styra.com/das/policies/policy-authoring/test-policies> | Official Styra DAS documentation on testing | Impact analysis, what-if testing, preview/validate/replay features | Tier 2 (Manufacturer) |
| <https://docs.styra.com/das/policies/bundles/bundle-registry> | Official Styra DAS documentation on bundles | Bundle registry, delta bundles, version management | Tier 2 (Manufacturer) |
| <https://www.styra.com/manage-open-policy-agent-with-styra-das/> | Official Styra DAS product page | Control plane features, management capabilities, enterprise governance | Tier 2 (Manufacturer) |
| <https://github.com/opcr-io/policy> | Open Policy Containers CLI GitHub repository | OCI image building, semantic versioning, policy CLI usage | Tier 2 (Manufacturer) |
| <https://openpolicycontainers.com/> | Open Policy Containers project site | OCI integration, cosign signing, registry evolution | Tier 2 (Manufacturer) |
| <https://www.wiz.io/academy/application-security/open-policy-agent-opa> | Wiz Application Security Academy OPA guide | Best practices synthesis, version control, CI/CD, GitOps patterns | Tier 3 (Industry) |
| <https://www.cncf.io/blog/2025/03/18/open-policy-agent-best-practices-for-a-secure-deployment/> | CNCF blog post on OPA security best practices (March 2025) | Security deployment best practices, OPAL integration, recent trends | Tier 3 (Industry) |
| <https://dustinspecker.com/posts/open-policy-agent-unit-testing-gatekeeper-policies/> | Dustin Specker blog on OPA testing | Practical testing examples, Kubernetes/Gatekeeper patterns | Tier 4 (Practitioner) |
| <https://www.aserto.com/blog/testing-rego-policies> | Aserto blog on Rego testing | Testing patterns, mock strategies | Tier 3 (Industry) |
| <https://www.styra.com/blog/advanced-rego-testing-techniques/> | Styra blog on advanced testing | Advanced testing patterns, test coverage strategies | Tier 3 (Industry) |
| <https://dev.to/mnaseem/distributing-api-authorization-policies-using-opa-bundles-1i4e> | DEV Community article on bundle distribution | Practical bundle distribution examples for API authorization | Tier 4 (Practitioner) |
| <https://github.com/shubhanshusingh/opa_bundle_server> | Example OPA bundle server implementation | Reference implementation for policy management | Tier 4 (GitHub) |
| <https://github.com/stevef1uk/opa-bundle-server> | Example OPA bundle server (non-production) | Simple bundle server implementation | Tier 4 (GitHub) |
| <https://codilime.com/blog/leveraging-opa-and-rego-to-automate-compliance/> | CodiLime blog on OPA in CI/CD | CI/CD automation patterns, Terraform integration | Tier 3 (Industry) |
| <https://www.harness.io/blog/policy-enforced-pipeline-opa> | Harness blog on policy-enforced pipelines | CI/CD policy enforcement patterns, pipeline governance | Tier 3 (Industry) |
| <https://medium.com/@debghosal01/opa-gitops-enhancing-compliance-security-and-automation-for-platform-teams-426bc53ce9c4> | Medium article on OPA + GitOps | GitOps integration patterns, compliance automation | Tier 4 (Practitioner) |
| <https://www.styra.com/blog/using-opa-with-gitops-to-speed-cloud-native-development/> | Styra blog on GitOps | GitOps workflows, policy-as-code deployment | Tier 3 (Industry) |
| <https://www.styra.com/blog/gitops-with-styra-das-and-opa-styra/> | Styra blog on DAS + GitOps | Styra DAS GitOps integration, management plane patterns | Tier 3 (Industry) |
| <https://github.com/anderseknert/opa-sign-verify> | OPA bundle signing demo repository | Signature creation and verification examples | Tier 4 (GitHub) |
| <https://github.com/open-policy-agent/opa/pull/2475> | OPA PR #2475 on bundle signature verification | Bundle signature verification implementation details | Tier 4 (GitHub) |
| <https://himido.io/blog/opa/opa-signing-bundles> | Hieu Doan blog on OPA bundle signing | Practical bundle signing tutorial | Tier 4 (Practitioner) |
| <https://github.com/open-policy-agent/opa/issues/3361> | OPA issue #3361 on ETag caching bug | ETag caching implementation issues, HTTP server compatibility | Tier 4 (GitHub) |
| <https://github.com/open-policy-agent/opa/issues/1055> | OPA issue #1055 on delta bundles | Delta bundle design discussion, feature rationale | Tier 4 (GitHub) |
| <https://github.com/open-policy-agent/opa/issues/4782> | OPA issue #4782 on cloud-native bundle persistence | Bundle persistence in containerized environments | Tier 4 (GitHub) |
| <https://github.com/open-policy-agent/opa/issues/428> | OPA issue #428 on policy testing improvements | Testing framework enhancement requests | Tier 4 (GitHub) |
| <https://github.com/open-policy-agent/opa/issues/5007> | OPA issue #5007 on --fail-defined for opa exec | CI/CD exit code flag feature request | Tier 4 (GitHub) |
| <https://github.com/marketplace/actions/conftest> | GitHub Actions: Conftest integration | CI automation for Conftest policy testing | Tier 4 (GitHub) |
| <https://github.com/YubicoLabs/action-conftest> | YubicoLabs Conftest GitHub Action | Advanced Conftest integration with PR comments | Tier 4 (GitHub) |
| <https://github.com/masterpointio/github-action-opa-rego-test> | GitHub Action for OPA Rego testing | Automated OPA testing in CI with coverage reports | Tier 4 (GitHub) |
| <https://oneuptime.com/blog/post/2026-01-28-opa-conftest-policy-testing/view> | OneUpTime blog on Conftest | Conftest practical usage guide | Tier 4 (Practitioner) |
| <https://oneuptime.com/blog/post/2026-01-28-opa-bundles-implementation/view> | OneUpTime blog on bundle implementation | Bundle implementation patterns | Tier 4 (Practitioner) |
| <https://oneuptime.com/blog/post/2026-01-28-monitor-opa-policy-decisions/view> | OneUpTime blog on decision monitoring | Decision logging and monitoring patterns | Tier 4 (Practitioner) |
| <https://hoop.dev/blog/audit-logs-open-policy-agent-opa-what-you-need-to-know/> | Hoop.dev blog on OPA audit logs | Audit logging best practices, compliance use cases | Tier 4 (Practitioner) |
| <https://devm.io/testing/open-policy-agent-tests-automation> | Dev.io article on OPA testability and automation | Testing patterns, automation strategies | Tier 4 (Practitioner) |
| <https://hoop.dev/blog/using-open-policy-agent-to-automate-qa-policy-checks/> | Hoop.dev blog on QA automation | QA policy checks, test framework integration | Tier 4 (Practitioner) |
| <https://docs.sigstore.dev/policy-controller/overview/> | Sigstore policy controller documentation | Kubernetes policy enforcement with signature verification | Tier 2 (Manufacturer) |
| <https://developer.harness.io/docs/continuous-delivery/get-started/tutorials/cloud-native-cicd-pipelines/cosign-opa/> | Harness tutorial on Cosign + OPA | Container image signing with OPA policy enforcement | Tier 3 (Industry) |
| <https://scalr.com/learning-center/enforcing-policy-as-code-in-terraform-a-comprehensive-guide/> | Scalr guide on Terraform policy-as-code | Terraform policy enforcement lifecycle | Tier 3 (Industry) |

## Preliminary Findings

### 1. Policy Testing Framework

**OPA Test Framework** (unverified)

- The `opa test` command discovers and executes test rules prefixed with `test_` in Rego files
- Tests expect rules to evaluate to true; failures occur when rules evaluate to false or undefined
- Coverage reporting available via `opa test --coverage --format=json` showing evaluated and non-evaluated lines
- The `with` keyword enables mocking of data documents, input, and built-in functions
- Test organization best practice: suffix test packages with `_test` (e.g., `package authz_test`)
- The `--fail-on-empty` flag ensures CI pipelines fail when no tests are executed
- The `--var-values` flag enriches test failure reports with exact expression values
- Coverage threshold enforcement available to fail builds below specified percentage

**Conftest** (unverified)
- Conftest is a CLI tool built on OPA for testing structured configuration files (Kubernetes, Terraform, Serverless configs)
- Writes policies in Rego language; validates configurations during CI/CD to prevent non-compliant resources
- GitHub Actions integration available via multiple community actions (YubicoLabs/action-conftest, instrumenta/conftest-action)
- Supports GitHub outputter format for source file annotations in GitHub Actions
- Conftest can export Terraform plans as JSON and validate without cloud access (no resource creation costs)

**Regal - Rego Linter** (unverified)
- Regal is an official OPA project providing linting and language server capabilities for Rego
- Rule categories: bugs, idiomatic, imports, performance, style, testing, custom
- Enforces OPA Style Guide recommendations and identifies common mistakes, inefficiencies
- Editor integration available for VS Code, Neovim, Zed, Helix with context-aware completion
- CI/CD integration for consistent policy quality enforcement across teams

### 2. Policy Versioning and Distribution

**Version Control and GitOps** (unverified)
- Store Rego policies in Git repositories for version control, collaborative reviews, and audit trails
- GitOps approach ensures policies are version-controlled, auditable, and consistently deployed across environments
- Policy code follows standard software development lifecycle: version control, branching workflows, reviews, automated testing
- OPAL (Open Policy Administration Layer) monitors Git repositories and pushes updates to OPA instances in real-time
- OPAL uses client-server stateless architecture with WebSocket PubSub for policy/data updates
- OPAL production usage includes Tesla, Walmart, NBA, Intel, Cisco, and thousands of other companies

**Semantic Versioning and OCI Images** (unverified)
- Open Policy Containers (OPCR) is a CNCF Sandbox project enabling OPA policies as OCI images
- Policy CLI tool supports building, tagging, pushing, and pulling policies like Docker images
- Semantic versioning supported via standard OCI image tags
- Policies can be signed using Sigstore's cosign (OCIv2 container signing)
- OPA natively consumes OCI images as of May 2022 contribution acceptance
- Open Policy Registry (opcr.io) retired January 31, 2023 — standard OCI registries (AWS ECR, Docker Hub, GitHub Container Registry, GCR) now used

**Bundle Management** (unverified)
- Bundles are gzipped tarballs containing policies and data, distributed via HTTP servers
- Bundle API expects services to expose endpoints serving bundles at arbitrary URLs
- ETag header enables HTTP 304 Not Modified responses for efficient caching (known bugs with some HTTP servers not returning ETag in 304)
- Bundle configuration includes service URL, credentials, resource path, persistence settings, and polling intervals (min_delay_seconds, max_delay_seconds)
- Bundle persistence: when `bundles[_].persist: true`, OPA writes activated bundles to disk (default: `./.opa/bundles/<bundle-name>/bundle.tar.gz`)
- Delta bundles contain incremental data changes only (not policy changes); not persisted to disk; require OPA 0.37+
- Bundle signing uses JWT with RS256 (default), HMAC, or ECDSA; `.signatures.json` file contains SHA hashes and cryptographic signature
- Signature verification: OPA validates JWT signature with public key, checks file set matches, verifies content hashes

### 3. CI/CD Integration

**OPA in CI/CD Pipelines** (unverified)
- `opa eval` command with `--fail` and `--fail-defined` flags sets exit code 1 based on query results
- `--fail-defined` returns exit code 1 when result is defined (useful for detecting violations)
- `--stdin-input` flag allows piping output from other commands directly into OPA
- GitHub Actions integration via official OPA setup action makes `opa` command available in workflows
- Terraform pipelines: policies executed before `terraform apply`; pipeline continues only when all rules fulfilled
- Repository governance use cases: commit message validation, PR metadata checks, dependency verification
- Test coverage enforcement: ensure test files added when code files created

**Regression Testing and Automation** (unverified)
- OPA policy testing integrated alongside unit and integration tests in CI/CD
- GitHub Action available (masterpointio/github-action-opa-rego-test) for automated testing with coverage reports and PR comments
- QA teams pair OPA with test frameworks: API contract tests include OPA checks, load tests assert scaling policies, security tests embed OPA validations
- Policy checks run as fast and deterministically as tests themselves (no delivery slowdown)

### 4. Policy Lifecycle Stages

**Development Lifecycle** (unverified)
- Policy Development: translate real-world requirements into version-controlled Rego
- CI and Testing: assemble policies into single repository, perform unit tests and QA
- Deployment: experiment with configurations (cluster front-end vs. sidecar proxy) for latency optimization
- Monitoring and Orchestration: monitor OPA health, policy version, data version like any service
- Decision Logging and Audit: separate decision logs from application logs for compliance

**Deployment Stages** (unverified)
- Infrastructure-as-Code level: validate configurations before deployment (Terraform plan validation)
- Runtime level: admission control in Kubernetes, API authorization in applications
- Speculative runs for policy changes: analyze impact before policies go live

**Progressive Delivery Integration** (unverified)
- OPA integrates with progressive delivery tools like Flagger for policy-based canary deployments
- Platform teams define policies once; Harness/similar tools automatically evaluate changes against policies in real-time
- Policy governance areas: feature flags (naming, ownership, tags), targeting rules (block unsafe production rollouts), segments (prevent risky definitions), change requests (require approvals for sensitive changes)

### 5. Policy Organization and Modularization

**Rego Module Structure** (unverified)
- Modules consist of: exactly one package declaration, zero or more import statements, zero or more rule definitions
- Packages group rules into namespaces; multiple modules can contribute to same package
- Modules in same package don't need same directory location
- Valid package names: variables or references with string operands only (e.g., `package foo.bar.baz`)
- Imports enable rule/data reuse from other packages
- Best practice: each .rego file addresses single domain (access control, resource quotas, compliance)
- Avoid monolithic files; use packages and imports for reusable logic blocks
- Separation of policy from infrastructure/application code simplifies issue identification

### 6. Decision Logging and Audit

**Decision Log Contents** (unverified)
- Decision logs contain events describing policy queries: policy queried, input data, bundle metadata, decision_id
- Full traceability for audits and offline debugging of policy decisions
- Organizations under regulatory guidelines rely on logs for certifications and compliance evidence

**Log Distribution** (unverified)
- OPA periodically reports decision logs to remote HTTP servers, custom plugins, or console output
- Logs forwarded to observability platforms: Prometheus, Loki, Elasticsearch, OpenTelemetry
- Centralized access to logs from all OPA instances across services

**Security Monitoring** (unverified)
- Decision logs treated as security telemetry (example: Wazuh integration)
- Detection rules identify suspicious or unauthorized access patterns, generate alerts
- Proof of policy enforcement at every pipeline stage for audit compliance

### 7. Management Plane: Styra DAS

**Styra DAS Overview** (unverified)
- Styra Declarative Authorization Service (DAS) is the control plane for OPA
- Single pane of glass for policy authoring, distribution, impact analysis, monitoring, auditing
- Saves time/effort of designing custom management plane

**Key Features** (unverified)
- Policy authoring through UI, CLI, or APIs; store policies in Git
- Fetch policy bundles from Git and distribute to OPA instances
- Impact analysis capabilities: Preview (test policy against input), Validate (run draft policy against real-world resources), Replay (reload past decision input for testing)
- Decision Replay ensures policy changes produce expected results
- Fine-grained access control for enterprise governance
- Styra Local Control Plane (SLP): sits between DAS and OPA, downloads policies from DAS, relays to OPAs

### 8. Real-Time Policy Updates: OPAL

**OPAL Architecture** (unverified)
- OPAL (Open Policy Administration Layer) is an administration layer for OPA and AWS Cedar Agent
- Detects changes to policy and data in real-time, pushes live updates to agents
- Client-server stateless architecture: OPAL-Servers publish updates over WebSocket PubSub, OPAL-clients subscribe via topics
- Upon updates, clients fetch data directly from source to load into managed policy engine
- Bridges OPA to speed needed by live applications where authorization state changes per user click/API call

**Production Adoption** (unverified)
- Used in production at Tesla, Walmart, NBA, Intel, Cisco, Live-Oak Bank, and thousands of teams
- CNCF blog (March 2025) highlights OPAL's push-based strategy for secure OPA deployments

### 9. Bundle Server Implementation

**Server Requirements** (unverified)
- OPA expects HTTP API endpoint serving bundles at arbitrary URLs
- HTTP 200 OK with gzipped tarball in message body when bundle exists
- ETag header identifies bundle revision; OPA includes ETag in If-None-Match header for subsequent requests
- HTTP 304 Not Modified response when bundle unchanged (reduces bandwidth, CPU, latency)
- Known issue: many HTTP servers (Nginx, Azure, GCS) don't return ETag in 304 responses (OPA should store/reuse ETag)

**Implementation Examples** (unverified)
- GitHub repositories: shubhanshusingh/opa_bundle_server, stevef1uk/opa-bundle-server
- FastAPI-based server example: stores bundles in directory structure, serves via `/bundles/{tenant}/{bundle_file}`
- Production deployments typically use S3, GCS, or HTTP servers in Kubernetes with multi-tenant configurations

### 10. Testing and Mocking

**Mocking with `with` Keyword** (unverified)
- `with` keyword replaces data documents or called functions with mocks
- Both base and virtual documents can be replaced
- Mock built-in functions by creating user-defined function and using `with` to substitute
- Constraints: cannot replace internal.*, rego.metadata.*, eq, relations (walk); replacement/replaced functions must have same arity
- Example: mock `io.jwt.decode_verify` for testing JWT-based policies without real tokens
- Mocking input and data: create mock objects for policies using external data (e.g., RBAC role definitions)

**Impact Analysis and What-If Testing** (unverified)
- Styra DAS Preview: evaluate current policy against provided input, view output
- Styra DAS Validate: run draft policy against real-world resources in system state (e.g., all resources in live Kubernetes cluster)
- Styra DAS Replay: open policy and pre-load input from past decision for testing
- Styra supports mocking `http.send` invocations for reproducible results

### 11. Storage and Persistence

**Disk-Based Storage** (unverified)
- Persistent disk storage enables OPA to work with data exceeding memory resources
- NOT intended as primary source of truth for data
- When enabled: data/policies persist over restarts, per-query disk usage metrics reported, Prometheus metrics per storage operation exported
- OPA stores internal values (bundle metadata) in data store under `/system`
- Critical warning: OPA should never be sole source of truth, even with disk storage

**Bundle Persistence** (unverified)
- `bundles[_].persist: true` enables OPA to persist activated bundles to disk
- On startup, OPA attempts to read bundle from disk (recovery when bundle server unavailable)
- Default location: `./.opa/bundles/<bundle-name>/bundle.tar.gz` (current working directory)
- Best-effort basis: errors during load/activation surfaced in bundle status update
- Important limitation: delta bundles NOT persisted to disk (only snapshot bundles)

## Confidence: 0.85

### Rationale

- Official OPA documentation available for core features (testing, bundles, CI/CD, decision logs, storage)
- Styra (OPA creators) provides well-documented commercial management plane (DAS) and linter (Regal)
- OPAL (Permit.io) provides well-documented open-source real-time update layer with production adoption evidence
- Open Policy Containers (OPCR) CNCF Sandbox project with clear OCI integration documentation
- Conftest official documentation and GitHub repository cover policy testing use cases
- Multiple tier 3 and tier 4 sources corroborate patterns and best practices
- Known gaps exist (e.g., canary deployment patterns not extensively documented for OPA-specific use cases)
- Some information from GitHub issues indicates evolving features (delta bundles, ETag caching bugs, persistence in cloud-native environments)

## Open Questions

### 1. Policy Lifecycle Orchestration Patterns

- How do organizations manage policy promotion across environments (dev → staging → production)?
- What tooling exists for policy drift detection across multiple OPA deployments?
- Are there established patterns for blue/green or canary deployments specifically for OPA policies (not just general canary deployment strategies)?
- How do teams handle policy rollback in production when issues detected?

### 2. Testing Maturity and Coverage

- What are realistic code coverage targets for Rego policies in production systems?
- How do teams measure test effectiveness beyond line coverage (mutation testing for Rego)?
- What percentage of teams use Conftest vs. native `opa test` in CI/CD?
- Are there established integration testing patterns for OPA policies with real services?

### 3. Bundle Distribution Scale and Performance

- What are typical bundle polling intervals in production (balance between update latency and server load)?
- How do organizations handle bundle distribution to thousands of OPA instances (CDN patterns)?
- What are bundle size limits before performance degrades?
- How prevalent is delta bundle adoption vs. snapshot bundles?

### 4. Security and Signing Adoption

- What percentage of OPA deployments use bundle signing in production?
- Is cosign the de facto standard for OPA bundle signing, or are other approaches common?
- How do teams manage key distribution for bundle signature verification?
- Are there documented patterns for key rotation without OPA downtime?

### 5. Decision Logging in Production

- What are typical decision log volumes in production API authorization scenarios?
- How do teams handle PII/sensitive data in decision logs for compliance?
- What percentage of deployments forward decision logs to centralized observability vs. local storage?
- Are there performance impacts from decision logging at high query rates?

### 6. Styra DAS vs. Self-Built Management Planes

- What percentage of OPA production deployments use Styra DAS vs. self-built management planes?
- What are typical engineering costs to build/maintain a self-built OPA management plane?
- What features of Styra DAS are most valued in production (impact analysis, decision replay, policy distribution)?
- Are there open-source alternatives to Styra DAS besides OPAL?

### 7. OPAL Adoption and Maturity

- How does OPAL real-time update performance compare to bundle polling (latency, resource usage)?
- What are failure modes for OPAL's WebSocket PubSub approach (e.g., network partitions)?
- How do organizations handle OPAL server high availability and failover?
- What percentage of OPAL deployments use it for policy updates vs. data updates?

### 8. Regal Adoption and Customization

- What percentage of OPA users integrate Regal into their CI/CD pipelines?
- How do teams customize Regal rules for organization-specific conventions?
- What are most commonly violated Regal rules in practice?
- Are there established patterns for integrating Regal with pre-commit hooks?

### 9. Multi-Engine and Multi-Cloud Patterns

- How do organizations manage OPA policies across multiple cloud providers?
- Are there patterns for synchronizing policies between OPA and other policy engines (Kyverno, Cedar)?
- How do teams handle policy conflicts when multiple engines enforce overlapping concerns?

### 10. FastAPI Integration Specifics

- What are FastAPI-specific patterns for OPA integration (middleware, dependency injection)?
- How do teams handle OPA availability failures in FastAPI applications (fallback policies, circuit breakers)?
- Are there established libraries for OPA + FastAPI integration, or do teams build custom clients?
- What are latency impacts of OPA calls in Python/FastAPI request paths (async patterns)?
