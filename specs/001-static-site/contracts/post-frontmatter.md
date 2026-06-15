# Contract: Post Front-matter & Rendering

A blog post is a single Markdown file in `posts/`. Authoring or removing a post
is a **one-file change** — no code edit, no admin (FR-010).

## File → URL

- Filename **stem** is the post id and URL slug: `posts/<slug>.md` → `id="<slug>"`
  → `/writing/<slug>` → `build/writing/<slug>/index.html`.
- Slugs should be URL-safe (lowercase, hyphens). Renaming the file changes the
  URL (FR-009).

## Front-matter (YAML, between `---` fences)

```yaml
---
title: "Stop the story-point voodoo. Look at the data."
date: 2026-05-01            # ISO YYYY-MM-DD — drives ordering
tag: "Forecasting"
excerpt: "Velocity is a ritual that lets a team lie to itself politely…"
read: "6 min"              # optional
featured: true             # optional; at most one post true
---

Markdown body here…
```

| Key | Required | Rule |
|---|---|---|
| `title` | ✅ | non-empty string |
| `date` | ✅ | parseable ISO date; used for most-recent-first ordering |
| `tag` | ✅ | non-empty string |
| `excerpt` | ✅ | non-empty string |
| `read` | optional | display string; templates show it in meta when present |
| `featured` | optional | boolean; promotes to the “Latest” feature block |

**Loader behavior**: a file missing any required key raises at load → the freeze
fails (authoring error caught at build). The loader adds `id`, `body_html`
(rendered Markdown), and `date_display`.

## Body rendering (FR-011, FR-017)

- Rendered at **build time** with Python-Markdown: standard Markdown, fenced
  code blocks with **Pygments** syntax highlighting, tables, and `attr_list`.
- Highlighting is pre-rendered HTML + a **self-hosted** `static/css/pygments.css`
  — no client-side highlighter, no CDN.
- Images use **site-relative** paths only (e.g. `/static/img/…`); no remotely
  loaded images.

## Index & article behavior

- **Writing index**: lists posts most-recent-first with title, date, tag,
  excerpt; the featured post (or most-recent fallback) fills the feature block;
  the rest fill the post list.
- **Article page**: renders title, metadata (tag, date, optional read time),
  the rendered body, and a back link to the index.
- **Empty index**: zero post files → clean empty state, no article pages, no
  error.
