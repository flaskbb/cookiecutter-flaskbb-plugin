# -*- coding: utf-8 -*-
"""
    {{ cookiecutter.plugin_module }}.views
    {{ "~" * cookiecutter.plugin_module|count }}~~~~~~

    This module contains the views for the
    {{ cookiecutter.plugin_name }} Plugin.

    :copyright: (c) {% now "utc", "%Y" %} by {{ cookiecutter.author_name }}.
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from flask import Blueprint, flash
from flask_babelplus import gettext as _

from flaskbb.utils.helpers import render_template
from flaskbb.plugins.models import PluginRegistry


{{ cookiecutter.plugin_module }}_bp = Blueprint("{{ cookiecutter.plugin_module }}_bp", __name__, template_folder="templates")


@{{ cookiecutter.plugin_module }}_bp.route("/")
def index():
    plugin = PluginRegistry.query.filter_by(name="{{ cookiecutter.plugin_name }}").first()
    if plugin and not plugin.is_installed:
        flash(_("Plugin is not installed."), "warning")

    return render_template("index.html", plugin=plugin)
