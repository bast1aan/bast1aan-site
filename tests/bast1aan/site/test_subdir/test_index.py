from flask import Response

from flask.testing import FlaskClient

from tests.bast1aan.site.app import app
from tests.bast1aan.site.test_base import SiteTestCase, read


class TestSubdirIndex(SiteTestCase):
	def test_subdir_index(self):
		client: FlaskClient = app.test_client()
		result: Response = client.get('/subdir/')
		self.assertHTMLEqual(result.data, read('test_index.html'))
