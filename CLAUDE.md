# cited-research

Citation-backed research documents produced by the `/cited-research` skill.

## Research Fan-Out (Batch Research via Screen)

When researching multiple tools/topics in the same domain, use a screen session to run them in parallel.

### Setup

1. **Prompt files** — one `.md` per topic in `prompts/<batch-name>/`. Use `scripts/generate-workflow-prompts.sh` as a template for generating them from a shared prompt template with per-topic substitution.

2. **Screenrc** — a `<batch-name>.screenrc` in the repo root. Each window launches an interactive `claude` session with the skill invocation as the initial prompt:
   ```text
   screen <N>
   title "<topic>"
   stuff "claude \"/cited-research prompts/<batch-name>/<topic>.md\" \015"
   ```

3. **Launch** (from repo root):
   ```bash
   screen -c <batch-name>.screenrc -S <batch-name>
   ```

### Notes

- The prompt template source lives outside this repo (e.g., `~/source/personal-assistant-work/scratch/`)
- Each session runs the `/cited-research` skill interactively, which handles web research, citation tracking, and audit
- Output lands in `research/<topic>/` following the standard structure (analysis, citations, references, audit)
- Use `Ctrl-A <number>` to switch between windows, `Ctrl-A "` to list all windows
