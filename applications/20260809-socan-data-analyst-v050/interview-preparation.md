# SOCAN — Data Analyst Interview Preparation

## Candidacy Reality

This is a significant technical stretch. SOCAN requests at least two years using Databricks or similar technology, intermediate Python, strong SQL, and an understanding of Spark/distributed computing. Jainali has strong SQL and data-quality foundations but no verified Databricks, Python, Spark, Lakehouse, Genie, or semantic-layer experience. The interview strategy is to be technically prepared, demonstrate fast learning, and never misrepresent hands-on experience.

## 90-Second Introduction

“I completed a Master of Business Analytics at Edith Cowan University in Australia and now live in Toronto. My analyst foundation comes from a Data Intern role at AYLA Solutions, where I gathered reporting requirements, supported SQL extraction and validation, prepared advanced Excel reports, and contributed dashboard insights for performance tracking. I have also published three PostgreSQL analytics projects across e-commerce, healthcare, and workforce data. Those projects required normalized models, complex SQL, KPI design, trend analysis, repeatable validation, GitHub Actions checks, documented recommendations, and Power BI dashboard planning. SOCAN interests me because accurate data directly supports fair royalty outcomes for music creators. I have not yet worked hands-on with Databricks, Python, or Spark, so I am approaching those requirements transparently. My SQL, modelling, validation, documentation, and Agile foundations give me a strong base from which to learn that stack quickly.”

## Why SOCAN

- SOCAN licenses music use, collects revenue, matches usage and rights information, and distributes royalties to eligible creators and publishers.
- Data accuracy has a direct human outcome: attribution and distribution errors can affect whether creators receive fair compensation.
- SOCAN's careers materials describe modernization of music monetization through innovative technology and support professional learning.
- The role combines SQL, data quality, KPI interpretation, documentation, cross-functional work, and modern cloud analytics.

## Music-Royalty Data Concepts

Potential entities in a simplified rights-management model:

- Works: songs or compositions and their identifiers.
- Creators and publishers: parties with ownership or representation interests.
- Rights/splits: ownership percentages, territories, effective dates, and rights types.
- Usage: streams, broadcasts, performances, reproductions, channels, dates, and territories.
- Licences/tariffs: authorized uses, rates, rules, and reporting periods.
- Matches: links between usage records and registered works/rightsholders.
- Distributions: calculated royalties, deductions, holds, adjustments, and payment status.

Important quality dimensions:

- Completeness: are required usage and ownership fields present?
- Validity: do identifiers, dates, percentages, and codes meet rules?
- Uniqueness: are duplicate works or usage events inflating results?
- Consistency: do titles, names, territories, and rights agree across sources?
- Referential integrity: does every usage/distribution record connect to a valid work and party?
- Timeliness: did data arrive before the distribution cut-off?
- Reconciliation: do licensed amounts, calculated pools, and paid distributions balance under approved rules?

## Databricks, Spark, and Lakehouse Fundamentals

Use these as studied concepts, never as prior experience.

### Databricks

A collaborative analytics platform built around Apache Spark. It commonly combines notebooks, SQL, workflows, data engineering, machine learning, governance, and BI capabilities.

### Spark

A distributed processing engine that divides large computations across a cluster. Key concepts:

- Driver coordinates work; executors process partitions.
- Transformations are lazy until an action triggers execution.
- Narrow transformations can be cheaper; wide transformations cause shuffles.
- Partitioning, data skew, unnecessary shuffles, and repeated scans affect performance.
- DataFrames provide structured, optimized operations.

### Lakehouse

A platform pattern combining flexible data-lake storage with warehouse-style reliability, performance, governance, and SQL analytics.

### Delta Lake

Common Databricks table layer supporting ACID transactions, schema enforcement/evolution, version history, and reliable batch/stream processing.

### Medallion Pattern

- Bronze: raw ingested data with source fidelity.
- Silver: cleaned, standardized, deduplicated, validated, and conformed data.
- Gold: business-ready aggregates, KPIs, semantic views, and reporting datasets.

### Semantic Layer and Genie

A semantic layer gives business-friendly names, definitions, relationships, measures, and governance over physical tables. For natural-language querying, reliable synonyms, descriptions, certified measures, join paths, filters, and example questions help users obtain consistent answers. Always validate generated answers against governed metrics and source queries.

## SQL Topics to Practise

- Joins and grain: prevent many-to-many duplication.
- CTEs and subqueries: organize multi-stage transformations.
- Window functions: `ROW_NUMBER`, `RANK`, `LAG`, rolling totals, and cohort comparisons.
- Conditional aggregation: KPI numerators, denominators, and status-based totals.
- Deduplication: define the business key and deterministic survivor rule.
- Null handling: distinguish missing, not applicable, zero, and unknown.
- Date logic: reporting periods, effective dates, late arrivals, and cut-offs.
- Reconciliation queries: compare counts and totals between stages.
- Exception queries: identify unmapped usage, invalid splits, duplicates, and orphan records.
- Performance concepts: filter early where appropriate, select needed columns, inspect plans, reduce repeated work, and understand partitions.

## Python Study Plan

Do not claim intermediate Python before completing hands-on practice. Prepare:

- Core syntax: variables, collections, loops, functions, comprehensions, exceptions, and modules.
- pandas: reading data, selecting/filtering, joins, groupby, missing values, type conversion, duplicates, reshaping, and validation.
- PySpark equivalents: `select`, `filter`, `withColumn`, `groupBy`, joins, windows, and null handling.
- Reproducibility: parameterized functions, assertions, logging, comments, and version control.
- Testing: expected schema, row counts, uniqueness, allowed values, ranges, referential integrity, and reconciled totals.

Safe interview wording: “My hands-on programming evidence is SQL rather than Python. I understand the role requires intermediate Python, and I am actively building that capability through data-cleaning, transformation, and validation exercises before representing it as proficiency.”

## Data-Quality Test Plan

For a royalty-usage pipeline:

1. Confirm source, destination, grain, key fields, and reporting cut-off.
2. Validate schema, types, required fields, formats, and accepted values.
3. Test uniqueness at the defined business key.
4. Check referential integrity across works, parties, licences, usage, and distributions.
5. Validate ownership splits and effective-date rules.
6. Reconcile row counts and financial/usage totals between pipeline stages.
7. Compare current distributions with historical ranges and expected seasonality.
8. Route failed records to an exception table with reason and owner.
9. Document thresholds, severity, resolution, and re-test results.
10. Monitor recurring failures and address their root cause upstream.

## Pipeline Discrepancy Framework

If a dashboard total differs from the source:

1. Pause publication if the difference could affect decisions or payments.
2. Confirm metric definition, grain, filters, time zone, and refresh time.
3. Reconcile counts and totals at source, Bronze, Silver, Gold, semantic, and dashboard layers.
4. Identify the first layer where values diverge.
5. Test duplicates, missing records, join multiplication, late arrivals, schema changes, nulls, mapping changes, and stale caches.
6. Correct and reprocess using controlled procedures.
7. Assess downstream impact and communicate affected reports/decisions.
8. Add a preventive test and document the resolution.

## KPI Root-Cause Analysis

When a KPI changes unexpectedly:

1. Validate the metric and data before interpreting it.
2. Quantify the change versus prior period, plan, and normal range.
3. Segment by source, channel, territory, rights type, creator/publisher cohort, and time.
4. Decompose numerator and denominator.
5. Examine mix, volume, rate, timing, late-arriving data, policy, mapping, and quality effects.
6. Use a comparison cohort or historical baseline where appropriate.
7. Identify the smallest number of drivers explaining most of the movement.
8. State confidence, uncertainty, impact, recommendation, and monitoring plan.

## Dashboard and Semantic-Layer Design

Before building:

- Identify the user, decision, frequency, and required action.
- Define certified KPIs, dimensions, filters, drill paths, and refresh expectations.
- Confirm data lineage and ownership.
- Use an executive summary, trend, driver decomposition, exceptions, and detail view.
- Provide definitions and last-refresh information.
- Test totals, filters, role access, edge cases, and performance.
- Track adoption and whether the dashboard changes decisions.

State accurately: Jainali has completed Power BI KPI and dashboard planning, not interactive implementation.

## Evidence Stories

### AYLA — Reporting Requirements and Validation

- Situation: An analytical request required reporting clarification and reliable preparation.
- Task: Support a structured reporting output.
- Action: Gathered requirements, supported SQL extraction and validation, prepared an advanced Excel report, and communicated progress through Agile planning/reviews.
- Result: Contributed reporting insights and maintained reliable documentation.
- Guardrail: no invented dataset size, stakeholder count, delivery time, or quantified impact.

### E-Commerce — Quality Rules and KPI Analysis

- Situation: Related order/payment data required defensible revenue logic.
- Task: Create reliable customer, product, payment, and monthly KPIs.
- Action: Built a normalized PostgreSQL model; added keys, uniqueness rules, checks, recognized-revenue logic, repeatable validation, and GitHub Actions checks; documented recommendations.
- Result: Produced reproducible SQL analysis with clear business rules.

### Healthcare — Multi-Table Trends

- Situation: Patient, appointment, treatment, billing, clinician, and claims data had to be interpreted together.
- Task: Analyze operational and financial performance.
- Action: Used CTEs and window functions for segmentation, rankings, running totals, lag comparisons, and automated validation.
- Result: Produced documented insights, recommendations, and Power BI planning.

### HR — Consistent Workforce Metrics

- Situation: Workforce metrics depended on consistent joins across five subject areas.
- Task: Analyze headcount, compensation, performance, attendance, hiring, and tenure.
- Action: Built a normalized model, applied SQL analytical functions, and added repeatable validation.
- Result: Created comparable KPI findings and recommendations.

## Likely Interview Questions

1. **Why SOCAN?** Connect fair creator compensation with accurate data, modern technology, and meaningful analytical work.
2. **Tell us about your SQL experience.** Use all three projects; explain grain, relationships, business rules, CTEs/window functions, and validation.
3. **How would you investigate a KPI fluctuation?** Use the root-cause framework above.
4. **How do you ensure data quality?** Define dimensions, implement tests, reconcile stages, quarantine exceptions, document ownership, and prevent recurrence.
5. **Describe a loosely defined problem.** Use AYLA requirements gathering; explain clarifying the decision, metric, scope, deadline, and output.
6. **How would you prioritize ad hoc requests?** Assess business impact, urgency, deadline, risk, dependencies, and effort; confirm trade-offs and communicate status.
7. **What is your Databricks experience?** Say none hands-on; explain studied concepts and how SQL/modelling/testing foundations transfer.
8. **What is your Python level?** Be direct that it is not yet verified; discuss the concrete learning plan.
9. **How would you document a semantic layer?** Cover business definitions, measures, dimensions, joins, grain, synonyms, lineage, owners, permissions, and validated examples.
10. **How do you communicate technical findings?** Lead with decision and impact, then evidence, risk/uncertainty, recommendation, and next step.

## Practice Case

Scenario: reported digital-streaming royalties for one distribution period are materially lower than expected.

Approach:

1. Confirm the KPI definition, comparison baseline, affected rights, territories, and cut-off.
2. Validate total usage, matched usage, licence revenue, distributable pool, and paid amount.
3. Reconcile records through ingestion, cleaned/conformed tables, allocation logic, and reporting.
4. Segment by source platform, territory, rights type, work, publisher/creator cohort, and status.
5. Check late files, schema changes, mapping failures, duplicates, unmatched works, ownership conflicts, rate changes, holds, and timing.
6. Quantify the main drivers and distinguish true business movement from data issues.
7. Provide a concise finding, confidence level, affected population, financial/operational risk, and recommended action.
8. Add monitoring or tests to prevent recurrence.

## Questions for the Interviewer

- Which reporting and Lakehouse initiatives would this analyst support first?
- What are the most important data-quality risks in SOCAN's analytics environment?
- How are KPI definitions and semantic-layer changes governed across departments?
- What balance of SQL, Python, Databricks notebooks, and AI/BI dashboard work is expected?
- What learning support is available for analysts developing deeper Spark and Databricks expertise?
- What would excellent performance look like after 90 days?

## 30-60-90 Day Plan

- First 30 days: learn royalty-domain definitions, stakeholders, data lineage, Databricks workspace standards, KPI catalogue, reporting cadence, and existing tests; reproduce a governed analysis with guidance.
- Days 31–60: support ad hoc SQL analysis, document a KPI or semantic subject area, investigate a discrepancy, and add or refine a reviewed data-quality test.
- Days 61–90: independently own a defined report/analysis, contribute to a dashboard or semantic-layer improvement, and recommend one evidence-based quality or process enhancement.

## Final Guardrails

- Never claim Databricks, Python, Spark, Lakehouse, Genie, semantic-layer, or distributed-compute experience.
- Never claim two years of analyst employment or large-scale dataset experience.
- Never claim implemented Power BI dashboards; say KPI/dashboard planning.
- Never claim French proficiency or a personal passion for music without new confirmation.
- Keep AYLA language at `supported`, `contributed`, and `participated` and retain the exact title `Data Intern`.
- Never invent metrics, dataset sizes, stakeholders, turnaround times, or outcomes.

## Official Research Sources

- SOCAN Careers: https://www.socan.com/about/careers/
- SOCAN Rights Management: https://www.socan.com/about/rights-management/
- SOCAN Music Creators: https://www.socan.com/about/music-creator/
- SOCAN Governance: https://www.socan.com/about/governance/
- SOCAN Inclusion and Anti-Racism: https://www.socan.com/inclusion-and-antiracism/
