---
id: isr.end.namd
type: endorsement
heading: NAMD Named Insured and Related Entities
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.insured.entity_count
  rules:
  - when: qs.isr.insured.entity_count > 1
    action: apply
  reason: Applies because the policy insures more than one entity.
---

The Insured includes:

- each entity named in the Schedule;
- each subsidiary of a named entity at the start of the Period of Insurance, as "subsidiary" is defined in the Corporations Act 2001 (Cth);
- each entity that becomes such a subsidiary during the Period of Insurance, for the acquisition period shown in the Schedule after it does so, or longer if we agree in writing; and
- any other person or entity named in the Schedule, for its own interest only.

Each is covered for its own interest in the insured property and the business. The entity named first in the Schedule acts for all of them in giving and receiving notices, paying premium and receiving claim payments, unless the Schedule says otherwise. An entity that becomes a subsidiary during the Period of Insurance is not covered for Damage that happened before it did.

Schedule variables: named entities; acquisition period (default 90 days); first-named entity.
