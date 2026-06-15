# Feature Specification: ctwarrick.dev — Public Static Personal Site

**Feature Branch**: `001-static-site`

**Created**: 2026-06-14

**Status**: Draft

**Input**: Build the public personal website for Chris Warrick from the Claude
Design handoff (`design_handoff_flask/`): translate the remaining pages,
establish the Markdown-authored blog pipeline, publish the whole site as static
HTML at a custom domain over HTTPS, with no backend-state surface and no
external/network dependency.

## Clarifications

### Session 2026-06-15

- Q: How is a post's stable URL identifier (`post_id`) derived? → A: From the Markdown filename (slug = filename without `.md`); e.g. `posts/my-post.md` → `/writing/my-post`.
- Q: What rich-content features must article bodies render? → A: Standard Markdown + fenced code blocks with build-time syntax highlighting + locally-hosted images, all resolved at build time and self-hosted (no client-side highlighter, no remote images).
- Q: Should the pipeline support unpublished/draft posts in the repo? → A: No — every `posts/*.md` file is always published; drafts are kept out of the repo or on a separate branch (no draft front-matter flag).
- Q: Which form is the canonical URL, and how is the other handled? → A: Apex `ctwarrick.dev` is canonical; `www.ctwarrick.dev` 301-redirects to it.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Visitor explores Chris's professional story (Priority: P1)

A prospective employer, client, or collaborator arrives at the site and forms a
clear picture of who Chris Warrick is: a landing page that states who he is and
what he does, a work history, the things he is currently building, and a
background/about page. They move between these pages through a persistent
navigation, on phone or desktop, in light or dark mode, and the experience feels
coherent and polished throughout.

**Why this priority**: This is the reason the site exists — to present the
person. Without these core pages there is no product. It is the minimum that
delivers value on its own.

**Independent Test**: Build and view the home, work, building, and about pages
locally; confirm each renders with the design system, the navigation links them
together with the correct active state, the theme toggle works, and the layout
adapts on a narrow viewport. Delivers a complete professional presence even
before any other story ships.

**Acceptance Scenarios**:

1. **Given** a visitor on a desktop browser, **When** they open the home page,
   **Then** they see Chris's name/identity, a summary of what he does, headline
   stats, a preview of recent work, and a call to action — all styled with the
   design system.
2. **Given** a visitor on any core page, **When** they use the navigation,
   **Then** they can reach home, work, building, and about, and the current
   page's nav item is visibly marked active.
3. **Given** a visitor on a phone-width screen, **When** they load any page,
   **Then** the layout adapts and the navigation remains usable.
4. **Given** a visitor, **When** they toggle the theme, **Then** the site
   switches between light and dark, the choice persists across pages and
   reloads, and there is no flash of the wrong theme on load.

---

### User Story 2 - Site is published live, static, and secure (Priority: P1)

A visitor reaches the site at its custom domain (`ctwarrick.dev`) over HTTPS and
every page loads as plain static content. No server is running, no database is
involved, and the page makes no request to any third-party origin. The owner
publishes updates simply by pushing to version control; the site rebuilds and
goes live automatically.

**Why this priority**: A personal site that nobody can reach delivers nothing,
and the project's whole premise is a secure, cheap, minimal-surface public site.
This story is what makes it *public* and *safe*.

**Independent Test**: Deploy the pre-rendered site; visit the custom domain in a
browser; confirm a valid HTTPS certificate, confirm via network inspection that
zero requests go to external/third-party origins, and confirm no server process
or database backs the site. Push a trivial content change and confirm it appears
live without any manual server step.

**Acceptance Scenarios**:

1. **Given** the site is deployed, **When** a visitor opens `ctwarrick.dev`,
   **Then** it loads over HTTPS with a valid certificate.
2. **Given** any page is open, **When** its network activity is inspected,
   **Then** every asset (HTML, CSS, JS, fonts, images) is served from the
   site's own origin and there are zero requests to third-party domains.
3. **Given** the owner commits a content change to the main branch, **When** the
   automated build runs, **Then** the updated static site is published with no
   manual server or database step.
4. **Given** a visitor requests a URL that does not exist, **When** the page is
   served, **Then** they receive a friendly 404 page consistent with the site
   design.

---

### User Story 3 - Visitor reads Chris's writing (Priority: P2)

A visitor browses a writing index listing Chris's posts (each with title, date,
tag, and a short excerpt), selects one, and reads the full article on its own
page with a back link to the index. The owner authors and publishes a post by
writing a single Markdown file — no code change, no admin interface.

**Why this priority**: Writing demonstrates expertise and is a primary draw for a
personal site, but the site is viable without it; it builds on the core presence.

**Independent Test**: Add a Markdown post file with front-matter and a body;
confirm it appears on the writing index and renders as a full article page
reachable by a stable URL, with the index→article→index navigation working — all
without touching application code.

**Acceptance Scenarios**:

1. **Given** one or more posts exist, **When** a visitor opens the writing page,
   **Then** they see each post's title, date, tag, and excerpt, ordered most
   recent first.
2. **Given** the writing index, **When** a visitor selects a post, **Then** they
   land on that article's page showing its title, metadata, and rendered body.
3. **Given** an article page, **When** the visitor follows the back link,
   **Then** they return to the writing index.
4. **Given** the owner adds a new Markdown post file and publishes, **When** the
   site rebuilds, **Then** the new post appears on the index and as an article
   page with no code change.
5. **Given** a request for a post identifier that does not exist, **When** the
   page is served, **Then** the visitor receives the site's 404 page.

---

### User Story 4 - Visitor reviews Chris's military service (Priority: P2)

A visitor opens a dedicated service page that presents Chris's military service
record and related highlights as a distinct narrative, reachable from the
navigation (grouped under Work).

**Why this priority**: A meaningful part of Chris's story and differentiator, but
secondary to the core professional presence and independently shippable.

**Independent Test**: Build and view the service page; confirm it renders the
service content with the design system and that the navigation marks Work active
when viewing it.

**Acceptance Scenarios**:

1. **Given** a visitor, **When** they open the service page, **Then** they see
   the service record and any service-specific highlights/stats, styled with the
   design system.
2. **Given** the service page is open, **When** the visitor looks at the
   navigation, **Then** the Work nav item is marked active.

---

### User Story 5 - Visitor gets in touch (Priority: P3)

A visitor who wants to contact Chris finds a clear way to do so that opens their
own email client — there is no on-site form that collects or stores their input.

**Why this priority**: Conversion matters, but a simple contact affordance is the
last slice and depends on the pages existing first.

**Independent Test**: From the relevant page(s)/footer, activate the contact
action and confirm it opens a pre-addressed email draft in the visitor's mail
client; confirm no form submits data to the site.

**Acceptance Scenarios**:

1. **Given** a visitor on the site, **When** they activate the contact action,
   **Then** their email client opens a new message addressed to Chris.
2. **Given** the site, **When** it is inspected for input-collecting forms,
   **Then** there are none that submit or persist visitor data.

---

### Edge Cases

- **Unknown route or unknown post identifier**: visitor sees the site's styled
  404 page, not a server error.
- **Empty writing index**: if no posts exist, the writing page renders cleanly
  with an appropriate empty state rather than breaking.
- **JavaScript disabled**: the site remains readable and navigable; the theme
  falls back to the visitor's OS preference (`prefers-color-scheme`); only the
  manual toggle is unavailable.
- **Reduced motion preference**: animations/transitions are suppressed when the
  visitor requests reduced motion.
- **Narrow viewport (below the mobile breakpoint)**: navigation remains operable.
- **Font fails to load**: text remains readable via the defined fallback stack.
- **Missing copy**: where the owner has not yet supplied text, a clearly-marked
  placeholder appears and is never auto-filled with fabricated content.
- **Broken internal link**: a link to a non-existent page is caught at build time
  and never ships.

## Requirements *(mandatory)*

### Functional Requirements

**Pages & navigation**

- **FR-001**: The site MUST provide these page types: home, work, building
  (projects), about, writing (post index), article (a single post), and service.
- **FR-002**: Every page MUST share a common header navigation and footer, and
  MUST visibly mark the active section; the article page marks Writing active and
  the service page marks Work active.
- **FR-003**: All internal navigation MUST use real, stable, shareable URLs (not
  client-side view switching), enabling deep links and browser history.
- **FR-004**: The site MUST present a friendly, on-brand 404 page for unknown
  URLs and unknown post identifiers.

**Design system & presentation**

- **FR-005**: All pages MUST render with the handoff design system — its
  components, hover states, shadows, transitions, and spacing/typographic
  tokens — at full fidelity.
- **FR-006**: The site MUST offer a light/dark theme toggle whose choice persists
  across pages and reloads and that applies before first paint (no flash of the
  wrong theme); absent a stored choice, it MUST honor the OS theme preference.
- **FR-007**: The layout MUST be responsive and the navigation MUST remain usable
  at mobile widths.
- **FR-008**: The site MUST use the three design-system typefaces (Space Grotesk,
  IBM Plex Sans, Old Timey Code) served from the site's own origin, including the
  weights and italics the design uses; it MUST NOT load fonts from any external
  service. (See Assumptions — carried-forward decision.)

**Writing / content pipeline**

- **FR-009**: Blog posts MUST be authored as individual Markdown files carrying,
  at minimum, title, date, tag, and excerpt, plus the post body. The file's name
  (without the `.md` extension) is the post's stable URL identifier (`post_id`)
  — e.g. `posts/my-post.md` is served at `/writing/my-post` — so renaming a file
  changes its URL.
- **FR-010**: Adding, editing, or removing a post MUST require only changing its
  Markdown file — no application-code change and no admin interface. Every
  `posts/*.md` file is published; there is no draft/unpublished state, so an
  unfinished post is kept out of the repo (or on a separate branch) rather than
  flagged in front-matter.
- **FR-011**: The writing index MUST list posts most-recent-first with title,
  date, tag, and excerpt; each article page MUST render the post's title,
  metadata, and formatted body and link back to the index. The Markdown renderer
  MUST support standard Markdown plus fenced code blocks with syntax highlighting
  and locally-hosted images; all such rich content MUST be resolved at build time
  and served from the site's own origin — no client-side highlighter and no
  remotely-loaded images — consistent with FR-017.

**Publication, hosting & operations**

- **FR-012**: The production site MUST be served entirely as pre-rendered static
  files — no application server runtime and no database in production.
- **FR-013**: The site MUST be reachable at the custom domain `ctwarrick.dev`
  over HTTPS with a valid, auto-renewing certificate, and `www.ctwarrick.dev`
  MUST 301-redirect to the canonical apex.
- **FR-014**: Publishing MUST happen by pushing to version control: a push to the
  main line MUST trigger an automated rebuild and deploy of the static site with
  no manual server steps. There is no CMS or admin.
- **FR-015**: The build MUST pre-render every page and post to static HTML, and
  MUST fail rather than publish if any internal link or referenced route does not
  resolve.

**Attack-surface & privacy invariants (from the constitution)**

- **FR-016**: The site MUST NOT include any backend-state surface — no server
  application logic in production, no database, no user accounts/logins, no
  comments, and no form or endpoint that accepts and persists visitor input.
- **FR-017**: The site MUST NOT load or call any external/third-party resource —
  no third-party scripts, trackers, analytics, CDN-hosted assets, or remote
  network calls; all assets are served from the site's own origin.
- **FR-018**: Any client-side script MUST be self-contained and
  presentation-only (no network calls, no external source, no execution of
  visitor-supplied content); the theme toggle and any optional mobile-nav toggle
  are the only expected scripts.
- **FR-019**: The contact affordance MUST work without collecting or storing
  visitor input (e.g., it opens the visitor's own email client).

**Accessibility**

- **FR-020**: Every page MUST meet a baseline of accessibility: semantic
  landmarks and heading order, keyboard operability (navigation, theme toggle,
  mobile nav) with visible focus, sufficient color contrast in both themes,
  meaningful images with alt text (decorative images marked as such), and respect
  for `prefers-reduced-motion` and `prefers-color-scheme`.

**Content ownership**

- **FR-021**: All site copy (page text and post bodies) is the owner's; where
  text is not yet supplied, the site MUST show a clearly-marked placeholder/TODO
  and MUST NOT contain fabricated biography, metrics, or post content.

**Security of the delivery pipeline**

- **FR-022**: Deployment credentials and cloud identifiers MUST NOT be committed
  to the repository; they live only in the build system's secret store.

### Key Entities

- **Site**: global identity and metadata (name, tagline, contact email, social
  links) and the navigation structure shown on every page.
- **Navigation item**: a labeled link to a page, with the rule for which section
  it activates (service → Work, article → Writing).
- **Work entry**: a role/position with organization, period, summary, and tag;
  the work page shows the full list, the home page a recent subset.
- **Project**: a thing Chris is building, with name, description, tech/stack
  note, and an optional link (the building page).
- **Service record**: Chris's military service narrative plus related
  highlight/stat figures (the service page).
- **Skill / Certification**: grouped capability and credential items (the about
  page).
- **Post**: a blog article identified by a stable id derived from its Markdown
  filename (the slug is the filename without `.md`; e.g. `posts/my-post.md` →
  `/writing/my-post`), with front-matter (title, date, tag, excerpt) and a
  Markdown body; powers both the writing index and the article page.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: All seven page types (home, work, building, about, writing,
  article, service) plus a 404 page are reachable and render correctly.
- **SC-002**: Loading any page results in **zero** requests to third-party or
  external origins (every asset comes from the site's own origin).
- **SC-003**: The production site runs with **zero** server processes and **zero**
  databases (cost and operational profile of pure static hosting).
- **SC-004**: The site is reachable at `ctwarrick.dev` over HTTPS with a valid
  certificate, with no certificate warnings.
- **SC-005**: A content change pushed to the main line is live on the public site
  within 10 minutes, with no manual server or database action.
- **SC-006**: Publishing a new blog post requires adding exactly one Markdown file
  and no code changes for it to appear on the index and as an article page.
- **SC-007**: Every page is fully operable with a keyboard alone, and text/UI
  meets WCAG AA contrast in both light and dark themes.
- **SC-008**: The theme toggle persists the visitor's choice across pages and
  reloads with no visible flash of the wrong theme on load.
- **SC-009**: No deployment secret or cloud credential is present anywhere in the
  repository's tracked files.
- **SC-010**: A build that contains a broken internal link or unresolved page
  reference fails and does not publish (0 broken internal links reach
  production).

## Assumptions

- **Hosting (locked decision)**: production hosting is Azure Static Web Apps
  (Free tier covers custom domain + managed TLS); the site is authored in a
  templating framework and pre-rendered to static HTML at build time, then
  deployed via the project's CI. Specific tooling is chosen in the plan phase.
- **Registrar / DNS**: the domain `ctwarrick.dev` is registered at GoDaddy. The
  canonical form is the apex `ctwarrick.dev`, with `www.ctwarrick.dev`
  301-redirecting to it (confirmed 2026-06-15). The specific DNS records that
  achieve this remain an infra decision for planning (GoDaddy does not natively
  flatten apex records).
- **Infrastructure**: cloud resources are provisioned as code into a **new**
  resource group within the existing tenant/subscription; resource group name and
  region are set during planning.
- **Contact mechanism**: contact uses a `mailto:` link to the owner's address
  (no on-site form), consistent with the no-input-surface rule.
- **Fonts (carried-forward decision, verified 2026-06-14)**: Space Grotesk and
  IBM Plex Sans are self-hosted (SIL OFL 1.1) alongside the already-self-hosted
  Old Timey Code; the design handoff's Google Fonts `@import` is removed. Self-
  hosting must include Space Grotesk 400/500/600/700 and IBM Plex Sans
  400/500/600/700 plus italic 400/500 so no styles regress.
- **Source of truth for unbuilt pages**: the design reference prototype
  (`_design_reference/*.jsx`) and the worked Flask example page define the visual
  and structural target; the remaining six pages are translated to match.
- **Content**: existing handoff copy is illustrative placeholder; the owner
  supplies final copy. Pages ship with marked TODO placeholders where final copy
  is pending rather than fabricated text.
- **SEO/meta**: each page carries static, self-contained metadata (title,
  description, and social-preview tags) with no external/analytics dependency.
- **Audience/scale**: a low-traffic personal site; static hosting comfortably
  covers expected load with no performance tuning beyond standard static-asset
  delivery.
