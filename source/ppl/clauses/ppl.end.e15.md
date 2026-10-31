---
id: ppl.end.e15
type: endorsement
heading: E15 Hot Works Conditions
since: 2.0.0
status: draft
trigger:
  questions:
  - qs.ppl.ops.hot_works_offsite
  - qs.ppl.ops.hot_works_permit
  rules:
  - when: qs.ppl.ops.hot_works_offsite == yes and qs.ppl.ops.hot_works_permit == no
    action: refer
  - when: qs.ppl.ops.hot_works_offsite == yes
    action: apply
  reason: Applies because you do hot works away from your premises; permit and fire watch conditions apply.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Decline risk
---

This endorsement applies to welding, cutting, grinding, brazing, soldering, the use of open flame or any other process producing sparks or heat (hot works) that you carry out away from your premises.

When you carry out hot works away from your premises, you must:

- use a hot works permit system that identifies and removes or protects combustible materials within 11 metres of the work;
- keep a suitable fire extinguisher at the work location; and
- keep a person on fire watch during the work and for at least 30 minutes after it ends.

If you do not, we may reduce our liability for an occurrence arising from the hot works to the extent that the failure caused or contributed to the loss, as s.54 of the Insurance Contracts Act 1984 (Cth) allows. The special excess shown for this endorsement applies to each occurrence arising from hot works away from your premises.

Schedule variables: special excess.
