# KPMG Canada — Data Consultant, Audit Technologies Group Interview Preparation

## Your Positioning

Your strongest truthful story is:

**I am an early-career Business Analytics graduate with hands-on SQL/PostgreSQL, advanced Excel, relational modelling, data extraction support, validation, reporting requirements, transaction analysis, documentation, and stakeholder coordination. I understand how those foundations transfer to audit data acquisition and analytics, while recognizing that I still need training in KPMG's audit methodology, ERP extracts, Alteryx, Databricks, Python, APIs, and the Microsoft Power Platform.**

Do not claim external-audit experience, ERP expertise, production ETL ownership, audit conclusions, Alteryx, Databricks, Python, VBA, Power Query, Power Apps, Power Automate, APIs, completed Power BI dashboards, proposal writing, leadership experience, or English fluency unless you can independently verify the claim.

## 60-Second Introduction

> I am an early-career Business Analytics graduate living in Toronto. At AYLA Solutions in Australia, I gathered and documented reporting requirements, supported SQL extraction and validation, prepared advanced Excel reports, contributed performance-tracking insights, and communicated progress through Agile planning and reviews. My E-Commerce Sales Analytics project demonstrates a control-oriented approach to transaction data: I modelled customers, products, orders, line items, and payments, enforced relational constraints, defined recognized-revenue rules, and added repeatable validation and GitHub Actions checks. I also analyzed Bank of Baroda customer transactions with Excel and SQL, and my earlier role at Arihant Investment developed my financial-services record accuracy and client communication. I have not yet worked in external audit or KPMG's broader technology stack, so I would bring strong SQL and data-quality fundamentals, learn the audit context from engagement teams, reconcile every transformation to source, and escalate exceptions with clear evidence.

## Understand KPMG's Audit D&A Purpose

KPMG Canada describes audit data analytics as supporting financial assurance, risk management, decision-making, and audit effectiveness. It also emphasizes audit quality, integrity, professional skepticism, objectivity, independence, and robust quality controls. Review KPMG's official [Audit Data & Analytics](https://kpmg.com/ca/en/services/audit/audit-data-analytics.html) and [Audit & Assurance](https://kpmg.com/ca/en/services/audit.html) pages.

Your role is not to replace the auditor's judgment. It is to help engagement teams obtain, transform, validate, analyze, visualize, and document data so auditors can perform appropriate procedures and evaluate evidence.

## Audit Foundations You Need

### Financial Statements

- **Balance sheet:** assets, liabilities, and equity at a point in time.
- **Income statement:** revenue, expenses, and profit/loss over a period.
- **Cash-flow statement:** operating, investing, and financing cash flows.
- **Trial balance:** account-level debit/credit balances used to prepare financial statements.
- **General ledger:** detailed postings by account, date, document, user, amount, and other attributes.
- **Subledgers:** detailed records supporting control accounts, such as accounts receivable, accounts payable, inventory, or fixed assets.
- **Journal entry:** a debit/credit posting, often with date, account, amount, source, preparer, approver, and description.

### Common Audit Assertions

- **Existence/occurrence:** recorded assets or transactions exist or occurred.
- **Completeness:** required transactions and balances are recorded.
- **Accuracy/valuation:** amounts and related information are appropriate.
- **Rights and obligations:** the entity owns assets or owes liabilities.
- **Cut-off:** transactions are recorded in the correct period.
- **Classification/presentation:** items are properly classified and disclosed.

Analytics identifies patterns and exceptions relevant to assertions; it does not prove that every flagged item is wrong or that every unflagged item is correct.

## Data Acquisition and ETL Workflow

Use this framework in a case interview:

1. **Scope with the audit team:** entity, period, process, population, assertions, source system, required fields, expected format, deadline, and output.
2. **Understand the ERP/data architecture:** modules, tables, keys, posting logic, fiscal calendar, currencies, status codes, interfaces, custom fields, and extract method.
3. **Define the request:** field-level specification, filters, population boundaries, control totals, secure transfer method, and accountable client contact.
4. **Acquire securely:** preserve the original extract, record source/timestamp/parameters, and avoid unnecessary personal or confidential fields.
5. **Profile:** row counts, file/schema structure, types, nulls, duplicates, invalid dates, sign conventions, currencies, and key uniqueness.
6. **Transform reproducibly:** retain source-to-target mappings, named steps, code/workflow versions, exception handling, and transformation logs.
7. **Reconcile:** compare record counts and financial control totals with the client-provided source/trial balance before and after transformation.
8. **Analyze:** apply engagement-approved procedures and document filters, thresholds, assumptions, and limitations.
9. **Review:** provide the audit team with results, exceptions, interpretation boundaries, and enough documentation to reproduce the work.
10. **Retain/dispose:** follow KPMG's approved security, retention, and confidentiality procedures.

## Reconciliation Is Non-Negotiable

For each stage, ask:

- Did the row count change? Why?
- Do debit/credit or amount totals reconcile to the source and trial balance?
- Did joins create duplicate rows or drop unmatched records?
- Were nulls, invalid records, reversals, deleted items, or late postings handled explicitly?
- Are dates, currencies, signs, and account mappings consistent?
- Can every output field be traced to its source or documented derivation?
- Is the transformed population complete for the audit purpose?

Example wording:

> I would never assume that a successful file load means the population is complete. I would reconcile row counts and control totals, inspect unmatched keys and rejected records, and document every intentional difference before the audit team relies on the output.

## ERP and Data Architecture Concepts

- **ERP:** an integrated system supporting functions such as finance, procurement, sales, inventory, payroll, and projects.
- **Master data:** relatively stable entities such as customers, vendors, products, employees, and chart of accounts.
- **Transactional data:** events such as invoices, payments, orders, receipts, and journal entries.
- **Primary key:** uniquely identifies a record.
- **Foreign key:** links a record to another table.
- **Grain:** what one row represents; never join or aggregate before confirming grain.
- **Chart of accounts:** organized account structure used to classify financial postings.
- **Source-to-target mapping:** documents how source fields become audit-tool fields.
- **Data lineage:** the trace from source, through transformations, to output.
- **API:** a controlled interface for systems to exchange requests and data. You understand the concept but have no verified implementation experience.

## Audit Analytics Examples to Understand

These are learning examples, not your prior experience:

- Journal entries posted on unusual dates/times or by unusual users.
- Manual entries to sensitive accounts.
- Entries with round amounts, rare account combinations, blank descriptions, or reversals.
- Revenue transactions near period end for cut-off testing.
- Duplicate invoices or payments based on vendor, amount, date, and invoice reference.
- Gaps or duplicates in document sequences.
- Aged receivables, negative balances, unusual credit memos, or inactive vendors with activity.
- Reconciliation of subledger totals to general-ledger control accounts.
- Changes in transaction patterns by period, account, location, user, or business unit.

Flags require investigation and context. Avoid calling an exception “fraud” or “misstatement” without audit evidence and authorized judgment.

## Professional Skepticism

Professional skepticism means maintaining a questioning mind, critically assessing evidence, and remaining alert to error, fraud, bias, inconsistency, or incomplete explanations. It is not automatic distrust.

The IAASB emphasizes pausing to assess whether evidence is persuasive, whether higher-risk matters were addressed, and whether bias may be influencing judgment. Review the IAASB's [Skeptic's Pause](https://www.iaasb.org/news-events/2026-03/skeptic-s-pause) and [professional-skepticism resources](https://www.iaasb.org/focus-areas/embedding-professional-skepticism).

Practical questions:

- Does the extract cover the full population and period?
- Is management's explanation consistent with the data and other evidence?
- What evidence contradicts the initial hypothesis?
- Did the procedure unintentionally exclude high-risk records?
- Could a system configuration, mapping, or user override explain the pattern?
- Is the threshold justified, or merely convenient?

## SQL Preparation

Be ready to write and explain:

- `INNER JOIN` versus `LEFT JOIN` and how each affects completeness.
- Aggregation and conditional counts/sums.
- Duplicate detection with `GROUP BY ... HAVING COUNT(*) > 1`.
- CTEs for staged transformations and reviewability.
- Window functions: `ROW_NUMBER`, `RANK`, `LAG`, and running totals.
- Anti-joins to identify unmatched source records.
- Date filters that correctly include period boundaries.
- Handling `NULL`, zero, negative amounts, reversals, and currencies.
- Validation queries before and after transformation.

### Example: Duplicate-Payment Candidate Logic

```sql
SELECT vendor_id, invoice_number, amount, COUNT(*) AS occurrences
FROM payments
WHERE payment_date BETWEEN :start_date AND :end_date
GROUP BY vendor_id, invoice_number, amount
HAVING COUNT(*) > 1;
```

Explain limitations: repeated invoice numbers may be legitimate, formatting differences may hide duplicates, and a candidate requires supporting evidence.

## Tool Landscape

### Alteryx

A visual workflow tool for connecting, cleaning, joining, transforming, summarizing, and analyzing data. Workflows should still be parameterized, documented, reconciled, versioned, and reviewed. Alteryx's official documentation describes tools such as Summarize for grouping, counting, and aggregation; use the [Alteryx Designer documentation](https://help.alteryx.com/current/en/designer/tools/transform/summarize-tool.html) for learning.

### Databricks

A data/lakehouse platform supporting SQL and programmatic transformations. Databricks describes a medallion pattern:

- Bronze: raw source data.
- Silver: cleaned, validated, deduplicated, and conformed data.
- Gold: business-ready models and aggregates.

Review the official [Databricks medallion architecture](https://docs.databricks.com/aws/en/lakehouse/medallion). You have not worked hands-on with Databricks.

### Power BI

Understand Power Query, semantic models, relationships, star schemas, DAX measures, visuals, refresh, permissions, row-level security, and UAT. Your verified status is dashboard planning only.

### Power Apps and Power Automate

Power Apps builds low-code business applications connected to data; Power Automate creates automated, scheduled, or approval workflows between systems. Review Microsoft's [Power Apps overview](https://learn.microsoft.com/mt-mt/power-apps/powerapps-overview) and [Power Automate documentation](https://learn.microsoft.com/en-us/power-automate/). Do not claim hands-on use.

### APIs

Know HTTP methods, endpoints, authentication, pagination, rate limits, JSON responses, status codes, schema changes, retries, logging, and secure secret handling. Do not claim API creation until you have built and tested one.

## Audit Documentation Structure

A well-structured D&A workpaper or technical record should answer:

- What audit objective and population were addressed?
- What source system, extract method, period, fields, and parameters were used?
- How was completeness and accuracy assessed?
- What transformations and mappings occurred?
- What procedure, filters, thresholds, and logic were applied?
- Who prepared and reviewed the work, and which version is final?
- What exceptions or limitations arose?
- Where are the result files and supporting evidence?
- What conclusion did the audit engagement team reach? The audit team owns the audit conclusion.

Your AYLA documentation and Git-based project history are transferable foundations, not prior audit workpapers.

## Client Communication and Issue Escalation

Use **fact → impact → evidence → options → owner → next update**.

> The extracted general-ledger total does not reconcile to the trial balance for the period. The current difference is [amount], concentrated in [accounts/period]. We confirmed the date and entity filters and found [evidence]. I recommend confirming whether adjustment-period entries or excluded ledgers are missing. The engagement team should decide whether we request a revised extract or modify the approved scope. I will retain the current file unchanged and update the reconciliation log by [time].

Never blame the client, silently edit source data, or allow deadline pressure to override reconciliation.

## Trusted AI Answer

Your portfolio includes AI-assisted prompts and interpretation, but responsible use is essential.

> I use AI to help structure questions and explore interpretations, but I validate the result against SQL outputs and retain human accountability. At KPMG, I would use only approved tools, never place client or confidential audit data into an unapproved system, document material AI use as required, test outputs for accuracy and bias, and follow KPMG's Trusted AI and engagement policies.

KPMG's Trusted AI framework highlights fairness, transparency, explainability, accountability, data integrity, reliability, security, safety, privacy, and sustainability. Review KPMG Canada's [Trusted AI framework](https://kpmg.com/ca/en/services/digital/ai-services/trusted-ai.html).

## Likely Questions and Defensible Answers

### Why KPMG Audit Technologies Group?

Connect KPMG's audit-quality focus, technology-enabled delivery, multidisciplinary teamwork, and structured learning with your interest in transaction data, controls, and client-facing analytics.

### Why should we choose you without the full platform stack?

> I would not overstate my tools. My direct evidence is SQL/PostgreSQL, advanced Excel, data extraction support, relational modelling, validation, repeatable checks, reporting requirements, documentation, and stakeholder coordination. My transaction projects also show that I think about business rules and reconcile meaning, not only code. I would need training in the audit methodology, ERP extracts, Alteryx, Databricks, Python, APIs, and Power Platform. I can contribute first in SQL, Excel, data profiling, reconciliation, documentation, and issue follow-up while building the broader stack under review.

### Tell me about applying professional skepticism.

Use E-Commerce Sales Analytics: explain why counting all orders as revenue would be misleading; define excluded statuses; use constraints and validation; inspect alternative explanations. Call this a skepticism-oriented analytical habit, not audit experience.

### How would you handle an incomplete client extract?

Preserve the file, profile it, reconcile control totals, identify missing periods/entities/accounts or rejected records, document the evidence, notify the audit team, request clarification/re-extraction through the approved channel, and do not proceed as if the population were complete.

### How do you explain technical issues to non-technical auditors?

Lead with audit impact, then evidence and decision. Example: “The join duplicated invoice lines, overstating the total; I corrected the grain and reconciliation now agrees.” Avoid unnecessary code details unless asked.

### How do you manage competing deadlines?

Make scope, dependencies, due dates, review time, and blockers visible. Prioritize by audit risk and engagement commitments, confirm expectations with managers, communicate early, and never sacrifice required validation silently.

### Tell me about working with external stakeholders.

Use Trans Globe Education: application/process updates with students and institutions, accurate records, client communication, workflow coordination. Do not invent stakeholder counts or deadlines.

## 30–60–90 Day Answer

- **First 30 days:** learn KPMG's audit methodology, D&A lifecycle, security/confidentiality rules, documentation standards, approved tools, escalation paths, and common ERP extracts; reproduce existing workflows under review.
- **Days 31–60:** support scoped acquisitions and analyses, perform profiling/reconciliation, document source-to-output logic, resolve defined issues, and communicate status clearly.
- **Days 61–90:** independently deliver routine components within authority, identify recurring data-quality patterns, and propose one controlled improvement to a validation, documentation, or workflow step.

## Pre-Interview Learning Plan

1. Build a fictional general-ledger project with chart of accounts, journal entries, users, vendors, invoices, and payments.
2. Create SQL tests for completeness, duplicate payments, unusual entries, cut-off, manual postings, and reconciliation.
3. Learn Alteryx fundamentals with non-confidential data and reproduce one SQL preparation workflow visually.
4. Complete a Databricks introductory SQL/lakehouse exercise and explain bronze/silver/gold layers.
5. Build one small Power BI report from the fictional ledger, including model, measures, filters, documentation, and QA.
6. Build a basic API exercise using public data, then explain authentication, pagination, errors, and logging.
7. Learn Power Query and one Power Automate approval/notification flow.
8. Do not add any tool to your résumé until you can independently demonstrate and defend it.

## Questions to Ask KPMG

- Which ERP systems and source formats does this team encounter most frequently?
- How are responsibilities divided between data consultants and the audit engagement team?
- What controls are required before transformed data can support audit procedures?
- Which tools should a new consultant become productive in first?
- How are D&A workflows reviewed, versioned, and documented across engagements?
- What does excellent performance look like after six months?
- How does the team support technical learning while maintaining audit quality and deadlines?

## English Requirement Reminder

The posting explicitly requires written and oral English fluency. The canonical profile does not verify language proficiency, so the résumé does not state it. Be prepared to answer the employer's screening question truthfully and to explain technical work clearly in English during the interview.

## Final Interview Rule

Distinguish clearly:

- **Hands-on:** SQL, PostgreSQL, Excel, extraction support, relational modelling, validation, constraints, CTEs/windows, transaction analysis, documentation, Git/GitHub Actions, stakeholder coordination.
- **Conceptual:** audit assertions, ERP architecture, ETL controls, audit analytics, Alteryx, Databricks, Power Platform, APIs, professional skepticism.
- **Gaps:** external audit, ERP extracts, full KPMG platform stack, API development/debugging, completed Power BI dashboards, proposals, leadership, and verified English proficiency.
