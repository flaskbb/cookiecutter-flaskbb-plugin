# -*- coding: utf-8 -*-
"""
    flaskbb.plugins.{{ cookiecutter.plugin_identifier }}.views
    ~~~~~~~~~~~~~~~~{{ '~' * cookiecutter.plugin_identifier|count }}~~~~~~

    This module contains the {{ cookiecutter.plugin_identifier }} view.

    :copyright: (c) 2016 by {{ cookiecutter.full_name }}.
    :license: BSD License, see LICENSE for more details.
"""
from flask import Blueprint
from flask_plugins import get_plugin_from_all

from flaskbb.utils.helpers import render_template

# You can modify this to your liking
plugin_bp = Blueprint("{{ cookiecutter.plugin_identifier }}", __name__, template_folder="templates")


def inject_navigation_link():
    return render_template("navigation_link.html")


@plugin_bp.route("/")
def index():
    plugin_obj = get_plugin_from_all("{{ cookiecutter.plugin_identifier }}")
    return render_template("{{ cookiecutter.plugin_identifier }}.html", plugin_obj=plugin_obj)
