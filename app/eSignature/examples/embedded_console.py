from docusign_esign import EnvelopesApi, ConsoleViewRequest
from flask import session, url_for, request

from ...consts import pattern
from ...docusign import create_api_client


class EmbeddedConsoleController:
    @staticmethod
    def get_args():
        args = {
            "envelope_id": False,
            "starting_view": 'front_page',
            "account_id": session["ds_account_id"],
            "base_path": session["ds_base_path"],
            "access_token": session["ds_access_token"],
            "ds_return_url": url_for("ds.ds_return", _external=True),
        }

        return args

    @staticmethod
    def worker(args):

        view_request = ConsoleViewRequest(return_url=args["ds_return_url"])

        api_client = create_api_client(base_path=args["base_path"], access_token=args["access_token"])

        envelope_api = EnvelopesApi(api_client)
        results = envelope_api.create_console_view(account_id=args["account_id"], console_view_request=view_request)
        url = results.url

        return {"redirect_url": url}
