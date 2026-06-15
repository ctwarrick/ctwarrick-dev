"""Attack-surface invariants over the frozen output (build/**/*.html).

- T014 [US2]: no external-origin script/link/img, no external @import/url() in
  inline styles, no <form>; the only <script>s are inline (theme toggle, and
  optionally a mobile-nav toggle); the theme-init script lives in <head> and
  references prefers-color-scheme (FR-006/SC-008, FR-016-018, SC-002).
- T032 [US5]: every contact affordance is a mailto: link to SITE["email"], and
  there is no <form> anywhere (FR-019).
"""

from __future__ import annotations

import re
from pathlib import Path

from bs4 import BeautifulSoup

import content

EXTERNAL_RE = re.compile(r"^(https?:)?//", re.IGNORECASE)


def _frozen_html_files(build: Path) -> list[Path]:
    files = sorted(build.rglob("*.html"))
    assert files, "expected at least one frozen HTML file"
    return files


def test_no_external_script_link_or_img_sources(build: Path) -> None:
    """No <script src>, <link href>, or <img src> points at an external origin."""
    offenders: list[str] = []
    for html_file in _frozen_html_files(build):
        soup = BeautifulSoup(html_file.read_text(encoding="utf-8"), "html.parser")
        for tag in soup.find_all(["script", "link", "img"]):
            attr = "src" if tag.name in ("script", "img") else "href"
            value = tag.get(attr)
            if value and EXTERNAL_RE.match(value.strip()):
                offenders.append(f"{html_file.relative_to(build)}: <{tag.name} {attr}={value!r}>")

    assert not offenders, "external-origin asset references found:\n" + "\n".join(offenders)


def test_no_external_import_or_url_in_inline_styles(build: Path) -> None:
    """No inline <style> uses an external @import or url(http...)."""
    offenders: list[str] = []
    for html_file in _frozen_html_files(build):
        soup = BeautifulSoup(html_file.read_text(encoding="utf-8"), "html.parser")
        for style in soup.find_all("style"):
            text = style.get_text()
            for match in re.finditer(r"(@import\s+|url\()\s*['\"]?([^'\")\s]+)", text):
                target = match.group(2)
                if EXTERNAL_RE.match(target) or target.startswith("http"):
                    offenders.append(f"{html_file.relative_to(build)}: {match.group(0)!r}")

    assert not offenders, "external @import/url() in inline <style>:\n" + "\n".join(offenders)


def test_no_form_elements(build: Path) -> None:
    """No <form> elements exist anywhere in the frozen output (FR-019)."""
    offenders: list[str] = []
    for html_file in _frozen_html_files(build):
        soup = BeautifulSoup(html_file.read_text(encoding="utf-8"), "html.parser")
        if soup.find("form") is not None:
            offenders.append(str(html_file.relative_to(build)))

    assert not offenders, "<form> elements found in:\n" + "\n".join(offenders)


def test_only_inline_scripts_are_theme_and_optional_nav_toggles(build: Path) -> None:
    """The only <script>s are inline (no src) — the theme toggle and an
    optional mobile-nav toggle."""
    offenders: list[str] = []
    for html_file in _frozen_html_files(build):
        soup = BeautifulSoup(html_file.read_text(encoding="utf-8"), "html.parser")
        for script in soup.find_all("script"):
            if script.get("src"):
                offenders.append(f"{html_file.relative_to(build)}: <script src={script['src']!r}>")

    assert not offenders, "non-inline <script> elements found:\n" + "\n".join(offenders)


def test_theme_init_script_is_inline_in_head_and_checks_prefers_color_scheme(build: Path) -> None:
    """The no-FOUC theme-init script lives in <head> and references
    prefers-color-scheme as the no-stored-choice fallback (FR-006/SC-008)."""
    html_file = build / "index.html"
    assert html_file.is_file(), "expected build/index.html to exist"

    soup = BeautifulSoup(html_file.read_text(encoding="utf-8"), "html.parser")
    head = soup.find("head")
    assert head is not None, "expected a <head> element"

    head_scripts = [s for s in head.find_all("script") if not s.get("src")]
    assert head_scripts, "expected an inline theme-init <script> in <head>"

    combined = "\n".join(s.get_text() for s in head_scripts)
    assert "prefers-color-scheme" in combined, (
        "theme-init script in <head> must reference prefers-color-scheme "
        "as the no-stored-choice fallback"
    )


def test_contact_affordances_are_mailto_to_site_email(build: Path) -> None:
    """Every contact affordance is a mailto: link to SITE["email"] (FR-019)."""
    email = content.SITE["email"]
    found_mailto = False

    for html_file in _frozen_html_files(build):
        soup = BeautifulSoup(html_file.read_text(encoding="utf-8"), "html.parser")
        for tag in soup.find_all(["a", "button"]):
            href = tag.get("href", "")
            if href.startswith("mailto:"):
                found_mailto = True
                assert href == f"mailto:{email}", (
                    f"{html_file.relative_to(build)}: mailto link {href!r} "
                    f"does not target SITE['email'] ({email!r})"
                )

    assert found_mailto, "expected at least one mailto: contact affordance"
