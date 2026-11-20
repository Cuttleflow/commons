---
id: isr.pay.co-insurance
type: payment
heading: Co-insurance
since: 1.1.0
status: draft
---

We test whether the Declared Values are adequate separately for the Situation where the Damage happens, at the time of the Damage.

- If the Declared Value of the Insured Property at that Situation is at least the co-insurance percentage shown in the schedule (85% if none is shown) of its Value at Risk, we pay the loss in full, subject to the Deductible and limits.
- If it is less, we pay this proportion of the loss: Declared Value divided by (co-insurance percentage multiplied by Value at Risk). We then deduct the Deductible.
- The test does not apply where the loss at that Situation, before the Deductible, is less than the minor-loss percentage shown in the schedule (10% if none is shown) of the Declared Value for that Situation.
- The test does not apply to Money, or to any amount the schedule shows as a first-loss amount.
- [[ref:isr.pay.bi-loss]] contains its own test for [[ref:isr.section.business-interruption]].

**Worked example.** The Value at Risk at the Situation is $10,000,000 and the co-insurance percentage is 85%, so the threshold is $8,500,000. The Declared Value is $7,000,000 and the loss is $1,000,000. We pay 7,000,000 divided by 8,500,000, which is 82.35% of the loss, or $823,529, less the Deductible. Had the loss been $600,000, which is under 10% of the $7,000,000 Declared Value, we would pay it in full less the Deductible.
