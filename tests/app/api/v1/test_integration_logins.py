import json

from tests import IntegrationTest


class LoginsTestCase(IntegrationTest):

    def test_logins(self):
        # given
        user = self.fixtures.regular_user

        email = user.email
        password = "9!8@7#6$5%4^3&2*1(0)-_=+[]{}|;:"

        data = {"email": email, "password": password}

        # when
        response = self.app.post(
            "/v1/logins", data=json.dumps(data), content_type="application/json")
        response_json = response.get_json()

        # then
        # TODO: improve checks in tests
        self.assertEqual(type(response_json["data"]), dict)
        self.assertEqual(
            len(response_json["data"]["id_token"].split(".")), 3)

    def test_wrong_password(self):
        # given
        user = self.fixtures.regular_user

        email = user.email

        data = {"email": email, "password": "jyohn_prok"}

        # when
        response = self.app.post(
            "/v1/logins", data=json.dumps(data), content_type="application/json")
        response_json = response.get_json()

        # then
        self.assertEqual(response_json, {'status': 'error', 'error': 'Wrong email or password.'})
        self.assertEqual(response.status_code, 403)
