---
id: isr.end.lead
type: endorsement
heading: LEAD Leading Insurer
since: 1.1.0
status: draft
note: Contains 1 WP REVIEW tag for the Wording Partner.
trigger:
  questions:
  - qs.isr.placement.participant_count
  - qs.isr.placement.lead_named
  rules:
  - when: qs.isr.placement.participant_count > 1 and qs.isr.placement.lead_named == yes
    action: apply
  reason: Applies because more than one insurer subscribes and a leading insurer is named.
---

- The leading insurer named in the Schedule acts for all insurers on this Policy in issuing documents; agreeing alterations that do not increase any insurer's exposure, or reduce premium by more than the threshold shown in the Schedule; appointing loss adjusters and experts; and agreeing claims up to the claims authority shown.
- Alterations and claims beyond that authority need the agreement of the insurers shown in the Schedule (all insurers, or insurers holding the share shown).
- A decision the leading insurer makes within its authority binds every insurer. Each insurer remains liable only for its own share.
- You may deal with the leading insurer on all matters under this Policy. Notice given to it is notice to all insurers.

[WP REVIEW: confirm the lead's authority is enforceable against followers through this clause alone.]

Schedule variables: leading insurer; alteration threshold; claims authority; agreement required above authority.
