"""Defines the home page route"""

from flask import (
    render_template,
    url_for,
    redirect,
    Blueprint,
    session,
    current_app as app
)

core = Blueprint("core", __name__)

@core.route("/")
def index():
    return render_template("home.html", title="Home - Python Code Examples",
                           crfEnabled="False")

@core.route("/index")
def r_index():
    return redirect(url_for("core.index"))


@core.app_errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404


@core.app_errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500
