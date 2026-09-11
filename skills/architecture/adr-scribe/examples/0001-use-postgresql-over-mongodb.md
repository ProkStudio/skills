# 0001. Use PostgreSQL over MongoDB for Core Banking API

* Status: Accepted
* Date: 2026-04-26

## Context and Problem Statement

Our new Internet Banking System needs a primary data store to handle user registration, hashed credentials, and account balances. We must choose a database technology that ensures high data integrity, supports complex transactional relationships, and scales adequately for expected initial load.

## Decision Drivers

* Strict ACID compliance required for financial transactions.
* Developer familiarity with SQL vs NoSQL paradigms.
* Need for structured relational queries for auditing.

## Considered Options

* Option 1: PostgreSQL
* Option 2: MongoDB

## Decision Outcome

Chosen option: "Option 1: PostgreSQL", because it provides robust, out-of-the-box ACID compliance which is non-negotiable for a banking system. While MongoDB offers faster initial prototyping for flexible schemas, our financial schemas are highly rigid and relational.

### Positive Consequences

* Guarantees data consistency across complex account transfers.
* Extensive ecosystem and tooling for backups and point-in-time recovery.
* High familiarity within the current engineering team.

### Negative Consequences

* Schema migrations will be more rigid and require careful coordination during CI/CD.
* Horizontal scaling for write-heavy workloads is more complex than a NoSQL counterpart, potentially requiring sharding in the future.
