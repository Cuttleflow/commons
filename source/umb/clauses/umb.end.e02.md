---
id: umb.end.e02
type: endorsement
heading: E02 Principals and Others
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.umb.contracts.principal_insured_required
  rules:
  - when: qs.umb.contracts.principal_insured_required == true
    action: broker_option
  reason: Offered because a contract requires you to include a principal or another party as an insured under this policy.
---

The persons or entities named in the schedule for this endorsement are insureds under both coverages, but only for liability arising from the business, only to the extent a written contract entered into before the occurrence requires you to insure them, and never for a higher limit than the contract requires.

[[ref:umb.excl.contractual-liability]] does not apply to liability you assumed under that contract to indemnify the named persons or entities for personal injury or property damage caused by your negligence.

Schedule variables: the named principals or other parties; the contracts.
