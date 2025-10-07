# Company Overview

- **Recruiter:** Doghouse Recruitment (Amsterdam-based tech recruitment agency).  
  - Public profile: LinkedIn lists Doghouse as a specialised tech recruitment firm (approx. 51–200 employees). Their website emphasizes senior recruiters, a sprint-based delivery model, and focused technical hiring for product and platform teams.
  - Website: https://www.doghouse.nl/
  - Role of Doghouse here: agency/advertiser for an unnamed client — they are not the hiring product company.

- **Hiring company (client):** unnamed in the public job posting (listed as "my client" or "client (Cloud Infrastructure company)").
  - What we can say from the job ad: this is a cloud infrastructure / data‑center / platform provider operating across Europe and North America, offering scalable compute for high‑compute applications. They run data centers and provide managed infrastructure (Kubernetes, managed DBs, compute).
  - Likely company profile: mid‑sized platform or scale‑up / established infrastructure provider. They’re large enough to operate multiple data centers and staff engineering teams in multiple regions, and they have dedicated teams for billing, monitoring, and security platform services.

# Mission and Values

- **Doghouse Recruitment (recruiter values)**:
  - Emphasizes honesty, technical understanding, senior recruiters only, fast and clear delivery sprints, and matching candidates to teams precisely.
- **Inferred values for the hiring client** (from job description & role focus):
  - *Reliability and uptime* — operates data centers and provides compute to demanding workloads.
  - *Scalability & performance* — targets high‑compute customers and high‑load services.
  - *Security & correctness* — hiring an engineer focused on security, billing and monitoring (areas that require correctness and strong operational practices).
  - *Operational excellence & automation* — heavy use of Kubernetes, managed DBs, and distributed systems implies a focus on automation, observability and DevOps culture.
  - Note: because the client is unnamed, confirm cultural and mission specifics during interviews.

# Recent News or Changes

- Public job posting channels (HubMub and other job boards) show active hiring in Amsterdam for senior backend Golang roles — signals growth or scaling of platform teams.
- Doghouse Recruitment has recent public posts about hiring sprints and placements on their LinkedIn and site — indicates the agency is actively recruiting for multiple technical roles.
- No public press release or named company announcement is available in the job posting to identify the client. That means:
  - The client prefers confidentiality in public adverts (common for strategic hires).
  - Ask during interviews for recent product milestones (new data center launches, major customer wins, funding or M&A), engineering roadmap, or operational changes (cloud migration, multi‑region rollout).

# Role Context and Product Involvement

- **Title:** Senior Backend Engineer – Golang (backend team in Amsterdam; hybrid).
- **Primary product context (from the ad):**
  - You will build backend services for *billing*, *monitoring*, and *security* — these are platform services which:
    - Support business-critical functions (billing accuracy, SLO/SLI detection, incident response).
    - Interact with other platform layers (compute orchestration, user accounts, metering, storage).
  - Tech environment: `Golang`, `Kubernetes`, *managed databases* (e.g., cloud RDBMS or distributed DBs), and distributed systems for high‑load workloads.
- **Likely team structure (inferred):**
  - Part of a backend/platform engineering chapter or team focused on platform services (billing/observability/security).
  - Cross-functional interaction with: SRE/ops, platform engineers, product managers, security engineers, and possibly customer support/finance for billing.
  - Reporting to an engineering manager or technical lead; hiring process includes team‑lead technical deep dives — expect interviews with peers and managers.
- **Typical responsibilities (expanded from ad):**
  - Designing, implementing, and owning services in Go that operate at scale.
  - Integrating with Kubernetes for deployment and scaling.
  - Working with managed DBs including schema design, scaling, and transactional correctness.
  - Building reliable monitoring and alerting; ensuring billing correctness (idempotency, audit trails).
  - Participating in on‑call rotations, system design and architectural decisions, and code reviews.

# Likely Interview Topics

Prepare for a mix of coding, system design, and platform / operations questions. Based on the posting, expect:

1. Coding & language fundamentals
   - Basic algorithms, problem solving, and coding tests (the ad explicitly mentions basic algorithms).
   - If you’re switching to Go: show core knowledge (types, slices, maps, interfaces) and idiomatic patterns.

2. Golang-specific topics
   - Concurrency model: goroutines, channels, sync primitives, context, race conditions.
   - Error handling patterns, packages, testing (`testing` package), benchmarking.
   - Memory model, pointers, zero values, and performance profiling (`pprof`).

3. System design (service & distributed design)
   - Design a billing service that aggregates usage and produces invoices (accuracy, idempotency, reconciliation).
   - Design metrics & monitoring pipelines for a distributed fleet (collectors, aggregation, retention, cardinality).
   - Architect for scale: partitioning/sharding, event-driven designs, eventual consistency tradeoffs.

4. Distributed systems and data consistency
   - Design choices for consistency vs availability for billing/monitoring.
   - Idempotency, retries, deduplication, and exactly-once vs at-least-once semantics.
   - Database patterns (transactions, leader election, distributed locks, CDC).

5. Kubernetes & platform operations
   - Deployments, rolling updates, health checks, probes, resource limits/requests, autoscaling.
   - Service meshes, ingress, network policies, secrets management.
   - Observability in K8s: Prometheus, OpenTelemetry, logging (ELK/EFK), tracing.

6. Databases & storage
   - Managed DBs: pros/cons of RDS/Cloud SQL vs self‑managed DBs; read replicas, backups, failover.
   - Data modeling for billing (time-series aggregation vs event store), data retention policies.
   - Scalability (partitioning, indexing, retention, cost considerations).

7. Security & compliance (given role touches security services)
   - Authz/authn patterns (JWT, OAuth), encryption at rest/in transit, audit logs.
   - PCI or regulatory concerns if billing for customers (ask if relevant).

8. Reliability, SRE & operational questions
   - Incident handling, on-call expectations, SLIs/SLOs, postmortems, runbooks.
   - CI/CD pipeline, testing strategy (unit, integration, contract tests), deployment frequency.

9. Behavioral & culture-fit
   - Examples of ownership, collaboration with cross-functional teams, mentoring, and how you handle ambiguity in scaling systems.

# Suggested Questions to Ask (to interviewers)

Use these to show product interest, technical maturity, and fit:

About the team & role
- How is the backend/platform org structured? Will I be embedded in a product team, platform team, or a cross‑functional chapter?
- How big is the team I’ll join (engineers, SREs, product/PMs) and what are their primary responsibilities?
- Who will I report to and what are the expectations for the first 3 / 6 / 12 months?

Technical scope & stack
- What parts of the stack are primarily written in Go today? Is the codebase mostly microservices or a mix with monoliths?
- Which managed databases are you running in production? (e.g., RDS, Cloud Spanner, CockroachDB, etc.)
- Which observability tools are used for metrics, logging, and tracing?

Product & impact
- What are the top business problems this team is solving right now? How does billing / monitoring impact revenue or customer SLAs?
- Can you share a recent example of a high‑impact project (e.g., a scale event, DC launch, or a billing migration)?

Reliability & operations
- What are your SLIs/SLOs for billing accuracy and monitoring latency? How do you measure and enforce them?
- What is the on‑call setup and how does the team handle incident response and postmortems?

Architecture & design
- Are there any planned migrations or architectural changes (e.g., moving to a new DB, event streaming platform, or multiregion setup)?
- How do you manage data consistency for billing events (reconciliation systems, delayed billing, or compensation logic)?

Delivery & culture
- How do teams handle technical debt vs feature work? What’s your roadmap cadence (e.g., quarterly objectives)?
- What growth/mentorship paths exist for senior engineers? How do you measure success in this role?

Logistics & compensation
- Can you clarify the total compensation mix (base / bonus / benefits) and whether equity is offered?
- Are visa sponsorship or relocation packages available (if applicable)?
- What is the hybrid working policy (expected in-office days)?

# Tailored preparation advice for Juan Srisaiwong (3 years experience, ready to switch to Go)

You have strengths (cloud, Node/Python, Docker, CI/CD, databases). The posting asks for 10+ years (senior) but also allows candidates ready to switch to Go — use that to position yourself.

Practical prep steps (30–60 day plan)
- Learn idiomatic Go (2–3 weeks):
  - Work through Go tour and key docs: goroutines/channels, interfaces, error handling.
  - Build a small service (metering endpoint → store events → aggregate) using Go and a managed DB (e.g., Postgres).
  - Add unit tests and a simple integration test; show a GitHub repo as a code sample.

- Demonstrate cloud & infra skills (1–2 weeks):
  - Create a Kubernetes manifest and Helm chart for your sample service; deploy to a free k8s cluster (e.g., k3s/minikube or a managed sandbox).
  - Add CI/CD with GitHub Actions to run tests and build Docker images.

- Study system design & domain specifics (2–3 weeks):
  - Prepare a design for a billing pipeline (event ingestion, aggregation, invoicing), focusing on idempotency and reconciliation.
  - Prepare a monitoring system design: metrics collection, cardinality concerns, retention, alerting strategy.

- Interview practice:
  - Brush up on algorithm basics (arrays, hash maps, sorting) — short coding questions are expected.
  - Prepare 2–3 STAR stories highlighting ownership, incident handling, and cross-team collaboration.

How to present your experience
- Lead with your cloud & devops experience: Kubernetes, Docker, AWS, CI/CD — these map well to their infra needs.
- Show quick learning ability: a public Go project or small service demonstrates commitment to switching languages.
- Emphasize any high‑load, scaling or reliability work (even in Node/Python) — explain patterns you used that apply to Go systems (caching, batching, retries, idempotency).

# Sample interview prompts you should practice (and short hints)

- Design a billing system for a cloud provider that bills by CPU hours and bandwidth. What API endpoints, data model, and reconciliation processes would you implement?  
  - Hint: cover event ingestion, aggregation windows, idempotency keys, storage schema vs cost, reconciliation & dispute resolution.

- How would you design a monitoring pipeline to collect, process and query high‑cardinality metrics across multi‑region clusters?  
  - Hint: consider ingestion rate limits, metric cardinality control, downsampling, retention, use of TSDBs (Prometheus long-term options), and alerting thresholds.

- (Golang) Explain goroutines and channels. When would you use buffered vs unbuffered channels? How do you avoid race conditions?  
  - Hint: show code examples for worker pools and `sync` primitives; mention `go vet`, `-race`, and profiling.

# Final recommendations and next steps

- During early screenings, ask directly for the client name (if they don’t disclose it up-front) — you need product context to tailor answers and negotiate.
- If the client remains confidential, request a pre-interview call to learn architecture, tech stack details (which DBs, which monitoring stack), team size and on-call expectations.
- Build a focused Go sample service (public repo + README) that solves a small billing/monitoring problem — this will strongly offset fewer years of experience.
- Prepare 3–4 concrete examples (ownership, production incident, cross-team collaboration) and a short technical walkthrough of a system you contributed to (architecture, decisions, trade-offs).

Good luck — if you want, I can:
- Draft 2–3 concise STAR stories from your resume to match billing/ops responsibilities.
- Create a 1–page Go microservice template you can use as a code sample (includes Dockerfile, basic tests, and Kubernetes manifest).
- Mock 3 interview questions (one coding, one system design, one Go concurrency) and walk through ideal answers. Which would you like next?