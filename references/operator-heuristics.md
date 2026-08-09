# Operator Heuristics

## Mission Qualification

- Prefer workflows with recurring pain, not ceremonial pain.
- Prefer loops with a named operator and a measurable failure cost.
- Reject "knowledge assistant" asks when there is no decision or action downstream.
- Separate executive curiosity from an operating mission with a proof path.

## Reality Capture

- Ask for one clean example and one ugly example.
- Trace where responsibility moves, not just where data moves.
- Look for shadow tools: spreadsheets, chat groups, photos, screenshots, handwritten notes.
- Capture exception handling. That is often where the real system lives.
- Rank evidence by strength; keep narrative and inference visibly labeled.

## System Framing

- If the ask is broad, separate sensing, judgment, routing, execution, verification, and governance.
- Choose one bottleneck to fix first.
- Make non-goals explicit early to avoid stakeholder-driven scope inflation.
- Classify the binding constraint before routing it into product, delivery, policy, data, or change-management work.

## State, Action & Evidence Model

- If an object has no action or state consequence, it may not belong in the first model.
- If an action changes the world, specify authority, evidence, audit, containment, and rollback.
- Distinguish advisory outputs from state-changing actions.
- Treat action logs as decision lineage, not only technical telemetry.

## Intervention Design

- Use AI for ambiguity reduction before you use it for autonomy.
- Keep the pilot on the narrowest loop that can show time, quality, or risk improvement.
- A credible pilot has a fallback path that still works on a bad model day.
- Build eval cases from field failures and ambiguous decisions before polishing the demo path.

## Delivery Architecture

- Read-only pilots are easier to launch but often weaker at proving value.
- Write-back without audit is a governance hazard.
- The best operator interface is usually the one people already live in.
- Freeze source-of-truth, write-back, identity, audit, and ownership decisions before production launch.

## Production Readiness

- Demo success supplies evidence for readiness; it does not grant launch approval by itself.
- Review operator adoption, workflow impact, system quality, reliability, governance, and support as separate readiness areas.
- Define incident triggers before launch so severity is not negotiated during failure.
- Cap blast radius with narrow permissions, bounded data, limited cohorts, and reversible actions.
- A launch with no production owner is a delayed incident.

## Day-2 Operations

- Monitor the workflow outcome and the technical service; either one can fail independently.
- Promote material production failures into the Eval Pack.
- Track manual workarounds as product and operating signals.
- Measure maintenance burden before declaring repeatability.

## Expansion Logic

- Scale only after one loop is trusted, measured, owned, and supportable.
- Expansion by adjacent loop is usually safer than expansion by bigger customer promise.
- If each new site needs heroics, you do not have a program yet.
- Re-run Production Readiness when authority, volume, integration surface, or operator cohort materially changes.

## Field Learning And Asset Distillation

- Promote only what another operator could reuse without your live explanation.
- Distill ugly cases into eval assets before memory smooths them out.
- If a lesson changes future delivery, template, or product work, give it an owner and a destination.
- Classify each Field Signal before sending it to a roadmap.
- Require recurrence or material impact before turning a local workaround into a shared product commitment.
