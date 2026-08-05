# Interview Preparation — Data Analyst, SHEIN

## Fit Assessment

This role is a credible early-career target because it welcomes new graduates and directly values advanced Excel, SQL, KPI reporting, analytical problem solving, business acumen, communication, and fast learning. Jainali's strongest evidence is her Australian Data Intern experience, Master of Business Analytics, Integrated MBA, Supply Chain Analytics coursework, and E-Commerce Sales Analytics portfolio project. The principal gaps are Python, professional logistics and customs experience, budget/forecast ownership, risk-management ownership, and unverified Canadian work authorization.

## 90-Second Introduction

“I currently live in Toronto, while my education and experience are international. I completed a Master of Business Analytics at Edith Cowan University in Australia and an Integrated MBA at Atmiya University in India. As a Data Intern at AYLA Solutions in Australia, I gathered reporting requirements, supported SQL extraction and validation, and prepared advanced Excel reports and dashboard insights. My E-Commerce Sales Analytics project connects customer, product, order, line-item, and payment data and uses controlled revenue rules, trend analysis, rankings, window functions, and repeatable validation to generate recommendations. I also completed Supply Chain Analytics coursework. I have not yet worked professionally in logistics, customs compliance, or budgeting, and I do not claim Python experience. I bring a strong SQL and Excel foundation, careful documentation, business thinking, and the ability to learn quickly in a fast-moving operating environment.”

## Why SHEIN?

- The role connects data analysis to tangible operational questions: delivery efficiency, cost, budget, risk, documentation, and customer experience.
- SHEIN describes its model as technology-enabled and on-demand, making reliable operational data and rapid decision cycles central to the business.
- The combination of e-commerce, supply-chain operations, KPIs, and process improvement closely matches Jainali's project evidence and graduate coursework.

## Honest Gap Answer

“My direct experience is in analytics and process support rather than logistics operations. I have not managed customs documentation, freight vendors, annual budgets, or last-mile cost programs professionally, and I have not used Python. My strongest tools are advanced Excel, PostgreSQL, and SQL. I would approach the learning curve by first understanding SHEIN's process definitions and data sources, documenting metric logic, validating outputs with operations partners, and learning the required domain rules and tools in a structured way. I would rather be transparent about the starting point and demonstrate how quickly and carefully I can build from it.”

## Supply-Chain Metrics to Understand

Be ready to explain the business meaning, formula, data source, and limitations of each metric:

- **On-time delivery rate:** Orders or shipments delivered by the promised date divided by eligible deliveries.
- **Order cycle time:** Time from order creation or release to final delivery; define the exact start and end events.
- **Transit time:** Time between carrier pickup and delivery, segmented by lane, carrier, service, and destination.
- **Cost per order/shipment:** Eligible logistics cost divided by orders or shipments; reconcile scope before comparing periods.
- **Mid-mile and last-mile cost:** Separate movements between facilities from the final delivery leg and control for geography, service level, weight, and volume.
- **First-attempt delivery rate:** Deliveries completed on the first attempt divided by attempted deliveries.
- **Exception rate:** Shipments with delay, damage, loss, customs hold, address issue, or other exception divided by eligible shipments.
- **Customs-clearance time:** Time from customs submission or arrival to clearance; distinguish controllable and external delay.
- **Forecast variance:** Actual minus forecast, shown in value and percentage terms with a clearly defined denominator.
- **Budget variance:** Actual cost minus budget; explain volume, rate, mix, timing, and one-time drivers.
- **Inventory or order aging:** Time items remain in a defined status; use aging buckets and investigate long-tail exceptions.

## KPI Design Framework

For every KPI, document:

1. Business question and intended decision.
2. Numerator, denominator, inclusions, exclusions, and time zone.
3. Source systems, grain, keys, refresh schedule, and owner.
4. Required dimensions such as lane, carrier, region, facility, service level, product category, and date.
5. Validation method and reconciliation total.
6. Target, threshold, trend, and escalation rule.
7. Known limitations and change-control process.

## Likely Technical Case

### Delivery cost increased while order volume was stable. How would you investigate?

1. Confirm the increase is real by reconciling totals and checking currency, duplicate charges, incomplete periods, and accounting timing.
2. Decompose total cost into shipment volume, weight, distance, lane, carrier, service level, fuel or accessorial charges, failed attempts, and returns.
3. Compare rate, volume, and mix effects rather than relying only on averages.
4. Segment mid-mile and last-mile costs and identify the locations, carriers, and services driving the change.
5. Examine operational causes such as routing, consolidation, address quality, delivery exceptions, peak surcharges, or expedited shipments.
6. Quantify opportunities, validate them with operations and finance, and present options with risks and assumptions.
7. Track approved actions through an owner, deadline, expected impact, and post-implementation KPI.

### A KPI suddenly drops. What do you check first?

- Confirm whether the definition, source, refresh, filters, joins, or denominator changed.
- Check missing dates, duplicates, nulls, status mappings, late-arriving records, and time-zone logic.
- Compare the result with a trusted control total and a prior stable period.
- Determine whether the change is a data-quality issue or a real operational event before recommending action.

## SQL Topics to Review

- Joins and how duplicate keys can multiply rows.
- `GROUP BY`, conditional aggregation, and distinct counts.
- CTEs for readable multi-step analysis.
- Window functions for ranking, running totals, lag comparisons, and rolling metrics.
- Date arithmetic for cycle time and aging.
- Null handling and division-by-zero protection.
- Duplicate detection and referential-integrity checks.
- Reconciliation queries that compare source totals with transformed outputs.

## Excel Topics to Review

- Pivot tables, filters, sorting, conditional formatting, and charts.
- `XLOOKUP` or equivalent lookup logic, `SUMIFS`, `COUNTIFS`, `IF`, date functions, and error handling.
- Data validation, duplicate checks, text cleaning, and consistent date/number formats.
- Variance bridges showing actual versus budget or forecast.
- A clean analysis structure: raw data, mapping/assumptions, calculations, checks, summary, and presentation.

Never claim a function or technique in the interview unless comfortable demonstrating it.

## Behavioural Stories to Prepare

- **Requirements and ambiguity:** AYLA Solutions—turning stakeholder questions into structured reporting tasks.
- **Accuracy:** Arihant Investment—maintaining confidential client records and accurate documentation.
- **Coordination:** Trans Globe Education—coordinating application updates with students and institutions.
- **Problem solving:** E-Commerce Sales Analytics—establishing revenue-status rules and validating relationships and outputs.
- **Learning new tools:** PostgreSQL projects and GitHub Actions—describe only the verified learning and implementation work, without inventing speed or outcomes.

Prepare each story using Situation, Task, Action, and Result. Where no measured result is verified, use a factual outcome such as completed analysis, accurate records, documented requirements, or clear recommendations.

## Questions to Ask the Interviewer

1. Which logistics decisions and KPIs would this analyst support most frequently during the first six months?
2. What are the principal data sources and reporting tools used by the Vaughan team?
3. How are metric definitions and data-quality issues governed across Operations, Finance, and other departments?
4. What is the balance between recurring reporting, special-case analysis, and project work?
5. Which mid-mile and last-mile cost drivers are currently the team's highest analytical priorities?
6. What training is provided for customs documentation, logistics processes, and internal budgeting standards?
7. How is analyst performance measured in this role?

## 30-60-90 Day Approach

- **First 30 days:** Learn the logistics process, systems, data definitions, KPI logic, reporting cadence, documentation controls, stakeholders, and escalation routes; reproduce existing reports and reconcile them to trusted totals.
- **Days 31-60:** Own assigned reporting under review, investigate exceptions, document metric logic, support forecast and cost analysis, and communicate concise findings with assumptions and next actions.
- **Days 61-90:** Deliver reliable recurring analysis with increasing independence, support a targeted process-improvement case, strengthen one validation or reporting control, and measure the result using an agreed KPI.

## Authorization and Accuracy Guardrails

- The posting requires authorization to work in Canada. Jainali must answer this based on her actual legal status; it is not verified in the resume profile.
- Do not claim Python, logistics employment, customs compliance, import-document expertise, budget ownership, forecast ownership, vendor management, or measured cost savings.
- Do not imply Canadian education or Canadian employment.
- Do not claim Tableau, IBM SPSS Statistics, or published interactive Power BI dashboards.
- If asked about an unfamiliar regulation, metric, or system, explain how it would be verified with the responsible owner and approved documentation.

## Official Company Research

- [SHEIN Group — Process and Waste-Less Innovation](https://www.sheingroup.com/process): on-demand model, resource efficiency, data analytics, testing, and value-chain improvement.
- [SHEIN Group — Sustainability](https://www.sheingroup.com/sustainability): digitalized supply chain and inventory-waste positioning.
- [SHEIN Group — Supply-Chain Logistics Improvements](https://www.sheingroup.com/newsroom/shein-advances-efforts-to-lower-supply-chain-emissions-and-divert-waste-from-landfill): logistics efficiency, route planning, multimodal transport, air-freight optimization, and last-mile initiatives.

Use these sources to understand the company's stated operating model; do not repeat corporate performance claims unless the interviewer asks and the current source has been rechecked.
