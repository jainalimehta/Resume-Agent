# Build QA

- Resume page count: PASS — one US Letter page.
- Cover-letter page count: PASS — one US Letter page.
- Short-line warnings: PASS — zero.
- Cover-letter length: PASS — 413 extracted words.
- Font embedding: PASS — all Latin Modern fonts embedded with Unicode mappings.
- ATS extraction: PASS — contact details, headings, dates, employers, project titles, bullets, education, and credentials extract as searchable text in reading order.
- Canonical geography: PASS — Toronto residence is separate from Australian and Indian education and employment.
- Education accuracy: PASS — both canonical degrees, institutions, countries, and dates are preserved.
- Experience accuracy: PASS — AYLA Solutions remains `Data Intern`; earlier titles and dates match the canonical profile.
- Project accuracy: PASS — only the three verified GitHub projects are included under their locked titles.
- Retail wording: PASS — e-commerce work is described as retail-relevant portfolio analysis, not professional retail experience.
- Tableau control: PASS — Tableau does not appear in the resume or cover letter and is not claimed.
- Power BI wording: PASS — dashboard planning is claimed; interactive implementation is explicitly outstanding.
- Experience-level wording: PASS — the cover letter explicitly states that the requested 2-3 years of Data Analyst employment are not held.
- Unsupported-scope control: PASS — no professional planning/allocation, large retail datasets, BI administration, dashboard training, or senior-leadership presentation is claimed.
- Banned tools: PASS — Tableau and IBM SPSS Statistics do not appear in application PDFs.
- Visual inspection: PASS — centered headers, recipient block, section rules, employer/project rows, dates, bullets, education, credentials, and signature are aligned; no clipping, overlap, orphaned heading, or excessive blank region.
- Locked format: PASS — canonical 10-point class, geometry, Latin Modern typography, section order, macros, and one-column ATS structure preserved.

## Verified Outputs

- `resume.pdf`
- `cover-letter.pdf`
- `qa/resume.png`
- `qa/cover-letter.png`
