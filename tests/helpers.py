"""Shared paths and parsing helpers for the test suite."""

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
CHAPTERS = SRC / "chapters"


def read_chapter(cid):
    return (CHAPTERS / f"{cid}.html").read_text(encoding="utf-8")


def code_blocks(text):
    """Yield (caption, code) for every <div class="code"> block, with tags removed and entities decoded."""
    for match in re.finditer(r'<div class="code">(.*?)</div>', text, re.S):
        inner = match.group(1)
        cap = re.search(r'<span class="cap">(.*?)</span>', inner, re.S)
        caption = html.unescape(re.sub(r"<[^>]+>", "", cap.group(1))).strip() if cap else ""
        pre = re.search(r"<pre>(.*?)</pre>", inner, re.S)
        if pre:
            yield caption, html.unescape(re.sub(r"<[^>]+>", "", pre.group(1)))
