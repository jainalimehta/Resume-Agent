# Build QA

- Resume page count: PASS — one US Letter page.
- Cover-letter page count: PASS — one US Letter page.
- Short-line warnings: PASS — zero.
- Cover-letter length: PASS — 416 extracted words including contact and recipient blocks.
- Font embedding: PASS — all Latin Modern fonts are embedded with Unicode mappings.
- ATS extraction: PASS — contact details, headings, dates, employers, project titles, bullets, education and credentials extract as searchable text in reading order.
- Canonical geography: PASS — Toronto residence is separate from Australian and Indian education and employment.
- Education accuracy: PASS — both canonical degrees, institutions, countries and dates are preserved.
- Experience accuracy: PASS — AYLA Solutions remains `Data Intern`; earlier titles and dates match the canonical profile.
- Project accuracy: PASS — E-Commerce Sales Analytics keeps its locked title; Bank of Baroda and Online GST projects match the canonical profile.
- GST correction: PASS — Google Forms and Excel are listed; IBM SPSS Statistics is absent.
- Banking evidence: PASS — Bank of Baroda is presented as analysis work, not professional banking employment.
- Power BI wording: PASS — dashboard planning is claimed; interactive implementation is explicitly outstanding.
- Product-experimentation control: PASS — A/B testing, event logs, large-scale data and senior-leadership reporting appear only as explicit gaps or study topics.
- Tool control: PASS — Metabase, Sigma, Periscope, Mode, dbt, cloud warehouses, Python and R are not affirmative resume claims.
- Tenure control: PASS — no two years of analyst employment is claimed.
- Banned tools: PASS — Tableau and IBM SPSS Statistics do not appear in the resume or cover letter.
- Visual inspection: PASS — centered headers, recipient block, section rules, employer and project rows, dates, bullets, education, credentials and signature are aligned; no clipping, overlap, orphaned heading or excessive whitespace.
- Locked format: PASS — canonical 10-point class, geometry, Latin Modern typography, section order, macros and one-column ATS structure are preserved.

## Verified Outputs

- `resume.pdf`
- `cover-letter.pdf`
- `qa/resume.png`
- `qa/cover-letter.png`
