"""T022 [US3]: tests for `posts.load_posts()`.

Targets the loader contract in `specs/001-static-site/contracts/post-frontmatter.md`
and `data-model.md`: `load_posts(posts_dir=...)` returns posts ordered
most-recent-first by ISO `date`, derives `id` from the filename stem, renders
`body_html` with Pygments-highlighted fenced code, requires
title/date/tag/excerpt (raising on a missing key), respects `featured`
(default False), and returns `[]` for an empty/absent directory.

Uses small, self-contained fixture posts under `tests/fixtures/`:
- `fixtures/posts_valid/` — two valid posts (one featured, one not).
- `fixtures/posts_invalid/` — one post missing the required `excerpt` key.
- `fixtures/posts_empty/` — no `.md` files (only a `.gitkeep`).
"""

from __future__ import annotations

from pathlib import Path

import pytest

FIXTURES = Path(__file__).parent / "fixtures"


def test_load_posts_returns_list_of_dicts() -> None:
    """`load_posts()` over a directory of valid posts returns a list of dicts."""
    from posts import load_posts

    result = load_posts(posts_dir=str(FIXTURES / "posts_valid"))
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(p, dict) for p in result)


def test_load_posts_derives_id_from_filename_stem() -> None:
    """Each post's `id` is its filename without the `.md` extension."""
    from posts import load_posts

    result = load_posts(posts_dir=str(FIXTURES / "posts_valid"))
    ids = {p["id"] for p in result}
    assert ids == {"older-post", "featured-post"}


def test_load_posts_orders_most_recent_first_by_date() -> None:
    """Posts are ordered most-recent-first by their ISO `date`."""
    from posts import load_posts

    result = load_posts(posts_dir=str(FIXTURES / "posts_valid"))
    titles = [p["title"] for p in result]
    assert titles == ["The Featured Post", "An Older Post"]


def test_load_posts_raises_on_missing_required_key() -> None:
    """A post missing a required front-matter key (here: excerpt) raises."""
    from posts import load_posts

    with pytest.raises(ValueError):
        load_posts(posts_dir=str(FIXTURES / "posts_invalid"))


def test_load_posts_renders_body_html_with_pygments_highlighting() -> None:
    """`body_html` contains Pygments-highlighted fenced code."""
    from posts import load_posts

    result = load_posts(posts_dir=str(FIXTURES / "posts_valid"))
    featured = next(p for p in result if p["id"] == "featured-post")
    assert "body_html" in featured
    body_html = featured["body_html"]
    assert "<pre" in body_html
    assert ("codehilite" in body_html) or ("highlight" in body_html)


def test_load_posts_respects_featured_flag_and_defaults_false() -> None:
    """`featured` is True for the featured fixture and defaults to False otherwise."""
    from posts import load_posts

    result = load_posts(posts_dir=str(FIXTURES / "posts_valid"))
    by_id = {p["id"]: p for p in result}
    assert by_id["featured-post"]["featured"] is True
    assert by_id["older-post"].get("featured", False) is False


def test_load_posts_returns_empty_list_for_empty_dir() -> None:
    """An empty (or absent) posts directory yields `[]`, not an error."""
    from posts import load_posts

    assert load_posts(posts_dir=str(FIXTURES / "posts_empty")) == []


def test_load_posts_returns_empty_list_for_absent_dir(tmp_path: Path) -> None:
    """A posts directory that does not exist on disk yields `[]`."""
    from posts import load_posts

    absent = tmp_path / "no-such-posts-dir"
    assert load_posts(posts_dir=str(absent)) == []
