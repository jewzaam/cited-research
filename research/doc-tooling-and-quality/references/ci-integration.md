# CI Integration Patterns for Documentation

How to wire documentation linting, link checking, and site builds into GitHub Actions for multi-repo setups. Sources: [citations.md](../citations.md).

## Recommended CI Pipeline

For a solo developer maintaining multiple projects with MkDocs Material + Vale + markdownlint + lychee:

```
on: [push, pull_request]

jobs:
  docs:
    runs-on: ubuntu-latest
    steps:
      # 1. Lint Markdown structure
      - markdownlint-cli2 (structural rules)

      # 2. Lint prose quality
      - vale (style guide enforcement)

      # 3. Check links
      - lychee (broken link detection)

      # 4. Build site
      - mkdocs build (verify site builds)

  deploy:
    if: github.ref == 'refs/heads/main'
    needs: docs
    # Deploy to GitHub Pages
```

## GitHub Actions for Each Tool

### Vale

Official Action: `vale-cli/vale-action` [20]. Reporter options: `github-pr-check` (annotations on files), `github-pr-review` (inline PR review comments), `github-check` (check run) [20]. Requires Vale >= 2.16.0 [20].

### markdownlint

`DavidAnson/markdownlint-cli2-action` — performance-optimized for large repos [15]. Supports custom rules via `rules` parameter [14].

### lychee

`lycheeverse/lychee-action` [19]. Configuration for args, format, output, fail behavior [19]. Repository-wide checking patterns available [44]. Can create GitHub Issues for broken links automatically [44].

### MkDocs Material Deployment

Official deployment workflow uses `mkdocs gh-deploy` with ghp-import tool [8][45]. Permissions required: `pages: write` and `id-token: write` [40]. Three-action sequence: `actions/configure-pages`, `actions/upload-pages-artifact`, `actions/deploy-pages` [40].

## Multi-Repo Reuse Patterns

### Reusable Workflows

GitHub supports reusable workflows via `workflow_call` trigger [42]. Nesting limits: 10 levels deep, 50 unique workflows maximum [42]. A central `.github` repository can host shared documentation workflows that individual project repos call.

Pattern: Create a reusable workflow in a shared repo that runs Vale + markdownlint + lychee with project-specific configuration passed as inputs.

### Shared Configuration

For consistent standards across repos:

- **Vale**: Share `.vale.ini` and custom styles via a dedicated styles repository. Vale's `Packages` directive can pull styles from remote sources [12].
- **markdownlint**: Share `.markdownlint.json` configuration (rules are version-stable, less need for centralization).
- **lychee**: Share `.lycheeignore` patterns for common false positives.

### Starter Workflows

GitHub's `actions/starter-workflows` repository [43] provides templates organized by category (ci, deployments, automation, pages) [43]. Templates use `.properties.json` metadata for UI display [43]. Organizations can create templates in their `.github` repository for org-wide use [43].

## GitHub Pages Deployment

Two approaches [40]:

1. **Official GitHub Actions** (recommended): `actions/configure-pages` → `actions/upload-pages-artifact` → `actions/deploy-pages`. Requires `pages: write` and `id-token: write` permissions [40].

2. **Third-party action**: `peaceiris/actions-gh-pages` — popular alternative supporting multiple generators [41].

Custom domains require DNS configuration (ALIAS, ANAME, or A records) and domain verification to prevent takeover attacks [40] (from discovery agent).

## Performance Considerations

- **Caching**: `setup-python` has built-in caching (`cache: 'pip'`) — reduces MkDocs install time on subsequent runs [40] (from discovery agent).
- **Incremental linting**: Run Vale and markdownlint on changed files only in PRs (via `git diff --name-only`), full scan on main branch merges.
- **Link checking frequency**: Run lychee on PRs for changed files, scheduled weekly for full-repo checks. Scheduled workflows auto-disable after 60 days of inactivity on public repos [40] (from discovery agent).
- **Pre-commit hooks**: Run markdownlint locally before commit. Target <10 seconds — developers skip slow hooks (from discovery agent).

## Gaps and Limitations

- No quantitative data on CI pipeline time impact for different repository sizes
- Multi-repo workflow coordination is still maturing — no established "best practice" pattern
- Reusable workflow debugging is harder than local workflows (limited visibility)
- Scheduled workflow reliability varies during high-load periods (start of each hour) (from discovery agent)
