# Commands

Each command is one Markdown file, and its filename becomes the slash command name.
`commands/review.md` becomes `/review`.

```markdown
---
description: Short summary shown in the command list.
argument-hint: <optional arguments>
---

Prompt text sent to the agent.
`$ARGUMENTS` is replaced with the text typed after the command.
```
