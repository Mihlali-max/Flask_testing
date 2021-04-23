from unittest import TestCase

from flask import json

from main import app


class TestCase(TestCase):

    def test_home(self):
        with app.test_client() as c:
            resp = c.get('/')

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(
                json.loads(resp.get_data()), {'message': 'Hello world'}
            )


