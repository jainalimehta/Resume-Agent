#!/usr/bin/env python3
"""Create a globally numbered, immutable application folder."""

from __future__ import annotations

import argparse
import datetime as dt
import fcntl
import os
import re
import shutil
from pathlib import Path


LATEX_ESCAPES = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}


def latex_escape(value: str) -> str:
    """Escape user- or job-derived text before inserting it into LaTeX."""
    return "".join(LATEX_ESCAPES.get(character, character) for character in value)


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "unknown"


def render_templates(skill: Path, replacements: dict[str, str]) -> dict[str, str]:
    """Render every application template and reject unresolved placeholders."""
    latex_replacements = {
        placeholder: latex_escape(value) for placeholder, value in replacements.items()
    }
    templates = {
        "resume-template.tex": "resume.tex",
        "cover-letter-template.tex": "cover-letter.tex",
        "match-notes-template.md": "match-notes.md",
    }
    rendered: dict[str, str] = {}
    for source_name, output_name in templates.items():
        text = (skill / "assets" / source_name).read_text(encoding="utf-8")
        selected = latex_replacements if output_name.endswith(".tex") else replacements
        for old, new in selected.items():
            text = text.replace(old, new)
        unresolved = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", text)))
        if unresolved:
            raise SystemExit(
                f"Unresolved placeholders in {source_name}: {', '.join(unresolved)}"
            )
        rendered[output_name] = text
    return rendered


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--company", required=True)
    parser.add_argument("--role", required=True)
    parser.add_argument("--location", default="Toronto, ON")
    parser.add_argument("--company-reason", default="the role connects careful analysis with practical business decisions")
    parser.add_argument("--job-description", type=Path, required=True)
    parser.add_argument("--date", default=dt.date.today().isoformat())
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()

    root = args.root.resolve()
    applications = root / "applications"
    skill = root / "skills" / "tailor-jainali-resume"
    job_description = args.job_description.resolve()
    if not job_description.is_file():
        raise SystemExit(f"Job description not found: {job_description}")
    applications.mkdir(parents=True, exist_ok=True)

    replacements = {
        "{{APPLICATION_DATE}}": dt.date.fromisoformat(args.date).strftime("%B %-d, %Y"),
        "{{COMPANY}}": args.company,
        "{{ROLE}}": args.role,
        "{{LOCATION}}": args.location,
        "{{COMPANY_REASON}}": args.company_reason,
    }
    history = applications / "HISTORY.md"
    with history.open("a+", encoding="utf-8") as stream:
        fcntl.flock(stream.fileno(), fcntl.LOCK_EX)
        existing = sorted(applications.glob("*-v[0-9][0-9][0-9]"))
        version_number = max([int(path.name[-3:]) for path in existing], default=0) + 1
        base = f"{args.date.replace('-', '')}-{slugify(args.company)}-{slugify(args.role)}"
        version = f"{base}-v{version_number:03d}"
        target = applications / version
        replacements["{{VERSION}}"] = version
        rendered = render_templates(skill, replacements)

        target.mkdir(exist_ok=False)
        for output_name, text in rendered.items():
            (target / output_name).write_text(text, encoding="utf-8")
        shutil.copy2(job_description, target / "job-description.md")

        row = f"| {version_number:03d} | {args.date} | {args.company} | {args.role} | [{version}](./{version}/) | draft |\n"
        stream.write(row)
        stream.flush()
        os.fsync(stream.fileno())
        fcntl.flock(stream.fileno(), fcntl.LOCK_UN)
    print(target)


if __name__ == "__main__":
    main()
