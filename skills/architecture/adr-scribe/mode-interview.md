# Mode: Interview — drafting a new decision

> Interview the user to draft a new Architecture Decision Record. Structured dialogue with **explicit validation at every phase**.

## When to use

- The user wants to document a new architectural decision they just made or are currently making.
- Typical phrasings: *"We decided to use X"*, *"Help me write an ADR for Y"*, *"Interview me about Z"*
- No existing ADR to review or codebase to infer from.

## Cardinal rule

**Never deliver without explicit validation.** The ADR emerges from dialogue, not from a one-shot generation. Ask a maximum of 3 questions at a time.

## Phase 0 — Framing

1. What is the title or the core decision we are documenting?
2. What is the status? (Proposed, Accepted, etc. Default to Accepted if they already made the decision).

## Phase 1 — Context

Dialogue:
- *"What is the problem we are solving or the business context that forced this decision?"*
- *"Were there any specific constraints (e.g., cost, compliance, team skills)?"*

Present a draft of the **Context** section. Ask for validation.

## Phase 2 — Alternatives

Dialogue:
- *"What were the other options considered?"*
- *"Why were they rejected? What were their drawbacks?"*

If the user only gives one option, politely remind them that a decision implies a choice between alternatives. If there truly were no other options, document it as a constraint rather than a decision.

Present a draft of the **Considered Options** section. Ask for validation.

## Phase 3 — Consequences

Dialogue:
- *"What are the positive outcomes of choosing this option?"*
- *"What are the negative consequences? (e.g., maintenance burden, cost, learning curve)"*

**Crucial:** Every decision has a trade-off. If the user provides no negatives, suggest potential ones and ask if they apply.

Present a draft of the **Decision Outcome** and **Consequences** sections.

## Phase 4 — Finalization

1. Run the checklist ([`review-checklist.md`](review-checklist.md)) — call out points that raise questions.
2. Deliver the final MADR template to the destination.
3. **Cross-skill integration:** Ask the user: *"Would you like me to update your C4 diagrams to reflect this new decision? (Using the c4designer skill)"*

## Links

- ← Back: [`SKILL.md`](SKILL.md)
- Deliverable template: [`adr-template.md`](adr-template.md)
- Filled-out example: [`examples/0001-use-postgresql-over-mongodb.md`](examples/0001-use-postgresql-over-mongodb.md)
- Review checklist: [`review-checklist.md`](review-checklist.md)
