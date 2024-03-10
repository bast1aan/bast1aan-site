from os.path import exists
from pathlib import Path

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

	return render_template(template), 200

def _is_public_template(template: str) -> bool:
	return any(exists(Path(pubdir) / template) for pubdir in app.public_template_dirs())
