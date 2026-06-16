"""Route tests for the core pages (US1), 404 handling (US2), and Service (US4).

This file is appended across phases per tasks.md:
- T007 [US1]: home/work/building/about render 200, mark the correct active
  nav item, and include representative context.
- T015 [US2]: unknown routes / unknown post ids 404 with the styled template.
- T030 [US4]: /service renders 200 and marks Work active.
"""

from __future__ import annotations

from bs4 import BeautifulSoup
from flask.testing import FlaskClient

import content


def _active_nav_id(html: str) -> str | None:
    """Return the nav item id whose link carries the active marker.

    The header in `templates/base.html` renders
    `class="navlink navlink--on"` on the `<a>` for the active nav item, with
    `href` built from `url_for(n.id)`. We match the link's visible label back
    to `content.NAV` to recover the active nav id.
    """
    soup = BeautifulSoup(html, "html.parser")
    on = soup.select(".hdr__nav a.navlink--on")
    if not on:
        return None
    label = on[0].get_text(strip=True)
    for item in content.NAV:
        if item["label"] == label:
            return item["id"]
    return None


def test_home_returns_200_and_marks_home_active(client: FlaskClient) -> None:
    """`/` returns 200 and marks the Home nav item active."""
    resp = client.get("/")
    assert resp.status_code == 200
    assert _active_nav_id(resp.text) == "home"


def test_home_includes_stats_and_work_preview(client: FlaskClient) -> None:
    """`/` renders a STATS value and a WORK_CIVILIAN org (recent work)."""
    resp = client.get("/")
    assert resp.status_code == 200
    assert "330" in resp.text
    assert content.WORK_CIVILIAN[0]["org"] in resp.text


def test_work_returns_200_and_marks_work_active(client: FlaskClient) -> None:
    """`/work` returns 200 and marks the Work nav item active."""
    resp = client.get("/work")
    assert resp.status_code == 200
    assert _active_nav_id(resp.text) == "work"


def test_work_includes_work_org(client: FlaskClient) -> None:
    """`/work` renders the civilian work history (an org from WORK_CIVILIAN)."""
    resp = client.get("/work")
    assert content.WORK_CIVILIAN[0]["org"] in resp.text


def test_building_returns_200_and_marks_building_active(client: FlaskClient) -> None:
    """`/building` returns 200 and marks the Building nav item active."""
    resp = client.get("/building")
    assert resp.status_code == 200
    assert _active_nav_id(resp.text) == "building"


def test_building_includes_a_project_name(client: FlaskClient) -> None:
    """`/building` renders a PROJECTS name (e.g. "Job Search Agent")."""
    resp = client.get("/building")
    assert "Job Search Agent" in resp.text


def test_about_returns_200_and_marks_about_active(client: FlaskClient) -> None:
    """`/about` returns 200 and marks the About nav item active."""
    resp = client.get("/about")
    assert resp.status_code == 200
    assert _active_nav_id(resp.text) == "about"


def test_about_includes_skills_and_certs(client: FlaskClient) -> None:
    """`/about` renders a SKILLS item and a CERTS item."""
    resp = client.get("/about")
    assert "Python" in resp.text
    assert content.CERTS[0] in resp.text


def test_unknown_url_returns_styled_404(client: FlaskClient) -> None:
    """An unknown URL returns the styled 404 page, not Flask's default."""
    resp = client.get("/this-route-does-not-exist")
    assert resp.status_code == 404
    assert "404 Not Found" not in resp.text  # Flask's default werkzeug title

    soup = BeautifulSoup(resp.text, "html.parser")
    # The styled 404 extends base.html, so it carries the shared header/nav.
    assert soup.select_one("header.hdr") is not None
    assert soup.select_one(".hdr__nav") is not None


def test_unknown_post_id_returns_styled_404(client: FlaskClient) -> None:
    """`/writing/does-not-exist` returns 404 using the styled site template."""
    resp = client.get("/writing/does-not-exist")
    assert resp.status_code == 404
    assert "404 Not Found" not in resp.text

    soup = BeautifulSoup(resp.text, "html.parser")
    assert soup.select_one("header.hdr") is not None
    assert soup.select_one(".hdr__nav") is not None


def test_service_returns_200_and_marks_work_active(client: FlaskClient) -> None:
    """`/service` returns 200 and marks Work nav active (active_for)."""
    resp = client.get("/service")
    assert resp.status_code == 200
    assert _active_nav_id(resp.text) == "work"


def test_service_includes_service_record_content(client: FlaskClient) -> None:
    """`/service` renders content from SERVICE (e.g. the intro)."""
    from markupsafe import escape

    resp = client.get("/service")
    # Compare against the HTML-escaped intro: Jinja autoescapes apostrophes /
    # quotes in the copy, so the raw string is not a literal substring.
    assert str(escape(content.SERVICE["intro"])) in resp.text
