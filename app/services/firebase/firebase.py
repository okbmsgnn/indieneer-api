import json

import firebase_admin
import firebase_admin.auth
import firebase_admin.credentials

from . import identity_toolkit, secure_token

# Firebase Admin SDK
# https://firebase.google.com/docs/reference/admin/python


class Firebase:
    _app: firebase_admin.App
    _api_key: str

    def __init__(self, service_account: str, api_key: str) -> None:
        self._app = self.init_app(service_account)
        self._api_key = api_key

    def init_app(self, service_account: str):
        try:
            # Use an initialized app if one exists
            return firebase_admin.get_app()
        except ValueError:
            # Initialize app
            service_account = json.loads(service_account)
            certificate = firebase_admin.credentials.Certificate(
                service_account
            )

            return firebase_admin.initialize_app(certificate)

    @property
    def auth(self):
        return firebase_admin.auth

    @property
    def identity_api(self):
        return identity_toolkit.IdentityToolkitApiClient(self._api_key)

    @property
    def secure_token_api(self):
        return secure_token.SecureTokenAPI(self._api_key)
