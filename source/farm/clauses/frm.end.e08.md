---
id: frm.end.e08
type: endorsement
heading: E08 Stud and High-Value Animals
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.frm.livestock.max_animal_value
  rules:
  - when: qs.frm.livestock.max_animal_value > 20000
    action: refer
  reason: Referred because an animal is worth more than $20,000. The underwriter lists high-value animals at agreed values.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

The animals listed for this endorsement are insured at their agreed values instead of the valuation in [[ref:frm.ls.valuation]], for the causes covered by [[ref:frm.section.livestock|heading]] and, if the schedule shows it, [[ref:frm.section.livestock-extended|heading]]. Each animal's agreed value is the most we pay for it, and the total of the agreed values is part of the livestock sum insured.

Before we list an animal, we may ask for a veterinary certificate of its health, and for its registration, purchase or sale records. This endorsement does not insure loss of use, infertility or failure to conceive.

Schedule variables: listed animals, with their identification and agreed values.
