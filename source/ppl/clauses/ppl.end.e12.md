---
id: ppl.end.e12
type: endorsement
heading: E12 Named Principals
since: 2.0.0
status: draft
trigger:
  questions:
  - qs.ppl.contracts.named_principals
  rules:
  - when: count(qs.ppl.contracts.named_principals) > 0
    action: apply
  reason: Applies because your contract with {qs.ppl.contracts.named_principals} requires them to be covered.
  responses:
  - Attach
  - Do not attach
---

Each principal shown in the schedule for this endorsement is an insured, but only for its liability arising from the business carried on for that principal under the contract shown, and only to the extent the contract requires you to insure it. [[ref:ppl.ext.cross-liabilities]] applies between you and the principal. If the contract requires, we will give the principal 30 days' written notice before we cancel this policy.

Schedule variables: principals and contract references; notice of cancellation (yes or no).
