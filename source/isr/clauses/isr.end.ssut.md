---
id: isr.end.ssut
type: endorsement
heading: SSUT Service of Suit
since: 1.1.0
status: draft
note: Contains 1 WP REVIEW tag for the Wording Partner.
trigger:
  questions:
  - qs.isr.placement.apra_authorised
  - qs.isr.placement.binder_jurisdiction_clause
  rules:
  - when: qs.isr.placement.apra_authorised == no and qs.isr.placement.binder_jurisdiction_clause == no
    action: apply
  reason: Applies because the capacity is not APRA-authorised and the binder supplies no jurisdiction clause.
---

If we do not pay an amount claimed to be due under this Policy, we will at your request submit to the jurisdiction of a competent court in Australia and do everything needed to give that court jurisdiction. Process may be served on the person named in the Schedule as our nominee for service in Australia, who is authorised to accept it for us. [WP REVIEW: align with Lloyd's and the capacity provider's own mandated clause.]

Schedule variables: nominee for service.
