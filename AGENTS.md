# ctwarrick-dev — Agent Instructions

This file is the platform-agnostic source of truth for AI agents working in
this repo. `CLAUDE.md` is a symlink to it. Detailed role definitions live in
`agents/*.md`; thin per-platform adapters (e.g. `.claude/agents/`) point at
those cards.

## Project overview

A public personal website for Chris Warrick — a **static content site** built
from the Claude Design handoff in `design_handoff_flask/`. Pages: home, work,
building, about, writing (blog index), article (a post), service.

**It is authored as a Flask + Jinja2 app and shipped as static HTML.** We keep
the entire Flask/Jinja codebase (templates, macros, routes, the `content.py`
data layer) for the developer ergonomics, then **pre-render every route to flat
HTML with Frozen-Flask** at build time. Production serves only static files
from **Azure Static Web Apps** — no Python runtime, no database.

Pipeline: **author (Flask/Jinja + Markdown) → freeze (Frozen-Flask) → deploy
(GitHub Actions → Azure Static Web Apps)**.

| Layer | Where | Notes |
|---|---|---|
| Routes | `app.py` | one route per page; `/writing/<post_id>` for articles |
| Structured content | `content.py` | site/nav/stats/work/projects/service as Python lists/dicts |
| Blog posts | `posts/*.md` | front-matter (title/date/tag/excerpt) + Markdown body; loaded into the `POSTS` shape |
| Templates | `templates/*.html` | `base.html` shell, `_macros.html` design-system components, one template per page |
| Design system | `static/css/` | `styles.css` (token manifest) → `components.css` → `site.css`; load order matters |
| Freeze | `freeze.py` | Frozen-Flask renders all routes to `build/` |
| Infra | `infra/*.bicep*` | Azure Static Web App + custom domain, deployed to a new resource group |
| Deploy | `.github/workflows/` | freeze + `Azure/static-web-apps-deploy` |

The current source of truth for visuals and unbuilt pages is
`design_handoff_flask/_design_reference/` (the original React/JSX prototype) and
`design_handoff_flask/` (the worked Flask skeleton: `work.html` is the complete
example; the other pages are translated from the matching `*.jsx`).

### Commands

```bash
uv sync                                  # install deps
uv run pytest                            # run the test suite
uv run flask --app app run --debug       # local dev server (authoring)
uv run python freeze.py                  # render the static site to build/
scripts/validate-infra.sh                # compile-check Bicep infra (no Azure needed)
az bicep build-params --file infra/main.bicepparam   # what validate-infra runs
```

(Some commands come online as speckit builds the app; this is the canonical set.)

## The attack-surface rule (load-bearing)

This site is public-facing and deliberately minimal-surface. "Minimal attack
surface" means **no backend-state surface**, not "minimal JavaScript":

- **Prohibited:** a server runtime in production, a database, user
  logins/accounts, comments, and any form or endpoint that accepts and persists
  user input (the injection / XSS-from-user-input surface). Also prohibited:
  external/third-party scripts, trackers, CDN-loaded JS/CSS, and any client
  network call.
- **Expected and first-class:** the design system runs **as designed** — hover
  states, shadows, transitions, the light/dark theme toggle, and the mobile
  nav. Most of these are pure CSS in `components.css`; the theme toggle is the
  one bit of self-contained vanilla JS. Client JS is allowed as long as it stays
  self-contained and presentation-only (no network, no external source, no
  execution of user-supplied content).

Any change that introduces a backend-state surface or an external/network
dependency is a constitution violation: flag it, do not build it.

## Secrets & content — never commit, never fabricate

- **Secrets:** Azure deployment tokens / publish profiles, subscription and
  tenant IDs, and any GitHub Actions secret value live in the runner's secret
  store, never in the repo. Never commit or quote them.
- **Content is the user's.** The copy in `content.py` and `posts/*.md` is the
  user's to write. The handoff content is illustrative placeholder. Agents
  translate structure and wire plumbing; they do **not** invent or rewrite copy.
  If a page needs text that doesn't exist yet, leave a clearly-marked TODO and
  hand back — don't fabricate biography, metrics, or post bodies.

## Multi-agent workflow

Work flows through phases. Each phase produces a **small artifact** (spec, plan,
review verdict) and the next phase starts from that artifact — never from the
previous phase's raw transcript. That is the context-control mechanism:
transcripts stay inside each role's own context window.

```
Specify → Plan → [HUMAN APPROVES] → Build (TDD: test-writer → implementer)
        → Review → [HUMAN APPROVES] → Commit/PR
        → Release (on request: freeze check, deploy-wiring check, README/docs
                   drift; retrospective edits to agents/*.md ship in the same
                   release push) → [HUMAN APPROVES]
        → Retrospective (recommends role-card refinements)
        → [HUMAN COMMITS AND PUSHES TO REMOTE]
```

Not every change is TDD-shaped. The **Python/build/security-invariant logic**
(routes, the Markdown post loader, the freeze, infra) is built test-first. The
**template/CSS translation** (JSX → Jinja, copying tokens) is mechanical and
plan-driven — verified by the freeze building, the rendered HTML matching the
class contract, and the reviewer's inspection rather than by unit tests.

### Role routing

| Role | Model tier | Handles | Returns |
|---|---|---|---|
| Orchestrator (main session) | top | routing, gates, prompt composition | phase artifacts to the human |
| Scout | haiku | read-only recon: locate macros/classes/JSX, trace CSS, summarize docs | ≤30-line digest with `file:line` refs |
| Planner | top (inherit) | spec + scout digest → implementation plan | plan markdown for the human gate |
| Test-writer | sonnet | failing pytest tests for Python/build/security-invariant logic | test paths + red-failure summary |
| Implementer | sonnet | minimal diff to green + the JSX→Jinja/CSS translation bulk | changed files + green pytest + freeze summary |
| Reviewer | top (inherit) | fresh-context review; re-runs pytest + the freeze itself | `APPROVE`/`REVISE` + numbered findings |
| Releaser | sonnet | ship prep: freeze check, deploy-wiring check, README/docs drift | proposed changelog + doc edits |
| Retrospective | top (inherit) | post-ship analysis of agent performance | recommended edits to `agents/*.md` |

Model-tier rationale: spend top-model tokens where judgment is the product
(orchestration, architecture, the final bug-catching gate, meta-review); use
sonnet where the task is well-scoped by an approved plan (mechanical translation
counts); use haiku where the work is mechanical search. This tiering is the
point — it keeps clerical work off the top model.

### Delegation rules (token discipline)

1. Don't spawn an agent for what a single read or grep answers — do it inline.
2. Every dispatch gives the subagent explicit file paths and one narrow
   question or task, plus the expected output format.
3. Subagents return structured summaries (findings + `file:line` refs), never
   file dumps or full transcripts.
4. One role per dispatch. A role that finds itself doing another role's job
   stops and hands back instead.
5. Phase artifacts are the only thing that crosses phase boundaries.

### Context budget protocol

Model performance degrades well before the context window is full, and
autocompact (which *summarizes* — lossy) only fires near the hard limit. We get
ahead of both. A hook (`.claude/hooks/context_monitor.py`, registered in
`.claude/settings.json`) measures real token usage after every tool call and
user prompt against an **effective budget** =
`min(200K performance budget, 80% of the current model's window)`. It is
model-aware: a Haiku subagent (200K window) is measured against 160K, while
1M-window models (Opus 4.x, etc.) are measured against the flat 200K sweet-spot
budget. Override the budget with env `CONTEXT_BUDGET`.

| Band | Trigger | Required action |
|---|---|---|
| ELEVATED | 60% | finish the current phase, then write/refresh all phase artifacts under `docs/work/<task>/` |
| HIGH | 75% | write `docs/work/<task>/handoff.md` (state, decisions, next steps, open questions); recommend a fresh session; start no new phases |
| CRITICAL | 85% | stop dispatching; write/update the handoff immediately |

Principles:

1. **Nothing is dropped.** Artifacts and the handoff live on disk, so a fresh
   session resumes with zero loss. Never summarize-in-place as a substitute for
   checkpointing.
2. **Checkpoint continuously, not reactively.** Phase artifacts are written to
   `docs/work/<task>/` at every phase boundary from the start — a band warning
   should normally be a confirmation, not a scramble.
3. **Resume from disk.** A fresh session starts by reading
   `docs/work/<task>/handoff.md` plus the phase artifacts — never by replaying
   old conversation history.

### Quality gates (hard rules)

1. **TDD ordering** (for testable logic): failing tests are authored and shown
   red *before* the Python/build code that satisfies them is written.
2. **Green + frozen before done**: no task is "done" until `uv run pytest`
   passes *and*, when the change affects templates/routes/content, the freeze
   (`uv run python freeze.py`) builds clean. The reviewer re-runs both rather
   than trusting the implementer's claim. When a change touches infra
   (`infra/*.bicep*`) or the deploy workflow, `scripts/validate-infra.sh` (a
   local `az bicep build-params` compile, no Azure needed) must also pass and
   the reviewer re-runs it — a param-file/command-shape mismatch such as BCP258
   is caught here, not at deploy.
3. **Independent review**: the reviewer gets a fresh context with only the diff
   and the plan — never the implementer's transcript.
4. **Human gates**: the plan needs explicit human approval before build, and
   nothing is committed, pushed, or deployed without explicit human go-ahead.
5. **Attack-surface gate**: no change ships that adds a backend-state surface or
   an external/network dependency (see "The attack-surface rule" above).

## Role card index

- `agents/orchestrator.md` — main-session behavior: routing, gates, dispatch prompts
- `agents/scout.md` — read-only recon (haiku)
- `agents/planner.md` — implementation plans (top)
- `agents/test-writer.md` — red phase: failing tests for Python/build logic (sonnet)
- `agents/implementer.md` — green phase + JSX→Jinja/CSS translation (sonnet)
- `agents/reviewer.md` — independent diff review; re-runs pytest + freeze (top)
- `agents/releaser.md` — ship prep: freeze/deploy-wiring/docs drift (sonnet)
- `agents/retrospective.md` — post-ship agent-performance review (top)

<!-- SPECKIT START -->
For additional context about technologies to be used, project structure,
shell commands, and other important information, read the current plan:
`specs/001-static-site/plan.md` (with `research.md`, `data-model.md`,
`contracts/`, and `quickstart.md` alongside it).
<!-- SPECKIT END -->
