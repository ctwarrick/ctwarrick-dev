/* Service view — the full Naval Aviation record. Reached on click (Work + About),
   never surfaced in primary nav. Detailed, but tucked away by design. */
const { Kicker: SVKicker } = window.ChrisWarrickDesignSystem_83291a;

function ServiceRole({ r }) {
  const Icon = window[r.icon] || window.Anchor;
  return (
    <div className="work">
      <div>
        <div className="work__period">{r.period}</div>
        <div className="work__org">{r.org}</div>
      </div>
      <div>
        <div className="work__head">
          <h3 className="work__role svrole"><span className="svrole__icon"><Icon size={18} /></span>{r.role}</h3>
        </div>
        <p className="work__sum">{r.summary}</p>
        <ul className="work__out">
          {r.outcomes.map((o, i) => <li key={i}>{o}</li>)}
        </ul>
      </div>
    </div>
  );
}

function Service({ onNav }) {
  const s = window.SERVICE;
  return (
    <section className="section">
      <div className="wrap">
        <button className="backlink" style={{ marginBottom: 26 }} onClick={() => onNav('work')}>
          <window.ArrowLeft size={14} /> Back to the work
        </button>
        <div className="section__head" style={{ marginBottom: 30 }}>
          <div>
            <SVKicker index="01" tone="gold">Service Record · {s.span}</SVKicker>
            <h2>Twenty years in Naval Aviation.</h2>
            <p style={{ maxWidth: '62ch' }}>{s.intro}</p>
          </div>
        </div>
        <div className="svstats">
          {s.headline.map((h, i) => (
            <div className="svstat" key={i}>
              <div className="svstat__v">{h.value}</div>
              <div className="svstat__l">{h.label}</div>
            </div>
          ))}
        </div>
        <div className="worklist" style={{ marginTop: 26 }}>
          {s.roles.map((r) => <ServiceRole key={r.id} r={r} />)}
        </div>
        <p className="svnote">
          Proud of it — just not the headline.{' '}
          <button className="inlinelink" onClick={() => onNav('work')}>Back to what I do now →</button>
        </p>
      </div>
    </section>
  );
}

Object.assign(window, { Service });
