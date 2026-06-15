---
description: "Task list for ctwarrick.dev — Public Static Personal Site"
---

# Tasks: ctwarrick.dev — Public Static Personal Site

**Input**: Design documents from `/specs/001-static-site/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: TDD applies to testable Python/build/security-invariant logic (post
loader, freeze, link/attack-surface invariants, routes, infra) per constitution
Principle VI — tests are authored and shown **red before** implementation.
JSX→Jinja/CSS **translation is plan-driven** (no unit tests; verified by the
freeze building, the class contract, and review).

**Organization**: Grouped by user story. Branch policy: solo dev, work on `main`
(no feature branches); commit only when the human asks.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependency on incomplete tasks)
- **[Story]**: US1–US5 (maps to spec.md user stories)
- All paths are repo-root (per plan Structure Decision)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Promote the handoff into the repo-root structure and wire tooling.

- [ ] T001 Promote `design_handoff_flask/` contents to repo root per the plan mapping: copy `app.py`, `content.py`, `templates/{base.html,_macros.html,work.html}`, and `static/{css,fonts,img}/**` to root; **drop** `requirements.txt`, `startup.txt`, `.github/workflows/azure-webapp.yml`, the handoff `README.md`, and all `*.Zone.Identifier` files (do not copy them)
- [ ] T002 Untrack the handoff: `git rm --cached -r design_handoff_flask/`, then add `/design_handoff_flask/` and `/build/` to `.gitignore` (keeps the local working copy as the `_design_reference/` translation source)
- [ ] T003 Configure `pyproject.toml` dependencies and run `uv sync`: add `flask`, `frozen-flask`, `markdown`, `pygments`, `python-frontmatter`, `pytest`, `beautifulsoup4`; remove the placeholder `main.py`
- [ ] T004 [P] Scaffold `tests/` with `tests/conftest.py` exposing a Flask `app`/`client` fixture and a `build/` freeze fixture; add `[tool.pytest.ini_options]` to `pyproject.toml`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Shared shell + asset work every page depends on.

**⚠️ CRITICAL**: No user story work begins until this phase is complete.

- [ ] T005 Self-host fonts: vendor **Space Grotesk** (400/500/600/700) and **IBM Plex Sans** (400/500/600/700 + italic 400/500) as woff2 into `static/fonts/`, then replace the Google Fonts `@import` at `static/css/tokens/fonts.css:8` with `@font-face` rules pointing at `../fonts/` (Principle I, FR-008/FR-017)
- [ ] T006 Accessibility baseline in `templates/base.html`: wrap `{% block content %}` in a `<main id="main">` landmark, add a skip-to-content link, ensure visible `:focus-visible` styles, and honor `prefers-reduced-motion` (suppress transitions) via a CSS block in `static/css/site.css` (Principle IV, FR-020)

**Checkpoint**: Shell + fonts ready — user stories can begin.

---

## Phase 3: User Story 1 - Visitor explores Chris's professional story (Priority: P1) 🎯 MVP

**Goal**: Home, Work, Building, About render with the design system, linked by a
persistent nav with correct active state, theme toggle, responsive layout.

**Independent Test**: `uv run flask --app app run --debug`; view `/`, `/work`,
`/building`, `/about` — each renders with the design system, nav marks the active
item, theme toggle persists with no FOUC, layout adapts at mobile width.

### Tests for User Story 1 (TDD — write first, must FAIL)

- [ ] T007 [P] [US1] Route tests in `tests/test_routes_core.py`: `/`, `/work`, `/building`, `/about` return 200, set the correct `active` nav key, and include their key context (stats, work preview, projects, skills/certs)

### Implementation for User Story 1 (translation — plan-driven)

- [ ] T008 [P] [US1] Translate `templates/home.html` from `_design_reference/Home.jsx` (hero, stats, recent-work preview, CTA) using `_macros.html`; emit the exact component classes
- [ ] T009 [P] [US1] Translate `templates/building.html` from `_design_reference/Projects.jsx`
- [ ] T010 [P] [US1] Translate `templates/about.html` from `_design_reference/About.jsx` (skills + certs)
- [ ] T011 [US1] Verify `templates/work.html` (promoted worked example) still renders against the promoted CSS/macros; adjust only if the promotion broke a path

**Checkpoint**: US1 fully functional locally (MVP).

---

## Phase 4: User Story 2 - Site is published live, static, and secure (Priority: P1)

**Goal**: Frozen static output, styled 404, attack-surface clean, infra + CI
wired to Azure Static Web Apps at `ctwarrick.dev` over HTTPS.

**Independent Test**: `uv run python freeze.py` emits all routes to `build/`;
pytest gates pass; network inspection shows zero third-party requests; a push
deploys with no manual server step.

### Tests for User Story 2 (TDD — write first, must FAIL)

- [ ] T012 [P] [US2] `tests/test_freeze.py`: after freeze, `build/` contains `index.html`, `work/`, `building/`, `about/`, `writing/`, `service/`, and `404.html`
- [ ] T013 [P] [US2] `tests/test_links.py`: every internal `href`/`src` in `build/**/*.html` resolves to an emitted file (pretty URL → `index.html`); build fails otherwise (FR-015/SC-010)
- [ ] T014 [P] [US2] `tests/test_attack_surface.py`: no external-origin `<script src>`/`<link href>`/`<img src>`/CSS `@import`/`url(...)`; no `<form>`; the **only** `<script>`s are the inline theme toggle and the optional inline mobile-nav toggle (FR-016/017/018, SC-002). Also assert the theme-init script is **inline in `<head>`** (so it runs before first paint, no FOUC) and references `prefers-color-scheme` as the no-stored-choice fallback (FR-006/SC-008)
- [ ] T015 [P] [US2] `tests/test_routes_core.py`: unknown URL and unknown `post_id` return 404; 404 response uses the styled template (FR-004)

### Implementation for User Story 2

- [ ] T016 [US2] Implement `freeze.py` (Frozen-Flask): `FREEZER_DESTINATION="build"`, `FREEZER_REMOVE_EXTRA_FILES=True`, a URL generator yielding one `article` URL per post (guard zero/absent posts), and emit `build/404.html` — green for T012/T013/T015
- [ ] T017 [P] [US2] Create `templates/404.html` (extends `base.html`, on-brand) and register the 404 error handler in `app.py`
- [ ] T018 [US2] Create `staticwebapp.config.json`: `responseOverrides."404".rewrite="/404.html"`, woff2/json MIME, and `www`→apex 301 redirect (per static-hosting contract)
- [ ] T019 [P] [US2] Create `infra/main.bicep` + `infra/main.bicepparam` provisioning an Azure Static Web App (Free SKU) into a **new** resource group (name + region in the param file)
- [ ] T020 [P] [US2] Create `scripts/validate-infra.sh` running `az bicep build-params --file infra/main.bicepparam`; run it and confirm it compiles
- [ ] T021 [US2] Create `.github/workflows/deploy.yml`: on push to `main`, `uv sync` → `uv run pytest` → **secret-scan gate** (`git ls-files`-scoped grep for committed deploy-token / publish-profile / subscription·tenant-id patterns; **fail the job** if any match, SC-009/FR-022) → `uv run python freeze.py` → `Azure/static-web-apps-deploy` (deploy token from runner secret store only; `skip_app_build: true`, output = `build/`)

**Checkpoint**: Site freezes clean, passes all invariant gates, and is deploy-ready.

---

## Phase 5: User Story 3 - Visitor reads Chris's writing (Priority: P2)

**Goal**: Markdown-authored blog — writing index + article pages from `posts/*.md`.

**Independent Test**: Add a `posts/<slug>.md` with front-matter + body; it appears
on `/writing` (most-recent-first) and renders at `/writing/<slug>` with back link
— no code change.

### Tests for User Story 3 (TDD — write first, must FAIL)

- [ ] T022 [P] [US3] `tests/test_posts.py`: `load_posts()` derives `id` from filename, requires title/date/tag/excerpt (missing → error), orders most-recent-first by ISO `date`, renders `body_html` with fenced-code Pygments highlighting, handles `featured` and empty `posts/`
- [ ] T023 [P] [US3] `tests/test_routes_writing.py`: `/writing` lists posts in order; `/writing/<slug>` renders the body + back link **and sets `active="writing"`** (the article page marks Writing active, FR-002); unknown slug → 404

### Implementation for User Story 3

- [ ] T024 [US3] Implement `posts.py:load_posts()` using `python-frontmatter` + Python-Markdown (`fenced_code`, `codehilite`, `tables`, `attr_list`) — green for T022
- [ ] T025 [US3] Wire `app.py` `writing`/`article` routes to `posts.load_posts()` and **remove** the inline `POSTS` dict from `content.py`
- [ ] T026 [P] [US3] Generate self-hosted `static/css/pygments.css` (`pygments -S <style> -f html`) and link it from the article template/`base.html`
- [ ] T027 [P] [US3] Create seed `posts/*.md` from existing `content.py` POSTS metadata; migrate post `p1` body **verbatim** from `_design_reference/Article.jsx`; give p2–p4 a clearly-marked `TODO` placeholder body (Principle V — never fabricate). Any post images are **self-hosted** under `static/img/` and referenced by root-relative path (no remote images — FR-011/FR-017)
- [ ] T028 [P] [US3] Translate `templates/writing.html` from `_design_reference/Writing.jsx` (featured block + post list); render a clean **empty state** when no posts exist rather than breaking (Edge Cases — empty writing index)
- [ ] T029 [P] [US3] Translate `templates/article.html` from `_design_reference/Article.jsx` (renders `post.body_html`, meta, back link)

**Checkpoint**: Blog works locally and freezes into static article pages.

---

## Phase 6: User Story 4 - Visitor reviews Chris's military service (Priority: P2)

**Goal**: Service page renders the service record; nav marks Work active.

**Independent Test**: View `/service` — service record + highlights render with the
design system; nav shows Work active.

### Tests for User Story 4 (TDD — write first, must FAIL)

- [ ] T030 [P] [US4] `tests/test_routes_core.py`: `/service` returns 200 and sets `active="work"` (via `active_for`)

### Implementation for User Story 4

- [ ] T031 [US4] Translate `templates/service.html` from `_design_reference/Service.jsx` (reuses `.work` markup + the `.svstats` block; classes already in `site.css`)

**Checkpoint**: Service page live and correctly attributed in nav.

---

## Phase 7: User Story 5 - Visitor gets in touch (Priority: P3)

**Goal**: Contact opens the visitor's mail client; no on-site form.

**Independent Test**: Activate the header "Get in touch" and footer email — both
open a `mailto:` draft to `site.email`; no form submits data.

### Tests for User Story 5 (TDD — write first, must FAIL)

- [ ] T032 [P] [US5] `tests/test_attack_surface.py` (extend): assert the contact affordances are `mailto:` links to `site.email` and no `<form>` exists anywhere

### Implementation for User Story 5

- [ ] T033 [US5] Verify/confirm the header "Get in touch" button and footer email in `base.html` use `mailto:` to `site.email` (carried from handoff); fix only if the promotion altered them

**Checkpoint**: Contact works with zero input surface.

---

## Phase 8: Polish & Cross-Cutting Concerns

- [ ] T034 [P] Accessibility pass across all pages: headshot/img alt text (decorative marked), heading order, AA contrast in both themes, keyboard operability of nav + theme toggle (FR-020, SC-007)
- [ ] T035 [P] Per-page static SEO/meta: title, description, and self-contained social-preview (OG) tags with a self-hosted image — no external/analytics (Assumptions)
- [ ] T036 [P] Rewrite root `README.md`: run/freeze/deploy commands and the static-pipeline overview
- [ ] T037 Run full `quickstart.md` validation: `uv run pytest` green, `uv run python freeze.py` clean, `scripts/validate-infra.sh` passes, attack-surface spot check shows zero third-party requests, **tracked-files secret scan is clean** (no committed token/credential, SC-009/FR-022), and a **theme-toggle browser check**: choice persists across pages + reloads with no flash of the wrong theme, and with JS disabled the theme falls back to the OS `prefers-color-scheme` (FR-006/SC-008)

---

## Dependencies & Execution Order

### Phase dependencies

- **Setup (P1)** → **Foundational (P2)** → **User Stories (P3–P7)** → **Polish (P8)**.
- Foundational (T005–T006) blocks all stories (every page extends `base.html` and uses the fonts).

### User story dependencies

- **US1 (P1)**: after Foundational. No dependency on other stories. **MVP.**
- **US2 (P1)**: after Foundational. Its freeze (T016) guards zero/absent posts, so US2 can ship before US3 (empty writing index).
- **US3 (P2)**: after Foundational. `posts.py` is independent; the freeze picks up posts when present.
- **US4 (P2)**: after Foundational. Independent.
- **US5 (P3)**: after Foundational. Largely carried from the handoff shell.

### Within each story

- Tests authored and shown **red** before implementation (testable logic only).
- Loader/freeze before the templates that depend on them where coupled (T024 before T028/T029 freeze cleanly).

### Parallel opportunities

- Setup: T004 ∥ (after T001–T003).
- US1: T007 first; then T008/T009/T010 in parallel (separate templates).
- US2 tests T012/T013/T014/T015 in parallel; infra T019/T020 ∥ template T017.
- US3 tests T022/T023 in parallel; T026/T027/T028/T029 largely parallel after T024.

---

## Parallel Example: User Story 1

```bash
# After T007 (red), translate the three new pages in parallel:
Task: "Translate templates/home.html from Home.jsx"
Task: "Translate templates/building.html from Projects.jsx"
Task: "Translate templates/about.html from About.jsx"
```

---

## Implementation Strategy

### MVP first (US1)

1. Phase 1 Setup → 2. Phase 2 Foundational → 3. Phase 3 US1 → **STOP & validate
   locally** (core professional presence renders). Optionally then do US2 to
   publish it.

### Incremental delivery

Setup + Foundational → US1 (local MVP) → US2 (live + secure) → US3 (blog) →
US4 (service) → US5 (contact) → Polish. Each story is independently testable;
the reviewer re-runs `pytest` + `freeze` (+ `validate-infra` for infra) per gate.

---

## Notes

- [P] = different files, no incomplete-task dependency.
- `tests/test_routes_core.py` is **appended** across phases (T007 US1, T015 US2, T030 US4). Their `[P]` markers are parallel *within their own phase*; the phases run sequentially, so the appends never collide.
- Translation tasks have no unit tests by design (Principle VI) — verified by the
  freeze building, exact class names, and review.
- No task is "done" until `uv run pytest` is green and (when templates/routes/
  content change) `uv run python freeze.py` builds clean; infra tasks also require
  `scripts/validate-infra.sh`.
- Commit only when the human asks; nothing deploys without explicit go-ahead.
