---
name: deployment-readiness
description: Lightweight Applied AI skill for deciding whether a bounded AI loop is ready for live operator work, and for rescuing deployments with adoption, reliability, governance, or day-2 failures.
---

# Deployment Readiness

Use this skill when the main question is:

- can this pilot enter production or a live operator workflow
- what blocks launch
- how will adoption, observability, incidents, containment, fallback, and rollback work
- why is a live deployment losing trust, quality, or operator use

## Scope

Stay focused on production readiness and the earliest failed operating gate.

Primary outputs:

- `Production Readiness Review`
- `Day-2 Operations Plan`
- `Governance And Risk Overlay`
- `Field Signal Log`

Supporting inputs:

- `POC Acceptance Contract`
- `Eval Pack`
- `Minimum Viable Loop`
- `Reality Capture Gate`

## Readiness Areas

Evaluate each area separately:

1. workflow and launch scope
2. production ownership and support
3. operator cohort and adoption
4. evaluation and regression
5. observability, audit, and incident response
6. security, privacy, compliance, and authority
7. containment, fallback, and rollback
8. data, integration, capacity, and cost
9. training and runbook readiness
10. field-learning destination

## Decision

Return one posture:

- `go`
- `conditional-go` with blockers, owners, and re-review triggers
- `no-go` with evidence and re-entry conditions

For a deployment rescue, identify the earliest failed gate and return there. Do not default to a rebuild until the failing workflow, eval, ownership, or production evidence is understood.

## Do Not Expand Into

- broad account strategy
- organization-wide transformation planning
- new feature ideation without a field signal and evidence
- scale planning before the current loop is stable

## Completion Standard

A reviewer outside the build team can decide whether the loop should launch or continue running, who owns each risk, how failure is detected and contained, and what evidence will trigger the next review.

## Output Style

- launch decision first
- evidence versus inference separated
- blockers with owner and next proof
- explicit incident, containment, fallback, and rollback paths
- operator adoption and workflow impact beside technical metrics
- field signals routed to a named destination

## Template Reference

This skill uses four primary templates:

- `assets/templates/production-readiness-review.md`
- `assets/templates/day-2-operations-plan.md`
- `assets/templates/governance-and-risk-overlay.md`
- `assets/templates/field-signal-log.md`

It also reads:

- `assets/templates/poc-acceptance-contract.md`
- `assets/templates/eval-pack.md`
- `assets/templates/minimum-viable-loop.md`
- `assets/templates/reality-capture-gating.md`
- `references/fde-practice-system.md`
- `references/failure-patterns.md`

**Hermes**: `skill_view(name='fde-operator-os', file_path='assets/templates/<template-name>')`
**Codex / others**: read paths relative to the skill root.
