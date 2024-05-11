from flask import Response

from flask.testing import FlaskClient

from tests.bast1aan.site.app import app
from tests.bast1aan.site.test_base import SiteTestCase, read


class TestSubdirWithoutModule(SiteTestCase):
	def test_subdir_without_module(self):
		client: FlaskClient = app.test_client()
		result: Response = client.get('/subdir/withoutmodule.html')
		self.assertHTMLEqual(result.data, read('test_withoutmodule.html'))
