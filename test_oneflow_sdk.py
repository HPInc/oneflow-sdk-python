import json
import unittest
from unittest.mock import patch

import requests

from OneflowSDK import OneflowSDK


class RequestBodyTest(unittest.TestCase):
    def setUp(self):
        self.client = OneflowSDK("https://example.invalid", "token", "secret")

    def prepare_request(self, body):
        response = requests.Response()
        response.status_code = 200
        response._content = b"accepted"
        with patch.object(requests.Session, "send", return_value=response) as send:
            result = self.client.request("POST", "/api/order", body)
        self.assertEqual(result, b"accepted")
        self.assertIs(send.call_args.kwargs["allow_redirects"], False)
        request = send.call_args.args[0]
        self.assertEqual(request.headers["content-type"], "application/json")
        return request

    def test_dictionary_is_sent_as_json(self):
        for body in ({"order": {"id": "test", "items": [1, 2]}}, {}):
            with self.subTest(body=body):
                request = self.prepare_request(body)
                self.assertEqual(json.loads(request.body), body)

    def test_serialized_json_is_preserved(self):
        for body in ('{"order": "test"}', b'{"order": "test"}'):
            with self.subTest(body=body):
                self.assertEqual(self.prepare_request(body).body, body)


if __name__ == "__main__":
    unittest.main()
