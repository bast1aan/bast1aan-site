import os.path
import importlib
import pkgutil
from pathlib import Path
from types import ModuleType

from flask import Flask
from jinja2 import ChoiceLoader, FileSystemLoader

from . import views


package_path = Path(os.path.dirname(__file__))

_system_template_dir = os.path.abspath(package_path / '..' / '..' / 'templates')

_system_public_template_dir = os.path.abspath(package_path / '..' / '..' / 'public_j2')

_static_dir = os.path.abspath(package_path / '..' / '..' / 'static')

_extra_template_dirs: dict[str, ModuleType] = {}

_extra_public_template_dirs: list[str] = []


def add_template_dir(dir: str, module:ModuleType=None, public=False) -> None:
	_extra_template_dirs[dir] = module
	if module:
		_recursive_import(module)
	if public:
		_extra_public_template_dirs.append(dir)

def public_template_dirs() -> tuple[str, ...]:
	return (*_extra_public_template_dirs, _system_public_template_dir)

def _all_template_dirs() -> tuple[str, ...]:
	return (*_extra_template_dirs.keys(), _system_public_template_dir, _system_template_dir)

def get_module(template_dir: str) -> ModuleType | None:
	return _extra_template_dirs.get(template_dir)

def _recursive_import(module: ModuleType) -> None:
	if not hasattr(module, '__all__'):
		module.__all__ = []
	for loader, module_name, is_pkg in pkgutil.walk_packages(module.__path__):
		try:
			module.__all__.append(module_name)
			_module = importlib.import_module('.' + module_name, package=module.__name__)
			if is_pkg:
				_recursive_import(_module)
			setattr(module, module_name, _module)
		except ImportError:
			pass
    
class App(Flask):
	def create_jinja_environment(self):
		self.jinja_options['loader'] = ChoiceLoader(tuple(
			FileSystemLoader(dir) for dir in _all_template_dirs()
		))
		return super().create_jinja_environment()

app = App(__name__, static_folder=_static_dir)

app.add_url_rule('/', view_func=views.template_view, defaults={'path': '/'})
app.add_url_rule('/<path:path>', view_func=views.template_view)
