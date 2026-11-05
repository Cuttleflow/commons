---
id: pcl.end.e03
type: endorsement
heading: E03 Jewellery Kept in a Safe
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pcl.premises.security
  rules:
  - when: qs.pcl.premises.security == alarm_and_safe
    action: apply
  reason: Applies because the premium allows for jewellery being kept in a safe.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Do not attach
---

The premium is based on jewellery and watches being kept in a safe at the premises. While any item of jewellery and watches with a value equal to or more than the amount shown in the schedule for this endorsement is at the premises and is not being worn, keep it locked in the safe.

If you do not, and the item is stolen, [[ref:pcl.cond.insurance-contracts-act]] applies: we may reduce the claim only by the amount that fairly represents the extent to which our interests were prejudiced.

Schedule variables: item value (default $10,000).
