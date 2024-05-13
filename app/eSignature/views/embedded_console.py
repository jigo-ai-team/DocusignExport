from docusign_esign.client.api_exception import ApiException
from flask import render_template, redirect, session, Blueprint

from ..examples.embedded_console import EmbeddedConsoleController
from ...docusign import authenticate
from ...error_handlers import process_error
from ...consts import API_TYPE

api = API_TYPE["ESIGNATURE"]
embedconsole = Blueprint("embedconsole", __name__)


@embedconsole.route("/embedconsole", methods=["POST"])
@authenticate(api=api)
def embedded_console():
    args = EmbeddedConsoleController.get_args()
    try:
        results = EmbeddedConsoleController.worker(args)
    except ApiException as err:
        return process_error(err)

    return redirect(results["redirect_url"])


@embedconsole.route("/embedconsole", methods=["GET"])
@authenticate(api=api)
def get_view():
    return render_template(
        "embedded_console.html"
    )
