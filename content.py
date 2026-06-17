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
            "Custom adapters for common Applicant Tracking Systems, normalizing data into a "
            "common schema.",
            "Data ingested from desired companies based on a registry of companies and their "
            "corresponding Applicant Tracking Systems.  Hash-based deduplication prevents "
            "disorganization and allows for idempotent database upserts.",
            "LLM scoring on fit and risk, data stored in SQLite, with a daily email "
            "digest using send-once tracking.",
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
                "While coaching the middleware team, built a Flask/SQLite dashboard aggregating "
                "status outputs from 150+ production and pre-production servers after a Chef "
                "failure silently pushed outdated application versions to production.  For "
                "on-call team members, this replaced a server-by-server hunt through status pages "
                "with one-click visibility into what was running where, enabling far faster "
                "incident triage and decreasing mean time to recover."
            ),
            (
                "Developed Python automation against the Azure DevOps REST API to generate and "
                "process QA approval documents and change orders for the middleware team's four "
                "separate applications, removing a manual gate that had helped lock the team into "
                "phase-gated, end-of-iteration deployments and clearing the path toward true CI/CD."
            ),
            (
                "After seven years with the middleware team, transitioned to stand up a new team "
                "writing ETL pipelines for a COBOL-to-Databricks medallion architecture.  "
                "Persuaded senior leadership to backfill the previous role at full seniority "
                "rather than down-level it.  Because I personally intervened to create a wider "
                "and more seasoned candidate pool and personally shortlisted candidates for "
                "management, we landed a former Senior Director with 20+ years of experience."
            ),
            (
                "While coaching the ETL team, used spec-driven development and AI to build a "
                "Flask dashboard that ingested YAML field-mapping files from the ETL pipeline "
                "and computed per-table Bronze-to-Silver mapping progress, giving leadership a "
                "real answer to “how far along are we?” that could be updated daily or with every "
                "YAML change."
            ),
            (
                "Created a Flask application to create cycle-time scatterplots and swarmplots "
                "from the Azure DevOps REST API, as well as Monte Carlo simulations for "
                "probabilistic delivery forecasting, replacing story-point guesswork with "
                "data-driven forecasting.  Extended it with XmR process-behavior charts "
                "(statistical process control) for Work Item Age, Throughput, and Cycle Time, "
                "separating signal from noise and enabling data-driven conversations on team "
                "process stability.  Introduced Monte Carlo and probabilistic forecasting to "
                "the Global Technology department in a 45-minute talk to 200+ attendees at "
                "exp.oCon, the annual innovation fair."
            ),
            (
                "Via AI-assisted development, migrated the Monte Carlo and ETL mapping Flask "
                "applications from on-prem VMs to Azure Container Apps behind an Application "
                "Gateway, with corporate vanity URLs for ease of use by nontechnical employees.  "
                "Built GitHub Actions CI/CD workflows (among the company's first) to build Docker "
                "images, push to a Container Registry, and auto-deploy on approved merges to "
                "main.  Coordinated subnets, VNet peering, and DNS with Datacenters and "
                "Networking teams and added health-check endpoints to eliminate gateway 502s."
            ),
            (
                "Co-authored formal Scrum Master performance standards adopted department-wide, "
                "improving evaluation and compensation for the entire role family, as well as "
                "an \"Expeditors Lean-Agile Foundations\" training curriculum used to onboard "
                "and upskill technology staff."
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
                "Took the middleware team from manual QA processes and ad-hoc releases to a "
                "reliable biweekly release cadence sustained for seven straight years, directly "
                "enabling 330+ operations branches worldwide and the company's strategic "
                "migration off legacy software."
            ),
            (
                "Built a Python bot for recurring Azure DevOps admin; forked by teams in "
                "Europe into an ongoing automation effort"
            ),
            (
                "Led delivery of a major initiative automating worldwide freight delivery "
                "timetable updates and improving their accuracy; coached business stakeholders "
                "up to the Vice President level on SAFe to keep priorities and expectations "
                "aligned."
            ),
            (
                "Onboarded three QA testers with their primary Lean-Agile training.  Mentored a "
                "career-changer into her first Scrum Master role through six months of direct "
                "shadowing; she's now a Release Train Engineer."
            ),
        ],
    },
]

PROJECTS = [
    {
        "id": "pr1",
        "name": "Job Search Agent",
        "stack": "Python · Claude · SQLite · SMTP",
        "icon": "terminal",
        "link": "github.com/ctwarrick/job-agent",
        ("blurb"): (
            "A multi-stage job search pipeline that turns job board noise into signal.  It uses "
            "custom adapters for common ATS systems to pull job posts, based on a registry of "
            "desired companies and what ATSes they use.  It normalizes the posts into a common "
            "format, using a hash function for deduplication and idempotent database upserts.  "
            "It then sends new postings to the Anthropic API, so an LLM can score them scoring "
            "against a pre-written candidate profile and salary floor.  Finally, it stores the "
            "roles in SQLite and sends a daily email with a ranked digest of roles, including "
            "numerical 1-10 scores for fit and career risk."
        ),
    },
    {
        "id": "pr2",
        "name": "Statistical Delivery Forecasting",
        "stack": "Flask · Azure DevOps API · Azure Container Apps",
        "icon": "gauge",
        "link": "Internal · Expeditors",
        ("blurb"): (
            "Inspired by Dan Vacanti's work in his <em>Actionable Agile Metrics</em> series and "
            "<em>When Will It Be Done?</em>, I set out to implement these concepts in a web app "
            "teams could use in their day-to-day syncs.  By the end, it offered four different "
            "types of flow visualizations, all drawn from live Azure DevOps data:  <ul><li>The "
            "classic Cycle Time Scatterplot of all work done in a given timeframe, along with "
            "50/70/85/90 cycle time percentiles.</li><li>A Cycle Time Swarmplot where teams can "
            "compare active work to the same historic cycle time percentiles.</li><li>Monte "
            "Carlo simulations forecasting the amount of completed work over an iteration, a "
            "Program Increment, any arbitrary due date, or any arbitrary quantity of work "
            "items, all with 50/70/85/90 percent forecast confidence lines.</li><li>Both mean- "
            "and median-based XmR Statistical Process Control charts for Cycle Time, total Work "
            "Item Age, and daily throughput.</li></ul>The Cycle Time and Monte Carlo pieces of "
            "this application were the centerpiece of a 45-minute talk I gave at exp.oCon 2026, "
            "Expeditors' annual innovation conference, called <em>Ditch the Points; Look at the "
            "Data! Probabilistic Forecasting for Predictable Delivery</em>."
        ),
    },
    {
        "id": "pr3",
        "name": "Server Observability Dashboard",
        "stack": "Flask · SQLite",
        "icon": "lightbulb",
        "link": "Internal · Expeditors",
        ("blurb"): (
            "One night, Chef broke.  It started spewing old versions of my team's code across "
            "random production servers around the globe, bringing freight to a grinding halt.  I "
            "was on call, and it was awful.  Because the only way to find the state of a given "
            "server was to go to a very specific URL for that particular server to show its "
            "status.  There were 150+ servers.  The next morning, after the smoke had cleared, "
            "I started writing a Flask dashboard that queried those individual URLs "
            "automatically, aggregating status across all 150+ production and pre-production "
            "servers into one view with near-real-time visibility, so on-call engineers could "
            "stop hunting page-by-page in the dark and get instant situational awareness."
        ),
    },
    {
        "id": "pr4",
        "name": "Mapping Progress Dashboard",
        "stack": "Flask · Azure Container Apps",
        "icon": "compass",
        "link": "Internal · Expeditors",
        ("blurb"): (
            "My team was responsible for mapping hundreds of data fields from legacy COBOL and "
            "DB2 applications into a new medallion architecture in Databricks.  On top of this, "
            "the Databricks Silver layer would be an entirely new data model designed from scratch "
            "to more accurately describe the process of shipping freight.  This produced a knotty "
            "problem where different fields from different places in the legacy DB needed to be "
            "mapped to Silver, in the priority that business needed them.  I took the YAML files "
            "my colleagues were writing to do the mapping and turned that data into a simple Flask "
            "dashboard.  It showed not only the details of what the mappings were, but also a "
            "used a not-null-vs-total count to show the percentage of Silver fields that had been "
            "successfully mapped.  Because it ingested directly from the source data, it gave "
            "senior leadership a daily up-to-date view of \"how far along are we?\" based in "
            "ground truth."
        ),
    },
    {
        "id": "pr5",
        "name": "Web App Cloud Migration",
        "stack": "GitHub Actions · Azure Container Apps",
        "icon": "cloud",
        "link": "Internal · Expeditors",
        ("blurb"): (
            "Related to two other efforts, but worth calling out on its own.  My Statistical "
            "Delivery Forecasting tool and the Mapping Progress Dashboard initially lived on "
            "small on-prem Linux VMs.  As I got ready to give my exp.oCon presentation, I was "
            "worried about the ability of a small VM to absorb 200+ attendees all trying to hit "
            "it at once.  An architect basically dared me to set my two webapps up as Azure "
            "Container Apps instead of on-prem ones.  This turned into a journey of teaching "
            "myself GitHub Actions (we were migrating off GitLab), Azure Container Registries, "
            "Azure Container Apps, Azure App Gateways, and how to tie all that together under the "
            "hood in the cloud.  By the end, I had set up all required resources and coordinated "
            "with the Networking and Datacenters teams for IP address space, hub-and-spoke VNet "
            "peering, and DNS assignments for two custom vanity URLs in the company's internal "
            "URL format, so nontechnical users wouldn't be intimidated trying to find them."
        ),
    },
    {
        "id": "pr6",
        "name": "Azure DevOps Admin Bot",
        "stack": "Python · Microsoft Graph · Azure DevOps",
        "icon": "bot",
        "link": "Internal · Expeditors",
        ("blurb"): (
            "My first foray into improving processes through code.  I wrote Python code to access "
            "the Azure DevOps REST API and automate common housekeeping tasks.  Moving active "
            "work items to the current iteration, activating parent items whose children were "
            "active, and sending emails when items might need to be closed.  I started writing it "
            "in 2018 shortly after joining the company and getting my bearings, and it was an "
            "ongoing project for my entire tenure.  It started out as a pile of scripts on a "
            "random on-prem Windows VM that was all I could get.  Over the years, I hosted it in "
            "GitLab, ported it to RHEL 8, and moved it to GitHub and Azure.  By the end, it was a "
            "fully containerized small cloud-native application with its own CI/CD pipeline.  A "
            "true microcosm of my own technical learning and growth."
        ),
    },
    {
        "id": "pr7",
        "name": "Change Request Automation",
        "stack": "Python · Microsoft Graph · Jenkins · GitLab · Azure DevOps",
        "icon": "check",
        "link": "Internal · Expeditors",
        ("blurb"): (
            "As an outgrowth of my Admin Bot work, I started exploring the idea of automating "
            "required software change requests, which were hosted as Azure DevOps work items. "
            "My team used a SharePoint list to host required QA approval documentation, so I "
            "created a Python tool that polled our build environment for both the latest prod "
            "release and the one staged for deployment, scraped Azure DevOps for all work items "
            "identified with the version numbers of the upcoming release, then used a template "
            "to take the information from those work items and build a QA approval document in "
            "SharePoint via the Graph API.  Then I wrote more code that would close out the QA "
            "approval in SharePoint, create a Change Request in Azure DevOps using the work item "
            "info, and send a QA approval email to the required addresses.  I hooked all this up "
            "to a GitLab pipeline so QA testers could simply push a button to trigger a \"Create "
            "QA docs\" job, then push another button to trigger a \"Create Change Request\" job."
        ),
    },
    {
        "id": "pr8",
        "name": "Holographic Freight Tracking",
        "stack": "Unity · C# · HoloLens 2",
        "icon": "globe",
        "link": "github.com/ctwarrick/Object-Tracker",
        ("blurb"): (
            "As a side project, given my company's interest in tracking freight and the "
            "availability of IoT devices to give GPS location, I decided to use my personal "
            "HoloLens 2 to explore the idea of holographic freight tracking.  I used the Bing "
            "Maps API and the Mixed Reality Toolkit in Unity to develop a prototype map display "
            "which showed pins on a holographic map with item locations.  Air tapping on those "
            "items showed details about the object.  This could have been extended via access to "
            "streaming location data in order to show the live location of an object "
            "holographically.  It wasn't accepted as an idea; I still have access to the code "
            "since I worked up the prototype on my own time on my own personal gear.  I later "
            "pitched the idea of QR-based holographic freight tracking and warehouse navigation "
            "to a VP, but this also did not gain traction."
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
            "icon": "globe",
            "role": "Department Head/Executive Officer",
            "org": "Navy Reserve US Indo-Pacific Command J5 Kitsap",
            "tag": "Plans and Policy",
            ("summary"): (
                "Served as Training Officer and then Executive Officer of a detachment of Navy "
                "Reservists based at Navy Reserve Center (NRC) Kitsap, who supported the "
                "headquarters staff of U.S. Indo-Pacific Command (USINDOPACOM), since renamed US "
                "Pacific Command or USPACOM.  Under either name, PACOM is a four-star theater "
                "headquarters responsible for planning and directing the activities of American "
                "forces across 52 percent of the Earth's surface, an area home to more than 50 "
                "percent of the world's population.  Per the Goldwater-Nichols Act of 1986, its "
                "commander is a skip-level report of the President of the United States."
            ),
            "outcomes": [
                "Directly supervised four Navy officers who were line managers of a team of "
                "Navy reservists assigned to support INDOPACOM's Strategic Planning and Policy "
                "Directorate (J5).",
                "Served as a Joint Operations Center Watch Officer during the command post "
                "exercise Pacific Sentry 21, giving daily briefings to the four-star commander "
                "about the status of the J5 Directorate in concert with a one-star Air Force "
                "Brigadier General.",
                "Served as a Plans Officer for the J56 Strategy and Policy Division, supporting "
                "the USINDOPACOM Theater Posture Plan and serving as a primary point of contact "
                "for the division during exercise Pacific Sentry 23.",
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
            "tag": "Air Operations",
            ("summary"): (
                "Served as Operations Officer and Administration Officer for the reserve element "
                "of VTC-12, an air operations unit which provides detachments of aviation "
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
                    "Operations Officer during the joint US/Australian exercise Talisman "
                    'Saber 17. "Out bush," as the Aussies say, in the Shoalwater Bay Training '
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
                    "joint US/Australian exercise Talisman Sabre 19, serving this time at the main "
                    "military command center for the Australian Defence Force outside Canberra."
                ),
                (
                    "Supported the pre-deployment training of a detachment of active duty officers "
                    "and enlisted Air Traffic Controllers and Operations Specialists so they could "
                    "deploy on board the amphibious assault ship USS <em>Bonhomme Richard</em>."
                ),
                ("Selected for promotion to the rank of Commander."),
            ],
        },
        {
            "id": "s3",
            "period": "2015-2016",
            "icon": "zap",
            "role": "Electronic Warfare Planner",
            "org": "Joint Special Operations Task Force",
            "tag": "Electronic Warfare",
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
            "icon": "check",
            "role": "Department Head and Assistant Officer-in-Charge",
            "org": "Operational Support Unit (OSU), Navy Operational Support Center Whidbey Island",
            "tag": "Personnel Administration/Air Operations",
            ("summary"): (
                "I joined the Navy Reserve and was initially assigned to the OSU, a unit that "
                "served as a holding tank for people from all walks of Navy Reserve life. These "
                "Sailors lived within commuting distance of the Whidbey Island reserve center, "
                "but were either assigned mobilization billets with units offsite or brand new "
                "to the Reserve and not yet placed."
            ),
            "outcomes": [
                (
                    "Served as Cross-Assigned Department Head, in charge of all OSU Sailors "
                    "assigned to drill locally at Whidbey Island while simultaneously holding "
                    "mobilization billets on the books of units elsewhere."
                ),
                (
                    'Was cross-assigned myself to the Navy Reserve element of the VTC-12 "Talons,"'
                    "beginning what would become a roughly 6 1/2-year affiliation with this "
                    "reserve unit."
                ),
                (
                    "Due to personnel shifts, when I became the second-most-senior officer in the "
                    "unit, stepped up as Assistant Officer-in-Charge or second-in-command, running "
                    "a full drill weekend for the unit when the Officer-in-Charge had to be "
                    "absent."
                ),
                (
                    "Served on an Operational Planning Team on the headquarters staff of "
                    "Commander, U.S. Third Fleet during the joint US/Australian exercise Talisman "
                    "Sabre 15."
                ),
                ("Selected for promotion to the rank of Lieutenant Commander."),
            ],
        },
        {
            "id": "s5",
            "period": "2011-2014",
            "icon": "plane",
            "role": "EA-6B Electronic Countermeasures Officer (ECMO)",
            "org": 'Electronic Attack Squadron 142 (VAQ-142) "Gray Wolves"',
            "tag": "Electronic Warfare",
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
                    "carrier-based unit deploying on board the nuclear-powered aircraft carrier "
                    "USS <em>Nimitz</em> as part of Carrier Air Wing Eleven."
                ),
                (
                    "Supported multiple large force exercises hosted by the US Air Force at Nellis "
                    "Air Force Base, Nevada, as well as participating in the pre-deployment workup "
                    "cycle for CVW-11, both on board USS <em>Nimitz</em> and at Naval Air Station "
                    "Fallon, Nevada."
                ),
                (
                    "Flew off USS <em>Nimitz</em> during pre-deployment workups in support of the "
                    "major international exercise Rim of the Pacific (RIMPAC) 18."
                ),
                (
                    "Deployed on board USS <em>Nimitz</em> in 2013, supporting both Operation "
                    "Enduring Freedom in Afghanistan and operations in the aftermath of the 2013 "
                    "Syrian chemical weapons crisis."
                ),
            ],
        },
    ],
}
