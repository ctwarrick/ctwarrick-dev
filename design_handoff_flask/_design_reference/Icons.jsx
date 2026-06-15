/* Lucide-style icon set (24×24, 2px stroke, round caps) — themeable via currentColor.
   The brand standardizes on Lucide; for production, swap to the lucide CDN. */
const _i = (paths, extra = {}) => ({ size, strokeWidth, style, ...props } = {}) =>
  React.createElement(
    'svg',
    {
      viewBox: '0 0 24 24', width: size || 20, height: size || 20,
      fill: 'none', stroke: 'currentColor', strokeWidth: strokeWidth || 2,
      strokeLinecap: 'round', strokeLinejoin: 'round',
      'aria-hidden': 'true', ...extra, ...props, style: { flex: 'none', ...(style || {}) },
    },
    paths.map((d, i) =>
      typeof d === 'string'
        ? React.createElement('path', { d, key: i })
        : React.createElement(d.tag, { ...d.attrs, key: i })
    )
  );

const ArrowRight   = _i(['M5 12h14', 'M13 6l6 6-6 6']);
const ArrowUpRight = _i(['M7 17 17 7', 'M7 7h10v10']);
const Mail = _i([
  { tag: 'rect', attrs: { x: 3, y: 5, width: 18, height: 14, rx: 2 } },
  'm3 7 9 6 9-6',
]);
const Github = _i(['M9 19c-4.3 1.4-4.3-2.5-6-3m12 5v-3.5c0-1 .1-1.4-.5-2 2.8-.3 5.5-1.4 5.5-6a4.6 4.6 0 0 0-1.3-3.2 4.2 4.2 0 0 0-.1-3.2s-1.1-.3-3.5 1.3a12 12 0 0 0-6.2 0C6.5 2.8 5.4 3.1 5.4 3.1a4.2 4.2 0 0 0-.1 3.2A4.6 4.6 0 0 0 4 9.5c0 4.6 2.7 5.7 5.5 6-.6.6-.6 1.2-.5 2V21']);
const Linkedin = _i([
  'M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6z',
  { tag: 'rect', attrs: { x: 2, y: 9, width: 4, height: 12 } },
  { tag: 'circle', attrs: { cx: 4, cy: 4, r: 2 } },
]);
const Sun = _i([
  { tag: 'circle', attrs: { cx: 12, cy: 12, r: 4 } },
  'M12 2v2', 'M12 20v2', 'm4.9 4.9 1.4 1.4', 'm17.7 17.7 1.4 1.4',
  'M2 12h2', 'M20 12h2', 'm6.3 17.7-1.4 1.4', 'm19.1 4.9-1.4 1.4',
]);
const Moon = _i(['M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9z']);
const Menu = _i(['M4 6h16', 'M4 12h16', 'M4 18h16']);
const X = _i(['M18 6 6 18', 'm6 6 12 12']);
const MapPin = _i(['M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z', { tag: 'circle', attrs: { cx: 12, cy: 10, r: 3 } }]);
const FileText = _i([
  'M14 3v4a1 1 0 0 0 1 1h4',
  'M17 21H7a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h7l5 5v11a2 2 0 0 1-2 2z',
  'M9 9h1', 'M9 13h6', 'M9 17h6',
]);
const Terminal = _i(['m4 17 6-6-6-6', 'M12 19h8']);
const Users = _i([
  'M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2',
  { tag: 'circle', attrs: { cx: 9, cy: 7, r: 4 } },
  'M22 21v-2a4 4 0 0 0-3-3.9', 'M16 3.1a4 4 0 0 1 0 7.8',
]);
const GitBranch = _i([
  { tag: 'line', attrs: { x1: 6, y1: 3, x2: 6, y2: 15 } },
  { tag: 'circle', attrs: { cx: 18, cy: 6, r: 3 } },
  { tag: 'circle', attrs: { cx: 6, cy: 18, r: 3 } },
  'M18 9a9 9 0 0 1-9 9',
]);
const Gauge = _i(['m12 14 4-4', 'M3.34 19a10 10 0 1 1 17.32 0']);
const Anchor = _i([
  { tag: 'circle', attrs: { cx: 12, cy: 5, r: 3 } },
  { tag: 'line', attrs: { x1: 12, y1: 22, x2: 12, y2: 8 } },
  'M5 12H2a10 10 0 0 0 20 0h-3',
]);
const Clock = _i([{ tag: 'circle', attrs: { cx: 12, cy: 12, r: 9 } }, 'M12 7v5l3 2']);
const ArrowLeft = _i(['M19 12H5', 'M11 18l-6-6 6-6']);
const Plane = _i(['M17.8 19.2 16 11l3.5-3.5a2.1 2.1 0 0 0-3-3L13 8 4.8 6.2a1 1 0 0 0-.9 1.7l5.6 3.3-2.1 2.1-2-.4a1 1 0 0 0-.9 1.6l1.7 1.7 1.7 1.7a1 1 0 0 0 1.6-.9l-.4-2 2.1-2.1 3.3 5.6a1 1 0 0 0 1.7-.9z']);
const Award = _i([{ tag: 'circle', attrs: { cx: 12, cy: 8, r: 6 } }, 'M15.5 12.9 17 22l-5-3-5 3 1.5-9.1']);

Object.assign(window, {
  ArrowRight, ArrowLeft, ArrowUpRight, Mail, Github, Linkedin, Sun, Moon, Menu, X,
  MapPin, FileText, Terminal, Users, GitBranch, Gauge, Anchor, Clock, Plane, Award,
});
