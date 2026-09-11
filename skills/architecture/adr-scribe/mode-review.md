# Mode: Review — critiquing an existing ADR

> Critique an existing Architecture Decision Record for completeness, objectivity, and clarity.

## When to use

- The user provides an existing ADR and asks for feedback.
- Typical phrasings: *"Is this ADR good?"*, *"Review this decision record"*, *"Critique my ADR"*

## Cardinal rule

**Be objective and constructive.** Use the [`review-checklist.md`](review-checklist.md) as your absolute source of truth for the critique.

## Phase 1 — Analysis against the Checklist

Read the provided ADR. Compare it against the rules in `review-checklist.md`.

Pay special attention to:
- Are there alternatives listed? If not, it's not a decision.
- Are the negative consequences documented? Every decision has trade-offs.
- Is the context objective? (e.g., it shouldn't just be "We wanted to use Redis").

## Phase 2 — Presentation

Group your feedback into two categories:

### 🔴 Critical Issues (Missing completely)
e.g., "You haven't documented any negative consequences. What happens if this service goes down?"

### 🟡 Improvements (Clarity/Formatting)
e.g., "The title could be more descriptive."

## Phase 3 — Refinement

Ask the user: *"Would you like me to rewrite the ADR incorporating these improvements? I will need you to answer the missing points first."*

If yes, gather the missing info and rewrite.

## Links

- ← Back: [`SKILL.md`](SKILL.md)
- Review checklist: [`review-checklist.md`](review-checklist.md)
