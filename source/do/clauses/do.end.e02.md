---
id: do.end.e02
type: endorsement
heading: E02 Small Capitalisation and Resources Companies
since: 1.3.0
status: draft
trigger:
  questions:
  - qs.do.insured.entity_type
  - qs.do.insured.anzsic_primary
  - qs.do.exposure.market_cap
  rules:
  - when: "qs.do.insured.entity_type == 'listed' and qs.do.exposure.market_cap < 500000000 and qs.do.insured.anzsic_primary startswith ['06','07','08','09','10']"
    action: refer
  - when: "qs.do.insured.entity_type == 'listed' and qs.do.exposure.market_cap < 500000000"
    action: suggest
  reason: Applies because the company is listed, has a market capitalisation under A$500 million and, if in resources, carries JORC and capital-raising exposure.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

Designed for ASX-listed companies with a market capitalisation below $500 million, particularly companies in the mining, exploration, oil and gas, and resources sectors.

**Additional Definitions**

Competent person means a person who is a member or fellow of a recognised professional body for mining or geoscience (such as the Australasian Institute of Mining and Metallurgy or the Australian Institute of Geoscientists), or of a professional organisation recognised for the public reporting of mineral resources and ore reserves, and who has experience appropriate to the deposit or mineralisation in question.

JORC Code means the Australasian Code for Reporting of Exploration Results, Mineral Resources and Ore Reserves, as published by the Joint Ore Reserves Committee, as amended from time to time.

Resources disclosure claim means a claim that alleges misleading or deceptive conduct, breach of continuous disclosure obligations, or breach of the JORC Code, in connection with public statements about exploration results, mineral resources, ore reserves, exploration targets, production targets, or financial forecasts based on production targets.

Capital raising claim means a claim arising from a prospectus, placement, share purchase plan, rights issue, entitlement offer, or other capital raising conducted by the company during the policy period.

**Extended Insured Persons**

The definition of insured person is extended to include: (a) any competent person who signs off on or is named in a public report by the company as the competent person for the purposes of the JORC Code, but only for claims arising from that report; and (b) any geologist, metallurgist, or technical consultant engaged by the company who is named in a public report as having reviewed or contributed to resource or reserve estimates, but only for claims arising from that report.

**JORC and Resources Disclosure — Coverage Clarification**

For the avoidance of doubt, this policy covers: (a) claims alleging that the company or an insured person published exploration results, resource estimates, or production targets that were misleading, incomplete, or not in compliance with the JORC Code; (b) claims alleging that announcement headers, summaries, or investor presentations about exploration results were unbalanced or gave an unduly favourable impression; (c) enforcement actions relating to forward-looking statements, scoping studies, or production targets that ASIC determines lacked a reasonable basis; and (d) ASX queries and price queries relating to disclosure of exploration results, and any resulting investigation or enforcement action. Each of the matters described in paragraphs (a) to (d) is a Resources disclosure claim.

**Frequent Capital Raisings**

Many small capitalisation companies conduct multiple capital raisings during a single policy period. We will cover each Capital raising claim arising from a capital raising conducted during the policy period, without requiring a separate prospectus policy for each raising — provided the aggregate proceeds of all raisings during the policy period do not exceed $100,000,000 (or such higher amount as agreed and shown in the schedule).

If the aggregate proceeds exceed this threshold, we may require a separate prospectus policy for subsequent raisings.

**Voluntary Suspension**

We will cover defence costs incurred by an insured person in connection with an ASX voluntary suspension requested by the company to comply with continuous disclosure obligations, including any subsequent inquiry about the basis for or duration of the suspension.

**Personal Guarantees by Directors**

We will cover claims against an insured person arising from a personal guarantee given by the insured person to secure a financial obligation of the company — but only where: (a) the guarantee was given in the insured person's capacity as a director of the company; (b) the guarantee was disclosed to and approved by the board; and (c) the claim arises from an alleged wrongful act in the management of the company, not from the mere failure to pay the guaranteed obligation.

**Insolvent Trading — Safe Harbour**

This policy covers claims against an insured person for insolvent trading under section 588G of the Corporations Act 2001 (Cth), including defence costs in establishing that the insured person qualifies for the safe harbour defence under section 588GA.

The costs of engaging a qualified restructuring adviser to develop a course of action reasonably likely to lead to a better outcome than immediate winding up are covered as defence costs, where the advice is obtained in connection with a potential or actual insolvent trading claim.

**Native Title and Heritage**

We will cover defence costs incurred by an insured person in connection with proceedings or regulatory action alleging that the company failed to comply with native title obligations, Aboriginal heritage protection obligations, or cultural heritage management obligations — to the extent the claim alleges a wrongful act by the insured person in their governance capacity.

This does not cover the company's operational compliance obligations, which are a general liability exposure.

Schedule variables: Aggregate capital raising proceeds cap, if above A$100,000,000.
