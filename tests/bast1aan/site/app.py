import os
from pathlib import Path

import bast1aan.site.app

from flask import Flask

from tests.bast1aan.site import public

package_path = Path(os.path.dirname(__file__))

_template_dir = os.path.abspath(package_path / 'templates')

_public_template_dir = os.path.abspath(package_path / 'public_j2')

bast1aan.site.app.add_template_dir(_template_dir)
bast1aan.site.app.add_template_dir(_public_template_dir, module=public, public=True)

app = Flask(__name__)
app.wsgi_app = bast1aan.site.app.app

