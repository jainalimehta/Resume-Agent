---
name: tailor-jainali-resume
description: Create a truthful, ATS-compatible, job-specific one-page LaTeX resume and matching one-page cover letter for Jainali Mehta from a job description or posting. Use for Business Analyst, Data Analyst, BI, reporting, operations analytics, referral applications, interview-defense preparation, and related Canadian applications. Preserve Jainali's verified profile, Dhruv-inspired locked format, immutable application history, and compile/render/QA workflow.
---

# Tailor Jainali Resume

Create the strongest truthful version of Jainali's application for one role. Optimize presentation, not history. Use the compact Dhruv-inspired layout adapted for Jainali; never copy Dhruv's facts or permissions to invent work.

## Load Required Sources

Read completely before drafting:

1. `references/jainali-profile.md` - canonical identity, education, employment, portfolio, and skills.
2. `references/freelance-evidence.md` - canonical freelance functions and engagement-level evidence.
3. `references/quality-rules.md` - truth, ATS, page-budget, and QA rules.
4. `references/reference-format-spec.md` - locked visual and structural contract.
5. The complete job description or posting.

Jainali's direct corrections override older sources. Do not infer a missing candidate fact.

## Candidate Guardrails

- Position Jainali as a Business Analytics graduate and early-career analyst living in Toronto, not an experienced or senior analyst.
- Keep geography explicit: current residence in Canada; education and Data Intern experience in Australia; earlier employment in India.
- Use verified titles and dates exactly: Data Intern, AYLA Solutions, 2025; Support Executive, Trans Globe Education, 2022--2023; Administrative Executive, Arihant Investment, 2020--2021.
- Use the exact degrees and dates in the canonical profile.
- Omit phone, work authorization, citizenship, language proficiency, GPA, honours, and unverified dates.
- Never list Tableau or IBM SPSS Statistics without new verified evidence.
- Describe Power BI only as dashboard/KPI/visualization planning until interactive dashboards or `.pbix` files are verified.
- Preserve exact published project titles: `E-Commerce Sales Analytics`, `Healthcare Patient & Hospital Analytics`, and `HR Analytics`.
- Jainali confirms genuine work as a freelance developer, freelance architect, and freelance data engineer. Include it selectively as standalone experience only when the freelance ledger supplies a date range and defensible engagement details.
- Never invent freelance clients, engagements, dates, production status, metrics, team sizes, dataset sizes, tools, collaboration hierarchy, or outcomes. Portfolio work is not client work unless Jainali explicitly confirms that relationship.

## Analyze the Job Description

Extract:

- company, exact role title, location, domain, and likely seniority;
- core responsibilities and expected outcomes;
- must-have and preferred qualifications;
- repeated tools, methods, behavioural terms, and domain language;
- location, regulatory, work-arrangement, and authorization expectations.

Separate real requirements from employer marketing language. Do not keyword-stuff.

## Build the Evidence Map

For each important requirement, classify the best canonical evidence:

- **Direct:** explicitly demonstrated in the profile.
- **Adjacent:** a related foundation that must be described narrowly.
- **Unsupported:** no defensible evidence; omit the affirmative claim and record the gap.

Record this map in `match-notes.md`. Every job-description keyword used as a skill or experience claim must point to verified evidence.

## Choose the Narrative

Select three to five reasons Jainali fits the role. Prioritize:

1. relevance to core responsibilities;
2. direct evidence over adjacent evidence;
3. recent internship and current published portfolio;
4. ownership level actually supported by the profile;
5. learning ability shown through completed education and hands-on work.

Use the same factual themes across resume and cover letter without duplicating whole sentences.

Role emphasis:

- **Business Analyst:** requirements, process mapping, documentation, workflow coordination, stakeholder communication, Agile ceremonies, and business coursework.
- **Data Analyst:** PostgreSQL, SQL, advanced Excel, relational modelling, validation, KPIs, CTEs, window functions, segmentation, and trend analysis.
- **BI/reporting:** reporting requirements, Excel reporting, KPI definition, Power BI planning, visualization requirements, insights, and recommendations.

## Preserve the Locked Format

Use `assets/resume-template.tex` and `assets/cover-letter-template.tex` as structural source of truth.

Resume contract:

- US Letter, `article`, 9.5-point option, single column.
- Two-row left/right header: name and email, then LinkedIn and GitHub/location.
- Compact small-caps headings with thin rules.
- Locked order: Skills, Experience, Projects, Education, Credentials.
- Bold evidence labels in experience and project bullets.
- Every Skills category must render on exactly one visual line. Split a wrapping row into two supported categories or shorten it.

Cover-letter contract:

- US Letter, 11 point, matching two-row header and rule.
- Current date, centered `RE: Role, Company`, verified recipient or `Dear Hiring Manager,`.
- Four to six short paragraphs, normally 300--425 words.
- Plain `Best regards,` close and Jainali's name; never fabricate a signature image.

Do not change the document class, margins, header, section order, commands, or typography to make one application fit. Rewrite and select content instead.

## Tailor the Resume

- Reorder skill rows and terms by job relevance.
- Require every Skills row to finish on the same rendered line. Do not accept a continuation line.
- Keep employers chronological; reorder bullets within each employer by relevance.
- Use compact labelled bullets: `action/scope + method + defensible result or purpose`.
- Prefer precise verbs, but keep `supported`, `contributed`, `participated`, or `coordinated` where ownership is limited.
- Use three internship bullets by default and one or two bullets for each earlier role.
- Add a standalone `Independent Freelance Consultant` entry when the role is relevant and `freelance-evidence.md` supports the dates and selected bullets. Use a narrower confirmed title such as `Freelance Data Engineer` when only one function is relevant.
- Select one to three verified projects only when materially useful.
- Keep education concise and keep Credentials separate.

Apply one-page reductions in this order:

1. remove irrelevant projects or optional credentials;
2. remove the least relevant bullets from older roles;
3. tighten wording and remove duplicated skills;
4. reduce the number of skill rows/items;
5. reduce content-specific vertical whitespace only where the template permits.

Never shrink below the locked size, change margins, or use horizontal scaling.

If the page is visually underfilled, add content in this order: verified relevant freelance evidence, another relevant verified project, relevant verified coursework, a useful credential, then older verified evidence. Remove repetition before delivery. Do not create filler claims.

## Write the Cover Letter

1. Name the role, company, and specific fit.
2. Explain the strongest relevant evidence and its purpose or outcome.
3. Add one or two supporting examples tied to the employer's needs.
4. Show how Jainali communicates, coordinates, validates, or learns when relevant.
5. Close with specific motivation and an invitation to discuss the role.

Avoid generic biography, exaggerated enthusiasm, `perfect fit`, or copied job-description blocks. Mention a referral only when the user supplies or confirms it.

## Create an Immutable Application

Run from repository root:

```bash
python3 skills/tailor-jainali-resume/scripts/new_application.py \
  --company "Company" \
  --role "Exact Role" \
  --location "Toronto, ON" \
  --job-description /path/to/job-description.md
```

Edit only the new folder's `resume.tex`, `cover-letter.tex`, and `match-notes.md`. Preserve `job-description.md` verbatim. Never overwrite an earlier application.

## Build and Verify

```bash
python3 skills/tailor-jainali-resume/scripts/build_application.py \
  applications/<version-folder>
```

Before delivery:

1. Resolve every build failure and short-line warning.
2. Require exactly one resume page and one cover-letter page.
3. Confirm searchable text, embedded fonts, header-first reading order, locked section order, one-line Skills rows, and balanced page coverage.
4. Confirm no unresolved placeholders, unsupported Tableau/SPSS claim, renamed published project, false internship title, or unverified phone number.
5. Inspect `qa/resume.png` and `qa/cover-letter.png` for clipping, overlap, poor alignment, crowded text, excessive whitespace, and awkward wraps.
6. Rebuild after every material content change.
7. Mark the application `verified` in `applications/HISTORY.md` only after automated and visual QA pass.

Return both PDFs, both LaTeX sources, preserved job description, match notes, and any requested referral/interview guide.
