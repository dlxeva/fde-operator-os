# Synthetic Cross-Border Commerce Operator Loop Pack

> This is a fictional composite case created solely to demonstrate the methodology. It does not describe any specific company, customer, marketplace account, shipment, deployment, or observed operational weakness.

## Scenario

A cross-border commerce operations team needs a tighter loop for resolving order exceptions across multiple marketplaces, fulfillment partners, and customer-support channels.

## Minimum Viable Loop Fragment

- **Trigger input**: an order enters the exception queue because marketplace, SKU, inventory, address-format, or fulfillment records disagree
- **Baseline manual path**: operator checks marketplace messages, order records, inventory sheets, and fulfillment updates before creating a resolution task
- **AI judgment / transformation**: AI consolidates the available records, identifies the disputed fields, and drafts a recommended next action with cited evidence
- **Action / routing**: operator reviews the recommendation and routes a confirmed task to the responsible fulfillment or support owner
- **Human confirmation**: operator must confirm the exception type, evidence, owner, and customer-facing message before any update
- **Output / write-back**: structured exception task linked to the original order and source records
- **Feedback / verification**: resolution owner confirms the action and attaches closure evidence
- **Archive / audit**: source records, AI draft, operator decision, task owner, timestamps, and closure evidence are retained
- **Required integrations**: none for the synthetic demonstration; source records are represented as fictional fixtures
- **Operating owner**: fictional cross-border operations lead
- **Operator adoption signal**: operators resolve eligible exceptions through the shared queue without rebuilding the case in private spreadsheets or chat threads
- **Day-2 maintenance burden**: weekly review of exception categories, SKU mappings, marketplace message formats, and rejected recommendations
- **Drift / degradation signal**: increasing operator overrides, repeated misrouting, or new marketplace formats that the evidence parser cannot reconcile
- **Rollback condition**: revert to manual exception triage when evidence links are missing, override rate exceeds the agreed threshold, or task routing becomes unreliable
- **Fallback mode**: operator follows the existing manual checklist and records the decision without an AI recommendation

## Case Replay Fragment

### Ugly Case

- **Operator involved**: cross-border order-operations specialist
- **Decision point**: whether an order should be rerouted, paused for clarification, or returned to the marketplace queue
- **Action taken**: operator compares a fictional marketplace message, SKU mapping, inventory sheet, and fulfillment update
- **Evidence available at the time**: synthetic order record, synthetic SKU table, synthetic inventory status, and synthetic partner message
- **Outcome**: the fictional case is held for human clarification because two source records disagree
- **What this case proves**: a bounded example can test evidence consolidation, uncertainty handling, and owned task routing
- **What this case does not prove**: any real customer weakness, real marketplace behavior, or production performance

## Eval Pack Fragment

- **Evaluation objective**: verify that exception recommendations cite the correct source records and route eligible tasks without hiding unresolved conflicts
- **Golden cases**: clear SKU mismatch, clear address-format mismatch, confirmed inventory discrepancy
- **Failure cases**: stale inventory sheet, duplicated marketplace message, missing order identifier
- **Edge cases**: bundled products, split fulfillment, translated marketplace messages
- **Ambiguous cases**: two valid SKU mappings, conflicting inventory timestamps, incomplete partner update
- **Acceptance threshold**: reviewer accepts or lightly edits the recommendation on at least 80 percent of in-scope synthetic cases, with zero unsupported write-backs
- **Demo-killing cases**: invented evidence, silent conflict resolution, or routing a task to the wrong owner
- **Review owner**: fictional cross-border operations supervisor

## Governance And Risk Overlay Fragment

- **AI authority level**: advisory with gated task creation
- **Advisory surfaces**: evidence consolidation, exception classification, recommended next action, message draft
- **Gated action surfaces**: task creation and customer-facing message after operator confirmation
- **Write-capable surfaces**: structured task stored only after human confirmation
- **Human confirmation points**: exception type, cited evidence, owner, next action, and customer-facing message
- **Audit trail**: source records, draft recommendation, operator decision, task assignment, and closure evidence
- **Rollback condition**: use the Minimum Viable Loop rollback condition
- **Risk owner**: fictional cross-border operations lead
- **Known unacceptable failure modes**: invented evidence, unconfirmed customer messages, unsupported inventory changes, or unowned exception tasks

## Day-2 Operations Fragment

- **Operating owner**: fictional cross-border operations lead
- **Exception owner**: fictional marketplace operations supervisor
- **Monitoring signals**: recommendation acceptance rate, override rate, routing accuracy, resolution time, and missing-evidence count
- **Drift or degradation signal**: use the Minimum Viable Loop drift or degradation signal
- **Manual fallback mode**: use the Minimum Viable Loop fallback mode
- **Review cadence**: weekly review of synthetic pilot cases
- **Operator adoption signal**: use the Minimum Viable Loop operator adoption signal
- **Asset promotion candidate**: reusable synthetic order-exception eval starter pack
