---
name: skill-xray
description: 'explicit xray/x-ray or adversarial requests, blindspots, improvement potential, inefficiencies, “what am I missing?”, specific critiques/suggestions, adversarial feedback, or multi-perspective analysis.'
---

Use GAN-style thinking: alternate between a generator and discriminator.
The generator proposes concrete improvements, simplifications, risks, and leverage points.
The discriminator attacks proposals for weak assumptions, missing evidence, and second-order effects.
It also attacks cost, failure modes, and misleading conclusions.
Iterate until only high-signal critiques and actionable suggestions remain.
Report the result, not the internal debate.
Report specific critiques, concrete suggestions, improvement potential, and inefficiencies.
Report obvious and non-obvious issues and blindspots that I, you, or we together see or miss.

## Scope Boundaries

- Structured or preflight risk analysis belongs to `skill-risk-map`.
- Explicit xray/x-ray or adversarial analysis intent overrides that routing.
- Preflight risk terms such as blindspots, failure modes, edge cases, assumptions, and constraints do not select xray.
- Tradeoffs, dependencies, invariants, verification gaps, and regressions also do not select xray by themselves.
- Expert-level implementation optimization without adversarial or blindspot intent belongs to `skill-expert`.
- Generic codebase analysis does not invoke this skill.
- Machine learning, neural-network architecture, medical imaging, and security-scanning tools are unrelated to this skill.
- If another explicitly loaded companion skill requires a language, that companion language contract takes precedence.

## Language

- Thinking and reasoning MUST be in English.
- Answer in natural German by default, unless the user explicitly requests another language.
- Canonical English field names define semantic identity and order, not the rendered language.
- Localize human-facing headings, labels, categories, values, and examples into that language.
- Keep a human-facing token exact only when the skill marks it as literal or machine-readable.
- Preserve the canonical contract's structure, order, meaning, modality, and completeness.
- Keep machine formats and code-like tokens exact.
- Never emit parallel schemas in two languages.
- Retain English technical terms when the answer language is less precise or natural.
