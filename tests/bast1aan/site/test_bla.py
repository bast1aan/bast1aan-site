from flask import Response

from flask.testing import FlaskClient

from tests.bast1aan.site.app import app
from tests.bast1aan.site.test_base import SiteTestCase, read


class TestBla(SiteTestCase):
	def test_bla(self):
		client: FlaskClient = app.test_client()
		result: Response = client.get('/bla.html')
		self.assertHTMLEqual(result.data, read('test_bla.html'))
