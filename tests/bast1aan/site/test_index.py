from flask import Response

from flask.testing import FlaskClient

from tests.bast1aan.site.app import app
from tests.bast1aan.site.test_base import SiteTestCase, read


class TestIndex(SiteTestCase):
	def test_index(self):
		client: FlaskClient = app.test_client()
		result: Response = client.get('/')
		self.assertHTMLEqual(result.data, read('test_index.html'))
