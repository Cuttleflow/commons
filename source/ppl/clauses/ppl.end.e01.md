---
id: ppl.end.e01
type: endorsement
heading: E01 Increased Tenants' Liability
since: 2.0.0
status: draft
trigger:
  questions:
  - qs.ppl.ops.tenant_liability_required
  rules:
  - when: qs.ppl.ops.tenant_liability_required > 2000000
    action: refer
  - when: qs.ppl.ops.tenant_liability_required > 500000
    action: broker_option
  reason: Offered because your lease requires {qs.ppl.ops.tenant_liability_required} cover for damage to the premises.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

The default sub-limit in [[ref:ppl.ext.tenants-liability]] is replaced by the sub-limit shown in the schedule for this endorsement.

Schedule variables: tenants' liability sub-limit (any one occurrence).
