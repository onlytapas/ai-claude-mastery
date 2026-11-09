"""Structure checks: every chapter exists, follows the template and has a valid quiz."""

import re
import subprocess
import sys

from tests.helpers import CHAPTERS, ROOT, read_chapter

REQUIRED = [
    'class="objectives"',
    'class="prereq"',
    'class="bigidea"',
    'class="lab"',
    'class="quiz"',
    "box takeaways",
    "box assignment",
    "box teach",
    'class="sources"',
]


def test_build_audit_passes():
    """build.py --check reports no broken links, duplicate ids, unbalanced tags or bad quizzes."""
    result = subprocess.run(
        [sys.executable, str(ROOT / "build.py"), "--check"], capture_output=True, text=True, cwd=ROOT
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_every_chapter_has_a_file(chapter_ids):
    missing = [cid for cid in chapter_ids if not (CHAPTERS / f"{cid}.html").exists()]
    assert not missing, f"chapters listed in curriculum.json without a file: {missing}"


def test_no_orphan_chapter_files(chapter_ids):
    orphans = sorted({p.stem for p in CHAPTERS.glob("ch*.html")} - set(chapter_ids))
    assert not orphans, f"chapter files not listed in curriculum.json: {orphans}"


def test_every_chapter_follows_the_template(chapter_ids):
    problems = {}
    for cid in chapter_ids:
        text = read_chapter(cid)
        missing = [r for r in REQUIRED if r not in text]
        if f'id="{cid}-r"' not in text:
            missing.append("Review section")
        if missing:
            problems[cid] = missing
    assert not problems, problems


def test_section_numbers_run_in_order(chapter_ids):
    problems = {}
    for cid in chapter_ids:
        n = cid[2:]
        text = read_chapter(cid)
        heads = re.findall(r'<h3 id="ch(\d+)-[^"]*"><span class="num">(\d+)\.(\d+)</span>', text)
        if any(h[0] != n or h[1] != n for h in heads):
            problems[cid] = "section id or number belongs to another chapter"
        nums = [int(h[2]) for h in heads]
        if nums != list(range(1, len(nums) + 1)):
            problems[cid] = f"section numbers {nums}"
    assert not problems, problems


def test_every_quiz_question_has_exactly_one_answer(chapter_ids):
    problems = []
    for cid in chapter_ids:
        for i, q in enumerate(read_chapter(cid).split('<div class="qz">')[1:], 1):
            question = q.split('<p class="why"')[0]
            if question.count("data-ok") != 1:
                problems.append(f"{cid} question {i}")
    assert not problems, problems
