---
id: pi.re.end.livestock-sales
type: endorsement
heading: Livestock Sales Injury and Damage Exclusion
profession: real-estate-strata
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pi.re.livestock_sales
  - qs.pi.practice_states
  rules:
  - when: qs.pi.re.livestock_sales = yes
    action: apply
  restrictions:
  - when: '''NSW'' in qs.pi.practice_states'
    action: refer
    note: The NSW regulation treats civil liability as including personal injury. An underwriter must confirm that a stock and station agent licensed in NSW may accept this exclusion.
  reason: Applies because you conduct livestock sales.
---

Despite the exception in [[ref:pi.excl.bodily-injury-and-property-damage]], we do not cover any claim for death, bodily injury or property damage caused by livestock at a sale, yard or property where you are conducting or preparing for a sale. This exposure is designed to be covered under a public liability policy.
