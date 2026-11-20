---
id: trv.inb.end.e18
type: endorsement
heading: E18 Extension of Stay
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.trv.inb.extension
  rules:
  - when: qs.trv.inb.extension == yes
    action: apply
  reason: Applied because the visitor asked to extend the stay.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

If you ask us before the end date shown in the schedule, and we agree in writing, the trip is extended to the new end date we confirm, up to a total of 365 days, for the additional premium we tell you. An injury or sickness that first shows itself before the extension starts is a pre-existing condition for the extended period unless we accept it.

Schedule variables: new end date; additional premium.
