---
id: ml.end.e03
type: endorsement
heading: E03 USA and Canada Jurisdiction
since: 1.4.0
status: draft
trigger:
  questions:
  - qs.ml.exposure.us_subsidiary
  - qs.ml.exposure.us_revenue_pct
  rules:
  - when: qs.ml.exposure.us_subsidiary == yes or qs.ml.exposure.us_revenue_pct >= 10
    action: refer
  - when: qs.ml.exposure.us_revenue_pct > 0
    action: suggest
  reason: Applies because the company has a subsidiary in, or earns {qs.ml.exposure.us_revenue_pct}% of its revenue from, the United States or Canada.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

[[ref:ml.excl.usa-canada]] does not apply to the sections shown in the schedule for this endorsement, for claims arising from the operations, subsidiaries or exposures named in the schedule.

For a claim brought or maintained in a court in the United States of America or Canada, or a claim to enforce a judgment of such a court:

- the most we will pay, including defence costs, is the USA and Canada sub-limit shown in the schedule, which is part of the section limit of liability and the overall aggregate;
- defence costs are within the limit of liability, whatever [[ref:ml.end.e02]] provides;
- the USA and Canada excess shown in the schedule applies in place of the section excess; and
- we do not pay punitive, exemplary or multiple damages, or any fine or penalty, whatever the law of the place where the claim is brought.

The Employment Practices Liability section does not respond to a claim brought by an employee employed in the United States of America or Canada unless the schedule for this endorsement names that section and that employer.

Schedule variables: sections; operations, subsidiaries or exposures; USA and Canada sub-limit; USA and Canada excess.
