/* Writing view — blog index with a featured post. */
const { Kicker: WRKicker, Badge: WRBadge, Button: WRButton } = window.ChrisWarrickDesignSystem_83291a;

function Writing({ onOpen }) {
  const featured = window.POSTS.find((p) => p.featured) || window.POSTS[0];
  const rest = window.POSTS.filter((p) => p.id !== featured.id);
  return (
    <section className="section">
      <div className="wrap wrap--narrow">
        <div className="section__head" style={{ marginBottom: 28 }}>
          <div>
            <WRKicker index="01">Writing</WRKicker>
            <h2>Field notes on delivery</h2>
            <p>Opinions on shipping, process, and the occasional war story. Roughly monthly.</p>
          </div>
        </div>

        <div className="feature" onClick={() => onOpen(featured.id)}>
          <WRKicker tone="gold" rule={false}>Latest</WRKicker>
          <h3 className="feature__title">{featured.title}</h3>
          <p className="feature__excerpt">{featured.excerpt}</p>
          <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
            <WRButton variant="gold" size="sm" iconRight={<window.ArrowRight size={16} />}>Read it</WRButton>
            <span style={{ fontFamily: 'var(--font-mono)', fontSize: 12, color: '#a9c0db' }}>
              {featured.date} · {featured.read}
            </span>
          </div>
        </div>

        <div className="postlist">
          {rest.map((p) => (
            <div className="post" key={p.id} onClick={() => onOpen(p.id)}>
              <div>
                <div className="post__meta">
                  <WRBadge variant="teal">{p.tag}</WRBadge>
                  <span>{p.date}</span>
                  <span>·</span>
                  <span>{p.read}</span>
                </div>
                <h3 className="post__title">{p.title}</h3>
                <p className="post__excerpt">{p.excerpt}</p>
              </div>
              <div className="post__arrow"><window.ArrowUpRight size={22} /></div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

Object.assign(window, { Writing });
