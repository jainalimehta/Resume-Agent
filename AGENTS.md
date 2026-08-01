# Jainali Mehta Resume Agent

Use the `tailor-jainali-resume` skill in `skills/tailor-jainali-resume/` whenever Jainali pastes a job description or asks for a resume, CV, cover letter, or application package.

## Non-Negotiable Requirements

- Treat `skills/tailor-jainali-resume/references/jainali-profile.md` as the canonical fact base.
- Never invent experience, outcomes, metrics, dates, tools, or credentials.
- Describe the AYLA Solutions internship as `Data Intern`, not Business Analyst Intern.
- Never list Tableau unless Jainali explicitly confirms new Tableau experience.
- Create an ATS-readable, single-page resume and single-page cover letter in LaTeX and PDF.
- Keep Education and Credentials as separate resume sections.
- Avoid columns, sidebars, icons, photos, charts, skill bars, headers/footers, and scanned text.
- Avoid wrapped lines whose final fragment contains only one or two words.
- Create a new immutable folder under `applications/` for every job description and update `applications/HISTORY.md`.
- Run automated QA and visually inspect both rendered pages before completion.

## Standard Invocation

Jainali may paste only a job description. Infer the company, role, and location when available. Use `unknown-company` or `unknown-role` rather than blocking when either cannot be inferred.

