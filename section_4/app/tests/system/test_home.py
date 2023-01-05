import json
from section_4.app.tests.system.base_test import BaseTest


class TestHome(BaseTest):
    def test_home(self):
        with self.app() as client:
            response = client.get('/')

            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                json.loads(response.get_data()),
                {'message': 'Hello, world!'}
            )
