# Website UI Kit — Chris Warrick

An interactive, light/dark personal site built entirely on the CW design system. This is the flagship surface — the home, work, about, and writing experience a hiring manager or client would land on.

## Run it
Open `index.html`. Use the nav to move between **Home · Work · About · Writing**, open any post into the **Article** reader, and toggle **light/dark** with the sun/moon button (persists to `localStorage`).

## Screens
- **Home** (`Home.jsx`) — hero with headshot + availability pill, outcome stats, a 2-item work preview, and a gold contact band.
- **Work** (`Work.jsx`) — full experience list, period/org rail + outcomes, service entry tagged in gold.
- **About** (`About.jsx`) — bio in Chris's voice, light-touch veteran framing, skills as badges.
- **Writing** (`Writing.jsx`) — blog index with a featured (navy/blueprint) card + post list.
- **Article** (`Article.jsx`) — long-form reader with blockquote, inline code, byline.

## Composition
- Chrome (`Chrome.jsx`) and content sections consume bundled primitives: `Monogram`, `Button`, `Card`, `Badge`, `Kicker`, `Stat`, `Avatar`.
- `Icons.jsx` — Lucide-style 24px/2px stroke icon set, themeable via `currentColor`.
- `Data.jsx` — all copy/content (placeholder, in-voice).
- `site.css` — kit-local layout (hero, sections, work list, article). Brand tokens come from root `styles.css`.

## ⚠️ Content is illustrative
Work history, metrics, post text, and the email are placeholders written to demonstrate tone. Replace with Chris's real history before publishing.
