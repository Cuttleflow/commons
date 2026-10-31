---
id: trv.end.e13
type: endorsement
heading: E13 Wedding and Event Cancellation
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.trv.cover.wedding
  rules:
  - when: qs.trv.cover.wedding == yes
    action: broker_option
  reason: Offered as an option because the trip is to a wedding or event.
  responses:
  - Attach
  - Do not attach
---

The reasons in [[ref:trv.cover.cancellation]] include the cancellation of the wedding or event named in the schedule because the couple or the host dies, or becomes seriously ill or injured.

Schedule variables: wedding or event, and its date.
