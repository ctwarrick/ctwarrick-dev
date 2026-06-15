/* About view — real bio in Chris's voice, service framing, skills, education. */
const { Kicker: ABKicker, Badge: ABBadge, Button: ABButton } = window.ChrisWarrickDesignSystem_83291a;

function About({ onNav }) {
  return (
    <section className="section">
      <div className="wrap">
        <div className="section__head" style={{ marginBottom: 40 }}>
          <div>
            <ABKicker index="01">About</ABKicker>
            <h2>Ship the work, not the ritual.</h2>
          </div>
        </div>
        <div className="about">
          <div className="about__photo">
            <img src="../../assets/chris-warrick-headshot.jpg" alt="Chris Warrick" />
            <div className="skillgrid" style={{ marginTop: 16 }}>
              <ABBadge variant="gold">U.S. Navy Veteran</ABBadge>
              <ABBadge variant="blue" dot>Open to work</ABBadge>
            </div>
          </div>
          <div>
            <p className="about__lede">
              Ex-Expeditors Global Technology, ex-Naval Aviation. A technical program manager and
              builder who works close to the code.
            </p>
            <p>
              I have a passion for using <b>data to surface a team's problems</b>, Lean and Agile principles
              to help solve them, and for doing whatever it takes to make that happen — whether that's dealing
              with people or getting my hands dirty writing the code my team doesn't have time to write. (Though
              I'm not above enlisting AI agents so my hands don't get quite so dirty these days.)
            </p>
            <p>
              I'm drawn to the seam between <b>delivery and engineering</b>: Monte Carlo forecasting and XmR
              process-behavior charts instead of story-point voodoo; REST API automation and CI/CD coupled to
              Value Stream Mapping and Theory of Constraints; dashboards that make system state legible at a glance.
              On call at 3 AM, you don't rise to the occasion — you fall to the level of your telemetry.
            </p>
            <p>
              My thesis: the most useful thing a TPM can do is <b>decrease friction and toil</b> and help build a
              system where doing the right thing is easy and baked into the architecture itself. Frameworks can help
              or hinder that. Use them appropriately.
            </p>
            <p>
              Before all of this I flew. EA-6B Prowler Naval Flight Officer — <b>1,094 flight hours, 16 missions over
              Afghanistan, 151 carrier arrested landings</b> — who rose to unit second-in-command and briefed up to a
              four-star Admiral. I'm proud of the service. I just don't lead with it. <button className="inlinelink" onClick={() => onNav('service')}>The full service record →</button>
            </p>

            <div style={{ marginTop: 30 }}>
              <ABKicker rule={false} tone="muted">Skills & tooling</ABKicker>
              <div className="skillgrid" style={{ marginTop: 14 }}>
                {window.SKILLS.map((s, i) => <ABBadge key={i} variant="neutral" solid>{s}</ABBadge>)}
              </div>
            </div>

            <div style={{ marginTop: 26 }}>
              <ABKicker rule={false} tone="muted">Certifications</ABKicker>
              <div className="skillgrid" style={{ marginTop: 14 }}>
                {window.CERTS.map((c, i) => <ABBadge key={i} variant="teal">{c}</ABBadge>)}
              </div>
            </div>

            <div style={{ marginTop: 26 }}>
              <ABKicker rule={false} tone="muted">Education</ABKicker>
              <ul style={{ listStyle: 'none', margin: '14px 0 0', padding: 0, display: 'flex', flexDirection: 'column', gap: 10 }}>
                <li><b style={{ fontFamily: 'var(--font-display)' }}>M.S., Information Science</b> — Penn State <span style={{ color: 'var(--text-muted)', fontFamily: 'var(--font-mono)', fontSize: 13 }}>· expected 2027</span></li>
                <li><b style={{ fontFamily: 'var(--font-display)' }}>B.S., Information Sciences & Technology</b> — Penn State</li>
                <li><b style={{ fontFamily: 'var(--font-display)' }}>Diploma, College of Naval Command & Staff</b> — U.S. Naval War College <span style={{ color: 'var(--gold-700)', fontFamily: 'var(--font-mono)', fontSize: 13 }}>· Highest Distinction</span></li>
              </ul>
            </div>

            <div style={{ marginTop: 32, display: 'flex', gap: 12, flexWrap: 'wrap' }}>
              <ABButton variant="primary" icon={<window.FileText size={18} />} onClick={() => onNav('work')}>See the work</ABButton>
              <ABButton variant="secondary" icon={<window.Mail size={18} />} onClick={() => onNav('contact')}>Get in touch</ABButton>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

Object.assign(window, { About });
