# Scotiabank Data Analyst — Global Compliance Data Analytics Interview Preparation

## Candidacy Positioning

Present yourself as an early-career analyst with strong foundations, not as a production data-governance specialist.

Your strongest evidence is:

1. SQL extraction and validation plus advanced Excel reporting at AYLA Solutions.
2. Requirements gathering, reporting documentation, and Agile planning/review participation.
3. Relational models with primary/foreign keys, uniqueness rules, checks, business rules, and validation.
4. CTEs, window functions, rankings, segmentation, running totals, and lag comparisons.
5. Financial-services record handling and an academic customer-transaction analysis project.

## 90-Second Introduction

“I currently live in Toronto and completed a Master of Business Analytics at Edith Cowan University in Australia. My professional analyst foundation comes from a Data Intern role at AYLA Solutions, where I gathered and documented business and reporting requirements, supported SQL-based extraction and validation, prepared advanced Excel reports, and participated in Agile planning and review sessions. I have also built published PostgreSQL projects across e-commerce, healthcare, and workforce analytics. Those projects use relational models, keys, constraints, documented business rules, CTEs, window functions, repeatable validation, and GitHub Actions. My formal compliance-governance experience is still developing, so I would not claim production ownership of CDE registration, lineage, ETL, or governance tools. What I can bring immediately is disciplined SQL analysis, data-quality thinking, clear documentation, careful handling of information, and the ability to learn structured governance processes.”

## Why This Role?

“I am interested in the role because it connects data quality, governance, analytics, documentation, and stakeholder requirements. I enjoy understanding what data means, how tables relate, which rules make an output trustworthy, and how analytical findings should be communicated. Global Compliance adds a meaningful control context where accuracy, traceability, and responsible escalation matter. That is an area where I want to develop deeper expertise.”

## Data Governance Concepts

### Critical Data Element

A Critical Data Element is a data field whose accuracy, completeness, timeliness, or availability is important to business decisions, regulatory obligations, risk management, customer outcomes, or reporting.

Possible examples in compliance might include customer identifier, account identifier, transaction date, transaction amount, country, risk rating, case status, or alert disposition. Do not claim these are Scotiabank's official CDEs.

### Authoritative Data Source

The approved system considered the trusted source for a defined data element. Selection normally requires clear ownership, controls, quality, timeliness, and reconciliation with downstream use.

### Master Data

Core entities shared across processes, such as customer, employee, product, account, or legal entity.

### Reference Data

Controlled value sets used to classify other data, such as country codes, currency codes, status codes, business-unit codes, or risk categories.

### Metadata

Information describing data: business definition, technical name, datatype, format, owner, source, allowed values, sensitivity, transformation, and usage.

### Data Lineage

The traceable path of data from origin through transformations and systems to reports, models, or decisions. Lineage should show where a value came from, what changed it, and where it is consumed.

### Source-to-Target Mapping

A field-level specification connecting source fields to target fields, including datatypes, transformation logic, joins, filters, default handling, and quality rules.

### Data Flow Diagram

A visual representation of systems, processes, data stores, and the movement of data among them. It is broader than a field-level Source-to-Target Mapping.

## Data-Quality Dimensions

Know these dimensions and be ready with examples:

- Completeness: required values are present.
- Validity: values conform to formats or allowed domains.
- Accuracy: values reflect the real-world fact or trusted source.
- Consistency: the same concept agrees across records and systems.
- Uniqueness: records that should be unique are not duplicated.
- Timeliness: data is available and current when needed.
- Referential integrity: relationships point to valid parent records.

## Business and Technical Data-Quality Rules

Business rule example:

- Transaction amount must be positive for a completed debit transaction.

Technical rule example:

- `transaction_id` must be non-null and unique; `customer_id` must exist in the customer table; `transaction_date` must parse as a valid date.

Tie this to your projects:

- E-commerce: primary/foreign keys, uniqueness rules, checks, and recognized-revenue exclusions.
- Healthcare: relationships across patients, clinicians, appointments, billing, and claims.
- HR: normalized departments, employees, salaries, reviews, and attendance.

Be clear that these are project examples, not compliance-production rules.

## Data Profiling Framework

For a new field or table, examine:

1. Row count and distinct count.
2. Null and blank rates.
3. Duplicate keys.
4. Minimum, maximum, mean, median, and percentiles where relevant.
5. Value frequencies and unexpected categories.
6. Format, datatype, and length distributions.
7. Date ranges and future or impossible dates.
8. Referential-integrity failures.
9. Cross-field logic, such as end date preceding start date.
10. Reconciliation to a trusted total or source.

Do not claim professional data-profiling ownership; describe this as the method you would apply.

## Root-Cause Analysis and Remediation

Use this sequence:

1. Define the symptom and affected metric, field, records, and time period.
2. Reproduce the issue with a controlled query.
3. Determine whether the problem originates in source capture, extraction, transformation, mapping, load, or reporting.
4. Compare good and bad records and inspect recent changes.
5. Identify the owner and business impact.
6. Agree on correction, prevention, and backfill where appropriate.
7. Test the remediation and reconcile outputs.
8. Document the cause, decision, evidence, and monitoring rule.

Avoid saying you have already led this process in production.

## Testing Concepts

### Quality Assurance Testing

Testing performed to confirm that technical requirements, mappings, transformations, controls, and expected outputs work correctly before business acceptance.

### Business Acceptance Testing

Business users confirm that the solution supports real workflows, rules, and intended outcomes.

### Post Implementation Validation

Checks after deployment to confirm production data, reports, controls, and integrations operate as expected.

Suggested gap answer:

“I have performed repeatable project validation and GitHub Actions checks, but I have not owned formal QAT, BAT, or PIV in a production organization. I understand their different purposes and would apply my validation discipline within Scotiabank's approved test plans and evidence standards.”

## ETL and Pipeline Concepts

- Extract: obtain data from an approved source.
- Transform: clean, standardize, join, filter, derive, and apply business rules.
- Load: place validated data into the target store.
- Orchestration: schedule and coordinate dependent tasks.
- Monitoring: detect failures, delays, volume anomalies, and quality problems.
- Idempotency: rerunning a process does not create unintended duplication.
- Auditability: transformations and outcomes can be traced and explained.

Truthful answer:

“I have supported SQL extraction and built relational analysis projects, but I do not have verified production pipeline implementation experience. I understand the ETL stages and the importance of validation, logging, lineage, error handling, and reconciliation, and I am prepared to learn the team's implementation standards.”

## SQL Preparation

Review and practise:

- Inner, left, and anti joins.
- Aggregation and conditional aggregation.
- CTEs and nested queries.
- `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LAG`, and running totals.
- Null handling with `COALESCE`.
- Duplicate detection.
- Referential-integrity checks.
- Date grouping and lag comparisons.
- Reconciliation queries.
- Query readability and explainable logic.

### Duplicate Critical Field Check

```sql
SELECT customer_id, COUNT(*) AS record_count
FROM customer_source
GROUP BY customer_id
HAVING COUNT(*) > 1;
```

### Missing Parent Check

```sql
SELECT t.transaction_id, t.customer_id
FROM transactions t
LEFT JOIN customers c
  ON t.customer_id = c.customer_id
WHERE c.customer_id IS NULL;
```

### Quality Summary

```sql
SELECT
  COUNT(*) AS total_rows,
  COUNT(*) FILTER (WHERE transaction_id IS NULL) AS missing_transaction_id,
  COUNT(*) FILTER (WHERE customer_id IS NULL) AS missing_customer_id,
  COUNT(*) FILTER (WHERE amount <= 0) AS nonpositive_amount
FROM transactions;
```

Explain assumptions before writing a query. In compliance data, a rule such as `amount <= 0` may be invalid for one transaction type and valid for another.

## Power BI and Visualization Gap

Your verified evidence is Power BI dashboard and KPI planning, not implemented `.pbix` dashboards.

Answer:

“I have completed Power BI KPI, layout, filter, and visualization planning in my published projects, but the interactive implementation is not yet published. I can explain the business questions, measures, validation, and dashboard structure I planned. I would not describe that as production dashboard experience.”

Review:

- Star schema and relationships.
- Measures versus calculated columns.
- Filter context.
- KPI definition and reconciliation.
- Role-based access concepts.
- Clear dashboard hierarchy and accessible design.
- Data refresh and quality indicators.

## Programming and Machine-Learning Gap

Do not claim Python, R, Matlab, or machine-learning libraries. Machine Learning is verified coursework only.

Suggested answer:

“My hands-on analysis stack is PostgreSQL, SQL, and advanced Excel. I completed Machine Learning coursework, but I do not yet claim production experience with Python, R, Matlab, or their libraries. I would rather be precise about that gap and demonstrate my SQL reasoning and learning ability.”

## Collibra Gap

“I have not used Collibra. I understand that governance platforms commonly support cataloguing, definitions, ownership, lineage, policies, stewardship workflows, and issue management. I would learn Scotiabank's configured processes rather than assume that generic tool knowledge matches the Bank's implementation.”

## Compliance and Risk Mindset

You do not have verified compliance experience. Demonstrate principles:

- Use only authorized data and approved environments.
- Apply least-privilege access.
- Protect confidential and sensitive information.
- Do not copy production data into personal tools.
- Document definitions, assumptions, transformations, and decisions.
- Escalate policy ambiguity and quality issues.
- Preserve evidence and auditability.
- Do not change source data without authorization.
- Consider false positives, false negatives, and customer impact.

## STAR Stories

### E-Commerce Data Controls

- Situation: customer, product, order, line-item, and payment data required a reliable relational structure.
- Task: create defensible analysis and recognized-revenue logic.
- Action: used keys, uniqueness rules, checks, documented business rules, validation, and GitHub Actions.
- Result: a repeatable project structure supporting SQL analysis and recommendations.

### AYLA Requirements and Reporting

- Situation: analytical work required clear business and reporting requirements.
- Task: support extraction, validation, reporting, and documentation.
- Action: gathered requirements, supported SQL and Excel work, and participated in Agile discussions.
- Result: structured reporting support and communicated progress. Do not invent metrics.

### Healthcare Relationship Validation

- Situation: patient, clinician, appointment, treatment, billing, and claim records were related.
- Task: analyze operational questions without losing relationship integrity.
- Action: built the relational model and used CTEs, windows, and validation.
- Result: repeatable analysis and documented recommendations.

### Confidential Financial Records

- Situation: Arihant Investment maintained client and business records.
- Task: support daily operations while protecting accuracy and confidentiality.
- Action: handled data entry, documentation, and record maintenance carefully.
- Result: dependable records for business operations.

## Likely Behavioural Questions

Prepare concise answers for:

1. Tell me about yourself.
2. Why compliance data analytics?
3. Describe a time requirements were unclear.
4. How do you validate your analysis?
5. How would you investigate a data-quality issue?
6. How do you explain technical findings to business users?
7. Describe a time you handled confidential information.
8. How do you prioritize competing analysis requests?
9. Tell me about an error you found and how you responded.
10. How do you work with business analysts, engineers, and data scientists?

Never invent a production incident. Use project validation or workflow examples and state their actual context.

## Questions to Ask the Interviewer

1. Which compliance datasets and Critical Data Elements would this analyst support first?
2. How are data ownership and stewardship divided across Compliance, Technology, and business teams?
3. What are the team's standards for lineage and Source-to-Target Mapping?
4. Which tools are used for profiling, issue management, testing, lineage, and dashboard delivery?
5. How is the success of a data-quality remediation measured?
6. What proportion of the role focuses on SQL analysis versus governance documentation and stakeholder discussions?
7. What training is provided on Scotiabank's risk, privacy, security, and compliance controls?
8. What would strong performance look like during the contract's first three months?

## 30-60-90 Day Outline

### First 30 Days

- Learn the compliance domain, priority datasets, business definitions, owners, and controls.
- Complete required security, privacy, risk, and conduct training.
- Review existing CDE inventory, lineage, mappings, quality rules, issues, and reports.
- Reproduce approved queries and reconcile known outputs.

### Days 31–60

- Support profiling and quality-rule execution under team standards.
- Document requirements, definitions, assumptions, and evidence clearly.
- Contribute to issue investigation and testing with appropriate review.
- Build relationships with analysts, engineers, scientists, and business owners.

### Days 61–90

- Own a bounded analysis or documentation deliverable within agreed authority.
- Improve one repeatable validation or reporting step after understanding controls.
- Present findings with business impact, limitations, and recommended next steps.
- Continue building compliance-domain and governance-tool proficiency.

## Final Accuracy Guardrail

Never claim:

- two years of analyst employment;
- formal CDE, authoritative-source, metadata, master/reference-data, lineage, STM, or governance ownership;
- production ETL or pipeline implementation;
- QAT, BAT, PIV, root-cause remediation, or compliance-control testing ownership;
- Collibra or another governance platform;
- Python, R, Matlab, machine-learning libraries, XML, JSON, log, or flat-file experience;
- implemented Power BI dashboards or any Tableau experience;
- Scotiabank systems, Canadian banking, AML/ATF, sanctions, or compliance experience; or
- freelance data-engineering details absent from the evidence ledger.

Use the concepts in this guide to demonstrate preparation, not to rewrite your history.
