---
description: Generates context-specific verification questions focused on decisive, falsifiable evidence.
disable-model-invocation: true
---

# Verification Questions

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


Generate context-specific verification questions that test what evidence establishes and what remains uncertain.

- Use any topical focus in the user instruction; otherwise use the current topic.
- Consider decisive evidence, falsifiers, baselines, observability, confounders, measurement quality, and unresolved uncertainty.
- Require each question to name a concrete observation, test, metric, or evidence source and the result that would change a decision.
- Distinguish what is observed from what is inferred.
- Never invent evidence, measurements, access, or certainty not present in the context.
- Select only relevant angles.
- Exclude generic QA checklists, “test more,” non-falsifiable prompts, vanity metrics, and implementation advice.
- Exclude experiments incapable of changing a decision.

THINK HARD and THINK HARDER and ULTRATHINK.

Use the local `V` prefix.

## Language

- Thinking and reasoning MUST be in English.
- Answer the user in natural German.
- Canonical English field names define semantic identity and order, not the rendered language.
- Localize human-facing headings, labels, categories, values, and examples into idiomatic German.
- Keep a human-facing token exact only when the command marks it as literal or machine-readable.
- Preserve the canonical contract's structure, order, meaning, modality, and completeness.
- Keep machine formats and code-like tokens exact.
- Never emit parallel English and German schemas.
- Retain English technical terms when German is less precise or natural.
