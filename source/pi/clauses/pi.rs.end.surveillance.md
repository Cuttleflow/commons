---
id: pi.rs.end.surveillance
type: endorsement
heading: Surveillance Exclusion
profession: risk-safety-claims
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pi.rs.surveillance_pct
  rules:
  - when: qs.pi.rs.surveillance_pct > 25
    action: refer
  - when: qs.pi.rs.surveillance_pct > 0
    action: suggest
  reason: Applies because {qs.pi.rs.surveillance_pct}% of your fees come from surveillance.
---

We do not cover any claim, loss or liability arising from covert surveillance of a person, including any claim for trespass, invasion of privacy or breach of a surveillance devices law.
