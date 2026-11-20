#!/usr/bin/env python3
"""Minimal dependency-free structural check for this repository's skill.

This intentionally checks only the conventions used here; it is not a YAML
parser or a replacement for the Agent Skills reference validator.
"""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "test-integrity"
SKILL_FILE = SKILL_DIR / "SKILL.md"
NAME_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


def check() -> list[str]:
    errors = []
    if not SKILL_FILE.is_file():
        return [f"Missing required file: {SKILL_FILE}"]

    lines = SKILL_FILE.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        return ["SKILL.md must begin with YAML frontmatter (---)."]
    try:
        end = lines.index("---", 1)
    except ValueError:
        return ["SKILL.md is missing the closing YAML frontmatter marker."]

    # This repo deliberately uses simple, single-line frontmatter values.
    fields: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            errors.append(f"Unsupported frontmatter entry: {line!r}")
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip().strip("\"'")
        if not key or not value or key in fields:
            errors.append(f"Invalid or repeated frontmatter field: {key!r}")
        else:
            fields[key] = value

    name = fields.get("name", "")
    description = fields.get("description", "")
    if not NAME_PATTERN.fullmatch(name) or len(name) > 64:
        errors.append("name must be lowercase kebab-case, max 64 characters.")
    if name != SKILL_DIR.name:
        errors.append("name must match the enclosing skill directory.")
    if not 1 <= len(description) <= 1024:
        errors.append("description must be 1-1024 characters.")
    if not any(line.strip() for line in lines[end + 1 :]):
        errors.append("SKILL.md instructions are empty.")

    for target in re.findall(r"\]\((references/[^)#]+\.md)\)", "\n".join(lines)):
        if not (SKILL_DIR / target).is_file():
            errors.append(f"Missing reference: {target}")
    return errors


def main() -> int:
    errors = check()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("OK: skill structure and local references verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
