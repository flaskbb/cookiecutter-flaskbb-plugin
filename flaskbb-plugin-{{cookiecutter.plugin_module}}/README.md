{{ cookiecutter.plugin_name }}
{{ '=' * cookiecutter.plugin_name|count }}


{{ cookiecutter.description}}


Installation
------------

Install *flaskbb-plugin-{{ cookiecutter.plugin_name }}* with
``pip install flaskbb-plugin-{{ cookiecutter.plugin_name }}``


License
-------
This project is licensed under the terms of the
{% if cookiecutter.license == "BSD" %}
[BSD License](/LICENSE)
{% elif cookiecutter.license == "MIT" %}
[MIT License](/LICENSE)
{% endif %}
