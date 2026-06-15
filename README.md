# ctwarrick.dev

Chris Warrick's public personal website — a static content site (home, work,
building, about, writing, service) authored as a Flask + Jinja2 app and
shipped as flat HTML.

## How it's built

```
author (Flask/Jinja + Markdown) → freeze (Frozen-Flask) → deploy (GitHub Actions → Azure Static Web Apps)
```

The whole Flask/Jinja codebase — templates, design-system macros, routes, and
the `content.py` data layer — exists for developer ergonomics while authoring.
At build time, [Frozen-Flask](https://pypi.org/project/Frozen-Flask/) crawls
every route and renders it to flat HTML in `build/`. **Production serves only
those static files** from Azure Static Web Apps: no Python runtime, no
database, no server-side state.

| Layer | Where | Notes |
|---|---|---|
| Routes | `app.py` | one route per page; `/writing/<post_id>` for articles |
| Structured content | `content.py` | site/nav/stats/work/projects/service data |
| Blog posts | `posts/*.md` | front-matter (title/date/tag/excerpt) + Markdown body |
| Templates | `templates/*.html` | `base.html` shell, `_macros.html` design-system components, one template per page |
| Design system | `static/css/` | `styles.css` (tokens) → `components.css` → `site.css`; load order matters |
| Post loader | `posts.py` | `load_posts()` — front-matter + Markdown → the shape templates consume |
| Freeze | `freeze.py` | Frozen-Flask renders all routes to `build/` |
| Infra | `infra/*.bicep*` | Azure Static Web App + custom domain, in its own resource group |
| Deploy | `.github/workflows/` | freeze + `Azure/static-web-apps-deploy` on push to `main` |

## Commands

```bash
uv sync                                  # install dependencies
uv run pytest                            # run the test suite
uv run flask --app app run --debug       # local dev server (authoring)
uv run python freeze.py                  # render the static site to build/
scripts/validate-infra.sh                # compile-check Bicep infra (no Azure needed)
```

## Writing posts

Add a Markdown file to `posts/<slug>.md` with YAML front-matter:

```yaml
---
title: "Post title"
date: 2026-06-01
tag: Delivery
excerpt: "One or two sentences shown on the writing index."
read: "5 min read"   # optional
featured: true       # optional — featured post on /writing
---

Post body in Markdown. Fenced code blocks are syntax-highlighted with
Pygments at build time.
```

The filename stem becomes the post's `id` and its URL (`/writing/<slug>`).
Posts are listed most-recent-first by `date`; no code change is needed to
add, edit, or remove a post — just edit `posts/*.md` and re-run the freeze.

## Design constraints (read before changing anything)

This site is public-facing and deliberately minimal-surface:

- **No backend-state surface in production** — no server runtime, database,
  user accounts, comments, or forms that accept and persist user input.
- **No external/third-party dependencies** — no CDN-loaded JS/CSS/fonts, no
  analytics or trackers, no client-side network calls. Fonts, icons, and
  images are all self-hosted under `static/`.
- The light/dark theme toggle is the one piece of client JavaScript: a small,
  self-contained, presentation-only script with no network access.
- Contact is a `mailto:` link to `site.email` — no on-site form.

See `agents/*.md` and `specs/001-static-site/` for the full constitution and
plan.
