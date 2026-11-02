# agents-playbook

Reusable skills, commands, and instruction snippets for coding agents.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

```text
skills/                        # loaded when a task matches the description
  skill-brutal                 Blunt critique or delegation analysis; brutal, harsh, roast, no-sugarcoating, or unfiltered requests.
  skill-expert                 Explicit request for expert insights, non-obvious optimizations, or expert-level code/config review.
  skill-obvious                Requests for practical obvious or non-obvious tips, tricks, hacks, shortcuts, and high-ROI moves.
  skill-xray                   Explicit xray/x-ray or adversarial requests, blindspots, improvement potential, inefficiencies, “what am I missing?”, specific critiques/suggestions, adversarial feedback, or multi-perspective analysis.
commands/                      # invoked as slash commands
  /questions-decision          Generates context-specific decision questions that sharpen concrete choices and trade-offs.
  /questions-first-principles  Generates context-specific first-principles questions that expose fundamental truths and assumptions.
  /questions-hacker            Generates context-specific hacker-style questions using unconventional but practical approaches.
  /questions-monetization      Generates context-specific monetization questions that uncover concrete and practical revenue mechanisms.
  /questions-proposal          Generates context-specific proposal questions that offer concrete next actions for selection.
  /questions-solution          Generates context-specific solution questions that identify plausible implementation failures and root-cause fixes.
  /questions-unethical         Generates context-specific unethical questions that expose aggressive but practical code and product advantages.
  /questions-verification      Generates context-specific verification questions focused on decisive, falsifiable evidence.
snippets/                      # pasted into global agent instructions
  snippet-q-questions          Q1–Q5 Contract
```
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
