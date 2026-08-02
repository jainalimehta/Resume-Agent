---
name: tailor-jainali-resume
description: Create a truthful, ATS-compatible, single-page LaTeX resume and tailored cover letter for Jainali Mehta from a pasted job description, using Jainali's locked canonical 10-point format, compiling both to PDF, validating layout and text, and preserving immutable application history. Use for Business Analyst, Data Analyst, BI, reporting, operations analytics, and related Canadian applications.
---

# Tailor Jainali Resume

Create one job-specific resume and cover letter from verified facts while preserving Jainali's locked LaTeX format. This skill is the operating manual; `references/jainali-profile.md` is the complete candidate record and must remain the single canonical fact base.

## Candidate Quick Reference

- Jainali Mehta is based in Toronto, Ontario, Canada and is targeting beginner/graduate Business Analyst, Data Analyst, reporting, BI, and operations-analytics roles.
- She is entering the Canadian job market for the first time and has not studied or worked in Canada. State residence, education, and employment geography separately; never use wording that could imply Canadian education or experience.
- Contact: `jainali2000@gmail.com`, `linkedin.com/in/jainali-mehta`, and `github.com/jainalimehta`; omit phone because no current Canadian number is verified.
- Education: Master of Business Analytics, Edith Cowan University, Australia, 2023--2025; Integrated Master of Business Administration, Atmiya University, India, 2018--2022.
- Experience: Data Intern, AYLA Solutions, Australia, 2025; Support Executive, Trans Globe Education, India, 2022--2023; Administrative Executive, Arihant Investment, India, 2020--2021.
- Portfolio: three published PostgreSQL/SQL analytics repositories covering e-commerce, healthcare, and workforce analytics. Their AI-assisted analysis and recommendations are complete. Their Power BI planning is complete, but interactive dashboards and `.pbix` files are not yet published.
- Core verified tools and methods: PostgreSQL, SQL, advanced Microsoft Excel, Power BI planning, relational modelling, data cleaning and validation, KPIs, reporting, requirements gathering, process documentation, stakeholder communication, Agile ceremonies, Git, GitHub Actions, Microsoft Office, and Google Workspace.
- Explicit exclusions: no Tableau, no verified phone number, no invented metrics, and no claim of published interactive Power BI dashboards.

Read the canonical profile for the full responsibility-level evidence, coursework, credentials, repositories, additional academic projects, activities, safe phrasing, and known unknowns.

## Load Required Sources

Read these files completely before drafting:

1. `references/jainali-profile.md` - canonical facts.
2. `references/quality-rules.md` - truth, ATS, page, and QA requirements.
3. `references/reference-format-spec.md` - locked formatting contract.
4. The supplied job description.

Jainali's direct corrections override older sources. Never infer missing facts. If a job description requests an unsupported capability, disclose it in `match-notes.md` and omit it from affirmative resume claims.

## Analyze the Job Description

Extract:

- company, role, location, and business domain;
- responsibilities and behavioural requirements;
- required tools, methods, and keywords;
- must-have versus preferred qualifications.

Map every selected keyword to a verified profile fact. Record unsupported requirements as genuine gaps in `match-notes.md`.

Role emphasis:

- Business Analyst: requirements, process mapping, documentation, stakeholder communication, workflow coordination, and business coursework.
- Data Analyst: PostgreSQL, SQL, advanced Excel, data modelling, validation, KPIs, CTEs, window functions, and portfolio evidence.
- BI/reporting: reporting, KPI definition, dashboard planning, Power BI exposure, business insights, and recommendations.

All three published projects contain completed AI-assisted analysis and completed Power BI dashboard planning. Do not claim that interactive Power BI dashboards or `.pbix` files are published until Jainali confirms completion.

## Preserve the Locked Format

Use `assets/resume-template.tex` and `assets/cover-letter-template.tex` as the structural source of truth.

Do not redesign, replace, or casually modify:

- document class, paper size, geometry, typeface, colour, header, section styling, macros, list geometry, or one-column structure;
- the centered contact header;
- resume section order: Professional Summary, Core Competencies, Professional Experience, Business Analytics Projects, Education, Credentials;
- the matching cover-letter typography and header.

Tailor content, ordering within sections, terminology, and project emphasis. Rewrite text to fit; do not solve overflow by shrinking the locked typography or margins.

## Create an Immutable Application

Run from the repository root:

```bash
python3 skills/tailor-jainali-resume/scripts/new_application.py \
  --company "Company" \
  --role "Role" \
  --location "Toronto, ON" \
  --job-description /path/to/job-description.md
```

Edit only the newly created folder's:

- `resume.tex`
- `cover-letter.tex`
- `match-notes.md`

Preserve the job description verbatim. Never overwrite an earlier application.

## Truth Rules

- Use `Data Intern` for AYLA Solutions, dated 2025.
- Use `Support Executive`, Trans Globe Education, 2022-2023.
- Use `Administrative Executive`, Arihant Investment, 2020-2021.
- Use Master of Business Analytics, Edith Cowan University, 2023-2025.
- Use Integrated Master of Business Administration, Atmiya University, 2018-2022.
- Never list Tableau.
- Omit phone until a current Canadian number is verified.
- Keep Education and Credentials separate.
- Do not invent metrics, outcomes, dates, tools, credentials, or responsibilities.
- Do not label coursework or projects as certifications.
- Never use ambiguous phrases such as `Toronto-based graduate`. If location matters, say Jainali currently lives in Toronto, then name the Australian and Indian institutions and employment locations separately.

## Drafting Standard

- Lead with evidence and job relevance; do not inflate seniority.
- Use exact capitalization for names, degrees, employers, titles, technologies, and credentials.
- Prefer concise action-and-scope bullets. Do not fabricate a result when no measured result is verified.
- Preserve the distinction between completed SQL/AI work, completed Power BI planning, and unpublished interactive dashboard implementation.
- Select the strongest verified portfolio evidence for the posting; do not add an older project merely to fill space.
- Keep the page visually full but readable. Remove repetition before removing relevant evidence.
- A cover letter must connect Jainali's education, Australian internship, portfolio, and earlier process-support experience to the employer's actual needs; it must not merely paraphrase the resume.

## Build and Verify

```bash
python3 skills/tailor-jainali-resume/scripts/build_application.py \
  applications/<version-folder>
```

Before completion:

1. Resolve every build failure and short-line warning.
2. Require exactly one resume page and one cover-letter page.
3. Confirm searchable text, embedded fonts, correct reading order, and no Tableau claim.
4. Inspect `qa/resume.png` and `qa/cover-letter.png` for clipping, overlap, inconsistent alignment, excessive whitespace, crowded emphasis, and one- or two-word final fragments.
5. Rebuild after every material content change.
6. Mark the application `verified` in `applications/HISTORY.md` only after all checks pass.

Return both PDFs, both LaTeX sources, the preserved job description, and match notes.
