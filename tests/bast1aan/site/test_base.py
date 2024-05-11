import os
import traceback
import unittest
from abc import ABCMeta

import bs4


class SiteTestCase(unittest.TestCase, metaclass=ABCMeta):
	def assertHTMLEqual(self, a: str, b: str, msg=None) -> None:
		self.assertEqual(_bs(a), _bs(b), msg)

def _bs(inp: str) -> str:
	return bs4.BeautifulSoup(inp, features="html.parser").prettify()

def read(filename: str) -> str:
	with open(os.path.join(os.path.dirname(_caller_filename()), filename), 'r') as f:
		return f.read()

def _caller_filename() -> str:
	return traceback.extract_stack()[-3].filename
