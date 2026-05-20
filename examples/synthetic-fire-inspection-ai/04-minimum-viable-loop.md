# Minimum Viable Loop

- **Trigger input**: Inspector submits a photo and short note for one target hazard category
- **AI judgment / transformation**: AI classifies the submission into likely valid hazard, likely not a hazard, or uncertain; it also drafts a rationale for supervisor review
- **Action / routing**: The submission is routed to the supervisor with a suggested disposition and a prefilled remediation ticket draft
- **Human confirmation**: Supervisor approves, edits, or rejects the suggested disposition before any ticket is created
- **Output / write-back**: Approved items create a ticket in the existing facilities system with attached evidence and standardized hazard metadata
- **Feedback / verification**: Facilities responder uploads closure evidence; supervisor reviews evidence against a minimal standard
- **Archive / audit**: Submission, decision rationale, approval, ticket ID, closure evidence, and timestamps are retained for reporting
- **Required integrations**:
  - mobile inspection form export
  - facilities ticketing system
  - evidence storage for photos
- **Operator interface**: Existing supervisor review screen or a lightweight review queue layered on top
- **Operating owner**: Regional safety supervisor
- **Fallback mode**: If AI confidence is low or the draft is obviously wrong, supervisor handles the case manually without ticket auto-drafting
