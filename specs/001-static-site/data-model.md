# Phase 1 Data Model: ctwarrick.dev

All content is authoring-time only (no production database). Structured data
lives in `content.py` as Python lists/dicts; articles live in `posts/*.md`.
Field names below match what the templates already consume (the JSX→Jinja
translation must not rename them).

## Site

Global identity + metadata, injected into every template via the context
processor (`base.html` header/footer).

| Field | Type | Notes |
|---|---|---|
| `name` | str | "Chris Warrick" |
| `role` | str | tagline / title (used in `<title>`) |
| `email` | str | `mailto:` target for the contact affordance (FR-019) |
| `github` | str | host/path (footer link) |

> Final values are the owner's (Principle V). Carry handoff values as
> placeholder; mark any missing field with a clear `TODO`.

## NavItem (`NAV`)

| Field | Type | Notes |
|---|---|---|
| `id` | str | doubles as the Flask endpoint name + active-state key |
| `label` | str | nav text |

Active-state rule (FR-002): `active_for(view)` maps `service → work` and
`article → writing`; all others map to themselves.

## Work entry (`WORK`) + `WORK_CIVILIAN`

| Field | Type | Notes |
|---|---|---|
| `id` | str | stable key |
| `period` | str | e.g. "Jan 2022 — Jun 2026" |
| `role` | str | position title |
| `org` | str | organization · location |
| `tag` | str | badge label |
| `summary` | str | paragraph |
| `outcomes` | list[str] | bullet list |
| `service` | bool (optional) | `True` marks a military entry |

**Derivation**: `WORK_CIVILIAN = [w for w in WORK if not w.get("service")]` —
the Work page and home preview render `WORK_CIVILIAN`; military entries surface
on the Service page instead.

## Project (`PROJECTS`) — Building page

| Field | Type | Notes |
|---|---|---|
| `id` | str | stable key |
| `name` | str | project name |
| `stack` | str | tech/stack note |
| `icon` | str | icon macro key |
| `link` | str | label or outbound URL (an outbound hyperlink, not a loaded resource) |
| `blurb` | str | description |

## ServiceRecord (`SERVICE`) — Service page

| Field | Type | Notes |
|---|---|---|
| `span` | str | e.g. "2003 — 2023" |
| `intro` | str | narrative paragraph |
| `headline` | list[{value,label}] | stat figures |
| `roles` | list[role] | each: `id, period, icon, role, org, summary, outcomes[]` |

## Skill / Cert (`SKILLS`, `CERTS`) — About page

`SKILLS`: `list[str]`. `CERTS`: `list[str]`.

## Post (`POSTS`) — built by `posts.py:load_posts()` from `posts/*.md`

**Identity**: `id` = the Markdown **filename without `.md`** (the clarified slug
rule). `posts/my-post.md` → `id="my-post"` → URL `/writing/my-post`. Renaming a
file changes its URL (FR-009).

### Front-matter (YAML)

| Key | Required | Type | Notes |
|---|---|---|---|
| `title` | ✅ | str | post title |
| `date` | ✅ | ISO date `YYYY-MM-DD` | used for ordering; rendered to a display string for templates |
| `tag` | ✅ | str | badge label |
| `excerpt` | ✅ | str | index summary |
| `read` | optional | str | read-time label (e.g. "6 min"); used by index + article meta |
| `featured` | optional | bool | at most one true; promotes a post to the Writing “Latest” feature block |

### Derived / rendered fields (added by the loader)

| Field | Type | Notes |
|---|---|---|
| `id` | str | filename stem |
| `body_html` | str (safe) | Markdown body rendered at build time (fenced code + Pygments highlighting + local images), marked safe for the article template |
| `date_display` | str | human label derived from `date` |

### Validation & ordering rules

1. A file missing any **required** front-matter key fails the loader (so the
   freeze fails) — surfaces authoring mistakes at build, not in production.
2. `POSTS` is ordered **most-recent-first** by `date` (FR-011).
3. **Featured**: the Writing page features the post with `featured: true`; if
   none is set, it falls back to the most-recent post (mirrors `Writing.jsx`).
4. **Empty index**: if `posts/` has no files, `POSTS == []` and the Writing page
   renders a clean empty state (Edge Case), and the freeze emits no article
   pages — no error.
5. **Unknown `post_id`**: `article()` `abort(404)` → the styled 404 page
   (FR-004).
6. **Missing body**: where the owner has not written a body, the file carries a
   clearly-marked `TODO` placeholder body — never fabricated (Principle V).

### State

Posts have no draft/unpublished state (clarified 2026-06-15): every `posts/*.md`
file is published; unfinished posts are kept out of the repo or on a branch.
