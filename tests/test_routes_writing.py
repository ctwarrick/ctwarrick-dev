"""T023 [US3]: /writing and /writing/<slug> route tests.

`/writing` lists posts most-recent-first (by title order); `/writing/<slug>`
renders the post body, a back link to `/writing`, and marks the Writing nav
item active (FR-002, active_for); an unknown slug returns 404.

Until `posts.load_posts()` exists and `app.py` is wired to it (US3), this is
red — the routes currently render from the static `content.POSTS` dict.
"""

from __future__ import annotations

from bs4 import BeautifulSoup
from flask.testing import FlaskClient

import content


def _active_nav_id(html: str) -> str | None:
    """Return the nav item id whose link carries the `navlink--on` marker."""
    soup = BeautifulSoup(html, "html.parser")
    on = soup.select(".hdr__nav a.navlink--on")
    if not on:
        return None
    label = on[0].get_text(strip=True)
    for item in content.NAV:
        if item["label"] == label:
            return item["id"]
    return None


def test_writing_index_lists_posts_most_recent_first(client: FlaskClient) -> None:
    """`/writing` returns 200 and lists post titles in most-recent-first order."""
    from posts import load_posts

    resp = client.get("/writing")
    assert resp.status_code == 200

    posts = load_posts()
    assert posts, "expected at least one post from posts/*.md"

    titles = [p["title"] for p in posts]
    positions = [resp.text.find(title) for title in titles]
    assert all(pos != -1 for pos in positions), "not every post title is rendered"
    assert positions == sorted(positions), "post titles are not most-recent-first"


def test_writing_index_marks_writing_active(client: FlaskClient) -> None:
    """`/writing` marks the Writing nav item active."""
    resp = client.get("/writing")
    assert resp.status_code == 200
    assert _active_nav_id(resp.text) == "writing"


def test_article_renders_body_and_back_link_and_marks_writing_active(
    client: FlaskClient,
) -> None:
    """`/writing/<slug>` renders the post body, a back link to /writing, and
    marks Writing active (active_for("article") == "writing")."""
    from posts import load_posts

    posts = load_posts()
    assert posts, "expected at least one post from posts/*.md"
    post = posts[0]

    resp = client.get(f"/writing/{post['id']}")
    assert resp.status_code == 200

    soup = BeautifulSoup(resp.text, "html.parser")

    # Body is rendered.
    assert post["title"] in resp.text

    # Back link to the writing index.
    back_links = [a for a in soup.find_all("a") if a.get("href") == "/writing"]
    assert back_links, "expected a back link with href='/writing'"

    # Article page marks Writing active via active_for.
    assert _active_nav_id(resp.text) == "writing"


def test_unknown_article_slug_returns_404(client: FlaskClient) -> None:
    """`/writing/<slug>` for an unknown slug returns 404."""
    resp = client.get("/writing/this-slug-does-not-exist")
    assert resp.status_code == 404
