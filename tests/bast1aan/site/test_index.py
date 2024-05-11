import os
import unittest
import bs4
from flask import Response

from flask.testing import FlaskClient

from tests.bast1aan.site.app import app


class TestIndex(unittest.TestCase):
	def assertHTMLEqual(self, a: str, b: str, msg=None) -> None:
		self.assertEqual(_bs(a), _bs(b), msg)
		
	def test_index(self):
		client: FlaskClient = app.test_client()
		result: Response = client.get('/')
		self.assertHTMLEqual(result.data, _read('test_index.html'))


def _bs(inp: str) -> str:
	return bs4.BeautifulSoup(inp, features="html.parser").prettify()

def _read(filename: str) -> str:
	with open(os.path.join(os.path.dirname(__file__), filename), 'r') as f:
		return f.read()
