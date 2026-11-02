# agents-playbook

Reusable skills, commands, and instruction snippets for coding agents.

<!-- BEGIN GENERATED CONTENTS -->
<!-- END GENERATED CONTENTS -->

## Installation

Clone the repository and symlink what you need into your agent's directories:

```bash
git clone https://github.com/harrypatcher/agents-playbook.git
ln -s "$PWD/agents-playbook/skills/<skill-name>" <agent-skills-dir>/
ln -s "$PWD/agents-playbook/commands/<command-name>.md" <agent-commands-dir>/
```

Paste snippets into your agent's global instructions, such as `AGENTS.md`.
Symlinks stay current after `git pull`.

## License

[MIT](LICENSE)
