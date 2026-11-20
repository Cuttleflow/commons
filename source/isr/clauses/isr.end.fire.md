---
id: isr.end.fire
type: endorsement
heading: FIRE Fire Protection Impairment
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.risk.sprinkler_credit
  rules:
  - when: qs.isr.risk.sprinkler_credit == yes
    action: apply
  reason: Applies because the premium includes a credit for sprinklers or fire detection.
---

Where the Schedule shows that a Situation is protected by automatic sprinklers, fire detection and alarm, or another fire protection system:

- keep the system in working order, and have it inspected, tested and maintained as Australian Standard AS 1851 (or the standard shown in the Schedule) requires;
- tell us before any planned shutdown longer than the period shown, and as soon as practicable after any unplanned impairment longer than that period; and
- take the reasonable precautions we ask for while the system is impaired.

Schedule variables: protected Situations and systems; maintenance standard (default AS 1851); notification period (default 24 hours).
