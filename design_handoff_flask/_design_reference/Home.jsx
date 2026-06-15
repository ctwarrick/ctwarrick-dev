/* Home view — hero, stats, selected work preview, contact band. */
const { Button: HButton, Kicker: HKicker, Stat: HStat, Badge: HBadge, Card: HCard } = window.ChrisWarrickDesignSystem_83291a;

function Hero({ onNav }) {
  return (
    <section className="hero cw-grid-bg">
      <div className="wrap hero__grid">
        <div>
          <HKicker>Technical Program Manager · Builder</HKicker>
          <h1>I make systems observable<br />and delivery <span className="accent">predictable.</span></h1>
          <p className="hero__lead">
            I'm Chris — a technical program manager who works close to the code. I use data to surface
            a team's problems and Lean to solve them, and I'll write the tooling myself when the team
            doesn't have time.
          </p>
          <div className="hero__cta">
            <HButton variant="primary" size="lg" iconRight={<window.ArrowRight size={18} />} onClick={() => onNav('work')}>
              See the work
            </HButton>
            <HButton variant="secondary" size="lg" icon={<window.Terminal size={18} />} onClick={() => onNav('building')}>
              What I'm building
            </HButton>
          </div>
          <div className="hero__meta">
            <span><window.MapPin size={14} /> Greater Seattle · open to relocation</span>
            <span><window.Anchor size={14} /> U.S. Navy veteran</span>
            <span><window.GitBranch size={14} /> github.com/ctwarrick</span>
          </div>
        </div>
        <div className="hero__portrait">
          <img src="../../assets/chris-warrick-headshot.jpg" alt="Chris Warrick" />
          <div className="hero__tickets">
            <span className="dot"></span>
            <span className="t">Open to new work</span>
          </div>
        </div>
      </div>
    </section>
  );
}

function HomeStats() {
  return (
    <section className="section section--sunken">
      <div className="wrap">
        <div className="statrow">
          {window.STATS.map((s, i) => <HStat key={i} {...s} />)}
          <div style={{ flex: 1, minWidth: 220, alignSelf: 'center' }}>
            <p style={{ color: 'var(--text-secondary)', margin: 0, fontSize: 'var(--text-sm)', lineHeight: 1.6 }}>
              Real numbers from real teams. The point isn't the figures — it's that I measure flow, not
              theater, and I can pull them myself.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}

function HomeWork({ onNav }) {
  const items = window.WORK.slice(0, 2);
  return (
    <section className="section">
      <div className="wrap">
        <div className="section__head">
          <div>
            <HKicker index="01">Right now</HKicker>
            <h2>What I'm working on</h2>
          </div>
          <HButton variant="ghost" iconRight={<window.ArrowRight size={16} />} onClick={() => onNav('work')}>
            All experience
          </HButton>
        </div>
        <div className="worklist">
          {items.map((w) => (
            <div className="work" key={w.id}>
              <div>
                <div className="work__period">{w.period}</div>
                <div className="work__org">{w.org}</div>
              </div>
              <div>
                <div className="work__head">
                  <h3 className="work__role">{w.role}</h3>
                  <HBadge variant={w.service ? 'gold' : 'teal'}>{w.tag}</HBadge>
                </div>
                <p className="work__sum">{w.summary}</p>
                <ul className="work__out">
                  {w.outcomes.map((o, i) => <li key={i}>{o}</li>)}
                </ul>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

function ContactBand({ onNav }) {
  return (
    <section className="cta cw-dot-bg">
      <div className="wrap wrap--narrow">
        <HKicker tone="gold" rule={false}>Let's talk</HKicker>
        <h2>Want delivery that's predictable — and observable?</h2>
        <p>That's the whole job. I'm equally at home debugging a pipeline, facilitating a retrospective, or briefing the C-suite.</p>
        <div className="cta__row">
          <HButton variant="gold" size="lg" icon={<window.Mail size={18} />}>christopher.t.warrick@alumni.psu.edu</HButton>
          <HButton variant="secondary" size="lg" onClick={() => onNav('building')}>See what I build</HButton>
        </div>
      </div>
    </section>
  );
}

function Home({ onNav }) {
  return (
    <React.Fragment>
      <Hero onNav={onNav} />
      <HomeStats />
      <HomeWork onNav={onNav} />
      <ContactBand onNav={onNav} />
    </React.Fragment>
  );
}

Object.assign(window, { Home });
