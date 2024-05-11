from flask import Response

from flask.testing import FlaskClient

from tests.bast1aan.site.app import app
from tests.bast1aan.site.test_base import SiteTestCase, read


class TestWithoutModule(SiteTestCase):
	def test_without_module(self):
		client: FlaskClient = app.test_client()
		result: Response = client.get('/withoutmodule.html')
		self.assertHTMLEqual(result.data, read('test_withoutmodule.html'))
