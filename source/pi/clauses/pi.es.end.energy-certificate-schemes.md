---
id: pi.es.end.energy-certificate-schemes
type: endorsement
heading: Energy Certificate Schemes Exclusion
profession: building-energy-sustainability
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pi.es.certificate_schemes_pct
  rules:
  - when: qs.pi.es.certificate_schemes_pct > 25
    action: refer
  reason: Applies because {qs.pi.es.certificate_schemes_pct}% of your fees come from creating energy saving certificates.
---

We do not cover any claim, loss or liability arising from the creation, registration or surrender of certificates under an energy efficiency or renewable energy certificate scheme, including the NSW Energy Savings Scheme and the Victorian Energy Upgrades program.
