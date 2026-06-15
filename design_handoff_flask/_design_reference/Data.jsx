/* Real content for Chris (Christopher T.) Warrick. Sourced from his résumé
   and github.com/ctwarrick. Voice is his own — direct, data-driven, builder. */

const NAV = [
  { id: 'home', label: 'Home' },
  { id: 'work', label: 'Work' },
  { id: 'building', label: 'Building' },
  { id: 'about', label: 'About' },
  { id: 'writing', label: 'Writing' },
];

const STATS = [
  { value: '8', suffix: '+ yr', label: 'Delivery at a Fortune 500', tone: 'accent' },
  { value: '330', suffix: '+', label: 'Ops branches enabled', tone: 'default' },
  { value: '200', suffix: '+', label: 'Audience, exp.oCon talk', tone: 'default' },
  { value: '7', suffix: ' yr', label: 'Unbroken biweekly release cadence', tone: 'accent' },
];

const SKILLS = [
  'Python', 'Flask', 'Azure DevOps API', 'Docker', 'GitHub Actions',
  'Azure Container Apps', 'CI/CD', 'Databricks / ETL', 'SQLite',
  'Monte Carlo forecasting', 'XmR / SPC', 'SAFe', 'Lean / Flow',
  'Theory of Constraints', 'Value Stream Mapping', 'Scrum',
];

const CERTS = ['ICAgile ICP-ACC', 'ICAgile ICP-ATF', 'Certified ScrumMaster'];

const WORK = [
  {
    id: 'w0', period: '2026', role: 'Builder — Independent Projects',
    org: 'Self-directed', tag: 'Building',
    summary: 'Designing and shipping spec-driven, AI-assisted tooling. Most recent: a job-search agent that pulls postings straight from ATS boards, scores them with an LLM against a written profile, and emails a ranked daily digest.',
    outcomes: ['Registry-driven ingestion → normalized SQLite with hash dedup', 'LLM scoring with a category-risk axis, send-once tracking', 'github.com/ctwarrick/job-agent'],
  },
  {
    id: 'w1', period: 'Jan 2022 — Jun 2026', role: 'Project Manager III',
    org: 'Expeditors · Federal Way, WA', tag: 'Delivery',
    summary: 'Steered a legacy-to-migrated messaging middleware team through return-to-office and the aftermath of a major cyberattack while holding a reliable release cadence — then stood up a new COBOL-to-Databricks ETL team.',
    outcomes: [
      'Built a Flask/SQLite dashboard over 150+ servers after a Chef failure pushed stale versions to prod — one-click "what\'s running where," faster triage, lower MTTR',
      'Replaced story-point guesswork with Monte Carlo forecasts + XmR process-behavior charts off the Azure DevOps API',
      'Migrated the Flask apps to Azure Container Apps with some of the company\'s first GitHub Actions CI/CD pipelines',
      'Co-authored the department-wide Scrum Master performance standards and Lean-Agile Foundations curriculum',
    ],
  },
  {
    id: 'w2', period: 'Jan 2018 — Jan 2022', role: 'Project Manager II',
    org: 'Expeditors · Seattle, WA', tag: 'Delivery',
    summary: 'Coached four teams (test automation, legacy-migration middleware, reference-data ETL, freight accounting) through the company\'s SAFe adoption and the 2020 shift to fully remote.',
    outcomes: [
      'Took the middleware team to a biweekly release cadence sustained seven straight years — enabling 330+ operations branches worldwide',
      'Built a Python bot for recurring Azure DevOps admin; forked by teams in Europe into an ongoing automation effort',
      'Mentored a career-changer into her first Scrum Master role — she\'s now a Release Train Engineer',
    ],
  },
  {
    id: 'w3', period: '2003 — 2023', role: 'Naval Flight Officer & Aviator',
    org: 'United States Navy', tag: 'Service', service: true,
    summary: 'EA-6B Prowler NFO who rose to unit second-in-command and served as an Electronic Warfare Planner for a joint special operations task force. Where "exacting" stopped being a personality trait and became a habit.',
    outcomes: [
      '1,094 flight hours · 16 missions over Afghanistan · 151 carrier arrested landings',
      'Directly supervised 4 line managers and teams up to 43 personnel; briefed up to a four-star Admiral',
      'Sole Navy electronic-attack SME at a JSOTF HQ; won buy-in from flag-level leadership',
    ],
  },
];

const PROJECTS = [
  {
    id: 'pr1', name: 'Job Search Agent', stack: 'Python · Claude · SQLite · SMTP',
    icon: 'Terminal', link: 'github.com/ctwarrick/job-agent',
    blurb: 'A multi-stage pipeline that turns job-board noise into signal: ATS ingestion adapters, fingerprint dedup, LLM scoring against a candidate profile, and a ranked daily email digest.',
  },
  {
    id: 'pr2', name: 'Delivery Forecasting Dashboards', stack: 'Flask · Azure DevOps API · NumPy',
    icon: 'Gauge', link: 'Internal · Expeditors',
    blurb: 'Monte Carlo simulation and XmR statistical process control over live Azure DevOps data — cycle-time scatterplots, throughput, and probabilistic "when will it ship?" forecasts. Replaces story-point voodoo with evidence.',
  },
  {
    id: 'pr3', name: 'Server Observability Dashboard', stack: 'Flask · SQLite',
    icon: 'GitBranch', link: 'Internal · Expeditors',
    blurb: 'Aggregated status across 150+ production and pre-production servers into one view, so on-call engineers stop hunting page-by-page and get instant situational awareness at 3 AM.',
  },
  {
    id: 'pr4', name: 'Augmented Reality Experiments', stack: 'HoloLens 2 · Unity',
    icon: 'Anchor', link: 'github.com/ctwarrick',
    blurb: 'Spatial-interaction prototypes — shape spawning, holographic freight tracking, and a work-in-progress HoloChess. Exploring what it means to make information inhabit physical space.',
  },
];

const POSTS = [
  {
    id: 'p1', title: 'Stop the story-point voodoo. Look at the data.',
    date: 'May 2026', read: '6 min', tag: 'Forecasting', featured: true,
    excerpt: 'Velocity is a ritual that lets a team lie to itself politely. Monte Carlo simulation and XmR process-behavior charts answer the only question that matters — "when?" — with evidence instead of a vote.',
  },
  {
    id: 'p2', title: 'At 3 AM you fall to the level of your telemetry',
    date: 'Mar 2026', read: '7 min', tag: 'Observability',
    excerpt: 'You don\'t rise to the occasion on-call; you fall to the level of your observability. Build the dashboard that makes system state legible at a glance, and stop inviting shoulder-taps from senior leadership.',
  },
  {
    id: 'p3', title: 'Automate the paperwork away',
    date: 'Feb 2026', read: '5 min', tag: 'Lean',
    excerpt: 'Find the bottleneck. Fix it. Find the new bottleneck. Most of mine turned out to be a manual QA gate and a change-order form — so I wrote the REST API automation that deleted them.',
  },
  {
    id: 'p4', title: 'A Scrum Master is not a ceremony facilitator',
    date: 'Jan 2026', read: '6 min', tag: 'Craft',
    excerpt: 'The most useful thing a TPM can do is decrease friction and toil and bake "doing the right thing" into the architecture itself. Anything else, to borrow from the Red Baron, is rubbish.',
  },
];

const SERVICE = {
  span: '2003 — 2023',
  intro: 'Twenty years as a Naval Flight Officer — ending as a unit second-in-command and a joint-task-force electronic-warfare planner. It’s where “exacting” stopped being a personality trait and became a habit, the same instinct I now point at delivery pipelines. The full record, since you clicked through for it.',
  headline: [
    { value: '1,094', label: 'Flight hours' },
    { value: '151', label: 'Carrier arrested landings' },
    { value: '16', label: 'Combat missions, Afghanistan' },
    { value: '43', label: 'Personnel led' },
  ],
  roles: [
    {
      id: 's1', period: 'Flying tours', icon: 'Plane',
      role: 'EA-6B Prowler Naval Flight Officer',
      org: 'Carrier-based Electronic Attack Squadron',
      summary: 'Flew the Navy’s electronic-attack mission from the carrier — jamming, suppression of enemy air defenses, and the back-seat coordination that keeps a strike package alive.',
      outcomes: [
        '1,094 flight hours in the EA-6B Prowler',
        '16 combat missions in support of operations over Afghanistan',
        '151 carrier arrested landings — day and night, blue-water',
      ],
    },
    {
      id: 's2', period: 'Senior tour', icon: 'Users',
      role: 'Unit Second-in-Command',
      org: 'United States Navy',
      summary: 'Rose to second-in-command of the unit — accountable for readiness, training, and the people, not just the flying.',
      outcomes: [
        'Directly supervised 4 line managers and teams of up to 43 personnel',
        'Owned training, qualifications, and operational readiness for the unit',
        'Briefed up the chain to a four-star Admiral',
      ],
    },
    {
      id: 's3', period: 'Joint tour', icon: 'Gauge',
      role: 'Electronic Warfare Planner',
      org: 'Joint Special Operations Task Force',
      summary: 'Embedded at a joint special operations task force HQ as the sole Navy electronic-attack subject-matter expert — translating a niche capability for a room that didn’t speak it.',
      outcomes: [
        'Sole Navy electronic-attack SME at a JSOTF headquarters',
        'Won buy-in for electronic-attack employment from flag-level leadership',
        'Planned and synchronized electronic-warfare effects across a joint force',
      ],
    },
    {
      id: 's4', period: 'In residence', icon: 'Award',
      role: 'College of Naval Command & Staff',
      org: 'U.S. Naval War College',
      summary: 'Mid-career professional military education in strategy, joint operations, and command leadership.',
      outcomes: [
        'Diploma — graduated with Highest Distinction',
      ],
    },
  ],
};

Object.assign(window, { NAV, STATS, SKILLS, CERTS, WORK, PROJECTS, POSTS, SERVICE });
