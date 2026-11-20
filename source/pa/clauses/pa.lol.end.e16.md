---
id: pa.lol.end.e16
type: endorsement
heading: E16 Foreign Licence Trigger
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pa.lol.foreign_licence
  rules:
  - when: qs.pa.lol.foreign_licence == yes
    action: refer
  reason: Referred because the pilot flies on a licence issued outside Australia.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

A decision by the aviation authority named in the schedule about the medical certificate you hold from it, of the same kind as a CASA decision about a Class 1 medical certificate, is treated as a CASA decision under this policy, for the licence shown.

Schedule variables: aviation authority; licence.
