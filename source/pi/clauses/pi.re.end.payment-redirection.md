---
id: pi.re.end.payment-redirection
type: endorsement
heading: Payment Redirection
profession: real-estate-strata
since: 1.0.0
changed: 1.1.0
status: draft
note: Adds cover. Whether this cover belongs in PI or in cyber cover is an open question for the capacity provider.
trigger:
  questions:
  - qs.pi.re.trust_money
  - qs.pi.re.callback_verification
  rules:
  - when: qs.pi.re.trust_money = yes and qs.pi.re.callback_verification = yes
    action: broker_option
  reason: Offered because you hold client money in trust.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Do not attach
---

Despite [[ref:pi.excl.cyber-event]], we will pay:

(a) your liability to a client or other party; and

(b) your direct loss of money held in trust,

where money you hold or control is paid to a third party because of a fraudulent instruction that appears to come from a client, a party to a transaction, or a supplier.

In assessing a claim under this endorsement, we consider whether, before making the payment, you confirmed any new or changed payment details by calling the person who appeared to give the instruction on a telephone number that you already held and did not obtain from the instruction. This is a factor in our assessment. It is not a condition of cover. If you did not confirm the details, we may reduce what we pay only by the amount that fairly represents the extent to which that failure caused or contributed to the loss. We will not refuse a claim only because you did not confirm the details.

The most we will pay for all losses under this endorsement in the policy period is the sub-limit shown in the schedule for this endorsement, which is part of the limit of liability.
