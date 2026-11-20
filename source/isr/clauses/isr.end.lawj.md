---
id: isr.end.lawj
type: endorsement
heading: LAWJ Governing Law and Jurisdiction
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.policy.base_wording
  rules:
  - when: qs.isr.policy.base_wording != 'meridian'
    action: apply
  reason: Applies because the base wording ties governing law to something that can change.
---

This Policy is governed by the law of the State or Territory shown in the Schedule or, if none is shown, the State or Territory in which the Insured named first had its registered office at the start of the Period of Insurance. The courts of that State or Territory, and the Federal Court of Australia, have non-exclusive jurisdiction. This does not limit your right to complain to the Australian Financial Complaints Authority.

Schedule variables: governing law State or Territory.
