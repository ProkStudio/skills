---
name: adr-scribe
version: 1.2.0
requires: ["c4-model >= 1.0.0"]
compatible_agents: ["copilot", "claude-code", "cursor", "devin", "windsurf"]
description: Interactively draft, retro-document, and review Architecture Decision Records (ADRs). The skill detects the usage mode (interview for a new decision, retro-documenting from a PR or code, or reviewing an existing ADR) and enforces the use of the Michael Nygard MADR template. Output format is Markdown. Destination is negotiated (default local filesystem in docs/adr/).
---

# ADR Scribe — documenting architectural decisions

While C4 diagrams document *what* the architecture is, an Architecture Decision Record (ADR) documents *why* it was built that way. This skill acts as a technical scribe to help you capture important architectural decisions consistently.

## Mode detection (router)

**Always start by identifying the mode.** 

### Signals to infer without asking

| User signal | Mode |
|---|---|
| *"We just decided to use X"*, *"Document this decision"*, *"I want to write an ADR"* | Interview |
| *"Here's a PR that changed our auth"*, *"Infer the decision from this code"* | Retro-Document |
| *"Is this ADR complete?"*, pastes an existing ADR | Review |

If the context is ambiguous, ask:
> "Do you want to: (a) **interview** me to draft a new ADR, (b) **retro-document** a decision from an existing PR/codebase, or (c) **review** an existing ADR?"

### File to load based on the mode

Once the mode is known, read the corresponding file to apply its detailed flow:

| Mode | File |
|---|---|
| Interview | [`mode-interview.md`](mode-interview.md) |
| Retro-Document | [`mode-retro-document.md`](mode-retro-document.md) |
| Review | [`mode-review.md`](mode-review.md) |

## The Template (Non-negotiable)

Every ADR must follow the structure defined in [`adr-template.md`](adr-template.md) (the Michael Nygard MADR format):
- Title
- Status (Proposed, Accepted, Deprecated, Superseded)
- Context
- Decision
- Consequences

## Common contract

### Output format
Default: **Markdown document**.

### Destination
Default: **local filesystem**, in `docs/adr/` (e.g., `docs/adr/0001-use-redis-for-caching.md`).
If an MCP is connected, you can propose saving it to Notion, Google Drive, etc. Confirm before writing.

### Dialogue rules
- **Max 3 questions per batch.** Never drown the user in a form.
- **Reformulate before assuming:** *"If I understand correctly, the main reason we chose X is Y. Is that right?"*
- **Offer options when the user hesitates:** *"Did you consider option Z? What were its drawbacks?"*
- **Incremental drafts:** Show a partial structure (e.g., just the Context) and validate as you go.
- **Explicit trade-offs.** Ensure the *Consequences* section includes both positive and negative impacts. If the user only provides positives, prompt them: *"What are the downsides or maintenance burdens of this choice?"*
- **Never deliver without validation.** Always present a draft and ask: *"Does this accurately reflect the decision?"* before writing the final file.

## Common pitfalls to avoid

- **Writing after the fact without context** — guessing why a decision was made instead of asking the stakeholders.
- **Listing only one option** — if there's no alternative, it's not a decision, it's a constraint.
- **Missing negative consequences** — every decision has trade-offs. An ADR without negative consequences is incomplete.
- **Leaving status as "Proposed" indefinitely** — remind the user to update statuses as the architecture evolves.

## Bundled references

Documentation for the selected mode (load with `Read` after detection):

- [`mode-interview.md`](mode-interview.md) — dialogued drafting
- [`mode-retro-document.md`](mode-retro-document.md) — inferring from code/PR
- [`mode-review.md`](mode-review.md) — critique of an existing ADR

Cross-cutting references:

- [`adr-template.md`](adr-template.md) — the MADR template to use
- [`review-checklist.md`](review-checklist.md) — checklist for completeness
- [`examples/0001-use-postgresql-over-mongodb.md`](examples/0001-use-postgresql-over-mongodb.md) — filled-out example
