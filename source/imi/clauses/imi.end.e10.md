---
id: imi.end.e10
type: endorsement
heading: E10 Prospectus and PDS Liability — Enhanced
since: 1.3.0
status: draft
trigger:
  questions:
  - qs.imi.cover.options_requested
  rules:
  - when: '''E10 Prospectus and PDS Liability — Enhanced'' in qs.imi.cover.options_requested'
    action: refer
  reason: Considered because you asked for cover for a prospectus or product disclosure statement.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

[[ref:imi.cover.financial-services-liability]] extends to any actual or alleged misleading or deceptive statement in, or omission from, a prospectus, product disclosure statement or other offer document for an offer shown in the schedule for this endorsement, including a claim by a person who acquired a financial product under the offer.

This endorsement does not cover a statement or omission in a document first issued before the retroactive date, or an offer made outside Australia unless Endorsement E01 is operative for that offer. [[ref:imi.excl.fund-performance]] continues to apply.

Schedule variables: offers covered (fund, document, date, offer size); sub-limit (optional).
