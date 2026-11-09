"""Nothing private may be committed: no real keys or tokens, no real email addresses, no home-folder paths.

The rules are generic on purpose, so this file itself names nothing private.
"""

import re
import subprocess

from tests.helpers import ROOT

TEXT_SUFFIXES = {".html", ".md", ".json", ".py", ".js", ".css", ".txt", ".yml", ".yaml", ".sh", ""}

SECRET_PATTERNS = {
    "Anthropic API key": r"sk-ant-api\d\d-[A-Za-z0-9_\-]{20,}",
    "OpenAI-style key": r"\bsk-(?:proj-)?[A-Za-z0-9]{32,}",
    "GitHub token": r"\bgh[pousr]_[A-Za-z0-9]{30,}",
    "AWS access key": r"\bAKIA[0-9A-Z]{16}\b",
    "Google API key": r"\bAIza[0-9A-Za-z_\-]{35}\b",
    "Slack token": r"\bxox[abprs]-[A-Za-z0-9-]{20,}",
    "private key": r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
}

# Placeholder domains reserved for documentation (RFC 2606) plus SSH-style git remotes.
ALLOWED_EMAIL = re.compile(
    r"@(?:[a-z0-9-]+\.)*(?:example\.(?:com|org|net)|example|test|invalid|localhost)$"
    r"|^git@github\.com$"
)
# Example home folders used in the book's sample output.
# linuxbrew is Homebrew's standard Linux path; computeruse is the user in a demo container.
ALLOWED_HOMES = {
    "alex",
    "asha",
    "you",
    "yourname",
    "username",
    "user",
    "me",
    "sam",
    "priya",
    "runner",
    "name",
    "linuxbrew",
    "computeruse",
}


def _repo_files():
    """Files git would commit (tracked or untracked but not ignored); falls back to a walk outside git."""
    try:
        out = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.split()
        files = [ROOT / f for f in out]
    except (subprocess.CalledProcessError, FileNotFoundError):
        skip = {"share", ".git", ".venv", "venv", "node_modules", "__pycache__", ".pytest_cache"}
        files = [p for p in ROOT.rglob("*") if p.is_file() and not skip & set(p.relative_to(ROOT).parts)]
    return [f for f in files if f.suffix in TEXT_SUFFIXES and f.exists()]


def test_no_secrets():
    hits = []
    for f in _repo_files():
        text = f.read_text(encoding="utf-8", errors="ignore")
        for name, pattern in SECRET_PATTERNS.items():
            for m in re.finditer(pattern, text):
                hits.append(f"{f.relative_to(ROOT)}: {name}: {m.group(0)[:24]}…")
    assert not hits, "\n".join(hits)


def test_only_placeholder_email_addresses():
    found = set()
    for f in _repo_files():
        text = f.read_text(encoding="utf-8", errors="ignore")
        for email in re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text):
            if not ALLOWED_EMAIL.search(email.lower()):
                found.add(f"{f.relative_to(ROOT)}: {email}")
    assert not found, "real-looking email addresses:\n" + "\n".join(sorted(found))


def test_no_real_home_folders():
    found = set()
    for f in _repo_files():
        text = f.read_text(encoding="utf-8", errors="ignore")
        for home in re.findall(r"/(?:Users|home)/([A-Za-z0-9._-]+)", text):
            if home.lower() not in ALLOWED_HOMES:
                found.add(f"{f.relative_to(ROOT)}: /Users/{home}")
    assert not found, "home-folder paths that may be real:\n" + "\n".join(sorted(found))
