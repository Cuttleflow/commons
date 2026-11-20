---
id: isr.end.cois
type: endorsement
heading: COIS Co-insurance by Situation
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.policy.base_wording
  rules:
  - when: qs.isr.policy.base_wording != 'meridian'
    action: apply
  reason: Applies because the base wording's co-insurance clause differs from the per-Situation test.
---

This endorsement replaces the co-insurance (average or underinsurance) provisions of the Base Wording for the Material Damage cover.

- The test is made separately for the Situation where the Damage happens, at the time of the Damage.
- If the Declared Value of the property at that Situation is at least the co-insurance percentage shown in the Schedule of its value at risk, we pay the loss in full, subject to the Deductible and limits.
- If it is less, we pay this proportion of the loss: Declared Value ÷ (co-insurance percentage × value at risk). We then deduct the Deductible.
- The test does not apply where the loss at that Situation, before the Deductible, is less than the minor-loss percentage shown in the Schedule of the Declared Value for that Situation.
- **Value at risk** means the cost, at the time of the Damage, of reinstating all the insured property at that Situation on the basis of settlement that applies to it.
- The Business Interruption cover keeps its own co-insurance provision in the Base Wording, unless the Schedule says otherwise.

**Worked example.** Value at risk at the Situation is $10,000,000 and the co-insurance percentage is 85%, so the threshold is $8,500,000. The Declared Value is $7,000,000 and the loss is $1,000,000. We pay 7,000,000 ÷ 8,500,000 = 82.35% of the loss, which is $823,529, less the Deductible. Had the loss been $600,000, which is under 10% of the $7,000,000 Declared Value, we would pay it in full less the Deductible.

Schedule variables: co-insurance percentage (default 85%); minor-loss percentage (default 10%).
