# Interview Preparation — Systems Integrator 1, Job ID 64493

## Position Snapshot

- **Employer:** City of Toronto
- **Division:** Parks, Forestry & Recreation / Business & Technology Transformation
- **Location:** Metro Hall, 55 John Street, Toronto
- **Term:** Full-time temporary vacancy for 12 months
- **Posting deadline:** August 13, 2026
- **Core themes:** software-delivery lifecycle, requirements, logical data models, database loading and cleansing, ETL/SSIS, testing, implementation, sustainment, project artifacts, client relationships, rollout, training, and work/asset management.

## Honest 90-Second Introduction

I am an early-career analyst currently living in Toronto. I earned a Master of Business Analytics from Edith Cowan University in Australia and an Integrated MBA from Atmiya University in India. In 2025, I worked as a Data Intern at AYLA Solutions in Australia, where I gathered and documented business, data, and reporting requirements, supported SQL extraction and validation, prepared advanced Excel reports, and contributed dashboard insights. I participated in Agile planning and reviews, communicated progress, and maintained analytical documentation. My three PostgreSQL projects demonstrate logical relational modelling, keys and constraints, data-quality validation, CTEs and window functions, GitHub Actions checks, documented assumptions, AI-assisted recommendations, and Power BI reporting plans. My strongest current evidence is in databases, requirements, validation, and documentation rather than production software development or enterprise integration. I am interested in applying that foundation while developing deeper testing, ETL/SSIS, web/mobile, and work-asset-management knowledge.

## Evidence Bank

### 1. Business and Reporting Requirements — AYLA Solutions

- **Situation:** Stakeholder questions needed to be converted into structured analytical work.
- **Task:** Help document business, data, and reporting requirements and support reliable delivery.
- **Action:** Gathered requirements, supported SQL extraction and validation, prepared advanced Excel reports, contributed dashboard insights, participated in Agile reviews, communicated progress, and maintained documentation.
- **Result:** Supported reporting aligned with stakeholder questions. Do not invent a metric or implementation outcome.

### 2. Logical Data Model and Rules — E-Commerce Analytics

- **Situation:** Customers, products, orders, line items, and payments needed consistent relationships and revenue logic.
- **Task:** Create a normalized analytical foundation.
- **Action:** Defined keys, constraints, relationships, recognized-revenue rules, validation checks, and reporting indicators; added GitHub Actions.
- **Result:** Produced traceable SQL analysis, documented assumptions, AI-assisted recommendations, and Power BI plans.

### 3. Multi-Entity Operations — Healthcare Analytics

- **Situation:** Six operational entities covered patients, clinicians, appointments, treatments, billing, and claims.
- **Task:** Model and validate relationships and reporting logic.
- **Action:** Used PostgreSQL, CTEs, rankings, running totals, and lag comparisons; documented assumptions and automated validation.
- **Result:** Produced validated operational findings and reporting requirements.

### 4. Workforce Information — HR Analytics

- **Situation:** Department, employee, salary, performance, and attendance data required an integrated model.
- **Task:** Establish relational and reporting logic.
- **Action:** Normalized the schema, applied quality controls, analyzed workforce KPIs, and documented recommendations and reporting plans.
- **Result:** Created repeatable analysis with clear relationships and decision uses.

### 5. Client Coordination — Earlier Roles

- Use Trans Globe Education for client and institution communication, documentation, workflow updates, and administrative reporting.
- Use Arihant Investment for accurate confidential records, client communication, and dependable operational support.

## Likely Interview Questions

### Why are you applying without considerable software-development experience?

Be candid. Explain that your closest verified strengths are database design, SQL, requirements, validation, Agile teamwork, and documentation. Connect those strengths to the data and analysis side of systems integration. State that you are actively building SDLC, testing, ETL/SSIS, API, and asset-management knowledge. Never imply production web/mobile development.

### Walk us through the software development lifecycle.

Cover discovery and business case, project initiation, requirements, architecture and design, development/configuration, data preparation, testing, deployment planning, training and change readiness, release/cutover, hypercare, sustainment, monitoring, and lessons learned. Explain that traceability, security, privacy, accessibility, documentation, and risk management span every phase.

### How would you translate client needs into a solution?

Identify users and decision makers; understand outcomes, current process, pain points, inputs/outputs, data, rules, exceptions, integrations, security, performance, accessibility, and constraints; distinguish requirements from solutions; create models and acceptance criteria; evaluate options; confirm priorities; maintain traceability; and validate the design through walkthroughs and testing.

### How would you create a logical data model?

Identify business concepts and definitions, entities, attributes, candidate keys, relationships, cardinality, optionality, reference data, business rules, and history needs. Normalize to reduce anomalies, validate with stakeholders and representative scenarios, document assumptions, and trace the model to reporting, integration, security, and retention requirements.

### What is the difference between logical and physical data models?

A logical model describes business entities, attributes, relationships, and rules without committing to a specific database implementation. A physical model implements that design using platform-specific tables, columns, data types, indexes, constraints, partitions, and storage/performance decisions.

### How would you create a test strategy?

State this as your learned method: define scope, objectives, environments, roles, entry/exit criteria, requirement traceability, test data, functional, integration, data, security, performance, usability, accessibility, regression, UAT, defect handling, reporting, retesting, and sign-off. Connect it to your repeatable SQL and GitHub Actions validation, while noting those are not production system tests.

### How would you identify and manage project risks?

Identify the risk event, cause, consequence, likelihood, impact, owner, mitigation, contingency, trigger, due date, and residual exposure. Review risks regularly, connect mitigations to project activities, escalate according to thresholds, and distinguish risks from active issues.

### How would you plan implementation and rollout?

Confirm scope and readiness criteria; assess users, sites, data, interfaces, security, infrastructure, support, and training; select pilot, phased, parallel, or big-bang rollout based on risk; plan migration rehearsals, cutover, communications, rollback, command centre, hypercare, defect triage, performance monitoring, and transition to sustainment.

### How would you conduct a deliverable walkthrough?

Send the artifact and review objective in advance; identify required reviewers and decision authority; trace sections to requirements; walk through scenarios and exceptions; capture questions, defects, assumptions, decisions, owners, and due dates; distinguish approval from information; revise and version the artifact; confirm closure.

## ETL and SSIS Knowledge

- ETL extracts from sources, transforms according to business and quality rules, and loads targets in controlled sequence.
- SSIS packages commonly use control flow, data flow, connection managers, sources, transformations, destinations, parameters, variables, event handlers, logging, checkpoints, and deployment environments.
- Know full versus incremental loads, change detection, lookup/reference data, slowly changing dimensions, rejects, reruns, idempotency, dependencies, audit columns, error handling, reconciliation, and recovery.
- Testing should cover counts, totals, duplicates, nulls, types, formats, domain values, keys, relationships, transformation rules, rejected records, performance, restartability, and source-to-target traceability.
- Be explicit that these are study concepts; your verified implementation evidence is PostgreSQL analysis and validation, not production SSIS packages.

## Web, Mobile, and Integration Fundamentals

- Client/server architecture, HTTP/HTTPS, request/response, methods, status codes, headers, cookies, sessions, authentication, authorization, and TLS.
- APIs, endpoints, REST concepts, JSON and XML payloads, schemas, validation, pagination, rate limits, versioning, retries, idempotency, and error responses.
- Front-end basics: HTML structure, CSS presentation, JavaScript behaviour, responsive design, browser compatibility, accessibility, and client-side validation.
- Mobile considerations: responsive web versus native/hybrid apps, connectivity, offline use, synchronization, device permissions, security, and field-user experience.
- Integration patterns: synchronous APIs, asynchronous messaging, batch/file transfer, ETL, webhooks, queues, and scheduled jobs.
- Never claim hands-on language or framework experience until you have built and can explain a real project.

## Work and Asset Management Fundamentals

- Core concepts: assets, locations, hierarchies, service requests, work orders, preventive maintenance, job plans, labour, materials, meters, inspections, failure codes, status lifecycle, costs, and maintenance history.
- Important data relationships: asset-to-location, parent/child assets, work order-to-asset/location, job plans, classifications, people/crews, inventory, and spatial coordinates.
- Implementation needs: current/future process mapping, configuration versus customization, data cleansing/migration, integrations, roles/security, mobile/field use, reports, testing, training, rollout, and sustainment.
- Risks: poor master data, unclear process ownership, excessive customization, weak integration controls, low field adoption, incomplete testing, and insufficient support transition.

## Required Project Artifacts to Study

- **Project charter:** purpose, objectives, scope, deliverables, stakeholders, governance, assumptions, constraints, milestones, risks, budget, and success measures.
- **Statement of work:** services, deliverables, acceptance criteria, schedule, responsibilities, dependencies, assumptions, pricing, change control, and terms.
- **Project plan:** work breakdown, owners, dependencies, estimates, milestones, critical path, resources, communications, quality, risk, and status cadence.
- **Gap analysis:** current state, target state, gap, impact, priority, option, recommendation, owner, and action.
- **Design document:** context, requirements, architecture, components, interfaces, data, security, errors, logging, deployment, testing, and operational support.
- **Status report:** period, accomplishments, milestone health, next steps, budget/resource status, risks, issues, decisions, and changes.
- **Lessons learned:** what happened, impact, root cause, what worked, what did not, recommendation, owner, and future application.

## Questions for the Panel

- Which digital solutions and work/asset-management capabilities would this position support first?
- How is work divided among business analysis, architecture, development, data, testing, vendors, and operational teams?
- Which technology stack, integration patterns, databases, ETL tools, and test-management tools are currently used?
- What are the most important data, process, and sustainment challenges in the transformation portfolio?
- What project artifacts and governance standards does the team expect this role to own?
- What would strong performance look like in the first three and six months?

## Final Checklist

- Apply before August 13, 2026.
- Recheck the official posting for amendments immediately before submission.
- Prepare two-minute STAR examples from AYLA, Trans Globe, Arihant, and all three repositories.
- Review each schema, constraint, validation query, GitHub Actions workflow, AI section, and Power BI plan.
- Practise drawing a logical data model and explaining cardinality, keys, constraints, and normalization.
- Practise a requirement-to-design-to-test traceability example.
- Study SDLC, SSIS/ETL, REST/JSON/XML, test strategies, rollout planning, and work/asset-management concepts.
- Never claim web/mobile development, SSIS, SQL Server, Oracle, production ETL, Maximo, geospatial, or formal system-testing experience.
- Never imply Canadian education or employment; state Toronto residence separately from Australian and Indian experience.
