---
description: Generates context-specific subtraction questions that find what to cut, defer, or never build without losing value.
disable-model-invocation: true
---

# Subtraction Questions

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


Generate context-specific subtraction questions that find what can be removed, deferred, or never built without losing value.

- Use any topical focus in the user instruction; otherwise use the current code, product, plan, or topic.
- Examine features, steps, options, configuration, dependencies, abstractions, documents, meetings, and commitments.
- Consider deletion, deferral, merging, replacing custom work with existing capabilities, and narrowing scope.
- Consider what nobody uses, what exists only for hypothetical needs, and what costs more to maintain than it returns.
- Make every question name a concrete removal candidate and the value or cost it would free.
- Never recommend removing something the context shows is required, used, or contractually promised.
- Exclude generic minimalism advice, cosmetic trimming, and cuts whose loss outweighs the saving.

THINK HARD and THINK HARDER and ULTRATHINK.

Use the local `C` prefix.

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
