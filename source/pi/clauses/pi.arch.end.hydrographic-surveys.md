---
id: pi.arch.end.hydrographic-surveys
type: endorsement
heading: Hydrographic Surveys Exclusion
profession: architects-engineers
since: 1.1.0
status: draft
note: Replaces the hydrographic survey exclusion in MERIDIAN-PI-SURV-v1.0.0, which applied to every surveyor.
trigger:
  questions: [qs.pi.ae.hydrographic_pct]
  rules:
    - when: qs.pi.ae.hydrographic_pct > 0
      action: refer
  reason: Applies because {qs.pi.ae.hydrographic_pct}% of your fees come from hydrographic surveys.
---

We do not cover any claim, loss or liability arising from a hydrographic survey, or any survey of the bed of the sea, a harbour, a river or another body of water.
