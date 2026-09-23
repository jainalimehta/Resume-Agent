# Interview Preparation — Bell BI Data Analyst I

## Candid Positioning

This is a high-risk stretch. Position yourself as an early-career analyst with strong relational SQL, KPI reasoning, validation, requirements, advanced Excel, and Agile collaboration—not as a production BI developer. SAS, enterprise BI maintenance, data warehousing, telecom experience, large-scale data, and management presentations are gaps.

## 60-Second Introduction

> I live in Toronto and completed a Master of Business Analytics at Edith Cowan University in Australia. As a Data Intern at AYLA Solutions, I gathered reporting requirements, supported SQL extraction and validation, prepared advanced Excel reports, and contributed performance insights through Agile planning and reviews. I have also published PostgreSQL projects in e-commerce, healthcare, and workforce analytics. These projects required relational modelling, KPI definitions, CTEs and window functions, repeatable validation, and recommendations grounded in the outputs. My current experience is stronger in SQL, Excel, and Power BI planning than in SAS or production BI maintenance, but the role fits the way I work: clarify the business driver, test the data carefully, explain the result, and keep learning.

## Why Bell and Consumer BI

> Bell's Consumer BI role connects performance measurement with decisions that affect customers and business outcomes at national scale. I am interested in working where KPI definitions, reporting accuracy, and cross-functional communication directly influence priorities. Bell also emphasizes current technology and formal training, which is attractive because I can contribute my SQL, validation, reporting-requirements, and analytical foundation while developing deeper SAS and production BI capability.

## Evidence Story 1 — AYLA Requirements and Reporting

**Situation:** Analytical work required clear business and reporting requirements and dependable reporting support.

**Task:** Support extraction, validation, reporting, and communication as a Data Intern.

**Action:** Gathered and documented requirements, supported SQL-based extraction and validation, prepared advanced Excel reports, contributed reporting insights, and participated in Agile planning and review sessions.

**Result/Purpose:** Supported structured performance reporting and maintained usable analytical documentation.

Do not add stakeholder counts, project names, management audiences, deadlines, or quantified improvements.

## Evidence Story 2 — E-Commerce Performance Measurement

**Situation:** Transactional information across customers, orders, products, line items, and payments needed a coherent analytical structure.

**Task:** Build a relational model and define useful performance measures.

**Action:** Created keys and integrity checks, defined recognized revenue to exclude pending/refunded/cancelled activity, and analyzed spend, order frequency, product ranking, monthly revenue, and payment methods using SQL. Added repeatable validation and planned Power BI KPIs, views, filters, and drill paths.

**Result/Purpose:** Produced traceable findings and recommendations based on validated SQL outputs.

Be ready to explain the grain of each table and how one-to-many joins can inflate totals.

## Evidence Story 3 — Bank of Baroda Customer Analysis

**Situation:** Customer transaction patterns needed to be organized and interpreted.

**Task:** Analyze the information and present useful recommendations.

**Action:** Used Excel and SQL for cleaning, visualization, and trend analysis, then presented findings and recommendations for customer engagement and service delivery.

**Result/Purpose:** Connected transaction patterns to practical customer-focused recommendations.

Do not invent the audience, data size, bank adoption, or business impact.

## Performance-Measurement Framework

When asked to design a KPI:

1. Clarify the decision, audience, and business driver.
2. Define the numerator, denominator, grain, population, exclusions, time period, and comparison baseline.
3. Identify the authoritative source and refresh timing.
4. Check duplicates, nulls, missing relationships, status logic, and date boundaries.
5. Reconcile to an accepted control and document the definition.
6. Select a visual that makes the change, trend, or exception immediately clear.
7. Explain the result, likely drivers, limitations, and recommended next action.

## Bell Mobility Metrics to Understand

- **Subscriber base:** active subscribers under Bell's reporting definition.
- **Gross activations:** new customer/service activations before deactivations.
- **Net activations:** activations less deactivations for the period.
- **Churn:** the rate at which existing subscribers cancel service.
- **ARPU:** average revenue per user; Bell defines mobile blended ARPU using wireless external services revenue divided by the average mobile-phone subscriber base, expressed monthly.
- **Connected-device activations:** additions related to IoT and other connected devices.

Interview scenario: if churn improves but ARPU declines, investigate pricing/discounts, customer and plan mix, overage, roaming, retention offers, activations, geography, brand, and cohort behaviour before recommending action. Do not assume causation from an aggregate trend.

## BI Quality-Assurance Checklist

- Confirm requirement, KPI definition, expected grain, and acceptance criteria.
- Validate source-to-report row counts and control totals.
- Check duplicates, nulls, relationship cardinality, filters, and date boundaries.
- Test calculations against manual samples and edge cases.
- Test period, segment, channel, and status filters.
- Verify labels, formats, sorting, tooltips, and refresh timestamp.
- Check security/access expectations and sensitive-data exposure.
- Record defect, steps to reproduce, expected versus actual result, severity, owner, and retest outcome.
- Obtain stakeholder acceptance before release.

Say explicitly that this is your proposed QA approach; do not imply you performed production BI QA at AYLA.

## SQL Topics to Practise

- `INNER JOIN` versus `LEFT JOIN` and their effect on missing matches.
- Diagnosing row multiplication after one-to-many joins.
- `WHERE` versus `HAVING`.
- CTEs versus subqueries.
- `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LAG`, and running totals.
- Monthly KPI trends with date grouping and consistent period boundaries.
- Duplicate detection at a declared grain.
- Reconciliation between detail and aggregate totals.
- Null handling and explicit status exclusions.

Example verbal answer:

> Before writing the final query, I define the output grain. I aggregate child tables such as line items or payments to the required grain before joining when necessary, then compare counts and totals before and after each join. I test known records, duplicate keys, nulls, and excluded statuses. That prevents a technically valid join from producing a misleading KPI.

## SAS Gap Answer

> I do not yet have hands-on SAS experience, so I would not present SQL knowledge as equivalent. I understand that SAS can access, transform, analyze, and report data, and that PROC SQL provides SQL-style querying within SAS. My transferable foundation is relational SQL, analytical logic, validation, and documented reporting. I would learn Bell's actual SAS environment and coding standards through formal training, reproduce an existing controlled report, compare results with the current output, and seek review before taking independent ownership.

Never claim SAS coursework, certification, PROC SQL use, SAS Viya, macros, or SAS Enterprise Guide.

## Power BI and Production BI Gap Answer

> I have completed dashboard planning across my three published projects: KPI definitions, page structure, visual requirements, filters, and drill paths. I have not published interactive `.pbix` dashboards or maintained production BI assets. I can contribute the SQL, metric logic, requirements, QA thinking, and documentation immediately while building hands-on development skill through Bell's tools and review process.

## Large and Complex Data Gap Answer

> I have worked with multi-table relational structures and complex analytical logic, but I do not claim enterprise-scale volume because my dataset sizes are not verified. The practices I would carry forward are defining grain, using keys and constraints, validating cardinality, profiling nulls and duplicates, reconciling totals, and designing work in testable steps. I would learn Bell's performance, access, and platform standards before working independently on large production data.

## Management-Presentation Gap Answer

> I have presented analytical findings and recommendations, but I do not have verified experience presenting to multiple management levels. My approach would be to lead with the decision, show the minimum evidence required, distinguish fact from interpretation, make the recommendation and trade-offs clear, and prepare backup detail for technical questions.

## Prioritizing Multiple Requests

> I would confirm the business impact, deadline, dependency, effort, and risk for each request. I would separate production defects and decision-critical deadlines from enhancements, agree priorities with the appropriate owner, make trade-offs visible, and communicate early when a dependency changes. I would track the requirement, status, next action, owner, and due date so that urgent work does not make other commitments disappear.

## Likely Questions

- Walk me through a report or analysis from request to recommendation.
- How do you define a reliable KPI?
- How did you validate recognized revenue?
- How would you investigate a sudden change in churn or ARPU?
- How do you prevent duplicate rows when joining complex tables?
- What BI quality checks would you complete before release?
- Describe your exact Power BI experience.
- What is your SAS experience?
- Have you worked with large datasets or data warehouses?
- Tell me about an ambiguous requirement.
- How do you manage simultaneous ad hoc and planned work?
- How would you present a technical finding to management?
- Why Bell Mobility and why Consumer BI?
- Can you attend the office at least three days each week?

## Questions to Ask Bell

- Which reporting assets and business functions would this analyst support first?
- What proportion of the role is SAS, SQL, BI development, QA, and ad hoc analysis?
- Which visualization platform does Consumer BI use most frequently?
- How are KPI definitions governed and reconciled across business and IT teams?
- What training path is available for SAS and Bell's data environment?
- What ownership would be expected in the first 30, 60, and 90 days?
- How does the team intake, prioritize, test, and release reporting requests?

## Never Claim

- SAS, Oracle, SQL Server, Teradata, MicroStrategy, or enterprise data-warehouse experience.
- Published or implemented Power BI dashboards or `.pbix` files.
- Production BI asset maintenance, automation, or QA ownership.
- Work with large datasets when scale is unknown.
- Telecommunications experience or Bell-specific system knowledge.
- Management presentations, cross-functional influence, leadership, or project counts not in the evidence.
- Canadian education or Canadian work experience.
- Metrics, dataset sizes, savings, accuracy improvements, deadlines, or business adoption that were not confirmed.

## Official Study Sources

- Bell job posting: https://jobs.bce.ca/bell/job/Mississauga-BI-Data-Analyst-I-ON/1429810700/
- BCE 2025 results and KPI definitions: https://www.bce.ca/news-and-media/newsroom?article=bce-reports-2025-q4-and-full-year-results-announces-2026-financial-targets
- BCE annual reports: https://www.bce.ca/investors/financial-reports/annual-documents
- SAS SQL documentation: https://documentation.sas.com/api/docsets/sqlug/9.4/content/sqlug.pdf?locale=en

