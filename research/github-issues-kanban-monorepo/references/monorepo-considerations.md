# Monorepo-Specific Considerations

Dimension covering how mono-repo structure creates unique issue management challenges.

Sources: see [citations.md](../citations.md) for full details.

## Path-Based Ownership (CODEOWNERS)

CODEOWNERS maps directory paths to teams/individuals [13]:

```
# Example CODEOWNERS for a mono-repo
/packages/api/       @org/api-team
/packages/frontend/  @org/frontend-team
/packages/shared/    @org/platform-team
```

**Key limitations for mono-repos** [13]:
- Only one CODEOWNERS file at repo root (not designed for distributed ownership)
- Tools like `codeowners-generator` compile distributed files into a single file
- Only affects PR reviewer assignment, **not issue routing**
- Requires write access (triage role insufficient)
- Pattern matching confusion (e.g., `/docs/` vs `docs/*`) causes silent failures
- File size limit: 3 MB (large mono-repos may exceed)

## Label Strategies for Mono-Repos

Mono-repos benefit from area/component labels to identify affected modules [15]:

| Pattern | Example | Used By |
|---------|---------|---------|
| Component: prefix | `Component: Build Infrastructure` | React [36] |
| Tech: prefix | `Tech: Monorepo` | React Native [36] |
| SIG prefix | `sig/architecture`, `area/code-organization` | Kubernetes [36] |
| App/Package prefix | `app:web`, `app:api`, `package:ui` | GitScrum pattern [34] |

Auto-labeling for mono-repos: `monorepo-pr-repo-labeler` GitHub Action labels PRs with affected modules based on changed file paths. For issues, automated labeling based on content/mentions requires custom Actions.

## CI Scope and Selective Testing

Change-based testing is critical for mono-repo CI/CD [33][34]:

| Tool | Approach |
|------|----------|
| Nx `nx affected` | Identifies affected packages from dependency graph |
| Turborepo | Fast task orchestration with workspace awareness |
| GitHub Actions path filters | Subdirectory-based triggers per package |
| Bazel | Hermetic builds, language-agnostic, multi-platform |

Real-world impact: change-based testing can reduce test time from 45 minutes to under 10 minutes [34].

**Interaction with issue tracking**: CI results (pass/fail per package) can be correlated to issues via automated comments or status updates, but this requires custom workflow implementation.

## Issue Routing

Tools for routing issues to the right team in a mono-repo:

| Tool | Mechanism |
|------|-----------|
| Monorobot [35] | Slackbot routing notifications by file prefixes, labels, CI status |
| GitHub Agentic Workflows [27] | AI-powered auto-labeling, summarization, routing |
| trIAge | LLM-based issue categorization and duplicate detection |
| Custom GitHub Actions | Label-triggered or content-triggered routing |

Monorobot (by Ahrefs) is specifically designed for mono-repos [35]:
- Routes GitHub notifications to Slack channels based on file prefixes
- Handles issue/PR labels and CI build status
- Maps GitHub handles to Slack users for @mentions
- Built in OCaml, runs as HTTP webhook server

## Cross-Package Dependencies

| Challenge | Impact |
|-----------|--------|
| API changes in one package affect downstream consumers [34] | Requires identifying all usage points across packages |
| Shared library updates cascade | Issues may need to track impact across multiple areas |
| Version conflicts between packages [34] | Inconsistent standards create friction |

Nx and Turborepo automatically identify affected packages, but this data doesn't directly feed into GitHub Issues [34]. Teams must build custom integrations to surface cross-package impact in issue metadata.

## Large Open-Source Mono-Repo Examples

**Kubernetes** [36]:
- Found that "a large monorepo works for Google, but not on GitHub"
- Cited ACLs, notification management, issue triage, PR reviews, merge conflicts as velocity limiters
- Uses labels: `area/code-organization`, `sig/architecture` for routing
- Peribolos for managing team permissions via configuration files

**React**:
- Yarn workspaces structure with 13 packages
- Labels: `Component: Developer Tools`, `Type: Feature Request`

## GitHub Well-Architected Guidance

GitHub's official mono-repo recommendations [33]:
1. Align organization with logical projects, team boundaries, release cadences
2. Use matrix builds, labeled PRs, subdirectory-based triggers for CI
3. Assign permissions precisely for high-impact areas
4. Implement well-defined branch protection and review policies
5. Adopt clear versioning strategies to prevent cascading incompatibilities
6. Plan for scalability concerns (clone time growth)

## Gaps and Limitations

- CODEOWNERS only affects PR reviews, not issue routing [13]
- Mono-repo build tools (Nx, Turborepo, Bazel) don't directly integrate with GitHub Issues [34]
- No native GitHub feature for package-scoped project views or filtering [4]
- Limited documentation on combining CODEOWNERS + bot automation + labels into cohesive issue routing
- No cross-package dependency visualization within GitHub Issues
