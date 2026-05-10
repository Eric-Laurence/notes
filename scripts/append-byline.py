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
INITIALS = "EL"
BIO = "writing up notes on math."
UUID = "979af0cf-9d1e-4435-bfc4-8cb8a4cf8c7b"

LINKS = [
    ("bi-github", "https://github.com/Eric-Laurence", "GitHub"),
    # Add more like ("bi-mastodon", "https://...", "Mastodon"),
    # ("bi-envelope-fill", "mailto:...", "Email"), etc.
]

links_html = "".join(
    f'<a href="{url}" aria-label="{label}" title="{label}">'
    f'<i class="bi {icon}"></i></a>'
    for icon, url, label in LINKS
)

BYLINE = (
    '<div class="page-byline">'
    f'<div class="page-byline-avatar">{INITIALS}</div>'
    '<div class="page-byline-text">'
    f'Written by <strong>{NAME}</strong>, {BIO}'
    '</div>'
    '</div>'
    f'<div class="page-links">{links_html}</div>'
    f'<div class="page-uuid">{UUID}</div>'
)

output_dir = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "_site"))

# Only target actual posts (posts/<slug>/index.html), not the listing or
# top-level pages like about.html.
for html_file in output_dir.glob("posts/*/index.html"):
    content = html_file.read_text(encoding="utf-8")
    if '<div class="page-byline"' in content:
        continue
    if "</main>" not in content:
        continue
    new_content = content.replace("</main>", BYLINE + "</main>", 1)
    html_file.write_text(new_content, encoding="utf-8")
