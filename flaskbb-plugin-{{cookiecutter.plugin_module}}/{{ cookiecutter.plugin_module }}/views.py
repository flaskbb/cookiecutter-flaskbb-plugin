# -*- coding: utf-8 -*-
"""
    {{ cookiecutter.plugin_module }}.views
    {{ "~" * cookiecutter.plugin_module + "views"|count }}

    This module contains the views for the
    {{ cookiecutter.plugin_name }} Plugin.

    :copyright: (c) {% now "utc", "%Y" %} by {{ cookiecutter.author_name }}.
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from flask import Blueprint, current_app, flash, request
from flask_babelplus import gettext as _

from flaskbb.utils.helpers import render_template
from flaskbb.plugins.models import PluginRegistry


{{ cookiecutter.plugin_module }}_bp = Blueprint("{{ cookiecutter.plugin_module }}", __name__, template_folder="templates")


@{{ cookiecutter.plugin_module }}_bp.route("/")
def index():
    plugin = PluginRegistry.query.filter_by(name="{{ cookiecutter.plugin_name }}").first()
    if plugin and not plugin.settings:
        flash(_("Plugin is not installed."), "warning")

    return render_template("index.html", )