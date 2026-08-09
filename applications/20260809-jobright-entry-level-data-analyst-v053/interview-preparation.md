# Jobright Entry-Level Data Analyst — Interview Preparation

## Your Positioning

Present yourself as an early-career analyst with a verified Data Intern foundation and hands-on SQL portfolio—not as an experienced BI developer.

Your strongest evidence:

- SQL and advanced Excel reporting support at AYLA Solutions.
- Three normalized PostgreSQL projects covering e-commerce, healthcare, and workforce analytics.
- KPI definition, business-rule documentation, trend analysis, and decision-focused recommendations.
- Repeatable validation and GitHub Actions checks.
- Reporting-requirement gathering, documentation, and Agile planning/reviews.

Your honest boundaries:

- Power BI work is KPI, visualization, and dashboard planning; no published interactive dashboard or `.pbix` yet.
- You have not used Tableau, Looker, Python, or a cloud data warehouse.
- GitHub Actions automates validation checks, not recurring business-report delivery.
- You can explain how you would work remotely, but should not claim verified remote employment.

## 90-Second Introduction

“I am a Business Analytics graduate living in Toronto, with a Master of Business Analytics from Edith Cowan University in Australia. My analyst foundation comes from my 2025 Data Intern role at AYLA Solutions, where I gathered reporting requirements, supported SQL extraction and validation, prepared advanced Excel reports, and contributed reporting insights for performance tracking.

I have also published three PostgreSQL analytics projects covering e-commerce, healthcare, and workforce data. I designed normalized relational models, defined business rules and KPIs, used joins, CTEs, rankings and window functions, and added repeatable validation with GitHub Actions. I then translated the findings into business recommendations and Power BI dashboard plans.

Jobright interests me because this role combines the areas where I am strongest—SQL, metrics, reporting logic, and data quality—with the opportunity to grow into production dashboards and reporting automation in an AI-driven product company.”

## How to Explain a Reliable Reporting System

Use this sequence:

1. Clarify the decision, audience, reporting frequency, and required level of detail.
2. Identify authoritative source systems and define the grain of each dataset.
3. Agree on metric definitions, inclusions, exclusions, time zones, and refresh rules.
4. Build reusable SQL transformations with clear names and documented assumptions.
5. Validate row counts, uniqueness, nulls, relationships, ranges, and totals.
6. Design a concise report or dashboard around decisions—not decorative visuals.
7. Reconcile results against a trusted baseline and obtain stakeholder sign-off.
8. Automate refreshes and quality checks where appropriate, then monitor failures.
9. Maintain a metric dictionary, change log, ownership, and escalation path.

## Metric Definition Example

Use your e-commerce project:

“Revenue could be overstated if pending, refunded, or cancelled orders were included. I defined recognized revenue using eligible transaction statuses, documented the rule, joined the relevant order, line-item, and payment data, and validated the output before using it in monthly revenue and customer-spend analysis. This illustrates why a metric needs an agreed business definition, not only a SQL expression.”

Be ready to discuss:

- Metric name and business purpose.
- Formula and dataset grain.
- Inclusion and exclusion rules.
- Date field and reporting period.
- Null, duplicate, cancellation, and refund treatment.
- Owner, refresh frequency, and validation checks.

## SQL Topics to Practise

### Joins and Grain

Explain how a one-to-many join can duplicate totals. State the grain before joining and aggregate at the correct level.

### CTEs

Use CTEs to separate extraction, cleaning, metric logic, and final presentation. They improve readability and testing; they do not automatically improve performance.

### Window Functions

Practise:

```sql
SELECT
    month_start,
    revenue,
    LAG(revenue) OVER (ORDER BY month_start) AS prior_month_revenue,
    revenue - LAG(revenue) OVER (ORDER BY month_start) AS revenue_change,
    SUM(revenue) OVER (ORDER BY month_start) AS running_revenue
FROM monthly_revenue;
```

Explain that `LAG` compares periods without collapsing rows, while the running sum shows cumulative performance.

### Duplicate and Null Checks

```sql
SELECT business_key, COUNT(*)
FROM reporting_dataset
GROUP BY business_key
HAVING COUNT(*) > 1;
```

```sql
SELECT
    COUNT(*) AS row_count,
    SUM(CASE WHEN required_field IS NULL THEN 1 ELSE 0 END) AS missing_required
FROM reporting_dataset;
```

### Reconciliation

Compare source and output counts, totals, distinct business keys, and status distributions. Investigate differences before release.

## Data-Quality Investigation Framework

If a dashboard number suddenly changes:

1. Confirm the exact metric, period, segment, and expected result.
2. Check whether the definition or dashboard filter changed.
3. Verify source freshness and pipeline/run status.
4. Compare row counts and totals at each transformation stage.
5. Test nulls, duplicates, key integrity, and unexpected categories.
6. Isolate the first stage where the discrepancy appears.
7. Correct the logic or data issue and rerun validation.
8. Document root cause, impact, resolution, and prevention.

Never say that a report is correct because the query ran successfully.

## Reporting Automation — Study Framework

You have not built a production recurring-report workflow. If asked, answer transparently:

“My verified automation experience is repeatable data validation through GitHub Actions. For recurring reporting, I understand the design principles and would begin by separating SQL transformation logic from presentation, scheduling refreshes through the organization’s approved platform, adding freshness and reconciliation checks, logging failures, and defining an owner and recovery procedure. I am actively building deeper hands-on capability in this area.”

Key concepts to study:

- Scheduled refresh and dependency ordering.
- Idempotent transformations.
- Logging, alerts, retries, and failure ownership.
- Data freshness and completeness tests.
- Version control and change management.
- Distribution permissions and sensitive-data controls.

## Dashboard and BI Questions

If asked about Power BI:

“I have completed KPI, visualization, and dashboard planning for all three portfolio projects, including intended audiences, business questions, measures, and layouts. I have not yet published an interactive dashboard or `.pbix`, so I would not describe myself as having production Power BI experience. My next step is implementing those plans while applying the SQL and validation foundation I already have.”

Good dashboard principles:

- Start with the business decision and audience.
- Use a small number of clearly defined KPIs.
- Show trends and comparisons with consistent scales.
- Keep filters purposeful and visible.
- Use colour sparingly and accessibly.
- Display refresh timing and definitions.
- Validate dashboard totals against source queries.

## Remote Request Management

Do not claim prior remote employment. Explain your method:

- Capture each request with owner, purpose, scope, due date, dependencies, and acceptance criteria.
- Confirm priority when deadlines conflict.
- Break delivery into checkpoints and communicate risks early.
- Maintain an action log and concise written updates.
- Document definitions and decisions so work is not dependent on meetings.
- Protect focused analysis time while remaining responsive to urgent issues.

Sample answer:

“I have not yet held a verified fully remote analyst role. My approach would be to make priorities and decisions visible through a request tracker, confirm acceptance criteria early, provide concise progress updates, and escalate conflicts with options rather than waiting until a deadline is at risk.”

## STAR Stories to Prepare

### 1. Defining Accurate Revenue

- **Situation:** E-commerce activity included statuses that should not count as recognized revenue.
- **Task:** Create defensible revenue logic for downstream analysis.
- **Action:** Defined exclusions, joined the required tables, applied business rules, and validated results.
- **Result:** Produced a consistent basis for revenue, customer, product, and monthly analysis.

### 2. Complex Healthcare Analysis

- **Situation:** Operational data spanned patients, clinicians, appointments, treatments, billing, and claims.
- **Task:** Structure the data for interpretable operational analysis.
- **Action:** Modelled relationships and used CTEs and window functions for rankings, segments, running totals, and lag comparisons.
- **Result:** Produced validated findings and decision-focused recommendations.

### 3. Reporting Requirements at AYLA

- **Situation:** Analytical work required clear business and reporting needs.
- **Task:** Support accurate, useful reporting outputs.
- **Action:** Gathered and documented requirements, supported SQL extraction and Excel reporting, and participated in Agile reviews.
- **Result:** Contributed structured reporting insights for performance tracking.

### 4. Protecting Record Accuracy

- **Situation:** Earlier administrative roles involved sensitive client and application records.
- **Task:** Keep information accurate while coordinating updates.
- **Action:** Maintained documentation, tracked process changes, and communicated with relevant parties.
- **Result:** Supported reliable operational records and workflows without inventing a numerical outcome.

## Likely Questions

1. How would you define a company-wide KPI?
2. How do you prevent duplicate totals after joining tables?
3. How would you validate a recurring report before distribution?
4. Describe a data-quality issue you investigated.
5. When would you use a CTE or window function?
6. How do you turn an ambiguous business request into a reporting specification?
7. How would you prioritize several remote reporting requests?
8. What would you automate first in a manual reporting process?
9. What is your current Power BI experience?
10. How have you used AI in analytical work?
11. Why Jobright and why an AI-driven job-search product?
12. What would you aim to learn in your first 90 days?

## Answering the AI Question

Say:

“In my portfolio, I used Generative AI to support interpretation and recommendation drafting after validating the SQL outputs. The recommendations remained grounded in the query results and documented business rules. I have not built production AI agents, but I am interested in learning how reliable data models, metrics, and monitoring support AI-product decisions.”

## Questions to Ask Jobright

- Which business metrics are least standardized today?
- What are the main data sources and current reporting stack?
- How are reporting requests prioritized and governed in the remote team?
- What data-quality failures create the most operational friction?
- What would successful ownership look like after 30, 60, and 90 days?
- How does the analytics function partner with product and AI-agent teams?

## 30-60-90 Day Outline

### First 30 Days

- Learn Jobright’s product, reporting consumers, source systems, metric definitions, and request process.
- Reproduce key reports and document data lineage, grain, owners, refresh timing, and existing controls.
- Resolve small ad hoc requests while learning review and release expectations.

### Days 31–60

- Take ownership of selected recurring reports and their validation checklist.
- Identify duplicate logic, unclear definitions, manual steps, and common quality issues.
- Propose a metric dictionary or reporting-standard improvement with stakeholder input.

### Days 61–90

- Deliver one scoped improvement to a recurring dataset or report.
- Add documented quality checks and a clear support procedure.
- Present findings, business impact, limitations, and next recommendations.

## Final Guardrail

The objective is not to sound experienced with every preferred tool. It is to show that your SQL, relational modelling, validation, reporting logic, and learning discipline make you a credible entry-level hire who can grow into Jobright’s production BI environment.
