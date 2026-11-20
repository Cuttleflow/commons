---
id: isr.end.arei
type: endorsement
heading: AREI Automatic Reinstatement of Limits after Loss
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.policy.situation_count
  rules:
  - when: qs.isr.policy.situation_count >= 1
    action: apply
  reason: Applies to every policy so that limits are restored after a claim.
---

After we pay a claim, the Limit of Liability and any sub-limit reduced by the payment are restored to their full amount from the date of the Damage. If the Schedule shows a reinstatement premium basis, we charge premium on the amount restored, pro rata for the unexpired Period of Insurance at the agreed rate. Reinstatement does not apply to an aggregate limit (AGGP) or to any limit the Schedule marks as not reinstated. The most we pay for any one Event remains the Limit of Liability.

Schedule variables: reinstatement premium (yes or no); limits not reinstated.
