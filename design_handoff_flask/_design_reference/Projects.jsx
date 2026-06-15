/* Building view — the builder showcase (real projects). */
const { Kicker: PRKicker, Badge: PRBadge } = window.ChrisWarrickDesignSystem_83291a;

function ProjectCard({ p }) {
  const Icon = window[p.icon] || window.Terminal;
  return (
    <div className="proj">
      <div className="proj__top">
        <span className="proj__icon"><Icon size={22} /></span>
        <span className="proj__stack">{p.stack}</span>
      </div>
      <h3 className="proj__name">{p.name}</h3>
      <p className="proj__blurb">{p.blurb}</p>
      <div className="proj__link"><window.GitBranch size={14} /> {p.link}</div>
    </div>
  );
}

function Projects() {
  return (
    <section className="section">
      <div className="wrap">
        <div className="section__head">
          <div>
            <PRKicker index="01">Building</PRKicker>
            <h2>Tools I've actually shipped</h2>
            <p>I don't just run the meeting — I write the code the team doesn't have time to. A sample of what that looks like.</p>
          </div>
        </div>
        <div className="projgrid">
          {window.PROJECTS.map((p) => <ProjectCard key={p.id} p={p} />)}
        </div>
      </div>
    </section>
  );
}

Object.assign(window, { Projects });
