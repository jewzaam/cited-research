# cited-research

Citation-backed research documents produced by the `/cited-research` skill.

## CHANGELOG.md Maintenance

[`CHANGELOG.md`](CHANGELOG.md) at the repo root is the append-only log of research adds and updates. Because `index.md` is sorted by creation (not revision), the changelog is the canonical place to spot recent work.

Whenever a research topic is added or updated, append an entry to `CHANGELOG.md` as part of the same change:

- Group by date (`YYYY-MM-DD`) with newest date at top.
- One bullet per topic per action: `- Added [Title](research/slug/)` or `- Updated [Title](research/slug/)`.
- Use the `Last revised` date from the topic's `README.md` as the group date.
- `Title` should match the topic's entry in `index.md`.
- If the date group already exists, append the bullet to it; otherwise create a new date group at the top.
- Keep it simple — no version numbers, no per-entry descriptions. `index.md` carries the summaries.
