#!/usr/bin/env python3
"""Build AI & Claude Mastery into one self-contained page, then audit it.

Sources:
  src/curriculum.json      parts and chapters (id, title, level, reading and practice minutes) and author details
  src/glossary.json        {"Term": {"d": "definition", "see": "ch14"}}, plus extra terms in src/glossary.d/*.json
  src/front/*.html         front-matter pages, in the order listed in FRONT
  src/back/*.html          back-matter pages, in the order listed in BACK
  src/chapters/<id>.html   chapter bodies
  src/shell.html           page frame; assets/style.css and assets/app.js are inlined into it

Run:
  python3 build.py           writes docs/index.html (the GitHub Pages site) and audits it
  python3 build.py --check   audits only and writes nothing
"""

import html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
DOCS = os.path.join(ROOT, "docs")
FRONT = ["welcome", "paths"]
BACK = ["glossary", "sources"]

OUTCOME = {"understand": "Understand", "use": "Use", "build": "Build"}
LEVEL_LABEL = {
    "beginner": "Beginner",
    "intermediate": "Intermediate",
    "advanced": "Advanced",
    "expert": "Expert",
    "reference": "Reference",
    "all": "All levels",
}
BALANCED_TAGS = ["section", "article", "div", "table", "details", "ol", "ul", "dl", "figure", "svg"]


# ---------- helpers


def read(*parts):
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as f:
        return f.read()


def esc(text):
    return html.escape(text, quote=True)


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def strip_tags(text):
    return re.sub(r"<[^>]+>", "", text)


def minutes(chapter):
    return chapter["read"] + chapter["practice"]


# ---------- loading


def load_curriculum():
    """Return the curriculum and a flat list of chapters with their part and labels."""
    cur = json.loads(read("src", "curriculum.json"))
    overrides = cur.get("outcomeOverride", {})
    optional = set(cur.get("optional", []))
    chapters = []
    for part in cur["parts"]:
        for cid, title, level, read_min, practice_min in part["chapters"]:
            chapters.append(
                {
                    "id": cid,
                    "num": int(cid[2:]),
                    "title": title,
                    "level": level,
                    "read": read_min,
                    "practice": practice_min,
                    "part": part["id"],
                    "partNum": part["num"],
                    "written": os.path.exists(os.path.join(SRC, "chapters", cid + ".html")),
                    "outcome": overrides.get(cid, part.get("outcome", "understand")),
                    "optional": cid in optional,
                }
            )
    return cur, chapters


def load_glossary():
    """Main glossary plus the per-chapter files in src/glossary.d (the main file wins on duplicates)."""
    glossary = json.loads(read("src", "glossary.json"))
    extra_dir = os.path.join(SRC, "glossary.d")
    if os.path.isdir(extra_dir):
        for name in sorted(os.listdir(extra_dir)):
            if name.endswith(".json"):
                for term, entry in json.loads(read("src", "glossary.d", name)).items():
                    glossary.setdefault(term, entry)
    return glossary


# ---------- rendering


def render_part_header(part, part_chapters):
    items = []
    for c in part_chapters:
        title = esc(c["title"])
        target = f'<a href="#{c["id"]}">{title}</a>' if c["written"] else f'<span class="planned">{title}</span>'
        items.append(f'<li><span class="n">{c["num"]}</span>{target}</li>')
    written = sum(1 for c in part_chapters if c["written"])
    written_chip = "" if written == len(part_chapters) else f'<span class="chip">{written} written</span>'
    return f"""
<section class="part" id="{part["id"]}" data-num="{part["num"]}">
<header class="part-head" id="{part["id"]}-head">
<div class="part-label">Part {part["num"]}</div>
<h2>{esc(part["title"])}</h2>
<p class="sub">{esc(part["sub"])}</p>
<p>{esc(part["intro"])}</p>
<div class="chips">
<span class="chip lvl">{esc(part["level"])}</span><span class="chip">{len(part_chapters)} chapters</span>{written_chip}
</div>
<ol class="part-toc">{"".join(items)}</ol>
</header>"""


def render_chapter(chapter, part, prev, nxt, author):
    c = chapter
    body = read("src", "chapters", c["id"] + ".html")
    nav_prev = f'<a href="#{prev["id"]}">← {prev["num"]}. {esc(prev["title"])}</a>' if prev else "<span></span>"
    nav_next = f'<a href="#{nxt["id"]}">{nxt["num"]}. {esc(nxt["title"])} →</a>' if nxt else "<span></span>"
    optional = '<span class="chip opt">Optional</span>' if c["optional"] else ""
    chips = (
        f'<span class="chip lvl">{LEVEL_LABEL[c["level"]]}</span>'
        f'<span class="chip goal">Goal · {OUTCOME[c["outcome"]]}</span>{optional}'
        f'<span class="chip">Read · {c["read"]} min</span>'
        f'<span class="chip">Practise · {c["practice"]} min</span>'
    )
    credit = (
        f"AI &amp; Claude Mastery · © {author['year']} {esc(author['name'])} · "
        f'<a href="{author["github"]}" target="_blank" rel="noopener">github.com/onlytapas</a> · '
        f'<a href="{author["site"]}" target="_blank" rel="noopener">onlytapas.github.io</a>'
    )
    return f"""
<article class="chapter" id="{c["id"]}" data-level="{c["level"]}"
 data-read="{c["read"]}" data-practice="{c["practice"]}">
<header class="ch-head">
<div class="ch-eyebrow">Part {part["num"]} · Chapter {c["num"]}</div>
<h2><span class="num">{c["num"]}</span>{esc(c["title"])}</h2>
<div class="ch-meta">{chips}</div>
</header>
{body}
<div class="ch-nav">{nav_prev}{nav_next}</div>
<p class="ch-credit">{credit}</p>
</article>"""


def render_glossary_items(glossary, chapters):
    numbers = {c["id"]: c["num"] for c in chapters}
    items = []
    for term in sorted(glossary, key=str.lower):
        entry = glossary[term]
        see = ""
        if entry.get("see"):
            target = entry["see"]
            label = f"Chapter {numbers[target]}" if target in numbers else target
            see = f' <a href="#{target}">{label}</a>'
        items.append(f'<dt id="g-{slug(term)}">{esc(term)}</dt><dd>{entry["d"]}{see}</dd>')
    return "\n".join(items)


def mark_unwritten_links(body, chapters):
    """Links to chapters that don't exist yet become plain 'being written' text instead of broken links."""
    planned = {c["id"]: c for c in chapters if not c["written"]}

    def replace(match):
        target = planned.get(match.group(1))
        if not target:
            return match.group(0)
        return f'<span class="xref-planned" title="Chapter {target["num"]} is being written">{match.group(2)}</span>'

    return re.sub(r'<a href="#(ch\d+)(?:-\d+)?">(.*?)</a>', replace, body)


def page_data(cur, chapters, glossary):
    """The JSON the page script reads: navigation, chapter labels and pop-up glossary."""
    chapter_keys = ("id", "num", "title", "level", "read", "practice", "part", "written", "outcome", "optional")
    return {
        "parts": [{k: p[k] for k in ("id", "num", "title", "level")} for p in cur["parts"]],
        "chapters": [{k: c[k] for k in chapter_keys} for c in chapters],
        "glossary": {slug(t): {"t": t, "d": strip_tags(v["d"])} for t, v in glossary.items()},
        "verified": cur["verified"],
    }


def assemble(cur, chapters, glossary):
    author = cur["author"]
    written = [c for c in chapters if c["written"]]
    out = [read("src", "front", name + ".html") for name in FRONT]

    for part in cur["parts"]:
        part_chapters = [c for c in chapters if c["part"] == part["id"]]
        out.append(render_part_header(part, part_chapters))
        for c in part_chapters:
            if c["written"]:
                i = written.index(c)
                prev = written[i - 1] if i > 0 else None
                nxt = written[i + 1] if i + 1 < len(written) else None
                out.append(render_chapter(c, part, prev, nxt, author))
        out.append("</section>")

    glossary_html = render_glossary_items(glossary, chapters)
    out += [read("src", "back", name + ".html").replace("<!--GLOSSARY-->", glossary_html) for name in BACK]
    body = mark_unwritten_links("\n".join(out), chapters)

    data = json.dumps(page_data(cur, chapters, glossary), ensure_ascii=False).replace("</", "<\\/")
    hours_all = sum(minutes(c) for c in chapters) / 60
    hours_core = sum(minutes(c) for c in chapters if not c["optional"]) / 60
    replacements = {
        "/*CSS*/": read("assets", "style.css"),
        "<!--BODY-->": body,
        "/*DATA*/": data,
        "/*JS*/": read("assets", "app.js"),
        "{{TOTAL}}": str(len(chapters)),
        "{{PARTS}}": str(len(cur["parts"])),
        "{{H_ALL}}": f"{hours_all:.0f}",
        "{{H_CORE}}": f"{hours_core:.0f}",
        "{{AUTHOR}}": esc(author["name"]),
        "{{YEAR}}": author["year"],
        "{{GITHUB}}": author["github"],
        "{{SITE}}": author["site"],
    }
    page = read("src", "shell.html")
    for placeholder, value in replacements.items():
        page = page.replace(placeholder, value)
    return page


# ---------- audit


def audit(page, chapters, glossary):
    """Return a list of problems: duplicate ids, broken links, missing glossary terms, unbalanced tags, bad quizzes."""
    problems = []
    page = re.sub(r"<script.*?</script>", "", page, flags=re.S)
    seen, dupes = set(), set()
    for element_id in re.findall(r'\sid="([^"]+)"', page):
        (dupes if element_id in seen else seen).add(element_id)
    if dupes:
        problems.append("Duplicate ids: " + ", ".join(sorted(dupes)))
    for href in sorted(set(re.findall(r'href="#([^"]+)"', page))):
        if href not in seen:
            problems.append(f"Broken internal link: #{href}")
    for term in sorted(set(re.findall(r'class="gl" href="#(g-[^"]+)"', page))):
        if term not in seen:
            problems.append(f"Glossary term missing: {term}")
    for tag in BALANCED_TAGS:
        opened = len(re.findall(r"<" + tag + r"[\s>]", page))
        closed = page.count("</" + tag + ">")
        if opened != closed:
            problems.append(f"Unbalanced <{tag}>: {opened} open vs {closed} close")
    for segment in page.split('<div class="qz">')[1:]:
        question = segment.split('<p class="why"')[0]
        if question.count("data-ok") != 1:
            problems.append("Quiz question without exactly one correct answer: " + strip_tags(question)[:70])
    return problems


def main():
    check_only = "--check" in sys.argv
    cur, chapters = load_curriculum()
    glossary = load_glossary()
    page = assemble(cur, chapters, glossary)

    if not check_only:
        os.makedirs(DOCS, exist_ok=True)
        with open(os.path.join(DOCS, "index.html"), "w", encoding="utf-8") as f:
            f.write(page)
        # GitHub Pages serves docs/ as plain files; .nojekyll stops it running Jekyll over them
        with open(os.path.join(DOCS, ".nojekyll"), "w", encoding="utf-8"):
            pass

    written = sum(1 for c in chapters if c["written"])
    action = "Checked" if check_only else "Built docs/index.html:"
    print(f"{action} {len(page) // 1024} KB, {written}/{len(chapters)} chapters, {len(glossary)} glossary terms")
    problems = audit(page, chapters, glossary)
    if problems:
        print("AUDIT PROBLEMS:")
        for problem in problems:
            print("  - " + problem)
        sys.exit(1)
    print("Audit: no broken links, duplicate ids or unbalanced tags.")


if __name__ == "__main__":
    main()
