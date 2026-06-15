# Contract: URL Routes & Frozen Output

The site exposes these routes (already declared in the handoff `app.py`). Each
must translate its template from the matching `_design_reference/*.jsx`, pass
the listed context, set the correct `active` nav key, and freeze to the listed
path under `build/`.

| Endpoint | URL | Template | JSX source | `active` | Context passed | Frozen output |
|---|---|---|---|---|---|---|
| `home` | `/` | `home.html` | `Home.jsx` | `home` | `stats`, `work=WORK_CIVILIAN[:2]` | `build/index.html` |
| `work` | `/work` | `work.html` ✅ | `Work.jsx` | `work` | `work=WORK_CIVILIAN` | `build/work/index.html` |
| `building` | `/building` | `building.html` | `Projects.jsx` | `building` | `projects=PROJECTS` | `build/building/index.html` |
| `about` | `/about` | `about.html` | `About.jsx` | `about` | `skills=SKILLS, certs=CERTS` | `build/about/index.html` |
| `writing` | `/writing` | `writing.html` | `Writing.jsx` | `writing` | `posts=POSTS` | `build/writing/index.html` |
| `article` | `/writing/<post_id>` | `article.html` | `Article.jsx` | `writing` (via `active_for`) | `post` | `build/writing/<post_id>/index.html` |
| `service` | `/service` | `service.html` | `Service.jsx` | `work` (via `active_for`) | `service=SERVICE` | `build/service/index.html` |
| — (error) | 404 | `404.html` | — | n/a | — | `build/404.html` |

## Active-nav contract (FR-002)

`active_for(view)` maps `service → work`, `article → writing`; everything else
maps to itself. The header marks `navlink--on` on the matching nav item.

## URL contract (FR-003)

- All navigation uses real, shareable URLs via `url_for(endpoint)` — no
  client-side view switching.
- `article` URLs are `/writing/<post_id>` where `post_id` is the post's filename
  slug (see post-frontmatter contract).
- In-page/footer contact uses `mailto:` (FR-019). Outbound profile links
  (GitHub/LinkedIn) are plain hyperlinks the visitor clicks — not loaded
  resources.

## 404 contract (FR-004)

- Unknown route or unknown `post_id` → the styled `404.html`, on-brand with the
  design system and the shared header/footer.
- Frozen to `build/404.html`; Azure Static Web Apps serves it for not-found
  responses (see static-hosting contract).

## Freeze contract (FR-015)

- `freeze.py` emits every route above; a URL generator yields one `article` URL
  per loaded post.
- The build **fails** if any internal link/`src` does not resolve to an emitted
  file (enforced by the link-resolution test, research §5).
