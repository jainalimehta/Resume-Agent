# Build QA

- Resume page count: PASS — one US Letter page.
- Cover-letter page count: PASS — one US Letter page.
- Short-line warnings: PASS — zero.
- Cover-letter length: PASS — 401 extracted words.
- Font embedding: PASS — all Latin Modern fonts embedded with Unicode mappings.
- ATS extraction: PASS — headings, dates, employers, project titles, bullets, education, and credentials extract as searchable text in reading order.
- Canonical identity and geography: PASS — Toronto residence is separate from Australian and Indian education and employment.
- Education accuracy: PASS — both canonical degree titles, institutions, countries, and dates are preserved.
- Experience accuracy: PASS — AYLA Solutions is `Data Intern`; other roles and dates match the canonical profile.
- Project accuracy: PASS — only the three verified GitHub projects are included; healthcare claims are described as portfolio data.
- Power BI wording: PASS — dashboard planning is claimed; interactive implementation is explicitly outstanding.
- Unsupported-tool control: PASS — AWS, Fabric, DAX, Power Query, Python, and predictive-model terms appear only in an explicit non-experience statement in the cover letter, not as affirmative resume skills.
- Banned tools: PASS — Tableau and IBM SPSS do not appear.
- Visual inspection: PASS — centered headers, rules, roles, dates, bullets, project labels, page margins, and signature are aligned; no clipping, overlap, orphaned heading, or excessive blank region.
- Locked format: PASS — canonical 10-point class, geometry, Latin Modern typography, section order, macros, and single-column ATS structure preserved.

## Verified Outputs

- `resume.pdf`
- `cover-letter.pdf`
- `qa/resume.png`
- `qa/cover-letter.png`
