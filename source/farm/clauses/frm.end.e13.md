---
id: frm.end.e13
type: endorsement
heading: E13 Agistment of Other Owners' Livestock
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.frm.livestock.agistment_in
  rules:
  - when: qs.frm.livestock.agistment_in == yes
    action: apply
  reason: Applies because the farm business takes in other owners' livestock on agistment.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

Taking in livestock on agistment is part of the farm business. [[ref:frm.ls.exclusions]] does not exclude livestock you hold on agistment, and they are insured under [[ref:frm.section.livestock|heading]] for their owners' interest, within the livestock sum insured, where the agistment agreement makes you responsible for them.

[[ref:frm.li.care-custody-control]] applies to livestock on agistment up to the agistment sub-limit for one occurrence and the agistment sub-limit for any one animal, instead of its own sub-limits. You must have a written agistment agreement with each owner that states the number and kind of animals and who is responsible for them.

Schedule variables: agistment sub-limit for one occurrence (default: $100,000); agistment sub-limit for any one animal (default: $10,000).
