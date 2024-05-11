from flask import Response

from flask.testing import FlaskClient

from tests.bast1aan.site.app import app
from tests.bast1aan.site.test_base import SiteTestCase, read


class TestBlie(SiteTestCase):
	def test_blie(self):
		client: FlaskClient = app.test_client()
		result: Response = client.get('/subdir/blie.html')
		self.assertHTMLEqual(result.data, read('test_blie.html'))
