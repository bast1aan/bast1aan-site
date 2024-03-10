import os.path
from pathlib import Path

from flask import Flask
from . import views


package_path = Path(os.path.dirname(__file__))

_template_folder =  os.path.abspath(package_path / '..' / '..' / 'templates')

app = Flask(__name__, template_folder=_template_folder)

app.add_url_rule('/', view_func=views.template_view, defaults={'path': '/'})
app.add_url_rule('/<path:path>', view_func=views.template_view)
