---
id: isr.end.lols
type: endorsement
heading: 'LOLS Limit of Liability: Any One Loss, Any One Situation'
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.policy.base_wording
  rules:
  - when: qs.isr.policy.base_wording != 'meridian'
    action: apply
  reason: Applies because the policy is written on a base wording other than the Meridian wording, which has this provision built in.
---

The most we pay for all Damage and all Business Interruption loss arising from one Event at one Situation is the Limit of Liability shown in the Schedule. The Schedule states whether this limit is combined for the Material Damage and Business Interruption covers or separate for each.

- Where one Event causes Damage at more than one Situation, the Limit of Liability applies separately at each Situation, unless the Schedule shows a limit for any one Event across all Situations. If it does, that limit is the most we pay for the Event.
- The Limit of Liability includes every additional benefit, extension and sub-limit, unless the Schedule says a particular amount is paid in addition.
- Declared Values are used to test the adequacy of values and to calculate premium. They do not increase the Limit of Liability.

Schedule variables: Limit of Liability (combined, or for each cover); any one Event limit across Situations (optional); amounts payable in addition.
