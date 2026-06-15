/* App shell — view routing + theme persistence. */
function Site() {
  const [view, setView] = React.useState('home');
  const [articleId, setArticleId] = React.useState('p1');
  const [theme, setTheme] = React.useState(() => localStorage.getItem('cw-theme') || 'light');

  React.useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('cw-theme', theme);
  }, [theme]);

  const nav = (id) => {
    if (id === 'contact') {
      setView('home');
      requestAnimationFrame(() => {
        const el = document.getElementById('contact');
        if (el) window.scrollTo({ top: el.offsetTop - 80, behavior: 'smooth' });
      });
      return;
    }
    setView(id);
    window.scrollTo({ top: 0, behavior: 'auto' });
  };

  const openArticle = (id) => { setArticleId(id); setView('article'); window.scrollTo({ top: 0 }); };

  return (
    <div className="site">
      <window.Header view={view} onNav={nav} theme={theme} onToggleTheme={() => setTheme(theme === 'dark' ? 'light' : 'dark')} />
      {view === 'home' && <window.Home onNav={nav} />}
      {view === 'work' && <window.Work onNav={nav} />}
      {view === 'building' && <window.Projects />}
      {view === 'about' && <window.About onNav={nav} />}
      {view === 'service' && <window.Service onNav={nav} />}
      {view === 'writing' && <window.Writing onOpen={openArticle} />}
      {view === 'article' && <window.Article id={articleId} onBack={() => nav('writing')} />}
      <window.Footer onNav={nav} />
    </div>
  );
}

ReactDOM.createRoot(document.getElementById('root')).render(<Site />);
