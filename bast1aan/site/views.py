from flask import typing as ft, render_template
from jinja2 import TemplateNotFound
from werkzeug.exceptions import NotFound


def template_view(path: str) -> ft.ResponseReturnValue:
	""" :raises NotFound """
	if path.endswith('/'):
		path += 'index.html'

	if not path.endswith('.html'):
		raise NotFound
	try:
		output = render_template(path[1:] + '.j2')
	except TemplateNotFound as e:
		raise NotFound from e

	return output, 200
