/* Work view — full experience list. */
const { Kicker: WKicker, Badge: WBadge } = window.ChrisWarrickDesignSystem_83291a;

function WorkItem({ w }) {
  return (
    <div className="work">
      <div>
        <div className="work__period">{w.period}</div>
        <div className="work__org">{w.org}</div>
      </div>
      <div>
        <div className="work__head">
          <h3 className="work__role">{w.role}</h3>
          <WBadge variant={w.service ? 'gold' : 'teal'}>{w.tag}</WBadge>
        </div>
        <p className="work__sum">{w.summary}</p>
        <ul className="work__out">
          {w.outcomes.map((o, i) => <li key={i}>{o}</li>)}
        </ul>
      </div>
    </div>
  );
}

function Work({ onNav }) {
  const items = window.WORK.filter((w) => !w.service);
  return (
    <section className="section">
      <div className="wrap">
        <div className="section__head">
          <div>
            <WKicker index="01">Experience</WKicker>
            <h2>Getting things across the line.</h2>
            <p>Two decades of it — Naval Aviation, then a Fortune 500 delivery org, now independent builds. Same instinct throughout: clear the path, measure the flow, tell the truth about risk.</p>
          </div>
        </div>
        <div className="worklist">
          {items.map((w) => <WorkItem key={w.id} w={w} />)}
        </div>
        <button className="servicelink" onClick={() => onNav('service')}>
          <span className="svl__icon"><window.Anchor size={20} /></span>
          <span className="svl__txt">
            <b>Before the pipeline: 20 years in Naval Aviation.</b> Where the habit started — tucked away, in full, for anyone who wants it.
          </span>
          <span className="svl__cta">The service record →</span>
        </button>
      </div>
    </section>
  );
}

Object.assign(window, { Work });
