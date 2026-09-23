# Interview Preparation — Moneris Business Data Analyst (Contract)

## Candid Positioning

This is a stretch role. Lead with verified SQL, relational modelling, revenue/payment analysis, validation, reporting requirements, and Excel. State plainly that dbt, Snowflake, production BI delivery, and the requested experience duration are gaps. The winning impression is: “I understand the work, can defend my foundation, and will learn responsibly without overstating.”

## 60-Second Introduction

> I live in Toronto and completed a Master of Business Analytics at Edith Cowan University in Australia. As a Data Intern at AYLA Solutions, I gathered reporting requirements, supported SQL extraction and validation, prepared advanced Excel reports, and contributed performance insights in an Agile environment. My published PostgreSQL projects extend that foundation into e-commerce, healthcare, and workforce analytics. In the e-commerce project, I modelled orders, line items, customers, products, and payments; defined recognized revenue; analyzed payment methods and customer spend; and added repeatable validation. I have not yet used dbt or Snowflake or delivered production BI dashboards, so I see this as a stretch role. I am interested because the work aligns with how I approach analysis: clarify the business definition, build traceable SQL, validate the result, and communicate the decision clearly.

## Why Moneris

> Moneris combines Canadian payments with analytical work that affects operational and strategic decisions. I am especially interested in the discipline required around financial definitions, trusted data, upstream sources, and explainable reporting. I would contribute SQL, validation, requirements, and communication skills while learning the team's dbt, Snowflake, and BI standards under experienced guidance.

## Best Project Walkthrough

Use **E-Commerce Sales Analytics** first.

1. **Question:** How should revenue and customer/product performance be measured from transactions?
2. **Model:** Customers, products, orders, line items, and payments connected through relational keys.
3. **Definition:** Recognized revenue excludes pending, refunded, and cancelled orders.
4. **Analysis:** Customer spend, product performance, payment methods, and revenue trends.
5. **Quality:** Constraints, repeatable validation queries, and automated repository checks.
6. **Communication:** Recommendations tied to verified SQL outputs; Power BI was planned, not implemented.

Be ready to explain table grain, keys, one-to-many joins, nulls, duplicate risks, refund/cancellation treatment, and why Finance must approve revenue definitions before dashboard construction.

## SQL Questions to Practise

- `INNER JOIN` versus `LEFT JOIN`, including row loss and row multiplication.
- `WHERE` versus `HAVING`; CTEs versus subqueries.
- `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LAG`, and running totals.
- Finding duplicates at the expected business grain.
- Reconciling line-item revenue to order and payment totals.
- Handling nulls, refunds, cancellations, and late-arriving data.
- Debugging an unexpected KPI change by isolating source, transformation, definition, and filter changes.

Never claim query-tuning experience. Say:

> I have written analytical SQL with joins, aggregations, CTEs, and window functions, but production query tuning is a development area. I would inspect the execution plan, confirm predicates and join cardinality, reduce unnecessary scans and columns, review indexes or clustering with the platform owner, test on representative data, and compare runtime and correctness before release.

## Data-Quality Framework

1. **Schema:** expected columns, types, keys, allowed values, and nullability.
2. **Volume:** row counts by load date/source and unusual changes.
3. **Uniqueness:** duplicates at the declared grain.
4. **Referential integrity:** orphan facts or dimension keys.
5. **Business reconciliation:** totals by date/status/channel against an authoritative control.

When a figure looks wrong: reproduce it, confirm definition and filters, trace lineage backwards, segment the variance, compare with the source total, document the cause, correct through an approved change, and re-run validation.

## Requirements-Gathering Answer

> I would begin with the decision the stakeholder needs to make, not the requested chart. I would document the audience, KPI definition, grain, dimensions, filters, refresh need, source of truth, acceptable latency, reconciliation control, access needs, and acceptance criteria. I would show a sample or wireframe, confirm definitions in writing, and maintain a decision log for changes.

## Power BI Knowledge Without Overclaiming

- Star schemas separate dimensions used for filtering/grouping from facts used for summarization.
- Fact tables need a consistent grain; relationships and filter direction affect every measure.
- Reports should follow audience and decision, then KPIs, trends, breakdowns, and drill paths.
- Measures need explicit definitions, formats, owners, and validation controls.
- Refresh, permissions, row-level security, lineage, and monitoring matter in production.

> My completed work covers KPI definitions, relational models, page layouts, filters, and drill-path planning, but not production Power BI development or administration. I can explain the analytical design and SQL behind it, and I am actively developing hands-on implementation skill.

## dbt and Snowflake Without Overclaiming

**dbt:** SQL transformations are organized as version-controlled models with dependencies, documentation, and tests. A common structure is source/staging, intermediate transformations, then curated marts or semantic outputs. Tests can cover uniqueness, non-null values, accepted values, and relationships.

**Snowflake:** storage and compute are separated. Virtual warehouses provide compute for SQL and loading operations and can be started, stopped, or resized. Role-based access, database/schema organization, and cost-aware compute use matter.

> I have not used dbt or Snowflake professionally, so I do not meet the one-year requirement. My transferable base is relational SQL, version-controlled projects, repeatable validation, and documented transformations. I would first learn the repository structure, naming/testing conventions, deployment workflow, access controls, and review expectations, then take a bounded task under review.

## Payments Fundamentals

- **Authorization:** issuer approves or declines a purchase request; approval is not final settlement.
- **Capture/clearing:** approved transaction details are submitted for processing.
- **Settlement:** funds and related fees are calculated and transferred.
- **Refund:** merchant-initiated return tied to a previous transaction.
- **Chargeback:** disputed-transaction reversal governed by network rules and timelines.
- **Reconciliation:** matching transactions, settlements, fees, refunds, and chargebacks across sources and dates.

Possible KPIs include authorization approval rate, volume/value, average ticket, refund rate, chargeback rate, settlement variance, active merchants, and processing trends. Confirm definitions, denominators, time zones, currencies, and status logic first.

Do not claim payments-industry experience. The e-commerce and Bank of Baroda projects provide adjacent transaction-analysis exposure only.

## Hard Questions

### Why hire you despite the gaps?

> I would not position myself as equivalent to someone with several years of production Snowflake, dbt, and BI ownership. My value is an inspectable foundation: relational SQL, metric definitions, transaction and revenue analysis, validation, requirements, documentation, and communication. If you need immediate independent ownership of the full stack, I may not be the right match. If there is room for an early-career analyst who can contribute bounded analysis quickly and grow under review, I bring rigor, transparency, and follow-through.

### Have you led complex projects?

> I have supported internship analysis and independently completed structured portfolio projects, but I have not led a highly complex enterprise analytics project. I have owned a project flow from question and model through SQL, checks, documentation, and recommendations. In an enterprise setting, I would establish scope, milestones, owners, risks, validation gates, and decisions with management guidance.

## Likely Questions

- Walk me through an SQL analysis from business question to recommendation.
- How did you define and validate recognized revenue?
- How would you investigate a dashboard total that differs from Finance?
- How do you prevent duplicate rows after joins?
- What makes a KPI definition reliable?
- Tell me about gathering ambiguous reporting requirements.
- Describe your Power BI experience precisely.
- What have you done with dbt and Snowflake?
- Why should we consider you without three to five years?
- What do you know about payments and Moneris?
- How would you prioritize ad hoc requests against committed work?
- Tell me about handling sensitive information.

## STAR Evidence Bank

- **AYLA:** requirements, SQL extraction support, validation, Excel reporting, Agile reviews, documentation.
- **E-Commerce:** relational model, recognized revenue, payment-method and customer analysis, repeatable checks.
- **Bank of Baroda:** transaction cleaning, Excel/SQL analysis, visualization, recommendations.
- **Healthcare:** joins and window functions across appointments, billing, and claims.
- **HR Analytics:** normalized workforce data, KPI definitions, and validation.
- **Trans Globe:** records, workflow follow-up, research, client/institution communication.
- **Arihant:** confidential financial-services records and client support.

Never invent dataset sizes, percentages, dollar impact, stakeholder titles, production use, deadlines, or team size.

## Questions to Ask

- Which deliverables need independent ownership during the six-month contract?
- What proportion is SQL/dbt transformation, Snowflake investigation, and BI development?
- How are KPI definitions approved and reconciled with Finance or source owners?
- What does the dbt review, testing, and deployment workflow look like?
- Which BI platform and semantic-model pattern does the team use most?
- What would success look like after 30, 60, and 90 days?

## 30/60/90-Day Outline

- **30 days:** learn payment definitions, stakeholders, source lineage, dbt conventions, Snowflake roles/warehouses, BI standards, and validation controls; reproduce an existing report.
- **60 days:** own a bounded request or defect analysis, document requirements, add reviewed SQL/tests, reconcile output, and communicate findings.
- **90 days:** deliver a small reporting enhancement end to end, strengthen documentation or quality checks, and propose one evidence-based improvement.

## Official Study Sources

- Moneris job: https://moneris.wd3.myworkdayjobs.com/en-US/Moneris/job/Business-Data-Analyst--Contract-_JR105877
- Moneris card-acceptance guide: https://www.moneris.com/-/media/Moneris/Files/EN/Support/Compliance-Information/CAG_booklet.pdf
- dbt Developer Hub: https://docs.getdbt.com/
- Snowflake warehouses: https://docs.snowflake.com/en/user-guide/warehouses
- Power BI star schema: https://learn.microsoft.com/en-us/power-bi/guidance/star-schema

