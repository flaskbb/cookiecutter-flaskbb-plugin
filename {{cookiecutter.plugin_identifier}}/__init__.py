# -*- coding: utf-8 -*-
"""
    flaskbb.plugins.portal
    ~~~~~~~~~~~~~~~~~~~~~~

    A Portal Plugin for FlaskBB.

    :copyright: (c) 2014 by the FlaskBB Team.
    :license: BSD, see LICENSE for more details.
"""
from flask_plugins import connect_event

from flaskbb.plugins import FlaskBBPlugin
from flaskbb.utils.populate import (create_settings_from_fixture,
                                    delete_settings_from_fixture)
from flaskbb.forum.models import Forum

from .views import {{ cookiecutter.plugin_identifier }}, inject_navigation_link

__version__ = "0.1"
__plugin__ = "HelloWorld"


fixture = (
    ('plugin_{{ cookiecutter.plugin_identifier }}', {
        'name': "{{ cookiecutter.plugin_name }} Settings",
        "description": "Configure the {{ cookiecutter.plugin_name }} Plugin",
        "settings": (
            ('{{ cookiecutter.plugin_identifier }}_display_in_navigation', {
                'value':        True,
                'value_type':   "boolean",
                'name':         "Show Link in Navigation",
                'description':  "If enabled, it will show the link in the navigation",
                'extra': {"min": 1},
            }),
        ),
    }),
)


class {{ cookiecutter.plugin_classname }}(FlaskBBPlugin):
    settings_key = 'plugin_{{ cookiecutter.plugin_identifier }}'

    def setup(self):
        self.register_blueprint({{ cookiecutter.plugin_identifier }}, url_prefix="/{{ cookiecutter.project_name.lower().replace(' ', '-') }}")
        connect_event("before-first-navigation-element", inject_navigation_link)

    def install(self):
        create_settings_from_fixture(fixture)

    def uninstall(self):
        delete_settings_from_fixture(fixture)
