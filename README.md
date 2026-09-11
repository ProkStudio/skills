# skills
A curated, vendored collection of **203** agent skills (`SKILL.md` format), covering everything from coding to video generation.
Every skill is copied verbatim from its upstream repository. Sources and licenses: see [ATTRIBUTION.md](ATTRIBUTION.md) and [licenses/](licenses).
## Install
```bash
# all skills for Claude Code / compatible agents
cp -r skills/*/*/ ~/.claude/skills/

# or for agents that read .agents/skills
cp -r skills/*/*/ ~/.agents/skills/

# or per project
mkdir -p .claude/skills && cp -r skills/*/*/ .claude/skills/
```
A skill is just a folder with a `SKILL.md` file, so you can also copy single folders. Remotion skills can alternatively be installed with `npx remotion skills add`.
## Catalog
| Category | Skills |
| --- | --- |
| [Architecture](#architecture) | 2 |
| [Collaboration & workflow](#collaboration) | 12 |
| [Data & databases](#data) | 13 |
| [Debugging](#debugging) | 4 |
| [DevOps, cloud & reliability](#devops) | 18 |
| [Documents & publishing](#docs) | 13 |
| [Software engineering](#engineering) | 27 |
| [App integrations](#integrations) | 18 |
| [Images, audio & design](#media-design) | 9 |
| [Agents, MCP & skill authoring](#meta) | 28 |
| [Problem solving](#problem-solving) | 6 |
| [Productivity](#productivity) | 6 |
| [Research](#research) | 7 |
| [Security](#security) | 11 |
| [Testing](#testing) | 5 |
| [Video generation & rendering](#video) | 16 |
| [Web, frontend & browser automation](#web) | 8 |

### architecture

Architecture

| Skill | What it does | Source |
| --- | --- | --- |
| `preserving-productive-tensions` | Recognize when disagreements reveal valuable context, preserve multiple valid approaches instead of forcing premature resolution | [superpowers-skills](https://github.com/obra/superpowers-skills) |
| `senior-architect` | This skill should be used when the user asks to "design system architecture", "evaluate microservices vs monolith", "create architecture diagrams", "analyze dependencies", "choose a database", "pla... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |

### collaboration

Collaboration & workflow

| Skill | What it does | Source |
| --- | --- | --- |
| `brainstorming` | Interactive idea refinement using Socratic method to develop fully-formed designs | [superpowers-skills](https://github.com/obra/superpowers-skills) |
| `dispatching-parallel-agents` | Use multiple Claude agents to investigate and fix independent problems concurrently | [superpowers-skills](https://github.com/obra/superpowers-skills) |
| `executing-plans` | Execute detailed plans in batches with review checkpoints | [superpowers-skills](https://github.com/obra/superpowers-skills) |
| `finishing-a-development-branch` | Complete feature development with structured options for merge, PR, or cleanup | [superpowers-skills](https://github.com/obra/superpowers-skills) |
| `handoff` | Compact the current conversation into a handoff document for another agent to pick up. References existing artifacts (PRDs, plans, ADRs, issues, commits, diffs) by path or URL instead of duplicatin... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `human-gate` | Runs the human-verification lane of an agent loop, and proves review happened before work is called done. Builds a single-file HTML review page, collects batched feedback as a structured artifact i... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `receiving-code-review` | Receive and act on code review feedback with technical rigor, not performative agreement or blind implementation | [superpowers-skills](https://github.com/obra/superpowers-skills) |
| `remembering-conversations` | Search previous Claude Code conversations for facts, patterns, decisions, and context using semantic or text search | [superpowers-skills](https://github.com/obra/superpowers-skills) |
| `requesting-code-review` | Dispatch code-reviewer subagent to review implementation against plan or requirements before proceeding | [superpowers-skills](https://github.com/obra/superpowers-skills) |
| `subagent-driven-development` | Execute implementation plan by dispatching fresh subagent for each task, with code review between tasks | [superpowers-skills](https://github.com/obra/superpowers-skills) |
| `using-git-worktrees` | Create isolated git worktrees with smart directory selection and safety verification | [superpowers-skills](https://github.com/obra/superpowers-skills) |
| `writing-plans` | Create detailed implementation plans with bite-sized tasks for engineers with zero codebase context | [superpowers-skills](https://github.com/obra/superpowers-skills) |

### data

Data & databases

| Skill | What it does | Source |
| --- | --- | --- |
| `data-quality-auditor` | Audit datasets for completeness, consistency, accuracy, and validity. Profile data distributions, detect anomalies and outliers, surface structural issues, and produce an actionable remediation pla... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `database-designer` | Use when the user asks to design database schemas, plan data migrations, optimize queries, choose between SQL and NoSQL, or model data relationships. | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `database-schema-designer` | Use when the user asks to create ERD diagrams, normalize database schemas, design table relationships, or plan schema migrations. | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `google-sheets` | \| Read and write Google Sheets spreadsheets - get content, update cells, append rows, fetch specific ranges, search for spreadsheets, and view metadata. Use when user asks to: read a spreadsheet,... | [sanjay-ai-skills](https://github.com/sanjay3290/ai-skills) |
| `llm-cost-optimizer` | Use proactively whenever LLM API costs come up -- or should. Triggers include: 'my AI costs are too high', 'optimize token usage', 'which model should I use', 'LLM spend is out of control', 'implem... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `migration-architect` | Zero-downtime migration planning, compatibility validation, and rollback strategy generation. Tools for system, database, and infrastructure migrations with minimal business impact. Use when planni... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `mssql` | Execute read-only SQL queries against multiple Microsoft SQL Server databases. Use when: (1) querying MSSQL/SQL Server databases, (2) exploring database schemas/tables, (3) running SELECT queries f... | [sanjay-ai-skills](https://github.com/sanjay3290/ai-skills) |
| `mysql` | Execute read-only SQL queries against multiple MySQL databases. Use when: (1) querying MySQL databases, (2) exploring database schemas/tables, (3) running SELECT queries for data analysis, (4) chec... | [sanjay-ai-skills](https://github.com/sanjay3290/ai-skills) |
| `postgres` | Execute read-only SQL queries against multiple PostgreSQL databases. Use when: (1) querying PostgreSQL databases, (2) exploring database schemas/tables, (3) running SELECT queries for data analysis... | [sanjay-ai-skills](https://github.com/sanjay3290/ai-skills) |
| `rag-architect` | Use when the user asks to design a RAG pipeline, choose a chunking strategy or embedding model, pick a vector database, or evaluate retrieval quality (precision@k, recall@k, NDCG). Examples: 'desig... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `snowflake-development` | Use when writing Snowflake SQL, building data pipelines with Dynamic Tables or Streams/Tasks, using Cortex AI functions, creating Cortex Agents, writing Snowpark Python, configuring dbt for Snowfla... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `sql-database-assistant` | Use when the user asks to write SQL queries, optimize database performance, generate migrations, explore database schemas, or work with ORMs like Prisma, Drizzle, TypeORM, or SQLAlchemy. | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `statistical-analyst` | Run hypothesis tests, analyze A/B experiment results, calculate sample sizes, and interpret statistical significance with effect sizes. Use when you need to validate whether observed differences ar... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |

### debugging

Debugging

| Skill | What it does | Source |
| --- | --- | --- |
| `defense-in-depth` | Validate at every layer data passes through to make bugs impossible | [superpowers-skills](https://github.com/obra/superpowers-skills) |
| `root-cause-tracing` | Systematically trace bugs backward through call stack to find original trigger | [superpowers-skills](https://github.com/obra/superpowers-skills) |
| `systematic-debugging` | Four-phase debugging framework that ensures root cause investigation before attempting fixes. Never jump to solutions. | [superpowers-skills](https://github.com/obra/superpowers-skills) |
| `verification-before-completion` | Run verification commands and confirm output before claiming success | [superpowers-skills](https://github.com/obra/superpowers-skills) |

### devops

DevOps, cloud & reliability

| Skill | What it does | Source |
| --- | --- | --- |
| `aws-solution-architect` | Design AWS architectures for startups using serverless patterns and IaC templates. Use when asked to design serverless architecture, create CloudFormation templates, optimize AWS costs, set up CI/C... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `azure-cloud-architect` | Design Azure architectures for startups and enterprises. Use when asked to design Azure infrastructure, create Bicep/ARM templates, optimize Azure costs, set up Azure DevOps pipelines, or migrate t... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `chaos-engineering` | Use when planning, running, or learning from chaos engineering experiments. Triggers on "chaos experiment", "fault injection", "gameday", "resilience test", "blast radius", "steady state", "abort c... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `ci-cd-pipeline-builder` | Generate pragmatic CI/CD pipelines from detected project stack signals — fast baseline generation, repeatable checks, environment-aware deployment stages. Use when setting up CI for a new project,... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `docker-development` | Docker and container development agent skill and plugin for Dockerfile optimization, docker-compose orchestration, multi-stage builds, and container security hardening. Use when: user wants to opti... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `env-secrets-manager` | Manage environment-variable hygiene and secrets safety across local development and production. Practical auditing, drift awareness, rotation readiness. Use when auditing .env files for committed s... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `feature-flags-architect` | Use when adding, retiring, or auditing feature flags. Triggers on "add a flag", "ship behind a flag", "rollout plan", "kill switch", "stale flags", "flag debt", "LaunchDarkly", "GrowthBook", "Stats... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `gcp-cloud-architect` | Design GCP architectures for startups and enterprises. Use when asked to design Google Cloud infrastructure, deploy to GKE or Cloud Run, configure BigQuery pipelines, optimize GCP costs, or migrate... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `git-worktree-manager` | Run parallel feature work safely with Git worktrees. Standardizes branch isolation, port allocation, environment sync, and cleanup so each worktree behaves like an independent local app. Optimized... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `helm-chart-builder` | Helm chart development agent skill and plugin for Claude Code, Codex, Gemini CLI, Cursor, OpenClaw — chart scaffolding, values design, template patterns, dependency management, security hardening,... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `incident-commander` | Comprehensive incident response framework from detection through resolution and post-incident review. Battle-tested SRE/DevOps practices: severity classification, timeline reconstruction, structure... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `incident-response` | Use when a security incident has been detected or declared and needs classification, triage, escalation path determination, and forensic evidence collection. Covers SEV1-SEV4 classification, false... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `kubernetes-operator` | Use when building a Kubernetes Operator — custom controllers that reconcile CRD state. Triggers on "build an operator", "CRD design", "reconcile loop", "controller-runtime", "kubebuilder", "operato... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `observability-designer` | Design production-ready observability strategies combining metrics, logs, and traces. Includes SLI/SLO design, golden-signals monitoring, alert optimization. Use when adding observability to a new... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `secrets-vault-manager` | Use when the user asks to set up secret management infrastructure, integrate HashiCorp Vault, configure cloud secret stores (AWS Secrets Manager, Azure Key Vault, GCP Secret Manager), implement sec... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `senior-devops` | Comprehensive DevOps skill for CI/CD, infrastructure automation, containerization, and cloud platforms (AWS, GCP, Azure). Includes pipeline setup, infrastructure as code, deployment automation, and... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `slo-architect` | Use when defining, reviewing, or operating SLOs/SLIs/error budgets. Triggers on "define an SLO", "what should our SLO be", "error budget", "burn rate", "SLI", "service level objective", "Google SRE... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `terraform-patterns` | Terraform infrastructure-as-code agent skill and plugin for Claude Code, Codex, Gemini CLI, Cursor, OpenClaw. Covers module design patterns, state management strategies, provider configuration, sec... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |

### docs

Documents & publishing

| Skill | What it does | Source |
| --- | --- | --- |
| `changelog-generator` | Automatically creates user-facing changelogs from git commits by analyzing commit history, categorizing changes, and transforming technical commits into clear, customer-friendly release notes. Turn... | [composio-awesome](https://github.com/ComposioHQ/awesome-claude-skills) |
| `content-research-writer` | Assists in writing high-quality content by conducting research, adding citations, improving hooks, iterating on outlines, and providing real-time feedback on each section. Transforms your writing p... | [composio-awesome](https://github.com/ComposioHQ/awesome-claude-skills) |
| `doc-coauthoring` | Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, decision docs, or similar structured content. This... | [anthropics-skills](https://github.com/anthropics/skills) |
| `docx` | Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files) or Word templates (.dotx files). Triggers include: any mention of 'Word doc', 'word document... | [anthropics-skills](https://github.com/anthropics/skills) |
| `internal-comms` | A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever asked to write some sort of internal... | [anthropics-skills](https://github.com/anthropics/skills) |
| `markdown-html-orchestrator` | Use when a user wants to convert any markdown file in their Claude project into a single-file, lightly-interactive HTML — long-form documents (specs, plans, RFCs, reports, explainers), code reviews... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `md-document` | Converts long-form markdown (specs, RFCs, reports, plans, explainers) into a single-file, lightly-interactive HTML document with sticky TOC, scrollspy, search filter, code-copy buttons, and design-... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `md-review` | Converts a markdown PR writeup or code review (one with ```diff fenced blocks and severity-tagged > [!BLOCKER]/[!MAJOR]/[!MINOR]/[!NIT] callouts) into a single-file 2-column HTML review — unified-d... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `md-slides` | Converts a markdown deck (slides separated by `---` HR boundaries or by `# ` H1 headings, with optional `<!-- notes: ... -->` presenter notes blocks) into a single-file HTML presentation with arrow... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `pdf` | Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, r... | [anthropics-skills](https://github.com/anthropics/skills) |
| `pptx` | Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting... | [anthropics-skills](https://github.com/anthropics/skills) |
| `runbook-generator` | Generate operational runbooks from a service name — deployment, incident response, maintenance, and rollback workflows. Templated structure customizable per environment. Use when documenting on-cal... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `xlsx` | Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .xltx, .csv, or .tsv file... | [anthropics-skills](https://github.com/anthropics/skills) |

### engineering

Software engineering

| Skill | What it does | Source |
| --- | --- | --- |
| `api-design-reviewer` | Comprehensive REST API design review with automated linting, breaking-change detection, and design scorecards. Catches inconsistent conventions, missing versioning, and design smells before APIs sh... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `api-test-suite-builder` | Use when the user asks to generate API tests, create integration test suites, test REST endpoints, or build contract tests. | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `code-reviewer` | Code review automation for TypeScript, JavaScript, Python, Go, Swift, Kotlin, C#, .NET, Java, C, C++, Rust, Ruby, PHP, and Dart/Flutter. Analyzes PRs for complexity and risk, checks code quality fo... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `code-tour` | Use when the user asks to create a CodeTour .tour file — persona-targeted, step-by-step walkthroughs that link to real files and line numbers. Trigger for: create a tour, onboarding tour, architect... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `codebase-onboarding` | Analyze a codebase and generate onboarding documentation for engineers, tech leads, and contractors. Fast fact-gathering and repeatable onboarding outputs. Use when onboarding a new engineer, writi... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `coverage` | >- Analyze test coverage gaps. Use when user says "test coverage", "what's not tested", "coverage gaps", "missing tests", "coverage report", or "what needs testing". | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `embedded-iot-mentor` | Mentor for embedded and IoT hardware projects. Helps select MCUs, dev boards, and toolchains, decides where sensor readings end up (phone, PC, dashboard, or alert), and gives time/cost estimates an... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `epic-design` | > Build immersive, cinematic 2.5D interactive websites using scroll storytelling, parallax depth, text animations, and premium scroll effects — no WebGL required. Use this skill for any web design... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `focused-fix` | Use when the user asks to fix, debug, or make a specific feature/module/area work end-to-end. Triggers: 'make X work', 'fix the Y feature', 'the Z module is broken', 'focus on [area]'. Not for quic... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `interview-system-designer` | This skill should be used when the user asks to "design interview processes", "create hiring pipelines", "calibrate interview loops", "generate interview questions", "design competency matrices", "... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `monorepo-navigator` | Navigate, manage, and optimize monorepos. Covers Turborepo, Nx, pnpm workspaces, and Lerna. Cross-package impact analysis, selective builds/tests on affected packages, remote caching, dependency gr... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `performance-profiler` | Systematic performance profiling for Node.js, Python, and Go applications. Identifies CPU, memory, and I/O bottlenecks, generates flamegraphs, analyzes bundle sizes, optimizes database queries, run... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `pr-review-expert` | Use when the user asks to review pull requests, analyze code changes, check for security issues in PRs, or assess code quality of diffs. | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `senior-backend` | Designs and implements backend systems including REST APIs, microservices, database architectures, authentication flows, and security hardening. Use when the user asks to "design REST APIs", "optim... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `senior-computer-vision` | Computer vision engineering skill for object detection, image segmentation, and visual AI systems. Covers CNN and Vision Transformer architectures, YOLO/Faster R-CNN/DETR detection, Mask R-CNN/SAM... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `senior-data-engineer` | Data engineering skill for building scalable data pipelines, ETL/ELT systems, and data infrastructure. Expertise in Python, SQL, Spark, Airflow, dbt, Kafka, and modern data stack. Includes data mod... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `senior-data-scientist` | World-class senior data scientist skill specialising in statistical modeling, experiment design, causal inference, and predictive analytics. Covers A/B testing (sample sizing, two-proportion z-test... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `senior-frontend` | Frontend development skill for React, Next.js, TypeScript, and Tailwind CSS applications. Use when building React components, optimizing Next.js performance, analyzing bundle sizes, scaffolding fro... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `senior-fullstack` | Fullstack development toolkit with project scaffolding for Next.js, FastAPI, MERN, and Django stacks, code quality analysis with security and complexity scoring, and stack selection guidance. Use w... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `senior-ml-engineer` | ML engineering skill for productionizing models, building MLOps pipelines, and integrating LLMs. Covers model deployment, feature stores, drift monitoring, RAG systems, and cost optimization. Use w... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `senior-qa` | Generates unit tests, integration tests, and E2E tests for React/Next.js applications. Scans components to create Jest + React Testing Library test stubs, analyzes Istanbul/LCOV coverage reports to... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `spec-driven-workflow` | Use when the user asks to write specs before code, define acceptance criteria, plan features before implementation, generate tests from specifications, or follow spec-first development practices. | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `strict-api` | Use when the user says 'no hallucinations', 'verify APIs', 'reality check', or 'don't invent functions'. Prevents the agent from calling methods, imports, or variables that do not provably exist in... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `tdd-guide` | Test-driven development skill for writing unit tests, generating test fixtures and mocks, analyzing coverage gaps, and guiding red-green-refactor workflows across Jest, Pytest, JUnit, Vitest, and M... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `tech-debt-tracker` | Scan codebases for technical debt, score severity, track trends, and generate prioritized remediation plans. Use when users mention tech debt, code quality, refactoring priority, debt scoring, clea... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `tech-stack-evaluator` | Technology stack evaluation and comparison with TCO analysis, security assessment, and ecosystem health scoring. Use when comparing frameworks, evaluating technology stacks, calculating total cost... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `zero-hallucination-coder` | Runs a disciplined Discuss -> Map -> Decompose -> Execute -> Verify loop that grounds code in verified structure — no invented APIs, no assumed imports, no placeholder code — with a lazy-senior-dev... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |

### integrations

App integrations

| Skill | What it does | Source |
| --- | --- | --- |
| `apple-container` | \| Apple's open-source `container` CLI to build, run, and manage OCI/Linux containers as lightweight per-container VMs on Apple-silicon macOS — no Docker daemon required. Use when the user mentions... | [sanjay-ai-skills](https://github.com/sanjay3290/ai-skills) |
| `atlassian` | \| Manage Jira issues and Confluence wiki pages in Atlassian Cloud. Use when: (1) searching/creating/updating Jira issues with JQL, (2) searching/reading/creating Confluence pages with CQL, (3) man... | [sanjay-ai-skills](https://github.com/sanjay3290/ai-skills) |
| `azure-devops` | \| Manage Azure DevOps projects, work items, repos, PRs, pipelines, wikis, test plans, security alerts, variable groups, environments/approvals, branch policies, and attachments. Use when user asks... | [sanjay-ai-skills](https://github.com/sanjay3290/ai-skills) |
| `file-organizer` | Intelligently organizes your files and folders across your computer by understanding context, finding duplicates, suggesting better structures, and automating cleanup tasks. Reduces cognitive load... | [composio-awesome](https://github.com/ComposioHQ/awesome-claude-skills) |
| `gmail` | \| Interact with Gmail - search emails, read messages, send emails, create drafts, and manage labels. Use when user asks to: search email, read email, send email, create email draft, mark as read,... | [sanjay-ai-skills](https://github.com/sanjay3290/ai-skills) |
| `google-calendar` | \| Interact with Google Calendar - list calendars, view events, create/update/delete events, and find free time. Use when user asks to: check calendar, schedule a meeting, create an event, find ava... | [sanjay-ai-skills](https://github.com/sanjay3290/ai-skills) |
| `google-chat` | \| Interact with Google Chat - send, read, edit, delete and react to messages, share images and files, reply in threads, and manage spaces and DMs. Use when user asks to: send a message on Google C... | [sanjay-ai-skills](https://github.com/sanjay3290/ai-skills) |
| `google-docs` | \| Interact with Google Docs - create documents, search by title, read content, and edit text. Use when user asks to: create a Google Doc, find a document, read doc content, add text to a doc, or r... | [sanjay-ai-skills](https://github.com/sanjay3290/ai-skills) |
| `google-drive` | \| Interact with Google Drive - search files, find folders, list contents, download files, upload files, create folders, move, copy, rename, and trash files. Use when user asks to: search Google Dr... | [sanjay-ai-skills](https://github.com/sanjay3290/ai-skills) |
| `google-slides` | \| Read and write Google Slides presentations - get text, find presentations, create presentations, add slides, replace text, and manage slide content. Use when user asks to: read a presentation, c... | [sanjay-ai-skills](https://github.com/sanjay3290/ai-skills) |
| `grok-build` | Orchestrate coding work by delegating well-specified implementation tasks to xAI's Grok Build CLI (grok) running headlessly, while the coding assistant plans, writes the task specs, reviews every d... | [sanjay-ai-skills](https://github.com/sanjay3290/ai-skills) |
| `jules` | Delegate coding tasks to Google Jules AI agent for asynchronous execution. Use when user says: 'have Jules fix', 'delegate to Jules', 'send to Jules', 'ask Jules to', 'check Jules sessions', 'pull... | [sanjay-ai-skills](https://github.com/sanjay3290/ai-skills) |
| `manus` | Delegate complex, long-running tasks to Manus AI agent for autonomous execution. Use when user says 'use manus', 'delegate to manus', 'send to manus', 'have manus do', 'ask manus', 'check manus ses... | [sanjay-ai-skills](https://github.com/sanjay3290/ai-skills) |
| `meeting-insights-analyzer` | Analyzes meeting transcripts and recordings to uncover behavioral patterns, communication insights, and actionable feedback. Identifies when you avoid conflict, use filler words, dominate conversat... | [composio-awesome](https://github.com/ComposioHQ/awesome-claude-skills) |
| `outline` | Search, read, and manage Outline wiki documents. Use when: (1) searching wiki for documentation, (2) reading wiki pages or articles, (3) listing wiki collections or documents, (4) creating or updat... | [sanjay-ai-skills](https://github.com/sanjay3290/ai-skills) |
| `stripe-integration-expert` | Production-grade Stripe integrations: subscriptions with trials and proration, one-time payments, usage-based billing, checkout sessions, idempotent webhook handlers, customer portal, and invoicing... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `telegram` | Send Telegram messages, files, and alerts via bot API; read replies; ask questions with inline buttons and wait for the answer (approve-from-phone). Supports multiple bots and named chat targets. U... | [sanjay-ai-skills](https://github.com/sanjay3290/ai-skills) |
| `whatsapp` | Send and receive WhatsApp messages via the unofficial linked-device client pywhats (pip install pywhats) — pair with QR, send text/images, group chat, read receipts, presence/typing, and a long-run... | [sanjay-ai-skills](https://github.com/sanjay3290/ai-skills) |

### media-design

Images, audio & design

| Skill | What it does | Source |
| --- | --- | --- |
| `algorithmic-art` | Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generative art, algorithmic art, flow fields,... | [anthropics-skills](https://github.com/anthropics/skills) |
| `brand-guidelines` | Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand colors or style guidelines, visual formatt... | [anthropics-skills](https://github.com/anthropics/skills) |
| `canvas-design` | Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other static piece. Create... | [anthropics-skills](https://github.com/anthropics/skills) |
| `design-system` | Captures the user's brand identity once via a 10-question onboarding wizard (primary/accent HEX + heading + body Google Fonts + design style editorial/technical/minimal/playful + default output dir... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `elevenlabs` | \| Convert documents and text to audio using ElevenLabs text-to-speech. Use this skill when the user wants to create a podcast, narrate a document, read aloud text, generate audio from a file, or c... | [sanjay-ai-skills](https://github.com/sanjay3290/ai-skills) |
| `google-tts` | \| Convert documents and text to audio using Google Cloud Text-to-Speech. Use this skill when the user wants to: narrate a document, read aloud text, generate audio from a file, convert text to spe... | [sanjay-ai-skills](https://github.com/sanjay3290/ai-skills) |
| `image-enhancer` | Improves the quality of images, especially screenshots, by enhancing resolution, sharpness, and clarity. Perfect for preparing images for presentations, documentation, or social media posts. | [composio-awesome](https://github.com/ComposioHQ/awesome-claude-skills) |
| `imagen` | \| Generate images using Google Gemini's image generation capabilities. Use this skill when the user needs to create, generate, or produce images for any purpose including UI mockups, icons, illust... | [sanjay-ai-skills](https://github.com/sanjay3290/ai-skills) |
| `theme-factory` | Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can apply to any artifac... | [anthropics-skills](https://github.com/anthropics/skills) |

### meta

Agents, MCP & skill authoring

| Skill | What it does | Source |
| --- | --- | --- |
| `academy-guide` | > Stop and check this skill before finishing any reply to a question about how to use Claude or a Claude product — it recommends matching courses, tutorials, and use cases from Claude Academy (acad... | [anthropics-skills](https://github.com/anthropics/skills) |
| `agent-designer` | Use when the user asks to design a multi-agent system, pick an orchestration pattern (supervisor/swarm/pipeline), generate tool schemas for agents, or evaluate agent execution logs for cost, latenc... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `agent-harness` | Turn any domain folder of skills into a bounded agentic loop: compile a goal into a verifiable task plan, execute tasks with the domain's own tools, verify every task with machine-run checks, retry... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `agent-memory` | Use when a project's CLAUDE.md has grown past what anyone reads and you want the agent to learn durable facts from its own sessions instead — or when asking why the agent keeps re-learning the same... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `agent-workflow-designer` | Design production-grade multi-agent workflows with clear pattern choice (sequential, parallel, hierarchical), handoff contracts, failure handling, and cost/context controls. Use when architecting a... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `board` | Read, write, and browse the AgentHub message board for agent coordination. Use when the user runs /hub:board or asks to post, read, or inspect coordination messages between competing AgentHub agents. | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `book-to-skill` | Converts books, documentation folders, and source collections (PDF, EPUB, DOCX, HTML, Markdown, RST, AsciiDoc, RTF, MOBI/AZW) into structured agent skills — extracting named frameworks, principles,... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `claude-api` | \|- Reference for the Claude API / Anthropic SDK — model ids, pricing, params, streaming, tool use, MCP, agents, caching, token counting, model migration. TRIGGER — read BEFORE opening the target f... | [anthropics-skills](https://github.com/anthropics/skills) |
| `claude-coach` | Personal coach that teaches users to become Claude power users. Use this skill the FIRST time a user asks to "learn Claude", "be a power user", "coach me", "teach me Claude tricks", "what can Claud... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `discernment-nudge` | > After you give a substantive answer or draft that the user may act on — advice or recommendations, drafted artifacts such as goals, plans, pitches, proposals, or emails, estimates or projections,... | [anthropics-skills](https://github.com/anthropics/skills) |
| `eval` | Evaluate and rank agent results by metric or LLM judge for an AgentHub session. Use when the user runs /hub:eval or asks to score, compare, or pick a winner among completed AgentHub agents. | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `gardening-skills-wiki` | Maintain skills wiki health - check links, naming, cross-references, and coverage | [superpowers-skills](https://github.com/obra/superpowers-skills) |
| `mcp-builder` | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate exte... | [anthropics-skills](https://github.com/anthropics/skills) |
| `mcp-server-builder` | Design and ship production-ready MCP (Model Context Protocol) servers from OpenAPI contracts instead of hand-written tool wrappers. Python and TypeScript support, schema validation, safe evolution.... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `memory-engineering` | Use when designing, reviewing, or paying for an agent memory system — adding memory to an agent, choosing between long-context / RAG / graph / agentic memory, auditing what a CLAUDE.md or memory di... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `prompt-governance` | Use when managing prompts in production at scale: versioning prompts, running A/B tests on prompts, building prompt registries, preventing prompt regressions, or creating eval pipelines for product... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `pulling-updates-from-skills-repository` | Sync local skills repository with upstream changes from obra/superpowers-skills | [superpowers-skills](https://github.com/obra/superpowers-skills) |
| `self-eval` | Honestly evaluate AI work quality using a two-axis scoring system. Use after completing a task, code review, or work session to get an unbiased assessment. Detects score inflation, forces devil's a... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `self-improving-agent` | Curate Claude Code's auto-memory into durable project knowledge. Analyze MEMORY.md for patterns, promote proven learnings to CLAUDE.md and .claude/rules/, extract recurring solutions into reusable... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `senior-prompt-engineer` | Use when the user asks to optimize prompts, design prompt templates, evaluate LLM outputs with an eval set, measure RAG retrieval quality, validate agent/tool configurations, analyze token usage, o... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `sharing-skills` | Contribute skills back to upstream via branch and PR | [superpowers-skills](https://github.com/obra/superpowers-skills) |
| `skill-creator` | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a sk... | [anthropics-skills](https://github.com/anthropics/skills) |
| `skill-doctor` | Use when the user wants their agent setup graded from real conversation history, asks which installed skills are actually working, or wants evidence-backed skill edits — scores recent local Claude... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `testing-skills-with-subagents` | RED-GREEN-REFACTOR for process documentation - baseline without skill, write addressing failures, iterate closing loopholes | [superpowers-skills](https://github.com/obra/superpowers-skills) |
| `using-skills` | Skills wiki intro - mandatory workflows, search tool, brainstorming triggers | [superpowers-skills](https://github.com/obra/superpowers-skills) |
| `workflow-builder` | Design and write deterministic multi-agent workflow scripts (.js files in .claude/workflows/) for Claude Code's Workflow tool. Use when a user wants to build, create, author, scaffold, or run a cus... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `write-a-skill` | Create new agent skills with proper structure, progressive disclosure, and bundled resources. Use when user wants to create, write, build, or author a new skill. | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `writing-skills` | TDD for process documentation - test with subagents before writing, iterate until bulletproof | [superpowers-skills](https://github.com/obra/superpowers-skills) |

### problem-solving

Problem solving

| Skill | What it does | Source |
| --- | --- | --- |
| `collision-zone-thinking` | Force unrelated concepts together to discover emergent properties - "What if we treated X like Y? | [superpowers-skills](https://github.com/obra/superpowers-skills) |
| `inversion-exercise` | Flip core assumptions to reveal hidden constraints and alternative approaches - "what if the opposite were true? | [superpowers-skills](https://github.com/obra/superpowers-skills) |
| `meta-pattern-recognition` | Spot patterns appearing in 3+ domains to find universal principles | [superpowers-skills](https://github.com/obra/superpowers-skills) |
| `scale-game` | Test at extremes (1000x bigger/smaller, instant/year-long) to expose fundamental truths hidden at normal scales | [superpowers-skills](https://github.com/obra/superpowers-skills) |
| `simplification-cascades` | Find one insight that eliminates multiple components - "if this is true, we don't need X, Y, or Z | [superpowers-skills](https://github.com/obra/superpowers-skills) |
| `when-stuck` | Dispatch to the right problem-solving technique based on how you're stuck | [superpowers-skills](https://github.com/obra/superpowers-skills) |

### productivity

Productivity

| Skill | What it does | Source |
| --- | --- | --- |
| `capture` | Captures and organizes chaotic brain dumps into a structured, actionable system with zero information loss. Use this skill whenever the user says 'capture this', 'brain dump', 'let me dump some ide... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `deep-work` | Use when someone wants to plan a deep work day, time-block their calendar or task list, budget or cut shallow work, protect focus hours, track deep-work sessions and streaks, run an end-of-day shut... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `inbox-triage` | Runs a full inbox triage using the knowledge base created by the 'inbox-setup' skill. Light-intake by design (most invocations skip questions and run with KB-default preferences); asks at most 2 gr... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `meetings` | Use when someone wants to decide whether a meeting is worth calling, price a meeting in dollars, build a timeboxed agenda with desired outcomes, or turn messy meeting notes into owned action items... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `reflect` | Mid-conversation reflection skill that pauses execution and zooms out from detail-mode to honestly reassess direction, assumptions, and bias. Use when the user says 'reflect', 'take a step back', '... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `weekly-review` | Use when someone wants to run a weekly review, close open loops, audit stalled projects and commitments, get their system back to trusted, restart a lapsed review habit, or says "/cs:weekly-review"... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |

### research

Research

| Skill | What it does | Source |
| --- | --- | --- |
| `autoresearch-agent` | Autonomous experiment loop that optimizes any file by a measurable metric. Inspired by Karpathy's autoresearch. The agent edits a target file, runs a fixed evaluation, keeps improvements (git commi... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `deep-research` | Execute autonomous multi-step research using Google Gemini Deep Research Agent. Use for: market analysis, competitive landscaping, literature reviews, technical research, due diligence. Takes 2-10... | [sanjay-ai-skills](https://github.com/sanjay3290/ai-skills) |
| `deepread` | Use when the user asks to deeply read a book, article, PDF, or document set; extract claims and evidence; build a knowledge map; or learn through Feynman explanation and recall. Covers quick, deep,... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `dossier` | Decision-grade entity research skill — produces a hypothesis-tested dossier on a specific company, person, nonprofit, or government org, not a generic profile. Forcing intake makes the user state t... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `litreview` | Academic literature orientation skill that searches papers via free keyless APIs (PubMed E-utilities + OpenAlex) by default — with the Consensus MCP as an optional enhancement lane when connected —... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `notebooklm` | Query and manage Google NotebookLM notebooks with persistent profile auth, source sync, batch/multi queries, and structured exports. Use when user asks to query NotebookLM, 'ask my notebook', share... | [sanjay-ai-skills](https://github.com/sanjay3290/ai-skills) |
| `tracing-knowledge-lineages` | Understand how ideas evolved over time to find old solutions for new problems and avoid repeating past failures | [superpowers-skills](https://github.com/obra/superpowers-skills) |

### security

Security

| Skill | What it does | Source |
| --- | --- | --- |
| `adversarial-reviewer` | Adversarial code review that breaks the self-review monoculture. Use when you want a genuinely critical review of recent changes, before merging a PR, or when you suspect Claude is being too agreea... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `ai-security` | Use when assessing AI/ML systems for prompt injection, jailbreak vulnerabilities, model inversion risk, data poisoning exposure, or agent tool abuse. Covers MITRE ATLAS technique mapping, injection... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `cloud-security` | Use when assessing cloud infrastructure for security misconfigurations, IAM privilege escalation paths, S3 public exposure, open security group rules, or IaC security gaps. Covers AWS, Azure, and G... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `dependency-auditor` | Audit and manage dependencies across multi-language projects. Identifies vulnerabilities, license conflicts, transitive dependency risks, and safe-upgrade paths. Use when auditing third-party packa... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `red-team` | Use when planning or executing authorized red team engagements, attack path analysis, or offensive security simulations. Covers MITRE ATT&CK kill-chain planning, technique scoring, choke point iden... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `security-guidance` | PreToolUse security-anti-pattern hook for Claude Code. Catches 12 common security risks (command injection, XSS, SQL injection, unsafe deserialization, GitHub Actions workflow injection, eval/new F... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `security-pen-testing` | Use when the user asks to perform security audits, penetration testing, vulnerability scanning, OWASP Top 10 checks, or offensive security assessments. Covers static analysis, dependency scanning,... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `senior-secops` | Senior SecOps engineer skill for application security, vulnerability management, compliance verification, and secure development practices. Runs SAST/DAST scans, generates CVE remediation plans, ch... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `senior-security` | Use when the user asks for STRIDE threat modeling, DREAD risk scoring, data-flow-diagram threat analysis, or a quick secret scan — or when a security request needs routing to the right specialist s... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `skill-security-auditor` | > Security audit and vulnerability scanner for AI agent skills before installation. Use when: (1) evaluating a skill from an untrusted source, (2) auditing a skill directory or git repo URL for mal... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `threat-detection` | Use when hunting for threats in an environment, analyzing IOCs, or detecting behavioral anomalies in telemetry. Covers hypothesis-driven threat hunting, IOC sweep generation, z-score anomaly detect... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |

### testing

Testing

| Skill | What it does | Source |
| --- | --- | --- |
| `condition-based-waiting` | Replace arbitrary timeouts with condition polling for reliable async tests | [superpowers-skills](https://github.com/obra/superpowers-skills) |
| `ship-gate` | > Pre-production audit that scans a codebase for security, database, deployment, code quality, AI/LLM, dependency, frontend, and observability issues. Intercepts deploy commands and blocks until cr... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `skill-tester` | Validate, test, and score the quality of skills within the claude-skills ecosystem. Comprehensive meta-skill: structure validation, Python script testing (syntax + imports + runtime + output format... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `test-driven-development` | Write the test first, watch it fail, write minimal code to pass | [superpowers-skills](https://github.com/obra/superpowers-skills) |
| `testing-anti-patterns` | Never test mock behavior. Never add test-only methods to production classes. Understand dependencies before mocking. | [superpowers-skills](https://github.com/obra/superpowers-skills) |

### video

Video generation & rendering

| Skill | What it does | Source |
| --- | --- | --- |
| `demo-video` | Use when the user asks to create a demo video, product walkthrough, feature showcase, animated presentation, marketing video, or GIF from screenshots or scene descriptions. Orchestrates playwright,... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `remotion-best-practices` | Router for all Remotion skills | [remotion-skills](https://github.com/remotion-dev/skills) |
| `remotion-captions` | Transcribing, displaying and animating captions | [remotion-skills](https://github.com/remotion-dev/skills) |
| `remotion-create` | Create a new Remotion video | [remotion-skills](https://github.com/remotion-dev/skills) |
| `remotion-docs` | Search Remotion documentation | [remotion-skills](https://github.com/remotion-dev/skills) |
| `remotion-interactivity` | Structure Remotion markup for interactivity | [remotion-skills](https://github.com/remotion-dev/skills) |
| `remotion-maps` | Remotion Map animation knowledge | [remotion-skills](https://github.com/remotion-dev/skills) |
| `remotion-markup` | Content, animation and effects best practices | [remotion-skills](https://github.com/remotion-dev/skills) |
| `remotion-motion-graphics` | Create and edit professional motion graphics videos with Remotion (React-based video). Use this skill EVERY time the user wants to create a video, edit a video, animate something, build an intro/ou... | [remotion-claude-skill](https://github.com/haidrrrry/claude-remotion-skill) |
| `remotion-multimedia` | Interacting with Mediabunny | [remotion-skills](https://github.com/remotion-dev/skills) |
| `remotion-render` | Export a Remotion video | [remotion-skills](https://github.com/remotion-dev/skills) |
| `remotion-saas` | Build an app with Remotion | [remotion-skills](https://github.com/remotion-dev/skills) |
| `remotion-studio` | Preview a Remotion video | [remotion-skills](https://github.com/remotion-dev/skills) |
| `remotion-upgrade` | Upgrade Remotion, and related packages | [remotion-skills](https://github.com/remotion-dev/skills) |
| `slack-gif-creator` | Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for Slack like "make me... | [anthropics-skills](https://github.com/anthropics/skills) |
| `video-downloader` | Download YouTube videos with customizable quality and format options. Use this skill when the user asks to download, save, or grab YouTube videos. Supports various quality settings (best, 1080p, 72... | [composio-awesome](https://github.com/ComposioHQ/awesome-claude-skills) |

### web

Web, frontend & browser automation

| Skill | What it does | Source |
| --- | --- | --- |
| `a11y-audit` | Accessibility audit skill for scanning, fixing, and verifying WCAG 2.2 Level A and AA compliance across React, Next.js, Vue, Angular, Svelte, and plain HTML codebases. Use when auditing accessibili... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `artifacts-builder` | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state ma... | [composio-awesome](https://github.com/ComposioHQ/awesome-claude-skills) |
| `browser-automation` | Use when the user asks to automate browser tasks, scrape websites, fill forms, capture screenshots, extract structured data from web pages, or build web automation workflows. NOT for testing — use... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `frontend-design` | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typography, and making choices that don't read as templated de... | [anthropics-skills](https://github.com/anthropics/skills) |
| `full-page-screenshot` | Use when the user asks to capture a full-page screenshot, long screenshot, or complete page capture of a web page. Handles SPA scroll containers, lazy-loaded images, and very tall pages via Chrome... | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `universal-scraping-architect` | Use for web scraping, crawling, document extraction, API parsing, or building validation-heavy data pipelines using Firecrawl or local Python scripts. | [alirezarezvani-skills](https://github.com/alirezarezvani/claude-skills) |
| `web-artifacts-builder` | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state ma... | [anthropics-skills](https://github.com/anthropics/skills) |
| `webapp-testing` | Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browse... | [anthropics-skills](https://github.com/anthropics/skills) |

## Validate

```bash
python scripts/validate_skills.py
```
