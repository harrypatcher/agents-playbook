---
description: Generates context-specific monetization questions that uncover concrete and practical revenue mechanisms.
---

# Monetization Questions

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
- Format each line as `**<prefix><number>** — [question]`, using the command's prefix and numbering from 1.


Generate context-specific monetization questions that uncover practical revenue opportunities in the current context.

- Use any topical focus in the user instruction; otherwise use the current code, product, business, or topic.
- Examine existing assets, user flows, distribution, data, integrations, and operational capabilities.
- Consider hidden revenue streams, affiliate flows, advertising, licensing, data products, platform leverage, and paid services.
- Explore aggressive or ethically contentious mechanisms when relevant instead of defaulting to subscriptions or upselling.
- Prefer mechanisms that avoid intrusive user interaction and fit the user's realistic capabilities.
- Make every question identify a concrete revenue mechanism or integration point.
- Exclude generic monetization advice, unrealistic scale assumptions, absurd ideas, blockchain, and cryptocurrency.

THINK HARD and THINK HARDER and ULTRATHINK.

Use the local `M` prefix.

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
