#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
ARCHIVE_TEMPLATE = ROOT / "_includes" / "archive-single.html"
PUBLICATIONS_DIR = ROOT / "_publications"


FRONT_MATTER_PATTERN = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
KEY_VALUE_PATTERN = re.compile(r'^([A-Za-z0-9_]+):\s*(.*)\s*$')


def parse_front_matter(path: Path) -> dict[str, str]:
    content = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_PATTERN.match(content)
    if not match:
        raise ValueError(f"Missing front matter in {path}")

    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        parsed = KEY_VALUE_PATTERN.match(line)
        if parsed:
            value = parsed.group(2).strip()
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            data[parsed.group(1)] = value
    return data


def main() -> int:
    template = ARCHIVE_TEMPLATE.read_text(encoding="utf-8")
    failures: list[str] = []

    if '{% if post.collection == \'publications\' %}' not in template:
        failures.append("Missing publications-specific title and button logic.")

    publication_title_snippet = "{% if post.collection == 'publications' %}\n        {{ title }}"
    if publication_title_snippet not in template:
        failures.append("Publication titles should render as plain text in the publications branch.")

    required_snippets = [
        '{% assign publication_url = base_path | append: post.url %}',
        '{% if post.paperurl and post.paperurl != "" %}',
        '>PDF</a>',
        '>Blog</a>',
        'class="btn btn--small"',
    ]
    for snippet in required_snippets:
        if snippet not in template:
            failures.append(f"Missing template snippet: {snippet}")

    publication_files = sorted(PUBLICATIONS_DIR.glob("*.md"))
    if not publication_files:
        failures.append("No publication markdown files found.")

    blog_count = 0
    pdf_count = 0
    missing_permalink: list[str] = []

    for path in publication_files:
        front_matter = parse_front_matter(path)
        if not front_matter.get("permalink"):
            missing_permalink.append(path.name)
        else:
            blog_count += 1

        if front_matter.get("paperurl"):
            pdf_count += 1

    if missing_permalink:
        failures.append(
            "Missing permalink for publication files: " + ", ".join(missing_permalink)
        )

    if blog_count != len(publication_files):
        failures.append("Every publication should expose a Blog button target.")

    if pdf_count < 8:
        failures.append("Expected at least eight publication entries with PDF targets.")

    if failures:
        print("Publication button checks failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Publication button checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
