# Operational Reality Map

## Actors

- Frontline submitter
- Operations coordinator
- Response owner
- Program manager

## Responsibility Chain

- Detect: Frontline submitter
- Decide: Operations coordinator
- Act: Response owner
- Approve: Operations coordinator
- Audit: Program manager / monthly review owner

## Current Workflow

1. Frontline submitter captures a screenshot and optional note when an issue appears.
2. Ambiguous submissions are discussed in a chat group before formal submission.
3. Coordinator reviews the submission and decides whether it qualifies as a resolution-worthy exception.
4. Coordinator manually creates a task in the existing system.
5. Response owner marks the item as fixed and may attach text or evidence.
6. Coordinator decides whether closure evidence is sufficient.
7. Overdue items are tracked in a private spreadsheet.
8. Monthly summaries are compiled manually.

## Systems / Channels

- web submission form
- unofficial chat group
- tasking system
- coordinator spreadsheet

## Evidence Artifacts

- SOP: issue triage guide and escalation rules
- Form / spreadsheet: submission export and overdue tracker
- Screenshot / attachment: issue evidence and closure evidence
- Task / log: resolution task IDs and timestamps

## Clean Case Replay

- Trigger: a frontline submitter sends a clear screenshot for the target exception category.
- Decision: the coordinator confirms the exception against the triage guide.
- Action: the coordinator creates a resolution task and assigns the response owner.
- Evidence available: screenshot, location, timestamp, category, and short note.
- Outcome: the response owner uploads closure evidence; the coordinator approves closure on the first review.
- What this case proves: the official path can close cleanly when evidence and category boundaries are clear.
- What this case does not prove: how the workflow handles ambiguity, weak evidence, or disputed ownership.

## Ugly Case Replay

- Trigger: a blurry screenshot arrives with no location and a vague note.
- Decision: two coordinators disagree in chat about whether the submission is in scope.
- Action: one coordinator creates a task after a private clarification; the clarification is absent from the task record.
- Evidence available: original screenshot, chat messages, and a late location update.
- Outcome: the response owner marks the task fixed with text only; closure is accepted after two follow-ups, while the overdue spreadsheet stays out of sync.
- What this case proves: ambiguity, shadow communication, weak closure evidence, and duplicate tracking create delay and audit gaps.
- What this case does not prove: the frequency of this failure class across all categories or regions.

## Exception Paths

- low-confidence submissions are discussed informally and may never enter the formal system
- closure may be accepted based on text only when evidence is missing
- disputed ownership can leave the item in chat without a task
- overdue items can diverge between the tasking system and private spreadsheet

## Failure Points

- qualification threshold is inconsistent across reviewers
- evidence quality is weak at intake and closure
- clarifying decisions occur outside the source-of-truth workflow
- overdue tracking lives outside the official task loop
