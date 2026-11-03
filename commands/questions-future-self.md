---
description: Generates context-specific future-self questions that expose what the current work will cost whoever maintains it months from now.
disable-model-invocation: true
---

# Future-Self Questions

<user-instruction>
$ARGUMENTS
</user-instruction>

- Generate the number of context-specific questions explicitly requested in the user instruction.
- Without an explicit count, generate ten questions.
- Treat a standalone positive integer as the question count; otherwise count numbers only when they explicitly request questions.
- Make the questions materially different and individually capable of changing the user's reasoning or action.
- Each question MUST have between 7 and 15 words.
- Count words after the `—` marker only.
- Return only consecutive question lines, without blank lines or surrounding commentary.
- Never append the global Q1–Q5 block after the question lines.
- Format each line as `• **<prefix><number>** — [question]`, using the command's prefix and numbering from 1.
- Draft more candidates internally than requested and drop near-duplicates.
- Order the questions by expected impact, strongest first, unless the command defines another order.
- A later selection such as `<prefix><number>` follows the Q selection rules and refers to this list.


Generate context-specific questions the user's future self will want answered now.
Assume that future self returns months later without today's context.

- Use any topical focus in the user instruction; otherwise use the current code, system, configuration, or decisions.
- Probe what exists only in current memory: rationale, rejected alternatives, workarounds, and implicit invariants.
- Probe ownership, the source of truth, and how to find the right entry point quickly.
- Probe drift in dependencies, versions, external APIs, credentials, and assumptions that change silently.
- Probe what breaks quietly, how anyone would notice, and how to recover or roll back.
- Probe names, structure, and layout that will confuse a reader without today's context.
- Probe temporary decisions, TODOs, and shortcuts likely to become permanent.
- Make every question name a concrete artifact and the future cost or confusion it creates.
- Never invent history, owners, or failures the context does not support.
- Exclude generic documentation checklists and questions that existing docs or code already answer.

THINK HARD and THINK HARDER and ULTRATHINK.

Use the local `L` prefix.

## Language

- Thinking and reasoning MUST be in English.
- Answer in natural German by default, unless the user explicitly requests another language.
- Canonical English field names define semantic identity and order, not the rendered language.
- Localize human-facing headings, labels, categories, values, and examples into that language.
- Keep a human-facing token exact only when the command marks it as literal or machine-readable.
- Preserve the canonical contract's structure, order, meaning, modality, and completeness.
- Keep machine formats and code-like tokens exact.
- Never emit parallel schemas in two languages.
- Retain English technical terms when the answer language is less precise or natural.
