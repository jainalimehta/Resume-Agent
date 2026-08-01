#!/usr/bin/env python3
"""Create a globally numbered, immutable application folder."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import shutil
from pathlib import Path


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "unknown"


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
    if not args.job_description.is_file():
        raise SystemExit(f"Job description not found: {args.job_description}")
    applications.mkdir(parents=True, exist_ok=True)

    existing = sorted(applications.glob("*-v[0-9][0-9][0-9]"))
    version_number = max([int(path.name[-3:]) for path in existing], default=0) + 1
    base = f"{args.date.replace('-', '')}-{slugify(args.company)}-{slugify(args.role)}"
    version = f"{base}-v{version_number:03d}"
    target = applications / version
    target.mkdir()

    replacements = {
        "{{APPLICATION_DATE}}": dt.date.fromisoformat(args.date).strftime("%B %-d, %Y"),
        "{{COMPANY}}": args.company,
        "{{ROLE}}": args.role,
        "{{LOCATION}}": args.location,
        "{{COMPANY_REASON}}": args.company_reason,
        "{{VERSION}}": version,
    }
    templates = {
        "resume-template.tex": "resume.tex",
        "cover-letter-template.tex": "cover-letter.tex",
        "match-notes-template.md": "match-notes.md",
    }
    for source_name, output_name in templates.items():
        text = (skill / "assets" / source_name).read_text(encoding="utf-8")
        for old, new in replacements.items():
            text = text.replace(old, new)
        (target / output_name).write_text(text, encoding="utf-8")
    shutil.copy2(args.job_description, target / "job-description.md")

    history = applications / "HISTORY.md"
    row = f"| {version_number:03d} | {args.date} | {args.company} | {args.role} | [{version}](./{version}/) | draft |\n"
    with history.open("a", encoding="utf-8") as stream:
        stream.write(row)
    print(target)


if __name__ == "__main__":
    main()

