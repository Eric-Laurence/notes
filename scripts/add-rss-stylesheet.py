#!/usr/bin/env python3
"""Inject an XSL stylesheet processing instruction into the rendered RSS feed.

Run as a Quarto post-render script. Quarto generates the feed without a
stylesheet reference, so without this the file shows as raw XML in browsers.
"""
import os
import sys
from pathlib import Path

PI = '<?xml-stylesheet type="text/xsl" href="rss-style.xsl"?>'

output_dir = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "_site"))
feed = output_dir / "index.xml"

if not feed.exists():
    sys.exit(0)

content = feed.read_text(encoding="utf-8")

if "xml-stylesheet" in content:
    sys.exit(0)

if content.startswith("<?xml"):
    decl_end = content.find("?>") + 2
    new_content = content[:decl_end] + "\n" + PI + content[decl_end:]
else:
    new_content = PI + "\n" + content

feed.write_text(new_content, encoding="utf-8")
