# IFDS Group UAT Analyst — Interview Preparation

## Your Positioning

### 90-second introduction

“I recently completed a Master of Business Analytics at Edith Cowan University in Australia and now live in Toronto. My analyst foundation comes from a Data Intern role at AYLA Solutions, where I gathered and documented business and reporting requirements, supported SQL extraction and validation, prepared advanced Excel reporting, and participated in Agile planning and reviews. My portfolio strengthened the testing mindset behind UAT: I defined business rules, built relational integrity checks, validated outputs repeatedly, and documented the logic. Earlier roles developed my accuracy, follow-through, client communication, and confidential-record handling, including experience at Arihant Investment. I have not yet owned production UAT or worked with iFAST or Canadian mutual-fund processing, but I understand the core UAT workflow and would bring a disciplined, transparent approach to learning IFDS processes and testing changes against business intent.”

### Your five evidence stories

1. **Requirements:** AYLA — gathered and documented business/reporting requirements.
2. **Validation:** E-Commerce project — transaction states, recognized-revenue logic, keys, checks, repeatable validation.
3. **Complex process:** Healthcare project — linked appointments, treatment, billing, and claims with automated checks.
4. **Financial data:** Bank of Baroda project — Excel/SQL transaction analysis and recommendations.
5. **Accuracy and follow-through:** Trans Globe and Arihant — records, process updates, confidentiality, client communication.

## UAT Knowledge You Must Know

### What UAT is

User acceptance testing confirms that a system change supports the intended business process and satisfies agreed business requirements from the end user's perspective. It is not only checking whether the software runs; it checks whether the outcome is usable and correct for the business.

### A strong UAT workflow

1. Review requirements, specifications, release notes, process maps, and acceptance criteria.
2. Clarify ambiguity with business and technical stakeholders.
3. Assess risk and build a requirements-traceability matrix.
4. Define scope, environment, users/roles, test data, schedule, entry criteria, and exit criteria.
5. Write positive, negative, boundary, exception, and end-to-end test cases.
6. Execute each case and capture expected result, actual result, status, and evidence.
7. Log reproducible defects; agree severity and priority with the appropriate team.
8. Retest fixes and run regression tests on affected functions.
9. Report coverage, progress, risks, unresolved defects, and readiness for sign-off.

### Test-case fields

Use: test-case ID; requirement ID; objective; preconditions; user role; test data; numbered steps; expected result; actual result; pass/fail/blocked status; evidence; defect ID; tester/date.

Example: “For a cancelled order, confirm recognized revenue excludes the transaction.” Include a valid cancelled record, run the calculation, compare actual revenue with the stated rule, and attach query/output evidence.

### Test types

- **Positive:** valid input follows the expected business path.
- **Negative:** invalid, missing, duplicate, unauthorized, or out-of-sequence input is rejected or handled safely.
- **Boundary:** values at and just beyond limits, dates, cut-offs, and thresholds.
- **Regression:** previously working functions still work after the change.

### Risk-based testing

Prioritize by business/client impact, financial impact, regulatory exposure, transaction volume or frequency, complexity, size of change, interfaces, history of defects, and reversibility. At IFDS, high-impact candidates could include incorrect ownership records, transaction amounts, statuses, dates, entitlements, or client-facing outputs. Present these as examples, not knowledge of iFAST behaviour.

### Requirements traceability and coverage

A traceability matrix maps each business or functional requirement to one or more test cases and their status. It exposes missing coverage and supports readiness reporting. Coverage should include core workflows, exceptions, affected interfaces, role permissions, and changed plus dependent areas.

### Defect reporting

A useful defect contains a concise title, build/environment, preconditions, exact steps, test data, expected result, actual result, screenshots or logs, reproducibility, business impact, severity, and linked requirement/test case.

- **Severity** describes impact, such as an unavailable critical process or incorrect financial output.
- **Priority** describes urgency and release importance.

Never blame a developer. Report observable facts, evidence, and impact. Follow the agreed escalation path when a defect threatens scope, timing, or client outcomes.

### Agile versus waterfall

- **Waterfall:** requirements and phases are more sequential; UAT commonly occurs after a larger build phase, so early traceability and controlled change management matter.
- **Agile:** requirements evolve through smaller increments; testers clarify acceptance criteria early, test within iterations, give fast feedback, and repeat regression testing.

Your direct evidence is Agile participation at AYLA. Do not claim waterfall project experience.

## IFDS and Transfer-Agency Foundations

- A transfer agent maintains investor and account records and supports transaction and servicing processes for investment products.
- Mutual-fund activity can include purchases, redemptions, switches, distributions, account maintenance, and reporting. Accurate dates, prices or NAV inputs, units, amounts, statuses, approvals, and records matter.
- Segregated funds are insurance contracts with investment features and potential guarantees; do not represent yourself as knowledgeable in their processing.
- The posting names iFast Base, Desktop, and Web as affected applications. Do not guess their screens or workflows. Say you would learn the end-to-end business process, roles, data, interfaces, controls, and expected outcomes before designing cases.
- NISM Series XII gives you a securities-market foundation, but it is not CSC or IFIC and does not prove Canadian mutual-fund operations knowledge.

### Best answer to the domain gap

“I want to be direct that I have not processed mutual or segregated funds and have not used iFAST. My related foundation is investment-services record accuracy, transaction analysis, and NISM securities-market study. Before executing UAT, I would learn the business flow and terminology, review procedures and specifications, shadow a subject-matter expert, document questions, and confirm my understanding through walkthroughs. I would then trace requirements to cases and start with supervised execution until my results were consistently accurate.”

## Reporting and Walkthroughs

Useful UAT spreadsheet metrics include requirements covered, cases planned and executed, pass/fail/blocked/not-run counts, execution percentage, defects by severity and status, retest results, defect age, and unresolved release risks. Optimize for risk coverage and reliable evidence, not merely a high number of tests.

A functionality walkthrough should cover the business objective, scope and change, impacted users and processes, requirements, demonstration path, test coverage, results, open defects and risks, decisions, and next steps. Use plain business language for an Operations audience.

## Likely Questions and Answer Shape

### “How would you build a test plan from unclear requirements?”

Identify ambiguities and assumptions; map stakeholders; ask scenario-based questions; confirm acceptance criteria and exclusions; document decisions; rank risks; create traceability; review the draft before execution.

### “A developer says your defect is not reproducible. What do you do?”

Recheck environment, build, role, data, and steps; reproduce with fresh data; attach evidence and timestamps; compare expected behaviour with the requirement; walk through it collaboratively; update or close the defect if your result was wrong.

### “What if the deadline is near and testing is incomplete?”

Report exact coverage and blockers early; prioritize high-risk workflows and recent changes; ask for scope or resource decisions; document residual risk. Never quietly mark unexecuted cases as passed.

### “Tell me about a quality problem you found.”

Use the e-commerce project: explain the risk of counting pending, refunded, or cancelled activity as revenue; define the business rule; enforce data integrity; run validation; explain how the check prevents misleading reporting. Do not invent a discovered production defect or metric.

### “How do you ensure zero defects?”

Zero defects is a quality target, not a promise that testing can prove the absence of every defect. Improve confidence through clear requirements, risk-based coverage, controlled data and environments, traceability, negative and boundary tests, peer review, regression testing, evidence, and transparent residual-risk reporting.

## Smart Questions to Ask IFDS

1. What would the first 60–90 days of transfer-agency and iFAST training look like?
2. How are requirements, test cases, defects, and release sign-off managed today?
3. Which business processes and change types create the greatest UAT risk?
4. How does UAT work with Operations, business analysts, development, and client teams?
5. What distinguishes analysts who become independently effective in this role?

## 30-60-90 Day Answer

- **First 30 days:** learn IFDS terminology, transfer-agency processes, iFAST environments, controls, templates, defect workflow, and escalation paths; shadow walkthroughs and test execution.
- **Days 31–60:** write and execute supervised cases, maintain traceability and metrics, document reproducible issues, and build knowledge of common risk paths.
- **Days 61–90:** own a defined testing scope with review, communicate coverage and risks independently, support walkthroughs, and propose one evidence-based process improvement.

## Final Accuracy Guardrails

- Do not say you have formal UAT employment, iFAST experience, mutual-fund processing, CSC/IFIC, PowerPoint expertise, or waterfall delivery experience.
- Say “validation and quality-check foundation transferable to UAT,” not “UAT experience.”
- Use only the examples in this guide and the submitted resume; do not invent volumes, savings, teams, defects, or production outcomes.
