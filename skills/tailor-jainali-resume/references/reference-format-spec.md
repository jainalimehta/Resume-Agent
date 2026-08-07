# Locked Resume and Cover-Letter Format

The canonical visual system is adapted from the user-provided Dhruv Doshi LaTeX references in `agent/`. Jainali's reusable implementations are `../assets/resume-template.tex` and `../assets/cover-letter-template.tex`. Copy the layout system only; never copy Dhruv's candidate facts, claims, metrics, signature, or fabrication permissions.

## Resume Contract

- US Letter, single-column `article`, 9.5-point document option.
- Compact full-page geometry matching the reference layout; do not change it per application.
- T1-encoded Latin Modern/Computer Modern-style serif text with XeTeX ligature suppression for ATS extraction.
- Two-row `tabular*` identity header:
  - row 1: large bold name on the left, email on the right;
  - row 2: visible LinkedIn on the left, visible GitHub plus `Toronto, Ontario, Canada` on the right.
- Small-caps section headings with thin black rules and compact spacing.
- Description-style Skills rows with bold category labels and no rating graphics.
- Each Skills row must remain on one visual line. Divide a long category into two semantically distinct supported rows rather than allowing a wrap.
- Employer and education rows use `\resumeSubheading{Organization}{Location}{Title/Degree}{Date}`.
- Experience and project evidence uses `\resumeItem{Short Label}{Defensible evidence}` with bold labels and compact circular sub-bullets.
- Locked order: Skills, Experience, Projects, Education, Credentials.
- Education and Credentials always remain separate.
- No summary section by default; the skills-first top third carries role positioning in this format.

## Cover-Letter Contract

- US Letter, 11-point `article`, same compact serif visual family; the cover-letter top offset is slightly lower than the resume so the larger name row cannot clip.
- Matching two-row identity header followed by `\hrulefill`.
- Current date in `Month D, YYYY` format.
- Centered subject: `RE: Exact Role, Company`.
- Verified salutation or `Dear Hiring Manager,`.
- Four to six evidence-led paragraphs separated with `\bigbreak`, normally 300--425 words.
- Plain `Best regards,` close followed by `Jainali Mehta`; no signature image unless Jainali provides and requests one.

## Allowed Tailoring

- Skill-row ordering and supported terminology.
- Bullet labels, evidence selection, and ordering within an employer.
- Selection and ordering of verified projects, coursework, and optional credentials.
- Supported job-description terminology and company-specific cover-letter content.
- Removal of low-priority content using the documented one-page budget.
- Selective inclusion of a genuine freelance role when its date range and bullets are supported by `freelance-evidence.md`.

## Prohibited Changes

- Changing the document class, font size, margins, header structure, section style, command definitions, or section order for one application.
- Adding a centered identity header, summary-first layout, columns, graphics, icons, ratings, sidebars, photos, text boxes, essential PDF headers/footers, or scanned text.
- Shrinking below 9.5 points, horizontal scaling, or collision-causing negative spacing.
- Copying Dhruv's content, signature, personal details, claims, metrics, or candidate-specific instructions.
- Inventing experience or projects to fill a job-description gap.
- Leaving excessive unused page space when additional relevant verified evidence is available.
