# Interview Preparation — Tayco BI Specialist / Data Analyst

## Candid Fit Assessment

This is an experienced, hands-on BI delivery position despite accepting related education as an alternative to three to five years of experience.

- **Strong direct evidence:** PostgreSQL, analytical SQL, joins, aggregation, CTEs, window functions, relational modelling, data validation, advanced Excel, reporting requirements, KPI analysis, Git/GitHub, GitHub Actions, documentation, and AI-assisted interpretation.
- **Adjacent evidence:** Power BI dashboard/KPI planning, visualization requirements, Agile collaboration, stakeholder communication, and operational analysis.
- **Major mandatory gaps:** DAX, Power Query, production Power BI publishing/refresh/gateway/workspace administration, Crystal Reports, Windows Server, HTML/CSS/Bootstrap, report embedding, Git branching/pull-request/code-review practice, SQL tuning/views/stored procedures, ERP data, and manufacturing reporting.

Apply if you want the opportunity, but expect a lower interview probability unless Tayco is prepared to train. Never imply production experience you do not have.

## 90-Second Introduction

> I am an early-career business analytics professional living in Toronto. I completed a Master of Business Analytics at Edith Cowan University in Australia. At AYLA Solutions in Australia, I gathered reporting requirements, supported SQL extraction and validation, prepared advanced Excel reports, and contributed dashboard and reporting insights through Agile planning and review cycles. My published PostgreSQL portfolio covers e-commerce, healthcare, and workforce data, with relational models, business rules, CTEs, window functions, repeatable validation, GitHub Actions checks, AI-assisted recommendations, and detailed Power BI dashboard planning. Earlier roles strengthened my workflow coordination, client communication, record accuracy, and confidentiality. My direct foundation is strongest in SQL, Excel, requirements, quality checks, and reporting design. I would be transparent that Crystal Reports, Windows Server, and production Power BI administration are development areas for me.

## Why Tayco

> Tayco appeals to me because the role sits directly between manufacturing operations, business reporting, and in-house software development. I enjoy tracing a business question back to its data definitions and source logic, then presenting the result clearly. The opportunity to work closely with developers and a project coordinator would let me contribute my SQL, validation, requirements, and documentation strengths while developing deeper production BI capability in a real operational environment.

Tayco describes itself as a Toronto-based manufacturer of customized commercial office furniture serving North America. Connect your interest to operational reporting, product quality, customer delivery, and practical decision support—not to unsupported manufacturing experience.

## Reporting-Requirements Framework

When management asks for a report:

1. Confirm the audience, decision, business question, delivery date, frequency, and required level of detail.
2. Define every KPI, including numerator, denominator, inclusions, exclusions, status, date basis, and unit.
3. Confirm the reporting grain, dimensions, filters, drill-downs, comparison period, target, and exception rules.
4. Identify authoritative sources, owners, joins, refresh frequency, access restrictions, and known limitations.
5. Sketch the layout and validate it with the user before investing in the full build.
6. Build transformations, model relationships, measures, and visuals with documented logic.
7. Reconcile totals to the source and test normal, boundary, missing, duplicate, and exception cases.
8. Obtain user review, control publication and access, document the report, and monitor refresh/use.

## Power BI Knowledge to Study

Present this as learned knowledge, not completed delivery.

- **Power Query:** Microsoft's data preparation and transformation engine. It connects to sources, applies repeatable transformations, and loads data into the host product.
- **Data model:** related tables with clear grain, keys, cardinality, filter direction, and preferably reusable dimensions for consistent analysis.
- **DAX:** expression language for calculations over related tabular data. Understand calculated columns versus measures and row context versus filter context.
- **Semantic model:** reusable governed model supplying reports and calculations.
- **Import mode:** data is loaded into the model and needs refresh.
- **DirectQuery:** queries the source at interaction time and depends on source performance/connectivity.
- **Gateway:** secure bridge needed for some on-premises sources to refresh or query through the Power BI service.
- **Scheduled refresh:** configured against the semantic model with connections, credentials, schedule, failure history, and notifications.
- **Workspace/access:** manage content lifecycle and permissions using least privilege and approved roles.

### DAX examples to understand

```text
Total Sales = SUM(Sales[SalesAmount])
Order Count = DISTINCTCOUNT(Sales[OrderID])
Average Order Value = DIVIDE([Total Sales], [Order Count])
Sales LY = CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Date'[Date]))
YoY % = DIVIDE([Total Sales] - [Sales LY], [Sales LY])
```

Be ready to explain what each measure means, what filters affect it, and how you would reconcile it. Do not claim you have implemented these in a published dashboard.

### Honest Power BI answer

> I have completed KPI, visual, filter, and dashboard planning for all three published projects, but I have not yet produced a `.pbix` file or administered production publishing, refreshes, gateways, or workspaces. My hands-on foundation is SQL, relational modelling, validation, and advanced Excel. I understand the Power BI lifecycle conceptually and would need structured hands-on onboarding before owning Tayco's production environment.

## SQL and Query-Tuning Preparation

Your verified SQL topics:

- joins, grouping, aggregation, `CASE`, CTEs, ranking, running totals, `LAG`, keys, constraints, business rules, and validation;
- PostgreSQL relational models across customer/order, healthcare, and workforce domains.

Topics to study before interview:

- confirm the query's grain and expected row count before aggregation;
- inspect joins for accidental one-to-many multiplication;
- use selective predicates and avoid unnecessary columns/rows;
- understand indexes and why an index is not always selected;
- use PostgreSQL `EXPLAIN` to inspect the planner's chosen query plan;
- compare estimated versus actual rows using `EXPLAIN ANALYZE` carefully because it executes the query;
- review scans, joins, sorts, aggregations, and expensive steps;
- consider statistics, data distribution, repeated calculations, and query maintainability;
- measure performance rather than claiming an optimization based on intuition.

### Honest tuning answer

> I have strong analytical SQL and validation experience, but I do not yet claim production query-performance tuning, views, or stored procedures. My approach would be to reproduce the issue safely, confirm the result and baseline runtime, inspect the plan with the approved tools, identify the expensive operation, make one controlled change, verify correctness, compare performance, and document the decision. I would seek review before changing production objects.

## Crystal Reports Knowledge

Crystal Reports is designed for structured operational and printable reporting. Core concepts include selecting a data source, linking tables, choosing fields, grouping, formulas, parameters, record selection, sections, totals, formatting, refresh, export, and distribution.

SAP documentation notes that reports commonly select sources through the Database Expert and can use parameters to let consumers filter or shape results. Testing should cover parameter values, missing/optional parameters, data changes, pagination, grouping, totals, print/export layout, permissions, and source connectivity.

### Honest gap answer

> I have not developed or maintained Crystal Reports. My closest foundation is SQL reporting logic, advanced Excel reporting, requirements clarification, documentation, and Power BI planning. I would learn an approved report by tracing its data source, parameters, formulas, groups, sections, and distribution process; reproduce it in a training environment; reconcile its figures; and request review before supporting a live operational report.

## Windows Server and Reporting Infrastructure

Know the purpose of each item:

- **Scheduled task/job:** runs a report, extract, script, or distribution process at a defined time or trigger.
- **Service account:** non-personal identity used by a service or scheduled process; permissions and credentials require controlled management.
- **File share:** network location with governed access, naming, retention, and distribution expectations.
- **Permissions:** grant only required access and test both authorized and unauthorized paths.
- **Monitoring:** check success/failure status, logs, runtime, missed schedules, credentials, storage, and downstream delivery.
- **Incident response:** identify impact, preserve evidence, communicate, restore service, validate outputs, and document the root cause and prevention.

Do not claim Windows Server administration. Emphasize caution with credentials, service accounts, and production changes.

## Git and GitHub Workflow

Your direct evidence is Git, GitHub, and GitHub Actions. Branching, pull requests, and code review are not verified.

A team workflow generally uses a short-lived branch, focused commits, automated checks, a pull request explaining the change and validation, peer review, resolution of feedback, and controlled merge. GitHub describes pull requests as proposals to discuss and review changes before merging.

### Honest answer

> I use Git, GitHub, and GitHub Actions in my portfolio, but I have not claimed professional pull-request or code-review ownership. I understand the collaborative workflow and would follow Tayco's branch naming, commit, review, testing, approval, and merge standards rather than assume my personal-repository habits are sufficient.

## Light Front-End and Report Embedding

Study the roles of HTML structure, CSS presentation, Bootstrap components/grid, responsive layout, accessibility, and embedded-report configuration. A safe change requires a scoped branch, local or test-environment verification, permission/security review, responsive checks, and peer review.

Do not claim HTML, CSS, Bootstrap, Django, JavaScript, or report-embedding experience.

## Manufacturing and ERP Reporting

Common subject areas to understand:

- **Production:** planned versus actual quantity, schedule attainment, throughput, cycle time, downtime, scrap/rework, and work-in-progress.
- **Inventory:** on-hand, available, allocated, safety stock, stockout, ageing, turnover, and valuation.
- **Purchasing:** purchase orders, requested/promised/received dates, supplier lead time, price variance, and late receipts.
- **Sales:** order intake, backlog, recognized revenue, margin, returns, cancellations, and on-time delivery.
- **Quality:** defects, first-pass yield, rework, inspection status, and corrective actions.

Definitions vary. For example, `on-time delivery` may use promised date, requested date, ship date, or receipt date. Always confirm the approved date and status logic before calculating it.

### Suggested star-schema design exercise

Study—but do not claim implementation of—a model with facts for sales orders, production transactions, inventory movements, and purchase receipts, plus dimensions for Date, Product, Customer, Supplier, Plant/Location, Employee/Work Centre, and Status. Define grain first and avoid mixing facts at different grains without controlled measures.

## Reconciliation and Discrepancy Answer

> I would first stop the figure from reaching the decision-maker if it might be materially wrong. I would confirm the KPI definition, report period, source, refresh time, and filters; compare row counts and control totals; inspect joins, duplicates, nulls, statuses, effective dates, and exclusions; and trace a sample record from the report back to the source. I would document the cause, correction, validation, impact, and any preventive check. If I could not resolve it before the deadline, I would communicate the limitation clearly rather than present the figure as final.

## Responsible AI Answer

> I use AI to accelerate bounded tasks such as generating alternative questions, checking documentation structure, or exploring an analytical interpretation. I remain responsible for the result. I protect confidential data, use only approved tools, inspect every query and measure, validate outputs against source data, test edge cases, and reject suggestions I cannot explain. My portfolio's AI-assisted recommendations are grounded in validated SQL outputs rather than accepted at face value.

## Report-Design Principles

- Start with the decision and audience, not the chart type.
- Establish visual hierarchy: title and context, headline KPI, trend/comparison, drivers, detail, and action.
- Use consistent labels, units, formats, colours, and definitions.
- Prefer tables for precise lookup; bars for comparisons; lines for time; avoid unnecessary 3-D or decoration.
- Highlight exceptions selectively and ensure colour is not the only signal.
- Include refresh date, reporting period, source/definition notes, and known limitations.
- Test readability on the actual screen or printed format used by management.

## Likely Interview Questions

- Why Tayco and why manufacturing BI?
- Walk us through an analytical project from data model to recommendation.
- How do you gather and confirm reporting requirements?
- How do you validate a KPI against its source?
- Explain a CTE and a window function you used.
- How would you investigate a slow SQL query?
- What is your hands-on Power BI experience?
- Explain Power Query, DAX measures, gateways, and scheduled refresh.
- What Crystal Reports experience do you have?
- What Windows Server or front-end experience do you have?
- How have you used Git/GitHub, and have you worked with pull requests?
- How would you design a production, inventory, purchasing, or sales dashboard?
- How would you communicate an incorrect management figure?
- How do you use AI while staying accountable?
- How would you prioritize report requests from several managers?

## STAR Story Plan

- **AYLA requirements/reporting:** clarify the need, support SQL extraction and validation, prepare Excel reporting, communicate progress, and document work.
- **E-Commerce Sales Analytics:** model relational data, define recognized revenue, analyze KPIs, validate results, automate checks, and develop evidence-grounded recommendations.
- **Healthcare Analytics:** apply CTEs and windows to operational measures and validate outputs.
- **HR Analytics:** define workforce entities and analyze headcount, compensation, performance, attendance, hiring, and tenure.
- **Trans Globe:** maintain records and coordinate process updates with students and institutions.
- **Arihant:** protect accuracy and confidentiality in investment-services records.

Do not add unverified scale, timings, audiences, savings, team sizes, deployments, or production outcomes.

## Questions for the Interviewer

- Which mandatory platform skills are expected on day one, and which can be developed during onboarding?
- What percentage of the role is Power BI, Crystal Reports, SQL, infrastructure support, and front-end work?
- What are the principal ERP and in-house data sources, and which system is authoritative for each reporting domain?
- How mature are the current semantic models, report catalogue, definitions, and documentation?
- What is the workflow for branch review, testing, deployment, access approval, refresh monitoring, and incident escalation?
- Which reports or data-quality risks would this person own first?
- How is success measured during the 12-month contract?

## 30/60/90-Day Outline

**First 30 days:** Learn Tayco's manufacturing processes, ERP entities, report inventory, owners, definitions, source systems, security, deployment standards, support expectations, and priority risks. Reproduce and reconcile an existing report under supervision.

**Days 31–60:** Own a bounded SQL or reporting change; document requirements, source logic, measures, validation, and release evidence; support issue triage and report-user communication.

**Days 61–90:** Deliver a reviewed enhancement, monitor refresh and data quality, present the result clearly, update documentation, and propose one practical reliability or usability improvement based on evidence.

## Accuracy Guardrails

- Use `Data Intern` for AYLA Solutions.
- Describe Power BI only as KPI/dashboard/visualization planning.
- Do not claim DAX, Power Query, `.pbix`, publishing, gateways, refreshes, workspaces, or access administration.
- Do not claim Crystal Reports, Windows Server, HTML, CSS, Bootstrap, Django, report embedding, ERP, or manufacturing experience.
- Do not claim SQL views, stored procedures, or performance tuning.
- Do not claim Git branching, pull requests, or code review.
- Do not claim Python, R, Azure, SSRS, Report Server, or star-schema implementation.
- Do not claim Canadian education or employment, work authorization, travel/overtime availability, or training ownership.

## Official Study Sources

- [Microsoft Learn — DAX Overview](https://learn.microsoft.com/en-us/dax/dax-overview)
- [Microsoft Learn — What Is Power Query?](https://learn.microsoft.com/en-us/power-query/power-query-what-is-power-query)
- [Microsoft Learn — Configure Power BI Scheduled Refresh](https://learn.microsoft.com/en-us/power-bi/connect-data/refresh-scheduled-refresh)
- [PostgreSQL Documentation — Using EXPLAIN](https://www.postgresql.org/docs/17/using-explain.html)
- [SAP Crystal Reports — Selecting a Data Source](https://help.sap.com/docs/SAP_CRYSTAL_REPORTS/dfc124becfa845ffa91b1e717b20e3ec/476224b76e041014910aba7db0e91070.html)
- [SAP Crystal Reports — Parameter Fields and Prompts](https://help.sap.com/docs/SAP_CRYSTAL_REPORTS/dfc124becfa845ffa91b1e717b20e3ec/476eb1b86e041014910aba7db0e91070.html)
- [GitHub Docs — Pull Requests](https://docs.github.com/en/pull-requests/reference/pull-requests)
- [Tayco — Company FAQ](https://www.tayco.com/faqs/)
