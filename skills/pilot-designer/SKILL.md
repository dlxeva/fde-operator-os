---
name: pilot-designer
description: Lightweight Applied AI skill for compressing a bounded loop into a credible pilot with acceptance, eval, governance, fallback, and production-readiness handoff.
---

# Pilot Designer

Use this skill when the main question is:

- what is the smallest credible pilot
- where should AI intervene
- what remains human-owned
- how will the pilot be judged
- what evidence is required before production-readiness review

## Scope

Stay focused on bounded pilot design and the G2 Pilot Contract gate.

Primary outputs:

- `AI Intervention Design`
- `Minimum Viable Loop`
- `POC Acceptance Contract`
- `Eval Pack`
- `Governance And Risk Overlay` when the AI influences operational action

## What To Define

- target bottleneck
- narrow AI surface
- human confirmation boundary
- baseline manual path
- representative tasks and failure classes
- explicit graders and acceptance thresholds
- fallback and rollback conditions
- audit and authority boundary
- operator adoption signal
- production-readiness dependencies

## Evidence Requirement

Build pilot cases from observed work where available:

- golden cases
- failure cases
- edge cases
- ambiguous cases
- demo-killing cases

Keep synthetic cases labeled. Carry missing production evidence into the Reality Capture Gate or Production Readiness Review as a blocker.

## Production Handoff

The pilot is ready to hand to `deployment-readiness` when:

- the bounded loop and baseline are stable
- the POC Acceptance Contract is locked
- representative eval cases and regression checks exist
- authority, audit, fallback, and rollback are defined
- the intended operator cohort and adoption signal are known
- remaining launch dependencies are explicit

This handoff does not imply launch approval. `deployment-readiness` owns the G3 go, conditional-go, or no-go decision.

## Do Not Expand Into

- broad account strategy
- full platform architecture before the loop is proven
- organization-wide rollout
- live launch approval
- detailed day-2 operations beyond the pilot boundary and handoff requirements

## Completion Standard

A reviewer can explain the bounded pilot, AI and human responsibilities, baseline, representative evals, acceptance and failure criteria, fallback and rollback paths, and the evidence still needed before live use.

## Output Style

- one narrow loop
- explicit baseline and measurement window
- explicit task, grader, threshold, and regression logic
- explicit failure, fallback, and rollback conditions
- operator adoption signal included
- production handoff blockers named

## Template Reference

This skill uses five primary templates:

- `assets/templates/ai-intervention-design.md`
- `assets/templates/minimum-viable-loop.md`
- `assets/templates/poc-acceptance-contract.md`
- `assets/templates/eval-pack.md`
- `assets/templates/governance-and-risk-overlay.md`

It may also read:

- `assets/templates/reality-capture-gating.md`
- `assets/templates/production-readiness-review.md`
- `references/fde-practice-system.md`

**Hermes**: `skill_view(name='fde-operator-os', file_path='assets/templates/<template-name>')`
**Codex / others**: read paths relative to the skill root.
