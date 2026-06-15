/* Article view — a rendered blog post. */
const { Kicker: ARKicker, Badge: ARBadge } = window.ChrisWarrickDesignSystem_83291a;

function Article({ id, onBack }) {
  const post = window.POSTS.find((p) => p.id === id) || window.POSTS[0];
  return (
    <article className="article">
      <div className="wrap">
        <div className="article__head">
          <button className="backlink" onClick={onBack}>
            <window.ArrowRight size={14} style={{ transform: 'rotate(180deg)' }} /> All writing
          </button>
          <h1>{post.title}</h1>
          <div className="article__meta">
            <ARBadge variant="teal">{post.tag}</ARBadge>
            <span><window.Clock size={13} style={{ verticalAlign: '-2px', marginRight: 5 }} />{post.read}</span>
            <span>{post.date}</span>
          </div>
        </div>
        <div className="article__body">
          <p>
            Here's a thing nobody says out loud at planning: a velocity chart is a machine for lying to
            yourself politely. Eight people argue about whether a card is a 3 or a 5, average their gut feelings,
            and call the result a forecast. It isn't. It's a vote with a spreadsheet attached.
          </p>
          <p>
            I stopped running that exercise. I point a script at the data instead, and let the team's own
            history answer the only question anyone actually cares about: <em>when?</em>
          </p>
          <h3>Measure flow, not feelings</h3>
          <p>
            Pull <code>cycle time</code> and <code>throughput</code> straight from the tracker — how long work
            actually takes to cross the board, and how much of it lands per week. Those two series embarrass you
            in useful ways. They show where work stalls, and they don't care how confident anyone felt in the room.
          </p>
          <blockquote>
            Stop using story-point voodoo and look at the data.
          </blockquote>
          <p>
            Feed throughput into a <b>Monte Carlo simulation</b> and you get a probabilistic delivery date: "85%
            chance we finish these 40 items by the 14th." That's a sentence you can take to a stakeholder without
            crossing your fingers. Layer <b>XmR process-behavior charts</b> on top and you can finally separate
            signal from noise — a genuinely slow sprint from ordinary variation — instead of overreacting to every wobble.
          </p>
          <h3>The flight-deck version</h3>
          <p>
            Naval aviation taught me that good instrumentation beats good intentions. You don't rise to the occasion
            under pressure; you fall to the level of your telemetry. Delivery is no different. Build the query once,
            point a dashboard at it, and spend planning on decisions instead of a guessing game.
          </p>
          <p>
            None of this requires a heavier process. It requires looking at the numbers you already have — and being
            willing to let them tell you something your story points were busy hiding.
          </p>
        </div>
        <div className="wrap--narrow" style={{ maxWidth: 'var(--container-md)', margin: '44px auto 0' }}>
          <div style={{ borderTop: '1px solid var(--border)', paddingTop: 22, display: 'flex', alignItems: 'center', gap: 14 }}>
            <ARKicker rule={false} tone="muted">Written by</ARKicker>
            <strong style={{ fontFamily: 'var(--font-display)' }}>Chris Warrick</strong>
            <span style={{ color: 'var(--text-muted)', fontSize: 14 }}>— TPM, occasional script author</span>
          </div>
        </div>
      </div>
    </article>
  );
}

Object.assign(window, { Article });
