/* 404 view — goofy, on-brand. Naval-aviation "foul deck waveoff" + a SQL "0 rows" gag. */
const { Button: NFButton, Kicker: NFKicker, Badge: NFBadge } = window.ChrisWarrickDesignSystem_83291a;

function Terminal404() {
  return (
    <div className="term404" role="img" aria-label="A database query that returned zero rows">
      <div className="term404__bar">
        <span className="term404__dot"></span>
        <span className="term404__dot"></span>
        <span className="term404__dot"></span>
        <span className="term404__title">chris@flightdeck — psql</span>
      </div>
      <div className="term404__body">
        <p><span className="term404__prompt">cw=&gt;</span> SELECT * FROM pages</p>
        <p className="term404__indent">WHERE url = <span className="term404__str">'the-one-you-wanted'</span>;</p>
        <p className="term404__out">(0 rows)</p>
        <p className="term404__cursor"><span className="term404__prompt">cw=&gt;</span> <span className="term404__blink">▋</span></p>
      </div>
    </div>
  );
}

function NotFound({ onHome }) {

  return (
    <section className="hero cw-grid-bg nf">
      <div className="wrap nf__grid">
        <div className="nf__left">
          <NFKicker>Waveoff · Foul deck · Go around</NFKicker>
          <div className="nf__digits" aria-hidden="true">
            <span>4</span>
            <span className="nf__o" title="foul deck"><window.Anchor size={null} /></span>
            <span>4</span>
          </div>
          <h1 className="nf__h1">Waveoff, waveoff . . .</h1>

          <div className="nf__diag">
            <div className="nf__diag-head">
              <NFBadge variant="gold">FOUL DECK</NFBadge>
              <span className="nf__diag-meta">Pass #01 · n=10,000</span>
            </div>
            <p className="nf__diag-text">Deck's not clear — the page you wanted isn't spotted. Waved off before the groove.</p>
          </div>

          <div className="nf__cta">
            <NFButton variant="primary" size="lg" iconRight={<window.ArrowRight size={18} />} onClick={onHome}>
              Take it around again
            </NFButton>
            <NFButton variant="secondary" size="lg" icon={<window.Mail size={18} />} onClick={onHome}>
              Tell me what broke
            </NFButton>
          </div>
        </div>

        <div className="nf__right">
          <Terminal404 />
          <p className="nf__caption">A 404 is just a query that returns no rows. This one does.</p>
        </div>
      </div>
    </section>
  );
}

Object.assign(window, { NotFound });
