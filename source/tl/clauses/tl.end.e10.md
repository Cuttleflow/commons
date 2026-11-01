---
id: tl.end.e10
type: endorsement
heading: E10 Government and Defence Contractor
since: 1.4.0
status: draft
trigger:
  questions:
  - qs.tl.ops.government_contracts
  rules:
  - when: qs.tl.ops.government_contracts == yes
    action: refer
  reason: Considered because you supply technology products or services to government or defence customers.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

[[ref:tl.excl.contractual-liability]] and [[ref:tl.ext.contractual-liability]] are read so that a liability under a contract with an Australian federal, state or territory government body, or a defence prime contractor, is covered only to the extent the liability would have arisen without the contract, or the schedule for this endorsement names the contract.

Cover for a claim under a contract named in the schedule includes liquidated damages, service credits and the cost of re-performing the work, up to the sub-limit shown for this endorsement, which is part of the limit of liability.

This endorsement does not cover: (a) a claim relating to classified information, or a breach of a security clearance or an export control; (b) a fine or penalty; (c) a claim made by a government body in its capacity as a regulator; or (d) a claim outside Australia unless [[ref:tl.end.e01]] applies.

Schedule variables: named contracts; sub-limit.
