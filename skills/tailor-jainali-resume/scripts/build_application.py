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
}


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
        run([command("tectonic"), "--keep-logs", "--outdir", str(app), str(source)], cwd=app)
        pdf = app / f"{stem}.pdf"
        if page_count(pdf) != 1:
            failures.append(f"{pdf.name}: must contain exactly one page")
        text_path = qa / f"{stem}.txt"
        run([command("pdftotext"), "-layout", str(pdf), str(text_path)])
        extracted = text_path.read_text(encoding="utf-8", errors="replace")
        if len(re.sub(r"\s+", "", extracted)) < 300:
            failures.append(f"{pdf.name}: insufficient searchable text")
        if re.search(r"[\ufb00-\ufb06]", extracted):
            failures.append(f"{pdf.name}: compatibility ligatures found")
        if re.search(r"\bTableau\b", extracted, re.IGNORECASE):
            failures.append(f"{pdf.name}: prohibited unsupported Tableau claim found")
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
