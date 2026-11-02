# agents-playbook

Reusable skills, commands, and instruction snippets for coding agents.

## Layout

```text
skills/
  <skill-name>/
    SKILL.md        # instructions with name and description frontmatter
    ...             # optional scripts, references, or templates
commands/
  <command-name>.md # slash command prompt
snippets/
  snippet-<name>.md # instruction block to paste into AGENTS.md or CLAUDE.md
```

- [`skills/`](skills/): self-contained capabilities that an agent loads when a task matches the skill description.
- [`commands/`](commands/): prompts that you invoke explicitly as slash commands.
- [`snippets/`](snippets/): always-on rules that you paste into a global instruction file.

## Installation

Copy or symlink the items you want into your agent's configuration directory.
For Claude Code:

```bash
git clone https://github.com/harrypatcher/agents-playbook.git
ln -s "$PWD/agents-playbook/skills/<skill-name>" ~/.claude/skills/<skill-name>
ln -s "$PWD/agents-playbook/commands/<command-name>.md" ~/.claude/commands/<command-name>.md
```

Symlinks keep installed items current after `git pull`.

## License

[MIT](LICENSE)
