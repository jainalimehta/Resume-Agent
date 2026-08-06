# Interview Preparation — Data & Business Insights Analyst, CGI

## Fit Reality

This is a substantial stretch role. Jainali has a relevant master's degree, Australian Data Intern experience, PostgreSQL, SQL, advanced Excel, requirements documentation, relational modelling, validation, operational and workforce KPIs, Power BI planning and stakeholder communication. She has not independently implemented Power BI dashboards, used ServiceNow or LiveLink, delivered executive reporting, facilitated workshops, or performed professional capacity, SLA, forecasting or financial-services analytics. The interview strategy must emphasize evidence, quality controls and learning ability without inflating delivery ownership.

## 90-Second Introduction

“I currently live in Toronto, while my education and work experience are international. I completed a Master of Business Analytics at Edith Cowan University in Australia and an Integrated MBA at Atmiya University in India. As a Data Intern at AYLA Solutions in Australia, I gathered reporting requirements, translated stakeholder questions into analytical tasks, supported SQL extraction and validation, and prepared advanced Excel reports and dashboard insights. My three PostgreSQL projects cover workforce, e-commerce and healthcare analytics. They use relational models, CTEs, window functions, repeatable validation and GitHub Actions, followed by SQL-grounded recommendations and Power BI dashboard planning. I have not independently implemented interactive Power BI dashboards, used ServiceNow or LiveLink, or delivered professional capacity, SLA, forecasting or executive reporting. I would bring strong SQL and Excel fundamentals, disciplined validation, requirements thinking and a structured approach to learning CGI's client environment.”

## Why CGI?

- CGI's consulting model connects analytics with client operations and implementable decisions.
- Its Canadian data analytics practice focuses on business use cases, data governance, dashboards, performance and operational improvement.
- CGI's ownership culture encourages partners to participate in strategy, collaboration, continuous improvement and collective success.
- The role offers exposure to enterprise systems, operational planning, stakeholder workshops and client-facing communication.

## Honest Power BI and Enterprise-Platform Gap Answer

“My Power BI evidence is dashboard planning—KPI definitions, filters, visual requirements and decision-use cases—not independent interactive implementation. I also have not used ServiceNow or LiveLink. My strongest hands-on tools are PostgreSQL, SQL and advanced Excel. If considered, I would first learn the client's certified sources, definitions, access model and existing report catalogue; reproduce a trusted report; reconcile every KPI to control totals; document transformations and limitations; build a bounded dashboard component in a sandbox; seek review; and only then expand ownership.”

## Requirements-to-Insight Framework

1. Clarify the decision, audience, action, frequency, deadline and current pain point.
2. Identify source systems, owners, grain, keys, refresh timing, history and access constraints.
3. Define KPI formulas, dimensions, filters, thresholds, exceptions and acceptance criteria.
4. Profile and reconcile data before analysis.
5. Separate descriptive findings, likely drivers, limitations and recommendations.
6. Design the report for the audience: operational detail for managers, concise drivers and decisions for executives.
7. Validate with technical and business owners, document sign-off and monitor adoption and quality.

## Power BI Preparation

- Understand star schemas, fact/dimension grain, relationships and filter direction.
- Review Power Query for ingestion and transformation; do not confuse it with DAX calculations.
- Review measures, calculated columns, row context, filter context and `CALCULATE` conceptually.
- Learn refresh, gateways, workspaces, permissions, row-level security, deployment and usage monitoring.
- Dashboard quality: certified definitions, visible refresh time, consistent filters, accessibility, performance and clear exception handling.
- Be explicit that these are preparation topics, not verified implementation experience.

## ServiceNow and LiveLink Concepts

- **ServiceNow:** Enterprise workflow platform often used for incidents, requests, changes, assets, service management and SLA tracking. Reporting requires understanding table relationships, statuses, assignments, timestamps and business rules.
- **LiveLink/OpenText:** Enterprise content and document-management environment. Analytics may involve document metadata, workflow states, ownership, timestamps, permissions and retention.
- Key questions: What is the authoritative source? What is the grain? Which status transitions matter? How are timestamps and business calendars handled? What privacy and access rules apply?
- Jainali has not used either platform.

## Capacity, Resource and Forecasting Concepts

- **Demand:** Expected workload such as tickets, transactions, cases or service requests by period and category.
- **Capacity:** Available productive effort after schedules, skills, leave, meetings and other constraints.
- **Utilization:** Productive or assigned effort relative to available capacity under an approved definition.
- **Backlog:** Uncompleted work at a point in time, classified by priority, age, owner or status.
- **Throughput:** Completed work per unit of time.
- **Cycle time:** Elapsed time from agreed start to completion.
- **Forecast variance:** Actual versus forecast using a consistent definition and period.
- Always segment by service, team, priority, skill, location and time where appropriate; distinguish volume, mix and productivity effects.

## SLA Analysis Framework

1. Confirm the SLA definition, start/stop events, target, business calendar, priority and exclusions.
2. Validate timestamps, status transitions, reopenings, pauses and missing records.
3. Calculate eligible volume, met/breached counts and rate using approved logic.
4. Segment breaches by service, priority, team, age, reason and period.
5. Distinguish demand spikes, capacity constraints, routing, rework, dependencies and data defects.
6. Recommend action with owner, timing, expected indicator and monitoring plan.

## Executive Storytelling Structure

1. **Headline:** What changed and why it matters.
2. **Evidence:** Two or three verified metrics and trends.
3. **Drivers:** Which segments explain the movement.
4. **Implication:** Effect on service, capacity, cost, client or risk.
5. **Recommendation:** Action, owner, timing and decision required.
6. **Appendix:** Definitions, sources, controls, assumptions and limitations.

## Data Quality and Multi-Source Reconciliation

- Confirm source ownership, grain, keys, refresh time, history and status definitions.
- Profile nulls, duplicates, ranges, referential integrity and schema changes.
- Avoid duplicate multiplication after joins.
- Reconcile record counts and control totals by stage and source.
- Maintain a mapping table for cross-system identifiers and statuses.
- Log exceptions, unmatched records, corrections and approvals.
- Communicate affected reports, business impact and prevention steps.

## Likely Case Questions

### SLA performance declined this month. What would you do?

Validate the SLA logic and data first. Compare demand, backlog, capacity, priority and service mix; segment breaches; examine staffing, routing, dependencies, rework and outages; distinguish verified causes from hypotheses; recommend actions and monitoring metrics.

### Two systems report different resource counts.

Confirm definitions, effective dates, employee/contractor scope, active-status rules, team mappings and refresh time. Reconcile identifiers, isolate unmatched records, identify the system of record, document the approved mapping and prevent local report patches from becoming competing truth.

### An executive asks for “a dashboard” without clear requirements.

Ask what decision must be made, who acts, how often, which outcomes matter and what currently fails. Propose a concise KPI definition sheet and prototype, validate against source controls and agree acceptance criteria before building broadly.

### A stakeholder challenges your recommendation.

Restate the question and definitions, show controls and evidence, separate findings from interpretation, invite domain context, test credible alternatives and revise the conclusion when stronger evidence appears.

## SQL and Excel Review

- SQL grain, keys, joins, null handling and duplicate control.
- CTEs for readable multi-stage logic.
- Conditional aggregation for status and SLA measures.
- Window functions for rank, lag, running totals and rolling trends.
- Date/time differences, business-calendar caveats and cohort comparisons.
- Reconciliation queries and exception tables.
- Excel pivot tables, formulas, lookups, conditional aggregations, date logic, charts and control tabs.

Discuss only functions Jainali can confidently demonstrate.

## Behavioural Stories

- **Ambiguous requirement:** AYLA—translated stakeholder questions into structured analytical tasks.
- **Workforce analysis:** HR project—headcount, compensation, performance, attendance, hiring and tenure.
- **Data quality:** E-commerce project—keys, revenue rules, validation and GitHub Actions.
- **Coordination:** Trans Globe Education—managed records and updates across students and institutions.
- **Confidentiality:** Arihant Investment—maintained accurate confidential client records.

Use Situation, Task, Action and Result. When no quantified outcome is verified, finish with the factual deliverable or improved clarity.

## Questions to Ask

1. Which business area, operational processes and executive audiences would this analyst support first?
2. What are the primary ServiceNow, LiveLink and other source datasets and systems of record?
3. Which capacity, SLA, resource and performance metrics are currently governed and standardized?
4. What level of independent Power BI ownership is expected during the first 90 days?
5. How are requirements, dashboard validation and business sign-off managed with the client?
6. What distinguishes a useful executive insight from a technically correct report on this team?
7. What onboarding supports CGI Partners who are learning a client's enterprise platforms and domain?

## 30-60-90 Day Approach

- **First 30 days:** Learn client processes, systems, definitions, report catalogue, stakeholders, quality controls and Power BI standards; reproduce trusted SQL/Excel outputs.
- **Days 31-60:** Own a bounded recurring report under review, document mappings and exceptions, support a requirements session and build a supervised dashboard component.
- **Days 61-90:** Deliver an approved reporting or quality improvement, present findings clearly, document user guidance and monitor quality, performance and adoption.

## Accuracy Guardrails

- Do not claim interactive Power BI implementation, ServiceNow, LiveLink, enterprise integration, executive reporting, workshop facilitation, capacity/SLA forecasting or financial-services analytics.
- Do not describe portfolio projects as production enterprise systems.
- Do not imply Canadian education or work experience.
- Do not invent quantified impact, dataset volumes, work authorization, language proficiency, client ownership or senior stakeholders.

## Official Research

- [CGI Canada — Data Analytics](https://www.cgi.com/canada/en-ca/data-analytics): official Canadian analytics capabilities, governance, dashboards and operational improvement context.
- [CGI Careers — Be an Owner](https://www.cgi.com/en/careers/be-an-owner): ownership culture, participation, collaboration and collective success.
- [CGI Careers](https://www.cgi.com/careers/our-benefits): ownership, client value, creativity, development, teamwork and belonging.
- [CGI Canada — Services](https://www.cgi.com/canada/en-ca/services): Canadian consulting, analytics, systems integration and industry context.

Recheck the posting, client requirements and approved enterprise-system definitions immediately before the interview.
