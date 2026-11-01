---
id: car.end.e09
type: endorsement
heading: E09 Principal-Arranged Insurance
since: 2.1.0
status: draft
trigger:
  questions:
  - qs.car.risk.principal_arranged_insurance
  rules:
  - when: qs.car.risk.principal_arranged_insurance == yes
    action: broker_option
  reason: Offered because the principal has arranged its own insurance for the project.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

Where the principal has arranged its own contract works or liability insurance for the project, this policy covers the insured contractors for the difference between that insurance and this policy:

- for any excess under the principal's policy that the construction contract makes the contractor bear, up to the amount shown in the schedule; and
- for damage or liability the principal's policy does not cover and this policy would.

This policy does not contribute with the principal's policy for loss it covers.

Schedule variables: principal's insurer and policy number; contractor's excess buy-down amount.
