---
id: ccl.end.e01
type: endorsement
heading: E01 Livestock
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.ccl.operations.livestock
  rules:
  - when: qs.ccl.operations.livestock == true
    action: refer
  reason: Applies because you carry livestock.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Decline risk
---

Livestock is not excluded goods. Under [[ref:ccl.cover.basic-load|heading]] we pay for the death of an animal, or its injury that requires it to be destroyed for humane reasons, caused by an event listed in that clause, at the value shown in the schedule for each animal or, if none is shown, its market value at the destination.

We also pay the reasonable cost of agisting, mustering and recovering livestock after an insured event, up to the amount shown in the schedule for each animal and for each event.

We do not pay for death or injury from disease, suffocation, crushing or trampling that an insured event did not cause, or from overloading of the deck.

Schedule variables: value for each animal; agistment and mustering limit for each animal (default $2,000) and for each event (default $50,000).
