---
id: mcg.end.e12
type: endorsement
heading: E12 Stock in Storage
since: 1.2.0
status: draft
trigger:
  questions:
  - qs.mcg.storage.stock_in_storage
  - qs.mcg.storage.max_location_value
  - qs.mcg.storage.locations
  rules:
  - when: qs.mcg.storage.max_location_value > 1000000
    action: refer
  - when: qs.mcg.storage.locations > 3
    action: refer
  - when: qs.mcg.storage.stock_in_storage == yes
    action: apply
  reason: Applies because you asked for cover for stock in storage; refers when more than $1,000,000 is held at one location or stock is held at more than 3 locations.
  responses:
  - Attach with premium loading
  - Attach with amended sub-limit
  - Do not attach
  - Decline risk
---

In this endorsement:

- **stock** means goods of the kinds this policy insures that you own, or that you hold for others and are responsible for, while they are not in the course of a transit;
- **third-party location** means premises operated by someone other than you, such as a warehouse, a bonded store or a logistics provider, shown in the schedule for this endorsement;
- **your premises** means premises you occupy, shown in the schedule for this endorsement; and
- **natural catastrophe** means storm, flood, earthquake, tsunami, cyclone or bushfire.

We insure stock against all risks of physical loss or damage while it is stored at a third-party location or at your premises, for loss or damage that happens during the policy period. Stock in the course of a transit, including storage in transit under [[ref:mcg.end.e09]], is insured under the Transit section and not under this endorsement. This endorsement insures property on land that is not in transit, and the Insurance Contracts Act 1984 (Cth) applies to it.

**Limits.** The most we pay is:

- for any one occurrence at any one third-party location, its location limit shown in the schedule (default $250,000);
- for any one occurrence at any one of your premises, its location limit shown in the schedule (default $100,000);
- for loss or damage caused by a natural catastrophe, 50% of the location limit at each location; and
- for all locations together, the aggregate limit shown in the schedule for any one occurrence and in total for the policy period (default $500,000).

**Your premises.** At your premises this endorsement applies only in excess of the property insurance policy shown in the schedule for those premises, and pays the part of the loss above the amount that policy pays. If the schedule shows no property insurance policy for your premises, this endorsement applies to them as the first insurance. [WP REVIEW: confirm that naming the property policy in the schedule makes this an excess-of-a-specified-contract provision within section 45(2) of the Insurance Contracts Act 1984 (Cth).]

**Valuation.** We value stock at the cost of replacing it with stock of the same kind and quality at the time of the loss, including freight and duties paid. For stock you hold for others, we pay the amount you are legally liable for, up to that value.

**Not insured.** We do not pay for:

- a shortage found only at a stocktake, or an unexplained disappearance;
- wear and tear, gradual deterioration, inherent vice, vermin or insects;
- a change in temperature or humidity, unless it is caused by physical damage to the building;
- stock kept in the open air;
- stock at any location not shown in the schedule; or
- theft from your premises without forcible and violent entry into the building.

The general exclusions of this policy also apply.

**Condition.** Each location must be a closed building, locked when it is unattended. This condition is not a warranty. If you do not meet it, we may refuse only the part of the claim that the failure caused or contributed to, as [[ref:mcg.cond.insurance-contracts-act]] sets out.

The excess shown in the schedule for this endorsement applies to each occurrence; if none is shown, the excess for the Transit section applies.

Schedule variables: third-party locations and the limit at each (default $250,000); your premises, the limit at each (default $100,000) and the property insurance policy for each; aggregate limit (default $500,000); excess (default the Transit section excess).
