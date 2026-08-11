# Jainali Mehta Resume Agent

A reusable, truth-first resume system for generating tailored Business Analyst and Data Analyst application packages from job descriptions.

Each run creates an immutable application version containing:

- a single-page ATS-readable LaTeX resume and compiled PDF;
- a focused single-page LaTeX cover letter and compiled PDF;
- the source job description;
- job-to-profile match notes; and
- automated page-count, searchable-text, and line-wrap QA.

## Current Application Package

- [Resume PDF](output/pdf/20260811-scotiabank-workplace-operations-coordinator-sbn-v058-resume.pdf)
- [Cover Letter PDF](output/pdf/20260811-scotiabank-workplace-operations-coordinator-sbn-v058-cover-letter.pdf)
- [Editable LaTeX and QA package](applications/20260811-scotiabank-workplace-operations-coordinator-sbn-v058/)
- [Scotiabank Workplace Operations Coordinator interview preparation](applications/20260811-scotiabank-workplace-operations-coordinator-sbn-v058/interview-preparation.md)
- [Application history](applications/HISTORY.md)

## Truth and ATS Rules

The canonical profile is stored in [`skills/tailor-jainali-resume/references/jainali-profile.md`](skills/tailor-jainali-resume/references/jainali-profile.md). The workflow must not invent employment history, dates, credentials, tools, metrics, or project outcomes. The GST adoption research used Google Forms and Microsoft Excel, not IBM SPSS Statistics.

Published project titles are identity-locked as **E-Commerce Sales Analytics**, **Healthcare Patient & Hospital Analytics**, and **HR Analytics**. Tailoring may change their order or omit an irrelevant project, but it must never rename them.

The locked document system follows Jainali's supplied format: a 9.5-point, one-column US Letter resume using Latin Modern serif, compact rules and bullets, searchable text, and no icons, photos, sidebars, skill bars, or scanned content. Education and Credentials remain separate. The matching 11-point cover letter uses the same typography and two-row identity header.

## Create a New Application Version

Save the job description as a Markdown file, then run:

```bash
python3 skills/tailor-jainali-resume/scripts/new_application.py \
  --company "Company Name" \
  --role "Role Name" \
  --location "Toronto, ON" \
  --job-description /path/to/job-description.md
```

The command prints the newly created immutable folder under `applications/`.

## Build and Validate

```bash
python3 skills/tailor-jainali-resume/scripts/build_application.py \
  applications/<version-folder>
```

The build requires Python 3, [Tectonic](https://tectonic-typesetting.github.io/), and Poppler utilities (`pdfinfo`, `pdftotext`, and `pdftoppm`). It compiles both LaTeX documents, requires exactly one page each, verifies searchable text, checks unsupported Tableau claims and short wrapped fragments, renders QA images, and copies final PDFs to `output/pdf/`.

## Repository Structure

```text
applications/                         Immutable application packages and history
output/pdf/                           Final compiled PDFs
skills/tailor-jainali-resume/         Reusable agent instructions, facts, templates, and scripts
```

## Portfolio Status

The three published analytics projects include completed PostgreSQL analysis, AI-assisted insights and recommendations, and Power BI dashboard planning. Interactive Power BI dashboard artifacts should not be described as published until that final stage is complete.

## Privacy

This is a public personal portfolio repository. It intentionally contains Jainali Mehta's professional contact information and immutable application versions created from this clean baseline. Do not add private phone numbers, employer-confidential data, API credentials, or unredacted third-party documents.
