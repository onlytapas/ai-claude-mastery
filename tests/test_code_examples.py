"""Every complete code file shown in the book must at least parse.

A code block counts as a complete file when its caption starts with a file name such as `app.py`,
`settings.json`, `run_tests.sh` or `ci.yml`. Terminal sessions and output are not checked, because
they mix commands with what the computer prints back.
"""

import json
import re
import shutil
import subprocess

import pytest

from tests.helpers import code_blocks, read_chapter


def _files(chapter_ids, pattern):
    for cid in chapter_ids:
        for caption, code in code_blocks(read_chapter(cid)):
            name = caption.split()[0] if caption else ""
            if re.search(pattern, name):
                yield f"{cid} [{caption}]", code


def test_python_files_compile(chapter_ids):
    errors = []
    for where, code in _files(chapter_ids, r"\.py$"):
        try:
            compile(code, where, "exec")
        except SyntaxError as e:
            errors.append(f"{where}: line {e.lineno}: {e.msg}")
    assert not errors, "\n".join(errors)


def test_python_snippets_compile(chapter_ids):
    """Short snippets captioned "Python ..." (not install commands, REPL sessions or output)."""
    errors = []
    for cid in chapter_ids:
        for caption, code in code_blocks(read_chapter(cid)):
            not_a_snippet = re.search(r"\.py\b|repl|output|install|terminal", caption, re.I)
            if not caption.lower().startswith("python") or not_a_snippet:
                continue
            try:
                compile(code, cid, "exec")
            except SyntaxError as e:
                errors.append(f"{cid} [{caption}]: line {e.lineno}: {e.msg}")
    assert not errors, "\n".join(errors)


def test_json_files_parse(chapter_ids):
    errors = []
    for where, code in _files(chapter_ids, r"\.json$"):
        try:
            json.loads(code)
        except ValueError as e:
            errors.append(f"{where}: {e}")
    assert not errors, "\n".join(errors)


@pytest.mark.skipif(shutil.which("bash") is None, reason="bash not installed")
def test_shell_scripts_parse(chapter_ids, tmp_path):
    errors = []
    for i, (where, code) in enumerate(_files(chapter_ids, r"\.sh$")):
        script = tmp_path / f"s{i}.sh"
        script.write_text(code)
        result = subprocess.run(["bash", "-n", str(script)], capture_output=True, text=True)
        if result.returncode:
            errors.append(f"{where}: {result.stderr.strip()}")
    assert not errors, "\n".join(errors)


def test_yaml_files_parse(chapter_ids):
    yaml = pytest.importorskip("yaml", reason="install pyyaml to check YAML examples")
    errors = []
    for where, code in _files(chapter_ids, r"\.ya?ml$"):
        try:
            list(yaml.safe_load_all(code))
        except yaml.YAMLError as e:
            errors.append(f"{where}: {e}")
    assert not errors, "\n".join(errors)
