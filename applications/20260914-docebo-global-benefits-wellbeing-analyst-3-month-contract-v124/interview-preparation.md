# Interview Preparation — Docebo Global Benefits & Wellbeing Analyst

## Candid Fit Assessment

This is a credible entry-level stretch application. Docebo explicitly welcomes recent graduates and candidates with up to one year of relevant experience. Jainali directly brings business/analytics education, advanced Excel, reporting requirements, data validation, workforce analytics, confidential-record handling, workflow coordination, client communication, and AI-assisted analysis.

The major gaps are Dayforce, benefits administration, open enrollment, carrier billing, payroll-deduction reconciliation, leave administration, workplace accommodations, US/Canadian benefits rules, and employee-facing HR support. Treat these as learning areas and never convert adjacent analytics or administrative work into benefits experience.

## 60-Second Introduction

> I live in Toronto and completed a Master of Business Analytics at Edith Cowan University in Australia. At AYLA Solutions, I gathered reporting requirements, supported SQL extraction and validation, prepared advanced Excel reports, and contributed reporting insights through Agile planning and reviews. Earlier roles involved accurate documentation, process updates, recurring workflows, confidential records, and client communication. I also built a published HR Analytics project covering departments, employees, salaries, performance, attendance, headcount, compensation, hiring, and tenure, with repeatable validation and AI-assisted recommendations. Formal benefits administration and Dayforce would be new to me, but the role fits my strengths in careful data handling, clear service, and structured learning.

## Why Docebo

> Docebo interests me because the role combines employee care, accurate operations, and learning under experienced Total Rewards specialists within an AI-first technology company. I appreciate the values of Clear is Kind, Own Outcomes, and Progress Over Perfection. I would bring careful validation and documentation immediately while developing benefits and Dayforce knowledge through coaching, approved procedures, and supervised practice.

## Benefits Administration Workflow

Learn this as a general operating model, not claimed experience:

1. Confirm the employee event, effective date, location, eligibility, and approved source documentation.
2. Check the applicable plan rules and enrollment window.
3. Enter or update the record only through the authorized process.
4. Validate plan, coverage level, dependent information, employee/employer cost, and payroll deduction.
5. Confirm the HRIS status and any carrier or payroll file/output.
6. Reconcile downstream records, document exceptions, and escalate discrepancies.
7. Communicate clearly with the employee without offering unapproved legal, tax, or financial advice.
8. Protect sensitive information and retain records under the approved policy.

Dayforce's current benefits documentation describes eligibility-driven plan availability, employee elections, plan records, carrier exports, and payroll mappings that apply deductions or earnings. Use this to understand system concepts; Docebo's configuration and procedures control the actual work.

## Carrier Billing Reconciliation

### Proposed monthly process

1. Obtain the approved carrier statement and HRIS enrollment/deduction extract for the same coverage period.
2. Confirm file versions, billing dates, plan names, currency, and population scope.
3. Standardize identifiers and formats without altering source files.
4. Match using an approved unique identifier rather than names alone.
5. Compare coverage, tier, effective/termination dates, employee count, employer cost, employee cost, and total premium.
6. Classify exceptions: carrier-only, HRIS-only, amount mismatch, plan/tier mismatch, effective-date mismatch, duplicate, or missing identifier.
7. Investigate timing differences and retroactive adjustments before treating them as errors.
8. Document the cause, owner, action, status, and financial impact; obtain approval before corrections.
9. Re-run the reconciliation and retain evidence of sign-off.

### Excel concepts to study

- Excel Tables and structured references;
- `XLOOKUP` or `VLOOKUP` for matching records;
- `COUNTIF`/`COUNTIFS` for duplicates and exception counts;
- `SUMIF`/`SUMIFS` for plan and employee totals;
- `IF`, `IFERROR`, date functions, text cleaning, and conditional formatting;
- pivot tables for counts and dollar summaries by plan, location, and exception type;
- source/control totals, filtered exception lists, and protected distribution.

Example study formulas:

```text
=XLOOKUP([@EmployeeID], HRIS[EmployeeID], HRIS[Plan], "Not found")
=IF([@CarrierPlan]=[@HRISPlan], "Match", "Review")
=COUNTIF(Carrier[EmployeeID],[@EmployeeID])
=SUMIFS(Carrier[Premium],Carrier[Plan],A2)
```

Do not claim prior use of `VLOOKUP` or `XLOOKUP` unless you can genuinely demonstrate it. The resume lists only verified advanced Excel, formulas, and pivot tables.

## Handling an Employee Benefits Question

> I would listen carefully, confirm the employee's question and relevant dates, check the approved plan document, HRIS record, and internal knowledge source, and explain only what is supported in clear language. If the question involved eligibility interpretation, a disputed claim, legal rights, tax advice, an accommodation, or a system discrepancy outside my authority, I would explain the next step and escalate it to the appropriate specialist. I would document the interaction appropriately and avoid unnecessary sensitive details.

Warm service means acknowledging the person's concern and giving a clear next step. It does not mean guessing or making exceptions outside policy.

## Leave and Accommodation Tracking

A reliable tracker may include case ID, employee ID, jurisdiction, leave type, request date, start/end dates, intermittent status, documents requested/received, notice deadlines, current status, next action, owner, and last contact. Access must be restricted because health and accommodation information is sensitive.

For US FMLA, the Department of Labor's current guidance covers employer coverage, employee eligibility, qualifying reasons, notices, certification, benefit continuation, intermittent/reduced schedules, and reinstatement. Ontario's Employment Standards Act guide lists multiple job-protected leaves, with different eligibility and documentation rules. Never apply one jurisdiction's rules to another or give legal advice; use the current authoritative source and Docebo's approved escalation process.

## Retirement-Plan Basics

- **RRSP:** A Canadian registered retirement savings plan established by an individual and registered by the CRA. Contributions may be deductible within applicable limits; tax is generally deferred until withdrawal. Employer programs and payroll handling depend on plan design.
- **401(k):** A US qualified retirement-plan feature that can allow employees to defer part of wages into individual accounts, with possible employer contributions. Traditional elective deferrals and qualified Roth treatment differ.

At interview level, explain the distinction and the need for accurate eligibility, elections, contribution/deduction data, effective dates, payroll mapping, and employee communication. Do not advise an employee on investment, tax, or personal contribution decisions.

## Responsible AI Answer

> I use AI to support bounded analytical tasks and develop recommendations from validated SQL results. In benefits operations, I would use only Docebo-approved enterprise tools and would not enter employee, health, payroll, dependent, or other confidential data unless policy explicitly permits it. AI could help structure a checklist or draft a general communication, but I would verify policy language, calculations, recipients, tone, and privacy before use. I would remain accountable for every record and message.

## Likely Interview Questions

- Why Docebo and why Global Total Rewards?
- What interests you about benefits and wellbeing?
- Tell us about a time you handled confidential information.
- How do you ensure spreadsheet accuracy?
- How would you reconcile carrier billing with Dayforce data?
- How would you handle an employee question you could not answer?
- What is your experience with `VLOOKUP`, `XLOOKUP`, and pivot tables?
- Tell us about your HR Analytics project.
- How do you prioritize several time-sensitive tasks?
- How do you respond to constructive feedback?
- What would you track in a leave or accommodation file?
- What is your understanding of RRSPs, 401(k)s, FMLA, and provincial leaves?
- How would you use AI responsibly with employee data?
- What is your experience with Dayforce or another HRIS?
- Can you attend the office Tuesday through Thursday for the contract term?

## STAR Story Plan

- **AYLA — accuracy and feedback:** requirements, SQL extraction support, validation, advanced Excel reporting, Agile reviews, progress updates, and documentation.
- **HR Analytics — people data:** workforce model, definitions, headcount/compensation/performance/attendance/hiring/tenure analysis, and repeatable checks.
- **Trans Globe — frontline coordination:** accurate documentation, application/process updates, workflows, reporting, and communication with students and institutions.
- **Arihant — confidentiality:** investment-services records, data entry, documentation, accuracy, and client communication.
- **Healthcare Analytics — billing and claims data:** relational model, billing status, insurance claims, operational measures, and automated validation.

Never invent volumes, dollar discrepancies, employee counts, error reductions, deadlines, or production outcomes.

## Questions to Ask Docebo

- Which benefits processes and jurisdictions would this analyst support during the first month?
- What does the monthly carrier-to-Dayforce reconciliation currently look like?
- Which Dayforce access, sandbox, documentation, and training will be available?
- How are routine employee questions separated from cases that require specialist escalation?
- What leave and accommodation trackers or case-management tools are used?
- Which international data project or wellbeing communication would be the first assignment?
- How will success be measured during the three-month contract?
- What factors would determine extension or permanent placement?

## 30/60/90-Day Outline

**Days 1–30:** Learn plan structures, jurisdictions, Dayforce navigation, privacy/access rules, calendars, escalation paths, reconciliation files, standard communications, and recurring deadlines. Shadow cases and complete supervised checks.

**Days 31–60:** Own bounded routine inquiries and tracking tasks; execute a reviewed reconciliation segment; maintain complete case notes; support an approved communication or international-data task.

**Days 61–90:** Handle defined recurring processes with appropriate independence, identify recurring exceptions, improve one checklist or tracker with approval, and complete a documented handoff for extension or transition.

## Accuracy Guardrails

- Do not claim Dayforce or HRIS experience.
- Do not claim benefits, leave, open-enrollment, onboarding, carrier, payroll, FMLA, RRSP, 401(k), or accommodations administration.
- Do not present healthcare insurance-claim analysis as employee-benefits experience.
- Do not claim employee-facing HR support; use verified client-service examples.
- Do not claim `VLOOKUP` or `XLOOKUP` experience unless personally demonstrable.
- Describe Power BI only as dashboard planning.
- Do not claim Canadian education/employment, work authorization, contract availability, hybrid attendance, or extension interest without confirmation.

## Official Study Sources

- [Dayforce — Getting Started with Dayforce Benefits](https://help.dayforce.com/r/documents/Benefits-Administration-Guide/Getting-Started-with-Dayforce-Benefits)
- [US Department of Labor — FMLA Fact Sheet #28](https://www.dol.gov/agencies/whd/fact-sheets/28-fmla)
- [Ontario — Employment Standards Act Guide](https://www.ontario.ca/document/your-guide-employment-standards-act-0)
- [Canada Revenue Agency — Registered Retirement Savings Plans](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/registered-retirement-savings-plan-rrsp.html)
- [Internal Revenue Service — 401(k) Plans](https://www.irs.gov/retirement-plans/401k-plans)
- [Docebo — Careers and Culture](https://www.docebo.com/careers/)

