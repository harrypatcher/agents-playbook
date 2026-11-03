# agents-playbook

Reusable skills, commands, and instruction snippets for coding agents.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

```text
skills/                                  # loaded when a task matches the description
  skill-brutal                           Blunt critique; brutal, harsh, roast, no-sugarcoating, or unfiltered requests.
  skill-expert                           Explicit request for expert insights, non-obvious optimizations, or expert-level code/config review.
  skill-obvious                          Requests for practical obvious or non-obvious tips, tricks, hacks, shortcuts, and high-ROI moves.
  skill-risk-map                         Maps assumptions, failure modes, edge cases, and other risks. Use when asked for a risk map, preflight, or what could go wrong, or before irreversible or high-stakes decisions.
  skill-xray                             Explicit xray/x-ray or adversarial requests, blindspots, improvement potential, inefficiencies, “what am I missing?”, critiques, or multi-perspective analysis.
commands/                                # invoked as slash commands
  /questions-agents-check-understanding  Generates context-specific self-check questions the agent should ask itself to test whether it fully understood the request.
  /questions-decision                    Generates context-specific decision questions that sharpen concrete choices and trade-offs.
  /questions-first-principles            Generates context-specific first-principles questions that expose fundamental truths and assumptions.
  /questions-goals                       Generates context-specific, thought-provoking questions focused on the user's goals and whether the current work serves them.
  /questions-hacker                      Generates context-specific hacker-style questions using unconventional but practical approaches.
  /questions-inspiration                 Generates context-specific inspiration questions that open distinct, thought-provoking directions like the Q1–Q5 block.
  /questions-monetization                Generates context-specific monetization questions that uncover concrete and practical revenue mechanisms.
  /questions-proposal                    Generates context-specific proposal questions that offer concrete next actions for selection.
  /questions-solution                    Generates context-specific solution questions that identify plausible implementation failures and root-cause fixes.
  /questions-subtract                    Generates context-specific subtraction questions that find what to cut, defer, or never build without losing value.
  /questions-unethical                   Generates context-specific unethical questions that expose aggressive but practical code and product advantages.
  /questions-user                        Generates context-specific user questions that expose how the current work affects the people who use it.
  /questions-verification                Generates context-specific verification questions focused on decisive, falsifiable evidence.
snippets/                                # pasted into global agent instructions
  snippet-q-questions                    Q1–Q5 Contract
```
<!-- END GENERATED CONTENTS -->

## License

[MIT](LICENSE)
