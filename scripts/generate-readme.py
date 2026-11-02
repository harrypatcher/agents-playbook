#!/usr/bin/env python3
"""Regenerate the contents section of README.md from skills, commands, and snippets.

Only the text between the BEGIN/END markers is replaced, so the rest of README.md stays hand-written.
Uses the standard library only, so the GitHub-hosted runner needs no setup step.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
BEGIN_MARKER = "<!-- BEGIN GENERATED CONTENTS -->"
END_MARKER = "<!-- END GENERATED CONTENTS -->"
QUOTES = "'\""


def frontmatter(path: Path) -> dict[str, str]:
    """Return top-level `key: value` pairs from the leading `---` block."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise SystemExit(f"{path.relative_to(ROOT)}: missing frontmatter")
    fields: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        key, sep, value = line.partition(":")
        if sep and not line.startswith((" ", "\t")):
            value = value.strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in QUOTES:
                value = value[1:-1]
            fields[key.strip()] = value
    raise SystemExit(f"{path.relative_to(ROOT)}: unterminated frontmatter")


def required(path: Path, fields: dict[str, str], key: str) -> str:
    value = fields.get(key, "").strip()
    if not value:
        raise SystemExit(f"{path.relative_to(ROOT)}: missing frontmatter field {key!r}")
    return value


def first_heading(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("#"):
            return line.lstrip("#").strip()
    raise SystemExit(f"{path.relative_to(ROOT)}: missing heading")


def sentence_case(text: str) -> str:
    # Source descriptions keep their own wording; only the first letter is normalized for a consistent list.
    return f"{text[:1].upper()}{text[1:]}"


def skill_rows() -> list[tuple[str, str]]:
    rows = []
    for path in sorted((ROOT / "skills").glob("*/SKILL.md")):
        fields = frontmatter(path)
        name = required(path, fields, "name")
        if name != path.parent.name:
            raise SystemExit(f"{path.relative_to(ROOT)}: name {name!r} differs from directory")
        rows.append((name, required(path, fields, "description")))
    return rows


def command_rows() -> list[tuple[str, str]]:
    rows = []
    for path in sorted((ROOT / "commands").glob("*.md")):
        if path.name == "README.md":
            continue
        description = required(path, frontmatter(path), "description")
        rows.append((f"/{path.stem}", description))
    return rows


def snippet_rows() -> list[tuple[str, str]]:
    return [
        (path.stem, first_heading(path))
        for path in sorted((ROOT / "snippets").glob("snippet-*.md"))
    ]


def contents() -> str:
    sections = [
        ("skills/", "loaded when a task matches the description", skill_rows()),
        ("commands/", "invoked as slash commands", command_rows()),
        ("snippets/", "pasted into global agent instructions", snippet_rows()),
    ]
    width = max(len(name) for _, _, rows in sections for name, _ in rows) + 2
    lines = ["## Contents", "", "```text"]
    for directory, purpose, rows in sections:
        lines.append(f"{directory:<{width + 2}}# {purpose}")
        lines += [f"  {name:<{width}}{sentence_case(description)}" for name, description in rows]
    lines.append("```")
    return "\n".join(lines)


def main() -> None:
    text = README.read_text(encoding="utf-8")
    head, begin, rest = text.partition(BEGIN_MARKER)
    _, end, tail = rest.partition(END_MARKER)
    if not begin or not end:
        raise SystemExit(f"README.md: missing {BEGIN_MARKER} or {END_MARKER}")
    README.write_text(f"{head}{BEGIN_MARKER}\n{contents()}\n{END_MARKER}{tail}", encoding="utf-8")


if __name__ == "__main__":
    main()
