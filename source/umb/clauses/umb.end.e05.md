---
id: umb.end.e05
type: endorsement
heading: E05 Employers' Liability Underlying
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.umb.underlying.el_states
  rules:
  - when: qs.umb.underlying.el_states == true
    action: suggest
  reason: Suggested because you have employees in a state or territory where workers compensation, including common law liability, is insured privately.
---

The employers' liability or workers compensation common law insurance shown in the schedule for this endorsement is underlying insurance. The second point of [[ref:umb.excl.workers-compensation-and-employers-liability]] does not apply to liability that insurance covers, and [[ref:umb.cover.coverage-a]] applies above it. The first point of that exclusion still applies: this policy never pays a statutory workers compensation benefit.

Schedule variables: the states or territories; the underlying employers' liability insurer and limit.
