---
name: fde-operator-os
description: Applied AI operator playbook for delivery leads who need to qualify an AI opportunity, turn messy operational reality into a structured business system, design a minimum viable loop, and define a delivery-ready expansion path. Use when the user needs full-cycle FDE judgment, operator-grade artifacts, state-action-evidence framing, pilot design, or a cross-industry method for taking an AI use case from opportunity to closed-loop delivery.
---

# Applied AI Operator OS

## Canonical Name And Aliases

Canonical skill name:

- `fde-operator-os`

Recommended short aliases:

- `fde`
- `applied`

Important:

- The canonical workflow and artifacts remain the same under all names.
- Slash-command behavior such as `/FDE` depends on the host runtime.
- If a runtime does not support aliases natively, keep `fde-operator-os` as the canonical package name and add local wrappers or prompt aliases in that host.

## Template Path Resolution

This skill uses `${CLAUDE_SKILL_DIR}` in template/artifact references throughout. That convention is **Codex-specific** and does NOT resolve in other runtimes.

**Hermes**: Load templates via `skill_view(name='fde-operator-os', file_path='assets/templates/mission-brief.md')`. The first `skill_view()` call returns a `linked_files` dict showing all available references, assets, and templates.

**Other runtimes**: Treat `assets/templates/` and `references/` as relative paths from the skill root. Browse the directory to find files rather than relying on `${CLAUDE_SKILL_DIR}` expansion.

## Role

Use this skill as an operator doctrine for senior FDE, applied AI, and delivery leads.

This is not a generic workshop template and not a field-notes checklist. It is a decision system for turning a customer problem into a delivery-worthy AI operating loop.

FDE here is not on-site outsourcing. It is the operating role that turns field ambiguity into reusable delivery and product capability.

## Router Behavior

This core skill is the canonical doctrine and routing surface.

Default behavior:

- classify the request shape first
- route to a lighter leaf skill when one request shape dominates
- run the full end-to-end doctrine directly only when the user explicitly asks for full-cycle operator work or when the problem truly spans multiple shapes

Preferred request-shape routing:

- qualification-heavy requests -> `mission-qualifier`
- reality and workflow reconstruction -> `reality-capture`
- bounded pilot compression -> `pilot-designer`

The router should avoid expanding into the full seven-stage workflow when a lighter skill can solve the request with less context and less process overhead.

## Default Stance

1. Qualify before designing.
2. Model the real operating system, not the narrated process.
3. Solve for closed-loop outcomes, not feature demos.
4. Keep AI on the narrowest surface that creates measurable value.
5. Treat human trust, governance, and operating ownership as first-class design inputs.
6. Every delivery should leave behind at least one reusable asset.
7. If the account context is broad, pick one operator loop before summarizing the whole project.

Read `${CLAUDE_SKILL_DIR}/references/doctrine.md` first when the request is broad, strategic, or politically messy.

## First-Run Mode

Use this mode when the user is trying the skill for the first time, or when the workspace contains broad strategy, sales, or project-management material that could drown the core FDE loop.

Rules:

1. Choose **one operator, one object, one trigger, and one output loop** before reading the whole account.
2. Prefer running **Stage 2 -> Stage 5 + POC Acceptance Contract** on that bounded loop.
3. Explicitly list what is **out of scope** for this run.
4. Stop before Delivery Architecture if operational evidence is still thin.
5. Treat broad project summaries as background only; the main output should be loop-operable artifacts.

This mode exists to prevent first-time use from collapsing into generic account strategy or project recap.

## Engagement Modes

Use `${CLAUDE_SKILL_DIR}/references/engagement-modes.md` to adapt the doctrine to different field situations without forcing every request through the deepest possible output.

Default modes:

- Discovery Sprint
- Pilot Design
- Deployment Rescue
- Post-Delivery Asset Distillation

The mode changes where you start, what depth is required, and where you should stop. It does not change the core doctrine.

## When To Use

Use this skill when the user needs any of the following:

- decide whether an industry or customer problem is worth an AI engagement
- turn a messy business situation into a structured system definition
- define the full-cycle FDE path from discovery to pilot to delivery
- design business objects, workflow, action surfaces, and human-in-the-loop boundaries
- compress a broad opportunity into a minimum viable loop or POC
- create operator-grade artifacts that another engineer or delivery lead can continue from

Typical trigger requests:

- "这个场景值不值得做 AI 交付"
- "帮我把这个行业问题拆成可落地系统"
- "梳理 FDE 全周期方法和交付工件"
- "先别做方案，先判断该不该做、先做哪段"
- "把 demo 压成一个能验收的最小闭环"

Do not use this skill for:

- pure vendor selection
- pure coding implementation without upstream delivery framing
- a one-off meeting summary that does not need system design
- industry knowledge lookup with no delivery decision attached

## FDE Boundary Discipline

Keep the output inside the FDE lane unless the user explicitly asks for broader account work.

Default exclusions:

- pricing and packaging debate
- relationship mapping that does not affect loop ownership
- generic project status reporting
- broad leadership narrative with no effect on operator, authority, evidence, or acceptance

If those topics do affect viability, mention them only as constraints on the loop, not as the center of the artifact set.

## Operating Loop

Run the seven stages in order unless the user explicitly enters with a later-stage artifact already in hand.

For every stage, produce:

- judgment questions
- entry conditions
- evidence you must not skip
- standard outputs
- failure signals
- exit condition to the next stage

If the user asks for speed, compress depth, not structure. Keep the stage order.

## Stage 1: Mission Qualification

Goal: decide whether the opportunity is worth committing to.

Answer:

- What problem class is this really in: perception, decision support, workflow orchestration, or closed-loop operations?
- Is the value density high enough to justify delivery effort?
- Is there a measurable operational outcome, not just executive curiosity?
- Are data, ownership, and organizational conditions minimally viable?
- What would make this a no-go or not-now?

Do not skip:

- business pain with consequence
- named operator or accountable owner
- success condition with observable proof
- blocking constraints such as policy, access, latency, or missing authority

Output artifact:

- `${CLAUDE_SKILL_DIR}/assets/templates/mission-brief.md`

Exit when:

- there is a clear mission statement, success test, and go/no-go posture

Failure signals:

- "we want to explore AI" with no operational target
- no accountable operator
- no plausible proof path inside 30-90 days

## Stage 2: Operational Reality Capture

Goal: capture how work actually moves today.

Answer:

- Who detects, decides, acts, approves, and bears risk?
- What does the real workflow look like, including exceptions and workarounds?
- Which systems, files, channels, and manual steps are in the loop?
- What evidence exists: logs, forms, SOPs, screenshots, tickets, photos, spreadsheets, transcripts?
- Where do trust, delay, rework, or responsibility break down?

Do not skip:

- exception paths
- one clean case replay
- one ugly case replay
- shadow workflows outside the official system
- sample artifacts from the current process
- failure cases and disputed cases

Output artifact:

- `${CLAUDE_SKILL_DIR}/assets/templates/operational-reality-map.md`
- `${CLAUDE_SKILL_DIR}/assets/templates/case-replay-pack.md` as a supporting artifact when concrete or disputed cases are available

Read `${CLAUDE_SKILL_DIR}/references/operator-heuristics.md` for reality-capture heuristics when the process is politically filtered or poorly documented.

Exit when:

- you can reconstruct the current operating loop without relying on stakeholder rhetoric

Failure signals:

- only ideal-state process maps
- no concrete examples
- no understanding of where responsibility transfers

## Stage 3: System Framing

Goal: define the actual system problem.

Answer:

- What is the system boundary?
- Which subproblem matters most right now?
- Is the bottleneck sensing, interpretation, routing, execution, verification, or governance?
- What north-star outcome should the system optimize for?
- Which assumptions, if false, collapse the project?

Do not skip:

- problem decomposition
- explicit non-goals
- constraints that shape architecture
- assumptions that require validation

Output artifact:

- `${CLAUDE_SKILL_DIR}/assets/templates/system-problem-frame.md`

Exit when:

- the team can say what problem is being solved and what problem is intentionally deferred

Failure signals:

- the system is trying to solve every stakeholder request at once
- the problem statement is really a tool wishlist

## Stage 4: State, Action & Evidence Model

Goal: translate the business world into an AI-operable system.

Answer:

- What are the key business objects, relationships, states, actions, rules, events, and permissions?
- Which actions are write-capable versus advisory only?
- Which states require human confirmation?
- What evidence moves an item from one state to another?

Do not skip:

- state transitions
- write permissions
- event triggers
- ambiguous or disputed entities

Output artifact:

- `${CLAUDE_SKILL_DIR}/assets/templates/ontology-action-model.md`

Read `${CLAUDE_SKILL_DIR}/references/doctrine.md` again if the team drifts into feature-thinking instead of system-thinking.

Exit when:

- the business loop can be described as objects plus actions plus proof of transition

Failure signals:

- ontology contains nouns only and no action surface
- actions exist with no owner or evidence requirement

## Stage 5: Intervention & Pilot Design

Goal: choose the minimum AI surface that changes the outcome.

Answer:

- Where should AI intervene: detect, classify, summarize, recommend, route, verify, or act?
- What must remain human-owned?
- What is the minimum viable loop that proves value?
- What are the critical failure modes and demo-killing edge cases?

Do not skip:

- false-positive and false-negative consequences
- fallback path when AI is wrong or uncertain
- scope cuts that keep the pilot honest

Output artifacts:

- `${CLAUDE_SKILL_DIR}/assets/templates/ai-intervention-design.md`
- `${CLAUDE_SKILL_DIR}/assets/templates/minimum-viable-loop.md`
- `${CLAUDE_SKILL_DIR}/assets/templates/eval-pack.md` as a required support artifact for credible pilots

Exit when:

- one narrow loop is defined with concrete inputs, outputs, and proof

Failure signals:

- pilot scope requires full enterprise integration to show value
- AI is inserted because it is impressive, not because it removes a bottleneck

## Stage 6: Delivery Architecture

Goal: define how the loop runs in the real world.

Answer:

- What systems must be read from or written to?
- What interface will operators actually use?
- What telemetry, audit, and governance are required?
- Who owns day-2 operations and exception handling?

Do not skip:

- source-of-truth systems
- write-back rules
- observability and audit trail
- operating owner after launch

Output addition:

- add delivery architecture details into `${CLAUDE_SKILL_DIR}/assets/templates/minimum-viable-loop.md`
- lock acceptance expectations in `${CLAUDE_SKILL_DIR}/assets/templates/poc-acceptance-contract.md`
- define trust, permissions, and rollback in `${CLAUDE_SKILL_DIR}/assets/templates/governance-and-risk-overlay.md`
- define support, monitoring, and exception ownership in `${CLAUDE_SKILL_DIR}/assets/templates/day-2-operations-plan.md`

Read `${CLAUDE_SKILL_DIR}/references/failure-patterns.md` before finalizing architecture in regulated or high-accountability domains.

Exit when:

- the loop can be explained as a runbook, not just a demo

Failure signals:

- no write-back plan
- no exception owner
- no audit path for decisions and actions

## Stage 7: Expansion Logic

Goal: decide how the pilot becomes a program.

Answer:

- What has to be true before replication?
- Which adjacent loops should come next?
- What platform, data, and org capabilities need to harden?
- Which risks grow faster than value?

Do not skip:

- sequence of expansion
- dependency map
- reasons not to scale yet
- proof required before broad rollout

Output artifact:

- `${CLAUDE_SKILL_DIR}/assets/templates/expansion-roadmap.md`

Exit when:

- there is a staged path from one loop to a broader operating system

Failure signals:

- scaling is justified only by leadership enthusiasm
- pilot success criteria do not map to expansion criteria

## Post-Delivery Overlay: Asset Distillation Loop

Goal: convert delivery learning into reusable capability.

Run this after a credible loop exists. This is not Stage 8 of delivery design. It is the closeout overlay that prevents the work from collapsing into custom-project labor.

Answer:

- What should be promoted from this case into a reusable problem pattern?
- Which workflow or operating steps are stable enough to become a template?
- What data-readiness, eval, or governance checks should be reused next time?
- Which failure cases should become test cases?
- What should be turned into SOP, skill, internal tool, or product backlog?
- What is still too project-specific to promote?
- Which day-2 failures or eval failures should be promoted into reusable checks, cases, or overlays?

Do not skip:

- source evidence for each lesson
- promotion threshold for reusability
- the difference between project notes and reusable assets
- explicit owner for maintaining promoted assets

Output artifacts:

- `${CLAUDE_SKILL_DIR}/references/asset-distillation-loop.md`
- `${CLAUDE_SKILL_DIR}/assets/templates/asset-distillation-log.md`

Exit when:

- at least one reusable asset is defined with owner, proof, and target reuse context

Failure signals:

- lessons remain trapped in narrative debriefs
- project artifacts cannot be reused without the original operator present
- no feedback path exists from delivery back into product, template, or eval assets

## Artifact Set

The core operator artifacts are:

1. `Mission Brief`
2. `Operational Reality Map`
3. `System Problem Frame`
4. `State, Action & Evidence Model`
5. `AI Intervention Design`
6. `Minimum Viable Loop`
7. `POC Acceptance Contract`
8. `Expansion Roadmap`

Execution-grade support artifacts should also be used when the loop reaches pilot or deployment depth:

9. `Case Replay Pack`
10. `Eval Pack`
11. `Governance And Risk Overlay`
12. `Day-2 Operations Plan`

Post-delivery closeout should also produce:

13. `Asset Distillation Log`

Use the templates in `${CLAUDE_SKILL_DIR}/assets/templates/`.

Rules:

1. Fill required fields before adding narrative.
2. Mark unknowns explicitly instead of smoothing them over.
3. Treat contradictions as design inputs, not cleanup noise.
4. Do not move forward if the current artifact still contains unowned decisions.

## References

- Doctrine: `${CLAUDE_SKILL_DIR}/references/doctrine.md`
- Heuristics: `${CLAUDE_SKILL_DIR}/references/operator-heuristics.md`
- Failure patterns: `${CLAUDE_SKILL_DIR}/references/failure-patterns.md`
- Asset distillation: `${CLAUDE_SKILL_DIR}/references/asset-distillation-loop.md`
- Engagement modes: `${CLAUDE_SKILL_DIR}/references/engagement-modes.md`

## Case Handling

Keep domain cases outside the core skill by default.

If you are validating this skill against a local project, treat that case material as private working context, not as part of the shipped skill. Use local notes or a separate private case pack to stress-test the doctrine, artifacts, heuristics, and asset-distillation outputs.

## Output Style

Return operator-grade outputs:

- concise judgment first
- evidence versus inference separated
- explicit risks and unknowns
- staged next action, not generic recommendations

If the user is early-stage, stop after Mission Qualification or System Framing instead of pretending the later stages are ready.

If the user is late-stage, backfill missing upstream artifacts before proposing architecture or scale.
