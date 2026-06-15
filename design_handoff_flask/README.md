# Bridge guide: design → Flask on Azure Web Apps

This package turns the HTML/React design prototype into a runnable Flask
app skeleton, and documents every decision in between. It's a **bridge**,
not a finished app: the visual layer and the tedious mechanical
translations are done for you; the routing/wiring of the remaining pages
is yours (it's repetitive and you're well-equipped for it).

> **Copy is yours.** All text lives in `content.py`. Rewrite it there.
> I'm a designer, not a copywriter — I carried the current words across
> verbatim so nothing breaks; swap them freely.

---

## 1. The big idea (why this port is cheap)

The design is a **content site with essentially no app-state**: navigation,
a theme toggle, and static content. That makes server-side rendering the
natural fit, and it means **~95% of the design carries over unchanged**:

| Layer | In the design | In Flask | Effort |
|---|---|---|---|
| Design tokens (color, type, spacing) | `styles.css` + `tokens/*.css` | same files, copied to `static/css/` | **none** |
| Page layout CSS | `site.css` | copied to `static/css/` | **none** |
| Component **styles** | injected by JS at runtime | extracted to `components.css` | **done for you** |
| Component **markup** | React components | Jinja macros (`_macros.html`) | **done for you** |
| Content/data | `Data.jsx` | `content.py` | **done for you** |
| Page structure | `*.jsx` views | Jinja templates | **you** (1 done as example) |
| Routing | React `useState` view switch | Flask routes | **you** (skeleton provided) |
| Interactivity | theme toggle, SPA nav | theme toggle + real URLs | **done for you** |

What you are **not** doing: rebuilding the design system, re-deriving
colors, or shipping React/Babel to the browser. The compiled
`_ds_bundle.js` and all of React/Babel are dropped — Flask renders HTML.

---

## 2. Architecture: Flask + Jinja2 (server-rendered)

Render every page on the server with Jinja templates. No build step, no
Node, no client framework. Benefits over the SPA prototype:

- **Real URLs** (`/work`, `/writing/p1`) → deep links, browser history,
  and SEO that a `useState` view-switch can't give you.
- **Faster first paint**, no Babel-in-the-browser.
- One language end to end (Python), which is where your tooling already lives.

The one thing the SPA did that you re-implement: the **theme toggle**.
It's ~15 lines of vanilla JS in `base.html`, written to be FOUC-free
(reads `localStorage` before first paint).

---

## 3. Folder structure (what's in this package)

```
design_handoff_flask/
├── app.py                      # Flask routes (skeleton; /work is complete)
├── content.py                  # ALL content, ported from Data.jsx  ← edit copy here
├── requirements.txt            # Flask + gunicorn
├── startup.txt                 # Azure startup command
├── .github/workflows/
│   └── azure-webapp.yml        # CI/CD reference
├── templates/
│   ├── base.html               # shell: head, header, footer, theme toggle  ✅
│   ├── _macros.html            # DS components as Jinja macros  ✅
│   ├── work.html               # WORKED EXAMPLE (full page)  ✅
│   ├── home.html               # ⬜ you build (from _design_reference/Home.jsx)
│   ├── building.html           # ⬜ you build (Projects.jsx)
│   ├── about.html              # ⬜ you build (About.jsx)
│   ├── writing.html            # ⬜ you build (Writing.jsx)
│   ├── article.html            # ⬜ you build (Article.jsx)
│   └── service.html            # ⬜ you build (Service.jsx)
├── static/
│   ├── css/
│   │   ├── styles.css          # token manifest (@imports tokens/*)
│   │   ├── components.css      # extracted cw-* component styles
│   │   ├── site.css            # page layout
│   │   └── tokens/             # fonts, colors, typography, spacing, base
│   ├── fonts/OldTimeyCode.ttf  # self-hosted mono
│   └── img/chris-warrick-headshot.jpg
└── _design_reference/          # the original prototype — your source of truth
```

---

## 4. Components → Jinja macros

The React components (`Button`, `Badge`, `Kicker`, `Stat`, `Card`,
`Monogram`, `Avatar`) are reproduced as macros in `templates/_macros.html`.
**Each macro emits the exact same class names**, so `components.css` styles
them with no changes. The prop names match too:

```jinja
{% from "_macros.html" import button, badge, kicker, stat, icon %}

{{ kicker("Experience", index="01") }}
{{ badge(w.tag, variant="teal") }}
{{ stat("1,094", label="Flight hours", tone="gold") }}
{{ button("See the work", variant="primary", size="lg",
          href=url_for("work"), icon_right=icon("arrow-right", 18)) }}
```

`Card` takes children, so it uses Jinja's `{% call %}`:

```jinja
{% from "_macros.html" import card %}
{% call card(interactive=true, ticked=true) %}
  <h3>…</h3><p>…</p>
{% endcall %}
```

### Translation cheat-sheet (React prop → macro arg)
- `<Button iconRight={<X/>}>` → `button(..., icon_right=icon("x"))`
- `variant`/`size`/`tone` → identical strings
- `<Kicker rule={false}>` → `kicker(..., rule=false)`
- `<Stat value suffix>` → `stat(value, suffix=...)`
- conditional class via prop → the macro already branches internally

---

## 5. CSS: load order and the `components.css` gotcha

In the prototype, each component **injected its own `<style>` at runtime**
(you'll see `<style data-cw="button">` in devtools). Dropping React drops
that injection — so those styles are extracted into
`static/css/components.css`. Link the three stylesheets **in this order**
(already wired in `base.html`):

```html
<link rel="stylesheet" href="…/css/styles.css">      <!-- 1. tokens -->
<link rel="stylesheet" href="…/css/components.css">  <!-- 2. components -->
<link rel="stylesheet" href="…/css/site.css">        <!-- 3. page layout -->
```

`styles.css` is just a manifest of `@import`s pulling in `tokens/*.css`;
keep the `tokens/` subfolder next to it so the relative imports resolve.

---

## 6. Fonts & assets

- **Space Grotesk** (display) and **IBM Plex Sans** (body) load from Google
  Fonts via the `@import` at the top of `tokens/fonts.css`. No action needed.
- **Old Timey Code** (mono) is self-hosted. The `@font-face` `url()` was
  repointed from `../assets/fonts/` to **`../fonts/`** to match the Flask
  `static/` layout — already done in the copied `tokens/fonts.css`.
- The headshot is at `static/img/chris-warrick-headshot.jpg`; reference it
  with `{{ url_for('static', filename='img/chris-warrick-headshot.jpg') }}`.

---

## 7. Data layer

`content.py` holds everything as plain Python lists/dicts — the simplest
thing that works and trivial to edit. The shapes match what the templates
expect. When you outgrow it:

- **SQLite** (you already reach for it): back `POSTS`/`WORK` with a table;
  the templates don't change, only `content.py`'s getters do.
- **Markdown for posts**: store article bodies as `.md`, render with
  `markdown` at request time. (The prototype's `Article.jsx` has hard-coded
  bodies — that's the one place you'll want real content plumbing.)

Note `WORK_CIVILIAN` — the Work page's filtered list (service entries
removed). The filter that lived in `Work.jsx` now lives in `content.py`.

---

## 8. Routes (React view → URL → template)

`app.py` already declares all of these. Build the ⬜ templates by
translating the matching reference file the same way `work.html` was done.

| View (JSX) | URL | Template | Status |
|---|---|---|---|
| `Home.jsx` | `/` | `home.html` | ⬜ |
| `Work.jsx` | `/work` | `work.html` | ✅ example |
| `Projects.jsx` | `/building` | `building.html` | ⬜ |
| `About.jsx` | `/about` | `about.html` | ⬜ |
| `Writing.jsx` | `/writing` | `writing.html` | ⬜ |
| `Article.jsx` | `/writing/<post_id>` | `article.html` | ⬜ |
| `Service.jsx` | `/service` | `service.html` | ⬜ |

**Nav active-state**: pass `active="work"` etc. to `render_template`; the
header underlines the match. `/service` and `/writing/<id>` map to their
parent (`work`, `writing`) — handled by `active_for()` in `app.py`.

**In-page links**: the SPA used `onNav('service')`. In Jinja that becomes
`href="{{ url_for('service') }}"`. The "Get in touch" button and footer
email use `mailto:` (the prototype's `onNav('contact')` scrolled to a
footer; with real pages a `mailto:` or a `/contact` route is cleaner).

---

## 9. What still needs client JS

Almost nothing. Two things only:

1. **Theme toggle** — done, in `base.html` (FOUC-free, persists to
   `localStorage` under `cw-theme`, same key the prototype used).
2. **Mobile nav** — the prototype hides the nav under 860px with no
   hamburger. If you want a mobile menu, that's a small `<details>` or a
   ~10-line toggle. Optional.

No other interactivity exists in the design, so there's no framework to
reach for.

---

## 10. Run it locally

```bash
cd design_handoff_flask
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
flask --app app run --debug
# visit http://127.0.0.1:5000/work  (the worked example)
```

`/work` renders fully today. The other routes 500 until you create their
templates — that's the build list.

---

## 11. Deploy to Azure Web Apps

Target: **Azure App Service** (Linux, Python 3.12), which is what "Azure
Web Apps" means for a Flask app. You've shipped Azure Container Apps + GitHub
Actions before, so this is familiar; the App Service specifics:

1. **Create** the Web App: runtime stack *Python 3.12*, OS *Linux*.
2. **Startup command** (App Service won't guess it for Flask):
   ```
   gunicorn --bind=0.0.0.0 --timeout 600 app:app
   ```
   Set under Configuration → General settings → Startup Command (also in
   `startup.txt`). `app:app` = the `app` object in `app.py`.
3. **Server-side build**: add app setting
   `SCM_DO_BUILD_DURING_DEPLOYMENT=true` so Oryx runs
   `pip install -r requirements.txt` on deploy. (Keep `requirements.txt`
   at the repo root you deploy.)
4. **Port**: App Service injects `$PORT` and gunicorn's `0.0.0.0` bind
   picks it up — you do **not** need `WEBSITES_PORT` for this setup.
5. **CI/CD**: use `.github/workflows/azure-webapp.yml` (set `APP_NAME`,
   add the `AZUREAPPSERVICE_PUBLISHPROFILE` secret), or just point
   Deployment Center at the repo and let Azure scaffold an equivalent.
6. **HTTPS / custom domain**: App Service gives you `*.azurewebsites.net`
   with TLS for free; add a custom domain + managed cert when ready.

**Observability (your wheelhouse):** turn on **Application Insights** for the
Web App — you get request traces, failure rates, and live metrics with no
code change, and can add custom telemetry later. Fits the "make system
state legible" thesis the site is literally about.

---

## 12. Suggested build order

1. `flask run`, confirm `/work` renders and the theme toggle works.
2. Translate `home.html` (hero + stats + work preview + CTA) — exercises
   `stat`, `kicker`, `button`, and the headshot asset.
3. `building.html`, `about.html` — straightforward content pages.
4. `writing.html` + `article.html` — decide your post storage here.
5. `service.html` — mirror `work.html`; it reuses the same `.work` markup
   plus the `.svstats` block (classes already in `site.css`).
6. Rewrite copy in `content.py`.
7. Wire CI/CD, deploy, enable App Insights.

Everything you need to translate each page is in `_design_reference/` —
that's the exact, working prototype these instructions describe.
