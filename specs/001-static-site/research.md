# Phase 0 Research: ctwarrick.dev Static Site

All decisions resolve unknowns in the plan's Technical Context. Format per
decision: **Decision / Rationale / Alternatives considered**.

## 1. Static freeze tool & freezing the dynamic + 404 routes

**Decision**: Use **Frozen-Flask**. `freeze.py` instantiates the app, sets
`FREEZER_DESTINATION = "build"`, `FREEZER_REMOVE_EXTRA_FILES = True`,
`FREEZER_IGNORE_MIMETYPE_WARNINGS = True`, and registers a URL generator that
yields one URL per post (`article` endpoint × each `post_id`) so every article
page is emitted. The 404 page is frozen by adding a generator/route that renders
`404.html` to `build/404.html` (Azure SWA serves it via `responseOverrides`,
see contract 3). Run with `uv run python freeze.py`.

**Rationale**: Frozen-Flask is the constitution's named tool; it freezes the
exact Flask/Jinja output with no second rendering path, so authoring and
production are byte-identical. URL generators are its standard mechanism for
parameterized routes.

**Alternatives considered**: A separate static-site generator (Pelican/Hugo) —
rejected: would discard the Flask/Jinja authoring ergonomics the constitution
mandates. Hand-rolled `render_template` + file-write loop — rejected:
re-implements Frozen-Flask's URL discovery and extra-file cleanup.

## 2. Markdown rendering + build-time syntax highlighting

**Decision**: Render post bodies with **Python-Markdown** using extensions
`fenced_code`, `codehilite` (Pygments), `tables`, `toc`, and `attr_list`.
Generate the Pygments stylesheet **at build time** into a self-hosted
`static/css/pygments.css` (one-time committed asset generated via
`pygments -S <style> -f html`); link it from `base.html`/article template.
Local post images live under `static/img/` and are referenced with site-relative
paths only.

**Rationale**: Satisfies the clarified scope (standard Markdown + fenced code
with highlighting + local images) with **all rich content resolved at build time
and self-hosted** — Pygments emits pre-colored `<span>` markup + a local
stylesheet, so there is **no client-side highlighter and no CDN** (FR-011,
FR-017, Principle I).

**Alternatives considered**: `markdown-it-py` + a JS highlighter (Prism/highlight.js)
— rejected: a client-side highlighter is extra JS and tempts a CDN include,
against the attack-surface rule. Server-side highlighting at request time —
rejected: there is no request time in production.

## 3. Front-matter parsing & the post model

**Decision**: Use **`python-frontmatter`** to parse YAML front-matter from each
`posts/*.md`. A new `posts.py` exposes `load_posts()` building the `POSTS` list
(same shape `app.py`/templates already consume): `id` = filename stem (the
clarified slug rule), `title/date/tag/excerpt` from front-matter (required),
optional `read` and `featured`, and `body_html` = rendered Markdown. Posts are
sorted **most-recent-first** by an ISO `date` field; the display string is
derived for the templates.

**Rationale**: Keeps the existing template contract intact (templates already
read `p.title`, `p.tag`, `p.date`, `p.excerpt`, `p.read`, `p.featured`). Storing
`date` as ISO (`YYYY-MM-DD`) makes ordering deterministic and testable, unlike
the handoff's free-text "May 2026". Filename-as-slug means adding a post is a
one-file change (FR-010).

**Alternatives considered**: Python-Markdown's `meta` extension — rejected:
its values are always lists of strings (awkward typing, no booleans). Hand-rolled
front-matter split on `---` — rejected: reinvents a solved, tested parser.

## 4. Self-hosting the typefaces (removing Google Fonts)

**Decision**: Delete the Google Fonts `@import` at
`static/css/tokens/fonts.css:8` and replace it with `@font-face` rules pointing
at self-hosted **woff2** files under `static/fonts/`: **Space Grotesk** 400/500/
600/700 and **IBM Plex Sans** 400/500/600/700 + italic 400/500 (the exact
weights/italics the design uses), alongside the already-self-hosted **Old Timey
Code**. Font files are vendored from their official SIL OFL 1.1 distributions
(author/build-time download; no runtime fetch).

**Rationale**: FR-008 and the carried-forward Assumption require self-hosting;
the Google `@import` is a third-party network dependency that violates Principle
I / FR-017 and would make SC-002 (“zero third-party requests”) fail. woff2 is
the smallest broadly-supported format. Both families are OFL-licensed, so
redistribution is permitted.

**Alternatives considered**: Keep Google Fonts with `&display=swap` — rejected:
it is exactly the external dependency the constitution forbids. Subset/variable
fonts — deferred as a later optimization; ship the discrete weights the design
already references so nothing regresses.

## 5. Build-time broken-internal-link gate

**Decision**: After the freeze, a pytest test parses every emitted
`build/**/*.html` with BeautifulSoup and asserts that each **internal** `href`/
`src` resolves to a file that exists in `build/` (mapping pretty URLs to their
`index.html`); external `http(s)://` and `mailto:` links are exempted from the
existence check (but counted for the attack-surface test, #6). CI runs freeze
then pytest, so a broken internal link **fails the build** before deploy.

**Rationale**: Directly enforces FR-015 / SC-010 (“0 broken internal links reach
production”). Frozen-Flask alone freezes registered URLs but does not crawl
authored HTML links, so an explicit link-resolution test is the reliable gate.

**Alternatives considered**: `FREEZER_REMOVE_EXTRA_FILES` / relying on
Frozen-Flask to error — rejected: it does not validate arbitrary in-page hrefs.
A standalone link-checker binary — rejected: adds a non-Python dependency when a
pytest + BeautifulSoup check is sufficient and runs in the same gate.

## 6. Attack-surface invariants as tests

**Decision**: A pytest module asserts over `build/**/*.html` and the CSS that:
no element references an external origin (`<script src>`, `<link href>`,
`@import`, `url(...)`, `<img src>`, fonts) other than `mailto:` and intentional
outbound footer/profile hyperlinks; there are **no `<form>`** elements; the only
`<script>` content is the inline theme (and optional mobile-nav) toggle with no
network calls. These run in CI.

**Rationale**: Turns FR-016/017/018 and SC-002 into an automated gate the
reviewer re-runs, rather than a manual inspection.

**Alternatives considered**: Manual network-tab inspection only — rejected: not
repeatable in CI; the spec's Independent Tests still call for a one-time manual
network check at deploy, which complements (not replaces) the automated test.

## 7. Azure Static Web Apps: custom domain, apex-vs-www, GoDaddy DNS

**Decision**: Provision a **Static Web App (Free SKU)** via Bicep into a **new
resource group** (name + region set in `main.bicepparam`). Canonical host is the
**apex `ctwarrick.dev`**; **`www.ctwarrick.dev` 301-redirects to it** (clarified
2026-06-15). Because GoDaddy does not flatten apex records, **delegate DNS to an
Azure DNS zone** (update GoDaddy nameservers): create an **alias/A** apex record
to the SWA and a **CNAME** `www` → the SWA default hostname; bind both as custom
domains on the SWA. The `www`→apex 301 is implemented at the SWA edge (custom-
domain redirect / `staticwebapp.config.json`), keeping one canonical URL.

**Rationale**: Azure DNS alias records are the supported way to point an apex at
an Azure resource when the registrar can't flatten — which is exactly the
GoDaddy limitation the spec calls out. Free SKU covers custom domain + managed
TLS (FR-013, SC-004). Infra-as-code into a new RG matches the constitution's
Technology table.

**Alternatives considered**: GoDaddy apex *forwarding* + keep DNS at GoDaddy —
rejected: forwarding is a fragile HTTP redirect, not a true apex binding, and
complicates managed-cert issuance. Make `www` canonical — rejected by the
clarification (apex is canonical). Azure Front Door for redirect — rejected:
unnecessary cost/surface for a personal site SWA already handles.

## 8. Tooling, env, and validate-infra

**Decision**: Manage the environment with **uv** (`uv sync`, `uv run …`); pin
deps in `pyproject.toml`. `scripts/validate-infra.sh` runs
`az bicep build-params --file infra/main.bicepparam` to compile-check the Bicep +
param file locally (no Azure auth needed), catching param/command-shape
mismatches (e.g., BCP258) before deploy, per the constitution's quality gates.

**Rationale**: Mirrors the commands the constitution/`CLAUDE.md` already
document; keeps the infra gate local and fast.

**Alternatives considered**: `pip`/`venv` — rejected: `uv` is the documented
toolchain. Full `az deployment group what-if` in the gate — rejected: needs Azure
auth; reserved for the actual (human-gated) deploy step.
