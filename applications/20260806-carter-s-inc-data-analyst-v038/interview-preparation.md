# Interview Preparation — Data Analyst, Carter's Planning & Allocation

## Fit Reality

This is a significant stretch. Jainali has a relevant master's degree, Australian Data Intern experience, SQL, advanced Excel, retail-relevant e-commerce analysis, data validation, KPI/reporting requirements, Power BI planning, and stakeholder communication. She does not meet the explicit Tableau or 2-3-year analyst requirements and lacks professional retail planning/allocation, large retail datasets, production dashboard ownership, BI training, and senior-leadership reporting. The interview approach must be transparent and evidence-led.

## 90-Second Introduction

“I currently live in Toronto, while my education and work experience are international. I completed a Master of Business Analytics at Edith Cowan University in Australia and an Integrated MBA at Atmiya University in India. As a Data Intern at AYLA Solutions in Australia, I gathered reporting requirements, supported SQL extraction and validation, and prepared advanced Excel reports and dashboard insights. My E-Commerce Sales Analytics project models customers, products, orders, line items, and payments and analyzes spend, order frequency, product rankings, monthly revenue, and payment methods using SQL. I added explicit revenue rules, repeatable validation, GitHub Actions, AI-assisted recommendations grounded in SQL, and Power BI dashboard planning. I have not used Tableau and do not have two to three years of analyst employment or professional retail-planning experience. I would bring strong SQL and Excel fundamentals, careful data-quality thinking, retail-relevant portfolio evidence, and a structured approach to learning Carter's BI and planning environment.”

## Why Carter's?

- Carter's connects planning and allocation decisions to availability, customer experience, and service for families with young children.
- The role combines SQL analysis, data quality, standardized reporting, BI, business partnership, and operational improvement.
- Carter's emphasizes meaningful work, learning, inclusion, collaboration, innovation, customer focus, and development programs.
- Planning and allocation would allow Jainali to extend e-commerce customer, product, revenue, and KPI analysis into a practical retail operating context.

## Honest Tableau and Experience Gap Answer

“I want to be direct: I have not used Tableau, and I do not have two to three years of Data Analyst employment. My hands-on foundation is PostgreSQL, SQL, advanced Excel, relational modelling, repeatable validation, and Power BI dashboard planning rather than implementation. I understand that Tableau is a must-have here, so I would not present planning work as equivalent experience. If considered, I would learn against Carter's real reporting standards: understand an approved dashboard and source definitions, rebuild a bounded view in a sandbox, reconcile every KPI to control totals, document filters and calculations, seek review, and only then expand ownership.”

## Retail Planning and Allocation Fundamentals

Use this as interview learning, not employment experience:

- **Merchandise planning:** Aligning sales, inventory, margin, and receipt plans with business targets.
- **Assortment planning:** Deciding which products, styles, colours, and sizes should be offered by channel or location.
- **Allocation:** Distributing available inventory across stores or channels based on demand, capacity, presentation needs, and constraints.
- **Replenishment:** Restocking inventory according to demand and inventory policies.
- **Markdown:** Price reduction used to support sell-through or clear inventory; assess margin and inventory implications.
- **Seasonality:** Demand patterns linked to calendar, weather, holidays, product lifecycle, and events.
- **Hierarchy:** Product may roll from SKU to style, subcategory, category, department, and brand; location may roll from store to region and channel.

Confirm Carter's definitions and systems before using any metric operationally.

## Retail KPI Framework

- **Net sales:** Revenue after approved returns, discounts, and other adjustments.
- **Units sold:** Quantity sold under an agreed status and time basis.
- **Average unit retail:** Sales divided by units sold, subject to approved net-sales definition.
- **Average transaction value:** Sales divided by transactions.
- **Units per transaction:** Units sold divided by transactions.
- **Sell-through:** Units sold relative to available or received inventory under an approved definition.
- **Inventory turnover:** Cost of goods sold relative to average inventory, usually over a period.
- **Weeks of supply:** Inventory relative to expected weekly demand.
- **In-stock rate:** Availability of eligible items under a defined channel/location basis.
- **Markdown rate:** Markdown amount relative to an agreed sales or inventory basis.
- **Gross margin:** Net sales less cost of goods sold, expressed in dollars or as a rate.
- **Forecast variance:** Actual versus forecast under consistent product, location, and time grain.

Always define numerator, denominator, period, grain, currency, channel, returns, cancellations, and refresh timing.

## Data Validation and Troubleshooting

When a retail report looks wrong:

1. Confirm business definition, report period, time zone, refresh time, product/location hierarchy, and filters.
2. Reconcile row counts, units, sales, cost, inventory, and transaction totals to authoritative controls.
3. Check duplicate multiplication after joins, missing keys, nulls, late-arriving transactions, returns, cancellations, and status mappings.
4. Compare store, e-commerce, region, product, category, brand, and date segments to isolate the issue.
5. Verify calculation logic and filter behaviour in both SQL and the BI layer.
6. Document root cause, affected reports, business impact, correction, validation evidence, and prevention.
7. Communicate clearly to users and update training or metric documentation when required.

## Dashboard Design Framework

1. Start with user, decision, frequency, and action—not the visualization.
2. Define certified sources, grain, dimensions, measures, calculations, and refresh expectations.
3. Put headline KPIs and exceptions first; provide trend and driver analysis beneath them.
4. Use consistent product, location, time, and channel filters.
5. Make definitions, refresh time, scope, and caveats visible.
6. Test totals, filters, drill paths, edge cases, permissions, and performance.
7. Provide a short user guide and a route for questions or defects.

## SQL Topics to Review

- Retail grain: transaction, line item, SKU-location-day, inventory snapshot, and purchase order.
- Customer, product, location, channel, calendar, sales, inventory, and payment relationships.
- Joins without duplicate multiplication.
- Conditional aggregation for completed, returned, cancelled, and pending activity.
- CTEs for staged logic and readable queries.
- Window functions for rankings, running totals, lag, rolling trends, and contribution.
- Product and location hierarchy aggregation.
- Period comparisons and seasonality.
- Reconciliation queries, exception tables, and data-quality tests.

## Excel and BI Review

- Pivot tables, filters, charts, conditional formatting, lookup logic, conditional aggregations, date functions, and error handling.
- Separate raw data, mappings, assumptions, calculations, validation, summaries, and presentation tabs.
- Review Tableau concepts: dimensions versus measures, discrete versus continuous fields, filters, level of detail, calculated fields, table calculations, extracts versus live connections, parameters, dashboard actions, publishing, permissions, and performance.
- Do not claim Tableau practice until actual hands-on work is completed.

## Likely Case Questions

### Sales are below plan but units are stable. How would you investigate?

Validate definitions, then decompose sales into units and average selling price. Examine markdowns, promotions, returns, channel and product mix, price changes, region, seasonality, and data freshness. Compare like-for-like periods and communicate verified drivers separately from hypotheses.

### A category has strong sales but low availability. What would you analyze?

Check inventory snapshots, in-stock and sell-through definitions, store/channel allocation, replenishment, lead times, size/colour availability, stockouts, transfers, returns, demand forecast, and regional patterns. Recommend actions only after confirming constraints with planning and allocation partners.

### Two teams disagree about a KPI.

Return to the business question, metric owner, source, grain, formula, filters, timing, and exceptions. Reconcile both outputs, document the approved definition, obtain sign-off, and standardize the calculation in a governed reporting source.

### Senior leadership needs a short update.

Use a clear headline, the most material KPI movement, verified drivers, customer or business implication, recommendation, decision required, owner, timing, and an appendix with definitions and limitations.

## Behavioural Stories

- **Ambiguous requirement:** AYLA—translated stakeholder questions into structured analytical tasks.
- **Data accuracy:** E-commerce project—keys, revenue rules, validation, and GitHub Actions.
- **Insight to recommendation:** E-commerce project—SQL findings converted into documented AI-assisted recommendations and Power BI plans.
- **Cross-party coordination:** Trans Globe Education—coordinated process updates with students and institutions.
- **Confidentiality:** Arihant Investment—maintained accurate confidential client records.

Use Situation, Task, Action, and Result. Do not invent percentages, savings, dataset volumes, or stakeholders.

## Questions to Ask

1. Which planning and allocation decisions and reports would this analyst support first?
2. What are the main retail data sources, product/location hierarchies, and refresh expectations?
3. Which Tableau dashboards are standardized today, and where are the largest self-service reporting gaps?
4. How does the Canadian team collaborate with corporate BI on certified data and dashboard changes?
5. Which KPI definitions cause the most frequent reconciliation or interpretation challenges?
6. How are ad hoc requests prioritized against dashboard maintenance and project work?
7. What learning support is available for Carter's BI standards and retail planning fundamentals?

## 30-60-90 Day Approach

- **First 30 days:** Learn product/location hierarchies, planning calendar, sources, KPI definitions, report catalogue, controls, stakeholders, and Tableau standards; reproduce trusted SQL/Excel outputs.
- **Days 31-60:** Own a bounded recurring report under review, investigate exceptions, document definitions, and rebuild a supervised dashboard component in a safe environment.
- **Days 61-90:** Deliver an approved reporting or quality enhancement, prepare user guidance, present the business impact clearly, and monitor agreed quality and adoption measures.

## Accuracy Guardrails

- Do not claim Tableau, 2-3 years of Data Analyst experience, professional retail planning/allocation, large retail datasets, dashboard ownership, BI training, or senior-leadership presentation experience.
- Do not describe e-commerce portfolio analysis as retail employment.
- Do not describe Power BI planning as interactive dashboard implementation.
- Do not imply Canadian education or Canadian work experience.
- Do not invent quantified impact, dataset sizes, work authorization, language proficiency, or vendor/project ownership.

## Official Research

- [Carter's Careers](https://careers.carters.com/): official company, brands, learning, development, inclusion, and career-culture context.
- [Carter's Team Culture](https://careers.carters.com/our-culture): official values and emphasis on meaningful work, belonging, learning, inclusion, and innovation.
- [Carter's Corporate Careers](https://careers.carters.com/corporate-page): official corporate functions and Canadian corporate presence.
- [Carter's 2025 Annual Report](https://ir.carters.com/static-files/33d8b387-afdb-4a8b-8a64-a1ea979dae6f): current company and retail-business context.

Recheck the posting, company information, and current reporting environment immediately before the interview.
