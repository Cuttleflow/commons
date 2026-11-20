---
id: chl.end.e14
type: endorsement
heading: E14 Fishing Vessels
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.chl.vessel.use_category
  rules:
  - when: qs.chl.vessel.use_category == 3
    action: apply
  reason: Applies because the vessel is a Class 3 fishing vessel.
---

For a Class 3 vessel:

- nets, pots, lines, trawl boards and other fishing gear are part of the vessel while on board, up to the amount shown in the schedule;
- we do not pay for loss of or damage to fishing gear while it is in the water, or being set or hauled, unless the vessel is also lost or damaged in the same accident;
- catch is not part of the vessel and is not insured; and
- [[ref:chl.section.pi|heading]] covers liability for damage to another person's fishing gear in the course of lawful fishing.

Schedule variables: fishing gear amount (default 10% of the agreed value).
