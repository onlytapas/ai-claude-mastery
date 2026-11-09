"""Shared fixtures for the test suite."""

import json

import pytest

from tests.helpers import SRC


@pytest.fixture(scope="session")
def curriculum():
    return json.loads((SRC / "curriculum.json").read_text(encoding="utf-8"))


@pytest.fixture(scope="session")
def chapter_ids(curriculum):
    return [chapter[0] for part in curriculum["parts"] for chapter in part["chapters"]]
