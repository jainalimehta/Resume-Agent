# Interview Preparation — Data Analyst, Product, Relay

## Fit Reality

This is a significant stretch role. Jainali has a relevant master's degree, Australian Data Intern experience, PostgreSQL, SQL, window functions, advanced Excel, customer and transaction analysis, survey analysis, relational modelling, data-quality controls, KPI reporting, business recommendations, AI-assisted analysis, and Power BI planning. She does not have two years of analyst employment, professional product analytics, A/B testing, production BI tools, event-log analysis, large-scale datasets, SQL performance tuning, cloud warehouses, dbt, Python, R, senior-leadership reporting, or implemented interactive dashboards. The strategy is to show excellent fundamentals, product reasoning, and learning capacity without disguising this gap.

## 90-Second Introduction

“I currently live in Toronto, while my education and work experience are international. I completed a Master of Business Analytics at Edith Cowan University in Australia and an Integrated MBA at Atmiya University in India. As a Data Intern at AYLA Solutions in Australia, I gathered reporting requirements, translated stakeholder questions into analytical tasks, supported SQL extraction and validation, and prepared advanced Excel reports and dashboard insights. My strongest product-relevant project is E-Commerce Sales Analytics, where I modelled customers, orders, products, line items, and payments; defined revenue and integrity rules; and analyzed spend, purchase frequency, product performance, revenue trends, and payment methods using CTEs and window functions. I also completed customer transaction analysis for Bank of Baroda and surveyed small businesses about online GST-filing adoption. I have not yet performed professional A/B testing or used Relay's BI and cloud tools, but I bring strong SQL foundations, disciplined data quality, clear documentation, and genuine interest in using data to improve small-business financial decisions.”

## Why Relay?

“Relay's mission makes the analytics work concrete: help self-made business owners understand cash flow and make stronger decisions. I am interested in product questions that connect behaviour to outcomes—for example, whether onboarding leads to funding, whether customers adopt useful money-management workflows, and where friction prevents repeat use. Relay's current growth also makes consistent definitions, trustworthy models, and careful experimentation increasingly important. I would value contributing my customer, payment, SQL, validation, and AI-assisted analysis foundation while growing into production product analytics.”

## Honest Gap Answer

“I do not have two years of analyst employment or professional product-experimentation experience. I have not used Metabase, Sigma, Mode, Periscope, dbt, cloud warehouses, Python, or R, and my Power BI work is dashboard planning rather than interactive implementation. My strongest hands-on tools are PostgreSQL, SQL, and advanced Excel. I would not present interview study as experience. I would begin by learning Relay's event taxonomy, governed models, KPI definitions, experimentation standards, and existing dashboards; reproduce a trusted analysis; reconcile it to control totals; own a bounded question under review; and expand responsibility only after demonstrating accuracy and sound reasoning.”

## Understand Relay's Product

- Relay describes itself as a financial technology company and a banking and money-management platform for U.S. small businesses, not a bank; banking services are provided through banking partners.
- Product areas include checking and savings, money movement, cards and controls, expense management, accounts payable, invoices, payment requests, cash-flow management, and accounting integrations.
- Product analytics should connect feature behaviour to customer outcomes without losing sight of security, compliance, trust, and operational reliability.
- Never invent Relay's internal north-star metric, data model, risk rules, or product definitions. Present proposed metrics as hypotheses to validate with product and data owners.

## Business-Problem-First Framework

1. What decision must be made, by whom, and by when?
2. Which customer problem or business objective does it address?
3. What behaviour should change if the product succeeds?
4. What is the primary metric, and what guardrails prevent a misleading win?
5. Which users are eligible, exposed, and measurable?
6. Which data sources, definitions, and quality risks apply?
7. What result would lead to launch, iteration, or stopping?
8. How will the outcome be communicated and monitored?

## Candidate Product-Metric Tree

Treat this as a discussion framework, not Relay's actual metric system.

- **Acquisition:** qualified visits, application starts, completion, approval, and acquisition cost.
- **Activation:** approved account, first funding, first money movement, first completed workflow, and time to value.
- **Engagement:** active businesses, transaction frequency, recurring activity, feature breadth, and workflow completion.
- **Retention:** repeat activity, retained funded accounts, cohort retention, dormancy, and reactivation.
- **Financial behaviour:** cash allocation, payment completion, account balance patterns, scheduled activity, and avoidable disruptions—only under approved definitions.
- **Customer experience:** support contacts, resolution, satisfaction, survey feedback, and recurring friction themes.
- **Reliability and risk guardrails:** failures, reversals, latency, defects, suspicious activity, complaints, and access or security incidents.

A possible north-star candidate could be “retained active businesses completing meaningful money-management activity,” but the exact event, frequency, eligibility, and retention window must be defined with Relay.

## Funnel and Cohort Analysis

Example funnel: eligible visitor → application started → application completed → approved → account funded → first successful transaction → repeat active use → adoption of another valuable workflow.

- Define one entity and one eligibility rule for each stage.
- Use ordered timestamps and agreed conversion windows.
- Distinguish user, business, account, and transaction grain.
- Segment carefully by acquisition source, business type, tenure, device, or product only when privacy and sample size permit.
- Analyze both conversion and time between stages.
- Use cohorts based on a consistent starting event; do not mix calendar trends with retention curves.
- Investigate instrumentation changes before interpreting a sudden funnel movement.

## A/B Testing Framework

Jainali has not run a professional A/B test. Use this as learned methodology.

1. State the customer problem, hypothesis, treatment, and expected mechanism.
2. Choose the randomization unit—often user or business—and prevent cross-group contamination.
3. Define eligibility and exposure before looking at results.
4. Select one primary success metric and a small set of guardrails.
5. Estimate baseline, minimum detectable effect, sample size, power, and required duration with a qualified reviewer.
6. Validate assignment and check sample-ratio mismatch.
7. Run for a sufficient business cycle; avoid stopping when results first look favourable.
8. Report effect size, uncertainty, practical significance, and guardrail movement—not only a p-value.
9. Check predefined segments cautiously and avoid uncontrolled multiple comparisons.
10. Decide whether to launch, iterate, extend, or stop; document limitations and follow-up monitoring.

If randomization is impossible, discuss pre/post analysis, matched cohorts, difference-in-differences, interrupted time series, or phased rollout only as alternatives with stronger assumptions—not as equivalent proof.

## Integrating Diverse Sources

| Source | Useful evidence | Main risks |
|---|---|---|
| Event logs | Feature exposure, clicks, workflow completion, sequence and timing | Missing events, duplicate events, version changes, bots, identity stitching |
| Operational data | Transactions, statuses, failures, support and processing outcomes | Different grains, late updates, reversals, mutable status |
| Surveys | Motivation, perception, unmet need and self-reported outcome | Response bias, wording effects, small samples, non-response |
| User feedback | Detailed context and friction themes | Not representative; subjective coding |
| Financial or account data | Behaviour and business outcome proxies | Privacy, access, definitions, compliance, extreme skew |

Triangulate: use behavioural data to show what happened, operational data to show system outcomes, and surveys or feedback to help explain why. Do not treat qualitative evidence as population prevalence without validation.

## Data-Quality Framework

- Confirm grain, keys, owners, refresh timing, lineage, permissions, and authoritative sources.
- Test completeness, uniqueness, validity, consistency, referential integrity, timeliness, and reconciliation.
- Validate event names, required properties, timestamps, ordering, version, and identity resolution.
- Protect against duplicate multiplication after joins.
- Reconcile row counts and financial or operational totals at each transformation stage.
- Maintain an exception output and document rule changes.
- When a defect appears: quantify impact, isolate source versus transformation, protect downstream reporting, correct and retest, communicate affected decisions, and add a preventive test.

## Data Modelling Preparation

- Identify fact-table grain before choosing dimensions or measures.
- Possible facts: product events, transactions, applications, support interactions, or daily business-account snapshots.
- Possible dimensions: business, user, account, product, date, channel, status, and experiment assignment.
- Use conformed definitions so KPIs agree across teams.
- Separate mutable current state from historical events or snapshots.
- Document slowly changing attributes and point-in-time logic.
- Add metric ownership, lineage, tests, and access controls.

Do not claim production data-modelling ownership; connect these concepts to Jainali's verified relational portfolio.

## SQL Case Preparation

Review and be able to explain:

- Grain, primary and foreign keys, and why joins can duplicate measures.
- `INNER JOIN` versus `LEFT JOIN`, null handling, and anti-joins for missing records.
- CTEs for readable multi-stage analysis.
- Conditional aggregation for funnel and status metrics.
- `ROW_NUMBER`, `RANK`, `LAG`, running totals, and rolling windows.
- Cohort month, retention, repeat activity, and time-to-event logic.
- Deduplication using a deterministic event key and timestamp.
- Percentiles and skewed transaction values conceptually.
- Reconciliation queries and exception tables.
- Performance concepts: select only required columns, filter early where appropriate, inspect query plans, understand join cardinality, and avoid unnecessary repeated computation.

Only write or discuss SQL that Jainali can explain line by line.

## Likely Take-Home Case Structure

1. Restate the business question and decision.
2. List assumptions, grain, metric definitions, and exclusions.
3. Profile and validate the supplied data.
4. Present a small number of decision-relevant analyses.
5. Show clear charts with direct titles and labelled units.
6. Separate observations from explanations and causal claims.
7. Recommend actions tied to evidence, owners, and monitoring metrics.
8. Include limitations, missing data, and follow-up questions.
9. Provide readable SQL or analysis logic and a data-quality appendix.
10. Prepare a concise verbal narrative: problem → evidence → implication → recommendation.

Never fabricate outcomes or hide a data limitation to make the case appear complete.

## Example Product Cases

### First funding declined after an onboarding change.

Validate instrumentation and eligibility first. Compare application, approval, funding, and time-to-fund by release version and cohort. Segment the largest drop carefully, examine errors and support contacts, and distinguish fewer eligible users from worse conversion. Recommend rollback, targeted remediation, or an experiment based on evidence and guardrails.

### A new feature has high clicks but low repeat use.

Define exposure, successful completion, and repeat window. Check whether clicks represent curiosity, confusion, or actual value. Analyze completion, errors, time, cohort retention, adjacent workflows, feedback, and support contacts. Recommend usability research, workflow simplification, better education, or targeted testing rather than treating clicks as success.

### Product and Finance report different transaction totals.

Confirm status, date, time zone, reversals, settlement versus initiation, currency, test records, and grain. Reconcile by stage, isolate unmatched records, agree on the certified definition for each use case, fix the governed model rather than one report, and add a regression test.

### A stakeholder asks for a dashboard without a clear question.

Ask which decision the dashboard supports, who acts, which behaviours matter, the required cadence, and what action follows a threshold. Draft a metric-definition sheet and prototype, validate it against control totals, and agree acceptance criteria before expanding.

## Behavioural Evidence

- **Ambiguous request:** AYLA—translated stakeholder questions into structured analytical tasks.
- **Customer insight:** E-Commerce project—customer spend, frequency, revenue, product, and payment analysis.
- **Banking context:** Bank of Baroda—customer transaction trends and engagement recommendations.
- **Survey insight:** GST research—Google Forms, Excel cleaning, pivot tables, adoption patterns, and barriers.
- **Data quality:** E-Commerce project—keys, revenue rules, integrity checks, repeatable validation, and GitHub Actions.
- **AI-enabled work:** Published AI-assisted recommendations grounded in validated SQL outputs.
- **Coordination:** Trans Globe Education—maintained records and coordinated updates with students and institutions.

Use Situation, Task, Action, and Result. Where no quantified result is verified, finish with the factual deliverable.

## Questions to Ask

1. Which product area and customer problem would this analyst support first?
2. What is Relay's current north-star metric, and which guardrails accompany it?
3. How are data responsibilities divided among product analysts, data engineers, product managers, and data scientists?
4. Which BI, warehouse, transformation, experimentation, and event-tracking tools are used today?
5. How mature are Relay's event taxonomy, semantic definitions, and automated quality tests?
6. What types of decisions have analysts most influenced recently?
7. What does an excellent take-home case demonstrate beyond technically correct analysis?
8. What support is available for a candidate growing into the full scope of the role?

## 30-60-90 Day Approach

- **First 30 days:** Learn customer journeys, product areas, data stack, event definitions, governed KPIs, security, existing dashboards, experimentation process, and stakeholders; reproduce a trusted analysis.
- **Days 31-60:** Own a bounded product question under review, document definitions and quality checks, contribute to a dashboard or model, and present findings to the immediate team.
- **Days 61-90:** Deliver an approved insight or reporting improvement, support an experiment or feature evaluation, document reusable logic, and monitor the recommended action and guardrails.

## Accuracy Guardrails

- Do not claim two years of analyst employment, professional product analytics, A/B testing, causal inference, event-log analysis, or large-dataset scale.
- Do not claim Metabase, Sigma, Periscope, Mode, cloud warehouses, dbt, Python, R, or implemented interactive Power BI dashboards.
- Do not claim SQL performance tuning or security implementation as experience.
- Do not describe academic projects as Relay, production, startup, or enterprise work.
- Do not invent dataset sizes, lift, revenue impact, customer counts, work authorization, or language proficiency.
- Keep Toronto residence separate from Australian and Indian education and employment.

## Official Research

- [Relay — About](https://relayfi.com/about/): mission, small-business focus, product purpose, banking partnership, and company context.
- [Relay — Product](https://relayfi.com/product/): checking, money movement, cards and controls, transaction data, and customer workflows.
- [Relay — Accountants and Bookkeepers](https://relayfi.com/accountants-and-bookkeepers/): banking, expense management, accounts payable, cash-flow management, and accounting integrations.
- [Relay — Safety and Security](https://relayfi.com/safety-and-security/): fintech status, banking partners, identity verification, security, and compliance context.
- [Relay — 2026 Growth Financing](https://relayfi.com/blog/relay-50m-financing-announcement/): current growth stage, product investment, and small-business customer context.

Recheck the posting, current official product information, and Relay's approved internal metric definitions before interviewing.
