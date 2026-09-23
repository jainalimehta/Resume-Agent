# Interview Preparation — Docebo Data Analyst

## Candid Positioning

I am an early-career analyst with a Master of Business Analytics, Australian Data Intern experience, and published PostgreSQL projects. My strongest direct evidence is SQL analysis, relational modelling, data validation, KPI definition, requirements documentation, Excel reporting, and translating validated outputs into recommendations. I am not presenting myself as a three-year Python, Snowflake, or dashboard-deployment specialist; I am presenting a rigorous foundation and a clear record of structured learning.

## 60-Second Introduction

I am a Business Analytics graduate living in Toronto. At AYLA Solutions in Australia, I gathered business and reporting requirements, supported SQL extraction and validation, prepared advanced Excel reports, and contributed insights for performance tracking while participating in Agile planning and reviews. My published portfolio extends that foundation across e-commerce, healthcare, and workforce analytics. I built normalized PostgreSQL models, used CTEs and window functions, defined KPI logic, added repeatable validation and GitHub Actions checks, and developed AI-assisted recommendations grounded in the SQL outputs. I am drawn to Docebo because the role combines analytical rigor, clear communication, AI, and real decisions within a learning-focused product company.

## Evidence Story 1 — Translating Reporting Needs at AYLA

**Situation:** Analytical work needed clearly defined business and reporting outputs.  
**Task:** Help clarify the need and support dependable reporting work.  
**Action:** Gathered and documented requirements, supported SQL-based extraction and validation, prepared advanced Excel reports, contributed dashboard insights, and communicated progress during Agile planning and reviews.  
**Result:** Supported structured analytical outputs for performance tracking and strengthened the traceability between the business question, source data, and reporting result.

## Evidence Story 2 — Making Revenue Logic Trustworthy

**Situation:** E-commerce activity included completed, pending, refunded, and cancelled transactions across connected tables.  
**Task:** Create a defensible data model and consistent KPI logic.  
**Action:** Connected customers, products, orders, line items, and payments in PostgreSQL; applied primary keys, foreign keys, uniqueness rules, and checks; defined recognized revenue to exclude pending, refunded, and cancelled activity; analyzed customer and product patterns; and added repeatable validation and GitHub Actions checks.  
**Result:** Produced validated SQL findings, documented KPI logic, Generative AI-assisted recommendations, and a defined Power BI dashboard plan.

## Evidence Story 3 — Turning Survey Data into Recommendations

**Situation:** The GST filing research examined adoption of online filing among small businesses in Gujarat.  
**Task:** Collect, organize, analyze, and explain the survey evidence.  
**Action:** Designed a Google Forms survey and used Excel formulas, sorting, filtering, pivot tables, percentages, and charts to analyze responses.  
**Result:** Identified adoption patterns and common barriers, documented findings and recommendations, and earned an A grade.

## Technical Answer Frameworks

### How do you move from a business question to an analysis?

1. Clarify the decision, audience, timeframe, and desired action.
2. Define the grain, population, dimensions, measures, exclusions, and KPI owner.
3. Identify source tables and assess keys, missingness, duplicates, and data limitations.
4. Build the smallest testable query or sample output.
5. Validate joins, totals, edge cases, and business definitions.
6. Interpret the result, distinguish evidence from assumptions, and recommend an action.
7. Document the logic so the output is reproducible.

### How do you validate a multi-table SQL analysis?

- Confirm primary and foreign keys and expected join cardinality.
- Compare row counts before and after each join.
- Check nulls, duplicates, valid ranges, and referential integrity.
- Reconcile totals to a trusted source or independent calculation.
- Test edge cases such as cancelled, refunded, pending, or missing records.
- Store validation queries alongside analytical queries and rerun them after changes.

### How would you explain a complex result to a non-technical audience?

Lead with the decision and the most important finding. Show one relevant KPI or visual, explain the business implication in plain language, state the recommended next action, and disclose any data limitation that could affect confidence.

### What makes a useful dashboard?

A useful dashboard starts with a decision, not a collection of charts. Each KPI needs a precise definition, owner, grain, timeframe, and comparison. Visual hierarchy should lead from overall performance to the drivers and then to the detail required for action. Data quality, refresh expectations, filters, and exceptions should be explicit.

## Gap Answers

### You do not have three years of analyst experience. Why should we consider you?

That requirement is a real gap. My direct analyst foundation is the 2025 Data Intern role plus substantial hands-on portfolio work, not three years of analyst employment. What I can demonstrate is disciplined SQL reasoning, normalized models, validation, KPI logic, requirements work, and clear recommendations across several domains. I would ask to be evaluated on the quality of that evidence and my learning trajectory rather than imply tenure I do not have.

### What is your Python experience?

Python is not part of the verified work I am presenting. My hands-on work is strongest in PostgreSQL, SQL, and advanced Excel. I would be transparent about that boundary, learn against the team's real analytical use cases, and apply the same validation and documentation discipline I use in SQL.

### Have you used Snowflake?

I have not used Snowflake in the verified experience represented here. My database work is PostgreSQL. The transferable concepts include relational modelling, data types, joins, aggregations, window functions, query validation, and translating business definitions into analytical logic, but I recognize Snowflake's architecture and operating practices require additional learning.

### Have you deployed interactive dashboards?

My published Power BI evidence is KPI, layout, and visualization planning rather than a deployed interactive `.pbix` artifact. I can explain the decision logic, measures, filters, visual hierarchy, and validation approach behind those plans, but I would not call that implementation experience.

### What predictive-modelling experience do you have?

I completed Machine Learning coursework and have a statistics foundation, but I do not have a verified predictive model deliverable in my employment or published portfolio. My current project evidence is descriptive and diagnostic. I would distinguish that clearly while explaining the framing, validation, and evaluation concepts I learned.

### Have you worked with star schemas or fact and dimension tables?

My direct work is normalized relational modelling with business entities, primary keys, foreign keys, uniqueness rules, and checks. I have not verified a star-schema implementation, so I would explain the relational foundation and avoid pretending that conceptual familiarity is hands-on delivery.

### Have you automated data pipelines or worked with Data Engineers?

I have added GitHub Actions checks that rerun project validation, but that is quality-check automation—not production data collection, transformation, or reporting pipelines. I also do not have verified direct collaboration with Data Engineers. I would bring clear data requirements, testable definitions, and careful validation to that partnership while learning the team's workflow.

### How have you used AI responsibly in analysis?

My repositories contain completed Generative AI-assisted analysis based on SQL outputs. I first establish and validate the data logic, then use structured prompts to explore interpretations and recommendations. I keep the SQL output as the evidence base and remain responsible for checking whether the AI-generated interpretation is consistent with it.

## Likely Questions

- Walk us through a project where you challenged an assumption or definition.
- Explain a window function you used and why it was appropriate.
- How would you diagnose a sudden change in a KPI?
- How do you detect duplicated records caused by joins?
- Describe your approach to data governance and documentation.
- How would you choose between a chart, table, or single KPI?
- What is the difference between descriptive, diagnostic, predictive, and prescriptive analysis?
- How would you evaluate a predictive model before business use?
- How do you prioritize competing analytical requests?
- How would you work with a Data Engineer when the source data does not meet reporting needs?
- Why Docebo and why Product Engineering?
- How does your experience prepare you for a fast-moving SaaS environment?

## Questions to Ask

- Which business decisions and product-engineering outcomes will this analyst influence most often?
- What visualization platform is used, and how much of the role is dashboard implementation versus SQL analysis?
- How are responsibilities divided among analysts, analytics engineers, and data engineers?
- Which datasets or KPI definitions currently create the greatest reliability challenges?
- What kinds of predictive work are already in production, and what would this analyst own?
- How does the team review analytical logic, data-quality tests, and stakeholder-facing recommendations?
- What would strong performance look like after three and six months?
- What learning support is available for Snowflake, Python, and Docebo's analytics stack?

## Never Claim

- Three or more years of BI, reporting, or data-analysis employment.
- Python or Snowflake experience.
- Implemented interactive Power BI dashboards or published `.pbix` files.
- Advanced visualization-tool proficiency beyond verified planning work.
- Predictive modelling, correlation-analysis, or deep statistical-modelling ownership.
- Star-schema, fact-table, or dimension-table implementation.
- Production-scale datasets, scalable solution architecture, or pipeline automation.
- Formal enterprise data-governance ownership.
- Direct collaboration with Data Engineers or Product Engineering teams.
- Production deployment, quantified impact, or stakeholder counts not in the evidence.
- Canadian SaaS employment, work authorization, or guaranteed Tuesday–Thursday availability.
- Freelance engagements not recorded in the canonical ledger.
