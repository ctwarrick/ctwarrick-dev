# Implementation Plan: ctwarrick.dev — Public Static Personal Site

**Branch**: `001-static-site` | **Date**: 2026-06-15 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-static-site/spec.md`

## Summary

Build Chris Warrick's public personal site by promoting the
`design_handoff_flask/` skeleton into a real repo-root Flask + Jinja2 app,
translating the six unbuilt pages (home, building, about, writing, article,
service) from `_design_reference/*.jsx` against the worked `work.html` example,
and replacing the handoff's *live-runtime* assumptions with the
constitution-mandated **static** pipeline: **author (Flask/Jinja + Markdown) →
freeze (Frozen-Flask → `build/`) → deploy (GitHub Actions → Azure Static Web
Apps)**.

Three deliberate divergences from the handoff (each required by the
constitution / spec):

1. **Hosting**: the handoff targets Azure **App Service** with gunicorn (a live
   Python runtime). We instead **pre-render to static HTML with Frozen-Flask**
   and serve from **Azure Static Web Apps** — no runtime, no DB in production
   (Principle II, FR-012).
2. **Fonts**: the handoff loads Space Grotesk + IBM Plex Sans from **Google
   Fonts** via `@import` in `static/css/tokens/fonts.css:8`. We **self-host**
   all three typefaces and delete that `@import` (Principle I, FR-008, FR-017).
3. **Posts**: the handoff hard-codes one article body in `Article.jsx` and keeps
   post metadata as inline dicts in `content.py`. We move posts to
   **`posts/*.md`** (front-matter + Markdown body) loaded into the `POSTS`
   shape, with `post_id` = filename slug (FR-009/FR-010, clarified 2026-06-15).

## Technical Context

**Language/Version**: Python 3.12 (`.python-version`, `pyproject.toml`
`requires-python >=3.12`); environment managed with `uv`.

**Primary Dependencies**: Flask 3.x (authoring), Frozen-Flask (static freeze),
Markdown + Pygments (build-time post rendering with `codehilite` syntax
highlighting), `python-frontmatter` (post front-matter parsing). Test/build:
pytest, BeautifulSoup4 (HTML/link assertions). Deploy: GitHub Actions +
`Azure/static-web-apps-deploy`. Infra: Azure Bicep.

**Storage**: None in production (no database — Principle II). Authoring-time
content lives in `content.py` (structured data) and `posts/*.md` (articles).

**Testing**: `uv run pytest` for Python/build/security-invariant logic;
`uv run python freeze.py` must build clean; `scripts/validate-infra.sh`
(`az bicep build-params`) compile-checks infra.

**Target Platform**: Static files on **Azure Static Web Apps (Free SKU)** at
`ctwarrick.dev` over HTTPS with managed, auto-renewing TLS.

**Project Type**: Static content website — *authored* as a Flask/Jinja app,
*shipped* as frozen flat HTML.

**Performance Goals**: Low-traffic personal site; standard static-asset
delivery only. A content push is live within **10 minutes** (SC-005).

**Constraints**: Zero third-party/network requests from any page (SC-002);
zero server processes and zero databases in production (SC-003); no flash of the
wrong theme on load (SC-008); WCAG AA contrast in both themes (SC-007); the
build **fails** if any internal link/route does not resolve (SC-010, FR-015).

**Scale/Scope**: 7 page types + a styled 404; ~4 seed posts; single author,
publish-by-git-push.

## Constitution Check

*GATE: must pass before Phase 0 research. Re-checked after Phase 1 design.*

| Principle | Gate | Plan compliance |
|---|---|---|
| I. Minimal Attack Surface (NON-NEGOTIABLE) | No backend-state surface; no external/network dependency; self-contained presentation-only JS only | Frozen-Flask emits static files (no prod runtime/DB); **Google Fonts `@import` removed** and all 3 typefaces self-hosted; no trackers/analytics/CDN; only JS is the existing FOUC-free theme toggle (and an optional self-contained mobile-nav toggle). `mailto:` contact, no forms. **PASS** |
| II. Static-Only Output | Author Flask/Jinja+MD → freeze → deploy SWA | `freeze.py` (Frozen-Flask) renders every route + each post to `build/`; CI deploys `build/`. **PASS** |
| III. Design System Renders As Designed | Exact component class names; CSS load order `styles.css → components.css → site.css`; full visual fidelity | JSX→Jinja translation emits the documented `cw-*`/component classes; `base.html` already wires the load order; macros reused unchanged. **PASS** |
| IV. Accessibility Baseline | Landmarks/heading order, keyboard + visible focus, AA contrast both themes, alt text, `prefers-reduced-motion`/`prefers-color-scheme` | Add a `<main>` landmark + skip behavior, honor reduced-motion, alt text on the headshot, keyboard-operable theme + (optional) mobile nav; verified in review. **PASS (with build work)** |
| V. Content Is the User's (NON-NEGOTIABLE) | No invented biography/metrics/post bodies; TODO + hand back where copy is missing | Carry `content.py` copy across verbatim as placeholder; the one existing article body (`Article.jsx`, post `p1`) migrates verbatim; **posts with no body (p2–p4) get a clearly-marked `TODO` body, never fabricated**. **PASS** |
| VI. Spec-Driven, Test-First, Independently Reviewed | TDD for testable logic; translation is plan-driven; fresh-context review; human gates | Post loader, freeze, link-resolution invariant, and infra are built test-first; page translation is plan-driven and verified by freeze + class-contract + review. **PASS** |

**Result**: No violations. **Complexity Tracking is empty** (nothing to justify).

## Project Structure

### Documentation (this feature)

```text
specs/001-static-site/
├── plan.md              # This file
├── research.md          # Phase 0 — decisions (freeze, markdown, fonts, SWA/DNS)
├── data-model.md        # Phase 1 — content entities + post front-matter schema
├── quickstart.md        # Phase 1 — run/validate guide
├── contracts/           # Phase 1 — URL/route, post front-matter, static-hosting contracts
│   ├── url-routes.md
│   ├── post-frontmatter.md
│   └── static-hosting.md
├── spec.md              # Feature spec (clarified 2026-06-15)
└── checklists/requirements.md
```

### Source Code (repository root)

The handoff's contents are **promoted into the repo root** — the layout the
constitution's Technology table prescribes, which is also the conventional
small-Flask + Frozen-Flask shape (a flat root module, not a `src/`/`app/`
package). Once promoted, **`design_handoff_flask/` is untracked and gitignored**
as a local-only reference. It is currently *tracked* (68 files), so this is
`git rm --cached -r design_handoff_flask/` **plus** a `.gitignore` entry — the
working-tree copy stays on disk so `_design_reference/*.jsx` remains the
translation source. The Windows `*.Zone.Identifier` files are cruft and are
**not** promoted.

```text
app.py                      # Flask routes (one per page; /writing/<post_id>)
content.py                  # structured content (SITE, NAV, STATS, WORK, PROJECTS, SERVICE, SKILLS, CERTS)
posts.py                    # NEW: Markdown post loader → POSTS (front-matter + rendered body)
freeze.py                   # NEW: Frozen-Flask freeze of all routes + posts → build/
posts/                      # NEW: one Markdown file per article (filename = slug = post_id)
│   ├── stop-the-story-point-voodoo.md
│   ├── ...
templates/
│   ├── base.html           # shell (head, header, footer, theme toggle)   [from handoff]
│   ├── _macros.html        # design-system components as macros           [from handoff]
│   ├── work.html           # worked example                               [from handoff]
│   ├── home.html building.html about.html writing.html article.html service.html   # translated
│   └── 404.html            # NEW: styled not-found page
static/
│   ├── css/                # styles.css → components.css → site.css (+ tokens/*)   [from handoff]
│   ├── fonts/              # Old Timey Code + NEW self-hosted Space Grotesk & IBM Plex Sans (woff2)
│   └── img/                # headshot + any post images (all self-hosted)
staticwebapp.config.json    # NEW: SWA 404 override, MIME types, HSTS header
infra/                      # NEW: main.bicep + dns.bicep + static-web-app.bicep + main.bicepparam (SWA + Azure DNS zone, new RG)
scripts/validate-infra.sh   # NEW: az bicep build-params compile check
.github/workflows/deploy.yml# NEW: uv sync → pytest → freeze → static-web-apps-deploy
tests/                      # pytest: routes, post loader, freeze output, link/attack-surface invariants
pyproject.toml              # uv deps (flask, frozen-flask, markdown, pygments, python-frontmatter, pytest, beautifulsoup4)
```

**Structure Decision**: Single repo-root Flask project (no `src/`/`app/` package
split — the constitution names these exact top-level paths, and a flat module is
the standard shape for a site this size). Tests live under `tests/`. Both
`build/` and the now-gitignored `design_handoff_flask/` are untracked.

### Handoff → repo-root promotion mapping

The **first build task** (before any translation) promotes the handoff and
untracks it. Mapping:

| Handoff path | Repo-root destination | Disposition |
|---|---|---|
| `app.py` | `app.py` | promote, then extend (posts loader wiring, freeze) |
| `content.py` | `content.py` | promote as-is (copy is the owner's placeholder) |
| `templates/{base,_macros,work}.html` | `templates/` | promote as-is |
| `static/css/**` (+ `tokens/`) | `static/css/` | promote; then delete Google `@import` (`tokens/fonts.css:8`) |
| `static/fonts/`, `static/img/` | `static/` | promote; add self-hosted Space Grotesk + IBM Plex Sans woff2 |
| `_design_reference/*.jsx` | *(stays in gitignored handoff dir)* | translation source only — not shipped, not tracked |
| `requirements.txt` | — | dropped; deps live in `pyproject.toml` (uv) |
| `startup.txt`, `.github/workflows/azure-webapp.yml`, `README.md` | — | dropped; App Service artifacts replaced by SWA freeze/deploy |
| `*.Zone.Identifier` | — | dropped (Windows cruft) |

Then: `git rm --cached -r design_handoff_flask/` and add `/design_handoff_flask/`
to `.gitignore` (keeps the local working copy, removes it from version control).

## Phase 0 — Research

See [research.md](./research.md). Resolves: the freeze tool + settings and how
the dynamic `/writing/<post_id>` route and the 404 page are frozen; the Markdown
renderer + build-time syntax-highlighting choice (self-hosted Pygments CSS); the
front-matter parser; self-hosting the two Google-hosted typefaces with the exact
weights/italics the design uses; the build-time broken-internal-link gate; and
the Azure Static Web Apps custom-domain + apex-vs-`www` 301 + GoDaddy DNS
approach. No open `NEEDS CLARIFICATION` items remain (spec clarified 2026-06-15;
infra specifics resolved here).

## Phase 1 — Design & Contracts

- [data-model.md](./data-model.md) — the content entities (Site, NavItem, Work
  entry, Project, ServiceRecord, Skill/Cert, **Post**) with fields, the
  `WORK_CIVILIAN` derivation, and the post front-matter schema + slug rule +
  most-recent-first ordering.
- [contracts/url-routes.md](./contracts/url-routes.md) — every route → template
  → active-nav → frozen output path, plus the 404 contract.
- [contracts/post-frontmatter.md](./contracts/post-frontmatter.md) — required vs
  optional front-matter keys, slug = filename rule, rendered-body contract,
  featured/empty-index behavior.
- [contracts/static-hosting.md](./contracts/static-hosting.md) — `build/`
  freeze contract, `staticwebapp.config.json` (404 override, redirect),
  attack-surface invariants the tests enforce.
- [quickstart.md](./quickstart.md) — run-and-validate guide.

## Complexity Tracking

No constitutional violations — no entries.
