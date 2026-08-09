# Junior Data Analyst — Remote Canada Interview Preparation

## Fit Reality

The junior title aligns with Jainali's career stage. The strongest direct evidence is SQL, PostgreSQL, advanced Excel, cleaning, validation, relational modelling, KPI analysis, requirements gathering, documentation, and Agile participation. The primary gap is the posting's required hands-on Power BI and DAX experience.

Do not claim:

- Completed or published interactive Power BI dashboards.
- DAX measures or calculated columns developed in a completed project.
- A `.pbix` portfolio artifact.
- One full year as a Data Analyst or BI professional.
- Production ETL pipeline ownership.
- Cloud analytics experience.
- Verified independent remote-work experience.

## 90-Second Introduction

“I completed a Master of Business Analytics at Edith Cowan University in Australia and now live in Toronto. My analyst foundation comes from my Data Intern role at AYLA Solutions, where I gathered reporting requirements, supported SQL extraction and validation, prepared advanced Excel reports, and contributed dashboard insights for performance tracking. I have also published three PostgreSQL analytics projects across e-commerce, healthcare, and workforce data. Those projects required relational modelling, complex SQL, KPI design, trend analysis, integrity rules, repeatable validation, GitHub Actions checks, and documented recommendations. I completed Power BI KPI and dashboard planning for each project, but I have not yet published an interactive dashboard or completed hands-on DAX work. I am transparent about that gap and am building the practical Power Query, star-schema, DAX, validation, and publishing skills required to move from analysis into end-to-end BI delivery.”

## Power BI Dashboard Workflow

Use this as studied knowledge until a real dashboard is completed:

1. Clarify the stakeholder, decision, reporting frequency, scope, and success criteria.
2. Inventory sources, grain, keys, owners, refresh expectations, and quality risks.
3. Use Power Query to clean, type, filter, merge, append, standardize, and reshape data.
4. Create a star schema with fact and dimension tables.
5. Use stable keys and clear one-to-many relationships; avoid ambiguous bidirectional filtering unless justified.
6. Create a dedicated date table.
7. Build explicit DAX measures for the required KPIs.
8. Design an executive summary, trends, drivers, exceptions, and detail/drill views.
9. Validate every total, filter, relationship, edge case, and refresh against a trusted source.
10. Publish, apply access controls, document definitions/ownership, gather feedback, and monitor adoption.

## DAX Fundamentals

### Measures Versus Calculated Columns

- Calculated column: evaluated row by row during refresh and stored in the model.
- Measure: evaluated at query time under the current filter context.
- Prefer measures for dynamic aggregations and KPIs; use calculated columns when a row-level stored attribute is genuinely required.

### Core Concepts

- Row context and filter context.
- Context transition through `CALCULATE`.
- Iterator functions such as `SUMX`.
- Safe division through `DIVIDE`.
- Distinct entities through `DISTINCTCOUNT`.
- Removing or preserving filters through `ALL`, `REMOVEFILTERS`, or `KEEPFILTERS`.
- Time intelligence with a proper date table.

### Example Practice Measures

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

These examples are study material, not portfolio claims.

## Power Query and ETL Concepts

- Extract: connect to source files, databases, APIs, or governed platform tables.
- Transform: standardize types, clean values, handle missing data, deduplicate, map categories, merge/append, reshape, and calculate controlled fields.
- Load: deliver validated data into the analytical model or downstream store.

Power Query preparation:

- Set data types explicitly.
- Filter unnecessary records and columns.
- Use query parameters where appropriate.
- Merge on validated keys and test join cardinality.
- Append only compatible schemas.
- Unpivot repeated period columns into tidy rows.
- Separate staging queries from business-ready queries.
- Document steps and test refresh failures.

Safe wording: “My hands-on evidence is SQL-based cleaning, transformation, modelling, and validation rather than production ETL ownership. I understand the ETL lifecycle and am practising Power Query implementation.”

## Data Modelling

- Define grain before adding columns or relationships.
- Fact tables hold measurable events; dimension tables describe entities used for filtering and grouping.
- Use surrogate/stable keys where required.
- Resolve many-to-many relationships deliberately rather than allowing accidental duplication.
- Keep dimensions conformed when multiple facts need consistent reporting.
- Document metric formulas, source fields, transformations, owners, and refresh cadence.

## Data-Quality Framework

For every source and reporting layer, test:

- Completeness: required fields and expected records.
- Validity: allowed values, ranges, formats, and types.
- Uniqueness: duplicate business keys.
- Consistency: matching definitions and categories across sources.
- Referential integrity: every foreign key has a valid parent.
- Timeliness: refresh completed before the reporting deadline.
- Reconciliation: counts and totals agree between source, model, and dashboard.

If a test fails, record the affected records, severity, owner, resolution, and re-test result.

## SQL Preparation

Practise:

- Inner/left joins and join-cardinality checks.
- CTEs and multi-stage transformations.
- `CASE` expressions and conditional aggregation.
- `ROW_NUMBER`, `RANK`, `LAG`, and running totals.
- Date grouping and comparison.
- Deduplication with deterministic survivor rules.
- Null handling and exception tables.
- Reconciliation queries and source-to-report checks.
- Reading an execution plan at a basic level.

Always explain the business grain and validation before presenting a result.

## Visualization Best Practices

- Start with the decision, not the chart type.
- Use cards for a small number of headline KPIs.
- Use line charts for time trends and bars for category comparison.
- Avoid pie charts with many categories, 3D effects, decorative gauges, and inconsistent scales.
- Use consistent colours and reserve warning colours for exceptions.
- Show units, definitions, period, filters, and last refresh.
- Provide accessible contrast and avoid relying only on colour.
- Place detail behind summaries through drill-through or tooltips.

## Remote-Work Approach

Do not claim prior remote experience. Explain the process you would use:

- Confirm priorities, deliverables, definitions, and deadlines in writing.
- Maintain a visible task/action log.
- Share early analytical checkpoints rather than waiting until final delivery.
- Document assumptions, data issues, decisions, and next steps.
- Communicate blockers early with evidence and a proposed solution.
- Protect focused work time while remaining responsive during agreed collaboration hours.
- Use version control and clear file/report ownership.

## Evidence Stories

### AYLA — Reporting Requirements and Analysis

- Situation: A reporting request needed clarification and reliable analytical support.
- Task: Help turn the business question into a structured output.
- Action: Gathered reporting requirements, supported SQL extraction and validation, prepared an advanced Excel report, and contributed dashboard insights.
- Result: Supported performance reporting and maintained reliable documentation.
- Guardrail: no invented dataset size, stakeholder count, delivery time, or quantified impact.

### E-Commerce — Modelling and KPI Quality

- Situation: Customer, order, product, line-item, and payment data needed consistent rules before analysis.
- Task: Create reliable financial and operational KPIs.
- Action: Built a normalized PostgreSQL model, added keys/uniqueness/checks, defined recognized-revenue logic, analyzed trends, and added repeatable validation and GitHub Actions checks.
- Result: Produced reproducible insights, documented recommendations, and Power BI dashboard planning.

### Healthcare — Multi-Source Analytical Logic

- Situation: Patient, clinician, appointment, treatment, billing, and claims data had to be interpreted together.
- Task: Analyze operational and financial performance.
- Action: Used CTEs and window functions for segmentation, rankings, running totals, lag comparisons, and validation.
- Result: Produced documented recommendations and Power BI planning.

### HR — Stakeholder-Oriented KPIs

- Situation: Workforce measures depended on relationships across departments, employees, salaries, performance, and attendance.
- Task: Analyze headcount, compensation, performance, attendance, hiring, and tenure.
- Action: Built a normalized model and applied CTEs, rankings, window functions, and repeatable checks.
- Result: Produced comparable KPI findings and recommendations.

## Likely Interview Questions

1. **Tell us about your Power BI experience.** State planning rather than implementation; explain the prepared end-to-end workflow.
2. **What DAX have you written?** State that hands-on DAX is not yet verified; discuss practised concepts only after completing them.
3. **How do you ensure dashboard accuracy?** Reconcile source/model/visual totals, test relationships and filters, verify refresh, document definitions, and peer-review material outputs.
4. **How would you gather reporting requirements?** Clarify user, decision, metric, grain, frequency, filters, drill-downs, source, quality, refresh, access, and acceptance criteria.
5. **Describe a difficult data problem.** Use e-commerce recognized-revenue logic or healthcare multi-table analysis.
6. **How do you communicate an insight?** Decision first, then two or three supporting facts, impact, uncertainty, recommendation, and next step.
7. **How would you work remotely?** Use the documented remote-work approach without claiming prior experience.
8. **What is your ETL experience?** Explain transferable SQL cleaning/transformation and the Power Query learning plan.
9. **What cloud platforms have you used?** State none verified; explain interest and transferable data fundamentals.
10. **Why should we choose you without completed Power BI dashboards?** Emphasize truthful SQL/modelling/quality foundations, structured dashboard planning, learning discipline, and readiness for a practical assessment—without minimizing the gap.

## Practical Case

Scenario: a Power BI revenue dashboard is 8% lower than the finance source.

Approach:

1. Confirm the metric definition, reporting period, currency, status rules, and cut-off.
2. Check refresh status and source version.
3. Reconcile row counts and revenue totals at source, Power Query output, model, measure, and visual layers.
4. Inspect excluded statuses, nulls, duplicates, joins, relationship direction, date filters, and currency logic.
5. Test whether a many-to-many relationship or filter context is suppressing or duplicating values.
6. Identify the first layer where the 8% variance appears.
7. Correct and revalidate against an independent check.
8. Communicate cause, affected reports, correction, confidence, and preventive control.

## Questions for the Interviewer

- Which dashboards and business functions would the Junior Data Analyst support first?
- What level of Power BI and DAX assessment is included in the selection process?
- Are the current data models and KPI definitions established, or would this role help design them?
- Which data sources and cloud platforms are used?
- How are dashboard quality, metric governance, and stakeholder sign-off managed?
- What would successful performance look like after 90 days?

## 30-60-90 Day Plan

- First 30 days: learn stakeholders, KPI definitions, source systems, existing models, quality controls, reporting cadence, and remote working norms; reproduce a governed analysis with review.
- Days 31–60: support SQL/Excel analysis, validate a dashboard dataset, document measures and lineage, and contribute to a reviewed Power BI enhancement.
- Days 61–90: independently own a defined analysis/report, deliver a validated dashboard component if trained and approved, and recommend one practical quality or reporting improvement.

## Final Guardrails

- Never claim Power BI dashboard implementation, DAX experience, `.pbix` files, production ETL, cloud analytics, remote experience, or one-plus years of analyst employment.
- Describe Power BI only as KPI, visualization, and dashboard planning until a completed artifact is verified.
- Retain `Data Intern` and calibrated ownership verbs.
- Never invent metrics, savings, dataset sizes, stakeholders, deadlines, or outcomes.
