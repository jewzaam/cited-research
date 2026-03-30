# Multi-User Collaboration Patterns

Dimension covering how multiple contributors coordinate using GitHub Issues in a single mono-repo.

Sources: see [citations.md](../citations.md) for full details.

## Assignment Strategies

GitHub supports up to **10 assignees per issue/PR** [10]. However, **team-based assignment is not natively supported** for issues — teams can only be assigned as PR reviewers [10].

Common workaround: assign all team members individually, then members un-assign themselves when another claims the work [10].

## Team-Based Filtering

GitHub search does not index team information [12]. You cannot search or filter issues by GitHub Team membership. Workarounds:
- Custom scopes with team-relevant repos
- CODEOWNERS for PR-based team routing (not issue routing) [13]
- Labels with team identifiers (manual)
- Custom "Team" field in Projects [12]

## Views for Team Coordination

GitHub Projects views enable team-specific filtering by assignee, labels, and repository [4][11]. Best practices from GitHub [11]:
- Use @mentions to alert collaborators
- Create issue dependencies to clarify blocking relationships
- Maintain project READMEs with purpose, view guidance, and contacts
- Post status updates marking project health as "On track" or "At risk"
- Use column limits on board views

**Key limitation**: all views are visible to all project members — no private/personal views exist [6].

## Multi-Team Project Organization

Two approaches with distinct tradeoffs [12]:

| Approach | Advantage | Disadvantage |
|----------|-----------|--------------|
| Separate project per team | Team autonomy, focused views | Custom field metadata doesn't sync between projects; status transitions lack history |
| Single unified project | Cross-team visibility, consistent metadata | Scalability concerns; view clutter |

This discussion remained unanswered in the GitHub community, suggesting no established best practice exists [12].

## CODEOWNERS for Ownership

CODEOWNERS file maps directory paths to teams/individuals for automatic PR reviewer assignment [13]:

- File location: `.github/`, repository root, or `docs/` [13]
- Patterns follow gitignore rules (no negation, no character ranges) [13]
- Code owners are auto-requested for PR review when matching files change [13]
- Requires **write access** to the repository [13]
- File size limit: 3 MB [13]
- **Does not affect issue assignment or routing** — only PR reviews [13]

## Notification Management

Automatic subscriptions trigger when: assigned to issue/PR, opening issue/PR, commenting, being @mentioned, or when your team is @mentioned [11].

For large teams, this creates notification fatigue. Best practices include:
- "Participating and @mentions" notification setting for balance
- Triage inbox with "Done" state
- Saved searches for relevant conversations
- Disable notifications for non-critical team @mentions

## Team Size Friction Points

| Size | Experience |
|------|-----------|
| 2-5 developers | Minimal friction; informal communication suffices |
| 5-15 developers | Boundary confusion emerges; need explicit CODEOWNERS, label conventions |
| 15+ developers | Exponential communication path growth; heavy tooling investment required |

Microsoft scaled GitHub usage to 25,000 engineers but required significant tooling and process investment [14].

## Gaps and Limitations

- No team-based issue assignment (teams only assignable as PR reviewers) [10]
- No filtering by GitHub Team membership in search or Projects [12]
- No private/personal views for team-specific boards [6]
- CODEOWNERS only affects PR reviews, not issue routing [13]
- Multi-team project organization lacks established best practices from GitHub [12]
