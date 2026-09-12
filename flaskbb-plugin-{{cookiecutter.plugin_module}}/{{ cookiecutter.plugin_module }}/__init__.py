"""
{{ cookiecutter.plugin_module }}
{{ "~" * cookiecutter.plugin_module|count }}

A {{ cookiecutter.plugin_name }} Plugin for FlaskBB.

:copyright: (c) {% now "utc", "%Y" %} by {{ cookiecutter.author_name }}.
:license: {{ cookiecutter.license }}, see LICENSE for more details.
"""

import os

from flask import Flask
from flask_babelplus import gettext as _
from flaskbb.display.navigation import NavigationLink
from flaskbb.settings import IntSetting, SettingGroup
from pluggy import HookimplMarker

from .views import {{ cookiecutter.plugin_module }}_bp

__version__ = "{{ cookiecutter.version }}"

hookimpl = HookimplMarker("flaskbb")


@hookimpl
def flaskbb_load_migrations():
    return os.path.join(os.path.dirname(__file__), "migrations")


@hookimpl
def flaskbb_load_translations():
    return os.path.join(os.path.dirname(__file__), "translations")


@hookimpl
def flaskbb_load_blueprints(app: Flask):
    app.register_blueprint(
        {{ cookiecutter.plugin_module }}_bp,
        url_prefix=app.config.get("PLUGIN_{{ cookiecutter.plugin_module.upper() }}_URL_PREFIX", "/{{ cookiecutter.plugin_module }}"),
    )


# the group key must match the plugin name registered in the
# flaskbb_plugins entry point
SETTINGS = SettingGroup(
    key="{{ cookiecutter.plugin_module }}",
    name="{{ cookiecutter.plugin_name }} Settings",
    description="{{ cookiecutter.description }}",
    settings=(
        IntSetting(
            key="FOOBAR",
            value=10,
            min=1,
            name="Foobar Number",
            description="The number of foo in bars.",
        ),
    ),
)


@hookimpl
def flaskbb_load_setting_groups():
    return SETTINGS


@hookimpl
def flaskbb_tpl_navigation_before():
    return NavigationLink(
        endpoint="{{ cookiecutter.plugin_module }}.index",
        name=_("{{ cookiecutter.plugin_name }}"),
        icon="fas fa-home",
    )
