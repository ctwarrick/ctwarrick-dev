"""Structured site content for the Chris Warrick personal site.

The data layer: plain Python lists and dicts (`SITE`, `NAV`, `STATS`,
`WORK`, `PROJECTS`, `SERVICE`, ...) consumed by the page templates. The
templates depend only on the shape of these structures, so the copy can
be edited here without touching any template.
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
    {
        "value": "8",
        "suffix": "+ years",
        "label": "Fortune 500 experience",
        "tone": "accent",
    },
    {"value": "330", "suffix": "+", "label": "Ops branches enabled", "tone": "default"},
    {
        "value": "<15",
        "suffix": "%",
        "label": "change failure rate",
        "tone": "default",
    },
    {
        "value": "200",
        "suffix": "+",
        "label": "Audience, Probabilistic forecasting",
        "tone": "default",
    },
    {"value": "7", "suffix": "+ years", "label": "Reliable cadence", "tone": "accent"},
]

SKILLS = [
    "Python",
    "Flask",
    "Azure DevOps",
    "Docker",
    "GitHub Actions",
    "Azure Container Apps",
    "CI/CD",
    "Scrum",
    "SAFe",
    "Monte Carlo forecasting",
    "XmR / Statistical Process Control",
    "Lean",
    "Agile",
    "Value Stream Mapping",
]

CERTS = ["ICAgile ICP-ACC", "ICAgile ICP-ATF", "Certified Scrum Master (CSM)"]

# Full experience. `service: True` marks military entries — the Work page
# filters these OUT of the civilian timeline and links to the Service page.
WORK = [
    {
        "id": "w0",
        "period": "2026",
        "role": "Builder, Independent Projects",
        "org": "Self-directed",
        "tag": "Building",
        ("summary"): (
            "Designing and shipping spec-driven, AI-assisted tooling. Most recent: a "
            "job-search agent that pulls postings straight from ATS boards, scores "
            "them with an LLM against a written profile, and emails a ranked daily "
            "digest."
        ),
        "outcomes": [
            "Registry-driven ingestion → normalized SQLite with hash dedup",
            "LLM scoring with a category-risk axis, send-once tracking",
            "github.com/ctwarrick/job-agent",
        ],
    },
    {
        "id": "w1",
        "period": "Jan 2022 — Jun 2026",
        "role": "Project Manager III",
        "org": "Expeditors · Federal Way, WA",
        "tag": "Delivery",
        ("summary"): (
            "Steered a legacy-to-migrated messaging middleware team through "
            "return-to-office and the aftermath of a major cyberattack while holding "
            "a reliable release cadence.  Onboarded six developers and QA testers.  Then "
            "stood up a new COBOL-to-Databricks ETL team."
        ),
        "outcomes": [
            (
                "Built a Flask/SQLite dashboard over 150+ servers after a Chef failure "
                "pushed stale versions to prod, giving on-call devs a one-click view to "
                '"what\'s running where" in a crisis, leading to faster triage and lower MTTR.'
            ),
            (
                "Replaced story-point guesswork with Monte Carlo forecasts + XmR "
                "process-behavior charts off the Azure DevOps API"
            ),
            (
                "Migrated the Flask apps to Azure Container Apps with some of the "
                "company's first GitHub Actions CI/CD pipelines"
            ),
            (
                "Co-authored the department-wide Scrum Master performance standards and "
                "Lean-Agile Foundations curriculum"
            ),
        ],
    },
    {
        "id": "w2",
        "period": "Jan 2018 — Jan 2022",
        "role": "Project Manager II",
        "org": "Expeditors · Seattle, WA",
        "tag": "Delivery",
        ("summary"): (
            "Coached four teams (test automation, legacy-migration middleware, "
            "reference-data ETL, freight accounting) through the company's SAFe "
            "adoption and the 2020 shift to fully remote."
        ),
        "outcomes": [
            (
                "Took the middleware team to a biweekly release cadence sustained seven "
                "straight years — enabling 330+ operations branches worldwide"
            ),
            (
                "Built a Python bot for recurring Azure DevOps admin; forked by teams in "
                "Europe into an ongoing automation effort"
            ),
            (
                "Mentored a career-changer into her first Scrum Master role — she's now "
                "a Release Train Engineer"
            ),
        ],
    },
    {
        "id": "w3",
        "period": "2021 — 2023",
        "role": "Plans Officer",
        "org": "Navy Reserve US Indo-Pacific Command J5 Kitsap",
        "tag": "Service",
        "service": True,
        ("summary"): "Training Officer and Executive Officer",
        "outcomes": [
            "1,094 flight hours · 16 missions over Afghanistan · 151 carrier arrested landings",
            (
                "Directly supervised 4 line managers and teams up to 43 personnel; "
                "briefed up to a four-star Admiral"
            ),
            "Sole Navy electronic-attack SME at a JSOTF HQ; won buy-in from flag-level leadership",
        ],
    },
    {
        "id": "w4",
        "period": "2017 — 2021",
        "role": "Department Head",
        "org": "Navy Reserve Tactical Air Control Squadron TWELVE (VTC-12) 'Talons'",
        "tag": "Service",
        "service": True,
        ("summary"): "Operations Officer and Administration Officer",
        "outcomes": [
            "1,094 flight hours · 16 missions over Afghanistan · 151 carrier arrested landings",
            (
                "Directly supervised 4 line managers and teams up to 43 personnel; "
                "briefed up to a four-star Admiral"
            ),
            "Sole Navy electronic-attack SME at a JSOTF HQ; won buy-in from flag-level leadership",
        ],
    },
    {
        "id": "w5",
        "period": "2015 — 2016",
        "role": "Active Duty Mobilization",
        "org": "US Joint Special Operations Task Force",
        "tag": "Service",
        "service": True,
        ("summary"): "Electronic Warfare Planner",
        "outcomes": [
            "1,094 flight hours · 16 missions over Afghanistan · 151 carrier arrested landings",
            (
                "Directly supervised 4 line managers and teams up to 43 personnel; "
                "briefed up to a four-star Admiral"
            ),
            "Sole Navy electronic-attack SME at a JSOTF HQ; won buy-in from flag-level leadership",
        ],
    },
    {
        "id": "w6",
        "period": "2014 — 2015",
        "role": "Department Head",
        "org": "Navy Reserve Operational Support Unit Whidbey Island",
        "tag": "Service",
        "service": True,
        ("summary"): "Cross-Assigned Department Head and Assistant Officer-in-Charge",
        "outcomes": [
            "1,094 flight hours · 16 missions over Afghanistan · 151 carrier arrested landings",
            (
                "Directly supervised 4 line managers and teams up to 43 personnel; "
                "briefed up to a four-star Admiral"
            ),
            "Sole Navy electronic-attack SME at a JSOTF HQ; won buy-in from flag-level leadership",
        ],
    },
    {
        "id": "w6",
        "period": "2014 — 2015",
        "role": "EA-6B Electronic Countermeasures Officer (ECMO)",
        "org": "Electronic Attack Squadron 142 (VAQ-142) 'Gray Wolves'",
        "tag": "Service",
        "service": True,
        ("summary"): "Cross-Assigned Department Head and Assistant Officer-in-Charge",
        "outcomes": [
            "1,094 flight hours · 16 missions over Afghanistan · 151 carrier arrested landings",
            (
                "Directly supervised 4 line managers and teams up to 43 personnel; "
                "briefed up to a four-star Admiral"
            ),
            "Sole Navy electronic-attack SME at a JSOTF HQ; won buy-in from flag-level leadership",
        ],
    },
]

# Convenience view: the civilian timeline the Work page renders.
WORK_CIVILIAN = [w for w in WORK if not w.get("service")]

PROJECTS = [
    {
        "id": "pr1",
        "name": "Job Search Agent",
        "stack": "Python · Claude · SQLite · SMTP",
        "icon": "terminal",
        "link": "github.com/ctwarrick/job-agent",
        ("blurb"): (
            "A multi-stage pipeline that turns job-board noise into signal: ATS "
            "ingestion adapters, fingerprint dedup, LLM scoring against a candidate "
            "profile, and a ranked daily email digest."
        ),
    },
    {
        "id": "pr2",
        "name": "Delivery Forecasting Dashboards",
        "stack": "Flask · Azure DevOps API · Azure Container Apps",
        "icon": "gauge",
        "link": "Internal · Expeditors",
        ("blurb"): (
            "Monte Carlo simulation and XmR statistical process control over live "
            "Azure DevOps data — cycle-time scatterplots, the statistical variation of flow"
            'metrics, and probabilistic "when will it ship?" forecasts via Monte Carlo'
            "simulation.  Replaces estimation theater with hard evidence."
        ),
    },
    {
        "id": "pr3",
        "name": "Server Observability Dashboard",
        "stack": "Flask · SQLite",
        "icon": "git-branch",
        "link": "Internal · Expeditors",
        ("blurb"): (
            "Aggregated status across 150+ production and pre-production servers "
            "into one view, so on-call engineers stop hunting page-by-page and get "
            "instant situational awareness at 3 AM."
        ),
    },
    {
        "id": "pr4",
        "name": "Mapping Progress Dashboard",
        "stack": "Flask · Azure Container Apps",
        "icon": "anchor",
        "link": "Internal · Expeditors",
        ("blurb"): (
            "My team was responsible for mapping hundreds of data fields from legacy COBOL and "
            "DB2 applications into a new medallion architecture in Databricks.  On top of this, "
            "the Databricks Silver layer would be an entirely new data model designed from scratch "
            "to more accurately describe the process of shipping freight.  This produced a knotty "
            "problem where different fields from different places in the legacy DB needed to be "
            "mapped to Silver, in the priority that business needed them.  I took the YAML files "
            "my colleagues were doing to do the mapping and turned that data into a simple Flask "
            "dashboard.  It showed not only the details of what the mappings were, but also a "
            "used a not null-vs-total count to show the percentage of Silver fields that had been "
            "successfully mapped.  Because it ingested directly from the source data, it gave "
            "senior leadership a daily up-to-date view of \"how far along are we?\" based in "
            "ground truth."
        ),
    },
]

# The tucked-away Naval Aviation record (its own page, not in primary nav).
SERVICE = {
    ("intro"): (
        "An EA-6B Prowler aviator turned Navy Reserve senior officer, ending as "
        "a unit Executive Officer.  It's where “exacting” became a way of working, "
        "the same instinct I now point at delivery pipelines.  The full record, "
        "since you clicked through for it."
    ),
    "headline": [
        {"value": "1,094", "label": "Flight hours"},
        {"value": "723", "label": "EA-6B Flight hours"},
        {"value": "151", "label": "Carrier arrested landings"},
        {"value": "16", "label": "Missions over Afghanistan"},
    ],
    "roles": [
        {
            "id": "s1",
            "period": "2021 — 2023",
            "icon": "anchor",
            "role": "Department Head/Executive Officer",
            "org": "Navy Reserve US Indo-Pacific Command J5 Kitsap",
            ("summary"): (
                "Served as Training Officer and then Executive Officer of a detachment of Navy "
                "Reservists based at Naval Reserve Center (NRC) Kitsap, who supported the "
                "headquarters staff of U.S. Indo-Pacific Command (USINDOPACOM).  INDOPACOM is a "
                "four-star theater headquarters responsible for planning and directing the "
                "activities of American forces across 52 percent of the Earth's surface, an area "
                "home to more than 50 percent of the world's population.  Its commander is a skip-"
                "level report of the President of the United States."
            ),
            "outcomes": [
                "Directly supervised four Navy officers who were line managers of a team of "
                "Navy reservists assigned to support INDOPACOM's Strategic Planning and Policy "
                "Directorate (J5).",
                "Served as a Joint Operations Center Watch Officer during the command post "
                "exercise PACIFIC SENTRY 21, giving daily briefings to the four-star commander "
                "about the status of the J5 Directorate in concert with a one-star Air Force "
                "Brigadier General.",
                "Served as a Plans Officer for the J56 Strategy and Policy Division, supporting "
                "the USINDOPACOM Theater Posture Plan, and serving as a primary point of contact "
                "for the division during exercise PACIFIC SENTRY 23.",
                "Provided quarterly weekend augmentation support to various staff divisions of "
                "the J5 directorate, supporting various projects and programs.",
            ],
        },
        {
            "id": "s2",
            "period": "2017-2021",
            "icon": "plane",
            "role": "Department Head",
            "org": 'Navy Reserve Tactical Air Control Squadron TWELVE (VTC-12) "Talons"',
            ("summary"): (
                "Served as Operations Officer and Administration Officer for the reserve element "
                "of TACRON TWELVE, an air operations unit which provides detachments of aviation "
                "officers, enlisted Air Traffic Controllers, and enlisted Operations Specialists "
                "to embark on Navy amphibious ships.  There, they coordinate and control flight "
                "operations for Navy and Marine aircraft within their assigned airspace, also "
                "sending liaison officers to other surrounding units in charge of air operations."
            ),
            "outcomes": [
                (
                    "Planned and directed support to the active-duty force for 12 Navy Reserve "
                    "officers and 33 enlisted Sailors."
                ),
                (
                    "Served in the field with the Australian Defence Force as an Air "
                    "Operations Officer during the joint US/Australian exercise TALISMAN "
                    'SABER 17. "Out bush," as the Aussies say, in the Shoalwater Bay Training'
                    'Area in north Queensland.'
                ),
                (
                    "During the major multinational military exercise Rim of the Pacific (RIMPAC) "
                    "18, served as a member of the Naval Amphibious Liaison Element (NALE) at the "
                    "US Air Force's Combined Air Operations Center (CAOC) at Hickam Air Force "
                    "Base, Hawai'i.  Ensured seamless communications between higher authorities "
                    "onshore and aviation forces embarked in multinational ships underway."
                ),
                (
                    "Served as a member of the Naval Amphibious Liaison Element (NALE) during the "
                    "joint US/Australian exercise TALISMAN SABRE 19, serving this time at the main "
                    "military command center for the Australian Defence Force outside Canberra."
                ),
                (
                    "Supported the pre-deployment training of a detachment of active duty officers "
                    "and enlisted Air Traffic Controllers and Operations Specialists so they could "
                    "deploy on board USS AMERICA (LHD 7)."
                ),
                ("Selected for promotion to the rank of Commander."),
            ],
        },
        {
            "id": "s3",
            "period": "2015-2016",
            "icon": "gauge",
            "role": "Electronic Warfare Planner",
            "org": "Joint Special Operations Task Force",
            ("summary"): (
                "Mobilized to active duty.  Served at a Joint Special Operations Task "
                "Force headquarters staff as a subject matter expert in electronic warfare, "
                "translating a niche capability for a room that didn't speak that language "
                "natively."
            ),
            "outcomes": [
                "Sole Navy electronic attack subject matter expert at a JSOTF headquarters.",
                "Won buy-in for various proposals and projects from flag-level leadership (Rear "
                "Admiral and Major General).",
                "Coordinated a site visit to the headquarters by a senior Pentagon civilian leader "
                "(Deputy Undersecretary of the Navy).",
                "Briefly augmented other understaffed areas of the headquarters staff.",
            ],
        },
        {
            "id": "s4",
            "period": "2014-2017",
            "icon": "award",
            "role": "Department Head and Assistant Officer-in-Charge",
            "org": "Operational Support Unit (OSU), Navy Operational Support Center Whidbey Island",
            ("summary"): (
                "Joined the Navy Reserve and was initially assigned to the OSU, a melting pot of "
                "people from all walks of Navy Reserve life who lived in commuting distance of the "
                "Whidbey Island reserve center but were either assigned to support units far "
                "away or new to the Navy Reserve and not yet assigned to a unit."
            ),
            "outcomes": [
                (
                    "Served as Cross-Assigned Department Head, in charge of all Navy Sailors "
                    "assigned to drill locally at Whidbey Island while simultaneously holding "
                    "mobilization billets on the books of units elsewhere."
                ),
                (
                    'Was cross-assigned myself to the "Talons" of Navy Reserve TACRON TWELVE, '
                    "beginning what would become a 6 1/2-year affiliation with this reserve unit. "
                ),
                (
                    "Due to personnel shifts, when I became the second-most-senior officer in the "
                    "unit, stepped up as Assistant Officer-in-Charge or second-in-command, running "
                    "a full drill weekend for the unit when the Officer-in-Charge had to be "
                    "absent."
                ),
                (
                    "Served on an Operational Planning Team on the headquarters staff of "
                    "Commander, U.S. Third Fleet during the joint US/Australian exercise TALISMAN "
                    "SABRE 15."
                ),
                ("Selected for promotion to the rank of Lieutenant Commander."),
            ],
        },
        {
            "id": "s5",
            "period": "2011-2014",
            "icon": "award",
            "role": "EA-6B Electronic Countermeasures Officer (ECMO)",
            "org": 'Electronic Attack Squadron 142 (VAQ-142) "Gray Wolves"',
            ("summary"): (
                "Served as a junior officer in VAQ-142, filling roles as Legal Officer, Personnel "
                "Officer, Aircraft Division Officer, Naval Air Training and Operating Procedures "
                "Standardization (NATOPS) Officer, and Assistant Tactics Officer.  Qualified as "
                "an EA-6B Mission Commander."
            ),
            "outcomes": [
                (
                    "Served as squadron aircrew in a Navy Electronic Attack squadron as it "
                    "transitioned from a land-based unit supporting US Air Force operations to a "
                    "carrier-based unit deploying on board USS NIMITZ (CVN 68) as part of Carrier "
                    "Air Wing ELEVEN (CVW 11)."
                ),
                (
                    "Supported multiple large force exercises hosted by the US Air Force at Nellis "
                    "Air Force Base, Nevada, as well as participating in the pre-deployment workup "
                    "cycle for CVW-11, both on board USS NIMITZ and at Naval Air Station Fallon, "
                    "Nevada."
                ),
                (
                    "Flew off NIMITZ during pre-deployment workups in support of the major "
                    "international exercise Rim of the Pacific (RIMPAC) 18."
                ),
                (
                    "Deployed on board NIMITZ in 2013, supporting both Operation ENDURING FREEDOM "
                    "in Afghanistan and operations in the aftermath of the 2013 Syrian chemical "
                    "weapons crisis."
                ),
            ],
        },
    ],
}
