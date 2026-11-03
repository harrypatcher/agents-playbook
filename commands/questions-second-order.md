---
description: Generates context-specific second-order questions that expose indirect, delayed, and feedback-driven consequences of the current work.
disable-model-invocation: true
---

# Second-Order Questions

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


Generate context-specific second-order questions that look past the immediate effect to what follows from it.

- Use any topical focus in the user instruction; otherwise use the current change, decision, plan, or topic.
- Start from the intended first-order effect and ask what it causes next.
- Probe changed incentives and how users, agents, teammates, or systems adapt their behavior in response.
- Probe feedback loops, accumulation over time, delayed costs, and effects that compound or reverse.
- Probe downstream consumers, dependent systems, and processes that inherit the change.
- Probe how success itself changes conditions, such as more load, more dependence, or new expectations.
- Probe precedent: what the change normalizes and what it makes easier or harder next.
- Make every question trace a concrete chain from the current work to a later consequence.
- Never invent consequences, actors, or mechanisms the context does not support.
- Exclude first-order effects, generic butterfly-effect speculation, and consequences too remote to change the work.

THINK HARD and THINK HARDER and ULTRATHINK.

Use the local `N` prefix.

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
