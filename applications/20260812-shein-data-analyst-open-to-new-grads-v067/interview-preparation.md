# SHEIN — Data Analyst (Open to New Grads) Interview Preparation

## 60-Second Introduction

“I am an early-career Business Analytics graduate living in Toronto. At AYLA Solutions in Australia, I gathered reporting requirements, supported SQL extraction and validation, prepared advanced Excel reports, contributed dashboard insights, and participated in Agile planning and reviews. My most relevant portfolio project is E-Commerce Sales Analytics, where I modelled customers, products, orders, line items, and payments; defined recognized revenue; analyzed spend, order frequency, product rankings, monthly trends, and payment methods; and added repeatable validation. I am interested in SHEIN because reliable data and clear operating metrics are central to an agile, global supply chain.”

## Four Stories to Prepare

1. **E-commerce KPI integrity:** Explain the recognized-revenue rule, why pending/refunded/cancelled activity was excluded, and how primary keys, foreign keys, uniqueness, and checks protected the analysis.
2. **Operational trend analysis:** Explain monthly revenue, product rankings, customer spend, order frequency, and how you would turn an observed pattern into a testable business question.
3. **Cost and workflow analysis:** Use the healthcare project to explain treatment costs, appointment completion, billing status, clinician workload, and insurance claims without implying logistics experience.
4. **Accurate documentation under coordination pressure:** Use Trans Globe to explain maintaining records and coordinating process updates with students and institutions.

## Supply Chain Metrics to Understand

- Order cycle time and on-time delivery rate
- Cost per shipment/order and cost per delivery segment
- First-attempt delivery success
- Carrier/vendor performance
- Inventory turnover, days of inventory, stockout rate, and sell-through
- Forecast accuracy and forecast bias
- Return rate and reasons
- Customs clearance time and exception rate
- Damage, loss, and documentation-error rates

Do not claim to have measured these professionally. Explain how you would define the denominator, grain, period, filters, source systems, and ownership before reporting them.

## A Strong Analysis Framework

When asked how you would investigate rising last-mile cost:

1. Confirm the metric definition and whether cost is total, per order, per parcel, per kilometre, or per successful delivery.
2. Validate source completeness, duplicates, currency, time zones, cancellations, returns, and allocation logic.
3. Segment by geography, carrier, service level, package characteristics, route, delivery attempt, and time period.
4. Compare trends against volume, mix, fuel or surcharge changes, failed deliveries, and SLA performance.
5. Quantify the largest drivers, test alternative explanations, and recommend a controlled action with success and risk measures.

## Honest Gap Answers

### “What logistics experience do you have?”

“I have not worked professionally in logistics. My transferable evidence is e-commerce data modelling and KPI analysis, advanced Excel reporting, SQL validation, operational analysis, and Supply Chain Analytics coursework. I would learn SHEIN's process, terminology, source systems, metric definitions, and regulatory controls from operational experts before recommending changes.”

### “How strong is your Python?”

“Python is a current development area rather than a skill I claim today. My strongest hands-on tools are SQL, PostgreSQL, and advanced Excel. I understand the analytical workflow I would transfer into Python—loading data, cleaning types and missing values, validating joins and totals, grouping and aggregating, and producing reproducible outputs—and I am ready to build that capability.”

### “Have you managed budgets or forecasts?”

“I have not owned annual or monthly logistics budgets or forecasts. My adjacent experience is defining revenue logic and analyzing treatment costs and performance trends. I understand that budget work requires a controlled baseline, actual-versus-budget variance, volume and rate drivers, forecast assumptions, ownership, and documented explanations.”

### “Do you know customs compliance?”

“I do not have customs or import-compliance experience. I do have verified experience maintaining accurate client and confidential records. In this role, I would first learn the required document types, data fields, approval points, retention rules, exception paths, and escalation procedures, then use checklists and reconciliations to support accuracy.”

## Technical Questions to Practice

- Explain `INNER JOIN` versus `LEFT JOIN` for orders and shipments.
- Find duplicate tracking numbers or orders with no shipment record.
- Calculate on-time delivery rate while handling cancelled orders and missing promised dates.
- Use a window function to rank carriers or products within each region.
- Calculate a rolling average, month-over-month change, and cumulative cost.
- Explain how you would validate a dashboard total against source data.
- Explain the difference between a trend, correlation, operational driver, and causal conclusion.

## Strong Questions for SHEIN

1. Which logistics decisions and KPIs would this analyst support most frequently?
2. What are the primary data sources and how are metric definitions governed across operations and finance?
3. Which mid-mile or last-mile cost drivers are currently most important to understand?
4. How does the team validate import documentation and escalate customs exceptions?
5. What would successful performance look like during the first 90 days for a new graduate?

## Interview Guardrails

- Say `Supply Chain Analytics coursework`, not professional supply-chain experience.
- Say `analyzed treatment costs and revenue logic`, not budget or cost-management ownership.
- Say `managed accurate records`, not customs-compliance experience.
- Say `Power BI KPI and dashboard planning`, not implemented dashboards.
- Say clearly that Python is a learning priority, not a current proficiency.
- Describe AYLA as `Data Intern`, never Data Analyst Intern.
