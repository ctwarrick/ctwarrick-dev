"""
app.py — Flask entry point for the Chris Warrick site.

Run locally:   flask --app app run --debug
Azure (gunicorn startup command):   gunicorn --bind=0.0.0.0 --timeout 600 app:app

This is a skeleton. The `work` route + work.html are fully worked
examples; the other routes render templates you still need to build by
translating the matching JSX in _design_reference/ (see README, "Routes").
"""
from flask import Flask, render_template, abort, url_for
import content

app = Flask(__name__)


@app.context_processor
def inject_globals():
    """Make nav + site info available to every template (header/footer)."""
    return {"nav": content.NAV, "site": content.SITE}


# Which nav item highlights for a given view. Mirrors the React active-state
# logic: the Service and Article pages light up their parent nav item.
ACTIVE = {"service": "work", "article": "writing"}


def active_for(view):
    return ACTIVE.get(view, view)


@app.route("/")
def home():
    return render_template(
        "home.html", active="home",
        stats=content.STATS, work=content.WORK_CIVILIAN[:2],
    )


@app.route("/work")
def work():
    return render_template(
        "work.html", active="work", work=content.WORK_CIVILIAN,
    )


@app.route("/building")
def building():
    return render_template(
        "building.html", active="building", projects=content.PROJECTS,
    )


@app.route("/about")
def about():
    return render_template(
        "about.html", active="about",
        skills=content.SKILLS, certs=content.CERTS,
    )


@app.route("/writing")
def writing():
    return render_template("writing.html", active="writing", posts=content.POSTS)


@app.route("/writing/<post_id>")
def article(post_id):
    post = next((p for p in content.POSTS if p["id"] == post_id), None)
    if post is None:
        abort(404)
    return render_template("article.html", active=active_for("article"), post=post)


@app.route("/service")
def service():
    return render_template(
        "service.html", active=active_for("service"), service=content.SERVICE,
    )


if __name__ == "__main__":
    app.run(debug=True)
