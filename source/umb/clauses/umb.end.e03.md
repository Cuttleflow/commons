---
id: umb.end.e03
type: endorsement
heading: E03 Excess Only Basis
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.umb.cover.excess_only_requested
  rules:
  - when: qs.umb.cover.excess_only_requested == true
    action: broker_option
  reason: Offered because you asked for excess cover only, without the umbrella cover or the aggregate drop-down.
---

[[ref:umb.cover.coverage-b]] does not apply. The paragraph of [[ref:umb.cover.retained-limit-and-exhaustion]] about the reduction or exhaustion of an aggregate underlying limit does not apply, and this policy responds only once the full underlying limits have been paid. The self-insured retention is not used.

Schedule variables: none.
