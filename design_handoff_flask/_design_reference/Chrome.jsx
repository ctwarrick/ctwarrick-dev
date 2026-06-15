/* Header + Footer chrome for the website kit. */
const { Monogram, Button } = window.ChrisWarrickDesignSystem_83291a;

function Header({ view, onNav, theme, onToggleTheme }) {
  const active = view === 'article' ? 'writing' : view === 'service' ? 'work' : view;
  return (
    <header className="hdr">
      <div className="wrap hdr__in">
        <button className="navlink" style={{ padding: 0, background: 'none' }} onClick={() => onNav('home')} aria-label="Home">
          <Monogram variant="lockup" size="sm" role="" />
        </button>
        <nav className="hdr__nav">
          {window.NAV.map((n) => (
            <button
              key={n.id}
              className={'navlink' + (active === n.id ? ' navlink--on' : '')}
              onClick={() => onNav(n.id)}
            >
              {n.label}
            </button>
          ))}
        </nav>
        <div className="hdr__right">
          <button className="iconbtn" onClick={onToggleTheme} aria-label="Toggle theme">
            {theme === 'dark' ? <window.Sun size={18} /> : <window.Moon size={18} />}
          </button>
          <Button variant="primary" size="sm" iconRight={<window.ArrowRight size={16} />} onClick={() => onNav('contact')}>
            Get in touch
          </Button>
        </div>
      </div>
    </header>
  );
}

function Footer({ onNav }) {
  return (
    <footer className="ftr" id="contact">
      <div className="wrap ftr__in">
        <Monogram variant="lockup" size="sm" />
        <div className="ftr__social">
          <a className="iconbtn" href="#" aria-label="GitHub"><window.Github size={18} /></a>
          <a className="iconbtn" href="#" aria-label="LinkedIn"><window.Linkedin size={18} /></a>
          <a className="iconbtn" href="#" aria-label="Email"><window.Mail size={18} /></a>
        </div>
        <div className="ftr__copy">© 2026 Chris Warrick · Built on the CW system</div>
      </div>
    </footer>
  );
}

Object.assign(window, { Header, Footer });
