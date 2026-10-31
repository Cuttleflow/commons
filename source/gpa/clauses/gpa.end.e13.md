---
id: gpa.end.e13
type: endorsement
heading: E13 Lloyd's Underwriters
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.gpa.issuer.lloyds
  rules:
  - when: qs.gpa.issuer.lloyds == yes
    action: apply
  reason: Applied because the policy is issued under a Lloyd's binding authority.
  responses:
  - Attach
---

This policy is underwritten by the Lloyd's underwriters named in the schedule. Each underwriter is liable only for its own share, and not for the share of any other underwriter.

The underwriters agree that any dispute about this policy may be heard by a court of competent jurisdiction in Australia, and that the Lloyd's General Representative in Australia named in the schedule may accept service of process for them. Complaints may also be made to Lloyd's Australia at the details shown in the schedule, as well as under [[ref:gpa.cond.disputes-and-complaints]].

Schedule variables: underwriters and their shares; Lloyd's General Representative; Lloyd's complaints contact.
