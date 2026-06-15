"""
content.py — all site content, ported from templates/website/Data.jsx.

This is the "data layer". Right now it is plain Python (lists of dicts),
which is the simplest thing that works and is trivial to edit. Later you
can swap any of these for a SQLite table or a Markdown/CMS source without
touching the templates — the templates only care about the shape.

Edit copy here. (You said you'd handle copywriting — this is the file.)
"""

SITE = {
    "name": "Chris Warrick",
    "role": "Technical Program Manager",
    "email": "christopher.t.warrick@alumni.psu.edu",
    "github": "github.com/ctwarrick",
    # Canonical apex domain (FR-013, specs/001-static-site/spec.md). Used to
    # build absolute URLs for Open Graph tags in the frozen output.
    "url": "https://ctwarrick.dev",
}

# Primary nav. `id` doubles as the Flask endpoint name (see app.py).
NAV = [
    {"id": "home", "label": "Home"},
    {"id": "work", "label": "Work"},
    {"id": "building", "label": "Building"},
    {"id": "about", "label": "About"},
    {"id": "writing", "label": "Writing"},
]

STATS = [
    {"value": "8", "suffix": "+ yr", "label": "Delivery at a Fortune 500", "tone": "accent"},
    {"value": "330", "suffix": "+", "label": "Ops branches enabled", "tone": "default"},
    {"value": "200", "suffix": "+", "label": "Audience, expoCon talk", "tone": "default"},
    {"value": "7", "suffix": " yr", "label": "Unbroken biweekly release cadence", "tone": "accent"},
]

SKILLS = [
    "Python", "Flask", "Azure DevOps API", "Docker", "GitHub Actions",
    "Azure Container Apps", "CI/CD", "Databricks / ETL", "SQLite",
    "Monte Carlo forecasting", "XmR / SPC", "SAFe", "Lean / Flow",
    "Theory of Constraints", "Value Stream Mapping", "Scrum",
]

CERTS = ["ICAgile ICP-ACC", "ICAgile ICP-ATF", "Certified ScrumMaster"]

# Full experience. `service: True` marks military entries — the Work page
# filters these OUT of the civilian timeline and links to the Service page.
WORK = [
    {
        "id": "w0", "period": "2026", "role": "Builder — Independent Projects",
        "org": "Self-directed", "tag": "Building",
        "summary": "Designing and shipping spec-driven, AI-assisted tooling. Most recent: a job-search agent that pulls postings straight from ATS boards, scores them with an LLM against a written profile, and emails a ranked daily digest.",
        "outcomes": [
            "Registry-driven ingestion → normalized SQLite with hash dedup",
            "LLM scoring with a category-risk axis, send-once tracking",
            "github.com/ctwarrick/job-agent",
        ],
    },
    {
        "id": "w1", "period": "Jan 2022 — Jun 2026", "role": "Project Manager III",
        "org": "Expeditors · Federal Way, WA", "tag": "Delivery",
        "summary": "Steered a legacy-to-migrated messaging middleware team through return-to-office and the aftermath of a major cyberattack while holding a reliable release cadence — then stood up a new COBOL-to-Databricks ETL team.",
        "outcomes": [
            "Built a Flask/SQLite dashboard over 150+ servers after a Chef failure pushed stale versions to prod — one-click \"what's running where,\" faster triage, lower MTTR",
            "Replaced story-point guesswork with Monte Carlo forecasts + XmR process-behavior charts off the Azure DevOps API",
            "Migrated the Flask apps to Azure Container Apps with some of the company's first GitHub Actions CI/CD pipelines",
            "Co-authored the department-wide Scrum Master performance standards and Lean-Agile Foundations curriculum",
        ],
    },
    {
        "id": "w2", "period": "Jan 2018 — Jan 2022", "role": "Project Manager II",
        "org": "Expeditors · Seattle, WA", "tag": "Delivery",
        "summary": "Coached four teams (test automation, legacy-migration middleware, reference-data ETL, freight accounting) through the company's SAFe adoption and the 2020 shift to fully remote.",
        "outcomes": [
            "Took the middleware team to a biweekly release cadence sustained seven straight years — enabling 330+ operations branches worldwide",
            "Built a Python bot for recurring Azure DevOps admin; forked by teams in Europe into an ongoing automation effort",
            "Mentored a career-changer into her first Scrum Master role — she's now a Release Train Engineer",
        ],
    },
    {
        "id": "w3", "period": "2003 — 2023", "role": "Naval Flight Officer & Aviator",
        "org": "United States Navy", "tag": "Service", "service": True,
        "summary": "EA-6B Prowler NFO who rose to unit second-in-command and served as an Electronic Warfare Planner for a joint special operations task force. Where \"exacting\" stopped being a personality trait and became a habit.",
        "outcomes": [
            "1,094 flight hours · 16 missions over Afghanistan · 151 carrier arrested landings",
            "Directly supervised 4 line managers and teams up to 43 personnel; briefed up to a four-star Admiral",
            "Sole Navy electronic-attack SME at a JSOTF HQ; won buy-in from flag-level leadership",
        ],
    },
]

# Convenience view: the civilian timeline the Work page renders.
WORK_CIVILIAN = [w for w in WORK if not w.get("service")]

PROJECTS = [
    {
        "id": "pr1", "name": "Job Search Agent", "stack": "Python · Claude · SQLite · SMTP",
        "icon": "terminal", "link": "github.com/ctwarrick/job-agent",
        "blurb": "A multi-stage pipeline that turns job-board noise into signal: ATS ingestion adapters, fingerprint dedup, LLM scoring against a candidate profile, and a ranked daily email digest.",
    },
    {
        "id": "pr2", "name": "Delivery Forecasting Dashboards", "stack": "Flask · Azure DevOps API · NumPy",
        "icon": "gauge", "link": "Internal · Expeditors",
        "blurb": "Monte Carlo simulation and XmR statistical process control over live Azure DevOps data — cycle-time scatterplots, throughput, and probabilistic \"when will it ship?\" forecasts. Replaces story-point voodoo with evidence.",
    },
    {
        "id": "pr3", "name": "Server Observability Dashboard", "stack": "Flask · SQLite",
        "icon": "git-branch", "link": "Internal · Expeditors",
        "blurb": "Aggregated status across 150+ production and pre-production servers into one view, so on-call engineers stop hunting page-by-page and get instant situational awareness at 3 AM.",
    },
    {
        "id": "pr4", "name": "Augmented Reality Experiments", "stack": "HoloLens 2 · Unity",
        "icon": "anchor", "link": "github.com/ctwarrick",
        "blurb": "Spatial-interaction prototypes — shape spawning, holographic freight tracking, and a work-in-progress HoloChess. Exploring what it means to make information inhabit physical space.",
    },
]

# The tucked-away Naval Aviation record (its own page, not in primary nav).
SERVICE = {
    "span": "2003 — 2023",
    "intro": "Twenty years as a Naval Flight Officer — ending as a unit second-in-command and a joint-task-force electronic-warfare planner. It's where “exacting” stopped being a personality trait and became a habit, the same instinct I now point at delivery pipelines. The full record, since you clicked through for it.",
    "headline": [
        {"value": "1,094", "label": "Flight hours"},
        {"value": "151", "label": "Carrier arrested landings"},
        {"value": "16", "label": "Combat missions, Afghanistan"},
        {"value": "43", "label": "Personnel led"},
    ],
    "roles": [
        {
            "id": "s1", "period": "Flying tours", "icon": "plane",
            "role": "EA-6B Prowler Naval Flight Officer",
            "org": "Carrier-based Electronic Attack Squadron",
            "summary": "Flew the Navy's electronic-attack mission from the carrier — jamming, suppression of enemy air defenses, and the back-seat coordination that keeps a strike package alive.",
            "outcomes": [
                "1,094 flight hours in the EA-6B Prowler",
                "16 combat missions in support of operations over Afghanistan",
                "151 carrier arrested landings — day and night, blue-water",
            ],
        },
        {
            "id": "s2", "period": "Senior tour", "icon": "users",
            "role": "Unit Second-in-Command", "org": "United States Navy",
            "summary": "Rose to second-in-command of the unit — accountable for readiness, training, and the people, not just the flying.",
            "outcomes": [
                "Directly supervised 4 line managers and teams of up to 43 personnel",
                "Owned training, qualifications, and operational readiness for the unit",
                "Briefed up the chain to a four-star Admiral",
            ],
        },
        {
            "id": "s3", "period": "Joint tour", "icon": "gauge",
            "role": "Electronic Warfare Planner",
            "org": "Joint Special Operations Task Force",
            "summary": "Embedded at a joint special operations task force HQ as the sole Navy electronic-attack subject-matter expert — translating a niche capability for a room that didn't speak it.",
            "outcomes": [
                "Sole Navy electronic-attack SME at a JSOTF headquarters",
                "Won buy-in for electronic-attack employment from flag-level leadership",
                "Planned and synchronized electronic-warfare effects across a joint force",
            ],
        },
        {
            "id": "s4", "period": "In residence", "icon": "award",
            "role": "College of Naval Command & Staff",
            "org": "U.S. Naval War College",
            "summary": "Mid-career professional military education in strategy, joint operations, and command leadership.",
            "outcomes": ["Diploma — graduated with Highest Distinction"],
        },
    ],
}
