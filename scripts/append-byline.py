#!/usr/bin/env python3
"""Append an author byline to every rendered HTML page just before </main>.

Runs as a Quarto post-render hook. We use this rather than a Pandoc Lua filter
because Quarto's listing component is inserted after Pandoc filters run, which
would push a filter-appended byline above the article list on the homepage.
Operating on the final HTML lets us put the byline after everything else.
"""
import os
from pathlib import Path

NAME = "Eric Laurence"
URL_LABEL = "eric-laurence.github.io/notes"
URL = "https://eric-laurence.github.io/notes"
UUID = "979af0cf-9d1e-4435-bfc4-8cb8a4cf8c7b"

BYLINE = (
    '<div class="page-byline"><p>'
    f'{NAME} · '
    f'<a href="{URL}">{URL_LABEL}</a> · '
    f'{UUID}'
    '</p></div>'
)

output_dir = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "_site"))

for html_file in output_dir.rglob("*.html"):
    content = html_file.read_text(encoding="utf-8")
    if "page-byline" in content:
        continue
    if "</main>" not in content:
        continue
    new_content = content.replace("</main>", BYLINE + "</main>", 1)
    html_file.write_text(new_content, encoding="utf-8")
