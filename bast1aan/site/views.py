import importlib
from os.path import exists
from pathlib import Path
from typing import Callable

from flask import typing as ft, render_template
from werkzeug.exceptions import NotFound

from . import app

def template_view(path: str) -> ft.ResponseReturnValue:
	""" :raises NotFound """
	if path.endswith('/'):
		path += 'index.html'

	if not path.endswith('.html'):
		raise NotFound

	template = path.strip('/') + '.j2'

	if not _is_public_template(template):
		raise NotFound

	context = _get_view_func(template)()

	return render_template(template, **context), 200

def _is_public_template(template: str) -> bool:
	return any(exists(Path(pubdir) / template) for pubdir in app.public_template_dirs())

def _get_view_func(template: str) -> Callable[[], dict]:
	for pubdir in app.public_template_dirs():
		if exists(Path(pubdir) / template) and (root_module := app.get_module(pubdir)):
			page_module = importlib.import_module('.' + template[:-8].replace('/', '.'),  package=root_module.__name__)
			if view := getattr(page_module, 'view'):
				return view
	return lambda: {}
