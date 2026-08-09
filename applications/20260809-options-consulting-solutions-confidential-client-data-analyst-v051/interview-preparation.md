# Data Analyst — Reference 13997 Interview Preparation

## Application Context

- Recruiting firm: Options Consulting Solutions.
- Recruiter: Rujeeka Manoharan, Temporary Division.
- Client: confidential.
- Location: Mississauga, Ontario; hybrid.
- Term: 12-month contract.

The role combines data analysis, Excel/Power BI reporting, records management, stakeholder follow-up, administrative support, and process improvement. It also explicitly requires Power BI dashboards from scratch, SharePoint, and Power Automate. Those three requirements are not verified experience and must be handled honestly.

## 90-Second Introduction

“I completed a Master of Business Analytics at Edith Cowan University in Australia and now live in Toronto. My analyst foundation comes from my Data Intern role at AYLA Solutions, where I gathered reporting requirements, supported SQL extraction and validation, prepared advanced Excel reports, and contributed dashboard insights for performance tracking. My projects strengthen that foundation: I have designed operational and financial KPIs, created repeatable validation controls, analyzed trends, and documented recommendations. My GST adoption research also required Excel formulas, sorting, filtering, pivot tables, percentages, and charts. Earlier support and administrative roles developed my records accuracy, confidential documentation, stakeholder follow-up, and ability to manage competing deadlines. My Power BI work is currently KPI and dashboard planning rather than completed interactive implementation, and I have not yet administered SharePoint or Power Automate. I am transparent about those gaps and prepared to demonstrate how my reporting, controls, and process foundation can transfer while I build those capabilities.”

## Strongest Evidence

- Advanced Excel reporting at AYLA.
- Excel formulas, sorting, filtering, pivot tables, percentages, and charts in Online GST Filing Adoption Research.
- SQL/PostgreSQL analysis, KPI definition, validation, and trend analysis across published projects.
- Reporting requirements and dashboard insights at AYLA.
- Accurate records, documentation, client communication, and follow-up coordination at Trans Globe and Arihant.
- Power BI KPI, visualization, and dashboard planning across the three GitHub projects.

## Critical Gaps

- No completed or published interactive Power BI dashboard.
- No `.pbix` portfolio artifact.
- No SharePoint administration.
- No Power Automate workflow implementation.
- No incident, audit, inspection, corrective-action, or compliance-tracking employment.
- No verified leadership-reporting cadence or two to three years as a data analyst.

## Excel Preparation

Be ready to demonstrate these concepts hands-on. Only claim proficiency after practising them:

- Cleaning: trim spaces, standardize cases/dates, remove duplicates, handle blanks, and validate types.
- Formulas: `SUMIFS`, `COUNTIFS`, `AVERAGEIFS`, `IF`, `IFS`, `IFERROR`, `XLOOKUP`, `INDEX/MATCH`, date functions, and text functions.
- Tables: structured references, named ranges, totals, filters, and calculated columns.
- Pivot tables: correct source grain, grouping, calculated fields where appropriate, slicers, refresh, and pivot charts.
- Controls: duplicate checks, missing-field checks, allowed values, reconciliation totals, conditional formatting, and data validation lists.
- Charts: select the visual based on the question; label clearly; avoid unnecessary decoration.
- Reporting: separate input, transformation, control, calculation, and output areas.
- Power Query: import, type, filter, merge, append, unpivot, standardize, and refresh. Treat this as a study item unless completed hands-on.

## Building a Power BI Dashboard from Scratch

This is interview preparation, not a claim of completed experience.

1. Clarify the users, decisions, reporting cadence, and success measures.
2. Inventory sources, owners, grain, refresh timing, and data-quality risks.
3. Use Power Query to clean and shape data.
4. Build a star schema with facts, dimensions, stable keys, and one-to-many relationships.
5. Create a dedicated date table and mark it appropriately.
6. Write explicit DAX measures for KPIs rather than relying on implicit aggregation.
7. Design an executive summary, trends, exceptions, drill-downs, filters, and action view.
8. Apply definitions, titles, units, last-refresh information, and accessible colour choices.
9. Validate totals against source/Excel, test filters, edge cases, refresh, and performance.
10. Publish, control permissions, document ownership, gather feedback, and monitor use.

### DAX Concepts to Practise

- Measures versus calculated columns.
- Filter context and row context.
- `CALCULATE`, `FILTER`, `DIVIDE`, `DISTINCTCOUNT`, `SUMX`, `RELATED`, and `SELECTEDVALUE`.
- Time intelligence with a valid date table.
- Variance, completion rate, overdue count, rolling trend, and status metrics.

Safe answer: “My completed Power BI evidence is dashboard and KPI planning, not an implemented dashboard. I understand the end-to-end build process and am developing hands-on Power Query, modelling, DAX, validation, and publishing skills, but I would not describe that as production experience yet.”

## Reporting Cadence Design

### Weekly

- New incidents/actions, overdue items, near-term deadlines, exceptions, and ownership.
- Short, operational, action-oriented.

### Monthly

- KPI performance, trends, root causes, corrective-action status, and management commentary.
- Reconcile totals before publication.

### Quarterly

- Directional trends, recurring issues, audit/compliance themes, process performance, and forecast risks.

### Annual

- Full-year performance, targets, recurring patterns, completed improvements, unresolved risks, and priorities.

For every report define owner, source, cut-off, refresh date, approval, audience, distribution, retention, and correction process.

## Records and Compliance Tracking

A defensible tracker should include:

- Unique record ID.
- Type: incident, audit finding, inspection, corrective action, or other controlled category.
- Description and source.
- Date opened, due date, and closed date.
- Severity, priority, status, and owner.
- Root cause and required action.
- Evidence/document link.
- Follow-up date and escalation flag.
- Closure approval and audit trail.

Controls:

- Required-field validation.
- Controlled vocabularies for status/type/priority.
- Duplicate prevention.
- Overdue and missing-owner exceptions.
- Change history and role-based access.
- Reconciliation between source documents and tracker.
- Regular review of open and aging items.

Do not claim prior compliance-tracking experience; explain this as the structure you would use.

## SharePoint Fundamentals

Study concepts only:

- Sites, document libraries, lists, pages, columns, views, metadata, content types, and version history.
- Prefer metadata and controlled views over deeply nested folders.
- Permissions should follow least privilege and clear ownership.
- Use list/library validation, required fields, versioning, retention, and audit features where appropriate.
- Define naming standards, document ownership, review dates, archival, and recovery.

Safe answer: “I have not administered SharePoint. My related evidence is structured records, documentation, and workflow coordination. I would learn the client's information architecture, permissions, retention requirements, and site-governance standards before making changes.”

## Power Automate Fundamentals

Example action-reminder workflow:

1. Trigger when a SharePoint list item is created or modified.
2. Validate required fields and avoid recursive updates.
3. Calculate whether the item is approaching or past due.
4. Send a notification to the owner and copy/escalate according to rules.
5. Update reminder status and timestamp.
6. Log failures and provide an owner for exceptions.
7. Test normal, missing-data, duplicate, overdue, and permission scenarios.
8. Document connection owners, service accounts, dependencies, and recovery.

Safe answer: “I have not built Power Automate workflows. I understand the trigger-action-condition structure and would start with a controlled, low-risk reminder process, test edge cases, and document ownership before broader automation.”

## Stakeholder Follow-Up System

- Record action, owner, due date, dependency, evidence required, and status.
- Confirm understanding during or immediately after the meeting.
- Send concise notes and make ownership visible.
- Review upcoming and overdue actions on a defined cadence.
- Escalate early with context, business impact, and a proposed next step.
- Close only after evidence or approval is recorded.

## Evidence Stories

### AYLA — Reporting Requirements to Output

- Situation: A reporting request required clarification and reliable analytical support.
- Task: Help translate the request into a structured output.
- Action: Gathered requirements, supported SQL extraction and validation, prepared an advanced Excel report, and contributed dashboard insights.
- Result: Supported performance reporting with maintained documentation.
- Guardrail: no invented dataset size, delivery time, stakeholder count, or quantified result.

### GST Research — Excel Analysis

- Situation: Small-business survey responses needed to be organized and interpreted.
- Task: Identify adoption patterns and barriers.
- Action: Designed the Google Forms survey and used Excel formulas, sorting, filtering, pivot tables, percentages, and charts to analyze responses.
- Result: Documented findings and recommendations and earned an A grade.

### Trans Globe — Records and Follow-Up

- Situation: Application records and updates had to remain accurate across students and institutions.
- Task: Maintain documentation and coordinate status updates.
- Action: Managed records, coordinated follow-ups, supported reporting, and communicated with clients and institutions.
- Result: Supported organized workflow progress and reliable records.

### E-Commerce — Controls and KPI Reporting

- Situation: Transactional data required consistent business rules before reporting.
- Task: Create defensible revenue, customer, product, and payment KPIs.
- Action: Built a relational PostgreSQL model, defined recognized-revenue logic, added integrity checks and repeatable validation, analyzed trends, and documented recommendations.
- Result: Produced reproducible analytical findings and Power BI dashboard planning.

## Likely Interview Questions

1. **What is your Power BI experience?** Use the honest planning-versus-implementation answer above.
2. **How would you create a dashboard from scratch?** Use the ten-step Power BI framework.
3. **How do you ensure report accuracy?** Define rules, validate inputs, reconcile totals, test exceptions, review outputs, and document corrections.
4. **Tell me about your advanced Excel experience.** Use AYLA and GST examples; be ready for a practical test.
5. **How would you manage weekly through annual reporting?** Explain purpose, cut-off, controls, commentary, ownership, and distribution at each cadence.
6. **How would you follow up on overdue corrective actions?** Maintain a controlled action log, send reminders, escalate based on severity/age, and close with evidence.
7. **What is your SharePoint experience?** State none; connect to records/documentation and explain the learning approach.
8. **What is your Power Automate experience?** State none; describe a safe reminder workflow conceptually.
9. **How do you prioritize competing requests?** Assess business impact, urgency, risk, decision deadline, dependencies, and effort; confirm trade-offs and communicate status.
10. **Why a 12-month contract?** Emphasize readiness to learn quickly, deliver defined reporting/coordination outcomes, and contribute during a focused assignment.

## Practical Case

Scenario: leadership says the monthly dashboard shows 20 overdue corrective actions, while the SharePoint tracker shows 27.

Approach:

1. Pause or flag the dashboard if the discrepancy affects decisions.
2. Confirm definitions of overdue, open, closed, cancelled, and due date.
3. Check refresh time, filters, permissions, and reporting cut-off.
4. Compare record IDs between the two outputs.
5. Test missing IDs, duplicates, null due dates, status mappings, time zones, archived items, and failed refreshes.
6. Identify the first stage where the seven records disappear.
7. Correct the mapping/query/workflow and re-run validation.
8. Communicate cause, affected reporting, correction, and confidence.
9. Add a reconciliation control so the discrepancy is detected before future publication.

## Questions for Ms. Manoharan or the Client

- Which dashboards and reporting cycles would the contractor own first?
- What is the balance between Excel reporting, Power BI development, SharePoint administration, and Power Automate work?
- Are existing datasets and dashboards available, or is the assignment primarily greenfield development?
- What compliance or operational framework governs the incidents, audits, and corrective actions?
- What level of Power BI technical assessment is included in the interview process?
- What would excellent performance look like after the first 90 days?

## 30-60-90 Day Plan

- First 30 days: learn data definitions, reporting calendar, stakeholders, records controls, current dashboards, SharePoint structure, workflows, and approval standards; reproduce an existing report with review.
- Days 31–60: support recurring Excel reporting, maintain action records, strengthen validation, and contribute to a controlled Power BI or workflow enhancement with guidance.
- Days 61–90: independently own defined reporting and follow-up tasks, document procedures, and recommend one practical improvement to accuracy, timeliness, or efficiency.

## Final Guardrails

- Never claim completed Power BI dashboards, `.pbix` files, SharePoint administration, or Power Automate implementation.
- Never claim compliance, incident, audit, inspection, or corrective-action employment.
- Never claim weekly/monthly/quarterly/annual leadership-report ownership.
- Never inflate analyst tenure or imply Canadian employment/education.
- Retain `Data Intern` and calibrated verbs such as `supported`, `contributed`, and `participated`.
- Never invent metrics, savings, dataset sizes, stakeholder counts, or outcomes.

## Official Research Sources

- Options Consulting Solutions: https://www.optionscs.com/
- About Options Consulting Solutions: https://www.optionscs.com/about-us
- Options Consulting Solutions Team: https://www.optionscs.com/our-team
