# Build QA

- Resume page count: PASS — one US Letter page.
- Cover-letter page count: PASS — one US Letter page.
- Short-line warnings: PASS — zero.
- Cover-letter length: PASS — 409 extracted words.
- Font embedding: PASS — all Latin Modern fonts embedded with Unicode mappings.
- ATS extraction: PASS — contact details, headings, dates, employers, project titles, bullets, education, and credentials extract as searchable text in reading order.
- Canonical geography: PASS — Toronto residence is separate from Australian and Indian education and employment.
- Education accuracy: PASS — both canonical degrees, institutions, countries, and dates are preserved.
- Experience accuracy: PASS — AYLA Solutions remains `Data Intern`; earlier titles and dates match the canonical profile.
- Project accuracy: PASS — only the three verified GitHub projects are included under their locked titles.
- Governance wording: PASS — project controls are described as a governance foundation, not regulated production-governance experience.
- Model wording: PASS — Machine Learning is identified as coursework and AI use as SQL-grounded assisted interpretation, not model development.
- Unsupported-tool control: PASS — Databricks, Python, ML libraries, unstructured pipelines, feature engineering, interpretability, and model lifecycle appear only in an explicit non-experience statement in the cover letter.
- Power BI wording: PASS — dashboard planning is claimed; interactive implementation is not claimed.
- Banned tools: PASS — Tableau and IBM SPSS Statistics do not appear.
- Visual inspection: PASS — centered headers, recipient block, section rules, employer and project rows, dates, bullets, education, credentials, and signature are aligned; no clipping, overlap, orphaned heading, or excessive blank region.
- Locked format: PASS — canonical 10-point class, geometry, Latin Modern typography, section order, macros, and one-column ATS structure preserved.

## Verified Outputs

- `resume.pdf`
- `cover-letter.pdf`
- `qa/resume.png`
- `qa/cover-letter.png`
