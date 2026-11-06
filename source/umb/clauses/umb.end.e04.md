---
id: umb.end.e04
type: endorsement
heading: E04 Heavy Vehicles
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.umb.underlying.heavy_vehicles
  - qs.umb.underlying.dangerous_goods
  rules:
  - when: qs.umb.underlying.heavy_vehicles > 25
    action: refer
  - when: qs.umb.underlying.dangerous_goods == true
    action: refer
  - when: qs.umb.underlying.heavy_vehicles > 0
    action: apply
  reason: Applies because you operate {qs.umb.underlying.heavy_vehicles} heavy vehicles, and this policy sits above their motor liability insurance.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

Motor vehicle liability insurance for the heavy vehicles described in the schedule is underlying insurance, and [[ref:umb.cover.coverage-a]] applies above it for property damage, and for personal injury where no compulsory third party scheme or statutory motor accident scheme provides cover. A heavy vehicle is a vehicle with a gross vehicle mass of more than 4.5 tonnes, or a trailer or prime mover.

This endorsement does not cover liability arising from the carriage of dangerous goods, within the meaning of the Australian Code for the Transport of Dangerous Goods by Road and Rail, unless the schedule says so.

Schedule variables: the number and type of heavy vehicles; the motor liability insurer and limit; whether dangerous goods are covered.
