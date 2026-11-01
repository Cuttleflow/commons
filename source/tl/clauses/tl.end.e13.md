---
id: tl.end.e13
type: endorsement
heading: E13 Missed Bid Income Loss
since: 1.4.0
status: draft
trigger:
  questions:
  - qs.tl.cover.options_requested
  rules:
  - when: '''E13'' in qs.tl.cover.options_requested'
    action: broker_option
  reason: Offered because you asked for cover for contracts you lose because of a cyber event.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

The [[ref:tl.section.cyber|heading]] section extends to your lost net profit on a tender or bid you were unable to submit by its closing date because a **cyber security breach** made your **computer system** unavailable, where you have the written tender documents showing the closing date and you had begun preparing the bid before the breach.

We pay net profit on the bid only to the extent you show, from the bid documents and your record of similar bids you won in the preceding 24 months, that you would have won it. We pay for no more than the number of bids and the amount per bid shown in the schedule for this endorsement.

This endorsement does not cover a bid you did not submit for a reason other than the **cyber security breach**, or a bid for work you could not have performed.

Schedule variables: sub-limit; maximum amount per bid; maximum number of bids.
