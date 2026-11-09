"""Open the built site in headless Chrome and check it works. Skipped when Chrome isn't installed."""

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from tests.helpers import ROOT

CHROME_PATHS = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    shutil.which("google-chrome") or "",
    shutil.which("chromium") or "",
    shutil.which("chromium-browser") or "",
]
CHROME = next((p for p in CHROME_PATHS if p and Path(p).exists()), None)

PROBE = r"""<script>
window.__errs = [];
window.addEventListener('error', function (e) { window.__errs.push(e.message); });
window.addEventListener('load', function () { setTimeout(function () {
  var q = function (s) { return document.querySelectorAll(s); }, d = document.documentElement, r = {};
  r.errors = window.__errs;
  r.chapters = q('article.chapter').length;
  r.planned = q('.nav-ch.planned').length;
  var bad = 0;
  q('a[href^="#"]').forEach(function (a) {
    var h = a.getAttribute('href').slice(1);
    if (h && !document.getElementById(h)) bad++;
  });
  r.brokenLinks = bad;
  var si = document.getElementById('searchInput'); document.getElementById('searchBtn').click();
  si.value = 'transformer'; si.dispatchEvent(new Event('input')); r.searchHits = q('#results a').length;
  r.overflow = d.scrollWidth - d.clientWidth;
  r.credit = q('.ch-credit').length;
  var out = document.createElement('pre');
  out.id = 'probe';
  out.textContent = JSON.stringify(r);
  document.body.appendChild(out);
}, 800); });
</script>"""


@pytest.fixture(scope="module")
def probe(tmp_path_factory, chapter_ids):
    if CHROME is None:
        pytest.skip("Google Chrome or Chromium not installed")
    subprocess.run([sys.executable, str(ROOT / "build.py")], check=True, capture_output=True, cwd=ROOT)
    page = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")
    test_page = tmp_path_factory.mktemp("site") / "index.html"
    test_page.write_text(page.replace("<body>", "<body>" + PROBE, 1), encoding="utf-8")
    dom = subprocess.run(
        [
            CHROME,
            "--headless=new",
            "--disable-gpu",
            "--window-size=1280,900",
            "--virtual-time-budget=20000",
            "--dump-dom",
            test_page.as_uri(),
        ],
        capture_output=True,
        text=True,
        timeout=180,
    ).stdout
    m = re.search(r'<pre id="probe">(.*?)</pre>', dom, re.S)
    assert m, "the page did not finish loading in headless Chrome"
    return json.loads(m.group(1).replace("&quot;", '"'))


def test_no_javascript_errors(probe):
    assert probe["errors"] == []


def test_every_chapter_is_rendered(probe, chapter_ids):
    assert probe["chapters"] == len(chapter_ids)
    assert probe["planned"] == 0


def test_no_broken_internal_links(probe):
    assert probe["brokenLinks"] == 0


def test_search_finds_results(probe):
    assert probe["searchHits"] > 0


def test_page_does_not_scroll_sideways(probe):
    assert probe["overflow"] <= 0


def test_author_credit_on_every_chapter(probe, chapter_ids):
    assert probe["credit"] == len(chapter_ids)
