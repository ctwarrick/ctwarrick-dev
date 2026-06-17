"""Flask application for the Chris Warrick personal site.

Declares one route per page plus `/writing/<post_id>` for individual blog
posts. Structured page content comes from `content`; blog posts are loaded
from Markdown by `posts`. The app is authored for developer ergonomics and
frozen to static HTML by `freeze` for deployment to Azure Static Web Apps,
so production runs no Python.

Run the authoring server locally:
    uv run flask --app app run --debug
"""

from __future__ import annotations

from flask import Flask, abort, render_template, send_from_directory
from werkzeug.exceptions import HTTPException

import content
import posts

app = Flask(__name__)


@app.context_processor
def inject_globals() -> dict[str, object]:
    """Expose nav and site info to every template (header and footer).

    Returns:
        A mapping with `nav` (the primary nav items) and `site` (site
        metadata) made available to all rendered templates.
    """
    return {"nav": content.NAV, "site": content.SITE}


# Which nav item highlights for a given view. Mirrors the React
# active-state logic: the Service and Article pages light up their
# parent nav item.
ACTIVE = {"service": "work", "article": "writing"}


def active_for(view: str) -> str:
    """Return the nav item that should be highlighted for a view.

    Args:
        view: the current view/endpoint name.

    Returns:
        The nav id to highlight: `view` itself, unless it maps to a
        parent (Service highlights Work, Article highlights Writing).
    """
    return ACTIVE.get(view, view)


@app.route("/")
def home() -> str:
    """Render the home page with summary stats and recent work."""
    return render_template(
        "home.html",
        active="home",
        stats=content.STATS,
        work=content.WORK[:2],
    )


@app.route("/work")
def work() -> str:
    """Render the work page with the civilian delivery timeline."""
    return render_template("work.html", active="work", work=content.WORK)


@app.route("/building")
def building() -> str:
    """Render the building page listing independent projects."""
    return render_template("building.html", active="building", projects=content.PROJECTS)


@app.route("/about")
def about() -> str:
    """Render the about page with skills and certifications."""
    return render_template(
        "about.html",
        active="about",
        skills=content.SKILLS,
        certs=content.CERTS,
    )


@app.route("/writing")
def writing() -> str:
    """Render the writing index (blog posts, most recent first)."""
    return render_template("writing.html", active="writing", posts=posts.load_posts())


@app.route("/writing/<post_id>")
def article(post_id: str) -> str:
    """Render a single blog post, or 404 if no post has that id.

    Args:
        post_id: the post identifier (the Markdown filename stem).

    Returns:
        The rendered article page.

    Raises:
        werkzeug.exceptions.NotFound: aborted with 404 when no post
            matches `post_id`.
    """
    post = next((p for p in posts.load_posts() if p["id"] == post_id), None)
    if post is None:
        abort(404)
    return render_template("article.html", active=active_for("article"), post=post)


@app.route("/writing/images/<path:filename>")
def post_image(filename: str) -> object:
    """Serve images referenced from blog posts.

    Posts live under `posts/` and reference images as `./images/<name>`, which
    the browser resolves to `/writing/images/<name>` when reading an article at
    `/writing/<post_id>`. This route closes that gap for both the dev server and
    the Frozen-Flask build (where `freeze.py` registers a generator to discover
    all files under `posts/images/`).

    Args:
        filename: path component after `/writing/images/`.

    Returns:
        The image file served from `posts/images/`.
    """
    return send_from_directory("posts/images", filename)


@app.route("/service")
def service() -> str:
    """Render the naval service page (linked from work, not in nav)."""
    return render_template(
        "service.html",
        active=active_for("service"),
        service=content.SERVICE,
    )


@app.errorhandler(404)
def not_found(error: HTTPException) -> tuple[str, int]:
    """Render the styled 404 page with a 404 status code.

    Args:
        error: the raised HTTP exception (unused; required by Flask's
            error-handler signature).

    Returns:
        The rendered 404 template paired with the 404 status code.
    """
    return render_template("404.html", active=None), 404


if __name__ == "__main__":
    app.run(debug=True)
