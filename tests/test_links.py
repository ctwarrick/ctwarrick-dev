"""T013 [US2]: every internal href/src in build/**/*.html resolves to an
emitted file (FR-015/SC-010).

Pretty URLs (`/foo/` or `/foo`) map to `foo/index.html`; the site root (`/`)
maps to `index.html`; `/static/...` maps to that file under build/. External
URLs (`http(s)://`), `mailto:`, fragment-only links (`#...`), and `javascript:`
are exempt.
"""

from __future__ import annotations

from pathlib import Path
from urllib.parse import urlsplit

from bs4 import BeautifulSoup


def _is_internal(href: str) -> bool:
    """Return True if `href` is a same-site path this build should resolve."""
    if not href:
        return False
    if href.startswith("#"):
        return False
    scheme = urlsplit(href).scheme
    if scheme in ("http", "https", "mailto", "tel", "javascript"):
        return False
    if href.startswith("//"):
        return False
    return True


def _resolve(build: Path, href: str, html_file: Path | None = None) -> Path:
    """Map an internal href to the file it should resolve to under build/.

    Absolute paths (starting with `/`) are resolved from the build root.
    Relative paths (e.g. `./images/foo.jpg`) are resolved relative to the
    directory of the HTML file that contains the reference.
    """
    path = urlsplit(href).path
    if not path or path == "/":
        return build / "index.html"
    if not path.startswith("/"):
        # Relative path — resolve against the containing HTML file's directory.
        base = html_file.parent if html_file is not None else build
        return (base / path).resolve()
    path = path.lstrip("/")
    if path.endswith("/"):
        return build / path / "index.html"
    target = build / path
    if target.suffix:
        return target
    return build / path / "index.html"


def test_internal_links_resolve_to_emitted_files(build: Path) -> None:
    """Every internal href/src in the frozen site resolves to a real file."""
    html_files = sorted(build.rglob("*.html"))
    assert html_files, "expected at least one frozen HTML file"

    missing: list[str] = []
    for html_file in html_files:
        soup = BeautifulSoup(html_file.read_text(encoding="utf-8"), "html.parser")
        for tag in soup.find_all(["a", "link", "script", "img"]):
            attr = "href" if tag.name in ("a", "link") else "src"
            href = tag.get(attr)
            if not href or not _is_internal(href):
                continue
            target = _resolve(build, href, html_file)
            if not target.is_file():
                missing.append(f"{html_file.relative_to(build)} -> {href} (expected {target})")

    assert not missing, "internal links/srcs do not resolve:\n" + "\n".join(missing)
