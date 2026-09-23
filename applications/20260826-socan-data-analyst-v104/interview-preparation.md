# SOCAN Data Analyst — Interview Preparation

Prepared for Jainali Mehta | Toronto, Ontario | August 26, 2026

## Candidacy Strategy

This is a stretch application. Your strongest evidence is SQL/PostgreSQL analysis, relational modelling, repeatable validation, KPI-oriented projects, reporting requirements, advanced Excel, documentation, and Agile participation. Your material gaps are the posting's requested two-plus years with Databricks or similar technology, intermediate Python, Spark/distributed compute, Databricks AI/BI dashboard implementation, semantic-layer curation, and Genie.

Do not disguise those gaps. Win credibility by showing that you understand the work, can defend your existing projects deeply, and have a precise learning plan. Never describe planned Power BI dashboards as built or published.

## 60-Second Introduction

> I recently completed a Master of Business Analytics at Edith Cowan University in Australia and now live in Toronto. My analyst foundation comes from my Data Intern role at AYLA Solutions, where I gathered reporting requirements, supported SQL extraction and validation, prepared advanced Excel reports, and participated in Agile planning and reviews. I have also built published PostgreSQL projects across e-commerce, workforce, and healthcare data. Those projects required relational modelling, business-rule validation, KPI analysis, window functions, and translating results into recommendations and dashboard plans. SOCAN interests me because analytics directly supports accurate decisions in a business that helps creators and publishers receive royalties. My current strength is disciplined SQL analysis and data quality. My next development area is applying that foundation in Databricks, Python, Spark, and AI/BI, and I can explain the concrete learning and validation approach I would use.

Keep this to roughly one minute. Speak naturally; do not memorize it word for word.

## What SOCAN Does and Why Data Matters

SOCAN licenses music use and collects and distributes royalties to creators, publishers, members, and clients. It administers performing and reproduction rights and works internationally with other copyright collectives. Its official material describes music uses that include radio, television, streaming, live performance, background music, downloads, CDs, and vinyl.

An analyst should therefore expect data concepts such as musical works, rightsholders, ownership shares, licenses, usage/performance records, territories, distribution periods, royalty streams, payments, and adjustments. Treat this as a conceptual model, not a claim about SOCAN's internal schema.

Why quality matters: a missing identifier, duplicate usage record, invalid ownership share, unmatched work, incorrect effective date, or late source feed can affect analysis and potentially downstream reporting or distribution decisions. Never say that one dashboard directly determines royalty payments unless SOCAN confirms the process.

Official background:

- SOCAN overview: https://www.socan.com/
- Rights management: https://www.socan.com/about/rights-management/
- Music creator information: https://www.socan.com/about/music-creator/

## Your Best Evidence Stories

### 1. E-Commerce Sales Analytics — closest fit

Use this for SQL, data modelling, financial logic, quality testing, KPI trends, and stakeholder-ready findings.

Situation: Transaction data needed a consistent model and a defensible definition of recognized revenue.

Task: Connect customers, products, orders, line items, and payments; establish business rules; calculate decision-ready measures.

Action: Built a PostgreSQL relational model with keys and checks. Used joins, CTEs, aggregation, rankings, and window functions. Excluded pending, refunded, and cancelled activity from recognized revenue. Added repeatable validation and GitHub Actions checks. Analyzed monthly revenue, customer spend, order frequency, product rankings, and payment methods.

Result: Produced a traceable analytical workflow and recommendations grounded in validated outputs. Dashboard work was planned, not implemented.

Defence questions to prepare:

- Why did you exclude each status from recognized revenue?
- Could a partially refunded order require different logic?
- How did you avoid double counting after joining order and payment tables?
- Which constraints and validation queries did you use?
- How would you reconcile aggregate revenue to a source total?
- What would change if late-arriving transactions updated a prior month?

### 2. HR Analytics — KPI and time-based analysis

Use this for KPI definitions, segmentation, rankings, running totals, lag comparisons, and interpreting changes over time.

Explain the grain of each table before describing a KPI. Distinguish headcount at a point in time from hires during a period. Explain why definitions, date logic, and missing values matter.

### 3. Healthcare Analytics — complex operational relationships

Use this for relational modelling across patients, clinicians, appointments, treatments, billing, and claims. Emphasize careful join logic, operational measures, validation, and confidentiality awareness. Do not claim healthcare-industry employment or production scale.

### 4. AYLA Solutions — business-facing delivery

Use this for reporting requirements, SQL-supported extraction and validation, Excel reporting, stakeholder clarification, documentation, progress updates, and Agile planning/reviews. Do not add metrics, dataset sizes, tools, ownership, or outcomes that are not in the resume.

## Requirement-Gathering Framework

When asked how you handle a loosely defined request, use this sequence:

1. Clarify the decision: “What decision will this analysis support?”
2. Identify the audience and required timing.
3. Define the metric, grain, filters, date logic, comparison period, and exclusions.
4. Identify source systems, owners, refresh frequency, and known limitations.
5. Agree on acceptance criteria and a sample output.
6. Profile and validate the data before analysis.
7. Share an early result with assumptions clearly labelled.
8. Reconcile, obtain sign-off, document, and monitor after release.

Strong phrase: “I would not begin with the visualization. I would first confirm the decision, metric definition, grain, and source-of-truth.”

## Data Quality Test Plan

Organize tests into six groups:

| Test group | Example | Why it matters |
|---|---|---|
| Schema | Expected columns, types, nullability | Detects structural change |
| Uniqueness | One row per declared key/grain | Detects duplicates |
| Completeness | Required identifiers and dates populated | Prevents unusable records |
| Validity | Allowed status values; non-negative amounts | Enforces business rules |
| Referential integrity | Every usage record maps to a valid parent when required | Detects broken relationships |
| Reconciliation | Row counts and totals compared with source/control totals | Confirms end-to-end consistency |

For a Lakehouse project, add freshness, volume-drift, distribution-drift, and transformation tests between layers. Define alert thresholds with business and engineering owners; do not invent thresholds alone.

## Root-Cause Analysis of a KPI Change

Use this interview answer structure:

1. Confirm the KPI definition did not change.
2. Check freshness, completeness, duplicates, joins, and filters.
3. Reconcile the current period with source/control totals.
4. Locate when the change began.
5. Segment by source, category, territory, channel, status, and other relevant dimensions.
6. Separate numerator, denominator, and mix effects.
7. Compare with seasonality, prior periods, known releases, and operational events.
8. Reproduce the result independently where possible.
9. Document evidence, confidence, limitations, and recommended action.

Example: if a hypothetical “usage-to-work match rate” falls, first rule out a pipeline or definition problem. Then segment unmatched records by provider, identifier type, file date, territory, and format. A concentration in one new provider may indicate a mapping or source-format issue; a broad decline may suggest a wider reference-data or processing change.

## KPI Ideas for Discussion

These are hypotheses to validate with SOCAN, not claims about its current scorecard:

- Data-feed freshness and on-time arrival rate
- Required-field completeness and duplicate rate
- Usage-record-to-work match rate
- Unmatched or exception volume and aging
- Data-quality test pass rate
- Reporting refresh success and latency
- Ad-hoc request turnaround time
- Reconciliation variance between source and curated totals
- Royalty-distribution timeliness or adjustment rate, only if owned and defined by the department

For every KPI, ask for owner, purpose, formula, grain, exclusions, source, refresh cadence, target, and action threshold.

## Databricks, Spark, and Lakehouse Concepts

### Honest answer about your gap

> I have not yet used Databricks or Spark in a professional environment, so I would not present myself as production-ready on that stack. My directly transferable base is SQL, relational modelling, business-rule validation, analytical documentation, and repeatable project checks. I understand that Spark SQL works with structured data through a distributed execution engine, and I am building the practical bridge through DataFrames, transformations, partition-aware processing, and Databricks workflows. In a role, I would start with the team's approved patterns, validate results against control totals, review query plans and logs with experienced colleagues, and document what I learn.

### Core vocabulary

- Driver: coordinates the application and schedules work.
- Executor: performs tasks on cluster nodes.
- Partition: a subset of distributed data processed by a task.
- Transformation: creates a new logical dataset, such as select, filter, or join.
- Action: triggers computation, such as count or collect.
- Shuffle: redistributes data across partitions, often during joins or aggregations; it can be expensive.
- DataFrame: structured, distributed data with named columns and an optimized execution plan.
- Lazy evaluation: transformations build a plan; execution occurs when an action needs a result.

Spark's official documentation describes Spark SQL as its structured-data module and notes that SQL and DataFrame/Dataset interfaces use the same execution engine. Source: https://spark.apache.org/docs/latest/sql-programming-guide

### Medallion pattern — conceptual answer

- Bronze: raw, source-aligned records retained for traceability.
- Silver: cleaned, typed, deduplicated, standardized, and conformed data.
- Gold: business-ready aggregates, metrics, or dimensional models for reporting.

Say “a common pattern” rather than implying every SOCAN pipeline uses these exact layers.

### SQL versus Python

Use SQL for set-based transformation, joins, filters, aggregation, window calculations, profiling, and reconciliation when the data is tabular. Use Python/PySpark for reusable functions, orchestration, complex parsing, testing frameworks, APIs, or algorithms that are awkward in SQL. Follow the team's standards; consistency and maintainability matter more than choosing a language for its own sake.

## Databricks AI/BI Dashboards and Genie

Current Databricks documentation describes AI/BI dashboards as low-code dashboards for predefined analytical questions and Genie Agents as conversational experiences for broader natural-language questions. Databricks also emphasizes Unity Catalog governance and reusable semantic context. Official overview: https://docs.databricks.com/aws/en/ai-bi/concepts

### Dashboard workflow

1. Confirm audience, decisions, measures, dimensions, filters, and refresh needs.
2. Use governed tables, views, or metric views.
3. Validate dataset SQL independently.
4. Build a simple visual hierarchy: headline measures, trend, drivers, detail.
5. Add useful filters and clear labels, units, and definitions.
6. Test edge cases, totals, cross-filtering, permissions, refresh, and performance.
7. Obtain business acceptance and document ownership/change control.

### Semantic layer explanation

> A semantic layer gives business users consistent, reusable meaning on top of physical data. It defines trusted measures, dimensions, relationships, time logic, terminology, and governance so different consumers do not recreate conflicting definitions.

For natural-language querying, quality depends on clear names and descriptions, correct relationships, certified metrics, representative examples, instructions, permissions, and continuous review of unanswered or incorrect questions. Never imply that natural-language output should bypass reconciliation or human judgment.

### Genie risk controls

- Use governed data and least-privilege access.
- Define business terms and trusted calculations.
- Test ambiguous wording and follow-up questions.
- Maintain a benchmark set of expected questions and answers.
- Review generated SQL and reconcile important outputs.
- Capture user feedback and recurring failure modes.
- State limitations and avoid exposing restricted dimensions.

## Troubleshooting a Data Discrepancy

Use this sequence:

1. Capture the exact output, filters, time, user, expected result, and first known occurrence.
2. Confirm whether the issue is data, logic, refresh, permissions, or presentation.
3. Trace lineage from dashboard to semantic definition, curated table, transformation, and source.
4. Compare row counts, key counts, nulls, duplicates, sums, minimum/maximum dates, and status distributions at each stage.
5. Check recent schema, code, mapping, schedule, and source-feed changes.
6. Reproduce with the smallest affected slice.
7. Fix the root cause through change control; avoid a dashboard-only patch that masks bad upstream data.
8. Backfill if authorized, re-run tests, reconcile, document, and monitor.

## SQL Questions to Practise

### 1. Monthly KPI with month-over-month change

```sql
WITH monthly AS (
    SELECT
        DATE_TRUNC('month', event_date) AS month,
        SUM(amount) AS total_amount
    FROM fact_events
    WHERE status = 'recognized'
    GROUP BY 1
), compared AS (
    SELECT
        month,
        total_amount,
        LAG(total_amount) OVER (ORDER BY month) AS prior_amount
    FROM monthly
)
SELECT
    month,
    total_amount,
    prior_amount,
    (total_amount - prior_amount) / NULLIF(prior_amount, 0) AS mom_change
FROM compared
ORDER BY month;
```

Explain `NULLIF`, missing months, late-arriving data, and whether the amount is additive.

### 2. Duplicate detection at the expected grain

```sql
SELECT source_id, event_id, COUNT(*) AS row_count
FROM usage_events
GROUP BY source_id, event_id
HAVING COUNT(*) > 1;
```

Explain that the correct key must be agreed first; a repeated event ID might be valid across sources.

### 3. Reconciliation by stage

```sql
SELECT 'source' AS stage, COUNT(*) AS rows, SUM(amount) AS amount
FROM source_events
UNION ALL
SELECT 'curated', COUNT(*), SUM(amount)
FROM curated_events;
```

Discuss why totals alone are insufficient: compare distinct keys, date coverage, nulls, statuses, and exception records.

### 4. Find unmatched records

```sql
SELECT u.*
FROM usage_events u
LEFT JOIN works w
  ON u.work_id = w.work_id
WHERE w.work_id IS NULL;
```

Discuss normalized identifiers, whitespace/case, effective dates, null IDs, and the danger of fuzzy matching without controls.

## Behavioural Questions and Answer Points

### Why SOCAN?

Connect the role to SOCAN's purpose and data responsibility. Say that reliable data can help leaders understand processes, investigate exceptions, and improve reporting that supports a creator-focused organization. If you genuinely love music, add one concise personal sentence in your own words; otherwise do not manufacture a passion story.

### Tell me about an ambiguous request.

Use AYLA. Explain how you clarified the business question, expected output, data fields, and definition; then documented it and shared progress. Do not invent the request details. If pressed for specifics you cannot verify, say what is documented in your experience and describe your general framework separately.

### Tell me about a data-quality problem.

Use the e-commerce recognized-revenue logic or relational validation. Explain the risk of including pending/refunded/cancelled records, the rule, checks, and how you would confirm the definition with a business owner in production.

### How do you prioritize ad-hoc requests?

Assess decision impact, urgency, regulatory or financial risk, audience, effort, dependencies, and existing commitments. Confirm priorities with the manager when requests conflict. Give each requester a clear scope, owner, delivery time, and status; preserve time for validation.

### How do you communicate to non-technical leaders?

Lead with the decision and one-sentence finding. Show the measure, comparison, main driver, implication, confidence/limitation, and recommended next action. Keep SQL and implementation details in an appendix unless asked.

### What if a stakeholder disputes your number?

Stay neutral. Compare definitions, filters, time zones, source versions, refresh times, and grains. Reconcile together from a shared control total. Correct the analysis openly if needed and document the agreed definition.

### What is your greatest technical gap?

Name Databricks/Spark/Python without apology or evasion. Follow with transferable evidence, what you already understand, the specific plan below, and how you validate work while learning.

## 30-60-90 Day Answer

### First 30 days

- Learn SOCAN's business glossary, analytical priorities, data access rules, reporting inventory, and team working agreements.
- Shadow requirement sessions and trace selected dashboards from source to output.
- Learn approved Databricks notebooks, SQL standards, tests, semantic definitions, and deployment/review process.
- Complete small SQL data requests with peer review and documented reconciliation.

### Days 31-60

- Own a bounded recurring or ad-hoc analysis.
- Add or improve documented data-quality checks.
- Participate actively in standups, planning, and retrospectives.
- Build a small reviewed dashboard enhancement or dataset change if assigned.

### Days 61-90

- Independently deliver a scoped analysis from requirement to validated output.
- Investigate a KPI change or discrepancy and present evidence-led findings.
- Propose one low-risk improvement to documentation, testing, or request intake.
- Agree on the next Databricks/Python/Spark capability milestone with the manager.

Frame this as a proposed plan that would be adapted to SOCAN's priorities.

## Seven-Day Technical Preparation Plan

1. Rehearse every resume bullet and project SQL file; prepare one quality check and one decision insight per project.
2. Practise CTEs, joins, `CASE`, date logic, `LAG`, rankings, running totals, deduplication, and reconciliation without assistance.
3. Learn PySpark DataFrame basics: read, select, filter, group, join, window, write; explain lazy evaluation and partitions.
4. Complete a small Databricks exercise using a sample dataset: raw ingest, cleaning, SQL analysis, and checks. Describe it only after you genuinely complete it.
5. Build a simple AI/BI dashboard tutorial and record the dataset, measures, filters, and QA steps. Do not add it to the resume unless it is complete and verified.
6. Study semantic metrics and configure a small set of natural-language questions; compare generated answers against expected SQL.
7. Run a mock interview: introduction, SOCAN motivation, SQL screen, root-cause scenario, gap answer, and questions for the panel.

Official learning entry points:

- Databricks AI/BI: https://docs.databricks.com/aws/en/ai-bi/concepts
- Databricks dashboard tutorials: https://docs.databricks.com/aws/en/dashboards/tutorials
- Spark SQL/DataFrames: https://spark.apache.org/docs/latest/sql-programming-guide

## Questions to Ask the Interviewers

- Which business decisions and organizational initiatives will this analyst support first?
- How are reporting requirements, KPI definitions, and semantic-layer changes governed?
- What are the main data-quality challenges across usage, rights, licensing, or royalty-related data?
- How is work divided among data engineers, BI analysts, and data analysts?
- What does the current Databricks architecture and review/deployment process look like?
- How do you measure success in the first three and six months?
- What learning support is available for someone extending a strong SQL foundation into Spark, Python, and Databricks?

## Final Accuracy Checklist

- Do not claim two years of Databricks or similar technology.
- Do not claim hands-on Python, Spark, Genie, or AI/BI dashboard implementation until completed and verified.
- Say “Power BI dashboard planning,” not “built Power BI dashboards.”
- Do not claim dataset scale, production ownership, deployment, or quantified outcomes not in your evidence.
- Do not claim French or native-level English proficiency unless you can truthfully verify it.
- Do not claim passion for music unless it is genuine and you can discuss it naturally.
- Keep Australian and Indian education/employment distinct from current Toronto residence.
