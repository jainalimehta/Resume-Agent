# Interview Preparation — Data Analyst & Integrator, Job ID 64125

## Position Snapshot

- **Employer:** City of Toronto
- **Division:** Parks & Recreation / Business & Technology Transformation
- **Initial location:** Metro Hall, 55 John Street, Toronto
- **Future location:** North York Civic Centre, 5100 Yonge Street
- **Work arrangement:** Hybrid under the City's policy
- **Term:** One temporary vacancy for 12 months
- **Posting deadline:** August 6, 2026
- **Core work:** data profiling, cleansing, mapping, transformation, migration, reconciliation, visualization, KPI tracking, governance, spatial data, and IBM Maximo implementation support.

## Honest 90-Second Introduction

I am an early-career Data Analyst currently living in Toronto. I earned a Master of Business Analytics from Edith Cowan University in Australia and an Integrated MBA from Atmiya University in India. In 2025, I worked as a Data Intern at AYLA Solutions in Australia, where I gathered business, data, and reporting requirements, supported SQL extraction and validation, prepared advanced Excel reports, and contributed dashboard insights. My three published PostgreSQL projects demonstrate relational modelling, primary and foreign keys, uniqueness rules, validation, operational and financial KPIs, CTEs, window functions, GitHub Actions checks, AI-assisted recommendations, and Power BI reporting plans. These are strong foundations for migration-quality work, although I have not yet supported a production enterprise migration or IBM Maximo implementation. I am interested in learning source-to-target mapping, ETL, spatial asset data, and Maximo while contributing reliable SQL analysis, validation, documentation, and stakeholder communication from the start.

## Evidence Bank

### 1. SQL Extraction, Validation, and Reporting — AYLA Solutions

- **Situation:** Stakeholder questions required structured data and reporting support.
- **Task:** Help clarify analytical needs and prepare reliable reporting outputs.
- **Action:** Gathered and documented requirements, supported SQL extraction and validation, prepared advanced Excel reports, contributed dashboard insights, communicated progress and findings, and maintained documentation through Agile reviews.
- **Result:** Supported decision-focused reporting aligned with stakeholder questions. Do not invent a numerical outcome.

### 2. Referential Integrity and Business Rules — E-Commerce Analytics

- **Situation:** Customer, product, order, line-item, and payment records required consistent relationships and revenue treatment.
- **Task:** Create a reliable relational and analytical foundation.
- **Action:** Applied primary and foreign keys, uniqueness rules, checks, and explicit recognized-revenue definitions; added repeatable validation and GitHub Actions; analysed financial and operational indicators.
- **Result:** Produced traceable SQL outputs, documented assumptions, recommendations, and Power BI reporting plans.

### 3. Connected Operational Data — Healthcare Analytics

- **Situation:** Six linked entities covered patients, clinicians, appointments, treatments, billing, and claims.
- **Task:** Model and validate the information for operational analysis.
- **Action:** Used relationships, CTEs, rankings, segmentation, running totals, and lag comparisons; documented assumptions and automated validation.
- **Result:** Produced validated operational insights covering completion, workload, costs, billing, and claims.

### 4. Workforce Data — HR Analytics

- **Situation:** Department, employee, salary, performance, and attendance information needed an integrated model.
- **Task:** Create workforce KPIs and reporting recommendations.
- **Action:** Normalized the data, applied quality controls, used CTEs and window functions, and analysed headcount, compensation, performance, attendance, hiring, and tenure.
- **Result:** Produced repeatable SQL analysis, AI-assisted recommendations, and Power BI reporting plans.

### 5. Accuracy and Confidentiality — Earlier Roles

- Use Trans Globe Education for documentation, accurate records, workflow coordination, reporting, and communication across students and institutions.
- Use Arihant Investment for data entry, confidential client records, accuracy, and dependable operational support.

## Likely Technical Questions

### Walk us through a data-migration lifecycle.

State this as your learned approach: establish scope and governance; inventory source systems; profile data; define target requirements; create the source-to-target mapping; agree transformation and quality rules; cleanse and standardize; build extraction and transformation workflows; execute test loads; reconcile counts, totals, keys, and exceptions; support business validation and UAT; resolve defects; run mock cutovers; complete final load and post-load validation; obtain sign-off; archive evidence; monitor after deployment.

### What belongs in a source-to-target mapping?

Source system/table/file and field, target object and attribute, business definition, datatype and length, required/optional status, transformation rule, default, lookup or controlled value, key and relationship, validation rule, exception treatment, owner, status, unresolved issue, and test evidence.

### How would you profile a dataset?

Assess row counts, column types, nulls, blanks, distinct values, duplicates, minimum/maximum, patterns, formats, invalid characters, outliers, domain violations, key uniqueness, referential integrity, taxonomy values, date ranges, precision, and cross-field logic. Record the rule, result, severity, affected records, owner, and disposition.

### How would you reconcile a migration?

Compare source, staged, rejected, and loaded record counts; key populations; control totals; null and duplicate rates; lookup matches; relationship integrity; aggregates by important dimensions; sample records; exception logs; and business totals. Explain every difference and retain reproducible evidence.

### How would you handle unresolved data-quality issues?

Document the issue and affected scope, identify its source and business impact, consult the data owner, propose remediation or exception options, assign an owner and target date, define acceptance thresholds, track the decision, retest, and escalate issues that threaten migration readiness or operational integrity.

### Explain ETL versus ELT.

ETL transforms data before loading to the target; ELT loads raw or lightly prepared data into a capable platform and transforms it there. Choice depends on platform capability, volume, security, auditability, latency, transformation complexity, and recovery needs. Never claim you built a production pipeline; connect the concepts to your SQL preparation and validation foundation.

### How would you validate referential integrity?

Confirm parent keys are unique and non-null where required; identify child foreign keys with no matching parent using anti-joins; check duplicate relationships; validate cardinality and effective dates; confirm deletion and inactive-record rules; reconcile exception counts; and rerun checks after remediation and loading.

### How do you communicate findings to non-technical stakeholders?

Lead with the decision and business impact, define the issue in plain language, quantify affected records when evidence exists, show a concise visual or example, state assumptions and limitations, present options and recommended action, identify owners and timing, and confirm understanding.

## SQL Practice Topics

- Null, blank, duplicate, and invalid-value profiling.
- `GROUP BY`, `HAVING`, `CASE`, joins, anti-joins, CTEs, subqueries, and window functions.
- Duplicate survivor rules using `ROW_NUMBER()`.
- Referential-integrity exceptions using `LEFT JOIN ... WHERE parent.key IS NULL` or `NOT EXISTS`.
- Standardizing dates, text, codes, whitespace, casing, and numeric precision.
- Comparing source and target counts and aggregates.
- Hash or field-by-field comparison concepts for changed records.
- Incremental loads, effective dates, late-arriving data, rejects, and audit columns.
- Reusable validation queries with pass/fail outputs and exception extracts.

## IBM Maximo and Asset-Data Knowledge

1. **Core Maximo concepts:** organizations, sites, locations, assets, service requests, work orders, preventive maintenance, job plans, inventory, meters, labour, and classifications.
2. **Asset hierarchy:** parent/child assets, functional locations, location hierarchy, site codes, asset status, criticality, condition, and maintenance history.
3. **Migration considerations:** external IDs, target keys, domains, required attributes, classifications, rotating assets, units, status mappings, locations, relationships, attachments, history, and load sequence.
4. **Typical sequence:** organizations/sites and domains, locations, classifications, assets, inventory and job plans, preventive maintenance, open transactions, and validated history—subject to the City's design.
5. **Data-quality risks:** duplicate asset IDs, missing locations, invalid hierarchies, inconsistent naming, uncontrolled descriptions, obsolete records, incomplete classifications, invalid coordinates, and conflicting ownership.

## GIS and Spatial Data Fundamentals

- Vector data: points, lines, and polygons; raster data; coordinate systems and projections.
- Spatial joins, geocoding, coordinates, geometry validity, topology, proximity, boundaries, and location identifiers.
- Importance of coordinate reference systems, precision, authoritative sources, and consistent location/asset keys.
- For Parks & Recreation, possible data includes facilities, parks, trails, fields, buildings, equipment, service areas, and work locations. Present these as examples, not confirmed project scope.
- Be honest: you have not used a verified GIS tool. Explain how relational keys, quality checks, and metadata discipline transfer to spatial datasets.

## Metadata and Governance Knowledge

- **Data dictionary:** field name, definition, type, length, format, allowed values, nullability, owner, source, target, and quality rule.
- **Lineage:** where data originated, how it changed, where it moved, and which reports or processes consume it.
- **Taxonomy and controlled vocabulary:** governed categories and permitted terms supporting consistent classification and reporting.
- **Business glossary:** shared business terms, definitions, owners, related rules, and approved usage.
- **Governance:** ownership, stewardship, quality thresholds, access, privacy, retention, issue management, change control, and audit evidence.

## Questions for the Panel

- Which Maximo modules, asset classes, and source systems are within the migration scope?
- What are the most significant current data-quality and source-to-target mapping challenges?
- Which ETL, database, GIS, quality-management, and visualization tools does the team use?
- How are data owners, Parks & Recreation users, implementation partners, and technical teams organized for validation and sign-off?
- What migration-readiness thresholds and reconciliation controls must be satisfied before deployment?
- What would strong performance look like in the first three and six months?

## Final Checklist

- Apply before August 6, 2026.
- Recheck the official posting for amendments immediately before submitting.
- Prepare two-minute STAR examples from AYLA and each published project.
- Review the three repositories and practise explaining schemas, constraints, validation queries, GitHub Actions, AI sections, and Power BI plans.
- Practise a small source-to-target mapping and write SQL checks for nulls, duplicates, domain values, and orphaned foreign keys.
- Study Maximo asset/work-management and spatial-data fundamentals from authoritative documentation.
- Never claim production ETL, migration, Python, Oracle, Tableau Prep, GIS, or Maximo experience.
- Never imply Canadian education or employment; state Toronto residence separately from Australian and Indian experience.
