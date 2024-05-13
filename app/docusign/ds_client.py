import uuid

import requests
from flask import current_app as app, url_for, request
from flask_oauthlib.client import OAuth

from ..ds_config import DS_CONFIG
from ..consts import API_TYPE

SCOPES = [
    "signature"
]


class DSClient:
    ds_app = None

    @classmethod
    def _init(cls, auth_type, api):
        cls._auth_code_grant(api)

    @classmethod
    def _auth_code_grant(cls, api):
        """Authorize with the Authorization Code Grant - OAuth 2.0 flow"""
        oauth = OAuth(app)
        request_token_params = {
            "scope": " ",
            "state": lambda: uuid.uuid4().hex.upper()
        }
        if not DS_CONFIG["allow_silent_authentication"]:
            request_token_params["prompt"] = "login"
        cls.ds_app = oauth.remote_app(
            "docusign",
            consumer_key=DS_CONFIG["ds_client_id"],
            consumer_secret=DS_CONFIG["ds_client_secret"],
            access_token_url=DS_CONFIG["authorization_server"] + "/oauth/token",
            authorize_url=DS_CONFIG["authorization_server"] + "/oauth/auth",
            request_token_params=request_token_params,
            base_url=None,
            request_token_url=None,
            access_token_method="POST"
        )

    @classmethod
    def destroy(cls):
        cls.ds_app = None

    @classmethod
    def login(cls, auth_type, api):
        cls._init(auth_type, api)
        return cls.get(auth_type, api).authorize(callback=url_for("ds.ds_callback", _external=True))

    @classmethod
    def get_token(cls, auth_type):
        resp = cls.get(auth_type).authorized_response()

        if resp is None or resp.get("access_token") is None:
            return "Access denied: reason=%s error=%s resp=%s" % (
                request.args["error"],
                request.args["error_description"],
                resp
            )

        return resp

    @classmethod
    def get_user(cls, access_token):
        url = DS_CONFIG["authorization_server"] + "/oauth/userinfo"
        auth = {"Authorization": "Bearer " + access_token}
        response = requests.get(url, headers=auth).json()

        return response

    @classmethod
    def get(cls, auth_type, api=API_TYPE["ESIGNATURE"]):
        if not cls.ds_app:
            cls._init(auth_type, api)
        return cls.ds_app
