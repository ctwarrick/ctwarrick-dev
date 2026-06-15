<!--
Sync Impact Report
==================
Version change: (template, unratified) → 1.0.0
Bump rationale: First ratification. Template placeholders replaced with concrete
  principles; initial adoption is a 1.0.0 baseline (MAJOR for first definition).

Principles defined (6):
  I.   Minimal Attack Surface (NON-NEGOTIABLE)   [headline]
  II.  Static-Only Output
  III. Design System Renders As Designed
  IV.  Accessibility Baseline
  V.   Content Is the User's (NON-NEGOTIABLE)
  VI.  Spec-Driven, Test-First, Independently Reviewed

Sections defined:
  - Technology & Deployment Constraints (was [SECTION_2_NAME])
  - Development Workflow & Quality Gates (was [SECTION_3_NAME])
  - Governance

Templates reviewed for consistency:
  ✅ .specify/templates/plan-template.md   — "Constitution Check" is a per-plan
       placeholder; aligns. No edit needed.
  ✅ .specify/templates/spec-template.md   — generic; account/auth examples are
       clearly illustrative ("e.g."), not project commitments. No edit needed.
  ✅ .specify/templates/tasks-template.md  — DB/auth tasks are explicitly SAMPLE
       tasks to be replaced per feature. No edit needed.
  ✅ AGENTS.md / CLAUDE.md (symlink)       — source of truth; constitution is
       derived from it and consistent with it.
  N/A .specify/templates/commands/*.md     — no such directory in this repo.

Follow-up TODOs: none. Ratification date set to first-adoption date (2026-06-14).
-->

# ctwarrick.dev Constitution

This constitution governs the personal website for Chris Warrick — a public,
deliberately minimal-surface static content site. It binds both human and AI
agents working in this repository. Where it conflicts with convenience, the
constitution wins.

## Core Principles

### I. Minimal Attack Surface (NON-NEGOTIABLE)

"Minimal attack surface" means **no backend-state surface and no
external/network dependency** — it does **NOT** mean "no JavaScript."

Prohibited in production:

- A server runtime, a database, or any persistent application state.
- User logins/accounts, comments, and **any** form or endpoint that accepts and
  persists user input (the injection / XSS-from-user-input surface).
- External or third-party scripts, trackers, analytics, and CDN-loaded
  JS / CSS / fonts.
- Any client-side network call to a remote origin.

Expected and first-class:

- The design system runs **as designed** (see Principle III).
- Self-contained, presentation-only vanilla JS is allowed **only if** it makes
  no network call, loads from no external source, and never executes
  user-supplied content. The theme toggle is the canonical example.

Rationale: a public personal site has no need for backend state or network
egress, and removing both eliminates entire vulnerability classes — injection,
XSS-from-input, supply-chain compromise, credential theft — at the cost of
nothing this site needs. Any change that introduces a backend-state surface or
an external/network dependency is a constitution violation: flag it, do not
build it.

### II. Static-Only Output

The site is **authored** as a Flask + Jinja2 application (templates, macros,
routes, the `content.py` data layer) for developer ergonomics, then
**pre-rendered** to flat HTML with Frozen-Flask at build time. Production serves
only static files from Azure Static Web Apps — no Python runtime, no database.

- Pipeline: **author (Flask/Jinja + Markdown) → freeze (Frozen-Flask) →
  deploy (GitHub Actions → Azure Static Web Apps)**.
- Blog posts are Markdown files (`posts/*.md`: front-matter
  title/date/tag/excerpt + Markdown body) loaded into the `POSTS` shape.
- Publish model is **git push → CI freeze → deploy**. There is no CMS or admin.

Rationale: this pairs the ergonomics of a real templating framework with the
security, cost, and operational profile of static hosting.

### III. Design System Renders As Designed

The design system from the handoff must render fully and faithfully: hover
states, shadows, transitions, the dark/light theme toggle, and the mobile nav.

- Most behavior is pure CSS in `components.css`; the theme toggle is the one bit
  of self-contained vanilla JS permitted under Principle I.
- CSS load order — `styles.css` (tokens) → `components.css` → `site.css` — is
  load-bearing and MUST be preserved.
- JSX → Jinja translation MUST emit the **exact** component class names from the
  design system so styles apply unchanged.

Rationale: minimal attack surface is about backend and network, not visual
austerity. The shipped site should look and behave exactly as designed.

### IV. Accessibility Baseline

Every page MUST meet a baseline of accessibility:

- Semantic HTML with proper landmarks and heading order.
- Keyboard-operable navigation, mobile nav, and theme toggle, with visible
  focus states.
- Sufficient color contrast in **both** light and dark themes.
- Meaningful images carry alt text; decorative images are marked as such.
- Honors `prefers-color-scheme` and `prefers-reduced-motion`.

Rationale: a public site must be usable by everyone; accessibility is a release
criterion, not an enhancement.

### V. Content Is the User's (NON-NEGOTIABLE)

The copy in `content.py` and `posts/*.md` belongs to Chris Warrick. Agents
translate structure and wire plumbing; they MUST NOT invent or rewrite
biography, metrics, or post bodies. Handoff content is **illustrative
placeholder only**. Where a page needs text that does not yet exist, leave a
clearly-marked `TODO` and hand back — never fabricate.

Rationale: a personal site speaks in its owner's voice, and fabricated facts
about a real person are never acceptable.

### VI. Spec-Driven, Test-First, Independently Reviewed

Work flows through phases — Specify → Plan → Build → Review → Release →
Retrospective — where each phase produces a **small artifact** that is the only
thing crossing the phase boundary (transcripts stay within a role's context).

- **Test-first** for testable logic: Python / build / security-invariant code
  (routes, the Markdown post loader, the freeze, infra) is built with failing
  tests authored and shown **red before** the implementation that satisfies
  them.
- **Translation is plan-driven:** JSX → Jinja and CSS token work is mechanical
  and verified by the freeze building, the rendered HTML matching the class
  contract, and review — not by unit tests.
- **Independent review:** every diff gets a fresh-context review against the
  plan, never the implementer's transcript.
- **Human authority:** the plan requires explicit human approval before build,
  and nothing is committed, pushed, or deployed without explicit human
  go-ahead.

Rationale: spending judgment where judgment is the product, proving invariants
with tests, and gating on a fresh reviewer plus a human keeps quality high and
context lossless.

## Technology & Deployment Constraints

| Layer | Where | Notes |
|---|---|---|
| Routes | `app.py` | one route per page; `/writing/<post_id>` for articles |
| Structured content | `content.py` | site/nav/stats/work/projects/service data |
| Blog posts | `posts/*.md` | front-matter + Markdown body → `POSTS` |
| Templates | `templates/*.html` | `base.html` shell, `_macros.html` components |
| Design system | `static/css/` | `styles.css` → `components.css` → `site.css` |
| Freeze | `freeze.py` | Frozen-Flask renders all routes to `build/` |
| Infra | `infra/*.bicep*` | Azure Static Web App + custom domain, **new** resource group |
| Deploy | `.github/workflows/` | freeze + `Azure/static-web-apps-deploy` |

- **No external/network dependency** ships in the built site (Principle I).
- **Secrets** — Azure deployment tokens/publish profiles, subscription and
  tenant IDs, and any GitHub Actions secret value — live in the runner's secret
  store, **never** in the repo, and are never committed or quoted.
- Infrastructure is declared in Bicep and deployed to a **new** resource group
  in the existing tenant/subscription. Azure Static Web Apps Free SKU covers
  custom domain + managed TLS.

## Development Workflow & Quality Gates

The work is executed by a tiered multi-agent fleet (defined in `agents/*.md`):
top-tier models for orchestration, planning, the review gate, and
retrospective; sonnet for plan-scoped build and translation; haiku for
mechanical recon. Spending top-model tokens only where judgment is the product
is intentional.

The following gates are **hard rules**; no task is "done" until they pass:

1. **TDD ordering** (testable logic): failing tests authored and shown red
   before the Python/build code that satisfies them is written.
2. **Green + frozen before done**: `uv run pytest` passes, and — when the change
   affects templates/routes/content — `uv run python freeze.py` builds clean.
   When a change touches infra (`infra/*.bicep*`) or the deploy workflow,
   `scripts/validate-infra.sh` must also pass. The reviewer **re-runs** these
   rather than trusting a claim.
3. **Independent review**: the reviewer gets a fresh context with only the diff
   and the plan.
4. **Human gates**: the plan needs explicit human approval before build; nothing
   is committed, pushed, or deployed without explicit human go-ahead.
5. **Attack-surface gate**: no change ships that adds a backend-state surface or
   an external/network dependency (Principle I).

When context pressure rises, phase artifacts and a handoff are checkpointed to
`docs/work/<task>/` so a fresh session resumes from disk with zero loss; this is
a process safeguard, not an excuse to summarize work in place.

## Governance

- This constitution supersedes other practices and conventions in this
  repository. `AGENTS.md` (and its `CLAUDE.md` symlink) is the operational
  source of truth and MUST remain consistent with this document; on any
  conflict, this constitution governs and `AGENTS.md` is corrected.
- **Amendments** are made by editing this file with a clear rationale, bumping
  the version per the policy below, updating the Last Amended date, and
  re-running the consistency propagation across dependent templates and docs.
  Amendments require explicit human approval (Principle VI).
- **Versioning policy** (semantic):
  - **MAJOR** — backward-incompatible governance/principle removal or
    redefinition.
  - **MINOR** — a new principle or section, or materially expanded guidance.
  - **PATCH** — clarifications, wording, and non-semantic refinements.
- **Compliance** — every plan records a Constitution Check, and every review
  verifies adherence (especially Principles I, IV, and V). Violations are fixed
  before merge or explicitly justified in the plan's Complexity Tracking.

**Version**: 1.0.0 | **Ratified**: 2026-06-14 | **Last Amended**: 2026-06-14
