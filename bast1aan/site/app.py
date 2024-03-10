import os.path
from pathlib import Path

from flask import Flask
from jinja2 import ChoiceLoader, FileSystemLoader

from . import views


package_path = Path(os.path.dirname(__file__))

_system_template_dir = os.path.abspath(package_path / '..' / '..' / 'templates')

_system_public_template_dir = os.path.abspath(package_path / '..' / '..' / 'public_j2')

_extra_template_dirs: list[str] = []

_extra_public_template_dirs: list[str] = []


def add_template_dir(dir: str, public=False) -> None:
	_extra_template_dirs.append(dir)
	if public:
		_extra_public_template_dirs.append(dir)

def public_template_dirs() -> tuple[str, ...]:
	return (*_extra_public_template_dirs, _system_public_template_dir)

def _all_template_dirs() -> tuple[str, ...]:
	return (*_extra_template_dirs, _system_public_template_dir, _system_template_dir)

class App(Flask):
	def create_jinja_environment(self):
		self.jinja_options['loader'] = ChoiceLoader(tuple(
			FileSystemLoader(dir) for dir in _all_template_dirs()
		))
		return super().create_jinja_environment()

app = App(__name__)

app.add_url_rule('/', view_func=views.template_view, defaults={'path': '/'})
app.add_url_rule('/<path:path>', view_func=views.template_view)
