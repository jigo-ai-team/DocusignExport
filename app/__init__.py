import os

from flask import Flask, session, current_app
from flask_wtf.csrf import CSRFProtect

from .ds_config import DS_CONFIG
from .eSignature import views as esignature_views
from .docusign.views import ds
from .views import core

session_path = "/tmp/python_recipe_sessions"
app = Flask(__name__)

app.config.from_pyfile("config.py")

# See https://flask-wtf.readthedocs.io/en/stable/csrf.html
csrf = CSRFProtect(app)

# Register home page
app.register_blueprint(core)

# Register OAuth
app.register_blueprint(ds)
# Register examples

app.register_blueprint(esignature_views.embedconsole)