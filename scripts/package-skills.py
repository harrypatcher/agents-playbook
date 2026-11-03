#!/usr/bin/env python3
"""Bundle every skill and command as a flat Markdown file into one release archive.

Claude treats skills and commands alike, so the release ships `release-skills.zip` with a single `release-skills/`
folder holding one `<name>.md` per skill and command; users extract once and add each file in Claude individually.
Flat files cannot carry supporting files, so a skill with anything beside SKILL.md is rejected instead of truncated.
Uses the standard library only, so the GitHub-hosted runner needs no setup step.
"""

import re
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
COMMANDS_DIR = ROOT / "commands"
DIST_DIR = ROOT / "dist"
RELEASE_NAME = "release-skills"
SKILL_FILE = "SKILL.md"
FORMAT_DOC = "README.md"
QUOTES = "'\""

# Limits from https://support.claude.com/en/articles/12512198-how-to-create-custom-skills
# The claude.ai article caps descriptions at 200 characters, stricter than the 1,024 of the API docs.
NAME_PATTERN = re.compile(r"^[a-z0-9-]{1,64}$")
RESERVED_WORDS = ("anthropic", "claude")
DESCRIPTION_MAX_CHARS = 200
XML_TAG_PATTERN = re.compile(r"<[^>]+>")

# A fixed timestamp keeps archives byte-identical across runs with unchanged sources.
ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)


def frontmatter(path: Path) -> dict[str, str]:
    """Return top-level `key: value` pairs from the leading `---` block."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise SystemExit(f"{path.relative_to(ROOT)}: missing frontmatter")
    fields: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        if ":" in line and not line.startswith((" ", "\t")):
            key, value = line.split(":", 1)
            value = value.strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in QUOTES:
                value = value[1:-1]
            fields[key.strip()] = value
    raise SystemExit(f"{path.relative_to(ROOT)}: unterminated frontmatter")


def validate(path: Path, name: str, description: str) -> None:
    """Reject entries that the Claude skill upload would refuse."""
    where = path.relative_to(ROOT)
    if not NAME_PATTERN.fullmatch(name):
        raise SystemExit(f"{where}: name must be 1-64 lowercase letters, digits, or hyphens")
    if any(word in name for word in RESERVED_WORDS):
        raise SystemExit(f"{where}: name contains a reserved word {RESERVED_WORDS}")
    if not description or len(description) > DESCRIPTION_MAX_CHARS:
        raise SystemExit(f"{where}: description has {len(description)} characters, allowed 1-{DESCRIPTION_MAX_CHARS}")
    if XML_TAG_PATTERN.search(name) or XML_TAG_PATTERN.search(description):
        raise SystemExit(f"{where}: name and description must not contain XML tags")


def skill_entry(skill_dir: Path) -> tuple[str, bytes]:
    skill_file = skill_dir / SKILL_FILE
    if not skill_file.is_file():
        raise SystemExit(f"{skill_dir.relative_to(ROOT)}: missing {SKILL_FILE}")
    extra = sorted(p.relative_to(skill_dir).as_posix() for p in skill_dir.rglob("*") if p.is_file() and p != skill_file)
    if extra:
        raise SystemExit(f"{skill_dir.relative_to(ROOT)}: supporting files cannot ship as flat Markdown: {extra}")
    fields = frontmatter(skill_file)
    name = fields.get("name", "")
    if name != skill_dir.name:
        raise SystemExit(f"{skill_file.relative_to(ROOT)}: name {name!r} differs from directory")
    validate(skill_file, name, fields.get("description", ""))
    return name, skill_file.read_bytes()


def command_entry(command_file: Path) -> tuple[str, bytes]:
    # Command sources derive their name from the filename, but an uploaded skill needs `name` in its frontmatter.
    fields = frontmatter(command_file)
    name = command_file.stem
    if "name" in fields:
        raise SystemExit(f"{command_file.relative_to(ROOT)}: commands take their name from the filename")
    validate(command_file, name, fields.get("description", ""))
    text = command_file.read_text(encoding="utf-8")
    return name, text.replace("---\n", f"---\nname: {name}\n", 1).encode("utf-8")


def main() -> None:
    entries = [skill_entry(p) for p in sorted(SKILLS_DIR.iterdir()) if p.is_dir()]
    entries += [command_entry(p) for p in sorted(COMMANDS_DIR.glob("*.md")) if p.name != FORMAT_DOC]
    if not entries:
        raise SystemExit("skills/, commands/: nothing to package")
    names = [name for name, _ in entries]
    duplicates = sorted({name for name in names if names.count(name) > 1})
    if duplicates:
        raise SystemExit(f"duplicate names across skills and commands: {duplicates}")

    shutil.rmtree(DIST_DIR, ignore_errors=True)
    DIST_DIR.mkdir()
    bundle = DIST_DIR / f"{RELEASE_NAME}.zip"
    with zipfile.ZipFile(bundle, "w", zipfile.ZIP_DEFLATED) as zf:
        for name, content in entries:
            info = zipfile.ZipInfo(f"{RELEASE_NAME}/{name}.md", ZIP_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, content)
            print(f"packaged  {name}")
    print(f"bundle    {bundle.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
