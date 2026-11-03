#!/usr/bin/env python3
"""Package every skill as a claude.ai upload ZIP and bundle them into one release archive.

claude.ai accepts exactly one skill folder per uploaded ZIP, so each skill gets its own ZIP.
All skill ZIPs are then wrapped in `release-skills.zip` under a `release-skills/` folder,
so a release ships one download whose extracted files are dragged into the upload dialog one by one.
Uses the standard library only, so the GitHub-hosted runner needs no setup step.
"""

import re
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
DIST_DIR = ROOT / "dist"
RELEASE_NAME = "release-skills"
QUOTES = "'\""

# Upload limits from https://support.claude.com/en/articles/12512198-how-to-create-custom-skills
NAME_PATTERN = re.compile(r"^[a-z0-9-]{1,64}$")
RESERVED_WORDS = ("anthropic", "claude")
DESCRIPTION_MAX_CHARS = 1024
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


def validate(skill_dir: Path) -> None:
    """Reject skills that the claude.ai upload dialog would refuse."""
    skill_file = skill_dir / "SKILL.md"
    where = skill_file.relative_to(ROOT)
    if not skill_file.is_file():
        raise SystemExit(f"{skill_dir.relative_to(ROOT)}: missing SKILL.md")
    fields = frontmatter(skill_file)
    name = fields.get("name", "")
    description = fields.get("description", "")
    if name != skill_dir.name:
        raise SystemExit(f"{where}: name {name!r} differs from directory")
    if not NAME_PATTERN.fullmatch(name):
        raise SystemExit(f"{where}: name must be 1-64 lowercase letters, digits, or hyphens")
    if any(word in name for word in RESERVED_WORDS):
        raise SystemExit(f"{where}: name contains a reserved word {RESERVED_WORDS}")
    if not description or len(description) > DESCRIPTION_MAX_CHARS:
        raise SystemExit(f"{where}: description must be 1-{DESCRIPTION_MAX_CHARS} characters")
    if XML_TAG_PATTERN.search(name) or XML_TAG_PATTERN.search(description):
        raise SystemExit(f"{where}: name and description must not contain XML tags")


def write_zip(archive: Path, files: list[Path], base: Path) -> None:
    """Write files into a ZIP with paths relative to base and a fixed timestamp."""
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(files):
            info = zipfile.ZipInfo(path.relative_to(base).as_posix(), ZIP_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, path.read_bytes())


def main() -> None:
    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    if not skill_dirs:
        raise SystemExit("skills/: no skill directories found")
    for skill_dir in skill_dirs:
        validate(skill_dir)

    release_dir = DIST_DIR / RELEASE_NAME
    shutil.rmtree(DIST_DIR, ignore_errors=True)
    release_dir.mkdir(parents=True)

    # Each upload ZIP must contain the skill folder itself at the top level, not its loose files.
    for skill_dir in skill_dirs:
        files = [p for p in skill_dir.rglob("*") if p.is_file()]
        write_zip(release_dir / f"{skill_dir.name}.zip", files, SKILLS_DIR)

    bundle = DIST_DIR / f"{RELEASE_NAME}.zip"
    write_zip(bundle, list(release_dir.glob("*.zip")), DIST_DIR)
    for skill_dir in skill_dirs:
        print(f"packaged  {skill_dir.name}")
    print(f"bundle    {bundle.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
