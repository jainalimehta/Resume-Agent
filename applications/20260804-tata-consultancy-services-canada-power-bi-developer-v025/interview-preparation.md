# Interview Preparation — TCS Enterprise Power BI and SQL Opportunity

## Application Reality Check

This is a major stretch role and appears to target an experienced enterprise BI developer. Its top-three requirements are production Power BI expertise, advanced SQL development and tuning, and Kyvos experience. Jainali's verified foundation is PostgreSQL/SQL analytics, relational modelling, data validation, requirements documentation, Agile participation, and Power BI dashboard planning—not enterprise BI implementation.

The supplied posting does not state a formal title. Use `enterprise Power BI and SQL opportunity` and refer to the detailed scope unless TCS provides an exact title.

## 90-Second Introduction

> I am an early-career business analytics professional currently living in Toronto. I completed a Master of Business Analytics at Edith Cowan University in Australia after an Integrated Master of Business Administration at Atmiya University in India. As a Data Intern at AYLA Solutions in Australia, I gathered and documented business and reporting requirements, supported SQL extraction and validation, prepared advanced Excel reports and dashboard insights, and participated in Agile sprint planning and reviews. My three published PostgreSQL projects demonstrate relational modelling, keys and constraints, CTEs, window functions, controlled business definitions, repeatable validation, GitHub Actions checks, and AI-assisted recommendations grounded in SQL outputs. Each includes completed Power BI KPI and dashboard planning. I want to be precise that I have not yet implemented production Power BI dashboards or worked with Kyvos or Azure. I would bring my verified SQL, modelling, requirements, validation, and documentation foundation along with a structured commitment to developing the enterprise BI stack.

## Direct Gap Answer

> My current Power BI work is completed dashboard and KPI planning rather than production implementation. I have not yet used DAX, Power Query, RLS, Power BI Service, Kyvos, Synapse, Data Factory, Azure SQL, or Databricks professionally or in my published portfolio. I also have not owned enterprise SQL performance tuning or mentored junior developers. My relevant strengths are PostgreSQL and SQL analysis, relational schema design, data-quality controls, automated validation, requirements documentation, Agile collaboration, and business interpretation. I understand that the technical evaluation must test actual capability, and I would not overstate mine.

## Evidence Bank

- **Requirements:** AYLA Solutions — gathered and documented business/reporting requirements and translated stakeholder questions into analytical work.
- **SQL:** Three repositories — joins, aggregations, CTEs, rankings, segmentation, running totals, lag comparisons, and window functions.
- **Relational modelling:** E-Commerce — customers, products, orders, line items, payments, keys, uniqueness, checks, and controlled revenue.
- **Data quality:** Healthcare and HR — integrity controls, repeatable validation, and GitHub Actions checks.
- **BI planning:** All three projects — KPI, filters, visuals, reporting use cases, and decision-oriented dashboard planning.
- **AI-assisted analysis:** Prompts, interpretations, and recommendations based on validated SQL outputs.
- **Agile:** AYLA — sprint planning and review participation, progress communication, and documentation.
- **Education:** Databases and Business Intelligence, Business Systems Analysis, Enterprise Architecture, Machine Learning, and Project Management.

## Power BI Architecture to Study

Understand this sequence:

1. Connect to source systems.
2. Use Power Query to profile and transform data.
3. Build a semantic model with fact and dimension tables, relationships, measures, hierarchies, and metadata.
4. Use DAX measures for business calculations evaluated in filter context.
5. Design reports for defined decisions and user groups.
6. Define and test security, including RLS where appropriate.
7. Publish to Power BI Service, configure workspaces, permissions, refresh, gateways, apps, and endorsements.
8. Monitor refresh, usage, performance, data quality, security, and change impact.

Microsoft's semantic-model documentation covers transformations, relationships, DAX measures, RLS, and model optimization: [Power BI semantic model designer](https://learn.microsoft.com/en-us/power-bi/personas/semantic-model-designer/).

## DAX Fundamentals to Learn

- Measures are calculated at query time in the current filter context; calculated columns are materialized during refresh.
- Row context and filter context are different; `CALCULATE` modifies filter context.
- Learn `SUM`, `COUNTROWS`, `DISTINCTCOUNT`, `DIVIDE`, `CALCULATE`, `FILTER`, `ALL`, `VALUES`, `RELATED`, and time-intelligence prerequisites.
- Prefer explicit measures with clear names, formatting, and business definitions.
- Validate totals, blanks, denominator behaviour, filter interactions, and edge cases.

Illustrative study examples—not portfolio claims:

```DAX
Total Revenue = SUM(FactSales[Revenue])

Completed Orders =
CALCULATE(
    DISTINCTCOUNT(FactSales[OrderID]),
    FactSales[Status] = "Completed"
)

Average Revenue per Order =
DIVIDE([Total Revenue], [Completed Orders])
```

## Power Query Fundamentals to Learn

- Data types, nulls, errors, duplicates, filters, column transformations, split/merge, group by, pivot/unpivot, merge, and append.
- Query dependencies, parameters, reusable functions, privacy levels, and incremental-refresh prerequisites.
- Query folding: push transformations to the source when supported rather than processing everything locally.
- Separate staging queries from curated model tables and document transformation rules.

Do not claim Power Query experience until Jainali completes hands-on work and can explain each transformation herself.

## Data Warehousing and Dimensional Modelling

- **Fact table:** Business events or measurements at a declared grain.
- **Dimension table:** Descriptive context such as date, customer, product, employee, or location.
- **Star schema:** Facts connected to dimensions through one-to-many relationships.
- Define grain before selecting facts and dimensions.
- Use stable keys, conformed dimensions, clear date handling, and controlled business definitions.
- Distinguish transaction facts, periodic snapshots, and accumulating snapshots.
- Understand slowly changing dimensions conceptually, especially Type 1 and Type 2.

Jainali has relational modelling evidence but not verified enterprise star-schema or warehouse implementation.

## Row-Level Security

RLS restricts which rows users can retrieve from a semantic model. A typical workflow is to define roles and DAX filters, publish the model, assign users to roles, and test the result. Microsoft notes that workspace permissions affect RLS behaviour, so security testing must include the actual access model: [Microsoft RLS guidance](https://learn.microsoft.com/en-us/fabric/security/service-admin-row-level-security).

Study:

- Static roles versus dynamic security using user identity and mapping tables.
- Role design, least privilege, test cases, unauthorized-access scenarios, and auditability.
- Interaction between workspace roles, semantic-model permissions, and RLS.
- Need to test totals, drill-through, exports, connected reports, and representative users.

Do not claim RLS implementation experience.

## SQL Technical-Evaluation Preparation

Be able to write and explain:

- Inner and outer joins, aggregations, `CASE`, subqueries, CTEs, and window functions.
- `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LAG`, `LEAD`, and running totals.
- Duplicate detection, missing relationships, reconciliation, and exception queries.
- Correct grouping level and protection against duplicate multiplication after joins.
- Null handling, date filters, inclusive/exclusive boundaries, and division-by-zero handling.

Performance-tuning study process:

1. Confirm correctness, business grain, parameters, and representative workload.
2. Review the execution plan rather than guessing.
3. Identify scans, expensive joins, cardinality-estimate problems, sorts, spills, repeated work, and non-sargable predicates.
4. Reduce unnecessary rows and columns early.
5. Evaluate indexes with workload and write cost in mind.
6. Avoid applying functions to filtered columns when it prevents index use.
7. Re-test runtime, reads, CPU, concurrency impact, and plan stability.

Jainali must not claim execution-plan analysis, index tuning, partitioning, or enterprise performance improvements without completing hands-on evidence.

## Kyvos Fundamentals

At a conceptual level, Kyvos provides a semantic and analytics layer intended to support high-performance BI across large cloud or on-premises data environments. Kyvos describes a live Power BI connection through its MDX connector: [Kyvos Power BI integration](https://www.kyvosinsights.com/semantic-layer/bi-performance/power-bi/).

Prepare to ask about:

- How TCS's client uses Kyvos, its source platform, semantic models, aggregates, security, refresh, and Power BI connection mode.
- Ownership boundaries between source engineering, Kyvos modelling, Power BI semantic models, reports, and governance.
- Expected monitoring, troubleshooting, deployment, access, and support responsibilities.

Do not pretend that reading about Kyvos equals platform experience.

## Azure Platform Map to Study

- **Azure Data Factory:** Data integration and orchestration pipelines.
- **Azure Synapse:** Integrated analytics capabilities spanning SQL, data integration, and related services.
- **Azure SQL:** Managed relational database services.
- **Azure Databricks:** Collaborative Spark-based data engineering and analytics.
- Understand source-to-target mapping, transformations, orchestration, monitoring, failure handling, security, and cost at a conceptual level.

These are learning topics only; there is no verified hands-on Azure experience.

## Governance and Production Readiness

- Business owner, technical owner, data steward, source of truth, glossary, lineage, and change approval.
- Workspace strategy, development/test/production separation, deployment controls, versioning, and rollback.
- Refresh schedules, gateway ownership, credentials, failure alerts, and service-level expectations.
- Sensitivity, least privilege, RLS, export controls, audit logs, retention, and privacy.
- Data-quality checks, reconciliation, certification, documentation, user support, and incident management.
- Performance measures for source queries, refresh, semantic model, DAX, visuals, concurrency, and capacity.

Present this as a framework you have studied, not production ownership.

## Likely Technical Questions

- Explain your current Power BI experience and show what is actually implemented.
- What is the difference between Power Query and DAX?
- Measures versus calculated columns: when would you use each?
- Explain row context, filter context, and `CALCULATE`.
- How would you design a star schema for sales reporting?
- How would you implement and test RLS?
- Import versus DirectQuery: what are the trade-offs?
- How would you diagnose a slow Power BI report?
- Walk through an SQL query using CTEs and window functions.
- How would you identify why an SQL query became slow?
- How do you prevent duplicate multiplication after joining fact-like tables?
- What data-quality controls would you implement before publishing a dashboard?
- What is your Kyvos experience?
- Which Azure data services have you used?
- Describe your experience providing technical guidance to junior team members.
- Why should TCS consider you when you lack several top-three requirements?

## Questions for the Interviewer

- What is the formal role title and expected seniority for this vacancy?
- Is Kyvos required on day one, and what depth of model administration or development is expected?
- What proportion of the role is Power BI modelling, report development, SQL tuning, Kyvos support, governance, and stakeholder consultation?
- Which Azure platform and connection modes underpin the current BI architecture?
- What production scale, performance challenges, release process, and support expectations define success?
- Is there scope for an early-career candidate with strong SQL and modelling fundamentals to enter through structured training?

## Focused Learning Plan Before Screening

1. Build one small Power BI Desktop model from a star schema using a verified portfolio dataset.
2. Use Power Query for documented cleaning and transformations.
3. Write and explain at least ten DAX measures, including filter-context examples.
4. Implement static and dynamic RLS in a practice model and test representative roles.
5. Publish only if Jainali has legitimate Power BI Service access and can document the process.
6. Practise SQL window functions and use `EXPLAIN` in PostgreSQL on several queries.
7. Study Kyvos concepts and prepare informed questions without claiming experience.
8. Add new skills to the resume only after the work is completed, published, and independently explainable.

## Accuracy Guardrails

- Do not claim production Power BI dashboards, DAX, Power Query, RLS, Power BI Service, Kyvos, Azure, Databricks, enterprise ETL, data warehousing, or dimensional-model delivery.
- Do not claim advanced SQL tuning, execution-plan expertise, index optimization, or measured performance improvements.
- Do not claim Power BI certification, technical leadership, or junior-team guidance.
- Use exact project titles and keep Power BI status as completed planning with interactive implementation still pending.
- Do not claim Tableau, IBM SPSS Statistics, Canadian education, or Canadian employment.
- Never invent users, rows, refresh time, performance gains, dashboard adoption, savings, or other metrics.
