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
- Format each line as `<span style="color:<hex>">●</span> **<prefix><number>** — [question]`, using the command's prefix and numbering from 1.
- Color the dots in this order:

  1. `#ff6a6c`
  2. `#fe9032`
  3. `#fbcc02`
  4. `#9fe800`
  5. `#0be274`
  6. `#10d5bf`
  7. `#13d3ef`
  8. `#5ca5fe`
  9. `#a789fe`
  10. `#ec73fe`

- After the tenth color, start again with the first.
  For example, questions 11, 21, and 31 use color 1, and questions 12, 22, and 32 use color 2.
- The colors only help the reader keep track of lines and carry no meaning.


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

- Think and reason in English.
- Answer in the language of the conversation.
- Localize human-facing headings, labels, and values, but keep code-like tokens exact.
