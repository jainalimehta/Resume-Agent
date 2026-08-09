# AspiringIT Junior Data Analyst — Interview Preparation

## Fit Reality

This is an entry-level role, but its mandatory Power BI and DAX requirements make it a stretch application. Your strongest direct evidence is PostgreSQL, SQL, advanced Excel, cleaning, validation, relational modelling, KPI analysis, reporting requirements, documentation, and Agile participation.

Do not claim:

- Completed or published interactive Power BI dashboards.
- DAX measures or calculated columns delivered in a completed project.
- A `.pbix` portfolio artifact.
- One full year as a Data Analyst or BI professional.
- Production ETL pipeline ownership.
- Cloud analytics experience.
- Verified independent remote-work experience.

The job board's match percentages and checked Power BI/DAX tags are automated assessments, not evidence of your experience.

## 90-Second Introduction

“I completed a Master of Business Analytics at Edith Cowan University in Australia and now live in Toronto. My analyst foundation comes from my 2025 Data Intern role at AYLA Solutions, where I gathered reporting requirements, supported SQL extraction and validation, prepared advanced Excel reports, and contributed dashboard insights for performance tracking.

I have also published three PostgreSQL analytics projects covering e-commerce, healthcare, and workforce data. Those projects required relational modelling, SQL joins, CTEs and window functions, KPI definition, integrity rules, repeatable validation, GitHub Actions checks, and documented recommendations. I completed Power BI KPI, visualization, and dashboard planning for all three projects, but I have not yet published an interactive dashboard or completed verified hands-on DAX work.

AspiringIT interests me because it combines technology consulting, software, AI-powered solutions, and talent services. I can contribute strong SQL, Excel, data-quality, and reporting foundations while developing the production Power BI and DAX capability this role requires.”

## Power BI Dashboard Workflow

Use this as studied knowledge until a real dashboard is completed:

1. Clarify the stakeholder, business decision, reporting frequency, scope, and acceptance criteria.
2. Inventory sources, grain, keys, owners, refresh expectations, access requirements, and quality risks.
3. Profile each source for types, missing values, duplicates, invalid categories, and inconsistent formats.
4. Use Power Query to clean, type, filter, merge, append, standardize, and reshape data.
5. Build a star schema with clearly defined fact and dimension tables.
6. Add a dedicated date table and intentional one-to-many relationships.
7. Create explicit DAX measures for approved KPIs.
8. Design summary, trends, drivers, exceptions, and detail views around decisions.
9. Reconcile every total, filter, relationship, edge case, and refresh against trusted sources.
10. Publish, apply access controls, document metric definitions, gather feedback, and monitor usage.

## DAX Fundamentals

### Measures Versus Calculated Columns

- A calculated column is evaluated row by row during refresh and stored in the model.
- A measure is evaluated at query time under the current filter context.
- Prefer measures for dynamic aggregations and KPIs; use calculated columns when a stored row-level attribute is necessary.

### Concepts to Understand

- Row context and filter context.
- Context transition through `CALCULATE`.
- Iterator functions such as `SUMX`.
- Safe division through `DIVIDE`.
- Distinct entities through `DISTINCTCOUNT`.
- Filter modification through `ALL`, `REMOVEFILTERS`, and `KEEPFILTERS`.
- Time intelligence with a proper date table.

### Practice Measures

```DAX
Total Revenue = SUM(FactSales[Revenue])

Completed Orders =
CALCULATE(
    DISTINCTCOUNT(FactOrders[OrderID]),
    FactOrders[Status] = "Completed"
)

Completion Rate =
DIVIDE([Completed Orders], DISTINCTCOUNT(FactOrders[OrderID]))

Revenue Variance = [Total Revenue] - [Revenue Target]

Revenue Variance % = DIVIDE([Revenue Variance], [Revenue Target])
```

These examples are study material, not portfolio claims. Do not say you have implemented them unless you actually practise and verify them before the interview.

## Power Query and ETL

- **Extract:** connect to approved files, databases, APIs, or platform tables.
- **Transform:** standardize types, clean values, handle missing data, deduplicate, map categories, merge or append, reshape, and calculate governed fields.
- **Load:** deliver validated data into the analytical model or downstream store.

Power Query topics:

- Explicit data types.
- Query parameters.
- Validated merge keys and join cardinality.
- Appending compatible schemas.
- Unpivoting repeated period columns.
- Staging versus business-ready queries.
- Query folding at a conceptual level.
- Refresh failures and diagnostics.

Safe answer:

“My hands-on evidence is SQL-based cleaning, transformation, modelling, and validation rather than production ETL ownership. I understand the ETL lifecycle and am building practical Power Query capability as the next step.”

## Data Modelling

- Define the grain before creating relationships or measures.
- Fact tables hold measurable events; dimension tables describe entities used for filtering.
- Use stable keys and document relationship cardinality.
- Resolve many-to-many relationships deliberately.
- Avoid bidirectional filters unless the business case requires them and the effect is tested.
- Use conformed dimensions when multiple facts need consistent reporting.
- Document metric formula, source, grain, refresh cadence, owner, and exceptions.

## Data-Quality Framework

Test every reporting layer for:

- **Completeness:** expected records and required fields.
- **Validity:** allowed values, types, ranges, and formats.
- **Uniqueness:** duplicate business keys.
- **Consistency:** definitions and categories agree across sources.
- **Referential integrity:** foreign keys have valid parents.
- **Timeliness:** refresh completes before the reporting deadline.
- **Reconciliation:** source, model, and dashboard totals agree.

When a test fails, record affected records, severity, owner, resolution, and retest evidence.

## SQL Preparation

Practise:

- Inner and left joins with cardinality checks.
- CTEs for readable multi-stage logic.
- `CASE` and conditional aggregation.
- `ROW_NUMBER`, `RANK`, `LAG`, and running totals.
- Date grouping and period comparisons.
- Deduplication with deterministic survivor rules.
- Null handling and exception queries.
- Source-to-report reconciliation.

Example:

```sql
WITH monthly_revenue AS (
    SELECT
        DATE_TRUNC('month', order_date) AS month_start,
        SUM(recognized_revenue) AS revenue
    FROM reporting_orders
    GROUP BY 1
)
SELECT
    month_start,
    revenue,
    LAG(revenue) OVER (ORDER BY month_start) AS prior_month_revenue,
    revenue - LAG(revenue) OVER (ORDER BY month_start) AS revenue_change
FROM monthly_revenue;
```

Explain the business definition of recognized revenue before explaining the query.

## Dashboard Accuracy Investigation

Scenario: a Power BI dashboard total differs from the trusted business report.

1. Confirm metric definition, period, status rules, filters, currency, and cut-off.
2. Check source version and refresh status.
3. Compare counts and totals at source, Power Query, model, DAX measure, and visual layers.
4. Inspect nulls, duplicates, joins, relationship direction, date filters, and hidden visual filters.
5. Test whether filter context or many-to-many relationships affect the result.
6. Identify the first layer where the discrepancy appears.
7. Correct and reconcile the result against an independent query.
8. Document root cause, affected reports, resolution, and preventive control.

## Visualization Best Practices

- Start with the decision, not the chart type.
- Use a small number of clearly defined headline KPIs.
- Use line charts for time and bars for category comparison.
- Avoid 3D charts, decorative gauges, and crowded pie charts.
- Apply consistent scales and accessible colours.
- Show units, reporting period, active filters, definitions, and last refresh.
- Reserve warning colours for exceptions.
- Use drill-through or tooltips for detail rather than overcrowding summaries.
- Validate visual totals against source SQL.

## Remote-Work Answer

Do not claim prior remote experience. Say:

“I have not yet held a verified fully remote analyst role. My approach would be to confirm deliverables and acceptance criteria in writing, maintain a visible request and action log, share early checkpoints, document assumptions and decisions, and communicate blockers with evidence and suggested options. I would also use clear version control and agreed collaboration hours to keep independent work accountable.”

## STAR Stories

### AYLA — Reporting Requirements

- **Situation:** Analytical work required clear reporting needs.
- **Task:** Help turn stakeholder questions into structured outputs.
- **Action:** Gathered requirements, supported SQL extraction and validation, prepared Excel reports, and participated in Agile reviews.
- **Result:** Contributed performance-reporting insights and maintained documentation.

### E-Commerce — Revenue and KPI Quality

- **Situation:** Customer, order, product, line-item, and payment data required consistent rules.
- **Task:** Create defensible revenue and performance analysis.
- **Action:** Built a normalized PostgreSQL model, added integrity controls, defined recognized revenue, analyzed KPIs, and added repeatable validation.
- **Result:** Produced reproducible findings, recommendations, and Power BI dashboard planning.

### Healthcare — Related Data Sources

- **Situation:** Patient, clinician, appointment, treatment, billing, and claims data needed to be interpreted together.
- **Task:** Analyze operational and financial performance.
- **Action:** Modelled the relationships and used CTEs and window functions for rankings, segmentation, running totals, and lag comparisons.
- **Result:** Produced validated findings, recommendations, and Power BI planning.

### HR — Workforce KPIs

- **Situation:** Workforce measures depended on related department, employee, salary, performance, and attendance data.
- **Task:** Analyze consistent workforce metrics.
- **Action:** Built a normalized model and applied CTEs, rankings, window functions, and repeatable checks.
- **Result:** Produced comparable KPI findings and dashboard recommendations.

## Likely Interview Questions

1. Tell us about your Power BI experience.
2. What DAX measures have you written?
3. How do you validate a dashboard?
4. How would you gather reporting requirements?
5. Describe a difficult data-quality problem.
6. How do you prevent duplicate totals after a join?
7. How would you work independently in a remote environment?
8. What is your ETL experience?
9. Which cloud platforms have you used?
10. How do you translate a trend into a recommendation?
11. Why AspiringIT?
12. Why should we select you without completed Power BI dashboards?

## Answering the Main Gap

“My strongest hands-on evidence is SQL, Excel, relational modelling, KPI logic, validation, and reporting requirements. I have completed Power BI KPI, visualization, and dashboard planning for three projects, but I have not yet published an interactive dashboard or verified DAX implementation. I would not overstate that. What I bring is a reliable analytical foundation, a clear understanding of the BI delivery workflow, and the discipline to learn through tested implementation rather than superficial tool familiarity.”

## Questions for AspiringIT

- Which dashboards and business functions would this role support first?
- Is the analyst working on AspiringIT's internal reporting, client delivery, or both?
- What is the current Power BI, data-source, and cloud technology stack?
- What level of DAX assessment is included in the selection process?
- Are KPI definitions and models established, or would this analyst help develop them?
- How does the remote team manage review, validation, and release approval?
- What would successful performance look like after the first 90 days?

## 30-60-90 Day Outline

### First 30 Days

- Learn reporting consumers, source systems, KPI definitions, data lineage, and release processes.
- Reproduce selected reports and document grain, filters, ownership, refresh timing, and controls.
- Complete focused Power BI and DAX exercises using approved sample data.

### Days 31–60

- Support selected recurring reports and data-quality checks under review.
- Implement a scoped Power BI dashboard or report enhancement using approved requirements.
- Reconcile calculations and document test evidence.

### Days 61–90

- Take ownership of a defined reporting deliverable appropriate to an entry-level analyst.
- Improve one repeatable validation or documentation process.
- Present findings, limitations, business recommendations, and next actions.

## Final Guardrail

Do not try to win the interview by sounding experienced with DAX or production Power BI. Win it by showing precise SQL reasoning, disciplined validation, honest self-awareness, and a concrete plan to convert your existing dashboard designs into tested BI deliverables.
