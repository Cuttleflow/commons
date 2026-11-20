---
id: chl.end.e05
type: endorsement
heading: E05 Scuba Diving
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.chl.operations.scuba
  rules:
  - when: qs.chl.operations.scuba == true
    action: refer
  reason: Applies because passengers scuba dive from the vessel.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Decline risk
---

[[ref:chl.excl.pi-water-activities]] does not apply to passengers scuba diving from the vessel, where:

- every dive is run under the supervision of a person who holds a current instructor or dive supervisor qualification from a recognised training organisation;
- you follow the code of practice for recreational diving and snorkelling that applies in the state or territory where the dive takes place;
- every diver completes a medical declaration before diving, and you keep it with the dive log for each dive; and
- emergency oxygen and first aid equipment are on board and crew trained to use them.

The special excess shown in the schedule applies to each claim for a diver. [[ref:chl.cond.insurance-contracts-act]] applies to these conditions.

Schedule variables: special excess (default $10,000).
