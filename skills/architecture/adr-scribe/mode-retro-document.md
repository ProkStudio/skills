# Mode: Retro-Document — inferring a decision

> Analyze an existing artifact (PR, codebase, design doc) to infer and draft a historical ADR.

## When to use

- The user wants to document a decision that has already been implemented.
- Typical phrasings: *"Here's a PR that changed our auth, document it"*, *"Read this code and extract the decision"*, *"Retro-document our choice of Kafka"*

## Cardinal rule

**Explicitly state your assumptions.** Since you are inferring the "why" from the "what", you must ask the user to confirm your inferences before finalizing the draft.

## Phase 1 — Analysis

Analyze the provided context (code snippet, PR description, or spec document).
Identify:
1. The Core Decision
2. The Context/Problem
3. The Consequences (Positive and Negative)

## Phase 2 — Draft & Validate

Present a complete draft using the [`adr-template.md`](adr-template.md).
Explicitly list any assumptions you made about *why* the alternatives were rejected.

Dialogue:
- *"Does this accurately reflect the decision?"*
- *"Are there any negative consequences or rejected alternatives I missed?"*

## Phase 3 — Finalization

1. Refine based on user feedback.
2. Run the checklist ([`review-checklist.md`](review-checklist.md)).
3. Save to the filesystem (default: `docs/adr/`).
4. **Cross-skill integration:** Ask the user: *"Would you like me to update your C4 diagrams to reflect this? (Using the c4designer skill)"*

## Links

- ← Back: [`SKILL.md`](SKILL.md)
- Deliverable template: [`adr-template.md`](adr-template.md)
