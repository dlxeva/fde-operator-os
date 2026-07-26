# FDE Practice System

## Purpose

This reference extends the seven-stage delivery chain into a production operating system. It synthesizes recurring practices from forward-deployed engineering, applied AI delivery, operational software, agent evaluation, and site reliability work.

The central standard is simple:

> A loop is credible when operators adopt it, workflow impact is measurable, production behavior is observable, failure is containable, and field learning changes future delivery or product capability.

## The FDE Operating Role

The FDE operating role owns the translation between four worlds:

1. customer mission and workflow reality
2. system design and implementation constraints
3. production operation and reliability
4. reusable product, platform, eval, and delivery assets

The role may be held by one person in an early team or distributed across delivery, engineering, product, operations, and domain owners. Decision rights still need to be explicit.

## Four Concurrent Control Loops

The seven delivery stages remain the sequencing backbone. Four control loops run across every stage.

### 1. Customer Value Loop

Sequence:

`mission fit -> bounded operator loop -> adoption -> workflow impact -> expansion decision`

Required evidence:

- a named operator and accountable owner
- a measurable baseline
- an adoption signal tied to real workflow use
- outcome evidence from the operating loop
- a stop, continue, or expand decision

### 2. System Quality Loop

Sequence:

`real cases -> error taxonomy -> eval cases -> regression gate -> production traces -> new eval cases`

Required evidence:

- clean, ugly, disputed, handoff-failure, and demo-killing cases
- task-level expected outcomes
- explicit graders and reviewer rubric
- versioned run results and traces
- a rule for promoting production failures into the regression set

### 3. Production Reliability Loop

Sequence:

`readiness review -> observable launch -> incident response -> rollback or recovery -> postmortem -> hardening`

Required evidence:

- production owner and exception owner
- service and workflow objectives
- telemetry, audit, and incident thresholds
- containment, fallback, and rollback paths
- post-incident actions with owners and verification

### 4. Product Learning Loop

Sequence:

`field observation -> evidence -> constraint classification -> recurrence test -> destination -> promoted asset or roadmap item`

Required evidence:

- field signal with source context
- impact, severity, and frequency
- constraint class
- reusable pattern hypothesis
- destination, owner, and next proof

## Five Decision Gates

| Gate | Decision | Minimum proof | Typical output |
|---|---|---|---|
| G0 — Mission Fit | Is this worth committing to? | named operator, consequence, observable success path, blocking constraints | Mission Brief |
| G1 — Evidence Sufficiency | Do we understand the real loop well enough to design? | real case replays, measured baseline, owners, source artifacts, explicit gaps | Operational Reality Map, Case Replay Pack, Reality Capture Gate |
| G2 — Pilot Contract | Can a bounded pilot prove or disprove value? | minimum loop, baseline, representative evals, acceptance and rollback criteria | Minimum Viable Loop, POC Acceptance Contract, Eval Pack, Governance Overlay |
| G3 — Production Readiness | Can the loop enter live work with controlled risk? | owner, adoption plan, regression gate, observability, incident response, containment, rollback | Day-2 Operations Plan, Production Readiness Review, Field Signal Log |
| G4 — Replication And Promotion | Should this expand, repeat, or become an asset? | repeatable impact, stable operating burden, known risks, reusable pattern evidence | Expansion Roadmap, Asset Distillation Log, promoted Field Signals |

A gate records one of three postures:

- `go`
- `conditional-go` with named blockers and proof dates
- `no-go` with the reason and re-entry condition

## Evidence Hierarchy

Use the strongest available evidence and label weaker evidence explicitly.

1. production trace, audit record, or measured operational event
2. real historical case with source artifacts
3. observed live workflow or shadow workflow
4. operator replay corroborated by multiple roles
5. single-stakeholder narrative
6. inferred workflow or synthetic assumption

Stages 6 and 7 should rely primarily on levels 1-3. Levels 4-6 can remain as named assumptions or gating items.

## Constraint Classification

Field teams often misroute every problem into the product backlog. Classify the binding constraint first.

- `product-capability` — shared capability is absent or structurally weak
- `model-or-eval` — behavior, quality, calibration, or test coverage is insufficient
- `data-readiness` — source, structure, quality, access, or lineage is missing
- `integration` — system boundary, interface, latency, or write-back blocks the loop
- `policy-or-compliance` — authority, legal, privacy, retention, or audit constraints bind
- `change-management` — incentives, training, role change, or adoption blocks use
- `delivery-execution` — local sequencing, ownership, staffing, or project control fails
- `operating-model` — day-2 ownership, support, funding, or maintenance is unresolved

Constraint classification determines destination. It also prevents local implementation work from being presented as a universal product gap.

## Decision Rights

| Decision | Accountable role | Required contributors | Evidence source |
|---|---|---|---|
| mission go / no-go | engagement owner | operator owner, domain lead, technical lead | Mission Brief |
| reality sufficient | FDE / delivery lead | frontline operators, exception owner | Reality Capture Gate |
| pilot acceptance | business reviewer | eval owner, technical lead, operator owner | POC Acceptance Contract and Eval Pack |
| AI authority | risk owner | operator owner, security / compliance, technical lead | Governance And Risk Overlay |
| production launch | production owner or designated approver | delivery, operations, security, business reviewer | Production Readiness Review |
| rollback | named rollback authority | incident lead, production owner | POC Acceptance Contract and runbook |
| expansion | program owner | product, operations, finance, risk | Expansion Roadmap |
| asset promotion | asset owner | product / platform / enablement owner | Field Signal Log and Asset Distillation Log |

A team can combine roles. It still needs one accountable owner for every decision.

## Field Cadence

### Discovery cadence

- replay at least one clean and one ugly case before solution design
- maintain the Reality Capture Gate after each evidence session
- log contradictions as open decisions or Field Signals

### Pilot cadence

- update the error taxonomy after every material failure class
- run regression checks on every meaningful behavior, prompt, model, tool, policy, or data change
- review adoption and workflow impact alongside model quality

### Launch cadence

- complete the Production Readiness Review before live authority, volume, or operator scope expands
- freeze the launch contract: owner, cohort, objectives, telemetry, incident triggers, containment, fallback, rollback, and approval

### Day-2 cadence

- inspect operational and quality signals on the agreed review cadence
- convert material production failures into incidents, eval cases, or both
- hold 24-hour, 7-day, and 30-day reviews for new live loops when risk and volume justify them
- track maintenance burden and operator workarounds

### Learning cadence

- review Field Signals on a fixed weekly or milestone cadence
- promote only signals with source evidence, recurrence or material impact, a destination, and an owner
- close rejected signals with the reason so the same weak claim does not re-enter later

## What To Measure

### Customer value

- time, quality, risk, throughput, or revenue impact against baseline
- operator adoption and repeat use
- share of eligible work completed through the loop
- reduction in shadow workflow or rework

### System quality

- task-level pass rate and critical failure count
- false-positive and false-negative consequences
- regression stability across versions
- production failures promoted into eval coverage

### Production reliability

- availability or workflow completion objective
- latency and queue health where relevant
- incident count, severity, detection time, and recovery time
- rollback success and manual fallback viability

### Product learning

- field signals classified and resolved
- reusable assets promoted
- recurrence across customers or workflows
- time from signal to validated product, template, eval, or policy decision

## Production Readiness Standard

A live loop needs all of the following:

- one bounded launch scope
- one production owner
- one target operator cohort
- measurable service and workflow objectives
- a versioned eval baseline and regression gate
- trace, audit, and monitoring coverage
- incident triggers and severity model
- support and escalation path
- containment boundary
- fallback and rollback path
- training and runbook readiness
- explicit launch decision

Use `assets/templates/production-readiness-review.md` as the decision artifact.

## Field Learning Standard

Field knowledge becomes reusable after it passes four tests:

1. **Evidence** — a source case, trace, incident, artifact, or observed workflow supports it.
2. **Meaning** — the constraint class and impact are clear.
3. **Recurrence or materiality** — it appears repeatedly or carries enough consequence to matter once.
4. **Destination** — a product, platform, eval, template, policy, operating process, or rejected-signal log owns the next action.

Use `assets/templates/field-signal-log.md` for this control loop.

## Delivery Packaging

For commercial and organizational settings where indefinite embedded engineering is hard to procure, package the operating role into bounded engagements with acceptance artifacts:

- Discovery Sprint -> G0 and G1
- Pilot Co-Build -> G2
- Production Readiness -> G3
- Deployment Rescue -> return to the broken gate
- Replication And Asset Distillation -> G4

The engagement is judged through evidence and decisions. On-site time, engineering effort, and advisory work remain inputs to the delivery plan.

## Official Practice Sources

The method above was synthesized from official materials describing production adoption, measurable workflow impact, eval-driven feedback, operational applications, action auditability, evaluation-driven development, containment, and operational readiness:

- OpenAI Forward Deployed Engineering roles: `https://openai.com/careers/search/?q=forward%20deployed`
- OpenAI evaluation practices: `https://openai.com/index/evals-drive-next-chapter-of-ai/`
- Palantir operational applications: `https://www.palantir.com/docs/foundry/app-building/operational-apps`
- Palantir action audit logs: `https://www.palantir.com/docs/foundry/action-types/action-log`
- Anthropic agent evaluations: `https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents`
- Anthropic agent containment: `https://www.anthropic.com/engineering/how-we-contain-claude`
- Google SRE postmortem culture: `https://sre.google/sre-book/postmortem-culture/`
- Google Cloud operational readiness: `https://cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops`
- Scale AI Forward Deployed Engineering roles: `https://scale.com/careers`
