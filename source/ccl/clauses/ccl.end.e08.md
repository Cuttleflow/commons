---
id: ccl.end.e08
type: endorsement
heading: E08 Terms of Carriage Not Approved
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.ccl.cover.legal_liability
  - qs.ccl.operations.trading_conditions_approved
  rules:
  - when: qs.ccl.cover.legal_liability == true and qs.ccl.operations.trading_conditions_approved == false
    action: refer
  reason: Applies because you chose legal liability cover and your terms of carriage are not yet approved.
  responses:
  - Attach
  - Do not attach
  - Decline risk
---

Your terms of carriage are not approved terms. Under [[ref:ccl.section.legal-liability|heading]] we pay only the liability you would have had under the terms of carriage we name in the schedule for this endorsement, or, if none are named, under the common law as a private carrier who is not a common carrier, up to the limit for that section.

Schedule variables: the terms of carriage that measure cover.
