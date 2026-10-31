---
id: pi.vt.end.live-export
type: endorsement
heading: Live Export Certification Exclusion
profession: veterinary
since: 1.0.0
status: draft
note: Live export certification is excluded from the definition of professional services. This endorsement records the exclusion where the insured does this work, and the underwriter may instead add it
  to the schedule as a professional service.
trigger:
  questions:
  - qs.pi.vt.live_export
  rules:
  - when: qs.pi.vt.live_export = yes
    action: refer
  reason: Applies because you certify animals for live export.
---

We do not cover any claim, loss or liability arising from inspecting or certifying animals for export, including as an accredited veterinarian under export control law, or from accompanying animals on an export voyage.
