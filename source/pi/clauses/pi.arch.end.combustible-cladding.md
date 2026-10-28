---
id: pi.arch.end.combustible-cladding
type: endorsement
heading: Combustible Cladding Exclusion
profession: architects-engineers
since: 1.0.0
status: draft
note: New optional endorsement on underwriter direction 29 October 2026. Draft text for counsel; terms to be aligned with the Victorian Ministerial Orders and current market wordings.
trigger:
  questions: [pi.q.cladding-work, pi.q.practice-states, pi.q.registrations]
  rules:
    - when: pi.q.cladding-work = yes
      action: apply
  restrictions:
    - when: "'VIC' in pi.q.practice-states and pi.q.registrations includes endorsed building engineer (Victoria)"
      action: refer
      note: The Victorian Ministerial Order for endorsed building engineers may not permit this exclusion. An underwriter must confirm before it is applied.
  reason: Applies because you design, specify, certify or inspect external wall cladding, or advise on it.
---

We do not cover any claim, loss or liability arising from the use, or proposed use, in a building of external wall cladding that is combustible or that does not comply with the National Construction Code, including aluminium composite panels with a polyethylene core and expanded polystyrene products. This applies to any design, specification, selection, certification, inspection or approval of that cladding, and to any advice about it.
