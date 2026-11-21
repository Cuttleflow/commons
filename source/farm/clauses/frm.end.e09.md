---
id: frm.end.e09
type: endorsement
heading: E09 Interested Party
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.frm.insured.has_financier
  rules:
  - when: qs.frm.insured.has_financier == yes
    action: apply
  reason: Applies because a financier has an interest in insured property.
  responses:
  - Attach
  - Do not attach
---

The interested party shown for this endorsement, such as a financier of farm machinery or a lender with a mortgage over the farm location, has an interest in the property shown with its name. We pay a claim for that property to you and the interested party as their interests appear, or as you and they direct in writing. An act or omission of yours does not reduce what we pay the interested party for its interest, unless the interested party knew of it and did not tell us.

Schedule variables: interested party; the property in which it has an interest.
