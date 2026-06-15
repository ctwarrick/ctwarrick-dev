/* Loads the Chris Warrick design system tokens/stylesheet into this template page.
   Consuming projects: point `base` at the bound _ds/<folder> tree relative to this page
   — e.g. '_ds/<folder>' at the project root, or '../_ds/<folder>' one level down.
   NOTE: this page also loads the React component bundle directly via
   <script src="../../_ds_bundle.js">; repoint that to <base>/_ds_bundle.js when rebasing. */
(() => {
  const base = '../..';
  for (const p of ['styles.css']) {
    const l = document.createElement('link');
    l.rel = 'stylesheet';
    l.href = base + '/' + p;
    document.head.appendChild(l);
  }
})();
