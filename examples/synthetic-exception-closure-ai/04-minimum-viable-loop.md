# Minimum Viable Loop

- **Trigger input**: Frontline submitter sends a screenshot and short note for one target exception category
- **AI judgment / transformation**: AI classifies the submission into likely valid exception, likely not an exception, or uncertain; it also drafts a rationale for coordinator review
- **Action / routing**: The submission is routed to the coordinator with a suggested disposition and a prefilled resolution task draft
- **Human confirmation**: Coordinator approves, edits, or rejects the suggested disposition before any task is created
- **Output / write-back**: Approved items create a task in the existing system with attached evidence and standardized exception metadata
- **Feedback / verification**: Response owner uploads closure evidence; coordinator reviews evidence against a minimal standard
- **Archive / audit**: Submission, decision rationale, approval, task ID, closure evidence, and timestamps are retained for reporting
- **Required integrations**:
  - web submission export
  - tasking system
  - evidence storage for attachments
- **Operator interface**: Existing coordinator review screen or a lightweight review queue layered on top
- **Operating owner**: Regional operations coordinator
- **Fallback mode**: If AI confidence is low or the draft is obviously wrong, coordinator handles the case manually without task auto-drafting
