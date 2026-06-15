# Quickstart: Validate the ctwarrick.dev Static Site

A run-and-validate guide. Implementation details live in `tasks.md` and the
build phase; this proves the feature works end to end.

## Prerequisites

- Python 3.12 + `uv` installed.
- (Infra/deploy steps only) Azure CLI + access to the existing
  tenant/subscription; GoDaddy DNS access for `ctwarrick.dev`.

## Setup

```bash
uv sync                 # install Flask, Frozen-Flask, Markdown, Pygments,
                        # python-frontmatter, pytest, beautifulsoup4
```

## Author locally (Flask dev server)

```bash
uv run flask --app app run --debug
# visit http://127.0.0.1:5000/  and click through:
#   /  /work  /building  /about  /writing  /writing/<slug>  /service
#   a bad URL (e.g. /nope) → styled 404
```

**Validate (US1, US3, US4):**
- Each page renders with the design system; nav marks the active section
  (Service → Work, article → Writing).
- Theme toggle flips light/dark, persists across pages/reloads, no FOUC.
- Narrow the window → layout adapts, nav stays usable.
- Writing index lists posts most-recent-first; opening one shows the rendered
  body; back link returns to the index.

## Add a post (US3 / FR-010, SC-006)

```bash
# create posts/my-new-post.md with required front-matter + body, then:
uv run flask --app app run --debug
# /writing now lists it; /writing/my-new-post renders it — no code change.
```

## Freeze to static (US2 / FR-012, FR-015)

```bash
uv run python freeze.py     # renders every route + post to build/
ls build/                   # index.html work/ building/ about/ writing/ service/ 404.html
```

**Validate:**
- `build/writing/<slug>/index.html` exists for each post.
- Re-run after deleting a post file → its page is pruned (REMOVE_EXTRA_FILES).

## Run the gates (Principle VI / quality gates)

```bash
uv run pytest               # routes, post loader, freeze output,
                            # broken-internal-link gate, attack-surface invariants
uv run python freeze.py     # must build clean
scripts/validate-infra.sh   # az bicep build-params compile check (no Azure auth)
```

**Expected:** pytest green; freeze clean; infra compiles. A broken internal link
or a post missing required front-matter must make the suite/freeze **fail**
(SC-010).

## Attack-surface spot check (US2 / SC-002, SC-003)

- Grep `build/` for `googleapis|http://|https://` in `<script>/<link>/<img>/@import`
  — only intentional outbound *anchor* hrefs (GitHub/LinkedIn) and `mailto:`
  should appear; **zero** asset loads from other origins.
- Confirm no `<form>` and no production server/DB — `build/` is files only.

## Deploy (US2 / FR-013, FR-014, SC-004, SC-005) — human-gated

1. Validate infra: `scripts/validate-infra.sh`.
2. Provision: deploy `infra/main.bicep` (new resource group) — creates the SWA.
3. Bind custom domains (apex + `www`); delegate DNS to the Azure DNS zone;
   `www` 301-redirects to apex.
4. Push to `main` → GitHub Actions runs pytest + freeze + deploy.
5. **Validate:** `https://ctwarrick.dev` loads with a valid cert; browser network
   tab shows **zero** third-party requests; a trivial content push is live
   within 10 minutes.
