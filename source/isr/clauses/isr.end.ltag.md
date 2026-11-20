---
id: isr.end.ltag
type: endorsement
heading: LTAG Long-Term Agreement
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.cover.options_requested
  rules:
  - when: '''LTAG'' in qs.isr.cover.options_requested'
    action: refer
  reason: Referred because the broker asked for a long-term agreement.
---

You and we agree that this Policy will be renewed for the number of further periods shown in the Schedule at the same rates and on the same terms, provided that the ratio of claims paid and outstanding to premium over the agreement does not exceed the percentage shown; there has been no material change in the risk; and the premium has been paid. Either of us may end this agreement at any renewal date by giving the other written notice at least the number of days shown before that date. If a proviso is not met, we may offer renewal on different terms. Premium continues to adjust for changes in Declared Values under DVAD.

Schedule variables: further periods; loss ratio threshold; notice days (default 60).
