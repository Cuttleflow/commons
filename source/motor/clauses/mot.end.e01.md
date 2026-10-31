---
id: mot.end.e01
type: endorsement
heading: E01 Heavy Vehicles
since: 3.0.0
status: draft
trigger:
  questions:
  - qs.mot.vehicles.heavy_count
  rules:
  - when: qs.mot.vehicles.heavy_count > 0
    action: apply
  reason: Applies because {qs.mot.vehicles.heavy_count} vehicle(s) have a gross vehicle mass over 4.5 tonnes.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
---

This Endorsement applies to each Insured vehicle shown in the Schedule with a gross vehicle mass over 4.5 tonnes. For those vehicles: the basic excess shown for heavy vehicles in the Schedule applies; we pay the reasonable cost of a replacement vehicle hired while the vehicle is off the road after loss or damage covered by [[ref:mot.section.vehicle-cover]], up to the daily amount and period shown in the Schedule, after a waiting period of 48 hours; and [[ref:mot.obl.maintain-vehicles]] applies with the addition that you must keep the maintenance, fatigue and mass records the Heavy Vehicle National Law requires and give them to us on request.

Schedule variables: heavy vehicle basic excess; replacement vehicle daily amount and period.
