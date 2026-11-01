---
id: do.end.e09
type: endorsement
heading: E09 Excess Layer
since: 1.3.0
changed: 1.4.0
status: draft
trigger:
  questions:
  - qs.do.cover.layer
  rules:
  - when: "qs.do.cover.layer == 'excess'"
    action: apply
  reason: Applies because this policy is written in excess of other directors' and officers' insurance.
  responses:
  - Attach
  - Do not attach
---

It converts this entire policy into an excess layer above a specified primary D&O policy.

**Excess Function**

This policy sits excess of the primary D&O policy identified in the schedule and follows its form, subject to the terms of this policy where they differ. Where the two are inconsistent, this policy applies.

**Attachment**

This policy responds only after the limit of the primary D&O policy has been exhausted by payment of loss that the primary D&O policy covers. The attachment point is the limit of the primary D&O policy shown in the schedule. This policy is excess of that specified policy for the purposes of [[ref:do.pay.other-insurance]].

**No Drop-Down**

This policy does not drop down. If the primary D&O policy does not pay for any reason, including insolvency of its insurer or its refusal to pay, we respond only above the attachment point. An amount the primary insurer does not pay does not reduce the attachment point. Drop-down cover for Side A is available only under [[ref:do.end.e08]].

Schedule variables: Primary D&O policy and its limit; attachment point.
