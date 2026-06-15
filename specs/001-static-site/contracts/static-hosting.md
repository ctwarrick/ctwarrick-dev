# Contract: Static Hosting, Build Output & Attack-Surface Invariants

## Freeze output (`build/`)

- `uv run python freeze.py` renders every route + each post to `build/` with
  `FREEZER_REMOVE_EXTRA_FILES = True` (stale files pruned).
- `build/` is git-ignored; CI regenerates it on every deploy.
- Output is pure static: HTML, CSS, self-hosted fonts/woff2, self-hosted images,
  and the inline theme/mobile-nav JS only.

## `staticwebapp.config.json` (Azure Static Web Apps)

- **404 override**: `responseOverrides."404".rewrite = "/404.html"` so unknown
  paths serve the styled 404 (FR-004).
- **MIME**: ensure `.woff2`, `.webmanifest`, `.json` content types as needed.
- **Canonical redirect**: `www.ctwarrick.dev` 301-redirects to apex
  `ctwarrick.dev` (clarified 2026-06-15) at the SWA edge.
- **No headers that load external origins** (no third-party CSP report endpoints,
  no remote anything).

## Deploy pipeline (FR-012, FR-014, SC-005)

`.github/workflows/deploy.yml` on push to `main`:

1. `uv sync` → `uv run pytest` (gate) → `uv run python freeze.py`.
2. `Azure/static-web-apps-deploy` uploads `build/` as the app artifact
   (`skip_app_build: true` — already pre-rendered), `output_location` = the
   frozen directory.
3. Deploy token / publish profile comes **only** from the runner secret store
   (FR-022, SC-009) — never committed.
4. A content-only push goes live within 10 minutes with no manual server step.

## Infra (`infra/main.bicep` + `main.bicepparam`)

- Provisions an **Azure Static Web App (Free SKU)** into a **new resource
  group** (name + region in the param file).
- `scripts/validate-infra.sh` runs `az bicep build-params --file
  infra/main.bicepparam` to compile-check locally (no Azure auth), catching
  param/command-shape mismatches (e.g. BCP258) before deploy.

## Attack-surface invariants (tests enforce — Principle I, FR-016–018, SC-002/003)

Over `build/**/*.html` and the shipped CSS:

1. **No external origin** is referenced by any `<script src>`, `<link href>`,
   `<img src>`, CSS `@import`, or `url(...)` — every asset is same-origin.
   Exemptions: `mailto:` and intentional outbound footer/profile hyperlinks
   (anchors the visitor clicks, not loaded resources).
2. **No `<form>`** elements anywhere (no input-collecting/persisting surface).
3. The only `<script>` is the inline, self-contained theme toggle (and optional
   mobile-nav toggle) — no `src`, no network call, no execution of
   visitor-supplied content.
4. **No production server runtime and no database** ship — the artifact is files
   only (SC-003).
5. **No deployment secret or cloud credential** appears in tracked files
   (SC-009).
