---
id: pi.vt.end.reproductive-services
type: endorsement
heading: Reproductive Services
profession: veterinary
since: 1.0.0
status: draft
note: Adds cover.
trigger:
  questions:
  - qs.pi.vt.reproductive_pct
  rules:
  - when: qs.pi.vt.reproductive_pct > 0
    action: broker_option
  reason: Offered because you provide reproductive services.
---

Artificial breeding and reproductive services, including artificial insemination, embryo transfer, semen collection and pregnancy diagnosis, are professional services under this policy.

This endorsement does not cover genetic modification or gene therapy, or a claim that an animal failed to conceive or produce offspring of a particular quality, unless the failure was caused by your negligence.
