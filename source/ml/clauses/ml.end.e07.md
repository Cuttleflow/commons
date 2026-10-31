---
id: ml.end.e07
type: endorsement
heading: E07 Social Engineering Fraud
since: 1.4.0
status: draft
trigger:
  questions:
  - qs.ml.crime.social_engineering_requested
  - qs.ml.crime.payment_verification
  rules:
  - when: qs.ml.crime.social_engineering_requested == yes and qs.ml.crime.payment_verification == no
    action: refer
  - when: qs.ml.crime.social_engineering_requested == yes
    action: broker_option
  reason: Offered because you asked for cover for payments made after a fraudulent instruction; referred where new or changed payment details are not verified independently.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Do not attach
---

The Crime section is extended to cover the company's direct financial loss of money or securities transferred, paid or delivered by an employee in good faith, during the policy period, in reliance on an instruction that:

- purports to come from a director, officer, employee, customer, supplier or other person with whom the company has an established business relationship; and
- was in fact sent by a person who impersonated that person, without the knowledge or consent of the company or of the person impersonated.

Cover under this endorsement is not conditional on the company having followed any verification procedure. Where the company has not followed the verification procedure shown in the schedule for this endorsement, and that failure caused or contributed to the loss, we may reduce our payment to the extent the failure caused or contributed to it, as s.54 of the Insurance Contracts Act 1984 (Cth) allows.

The most we will pay under this endorsement during the policy period is the social engineering sub-limit shown in the schedule, which is part of the Crime section limit of liability. The social engineering excess shown in the schedule applies to each loss. All losses arising from one impersonation, or from a series of related impersonations by the same person or group, are one loss.

This endorsement does not cover loss of cryptocurrency or other digital assets, or loss covered by any cyber insurance policy. For this endorsement, [[ref:ml.def.dishonest-act]] and [[ref:ml.cover.employee-dishonesty]] do not require a dishonest act by an employee.

Schedule variables: social engineering sub-limit; social engineering excess; verification procedure.
