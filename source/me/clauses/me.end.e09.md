---
id: me.end.e09
type: endorsement
heading: E09 Additional Facilities
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.me.ops.additional_facilities
  rules:
  - when: qs.me.ops.additional_facilities == yes
    action: apply
  reason: Applies because you named facilities to add from a later date.
---

The facilities named in the schedule are added as facilities from the date shown, outside the automatic cover in [[ref:me.ext.new-subsidiaries-and-facilities]].

Schedule variables: facilities and dates.
