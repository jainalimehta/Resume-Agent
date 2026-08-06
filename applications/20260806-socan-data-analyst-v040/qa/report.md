# Build QA

- Resume page count: PASS — one US Letter page.
- Cover-letter page count: PASS — one US Letter page.
- Short-line warnings: PASS — zero.
- Cover-letter length: PASS — 425 extracted words including the contact and recipient blocks.
- Font embedding: PASS — all Latin Modern fonts are embedded with Unicode mappings.
- ATS extraction: PASS — contact details, headings, dates, employers, project titles, bullets, education and credentials extract as searchable text in reading order.
- Canonical geography: PASS — Toronto residence is separate from Australian and Indian education and employment.
- Education accuracy: PASS — both canonical degrees, institutions, countries and dates are preserved.
- Experience accuracy: PASS — AYLA Solutions remains `Data Intern`; earlier titles and dates match the canonical profile.
- Project accuracy: PASS — only the three verified GitHub projects are included under their locked titles.
- Data-quality evidence: PASS — relational controls, documented assumptions, repeatable validation and GitHub Actions are supported by published project evidence.
- Power BI wording: PASS — dashboard planning is claimed; independent interactive implementation is explicitly outstanding.
- Cloud-platform control: PASS — Databricks, Python, Spark, distributed computing, Lakehouse, Genie and semantic-layer tools appear only in explicit non-experience or learning statements.
- Tenure control: PASS — no two years of analytics-platform experience is claimed.
- Language and interest control: PASS — English proficiency, French fluency and passion for music are not claimed.
- Banned tools: PASS — Tableau and IBM SPSS Statistics do not appear in the resume or cover letter.
- Visual inspection: PASS — centered headers, recipient block, section rules, employer and project rows, dates, bullets, education, credentials and signature are aligned; no clipping, overlap, orphaned heading or excessive blank region.
- Locked format: PASS — canonical 10-point class, geometry, Latin Modern typography, section order, macros and one-column ATS structure are preserved.

## Verified Outputs

- `resume.pdf`
- `cover-letter.pdf`
- `qa/resume.png`
- `qa/cover-letter.png`
