---
name: tailor-jainali-resume
description: Create truthful, ATS-compatible, single-page LaTeX resumes and tailored cover letters for Jainali Mehta from pasted job descriptions, compile them to PDF, validate layout and text extraction, and preserve immutable application history. Use for Business Analyst, Data Analyst, reporting, operations analytics, and related entry-level applications in Toronto or elsewhere in Canada.
---

# Tailor Jainali Resume

Build a complete, versioned application package from Jainali's verified profile and the supplied job description.

## Load the Sources

1. Read `references/jainali-profile.md` completely.
2. Read `references/quality-rules.md` completely.
3. Preserve the job description verbatim in the new application folder.
4. Treat direct corrections from Jainali as authoritative and update the canonical profile when appropriate.

## Analyze the Job

1. Extract responsibilities, required tools, business domain, and behavioural requirements.
2. Map every selected keyword to a verified profile fact.
3. Exclude unsupported requirements rather than implying experience.
4. Choose projects by role:
   - Data or SQL-heavy: prioritize the PostgreSQL GitHub projects.
   - BI or reporting-heavy: include the Power BI Sales Performance Dashboard.
   - Business Analyst-heavy: prioritize requirements, process, stakeholder, Bank of Baroda, or GST research evidence.

## Create an Immutable Version

Run from the repository root:

```bash
python3 skills/tailor-jainali-resume/scripts/new_application.py \
  --company "Company" --role "Role" --job-description /path/to/job-description.md
```

Edit only the newly printed folder. Never overwrite an earlier application.

## Tailor the Documents

- Edit `resume.tex`, `cover-letter.tex`, and `match-notes.md`.
- Keep the resume and cover letter to exactly one page each.
- Keep Education and Credentials separate.
- Use `Data Intern` for AYLA Solutions.
- Do not list Tableau.
- Use conventional capitalization and ASCII hyphens.
- Do not fabricate quantitative outcomes.

## Build and Verify

Run:

```bash
python3 skills/tailor-jainali-resume/scripts/build_application.py applications/<version-folder>
```

Resolve every failure and short-line warning. Inspect `qa/resume.png` and `qa/cover-letter.png`. Rebuild after every material edit.

## Finish

- Mark the application `verified` in `applications/HISTORY.md`.
- Commit the immutable version when Git is available.
- Return the final PDFs, LaTeX sources, job description, and match notes.

