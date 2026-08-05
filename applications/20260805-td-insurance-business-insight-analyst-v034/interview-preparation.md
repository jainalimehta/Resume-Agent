# Interview Preparation — Business Insight Analyst, TD Insurance

## Fit Assessment

This is a stretch application. Jainali has strong SQL, advanced Excel, KPI, validation, reporting, requirements, and claims-related portfolio evidence, plus a Master of Business Analytics. She does not meet the stated two-year experience minimum and has no General Insurance, Python, R, actuarial, pricing, or professional claims-operations experience. The interview strategy is to be transparent, demonstrate strong analytical reasoning, and show deliberate preparation for General Insurance claims analytics.

## 90-Second Introduction

“I currently live in Toronto, while my education and work experience are international. I completed a Master of Business Analytics at Edith Cowan University in Australia and an Integrated MBA at Atmiya University in India. As a Data Intern at AYLA Solutions in Australia, I gathered reporting requirements, supported SQL extraction and validation, and prepared advanced Excel reports and dashboard insights. My Healthcare Patient & Hospital Analytics project models appointments, treatments, billing, and insurance claims and examines completion, treatment costs, billing status, workload, and claims using CTEs, segmentation, rankings, running totals, lag comparisons, and validation. I do not yet have General Insurance employment or two years of analyst experience, and I have not used Python or R. My strongest hands-on tools are SQL and Excel. I bring analytical discipline, careful documentation, clear recommendations, and strong motivation to develop the insurance domain knowledge required by TD’s Claims Insights team.”

## Why TD Insurance and Claims Insights?

- The team connects detailed claims analysis with operational, pricing, actuarial, product, and vendor decisions.
- The role values insight quality and communication, not merely report production.
- TD Insurance combines a large Canadian insurance business with TD's broader investment in analytics, AI, training, and colleague development.
- The claims domain offers a clear path to deepen Jainali's SQL, KPI, trend-analysis, and stakeholder-partnership skills.

## Honest Experience and Programming Gap Answer

“I want to be precise about my current experience. My insurance-claims evidence comes from a healthcare analytics portfolio project, not General Insurance employment. I also do not yet have two years of analyst work, Python, or R. I do have hands-on PostgreSQL and SQL experience, advanced Excel reporting, repeatable validation, requirements documentation, and experience converting findings into recommendations and dashboard plans. I would approach the gap systematically: learn TD's claims process and metric definitions, reproduce established analyses, reconcile results to trusted controls, seek review from domain specialists, and expand into the team's programming environment without overstating my current level.”

## General Insurance Claims Concepts

Use these as conceptual interview preparation, not experience claims. TD's approved definitions must govern actual work.

- **Claim frequency:** Number of claims relative to an exposure measure, such as policies, vehicles, earned exposures, or insured units.
- **Claim severity:** Average cost per claim under a defined basis; clarify paid, incurred, ultimate, open, closed, gross, or net.
- **Claims expense:** Costs associated with investigating, adjusting, managing, and settling claims; confirm classification rules.
- **Pure premium or loss cost:** Expected or observed claim cost per unit of exposure, often combining frequency and severity.
- **Loss ratio:** Claims or losses relative to earned premium under an approved accounting basis.
- **Combined ratio:** Loss ratio plus expense ratio; definitions and accounting treatment must be confirmed.
- **Paid versus incurred:** Paid reflects cash disbursed; incurred commonly incorporates paid amounts plus case reserves and may involve other adjustments.
- **Claim lifecycle:** Notice or first report of loss, triage, assignment, investigation, reserving, repair or treatment, settlement, closure, and possible reopening.
- **Claims development:** How estimated claim cost changes as a cohort matures; compare consistent accident, report, or calendar periods.
- **Exposure and mix:** Frequency and severity interpretation requires controlling for product, coverage, geography, vehicle/property type, customer, channel, peril, and policy period.

## Claims-Analysis Framework

When a claims KPI moves:

1. Confirm the metric definition, exposure basis, reporting period, valuation date, and data refresh.
2. Reconcile claim counts, paid amounts, incurred amounts, reserves, and exposure totals to trusted controls.
3. Separate frequency, severity, expense, volume, and mix effects.
4. Segment by product, coverage, peril, geography, channel, claim age, accident period, report period, and operational team.
5. Examine large-loss effects, catastrophe or weather events, inflation, repair or medical costs, litigation, fraud, reporting delay, and operational changes.
6. Compare cohorts at consistent maturity and avoid mixing immature and developed claims.
7. Distinguish facts, plausible drivers, limitations, and recommendations.
8. Define an action owner and monitoring metric.

## Likely Case Questions

### Claim severity increased while frequency was stable. How would you investigate?

- Validate paid/incurred basis, valuation date, currency, duplicates, reopenings, recoveries, and reserve treatment.
- Check whether a small number of large claims explains the movement; present mean, median, percentiles, and capped/uncapped views as appropriate.
- Segment by coverage, peril, geography, repair type, vendor, claim age, and accident period.
- Examine cost inflation, parts/labour, medical or legal cost, policy-limit mix, operational handling, and external events.
- Compare like-for-like cohorts and document limitations before recommending operational or pricing follow-up.

### Frequency increased in one region. What would you do?

Confirm exposure growth and mix, map the change by peril and time, check weather or catastrophe events, validate reporting delays and status definitions, compare neighbouring regions and prior years, and assess whether the movement is temporary, seasonal, operational, or structural.

### Executives challenge your finding. How do you respond?

Restate the business question, show the definition and control totals, separate verified evidence from interpretation, explain sensitivity and limitations, invite domain context, test credible alternatives, and update the conclusion if stronger evidence emerges. Confidence should come from transparent method, not defensiveness.

## SQL Topics to Review

- Claim-level versus transaction-level grain and duplicate multiplication after joins.
- Conditional aggregation for open, closed, reopened, paid, incurred, and status-based metrics.
- Distinct claim counts and exposure denominators.
- CTEs for readable multi-stage analysis.
- Window functions for rankings, cumulative paid amounts, lag comparisons, and rolling trends.
- Accident-date, report-date, close-date, payment-date, and valuation-date logic.
- Cohort or development-triangle concepts at a high level.
- Null, negative, recovery, reserve, and status-mapping treatment.
- Reconciliation queries and exception tables.

## Excel Topics to Review

- Pivot tables, filters, charts, and conditional formatting.
- `XLOOKUP` or equivalent logic, `SUMIFS`, `COUNTIFS`, `IF`, date functions, and error handling.
- Frequency/severity decomposition and actual-versus-prior variance analysis.
- Large-loss identification and percentile summaries.
- Separate raw data, mappings, assumptions, calculations, checks, summaries, and presentation tabs.

Only discuss functions Jainali can confidently demonstrate.

## Insight Presentation Structure

1. **Headline:** What changed and by how much, using the approved metric.
2. **Drivers:** Which segments or factors explain the movement.
3. **Business meaning:** Implications for claims operations, pricing, expense, customer outcomes, or risk.
4. **Recommendation:** Action, owner, timing, and monitoring KPI.
5. **Appendix:** Definitions, methodology, controls, assumptions, sensitivity, and limitations.

## Behavioural Stories to Prepare

- **Ambiguous demand:** AYLA Solutions—turning stakeholder questions into structured analytical tasks.
- **Quality rigor:** Healthcare project—relationships, repeatable validation, assumptions, and SQL-based recommendations.
- **Confidentiality and accuracy:** Arihant Investment—maintaining client records and business information.
- **Stakeholder coordination:** Trans Globe Education—coordinating process updates with students and institutions.
- **Learning:** Building the PostgreSQL repositories and validation workflow; do not invent the learning duration or business result.

Prepare each answer using Situation, Task, Action, and Result. When no quantified outcome is verified, finish with the factual deliverable or improved clarity produced.

## Questions to Ask the Interviewer

1. Which claims lines, products, and KPIs would this analyst support first?
2. How does Claims Insights partner with Claims Operations, Pricing, Corporate Actuarial, Product, and Vendor Management?
3. What SQL, Python, R, BI, and data-platform environment does the team use?
4. How are frequency, severity, expense, and valuation definitions governed and reconciled?
5. What distinguishes a strong deep-dive analysis from a useful executive recommendation on this team?
6. How does the team balance recurring reporting, emerging-trend investigation, and strategic projects?
7. What training helps analysts develop General Insurance and claims-process knowledge?

## 30-60-90 Day Approach

- **First 30 days:** Learn products, claim lifecycle, definitions, source systems, controls, existing reports, stakeholders, privacy expectations, and review standards; reproduce established metrics and reconcile totals.
- **Days 31-60:** Own assigned recurring analysis under review, investigate KPI movement, document assumptions and limitations, and build fluency in the team's programming and reporting environment.
- **Days 61-90:** Deliver an appropriately scoped claims deep dive, communicate findings to partners, improve one analytical control or workflow, and monitor an agreed follow-up metric.

## Accuracy Guardrails

- Do not claim General Insurance, claims-operations, actuarial, pricing, reserving, Python, R, or two years of analyst experience.
- Do not present healthcare portfolio claims as property-and-casualty experience.
- Do not describe Power BI planning as interactive dashboard implementation.
- Do not imply Canadian education or work experience.
- Do not invent executive presentations, dataset volumes, claim savings, quantified outcomes, or work authorization.
- Verify all TD-specific definitions, regulatory requirements, and accounting treatments through approved internal documentation.

## Official Research

- [TD — Corporate Information](https://www.td.com/ca/en/about-td/corporate-profile/corporate-information): TD Insurance's place within Wealth Management and Insurance and its property-and-casualty and life-and-health businesses.
- [TD — Who We Are](https://www.td.com/ca/en/about-td/who-we-are): strategy, client experience, disciplined execution, and colleague principles.
- [TD — Simpler and Faster](https://www.td.com/ca/en/about-td/for-investors/investor-relations/financial-information/annual-report-2025/simpler-faster): official analytics and AI context, including TD Insurance initiatives.
- [TD Insurance Products](https://www.td.com/ca/en/personal-banking/products/insurance): current insurance product and claims context.

Recheck current product, company, and regulatory information immediately before the interview.
