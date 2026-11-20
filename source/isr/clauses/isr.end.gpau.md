---
id: isr.end.gpau
type: endorsement
heading: GPAU General Property Anywhere in Australia
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.cover.options_requested
  rules:
  - when: '''GPAU'' in qs.isr.cover.options_requested'
    action: broker_option
  reason: Offered as an option for portable property anywhere in Australia.
---

The portable property described in the Schedule (for example laptops, tools, unregistered mobile plant, samples and display goods) is covered against Damage anywhere in Australia, including in transit, up to the sub-limit shown. If the Schedule says so, cover also applies outside Australia for trips of up to the number of days shown. We do not pay for theft from an unattended vehicle unless it was locked and the theft followed forcible entry; property lent or hired to others; or vehicles registered for road use.

Schedule variables: property description; sub-limit; overseas days (optional).
