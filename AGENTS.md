# Jainali Mehta Resume Agent

Use the `tailor-jainali-resume` skill in `skills/tailor-jainali-resume/` whenever Jainali pastes a job description or asks for a resume, CV, cover letter, referral package, interview-defense guide, or application package.

## Candidate Identity and Positioning

- Jainali Mehta lives in Toronto, Ontario, Canada and is applying as a beginner/graduate candidate for Business Analyst, Data Analyst, reporting, BI, and operations-analytics work.
- She is entering the Canadian job market for the first time and has not studied or worked in Canada. State current residence separately from Australian and Indian education and employment.
- Her analyst foundation is Australian experience as a `Data Intern` at AYLA Solutions in 2025. Do not present her as an experienced or senior analyst.
- Earlier experience is `Support Executive` at Trans Globe Education in India, 2022--2023, and `Administrative Executive` at Arihant Investment in India, 2020--2021.
- Education must appear exactly as `Master of Business Analytics`, Edith Cowan University, Australia, 2023--2025, and `Integrated Master of Business Administration`, Atmiya University, India, 2018--2022.
- Her three published GitHub projects cover e-commerce, healthcare, and workforce analytics using PostgreSQL and SQL. AI-assisted analysis and Power BI dashboard planning are complete; interactive Power BI dashboards and `.pbix` files are not published.
- Jainali directly confirms genuine freelance work as a freelance developer, freelance architect, and freelance data engineer. Dates, engagements, tools, deliverables, and outcomes must come from `skills/tailor-jainali-resume/references/freelance-evidence.md` before being claimed.
- Read `skills/tailor-jainali-resume/references/jainali-profile.md` and `references/freelance-evidence.md` completely before drafting. Together they are the canonical candidate fact base.

## Non-Negotiable Accuracy

- Never invent freelance engagements, clients, outcomes, metrics, dates, tools, credentials, ownership, seniority, production status, team size, or dataset scale. Strong framing and relevant emphasis are allowed; changing the underlying fact is not.
- Never convert exposure, coursework, planning, adjacent knowledge, or a supporting contribution into hands-on production experience.
- Use narrower wording when evidence is ambiguous. Record unsupported requirements as gaps instead of smuggling them into skills or bullets.
- Describe AYLA Solutions as `Data Intern`, never Business Analyst Intern or another title.
- Never list Tableau or IBM SPSS Statistics unless Jainali explicitly supplies new verified evidence.
- Do not claim implemented or published Power BI dashboards until Jainali confirms that status.
- Do not add a phone number, Canadian work/education experience, work authorization, or language proficiency without verification.
- Include genuine freelance experience as a standalone role when the posting benefits from it and the evidence ledger contains a defensible date range plus relevant work details. Use `Independent Freelance Consultant` or a narrower confirmed function; never present portfolio projects as client work.

## Locked Format

- Treat `skills/tailor-jainali-resume/assets/resume-template.tex` and `assets/cover-letter-template.tex` as the structural source of truth.
- Use the Dhruv-inspired compact visual system adopted for Jainali: US Letter, 9.5-point resume, 11-point cover letter, two-row left/right identity header, compact small-caps ruled sections, bold evidence labels, and single-column ATS-readable text.
- Resume section order is locked: Skills, Experience, Projects, Education, Credentials. Keep Education and Credentials separate.
- Every Skills category must render on one visual line. If a row wraps, shorten it or split it into two distinct supported categories; never accept a continuation line.
- Cover letter uses the matching two-row header, rule, date, centered `RE:` subject, four to six evidence-led paragraphs, and plain-text signature name.
- Do not add columns, sidebars, icons, photos, charts, skill bars, essential header/footer content, or scanned text.
- Do not solve overflow by shrinking below 9.5 points, extreme margin changes, horizontal scaling, or collisions. Trim content in the documented order.
- Fill the page with relevant verified evidence and balanced spacing. Resolve excessive bottom whitespace using verified freelance work, relevant projects, coursework, credentials, or older evidence before adjusting permitted spacing. Never add fiction or repetition as filler.

## Job-Description Workflow

1. Read the full skill, canonical profile, freelance evidence ledger, quality rules, format specification, and complete job description.
2. Classify each important requirement as direct, adjacent, or unsupported evidence.
3. Choose three to five truthful fit themes and use them consistently across the resume and cover letter.
4. Create a new immutable folder under `applications/` with the supplied script; never overwrite an earlier application.
5. Tailor evidence selection, bullet labels, keyword ordering, project selection, and cover-letter narrative inside the locked structure.
6. Compile and resolve every automated failure and short-line warning.
7. Visually inspect the rendered resume and cover letter. Mark history `verified` only after both pages pass.

## Standard Invocation

Jainali may paste only a job description or link. Infer company, exact role, and location when available. Use `unknown-company` or `unknown-role` rather than blocking when they cannot be inferred.
