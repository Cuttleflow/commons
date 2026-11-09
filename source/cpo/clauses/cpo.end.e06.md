---
id: cpo.end.e06
type: endorsement
heading: E06 Vacant Tenancies
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.cpo.occupancy.vacant_pct
  rules:
  - when: qs.cpo.occupancy.vacant_pct > 50
    action: refer
  - when: qs.cpo.occupancy.vacant_pct > 0
    action: apply
  reason: "{qs.cpo.occupancy.vacant_pct}% of the floor area is vacant."
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
---

Cover continues for the vacant tenancies shown in the schedule for this endorsement, and [[ref:cpo.excl.unoccupied-building]] does not apply while you meet these conditions:

- the vacant tenancies are locked and secured, and all services not needed for fire protection or security are turned off;
- you, your property manager or a person acting for you inspects them inside and out at least every 14 days, and keeps a record;
- rubbish and combustible material are removed from them.

If you can show that a breach of a condition did not cause or contribute to the damage, we pay the claim as if the condition had been met. Otherwise, [[ref:cpo.cond.insurance-contracts-act]] applies. The special excess shown applies to damage caused by malicious damage or the escape of liquid in a vacant tenancy.

Schedule variables: vacant tenancies and their share of the floor area; special excess (default: $2,500).
