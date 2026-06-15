"""freeze.py — render the Flask app to static HTML with Frozen-Flask.

Why: production serves only static files from Azure Static Web Apps (no
Python runtime). This module builds a `Freezer` around the app from `app.py`,
registers a URL generator that yields one `article` URL per blog post (so
Frozen-Flask discovers the parameterized `/writing/<post_id>` routes that it
cannot find by crawling alone), and adds a dedicated `/404.html` route that
renders `templates/404.html` — Frozen-Flask does not invoke Flask's error
handlers, but it does freeze any zero-argument route it can crawl, so this
route gives it a `404.html` to emit. Azure SWA's `staticwebapp.config.json`
rewrites unknown paths to that file (contracts/static-hosting.md, FR-004).

Run:
    uv run python freeze.py

Tests (`tests/conftest.py`) call `build_freezer(app)` directly with an
overridden `FREEZER_DESTINATION` so the freeze fixture can target a temporary
directory without mutating module-level state at import time.
"""

from __future__ import annotations

import os

from flask import Flask, render_template
from flask_frozen import Freezer

import posts
from app import app


class PrettyURLFreezer(Freezer):
    """A `Freezer` that writes extensionless, no-trailing-slash URLs as
    `<path>/index.html` rather than a bare file named `<path>`.

    `app.py`'s routes (`/work`, `/writing/<post_id>`, ...) are declared
    without a trailing slash so `client.get("/work")` returns 200 directly
    (no redirect) for the route tests. Frozen-Flask's default
    `urlpath_to_filepath` would write such a URL to a bare file (`work`),
    which collides with nested paths (e.g. `/writing` vs `/writing/<post_id>`)
    and doesn't match the "pretty URL" contract
    (`contracts/url-routes.md`: `build/work/index.html`). Paths that already
    end in `/` or have a file extension (e.g. `/404.html`,
    `/static/css/site.css`) are left untouched.
    """

    def urlpath_to_filepath(self, path: str) -> str:
        """Map `/work` -> `work/index.html`; pass `/`, `*.ext`, `*/` through."""
        if not path.endswith("/") and not os.path.splitext(path)[1]:
            path += "/index.html"
        return super().urlpath_to_filepath(path)


def build_freezer(flask_app: Flask) -> Freezer:
    """Configure and return a `Freezer` bound to `flask_app`.

    Sets the freeze destination/cleanup config (if not already set by the
    caller), registers the `article` URL generator that yields one URL per
    post from `posts.load_posts()` (yields nothing when there are no posts,
    so an empty `posts/` directory freezes cleanly — Edge Case: empty writing
    index), and adds a `/404.html` route rendering `templates/404.html` so
    the freeze emits a styled 404 page.

    Args:
        flask_app: the Flask application to freeze.

    Returns:
        A `Freezer` instance ready to call `.freeze()` on.
    """
    flask_app.config.setdefault("FREEZER_DESTINATION", "build")
    flask_app.config.setdefault("FREEZER_REMOVE_EXTRA_FILES", True)
    flask_app.config.setdefault("FREEZER_IGNORE_MIMETYPE_WARNINGS", True)

    if "freeze_404" not in flask_app.view_functions:

        @flask_app.route("/404.html", endpoint="freeze_404")
        def freeze_404() -> str:
            """Render the styled 404 page for the freeze to emit as a file."""
            return render_template("404.html", active=None)

    site_freezer = PrettyURLFreezer(flask_app)

    @site_freezer.register_generator
    def article() -> "list[dict[str, str]]":  # noqa: ANN202 - Frozen-Flask generator
        """Yield one `article` URL per post, or nothing if `posts/` is empty."""
        return [{"post_id": post["id"]} for post in posts.load_posts()]

    return site_freezer


freezer = build_freezer(app)


if __name__ == "__main__":
    freezer.freeze()
