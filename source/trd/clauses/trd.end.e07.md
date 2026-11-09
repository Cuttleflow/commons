---
id: trd.end.e07
type: endorsement
heading: E07 Plumbing and Gas Work Conditions
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.trd.business.trade
  - qs.trd.ops.gas_work
  rules:
  - when: qs.trd.business.trade == 3231
    action: refer
  - when: qs.trd.ops.gas_work == yes
    action: apply
  reason: Applies because you do plumbing or gas fitting work. A plumbing business is referred to an underwriter.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

When you carry out plumbing, drainage or gas fitting work:

- gas fitting must be done by a person licensed for it in the state or territory, and the compliance certificate the law requires must be issued for it;
- new or altered water and gas pipework must be pressure tested before it is concealed in a wall, floor or ceiling; and
- you must turn off and make safe the supply before you leave a site where work on it is not finished.

The special excess shown for this endorsement applies to each occurrence of property damage caused by water escaping from pipework or fittings you installed, altered or repaired. If you did not meet a condition in this endorsement, [[ref:trd.cond.insurance-contracts-act]] applies.

Schedule variables: special excess (default: $2,500).
