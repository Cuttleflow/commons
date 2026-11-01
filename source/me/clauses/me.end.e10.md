---
id: me.end.e10
type: endorsement
heading: E10 Contractual Liability Buy-back
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.me.ops.contractual_liability
  rules:
  - when: qs.me.ops.contractual_liability == yes
    action: refer
  reason: Referred because you asked us to cover liability assumed under named contracts.
---

[[ref:me.excl.contractual-liability]] does not apply to liability assumed under the specific contracts listed in the schedule, to the extent stated there.

Schedule variables: contracts; extent.
