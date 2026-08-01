# Resume and Cover-Letter Quality Rules

## Truth and Relevance

- Tailor ordering and language without changing factual meaning.
- Use job-description terminology only when verified evidence supports it.
- Prefer evidence over adjectives and never invent metrics.
- Make the top third immediately communicate the target role, relevant tools, and strongest evidence.

## ATS Design

- Use US Letter, one column, standard section names, embedded searchable fonts, and black body text.
- Put contact details in the document body, not a PDF header or footer.
- Do not use icons, photos, graphics, rating bars, text boxes, or sidebars.
- Keep links visible and confirm `pdftotext` reading order.
- ATS is the correct acronym; do not call the document ATDS-supported.

## Page and Locked Typography

- Resume and cover letter must each be exactly one page.
- Resume must use the canonical 10-point LaTeX template with 0.52-inch side margins and 0.42-inch top/bottom margins.
- Keep the T1-encoded Latin Modern serif and suppress common ligatures under XeTeX so `pdftotext` produces ordinary character sequences for ATS parsing.
- Do not change the locked typeface, geometry, header, section rules, or list geometry to make content fit.
- Avoid empty visual rows and one- or two-word wrapped fragments.
- Rewrite content before reducing font size.
- Use consistent capitalization for employers, titles, technologies, sections, and project names.

## Locked Resume Structure

- Professional Summary
- Core Competencies
- Professional Experience
- Business Analytics Projects
- Education
- Credentials
- Keep Education and Credentials separate under all circumstances.

## Cover Letter

- Use a clean, non-overlapping letterhead.
- Target 300-425 words.
- Include employer-specific motivation when a real job description is supplied.
- Use two evidence paragraphs and a direct close; do not simply repeat the resume.

## Final QA

- Compile with Tectonic.
- Require exactly one page per PDF.
- Extract searchable text and reject compatibility ligatures.
- Resolve every short-line warning.
- Render both PDFs and visually inspect clipping, overlap, spacing, alignment, capitalization, and excessive whitespace.
