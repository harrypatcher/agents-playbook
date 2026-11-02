# Skills

Each skill lives in its own directory named after the skill.
The directory contains a `SKILL.md` file and optional supporting files.

```markdown
---
name: skill-name
description: One sentence that tells the agent when to use this skill.
---

# Skill Name

Instructions the agent follows when the skill applies.
```

The agent selects a skill by its `description`, so the description states the trigger, not the content.
