#!/usr/bin/env python3
"""Make personal offline copies of the book. They are for your own use and are never committed
(share/ is listed in .gitignore).

  python3 export.py    writes share/AI-Claude-Mastery.html  (one offline file with the fonts embedded)
                       and    share/AI-Claude-Mastery.pdf   (printable, light theme; needs Google Chrome)
"""

import base64
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "share")
NAME = "AI-Claude-Mastery"
CHROME_CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    shutil.which("google-chrome"),
    shutil.which("chromium"),
]
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
)
FONT_SUBSETS = ("latin", "latin-ext")  # unicode ranges worth embedding

# Print version: light theme, every optional section open, quiz answers shown.
PRINT_PREP = r"""<script>
try { localStorage.setItem('ai-claude-mastery:theme', 'light'); } catch (e) {}
window.addEventListener('load', function () {
  document.documentElement.setAttribute('data-theme', 'light');
  document.querySelectorAll('details').forEach(function (d) { d.open = true; });
  document.querySelectorAll('.qz').forEach(function (q) {
    q.querySelectorAll('[data-ok]').forEach(function (b) {
      b.classList.add('right');
      b.insertAdjacentText('afterbegin', '✓ ');
    });
    var why = q.querySelector('.why');
    if (why) { why.hidden = false; why.insertAdjacentHTML('afterbegin', '<b>Answer: </b>'); }
  });
  document.querySelectorAll('.quiz .score').forEach(function (s) { s.textContent = 'Answers shown'; });
  document.querySelectorAll('.nav-subs').forEach(function (s) { s.classList.remove('open'); });
});
</script>"""


def fetch(url):
    """Download with curl, which uses the system certificate store (Python's may not be set up on macOS)."""
    result = subprocess.run(["curl", "-sfL", "-m", "30", "-A", USER_AGENT, url], check=True, capture_output=True)
    return result.stdout


def embed_fonts(page):
    """Replace the Google Fonts link with the font files themselves, so the copy works offline."""
    link = re.search(r'<link rel="stylesheet" href="(https://fonts\.googleapis\.com/[^"]+)">', page)
    if not link:
        return page
    css = fetch(link.group(1).replace("&amp;", "&")).decode()
    faces = []
    for subset, block in re.findall(r"/\* ([a-z\-]+) \*/\s*(@font-face\s*\{.*?\})", css, re.S):
        if subset in FONT_SUBSETS:
            url = re.search(r"url\((https://[^)]+)\)", block).group(1)
            faces.append(block.replace(url, "data:font/woff2;base64," + base64.b64encode(fetch(url)).decode()))
    page = re.sub(r'<link rel="preconnect"[^>]*>\s*', "", page)
    return page.replace(link.group(0), "<style>\n" + "\n".join(faces) + "\n</style>")


def write(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def make_pdf(page, pdf_path):
    chrome = next((c for c in CHROME_CANDIDATES if c and os.path.exists(c)), None)
    if chrome is None:
        print("PDF:  skipped (Google Chrome or Chromium not found)")
        return
    print_page = os.path.join(OUT, ".print.html")
    write(print_page, page.replace("</body>", PRINT_PREP + "</body>"))
    try:
        subprocess.run(
            [
                chrome,
                "--headless=new",
                "--disable-gpu",
                "--no-pdf-header-footer",
                "--virtual-time-budget=90000",
                "--run-all-compositor-stages-before-draw",
                f"--print-to-pdf={pdf_path}",
                "file://" + print_page,
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    finally:
        os.remove(print_page)
    print(f"PDF:  {pdf_path} ({os.path.getsize(pdf_path) // 1024} KB)")


def main():
    subprocess.run([sys.executable, os.path.join(ROOT, "build.py")], check=True)
    with open(os.path.join(ROOT, "docs", "index.html"), encoding="utf-8") as f:
        page = embed_fonts(f.read())
    os.makedirs(OUT, exist_ok=True)
    html_path = os.path.join(OUT, NAME + ".html")
    write(html_path, page)
    print(f"HTML: {html_path} ({os.path.getsize(html_path) // 1024} KB)")
    make_pdf(page, os.path.join(OUT, NAME + ".pdf"))


if __name__ == "__main__":
    main()
