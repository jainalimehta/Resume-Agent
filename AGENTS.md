# Jainali Mehta Resume Agent

Use the `tailor-jainali-resume` skill in `skills/tailor-jainali-resume/` whenever Jainali pastes a job description or asks for a resume, CV, cover letter, or application package.

## Candidate Identity and Positioning

- Jainali Mehta lives in Toronto, Ontario, Canada and is applying as a beginner/graduate candidate for Business Analyst, Data Analyst, reporting, BI, and operations-analytics work.
- Her relevant professional foundation is Australian experience as a `Data Intern` at AYLA Solutions in 2025. Do not present her as an experienced or senior analyst.
- Earlier experience is `Support Executive` at Trans Globe Education in India, 2022--2023, and `Administrative Executive` at Arihant Investment in India, 2020--2021.
- Education must appear exactly as `Master of Business Analytics`, Edith Cowan University, Australia, 2023--2025, and `Integrated Master of Business Administration`, Atmiya University, India, 2018--2022.
- Her three published GitHub projects cover e-commerce, healthcare, and workforce analytics using PostgreSQL and SQL. AI-assisted analysis and Power BI dashboard planning are complete; interactive Power BI dashboards and `.pbix` files are not yet published.
- Contact details, credentials, verified coursework, responsibility-level evidence, repository links, older analysis work, skills, activities, and known unknowns are documented in `skills/tailor-jainali-resume/references/jainali-profile.md`. Read that file completely before drafting.

## Non-Negotiable Requirements

- Treat `skills/tailor-jainali-resume/references/jainali-profile.md` as the canonical fact base.
- Treat `skills/tailor-jainali-resume/assets/resume-template.tex` as the locked resume format and `assets/cover-letter-template.tex` as its matching cover-letter format.
- Never invent experience, outcomes, metrics, dates, tools, or credentials.
- Describe the AYLA Solutions internship as `Data Intern`, not Business Analyst Intern.
- Never list Tableau unless Jainali explicitly confirms new Tableau experience.
- Create an ATS-readable, single-page resume and single-page cover letter in LaTeX and PDF.
- Preserve the canonical 10-point document class, geometry, Latin Modern serif typography, centered contact header, section styling, macros, and section order.
- Keep Education and Credentials as separate resume sections.
- Avoid columns, sidebars, icons, photos, charts, skill bars, headers/footers, and scanned text. Do not redesign the locked template.
- Avoid wrapped lines whose final fragment contains only one or two words.
- Create a new immutable folder under `applications/` for every job description and update `applications/HISTORY.md`.
- Run automated QA and visually inspect both rendered pages before completion.

## Job-Description Workflow

1. Read the full skill, canonical profile, quality rules, locked format specification, and job description.
2. Map every proposed keyword to verified evidence; record unsupported requirements as gaps.
3. Create a new immutable application folder with the supplied script.
4. Tailor only content and evidence emphasis inside the locked LaTeX structure.
5. Compile and resolve all automated failures and short-line warnings.
6. Visually inspect both rendered pages, then mark the history entry verified and return the source and PDF files.

## Standard Invocation

Jainali may paste only a job description. Infer the company, role, and location when available. Use `unknown-company` or `unknown-role` rather than blocking when either cannot be inferred.
