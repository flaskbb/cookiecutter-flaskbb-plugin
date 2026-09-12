# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
project = "{{ cookiecutter.plugin_name }}"
copyright = "{% now 'utc', '%Y' %}, {{ cookiecutter.author_name }}"
author = "{{ cookiecutter.author_name }}"
release = "{{ cookiecutter.version }}"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
html_theme = "alabaster"
html_theme_options = {
    "description": "{{ cookiecutter.description }}",
    "fixed_sidebar": True,
    "show_related": True,
}
html_title = "{{ cookiecutter.plugin_name }} Documentation"
html_static_path = ["_static"]
html_show_sourcelink = False

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "flask": ("https://flask.palletsprojects.com/en/latest/", None),
    "flaskbb": ("https://flaskbb.readthedocs.io/en/latest/", None),
    "jinja": ("https://jinja.palletsprojects.com/en/latest/", None),
    "pluggy": ("https://pluggy.readthedocs.io/en/latest/", None),
    "wtforms": ("https://wtforms.readthedocs.io/en/main/", None),
}

autodoc_member_order = "bysource"

root_doc = master_doc = "index"
