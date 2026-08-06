# Build QA

- Resume page count: PASS — one US Letter page.
- Cover-letter page count: PASS — one US Letter page.
- Short-line warnings: PASS — zero.
- Cover-letter length: PASS — 419 extracted words including contact and recipient blocks.
- Font embedding: PASS — all Latin Modern fonts are embedded with Unicode mappings.
- ATS extraction: PASS — contact details, headings, dates, employers, project titles, bullets, education and credentials extract as searchable text in reading order.
- Canonical geography: PASS — Toronto residence is separate from Australian and Indian education and employment.
- Education accuracy: PASS — both canonical degrees, institutions, countries and dates are preserved.
- Experience accuracy: PASS — AYLA Solutions remains `Data Intern`; earlier titles and dates match the canonical profile.
- Project accuracy: PASS — only the three published GitHub projects appear and retain their locked titles.
- Data-quality evidence: PASS — relational controls, assumptions, validation and GitHub Actions are supported by published project evidence.
- Power BI wording: PASS — dashboard planning is claimed; interactive implementation remains explicitly outstanding.
- Construction control: PASS — no construction employment or large-project experience is claimed.
- Migration and ETL control: PASS — migration, ETL, data-collection systems and Workday appear only as explicit gaps or interview-study topics.
- Tool control: PASS — DundasBI, NoSQL, specialized statistical packages and scripting languages are not affirmative resume claims.
- Tenure control: PASS — no two to four years of analyst employment is claimed.
- Banned tools: PASS — Tableau and IBM SPSS Statistics do not appear in the resume or cover letter.
- Visual inspection: PASS — centered headers, recipient block, section rules, employer and project rows, dates, bullets, education, credentials and signature are aligned; no clipping, overlap, orphaned heading or excessive whitespace.
- Locked format: PASS — canonical 10-point class, geometry, Latin Modern typography, section order, macros and one-column ATS structure are preserved.

## Verified Outputs

- `resume.pdf`
- `cover-letter.pdf`
- `qa/resume.png`
- `qa/cover-letter.png`
