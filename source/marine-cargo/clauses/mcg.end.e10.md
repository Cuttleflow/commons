---
id: mcg.end.e10
type: endorsement
heading: E10 High-Risk Areas
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.mcg.ops.high_risk_destinations
  rules:
  - when: qs.mcg.ops.high_risk_destinations == yes
    action: refer
  reason: Referred because you send or receive goods to or from a high-risk or sanctioned area.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

The transits to or from the countries or areas shown in the schedule for this endorsement are insured on the terms and at the additional premium shown for them. Any other transit to or from an area listed as a war risk area by the Joint War Committee of the Lloyd's Market Association, or to or from a country subject to sanctions under the laws named in [[ref:mcg.cond.sanctions]], is insured only if you tell us before it starts and we agree.

This endorsement does not change [[ref:mcg.cond.sanctions]].

Schedule variables: countries or areas; terms and additional premium for each.
