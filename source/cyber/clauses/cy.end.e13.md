---
id: cy.end.e13
type: endorsement
heading: E13 Non-IT Dependent Business Interruption
since: 1.4.0
status: draft
trigger:
  questions:
  - qs.cy.cover.options_requested
  rules:
  - when: '''E13'' in qs.cy.cover.options_requested'
    action: broker_option
  reason: Offered because you asked for cover for outages at suppliers you depend on.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

[[ref:cy.ext.dependent-business-interruption]] extends to interruption of your business resulting from a cyber event affecting the computer systems of a supplier named in the schedule for this endorsement, even though that supplier is not a service provider. For this endorsement, a cyber event at a named supplier is treated as a dependent event.

The waiting period shown for this endorsement applies on a threshold basis: once the interruption exceeds it, we pay net income loss and extra expense measured from the start of the interruption.

This endorsement does not cover interruption arising from physical damage to the supplier's premises or plant, insolvency of the supplier, industrial action, or the supplier's commercial decision to stop supplying.

Schedule variables: named suppliers; sub-limit; waiting period.
