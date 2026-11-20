---
id: chl.end.e15
type: endorsement
heading: E15 Hire and Drive Vessels
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.chl.vessel.use_category
  rules:
  - when: qs.chl.vessel.use_category == 4
    action: refer
  reason: Applies because the vessel is a Class 4 hire and drive vessel.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Decline risk
---

Where the vessel is hired without crew to a person who operates it for their own recreation, under a written hire agreement:

- before each hire, you must check that the hirer holds any licence the law requires, give the hirer the briefing and demonstration the vessel's safety management system requires, record the hirer's name and contact details, and tell the hirer the area within the operational area where the vessel may go; and
- the hirer excess shown in the schedule applies to each claim arising during a hire.

[[ref:chl.section.pi|heading]] insures your liability, not the hirer's. We will not seek recovery from a hirer except for loss caused by the hirer's deliberate or reckless act, or while the hirer was under the influence of alcohol or drugs. [[ref:chl.cond.insurance-contracts-act]] applies to these conditions.

Schedule variables: hirer excess (default $2,500).
