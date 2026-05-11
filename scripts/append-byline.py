#!/usr/bin/env python3
"""Append byline + post navigation to every rendered post.

Runs as a Quarto post-render hook. The byline (avatar, author, bio, personal
icon links) goes inside <main>. Below it, a nav row with prev/next/all-posts
links. Chronological order comes from the post frontmatter dates; a
`featured-next: <slug>` frontmatter key overrides the chronological next.
"""
import os
import re
from pathlib import Path

NAME = "Eric Laurence"
INITIALS = "EL"
BIO = "writing up notes on math."
UUID = "979af0cf-9d1e-4435-bfc4-8cb8a4cf8c7b"

LINKS = [
    ("bi-github", "https://github.com/Eric-Laurence", "GitHub"),
    # Add more like ("bi-mastodon", "https://...", "Mastodon"),
]

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
KV_RE = re.compile(r"^([\w-]+)\s*:\s*(.*)$")


def parse_frontmatter(qmd_text):
    """Tiny key:value YAML reader for post frontmatter; ignores nested blocks."""
    m = FRONTMATTER_RE.match(qmd_text)
    if not m:
        return {}
    result = {}
    for line in m.group(1).splitlines():
        if not line or line.startswith((" ", "\t", "-", "#")):
            continue
        m2 = KV_RE.match(line.strip())
        if m2:
            result[m2.group(1)] = m2.group(2).strip().strip('"').strip("'")
    return result


project_root = Path(__file__).resolve().parent.parent
posts_dir = project_root / "posts"

posts = []
for qmd in sorted(posts_dir.glob("*/index.qmd")):
    fm = parse_frontmatter(qmd.read_text(encoding="utf-8"))
    posts.append(
        {
            "slug": qmd.parent.name,
            "title": fm.get("title", qmd.parent.name),
            "date": fm.get("date", ""),
            "featured_next": fm.get("featured-next"),
        }
    )

# Newest first
posts.sort(key=lambda p: p["date"], reverse=True)
by_slug = {p["slug"]: p for p in posts}


def nav_for(slug):
    p = by_slug.get(slug)
    if not p:
        return None, None
    idx = posts.index(p)
    prv = posts[idx + 1] if idx + 1 < len(posts) else None
    featured = p.get("featured_next")
    if featured and featured in by_slug:
        nxt = by_slug[featured]
    else:
        nxt = posts[idx - 1] if idx > 0 else None
    return prv, nxt


links_html = "".join(
    f'<a href="{url}" aria-label="{label}" title="{label}">'
    f'<i class="bi {icon}"></i></a>'
    for icon, url, label in LINKS
)


def byline_html(slug):
    prv, nxt = nav_for(slug)
    nav_parts = []
    if prv:
        nav_parts.append(
            f'<a class="page-nav-prev" href="../{prv["slug"]}/">'
            f'<i class="bi bi-arrow-left"></i><span>{prv["title"]}</span></a>'
        )
    else:
        nav_parts.append('<span class="page-nav-placeholder"></span>')
    nav_parts.append('<a class="page-nav-all" href="../../">All posts</a>')
    if nxt:
        nav_parts.append(
            f'<a class="page-nav-next" href="../{nxt["slug"]}/">'
            f'<span>{nxt["title"]}</span><i class="bi bi-arrow-right"></i></a>'
        )
    else:
        nav_parts.append('<span class="page-nav-placeholder"></span>')

    return (
        '<div class="page-byline">'
        f'<div class="page-byline-avatar">{INITIALS}</div>'
        '<div class="page-byline-text">'
        f'Written by <strong>{NAME}</strong>, {BIO}'
        "</div>"
        f'<div class="page-byline-links">{links_html}</div>'
        "</div>"
        '<nav class="page-nav">' + "".join(nav_parts) + "</nav>"
        f'<div class="page-uuid">{UUID}</div>'
    )


output_dir = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "_site"))

for html_file in output_dir.glob("posts/*/index.html"):
    content = html_file.read_text(encoding="utf-8")
    if '<div class="page-byline"' in content:
        continue
    if "</main>" not in content:
        continue
    slug = html_file.parent.name
    new_content = content.replace("</main>", byline_html(slug) + "</main>", 1)
    html_file.write_text(new_content, encoding="utf-8")
