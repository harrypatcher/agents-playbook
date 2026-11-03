---
name: skill-risk-map
description: 'Maps assumptions, failure modes, edge cases, and other risks across fixed lenses. Use when the user asks for a risk map, risk preflight, or what could go wrong, or before an irreversible or high-stakes decision.'
---

Run a structured risk map when the user asks for risk or preflight analysis.
Also run it before irreversible, expensive, public, or data-destructive decisions.

Use `skill-xray` for adversarial critique.
Obvious insights do not require this preflight analysis.

## Methodology

Analyze the target through distinct lenses.
Do not collapse these into synonyms.

- assumptions: unverified claims that carry the conclusion.
- constraints: hard rules, limits, policies, APIs, compatibility requirements, or user preferences that bound valid solutions.
- failure modes: concrete ways the plan, code, process, or verification can fail.
- edge cases: rare but plausible inputs, states, timings, permissions, environments, or user flows.
- tradeoffs: real cost/benefit tensions between viable options.
- dependencies: external, implicit, transitive, runtime, operational, or human prerequisites.
- invariants: facts or states that must remain true before, during, and after the change.
- second-order effects: consequences after the direct change, including maintenance, operations, user behavior, and future work.
- ambiguities: multiple plausible meanings in requirements, names, APIs, data, or observed behavior.
- verification gaps: what is not yet proven by tests, commands, inspection, or source evidence.
- regressions: existing behavior, contracts, workflows, or integrations that could break.
- irreversibility: actions that are hard to roll back, data-destructive, public, expensive, or stateful.
- scope creep: additions that exceed the ask or silently change the contract.
- false positives/negatives: things tools, tests, heuristics, or reasoning may incorrectly flag or miss.

Rules:

- Separate real findings from generic possibilities.
- Prefer concrete evidence from the conversation, uploaded files, cited sources, and specific failure examples.
- If a lens has no meaningful finding, omit it unless the absence is itself important.
- Distinguish “must fix now” from “watch/verify”.
- Use findings to adjust the plan, not to create analysis theater.

## Language

- Thinking and reasoning MUST be in English.
- Answer in the language the user writes in.
- Canonical English field names define semantic identity and order, not the rendered language.
- Localize human-facing headings, labels, categories, values, and examples into that language.
- Keep a human-facing token exact only when the skill marks it as literal or machine-readable.
- Preserve the canonical contract's structure, order, meaning, modality, and completeness.
- Keep machine formats and code-like tokens exact.
- Never emit parallel schemas in two languages.
- Retain English technical terms when the answer language is less precise or natural.

## Output Format

Use compact sections.
Do not use markdown tables.
The template fixes order and labels only.
Omit lenses without meaningful findings.

```
## Risk Map

- **Assumptions**
  - [finding]
- **Constraints**
  - [finding]
- **Failure Modes**
  - [finding]
- **Edge Cases**
  - [finding]
- **Tradeoffs**
  - [finding]
- **Dependencies**
  - [finding]
- **Invariants**
  - [finding]
- **Second-Order Effects**
  - [finding]
- **Ambiguities**
  - [finding]
- **Verification Gaps**
  - [finding]
- **Regressions**
  - [finding]
- **Irreversibility**
  - [finding]
- **Scope Creep**
  - [finding]
- **False Positives/Negatives**
  - [finding]

## Action Impact

- [what changes in the plan because of these findings]
```

If the user asks for only a quick check, return only the top 3-7 highest-impact findings under `## Risk Map`.
Include `## Action Impact`.
