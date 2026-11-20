---
id: ccl.end.e03
type: endorsement
heading: E03 Household Removals
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.ccl.operations.household_removals
  rules:
  - when: qs.ccl.operations.household_removals == true
    action: refer
  reason: Applies because you carry household removals.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Decline risk
---

Household furniture and personal effects carried in a household removal are not excluded goods. We pay for them at their market value at the time of the loss, not at replacement cost, up to the limit any one vehicle, and up to the amount shown in the schedule for any one article. We do not pay for scratching, denting, chipping or breakage of fragile articles unless an event listed in [[ref:ccl.cover.basic-load|heading]] causes it, or the articles were packed by you.

Schedule variables: limit for any one article (default $5,000).
