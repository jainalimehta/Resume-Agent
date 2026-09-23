# Interview Preparation — SureWerx Junior Data Analyst

## Core Positioning

Present yourself as an early-career analyst in Toronto with direct strengths in PostgreSQL, SQL, relational modelling, advanced Excel, data cleaning and validation, requirements documentation, KPI analysis, and repeatable testing. Describe Power BI accurately as KPI, visualization, and dashboard planning. Do not claim implemented dashboards, DAX, Power Query, Fabric, Copilot, ERP, integrations, UAT ownership, training, or production support.

## 90-Second Introduction

“I completed a Master of Business Analytics at Edith Cowan University in Australia and now live in Toronto. As a Data Intern at AYLA Solutions, I gathered and documented business and reporting requirements, supported SQL-based extraction and validation, prepared advanced Excel reports, contributed performance insights, and participated in Agile planning and reviews. My three published projects demonstrate relational PostgreSQL modelling, joins, CTEs, window functions, validation, GitHub Actions checks, KPI analysis, and completed AI-assisted interpretation across e-commerce, healthcare, and workforce data. Each also includes Power BI KPI and dashboard planning, although I have not yet published interactive dashboards. I am interested in SureWerx because this role would let me contribute my SQL, data-quality, and documentation foundation while learning deeper Power BI, integration, testing, and support practices from senior analysts.”

## Honest Power BI Answer

“My verified Power BI experience is in defining KPIs, visualization requirements, and dashboard layouts for three analytical projects. I have not yet published interactive dashboards or worked professionally with DAX, Power Query, Power BI Service, Fabric, or Copilot, so I would not overstate that. What I can contribute immediately is strong SQL, relational modelling, validation, advanced Excel, requirements documentation, and traceable analytical logic. I am actively prepared to build the implementation layer and can explain how I would move from a validated source through Power Query, a star schema, DAX measures, visual design, reconciliation, testing, and deployment under review.”

## Primary Technical Story — E-Commerce Sales Analytics

1. **Business question:** Understand customer, product, order, revenue, and payment performance.
2. **Model:** Customers, products, orders, line items, and payments connected through primary and foreign keys, uniqueness rules, and checks.
3. **Business rule:** Recognized revenue excludes pending, refunded, and cancelled activity.
4. **SQL analysis:** Customer spend, order frequency, product rankings, monthly revenue, and payment methods.
5. **Quality:** Repeatable validation and GitHub Actions checks.
6. **Communication:** AI-assisted insights and recommendations grounded in SQL outputs, plus Power BI KPI and dashboard planning.
7. **Boundary:** Interactive implementation is the next stage; never imply a published `.pbix` file.

## SQL Knowledge to Practise

- `INNER JOIN`, `LEFT JOIN`, and anti-join patterns; explain duplicates and null behaviour.
- `GROUP BY`, `HAVING`, conditional aggregation, and date grouping.
- CTEs, subqueries, `ROW_NUMBER`, `RANK`, running totals, and `LAG` comparisons.
- Duplicate detection, missing-value checks, referential-integrity checks, and reconciliations.
- Views as reusable logic; distinguish creating a view from managing production views.
- Query-performance concepts: selective columns, early filters, indexes, execution plans, and avoiding repeated calculations.
- Explain correctness testing versus performance tuning without claiming professional optimization ownership.

## Power BI Knowledge to Review

- **Power Query:** Connect, assign data types, clean, merge, append, reshape, and document steps.
- **Model:** Star schema, fact and dimension tables, granularity, date tables, relationships, and filter direction.
- **DAX:** Measures versus calculated columns; filter context; `CALCULATE`, `DIVIDE`, iterators, and time intelligence.
- **Visual design:** Select the chart for the question, use clear titles, reduce clutter, expose definitions, and support accessibility.
- **Testing:** Reconcile totals, test filters, blanks, dates, duplicates, edge cases, and role-specific views.
- **Service concepts:** Workspaces, publishing, refresh, permissions, lineage, deployment, and usage monitoring.

Treat these as study topics until you can build and explain them independently.

## Requirements-to-Report Method

1. Clarify the decision, users, process, source systems, metric definitions, grain, filters, refresh frequency, security, and deadline.
2. Document business rules, assumptions, exclusions, visual needs, and acceptance criteria.
3. Trace each requirement to source fields, transformations, measures, visuals, and tests.
4. Prototype with users and resolve definition disagreements early.
5. Reconcile results to trusted sources and document limitations.
6. Obtain acceptance and record post-release issues for continuous improvement.

Present this as your proposed approach, not previous UAT ownership.

## Troubleshooting a Wrong Dashboard Total

“I would first reproduce the issue and confirm the expected value, filters, refresh time, and affected users. I would then trace the number through the source, extraction, transformation, model relationships, measure logic, and visual filters. I would compare row counts and control totals at each stage, isolate the smallest failing case, and document the evidence. After correction, I would retest the original scenario and related edge cases, reconcile the result, communicate status, and add a preventive check where appropriate.”

## Data Integration and Reconciliation Concepts

- Confirm source ownership, field definitions, keys, formats, refresh timing, and expected row counts.
- Profile each source for nulls, duplicates, invalid values, and inconsistent types.
- Define mapping rules and preserve source-to-target traceability.
- Reconcile control totals before and after transformations.
- Quarantine exceptions instead of silently dropping them.
- Log errors, document decisions, and rerun tests after changes.

These are proposed practices; do not claim production integration experience.

## Fabric, Copilot, and ERP Talking Points

- **Microsoft Fabric:** An integrated analytics platform spanning data engineering, warehousing, data science, real-time workloads, and Power BI around OneLake.
- **Copilot:** Can assist with queries, measures, documentation, summaries, and exploration; outputs still require privacy, data, logic, and business validation.
- **ERP:** Supports processes such as inventory, procurement, sales, finance, and supply chain; analytics depends on understanding master data, transaction keys, timing, and business rules.

State clearly that these are concepts you are learning, not tools you have used in production.

## Likely Interview Questions

- Why SureWerx and why this Junior Data Analyst position?
- Walk us through your e-commerce data model and revenue definition.
- Explain a CTE or window function you used and why.
- How do you validate data before reporting it?
- What is your actual Power BI experience?
- How would you turn a vague request into dashboard requirements?
- How would you troubleshoot a total that differs from the source?
- How would you test a report before release?
- What is the difference between a DAX measure and calculated column?
- What do you know about Fabric, Copilot, or ERP data?
- How would you train a non-technical user on a new report?
- How do you collaborate and stay organized in a remote environment?

## STAR Evidence Bank

- **AYLA requirements:** Gathered and documented business and reporting needs.
- **AYLA data work:** Supported SQL extraction, validation, and advanced Excel reporting.
- **AYLA collaboration:** Participated in Agile planning/reviews and communicated progress.
- **Trans Globe:** Maintained records and coordinated process updates with students and institutions.
- **E-Commerce:** Relational model, revenue definition, analytical SQL, validation, recommendations, and Power BI planning.
- **Healthcare:** CTEs and window functions for rankings, segmentation, running totals, and lag comparisons.
- **HR:** Normalized workforce model and repeatable analysis of people-related measures.

Never invent volumes, time savings, stakeholder counts, accuracy percentages, or production use.

## Questions to Ask SureWerx

1. Which Power BI reports and operational areas would the junior analyst support first?
2. How are responsibilities divided between the junior analyst, Senior Business Analyst, and data or application teams?
3. Which source systems, ERP platforms, and Fabric components are currently in use?
4. What does the report lifecycle look like from requirements through testing, UAT, release, and support?
5. How does the team measure report quality, adoption, and support effectiveness?
6. What training or mentorship is available for Power BI, Fabric, integrations, and AI-assisted reporting?

## 30/60/90-Day Plan

### First 30 days

Learn SureWerx's products, operational processes, data definitions, architecture, security expectations, report inventory, support workflow, and development standards. Shadow requirements, testing, user-support, and training sessions.

### Days 31--60

Support a bounded requirement or data-quality task; reproduce and document issues; validate an existing metric; contribute SQL or Excel analysis; and complete supervised report testing and documentation.

### Days 61--90

Deliver a defined enhancement or junior-level report component under review; support UAT and rollout documentation; and propose one evidence-based validation or support-process improvement.

## Final Accuracy Guardrails

- Say `Power BI dashboard planning`, not implemented or published dashboards.
- Do not claim DAX, Power Query, Fabric, Copilot, ERP, integrations, migrations, formal UAT, training, or production support experience.
- Do not claim Canadian employment or education, work authorization, or unverified remote-work history.
- Use `Data Intern` for AYLA Solutions.
- Do not mention Tableau or IBM SPSS Statistics as skills.
