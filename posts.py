"""posts.py — Markdown blog post loader.

Why: the writing index and article pages render from `posts/*.md` rather than
hardcoded data, so adding/removing a post is a one-file change (FR-009/FR-010,
contracts/post-frontmatter.md). This module is the only place that knows how a
Markdown file with YAML front-matter becomes the `dict` shape the `writing`
and `article` templates consume.

Data contract (specs/001-static-site/data-model.md, "Post (`POSTS`)"):
    Required front-matter: title, date (ISO YYYY-MM-DD), tag, excerpt.
    Optional front-matter: read, featured (bool, default False).
    Derived fields added by the loader: id (filename stem), body_html
    (Markdown body rendered to HTML with Pygments-highlighted fenced code),
    date_display (human-readable date for templates).

Ordering: posts are returned most-recent-first by `date` (FR-011). A missing
required key raises `ValueError` so the freeze fails loudly at build time
rather than shipping a broken post. An empty or absent `posts_dir` yields
`[]` (Edge Case: empty writing index, no error).
"""

from __future__ import annotations

import datetime as _dt
import re
from pathlib import Path

import frontmatter
import markdown as _markdown

REQUIRED_KEYS = ("title", "date", "tag", "excerpt")

_MARKDOWN_EXTENSIONS = ["fenced_code", "codehilite", "tables", "attr_list"]


def _date_display(value: object) -> str:
    """Render a front-matter `date` value as a human-readable label.

    Accepts a `datetime.date`/`datetime.datetime` (what PyYAML parses an
    unquoted `YYYY-MM-DD` into) or a string, and formats it as e.g. "May 1,
    2026". Falls back to `str(value)` if the value can't be parsed.
    """
    if isinstance(value, _dt.datetime):
        value = value.date()
    if isinstance(value, _dt.date):
        return value.strftime("%B %-d, %Y")
    try:
        parsed = _dt.date.fromisoformat(str(value))
    except ValueError:
        return str(value)
    return parsed.strftime("%B %-d, %Y")


def _date_key(value: object) -> _dt.date:
    """Return a `datetime.date` suitable for most-recent-first sorting."""
    if isinstance(value, _dt.datetime):
        return value.date()
    if isinstance(value, _dt.date):
        return value
    return _dt.date.fromisoformat(str(value))


def load_posts(posts_dir: str = "posts") -> list[dict]:
    """Load and render all Markdown posts from `posts_dir`.

    Args:
        posts_dir: directory containing `*.md` post files (default `"posts"`).

    Returns:
        Posts as dicts, ordered most-recent-first by `date`. Each dict carries
        the front-matter keys plus `id`, `body_html`, `date_display`, and
        `featured` (defaulted to `False`). Returns `[]` if `posts_dir` is
        empty, absent, or contains no `.md` files.

    Raises:
        ValueError: a post is missing a required front-matter key
            (`title`, `date`, `tag`, `excerpt`).
    """
    directory = Path(posts_dir)
    if not directory.is_dir():
        return []

    posts: list[dict] = []
    for md_file in sorted(directory.glob("*.md")):
        post = frontmatter.load(md_file)

        missing = [key for key in REQUIRED_KEYS if key not in post.metadata]
        if missing:
            raise ValueError(
                f"{md_file}: missing required front-matter key(s): {', '.join(missing)}"
            )

        body_html = _markdown.markdown(post.content, extensions=_MARKDOWN_EXTENSIONS)
        body_html = re.sub(r'src="\./(images/[^"]+)"', r'src="/writing/\1"', body_html)

        entry = dict(post.metadata)
        entry["id"] = md_file.stem
        entry["date_display"] = _date_display(entry["date"])
        entry["date"] = str(entry["date"])
        entry["featured"] = bool(entry.get("featured", False))
        entry["body_html"] = body_html
        posts.append(entry)

    posts.sort(key=lambda p: _date_key(p["date"]), reverse=True)
    return posts
