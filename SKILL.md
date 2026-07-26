---
name: fde-operator-os
description: Applied AI operator system for delivery leads who need to qualify an AI opportunity, reconstruct operational reality, design a minimum viable loop, pass production-readiness gates, and return field learning into reusable delivery and product assets. Use for full-cycle FDE judgment, state-action-evidence framing, pilot contracts, production adoption, deployment rescue, and cross-industry closed-loop delivery.
---

# Applied AI Operator OS

## Role

Use this skill as the canonical doctrine and router for Forward Deployed Engineering and Applied AI delivery.

The operating role connects four worlds:

1. customer mission and workflow reality
2. system design and implementation constraints
3. production operation and reliability
4. reusable product, platform, eval, and delivery assets

The output standard is an evidenced, owned, judgeable operator loop. Route pure implementation, generic workshops, vendor comparison, or context-free industry research elsewhere.

## Canonical Name And Paths

Canonical skill name:

- `fde-operator-os`

Recommended aliases:

- `fde`
- `applied`

Relative paths start from the folder containing this `SKILL.md`.

- **Codex / Claude Code / similar hosts**: read paths relative to the skill root.
- **Hermes**: use `skill_view(name='fde-operator-os', file_path='assets/templates/mission-brief.md')`.
- **Other runtimes**: expose the root skill or selected child skills; see `references/runtime-portability.md`.

Host-specific slash commands belong in wrappers under `aliases/`.

## Router

Classify the request before loading the full method.

| Dominant request shape | Route |
|---|---|
| opportunity qualification or early go / no-go | `mission-qualifier` |
| workflow reconstruction, evidence collection, or exception replay | `reality-capture` |
| bounded pilot, acceptance contract, or eval design | `pilot-designer` |
| launch review, production adoption, day-2 risk, or deployment rescue | `deployment-readiness` |
| multi-stage or full-cycle operator work | root `fde-operator-os` |

Use the lightest skill that can make the required decision. Return to the root method when the request crosses multiple gates.

## Default Stance

1. Qualify before designing.
2. Model observed work, shadow workflows, and exception paths.
3. Solve for a closed-loop outcome with a named operator.
4. Keep AI on the narrowest surface that changes measurable value.
5. Define action, authority, evidence, audit, containment, fallback, and rollback together.
6. Treat operator adoption and workflow impact as delivery outcomes.
7. Treat evals, production traces, incidents, and regression cases as one quality system.
8. Make every gate decision explicit: `go`, `conditional-go`, or `no-go`.
9. Make every credible delivery leave reusable capability behind.

Read `references/doctrine.md` for the shared principles and `references/fde-practice-system.md` for the production-grade operating model.

## Four Concurrent Control Loops

Run the seven delivery stages through four control loops:

1. **Customer value** — mission fit -> operator adoption -> measurable workflow impact.
2. **System quality** — real cases -> eval tasks -> regression gates -> production traces.
3. **Production reliability** — readiness review -> telemetry -> incident response -> postmortem and hardening.
4. **Product learning** — field signal -> constraint classification -> reusable asset or roadmap decision.

The delivery stages sequence work. The control loops prevent local progress from hiding quality, adoption, reliability, or learning failures.

## Five Gates

| Gate | Decision | Required evidence |
|---|---|---|
| G0 Mission Fit | Is this worth committing to? | named operator, consequence, observable outcome, blocking constraints |
| G1 Evidence Sufficiency | Do we understand the real loop? | real case replays, measured baseline, source artifacts, owners, explicit gaps |
| G2 Pilot Contract | Can a bounded pilot prove or disprove value? | minimum loop, representative evals, acceptance, authority, fallback, rollback |
| G3 Production Readiness | Can the loop enter live work with controlled risk? | owner, adoption plan, regression gate, observability, incident response, containment, support |
| G4 Replication And Asset Promotion | Should this repeat, expand, or become reusable capability? | repeatable impact, stable operating burden, known risks, reusable evidence |

Use the machine-readable definitions in `contracts/artifacts.json` as the artifact and gate source of truth.

## First-Run Mode

Use this mode when the input contains broad account, sales, strategy, or project material.

1. Choose one operator.
2. Choose one business object.
3. Choose one trigger.
4. Choose one output.
5. State the out-of-scope boundary.
6. Run Stage 2 through Stage 5 on that bounded loop.
7. Stop before Delivery Architecture while evidence remains thin.

The default first-run deliverables are:

- Mission Brief
- Operational Reality Map
- System Problem Frame
- State, Action & Evidence Model
- AI Intervention Design
- Minimum Viable Loop
- POC Acceptance Contract
- Eval Pack

## Stage Execution Protocol

For each stage, record:

- judgment questions
- entry evidence
- required artifacts
- unknowns and blockers
- exit or gate posture
- owner and next proof
- failure signals that require returning upstream

When speed matters, compress depth and preserve the decision sequence.

## Stage 1: Mission Qualification

**Goal:** decide whether the opportunity deserves delivery effort.

Answer:

- What recurring operational pain carries measurable consequence?
- Who owns the outcome and who performs the work?
- What proof can be collected in a bounded time window?
- Which constraint could force `no-go` or `conditional-go`?

Required evidence:

- operational pain and consequence
- accountable owner
- observable success metric
- critical constraints and verification path

Artifact:

- `assets/templates/mission-brief.md`

Exit through G0 when the mission, proof path, and posture are explicit.

Failure signals:

- executive curiosity with no operating target
- no accountable owner
- no plausible baseline or proof path

## Stage 2: Operational Reality Capture

**Goal:** reconstruct how work moves today.

Capture:

- actors and responsibility transfers
- official workflow and shadow workflow
- systems, files, channels, and manual steps
- clean, ugly, disputed, and handoff-failure cases
- evidence available at each decision point
- measured baseline, reviewer capacity, and open gaps

Artifacts:

- `assets/templates/operational-reality-map.md`
- `assets/templates/case-replay-pack.md`
- `assets/templates/reality-capture-gating.md`

Use `references/operator-heuristics.md` when the workflow is politically filtered or poorly documented.

Exit through G1 when another operator can replay the real loop and the Reality Capture Gate states which evidence is collected, inferred, or blocking.

Failure signals:

- ideal-state process only
- narrative without source artifacts
- unnamed responsibility transfers
- estimated baseline presented as measured fact

## Stage 3: System Framing

**Goal:** define the bounded system problem and binding constraint.

Answer:

- What is inside the system boundary?
- Which bottleneck matters now: sensing, interpretation, routing, execution, verification, or governance?
- Which adjacent requests remain deferred?
- Which assumption could invalidate the plan?
- Is the binding constraint product, model/eval, data, integration, policy, change management, delivery execution, or operating model?

Artifact:

- `assets/templates/system-problem-frame.md`

Exit when the team can state the bottleneck, boundary, non-goals, and invalidating assumptions.

Failure signals:

- feature wishlist presented as a problem frame
- multiple bottlenecks bundled into the first loop
- local delivery friction routed directly into product scope without classification

## Stage 4: State, Action & Evidence Model

**Goal:** translate the business world into a run-capable control model.

Define:

- business objects and relationships
- states and valid transitions
- events and triggers
- actions and owners
- advisory, gated, and write authority
- evidence required for state change
- audit, containment, and rollback rules

Canonical artifact:

- `assets/templates/state-action-evidence-model.md`

Compatibility path:

- `assets/templates/ontology-action-model.md`

Exit when a technical team can infer what the system reads, decides, changes, proves, and reverses.

Failure signals:

- nouns without state consequence
- actions without authority or owner
- state changes without evidence or audit

## Stage 5: Intervention & Pilot Design

**Goal:** choose the smallest AI surface that can prove or disprove value.

Define:

- target bottleneck and AI role
- human confirmation boundary
- baseline manual path
- trigger, transformation, action, output, verification, and audit
- golden, failure, edge, ambiguous, and demo-killing eval cases
- graders, thresholds, measurement window, and regression check
- fallback and rollback conditions
- operator adoption signal

Artifacts:

- `assets/templates/ai-intervention-design.md`
- `assets/templates/minimum-viable-loop.md`
- `assets/templates/poc-acceptance-contract.md`
- `assets/templates/eval-pack.md`
- `assets/templates/governance-and-risk-overlay.md` when AI influences operational action

Exit through G2 when an independent reviewer can judge the pilot without renegotiating scope or success.

Handoff to `deployment-readiness` after the pilot contract, representative evals, authority, audit, adoption signal, fallback, rollback, and remaining launch dependencies are explicit.

Failure signals:

- full enterprise integration required before any proof
- polished demo cases with no failure taxonomy
- acceptance defined after build
- pilot completion treated as launch approval

## Stage 6: Delivery Architecture

**Goal:** define how the loop enters and survives real operator work.

Entry condition:

- G1 is evidence-sufficient, or partial with every inferred section flagged
- at least one real clean and ugly case exists
- operating and exception owners are named
- current cycle time and volume are measured
- source-of-truth and knowledge dependencies are known

Decide:

- read and write integrations
- operator interface and target cohort
- service and workflow objectives
- versioned eval baseline and regression gate
- telemetry, traces, audit, and production sampling
- incident triggers and severity model
- containment boundary
- support, escalation, fallback, and rollback
- training, runbook, capacity, and cost guardrails
- field-signal destination

Artifacts:

- `assets/templates/day-2-operations-plan.md`
- `assets/templates/governance-and-risk-overlay.md`
- `assets/templates/production-readiness-review.md`
- `assets/templates/field-signal-log.md`

Use `references/failure-patterns.md` before a high-accountability launch.

Exit through G3 with an explicit `go`, `conditional-go`, or `no-go` decision, including blockers, owners, next proof, and re-review triggers.

Failure signals:

- no production owner or exception owner
- missing operator adoption plan
- no regression or production trace path
- incident severity negotiated during failure
- no containment, fallback, or rollback path

## Stage 7: Expansion Logic

**Goal:** decide whether the proven loop should repeat or expand.

Answer:

- Which outcome and adoption signals are repeatable?
- What operating burden remains?
- Which adjacent loop is the safest next step?
- Which platform, data, governance, or organizational capability must harden first?
- Which risks grow faster than value?
- What evidence would force a hold?

Artifact:

- `assets/templates/expansion-roadmap.md`

Re-run G3 when authority, volume, integration surface, data sensitivity, or operator cohort changes materially.

Exit through G4 when replication conditions, dependencies, risks, stage gates, and hold reasons are explicit.

Failure signals:

- expansion justified by leadership enthusiasm
- operating burden hidden by embedded heroics
- pilot criteria disconnected from replication criteria

## Post-Delivery Asset Distillation

**Goal:** convert field learning into reusable capability.

Run the overlay after credible evidence exists. A prospective pass may mark candidates `hold` while naming what evidence to collect.

Capture:

- source case and evidence
- reusable pattern hypothesis
- constraint classification
- asset type and reuse target
- promotion status: `observe`, `validate`, `promote`, or `reject`
- destination, owner, next proof, and maintenance action

Artifacts:

- `assets/templates/field-signal-log.md`
- `assets/templates/asset-distillation-log.md`
- `references/asset-distillation-loop.md`

Exit when at least one asset or roadmap decision has evidence, owner, destination, and a concrete next reuse context.

Failure signals:

- lessons trapped in recap narratives
- every customer request routed into the product backlog
- assets require the original operator to explain them live
- no owner or maintenance path

## Artifact Set And Source Of Truth

The 16 governed artifacts and required fields are defined in `contracts/artifacts.json`.

Canonical cross-artifact fields:

- **Operating owner** — Day-2 Operations Plan
- **Exception owner** — Day-2 Operations Plan
- **Rollback condition** — POC Acceptance Contract
- **Fallback mode** — Minimum Viable Loop
- **Drift / degradation signal** — Day-2 Operations Plan
- **Success / failure criteria** — POC Acceptance Contract
- **AI authority level** — Governance And Risk Overlay
- **Production launch decision** — Production Readiness Review
- **Operator adoption signal** — Day-2 Operations Plan
- **Field constraint and destination** — Field Signal Log

Reference canonical values from other artifacts. When the source artifact is pending, mark the temporary value for later consolidation.

## Engagement Modes

Use `references/engagement-modes.md` for bounded delivery packages:

- Discovery Sprint -> G0 and G1
- Pilot Design -> G2
- Production Readiness -> G3
- Deployment Rescue -> return to the earliest failed gate
- Post-Delivery Asset Distillation -> G4

## Case Discipline

Keep private customer material outside the shipped skill.

A public case must be synthetic, public, or explicitly sanitized. Index governed examples through `case-manifest.json`, record gate posture honestly, and keep domain-specific lessons separate from cross-industry doctrine.

## Output Standard

Return operator-grade outputs with:

- judgment first
- evidence and inference separated
- named unknowns and blockers
- owner, authority, and next proof
- explicit gate posture
- staged action tied to the earliest unresolved constraint

For early-stage work, stop when the next gate lacks evidence. For late-stage work, backfill the earliest missing upstream artifact before proposing architecture or scale.

## Validation

Before changing or shipping this skill, run:

```bash
python tools/validate_repo.py
python -m unittest discover -s tests -v
```

Repository editing rules live in `AGENTS.md`.
