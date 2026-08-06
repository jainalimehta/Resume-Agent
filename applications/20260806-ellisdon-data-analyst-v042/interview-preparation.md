# Interview Preparation — Data Analyst, EllisDon

## Fit Reality

This is a stretch role. Jainali has a relevant master's degree, Australian Data Intern experience, PostgreSQL, SQL, advanced Excel, relational modelling, quantitative analysis, requirements documentation, KPI definition, repeatable validation, Power BI planning, GitHub Actions, and Agile planning and review exposure. She does not have two to four years of analyst employment, construction experience, large-project experience, implemented dashboards, legacy migration, ETL pipelines, data-collection systems, DundasBI, NoSQL, Workday, specialized statistical packages, or scripting-language experience. The interview strategy is to demonstrate transferable analytical discipline and a realistic learning plan.

## 90-Second Introduction

“I currently live in Toronto, while my education and work experience are international. I completed a Master of Business Analytics at Edith Cowan University in Australia and an Integrated MBA at Atmiya University in India. As a Data Intern at AYLA Solutions in Australia, I gathered and documented reporting requirements, translated stakeholder questions into analytical tasks, supported SQL extraction and validation, prepared advanced Excel reports, and contributed dashboard insights. My three PostgreSQL projects cover workforce, financial, and operational analytics. They use relational models, CTEs, window functions, documented business rules, repeatable validation, GitHub Actions, and SQL-grounded recommendations with Power BI planning. I have not worked in construction or implemented migrations, ETL pipelines, DundasBI, Workday, or interactive dashboards. I would bring strong SQL and Excel fundamentals, requirements discipline, careful validation, and a structured approach to learning EllisDon's systems and project environment.”

## Why EllisDon?

“EllisDon combines construction services with meaningful technology capability. I was interested that its Digital & Data Engineering organization has supported software, data analytics, cybersecurity, and enterprise technology, and that Building Digital focuses on practical technology adoption in the architecture, engineering, and construction industry. I also connect with its values of freedom and trust, complete openness, mutual accountability, entrepreneurial enthusiasm, and integrity and mutual respect. This role would let me contribute analytical fundamentals while learning how trustworthy data improves real projects, operations, and communities.”

## Honest Gap Answer

“My strongest hands-on tools are PostgreSQL, SQL, and advanced Excel. I have not worked on construction projects or implemented production migrations, ETL pipelines, data-collection systems, DundasBI, Workday, NoSQL, statistical packages, or scripting. My Power BI evidence is dashboard planning rather than interactive implementation. I would not describe conceptual preparation as experience. I would first learn the approved business definitions, source systems, project lifecycle, access controls, and existing reports; reproduce a trusted metric; reconcile it to control totals; own a bounded analysis under review; and expand responsibility only after demonstrating accuracy.”

## Construction Analytics Context to Learn

The following are study concepts, not verified experience.

- **Project lifecycle:** pursuit and pre-construction, design, procurement, construction, commissioning, turnover, and operations or maintenance.
- **Cost:** budget, commitments, actuals, accruals, forecast, contingency, approved and pending changes, and estimate at completion.
- **Schedule:** planned versus actual milestones, critical activities, float, delay, look-ahead completion, and schedule variance.
- **Productivity:** installed quantity or completed work relative to labour hours or another approved input.
- **Quality:** inspections, deficiencies, rework, closure time, and recurring issue categories.
- **Safety:** observations, incidents, corrective actions, exposure hours, severity, and closure—only under approved safety definitions.
- **Commercial and procurement:** packages, bids, purchase orders, subcontracts, invoices, payment status, change orders, and vendor performance.
- **Information flow:** requests for information, submittals, drawings, approvals, document revisions, and turnaround time.

Never assume a metric definition or interpret safety, cost, or schedule performance without the appropriate project expert.

## Requirements-to-Metric Framework

1. Clarify the decision, stakeholder, action, cadence, deadline, and current pain point.
2. Map the business process and identify system owners and subject-matter experts.
3. Define the metric population, grain, formula, exclusions, dimensions, threshold, owner, and source.
4. Identify data availability, permissions, quality risks, historical depth, and refresh timing.
5. Prototype the analysis and reconcile it to an approved control.
6. Validate interpretation with business and technical owners.
7. Document acceptance criteria, sign-off, lineage, limitations, and change control.
8. Monitor accuracy, usage, action, and unintended consequences after release.

## Metric Dictionary Template

For every metric document:

- Business name and plain-language purpose
- Decision and responsible owner
- Formal calculation and record grain
- Numerator, denominator, population, inclusions, and exclusions
- Dimensions and permitted filters
- Source systems and lineage
- Refresh schedule and effective date
- Reconciliation control and quality threshold
- Security classification and access
- Known limitations and change history

## Legacy Migration and ETL Framework

Jainali has not implemented a migration. Use this as learned methodology.

1. Inventory sources, owners, tables or files, interfaces, retention requirements, and downstream reports.
2. Profile fields, types, nulls, duplicates, code values, keys, date ranges, and historical anomalies.
3. Define source-to-target mappings, transformation rules, defaults, reference data, exceptions, and unresolved decisions.
4. Clean and standardize data without destroying source traceability.
5. Extract from controlled snapshots; transform using versioned rules; load to a test environment.
6. Reconcile counts, control totals, key populations, and exception records by stage.
7. Perform functional, integration, security, performance, and user-acceptance testing as required.
8. Run mock conversions, track defects, define cutover and rollback, and obtain sign-off.
9. Validate post-load data and critical reports; monitor early production issues.
10. Archive mappings, test evidence, approvals, lineage, lessons learned, and ownership.

Important principle: migration success is not merely “the load completed.” It means approved business records are complete, accurate, usable, secure, and reconciled in the target system.

## Workday and Financial-System Concepts

- **Workday:** may contain worker, organization, position, compensation, time, absence, recruiting, or finance-related data depending on configured modules.
- **Financial systems:** may contain chart of accounts, cost centres, projects, commitments, invoices, payments, journals, budgets, forecasts, and vendor records.
- Effective dating, organization hierarchies, status logic, security roles, reference data, and historical changes are critical.
- Workforce records and project financial records may have different grains and access restrictions.
- Ask which system is authoritative for each field and which reports must reconcile after migration.

Jainali has not used Workday or production financial systems.

## Data-Quality Framework

| Dimension | Example control |
|---|---|
| Completeness | Required project, worker, vendor, date, amount, status, and code fields are populated |
| Uniqueness | Approved business keys do not contain unauthorized duplicates |
| Validity | Types, ranges, dates, statuses, and codes meet approved rules |
| Consistency | Entities and definitions agree across systems and reports |
| Referential integrity | Project, cost-code, worker, vendor, and organization references resolve |
| Timeliness | Sources and loads arrive within the agreed reporting window |
| Reconciliation | Counts and financial or operational totals match approved controls |
| Lineage | Source, transformation, owner, refresh, and downstream use are documented |

When a defect appears: quantify affected records and decisions, isolate source versus transformation, protect downstream outputs, notify owners, correct and retest, then add a preventive control.

## Dashboard Design Framework

- Start with the decision and audience, not the chart type.
- Use a limited set of governed KPIs with visible definitions and refresh timing.
- Show status, trend, target, variance, and the segments that explain movement.
- Provide project or operational drill-down without exposing unauthorized data.
- Use direct titles, labelled units, consistent colours, accessible contrast, and sensible default filters.
- Distinguish actuals, forecasts, commitments, and pending changes.
- Include data-quality or completeness indicators when they affect interpretation.
- Validate every displayed value against source controls before release.
- Track usage and whether the dashboard changes decisions or actions.

## Working With a Scrum Data-Product Team

- Translate stakeholder needs into a clear problem statement, user story, metric definition, and acceptance criteria.
- Participate in refinement, planning, review, and retrospectives without claiming unverified ceremony ownership.
- Break analysis into testable increments and identify dependencies early.
- Maintain traceability from requirement to model, metric, test, visualization, and acceptance.
- Review feasibility and data implications with developers or data engineers.
- Demonstrate outputs with business context and record feedback and decisions.
- Treat definition changes as controlled product changes, not local report edits.

## Identifying New Data Sources

1. Begin with an unresolved business question or quality gap.
2. Identify possible internal or external sources and responsible owners.
3. Assess relevance, grain, history, coverage, refresh, accuracy, cost, permissions, privacy, and retention.
4. Profile a representative sample and test linkage to existing entities.
5. Compare incremental decision value against collection and governance burden.
6. Pilot with documented controls, ownership, and success criteria.
7. Approve, operationalize, monitor, or reject based on evidence.

## Statistical and Quantitative Preparation

- Descriptive statistics: count, proportion, mean, median, spread, percentiles, distribution, and outlier review.
- Compare appropriate rates and denominators, not only raw totals.
- Distinguish correlation from causation.
- Consider seasonality, project mix, stage, size, geography, and data-collection changes.
- Use confidence intervals and hypothesis tests only when assumptions, sampling, and decision context support them.
- Explain practical significance, uncertainty, and limitations in plain language.
- Use Excel capabilities Jainali can demonstrate; do not claim software she has not used.

## Likely Case Questions

### Workforce totals differ before a Workday migration.

Confirm worker grain, employee versus contingent-worker scope, active-status logic, effective dates, positions, organizations, leave handling, and duplicate identifiers. Reconcile counts by source and status, isolate unmatched records, agree authoritative rules with HR and system owners, document mappings and exceptions, and retest before load.

### Two reports show different project costs.

Confirm project and cost-code scope, posting period, currency, actual versus commitment versus accrual, approved and pending changes, refresh timing, and reversals. Reconcile by stage, identify the certified definition for each decision, correct the governed model rather than one report, and add a regression control.

### A project dashboard shows declining productivity.

Validate quantities, labour hours, work package, period, and project-stage definitions. Decompose by activity, crew, location, shift, change, weather or constraint only with domain experts. Separate verified contributors from hypotheses and recommend an action, owner, expected indicator, and review period.

### A stakeholder asks for “all project data” in one dashboard.

Clarify the decision, audience, priorities, security, and action. Propose a small governed metric set and layered design, document definitions, validate against controls, and phase delivery rather than combining incompatible grains into an unreadable report.

### A legacy field has no target-system equivalent.

Determine its business meaning, owner, downstream use, legal or retention need, and whether it should map, transform, derive, archive, or remain an approved exception. Never silently discard it or force it into an inaccurate target field.

## SQL Review Priorities

- Grain, keys, join cardinality, and duplicate multiplication.
- `INNER` versus `LEFT JOIN`, null handling, and anti-joins for missing records.
- CTEs for readable transformations.
- Conditional aggregation for status and quality metrics.
- Window functions for rank, running total, lag, and period comparisons.
- Effective-dated and snapshot logic.
- Reconciliation queries and exception tables.
- Deterministic deduplication.
- Performance concepts: required columns, selective filters, indexes conceptually, query plans, and avoiding repeated computation.

Discuss only SQL Jainali can explain line by line.

## Behavioural Evidence

- **Ambiguous requirement:** AYLA—translated stakeholder questions into structured analytical tasks.
- **Workforce metrics:** HR project—headcount, compensation, performance, attendance, hiring, and tenure.
- **Financial controls:** E-commerce project—revenue rules, payments, keys, integrity checks, and validation.
- **Operational metrics:** Healthcare project—completion, costs, workload, billing, claims, and lag comparisons.
- **Agile collaboration:** AYLA—participated in sprint planning and review sessions.
- **Coordination:** Trans Globe Education—maintained records and coordinated updates with students and institutions.
- **Confidentiality:** Arihant Investment—maintained accurate confidential client records.

Use Situation, Task, Action, and Result. Where no measured result is verified, finish with the factual deliverable.

## Questions to Ask

1. Which business area, projects, and data products would this analyst support first?
2. What are the primary source systems and current reporting or migration priorities?
3. How are responsibilities divided among analysts, data engineers, Scrum teams, and business subject-matter experts?
4. Which construction metrics are already standardized, and where are definitions governed?
5. What is the current BI, database, ETL, and data-quality toolset?
6. What role would this analyst play in Workday or financial-system migration activities?
7. What does strong performance look like during the first 90 days?
8. What training supports analysts who are new to the construction domain and EllisDon's platforms?

## 30-60-90 Day Approach

- **First 30 days:** Learn the project lifecycle, systems, metric dictionary, stakeholders, security, existing reports, Scrum process, and quality controls; reproduce a trusted SQL or Excel output.
- **Days 31-60:** Own a bounded analysis or quality check under review, document lineage and exceptions, support a requirements session, and contribute to a supervised report or migration deliverable.
- **Days 61-90:** Deliver an approved reporting or data-quality improvement, present findings clearly, document reusable logic, and monitor accuracy, usage, and unresolved issues.

## Accuracy Guardrails

- Do not claim two to four years of analyst employment, Canadian work experience, construction experience, or work on large civil or building projects.
- Do not claim DundasBI, NoSQL, Workday, migration, ETL, data-collection systems, specialized statistical packages, or scripting languages.
- Do not claim implemented interactive Power BI dashboards or `.pbix` deliverables.
- Do not describe portfolio projects as production, enterprise, construction, Workday, or financial-system implementations.
- Do not invent dataset volumes, cost savings, project values, schedule improvements, safety outcomes, work authorization, or language proficiency.

## Official Research

- [EllisDon — About Us](https://www.ellisdon.com/about-us): employee ownership, scale, construction and technology identity, communities, inclusion, and company context.
- [EllisDon — Our Values](https://www.ellisdon.com/our-values): freedom and trust, complete openness, mutual accountability, entrepreneurial enthusiasm, integrity, and mutual respect.
- [EllisDon — Building Digital](https://www.ellisdon.com/news/ellisdon-unveils-building-digital-pioneering-the-future-of-construction-technology-for-customers): Digital & Data Engineering, data analytics, enterprise software, data infrastructure, and practical technology adoption.
- [EllisDon — 2025 Impact Report](https://impactreport2025.ellisdon.com/): climate and environment, inclusion, Indigenous relations, health and safety, community, innovation, and governance.

Recheck the posting, current official documentation, and EllisDon's approved project and system definitions before interviewing.
