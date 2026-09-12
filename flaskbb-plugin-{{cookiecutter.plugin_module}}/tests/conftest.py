import pytest
from flaskbb.extensions import pluggy
from tests.fixtures.app import *
from tests.fixtures.forum import *
from tests.fixtures.user import *

import {{ cookiecutter.plugin_module }}
from {{ cookiecutter.plugin_module }}.views import {{ cookiecutter.plugin_module }}_bp


@pytest.fixture(scope="package", autouse=True)
def _register_{{ cookiecutter.plugin_module }}_blueprint(application):
    """Normally flaskbb_load_blueprints registers this for us. Doing it
    here directly makes the plugin's own templates resolvable without
    requiring an entry-point install."""
    if "{{ cookiecutter.plugin_module }}" not in application.blueprints:
        application.register_blueprint({{ cookiecutter.plugin_module }}_bp, url_prefix="/{{ cookiecutter.plugin_module }}")
    if not pluggy.is_registered({{ cookiecutter.plugin_module }}):
        pluggy.register({{ cookiecutter.plugin_module }}, name="{{ cookiecutter.plugin_module }}")
