# Commands

Each command is one Markdown file, and its filename becomes the slash command name.
`commands/review.md` becomes `/review`.
Commands are user-invocable only.
`disable-model-invocation: true` keeps the model from running a command on its own and keeps its description out of the model context until the user invokes it.

```markdown
---
description: Short summary shown in the command list.
disable-model-invocation: true
argument-hint: <optional arguments>
---

Prompt text sent to the agent.
`$ARGUMENTS` is replaced with the text typed after the command.
```
