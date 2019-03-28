# -*- coding: utf-8 -*-
"""
    {{ cookiecutter.plugin_module }}
    {{ "~" * cookiecutter.plugin_module|count }}

    A {{ cookiecutter.plugin_name }} Plugin for FlaskBB.

    :copyright: (c) {% now "utc", "%Y" %} by {{ cookiecutter.author_name }}.
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
import os

from pluggy import HookimplMarker

from flaskbb.forum.models import Forum
from flaskbb.utils.forms import SettingValueType
from flaskbb.utils.helpers import render_template

from .views import {{ cookiecutter.plugin_module + "_bp" }}

__version__ = "{{ cookiecutter.version }}"


hookimpl = HookimplMarker("flaskbb")


# connect the hooks
@hookimpl
def flaskbb_load_migrations():
    return os.path.join(os.path.dirname(__file__), "migrations")


@hookimpl
def flaskbb_load_translations():
    return os.path.join(os.path.dirname(__file__), "translations")


@hookimpl
def flaskbb_load_blueprints(app):
    app.register_blueprint({{ cookiecutter.plugin_module + "_bp" }}, url_prefix="/{{ cookiecutter.plugin_module }}")


@hookimpl
def flaskbb_tpl_before_navigation():
    return render_template("{{ cookiecutter.plugin_module }}_navlink.html")


# plugin settings
SETTINGS = {
    "foobar": {
        "value": 10,
        "value_type": SettingValueType.integer,
        "name": "Foobar Number",
        "description": "The number of foo in bars.",
        "extra": {"min": 1},
    },
}
