---
id: ah.end.e12
type: endorsement
heading: E12 Second Reinstatement of the Limit
since: 1.3.0
status: draft
trigger:
  questions:
  - qs.ah.cover.second_reinstatement
  rules:
  - when: qs.ah.cover.second_reinstatement == yes
    action: broker_option
  reason: Offered because you asked for a second reinstatement of the limit.
---

In addition to [[ref:ah.pay.automatic-reinstatement]], the limit of liability for [[ref:ah.section.pi|heading]] is reinstated a second time, in full, for claims wholly unrelated to the claims that exhausted it and first made and notified later in the same policy period. The reinstated limit never applies to a claim that exhausted an earlier limit, or to any claim treated as one with it under [[ref:ah.cond.aggregation]], and sub-limits are not reinstated.

Schedule variables: none.
