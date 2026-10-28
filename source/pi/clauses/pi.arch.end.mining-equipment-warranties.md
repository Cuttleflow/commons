---
id: pi.arch.end.mining-equipment-warranties
type: endorsement
heading: Mining Equipment Warranties Exclusion
profession: architects-engineers
since: 1.0.0
status: draft
note: Limb (a) of "4.5 Assumed Duty" in MERIDIAN-PI-ARCH-v1.0.0, moved to an optional endorsement on underwriter direction 29 October 2026.
trigger:
  questions: [pi.q.fees.mining]
  rules:
    - when: pi.q.fees.mining > 10
      action: refer
    - when: pi.q.fees.mining > 0
      action: suggest
  reason: Applies because {pi.q.fees.mining}% of your fees come from services to the mining industry.
---

We do not cover any claim, loss or liability arising from any express or implied warranty or guarantee of the safety or performance of mining equipment.
