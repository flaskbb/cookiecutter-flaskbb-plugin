{%- set license_classifiers = {
    "MIT License": "License :: OSI Approved :: MIT License",
    "BSD License": "License :: OSI Approved :: BSD License",
    "GPLv3": "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Apache Software License 2.0": "License :: OSI Approved :: Apache Software License"
}
-%}
# -*- coding: utf-8 -*-
"""
    {{ cookiecutter.plugin_module }}
    {{ "~" * cookiecutter.plugin_module|count }}

    {{ cookiecutter.description }}

    :copyright: (c) {% now "utc", "%Y" %} by {{ cookiecutter.author_name }}.
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
import ast
import re
from setuptools import find_packages, setup
from setuptools.command.install import install


with open("{{ cookiecutter.plugin_module }}/__init__.py", "rb") as f:
    version_line = re.search(
        r"__version__\s+=\s+(.*)", f.read().decode("utf-8")
    ).group(1)
    version = str(ast.literal_eval(version_line))


class InstallWithTranslations(install):
    def run(self):
        # https://stackoverflow.com/a/41120180
        from babel.messages.frontend import compile_catalog  # noqa
        compiler = compile_catalog(self.distribution)
        option_dict = self.distribution.get_option_dict("compile_catalog")
        compiler.domain = [option_dict["domain"][1]]
        compiler.directory = option_dict["directory"][1]
        compiler.run()
        super().run()


setup(
    name="flaskbb-plugin-{{ cookiecutter.plugin_module }}",
    version=version,
    url="{{ cookiecutter.website }}",
{%- if cookiecutter.license in license_classifiers %}
    license="{{ cookiecutter.license }}",
{%- endif %}
    author="{{ cookiecutter.author_name.replace('\"', '\\\"') }}",
    author_email="{{ cookiecutter.email }}",
    description="{{ cookiecutter.description }}",
    long_description=__doc__,
    keywords="flaskbb plugin",
    cmdclass={"install": InstallWithTranslations},
    packages=find_packages("."),
    include_package_data=True,
    package_data={
        "": ["{{ cookiecutter.plugin_module }}/translations/*/*/*.mo",
             "{{ cookiecutter.plugin_module }}/translations/*/*/*.po"]
    },
    zip_safe=False,
    platforms="any",
    entry_points={
        "flaskbb_plugins": [
            "{{ cookiecutter.plugin_name }} = {{ cookiecutter.plugin_module }}"
        ]
    },
    install_requires=[
        "FlaskBB"  # pin to a version to has pluggy integration
    ],
    setup_requires=[
        "Babel",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Environment :: Plugins",
        "Framework :: Flask",
        "Intended Audience :: Developers",
{%- if cookiecutter.license in license_classifiers %}
        "{{ license_classifiers[cookiecutter.license] }}",
{%- endif %}
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
