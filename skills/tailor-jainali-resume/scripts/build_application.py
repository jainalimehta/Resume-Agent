#!/usr/bin/env python3
"""Compile and validate one-page ATS application PDFs."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path


RUNTIME_BIN = Path.home() / ".cache" / "codex-runtimes" / "codex-primary-runtime" / "dependencies" / "bin" / "override"
ALLOWED_SHORT = {
    "sincerely,", "best regards,", "jainali mehta", "dear hiring manager,", "hiring manager",
    "general application", "toronto, on", "thank you for your consideration.",
    "hr analytics", "credentials", "education", "experience", "profile", "projects", "selected projects", "professional experience",
    "professional summary", "technical and business skills",
    "core competencies", "master baseline", "prospective employer", "skills",
}
REQUIRED_RESUME_SECTIONS = ("Skills", "Experience", "Projects", "Education", "Credentials")


def command(name: str) -> str:
    found = shutil.which(name)
    if found:
        return found
    bundled = RUNTIME_BIN / name
    if bundled.exists():
        return str(bundled)
    raise SystemExit(f"Required command not found: {name}")


def run(args: list[str], cwd: Path | None = None) -> str:
    result = subprocess.run(args, cwd=cwd, text=True, capture_output=True)
    if result.returncode:
        sys.stderr.write(result.stdout + result.stderr)
        raise SystemExit(result.returncode)
    return result.stdout


def page_count(pdf: Path) -> int:
    info = run([command("pdfinfo"), str(pdf)])
    match = re.search(r"^Pages:\s+(\d+)", info, re.MULTILINE)
    if not match:
        raise SystemExit(f"Could not read page count: {pdf}")
    return int(match.group(1))


def source_contract_failures(stem: str, source_text: str) -> list[str]:
    failures: list[str] = []
    unresolved = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", source_text)))
    if unresolved:
        failures.append(f"{stem}.tex: unresolved placeholders: {', '.join(unresolved)}")
    expected_class = "9.5pt" if stem == "resume" else "11pt"
    class_pattern = rf"\\documentclass\[letterpaper,{re.escape(expected_class)}\]\{{article\}}"
    if not re.search(class_pattern, source_text):
        failures.append(f"{stem}.tex: locked letterpaper/{expected_class} document class missing")
    if r"\begin{tabular*}{\textwidth}" not in source_text:
        failures.append(f"{stem}.tex: locked two-row tabular header missing")
    if stem == "resume":
        positions = [source_text.find(rf"\section{{{section}}}") for section in REQUIRED_RESUME_SECTIONS]
        if any(position < 0 for position in positions) or positions != sorted(positions):
            failures.append("resume.tex: locked section order must be Skills, Experience, Projects, Education, Credentials")
    return failures


def font_embedding_failures(pdf: Path) -> list[str]:
    output = run([command("pdffonts"), str(pdf)])
    failures: list[str] = []
    font_rows = [line for line in output.splitlines()[2:] if line.strip()]
    if not font_rows:
        return [f"{pdf.name}: no fonts reported"]
    for row in font_rows:
        flags = re.search(r"\s+(yes|no)\s+(yes|no)\s+(yes|no)\s+\d+\s+\d+\s*$", row)
        if not flags or flags.group(1) != "yes":
            failures.append(f"{pdf.name}: unembedded or unreadable font row: {row.strip()}")
    return failures


def reading_order_failures(stem: str, extracted: str) -> list[str]:
    positions = [extracted.find("Jainali Mehta"), extracted.find("jainali2000@gmail.com")]
    if stem == "resume":
        for section in REQUIRED_RESUME_SECTIONS:
            match = re.search(rf"(?m)^{re.escape(section)}\s*$", extracted)
            positions.append(match.start() if match else -1)
    if any(position < 0 for position in positions) or positions != sorted(positions):
        return [f"{stem}.pdf: header-first reading order or locked section order failed"]
    return []


def skills_layout_failures(source_text: str, extracted: str) -> list[str]:
    """Require every source Skills item to occupy exactly one extracted line."""
    source_start = source_text.find(r"\section{Skills}")
    source_end = source_text.find(r"\section{Experience}")
    if source_start < 0 or source_end < 0 or source_end <= source_start:
        return ["resume.tex: could not inspect locked Skills section"]
    expected_rows = len(re.findall(r"\\item\[\]", source_text[source_start:source_end]))

    text_start = re.search(r"(?m)^Skills\s*$", extracted)
    text_end = re.search(r"(?m)^Experience\s*$", extracted)
    if not text_start or not text_end or text_end.start() <= text_start.end():
        return ["resume.pdf: could not inspect rendered Skills section"]
    rendered_rows = [
        line.strip()
        for line in extracted[text_start.end():text_end.start()].splitlines()
        if line.strip()
    ]
    if expected_rows != len(rendered_rows):
        return [
            "resume.pdf: every Skills category must render on one line "
            f"({expected_rows} source rows produced {len(rendered_rows)} visual lines)"
        ]
    return []


def resume_density_failures(pdf: Path, bbox_path: Path) -> list[str]:
    """Reject visibly underfilled resumes while leaving a safe bottom margin."""
    run([command("pdftotext"), "-bbox", str(pdf), str(bbox_path)])
    bbox = bbox_path.read_text(encoding="utf-8", errors="replace")
    bottoms = [float(value) for value in re.findall(r'yMax="([0-9.]+)"', bbox)]
    if not bottoms:
        return ["resume.pdf: could not measure page coverage"]
    content_bottom = max(bottoms)
    if content_bottom < 675:
        return [
            "resume.pdf: excessive bottom whitespace; add relevant verified evidence "
            f"or rebalance permitted spacing (content ends at y={content_bottom:.1f})"
        ]
    if content_bottom > 760:
        return [f"resume.pdf: content is too close to the page edge (y={content_bottom:.1f})"]
    return []


def short_line_warnings(text: str) -> list[str]:
    warnings: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        words = re.findall(r"[A-Za-z0-9][A-Za-z0-9&+./'-]*", line)
        if not words or len(words) > 2 or line.lower() in ALLOWED_SHORT or line.isupper():
            continue
        if "@" in line or "|" in line or re.search(r"\b(?:19|20)\d{2}\b", line):
            continue
        warnings.append(line)
    return warnings


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("application", type=Path)
    args = parser.parse_args()
    app = args.application.resolve()
    if not app.is_dir():
        raise SystemExit(f"Application folder not found: {app}")
    qa = app / "qa"
    qa.mkdir(exist_ok=True)
    failures: list[str] = []
    warnings: list[str] = []

    for stem in ("resume", "cover-letter"):
        source = app / f"{stem}.tex"
        source_text = source.read_text(encoding="utf-8")
        failures.extend(source_contract_failures(stem, source_text))
        run([command("tectonic"), "--keep-logs", "--outdir", str(app), str(source)], cwd=app)
        pdf = app / f"{stem}.pdf"
        if page_count(pdf) != 1:
            failures.append(f"{pdf.name}: must contain exactly one page")
        failures.extend(font_embedding_failures(pdf))
        text_path = qa / f"{stem}.txt"
        run([command("pdftotext"), "-layout", str(pdf), str(text_path)])
        extracted = text_path.read_text(encoding="utf-8", errors="replace")
        if len(re.sub(r"\s+", "", extracted)) < 300:
            failures.append(f"{pdf.name}: insufficient searchable text")
        if re.search(r"[\ufb00-\ufb06]", extracted):
            failures.append(f"{pdf.name}: compatibility ligatures found")
        failures.extend(reading_order_failures(stem, extracted))
        if stem == "resume":
            failures.extend(skills_layout_failures(source_text, extracted))
            failures.extend(resume_density_failures(pdf, qa / "resume-bbox.html"))
        if re.search(r"\bTableau\b", extracted, re.IGNORECASE):
            failures.append(f"{pdf.name}: prohibited unsupported Tableau claim found")
        if re.search(r"\b(?:IBM\s+)?SPSS(?:\s+Statistics)?\b", extracted, re.IGNORECASE):
            failures.append(f"{pdf.name}: prohibited unsupported IBM SPSS Statistics claim found")
        if re.search(r"\b(?:Business Analyst|Data Analyst|Analytics Engineer) Intern\b", extracted, re.IGNORECASE):
            failures.append(f"{pdf.name}: prohibited altered AYLA internship title found")
        if re.search(r"(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}", extracted):
            failures.append(f"{pdf.name}: unverified phone number found")
        prohibited_project_aliases = (
            "E-Commerce Sales & Customer Analytics",
            "Healthcare Operations Analytics",
            "Workforce & Employee Analytics",
        )
        for alias in prohibited_project_aliases:
            if alias.lower() in extracted.lower():
                failures.append(f"{pdf.name}: prohibited renamed project title found: {alias}")
        warnings.extend(f"{stem}: {line}" for line in short_line_warnings(extracted))
        run([command("pdftoppm"), "-png", "-r", "150", "-f", "1", "-singlefile", str(pdf), str(qa / stem)])

    report = ["# Build QA", ""]
    report.append("- Page count: PASS" if not failures else "- Page count or ATS checks: FAIL")
    report.append(f"- Short-line warnings: {len(warnings)}")
    if warnings:
        report.extend(["", "## Short-Line Warnings", ""] + [f"- `{item}`" for item in warnings])
    if failures:
        report.extend(["", "## Failures", ""] + [f"- {item}" for item in failures])
    (qa / "report.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print("\n".join(report))
    if failures or warnings:
        raise SystemExit(1)

    final_dir = app.parents[1] / "output" / "pdf"
    final_dir.mkdir(parents=True, exist_ok=True)
    for stem in ("resume", "cover-letter"):
        shutil.copy2(app / f"{stem}.pdf", final_dir / f"{app.name}-{stem}.pdf")


if __name__ == "__main__":
    main()
