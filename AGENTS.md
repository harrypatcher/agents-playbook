# AGENTS.md

This public repository publishes reusable skills and commands for coding agents.
Everything committed here is world-readable, so every change MUST be safe to publish.

## Layout

- `skills/<skill-name>/SKILL.md`: one directory per skill, with optional supporting files beside `SKILL.md`.
- `commands/<command-name>.md`: one Markdown file per slash command.
- `skills/README.md` and `commands/README.md` own the file formats; keep them in sync with format changes.
- `README.md` owns the repository overview and installation instructions.

## Skills

- Directory names and the frontmatter `name` MUST match and use kebab-case.
- The frontmatter `description` MUST state when to use the skill in one sentence.
- A skill MUST work on its own and MUST NOT depend on files outside its directory.
- Supporting scripts MUST run without private tools, accounts, or local configuration.

## Commands

- Filenames use kebab-case because the filename becomes the slash command name.
- The frontmatter `description` MUST summarize the command in one sentence.
- Use `$ARGUMENTS` for user input instead of hardcoded values.

## Privacy

- NEVER commit personal names, e-mail addresses, usernames of other accounts, or private repository names.
- NEVER commit hostnames, IP addresses, absolute home paths, or machine-specific configuration.
- NEVER commit tokens, keys, passwords, or other credentials.
- Replace environment-specific values with placeholders such as `<project-dir>` or `$HOME`.
- Review the staged diff for these traces before every commit.
- NEVER override the repository's configured Git identity.

## Writing

- Write all content in English.
- Put each Markdown sentence on its own line so diffs show changes per sentence.
- Keep instructions decision-dense and free of filler.

## Commits

- Use Conventional Commits, for example `feat(skills): add code-review skill`.
- Use `skills`, `commands`, or `docs` as the scope.
