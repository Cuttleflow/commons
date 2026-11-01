---
id: xol.end.e09
type: endorsement
heading: E09 Drop-down for Underlying Insurer Insolvency
since: 2.0.0
status: draft
trigger:
  questions:
  - qs.xol.endorsements.dropdown_insolvency_requested
  - qs.xol.underlying.insurers_apra_authorised
  rules:
  - when: qs.xol.endorsements.dropdown_insolvency_requested == true
    action: refer
  reason: Referred because you asked for this layer to replace an underlying insurer that becomes insolvent.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

Where an underlying insurer named in the schedule for this endorsement becomes subject to an insolvency event during the policy period and, solely because of that event, does not pay loss that its policy covers, we will treat its unpaid share of its underlying limit as paid for the purpose of [[ref:xol.cover.attachment-and-exhaustion]], and pay that loss as if this policy attached at that point, up to the drop-down sub-limit shown in the schedule, which is part of and not in addition to the limit of liability.

An insolvency event means the appointment of a liquidator, provisional liquidator, administrator, judicial manager or receiver to the underlying insurer, or the underlying insurer becoming unable to pay its debts as they fall due, or the equivalent under the law of its place of incorporation.

Once we pay, we are subrogated to your rights against the underlying insurer and its estate, including under the Financial Claims Scheme, to the extent of our payment.

Schedule variables: the underlying insurers to which it applies; the drop-down sub-limit.
