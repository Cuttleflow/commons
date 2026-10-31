---
id: ml.end.e11
type: endorsement
heading: E11 Aggregate Limit Reinstatement
since: 1.4.0
status: draft
trigger:
  questions:
  - qs.ml.cover.options_requested
  rules:
  - when: '''E11'' in qs.ml.cover.options_requested'
    action: broker_option
  reason: Offered because you asked for the aggregate limit to be reinstated after a large claim.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

When the overall aggregate limit of liability under [[ref:ml.pay.overall-aggregate]] has been exhausted by payment, it is reinstated once, by the reinstatement amount shown in the schedule for this endorsement, for the rest of the policy period.

The reinstated amount:

- does not apply to any claim or Crime Loss that, or any related claim or Crime Loss that, has already caused payment under the original aggregate;
- is the most we will pay for all other claims and Crime Losses during the rest of the policy period, and each section limit of liability within it is as shown in the schedule for this endorsement; and
- does not apply to the Crime section unless the schedule for this endorsement says so.

Schedule variables: reinstatement amount; section limits within it; whether the Crime section is included.
