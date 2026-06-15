---
title: "Stop the story-point voodoo. Look at the data."
date: 2026-05-01
tag: "Forecasting"
excerpt: "Velocity is a ritual that lets a team lie to itself politely. Monte Carlo simulation and XmR process-behavior charts answer the only question that matters — \"when?\" — with evidence instead of a vote."
read: "6 min"
featured: true
---

Here's a thing nobody says out loud at planning: a velocity chart is a machine for lying to
yourself politely. Eight people argue about whether a card is a 3 or a 5, average their gut feelings,
and call the result a forecast. It isn't. It's a vote with a spreadsheet attached.

I stopped running that exercise. I point a script at the data instead, and let the team's own
history answer the only question anyone actually cares about: *when?*

### Measure flow, not feelings

Pull `cycle time` and `throughput` straight from the tracker — how long work
actually takes to cross the board, and how much of it lands per week. Those two series embarrass you
in useful ways. They show where work stalls, and they don't care how confident anyone felt in the room.

> Stop using story-point voodoo and look at the data.

Feed throughput into a **Monte Carlo simulation** and you get a probabilistic delivery date: "85%
chance we finish these 40 items by the 14th." That's a sentence you can take to a stakeholder without
crossing your fingers. Layer **XmR process-behavior charts** on top and you can finally separate
signal from noise — a genuinely slow sprint from ordinary variation — instead of overreacting to every wobble.

### The flight-deck version

Naval aviation taught me that good instrumentation beats good intentions. You don't rise to the occasion
under pressure; you fall to the level of your telemetry. Delivery is no different. Build the query once,
point a dashboard at it, and spend planning on decisions instead of a guessing game.

None of this requires a heavier process. It requires looking at the numbers you already have — and being
willing to let them tell you something your story points were busy hiding.
