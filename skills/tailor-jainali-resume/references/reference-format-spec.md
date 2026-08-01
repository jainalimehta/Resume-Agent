# Locked Resume and Cover-Letter Format

The user-supplied LaTeX in Codex attachment `7d512484-66d1-4a59-9772-09e1c09f05ed/pasted-text.txt` is the canonical structural source. The reusable implementation is stored in `../assets/resume-template.tex` and `../assets/cover-letter-template.tex`.

## Resume Contract

- `letterpaper`, 10-point `article`.
- Geometry: left/right `0.52in`, top/bottom `0.42in`.
- T1-encoded Latin Modern serif. Under Tectonic/XeTeX, zero-width inter-character breaks suppress common ligatures for reliable ATS extraction without changing the supplied template's visual typography.
- Black `ink` colour (`#111111`).
- Centered 17-point name and compact one-line contact details.
- Bold small-caps section headings with thin rules.
- `tabularx` employer/project rows with right-aligned location, date, or technology labels.
- Compact standard bullets with 0.16-inch left margin.
- One column, no icons, photo, sidebar, chart, skill bar, footer, or decorative graphic.
- Section order is locked: Professional Summary, Core Competencies, Professional Experience, Business Analytics Projects, Education, Credentials.

## Cover-Letter Contract

- Match the resume's 10-point Latin Modern serif typography, black colour, and centered contact header.
- Use US Letter with compact but readable margins.
- Include a thin rule beneath the contact header.
- Follow date, recipient, salutation, evidence paragraphs, motivation, direct close, and signature-name structure.
- Keep the letter to one page and approximately 300-425 words.

## Allowed Tailoring

- Job-specific summary and competency ordering.
- Wording and ordering of verified responsibilities.
- Selection and emphasis of verified projects and coursework.
- Job-description terminology supported by verified facts.
- Company-specific cover-letter motivation.

## Prohibited Changes

- Redesigning the document or substituting a different template.
- Changing typeface, colour, margins, document class, header structure, section styling, or list geometry merely to fit content.
- Adding columns, graphics, icons, ratings, sidebars, photos, text boxes, headers, or footers.
- Shrinking text before rewriting content.
- Copying facts or prose from any third-party formatting reference.
