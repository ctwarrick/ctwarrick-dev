"""Shared pytest fixtures for the ctwarrick.dev test suite.

Provides a Flask `app` fixture and a `client` fixture for route-level tests,
plus a `build` fixture that lazily freezes the site to a temporary directory
for the freeze/link/attack-surface tests added in later phases.

`freeze.py` does not exist yet (it lands in US2), so the `build` fixture
imports it lazily inside the fixture body — this keeps collection clean even
before that module is written.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterator

import pytest
from flask import Flask
from flask.testing import FlaskClient


@pytest.fixture
def app() -> Flask:
    """Return the site's Flask application instance."""
    from app import app as flask_app

    flask_app.config.update(TESTING=True)
    return flask_app


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    """Return a Flask test client bound to the `app` fixture."""
    return app.test_client()


@pytest.fixture
def build(tmp_path: Path) -> Iterator[Path]:
    """Freeze the site to a temporary directory and yield the output path.

    Imports `freeze.py` lazily so that test collection does not fail before
    that module exists (it is implemented in US2).
    """
    import freeze

    dest = tmp_path / "build"
    freeze.app.config["FREEZER_DESTINATION"] = str(dest)
    freezer = freeze.build_freezer(freeze.app)
    freezer.freeze()
    yield dest
