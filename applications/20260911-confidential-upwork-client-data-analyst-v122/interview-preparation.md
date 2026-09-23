# Interview Preparation — Confidential Upwork Client Data Analyst

## Candid Fit Assessment

The posting is broad and does not identify its data sources, dashboard platform, industry, deliverables, or reporting cadence. Jainali directly matches data interpretation, SQL-based transformation, validation, advanced Excel reporting, requirements gathering, and business KPI analysis. Dashboard building is only adjacent evidence because the verified Power BI work is planning, not a published interactive dashboard.

The client labels the role intermediate and expects more than 30 hours per week for at least six months. Do not confirm schedule, duration, rate, or contract-to-hire interest until Jainali has reviewed her real availability and the engagement terms.

## 90-Second Introduction

> I am a business analytics graduate living in Toronto, with a Master of Business Analytics from Edith Cowan University in Australia. As a Data Intern at AYLA Solutions, I gathered reporting requirements, supported SQL extraction and validation, prepared advanced Excel reports, and contributed reporting insights for performance tracking. My published PostgreSQL portfolio covers e-commerce, healthcare, and workforce analytics. Across those projects, I built relational models, applied business rules, transformed data with joins, CTEs, and window functions, analyzed KPIs and trends, and added repeatable validation and GitHub Actions checks. I have completed detailed Power BI dashboard planning, although interactive dashboards are not yet published. My strongest value is converting an unclear business question into defined metrics, validated analysis, and an understandable report.

## Discovery Questions for the Client

Ask these before committing to scope or delivery dates:

- What business decisions should the first reports support?
- Which departments and stakeholders will consume them?
- What are the data sources: spreadsheets, CSV files, databases, APIs, CRM, ERP, or another system?
- How much historical data exists, how often does it change, and who owns it?
- Which dashboard/reporting platform is required?
- Are KPI definitions already approved, or should the analyst facilitate definition?
- What are the expected deliverables, update cadence, access controls, and acceptance criteria?
- Is the work primarily recurring reporting, one-time analysis, dashboard development, or data-pipeline maintenance?
- What time-zone overlap and meeting cadence are required?
- How will hourly work, milestones, revisions, and contract-to-hire evaluation be handled?

## Data Transformation Framework

1. Clarify the business question, audience, decision, and definition of success.
2. Inventory sources, owners, refresh timing, keys, access restrictions, and known issues.
3. Profile columns, types, ranges, categories, nulls, duplicates, invalid values, and outliers.
4. Define the target grain before joining or aggregating.
5. Clean and standardize dates, text, units, categories, identifiers, and missing-value handling.
6. Join sources carefully and compare row counts after each step to detect multiplication or loss.
7. Derive approved business fields and KPIs with documented rules.
8. Reconcile counts and totals to source/control figures and test boundary cases.
9. Produce a repeatable transformation with clear assumptions and version-controlled logic.
10. Obtain stakeholder review before treating the output as final.

## Data Interpretation Framework

Move from description to action:

- **What happened?** Trend, variance, mix, volume, distribution, and exceptions.
- **Where did it happen?** Department, customer, product, geography, channel, or time period.
- **What may explain it?** Segment drivers, timing, process changes, data-quality issues, or confounding factors.
- **How confident are we?** Completeness, sample size, missing data, measurement definitions, and alternative explanations.
- **What should happen next?** Specific decision, experiment, investigation, or operational follow-up.

Do not call correlation causation. Separate a verified finding from a possible explanation.

## Dashboard Requirements Checklist

- audience and decisions;
- KPI name, formula, numerator, denominator, inclusions, exclusions, and owner;
- grain, dimensions, filters, drill-downs, targets, and comparison periods;
- authoritative source, refresh schedule, latency, and data-quality status;
- visual hierarchy, chart purpose, labels, units, and accessibility;
- permissions, exports, mobile/desktop use, and distribution;
- acceptance tests, reconciliation examples, owner, and change process.

### Honest dashboard answer

> I have completed KPI, visualization, filter, and Power BI dashboard planning for my three published projects, but I have not yet published interactive dashboards or `.pbix` files. My strongest hands-on foundation is PostgreSQL, SQL, relational modelling, validation, advanced Excel, and report requirements. I would want to understand your required platform and expected ownership before confirming the dashboard scope.

## SQL Topics to Defend

- inner versus left joins and how one-to-many joins can duplicate measures;
- `GROUP BY`, conditional aggregation, and distinct counts;
- CTEs for readable multi-step transformations;
- `ROW_NUMBER`, `RANK`, and `DENSE_RANK` distinctions;
- running totals and `LAG` for period comparisons;
- primary keys, foreign keys, uniqueness rules, and checks;
- null handling and why replacing null with zero may change meaning;
- defining recognized revenue by valid business status;
- validation queries for duplicates, missing references, invalid states, and control totals.

## Portfolio Story: E-Commerce Sales Analytics

> I modelled customers, products, orders, line items, and payments in PostgreSQL. The first analytical challenge was defining recognized revenue so pending, refunded, and cancelled activity would not be counted as earned sales. I used keys and checks to strengthen integrity, analyzed monthly revenue, customer spend, order frequency, product rankings, and payment methods, and added repeatable validation and GitHub Actions checks. I then documented AI-assisted business recommendations based on the validated SQL outputs and planned the KPIs and layout for Power BI.

Be ready to open the repository and explain the schema, one query, one validation check, one finding, and one limitation. Do not invent scale or business impact.

## Likely Interview Questions

- Walk me through a data transformation you completed.
- How do you validate a report before sharing it?
- How do you turn an unclear request into reporting requirements?
- Tell me about a trend you identified and how you interpreted it.
- How would you combine performance data from several departments?
- What is your dashboard-building experience?
- How do you handle inconsistent spreadsheet categories or missing values?
- Explain a CTE or window function you used.
- What would you do if a dashboard total did not match the source?
- How would you manage recurring reports and urgent ad-hoc requests?
- What documentation would you provide at handoff?
- Are you available for more than 30 hours weekly and at least six months?
- What hourly rate and time-zone overlap do you propose?

## STAR Story Plan

- **AYLA:** requirements, SQL extraction support, validation, advanced Excel reporting, Agile communication, and documentation.
- **E-Commerce Sales Analytics:** relational model, revenue definition, KPI analysis, checks, interpretation, and reporting plan.
- **Healthcare Patient & Hospital Analytics:** multi-entity model, CTE/window transformations, operational measures, and validation.
- **HR Analytics:** departmental workforce model and analysis across headcount, compensation, performance, attendance, hiring, and tenure.
- **Trans Globe:** accurate documentation, workflow updates, reporting support, and external-party communication.
- **Arihant:** reliable and confidential records in investment-services operations.

## Accuracy Guardrails

- Use `Data Intern` for AYLA Solutions.
- Do not claim an intermediate-level analyst employment history.
- Describe Power BI only as KPI/dashboard/visualization planning.
- Do not claim interactive dashboards, `.pbix` files, production deployment, refresh administration, or dashboard maintenance.
- Do not claim Python, R, Tableau, SPSS, cloud platforms, APIs, ERP/CRM systems, or unverified source tools.
- Do not claim freelance dates, clients, deliverables, outcomes, or remote-work history.
- Do not invent dataset sizes, percentages, turnaround time, savings, revenue impact, stakeholder counts, or department counts.
- Confirm availability, duration, hourly rate, time-zone overlap, work authorization, and contract-to-hire interest personally.

