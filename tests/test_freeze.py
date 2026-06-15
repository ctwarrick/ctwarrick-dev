"""T012 [US2]: the freeze emits every core route plus the styled 404 page.

Uses the `build` fixture from `tests/conftest.py`, which imports `freeze.py`
lazily (it does not exist yet) and freezes the site to a temporary directory.
"""

from __future__ import annotations

from pathlib import Path


def test_freeze_emits_core_pages_and_404(build: Path) -> None:
    """After freeze, build/ contains the core pages and a styled 404.html."""
    expected = [
        "index.html",
        "work/index.html",
        "building/index.html",
        "about/index.html",
        "writing/index.html",
        "service/index.html",
        "404.html",
    ]
    for rel in expected:
        assert (build / rel).is_file(), f"missing {rel} in frozen output"
