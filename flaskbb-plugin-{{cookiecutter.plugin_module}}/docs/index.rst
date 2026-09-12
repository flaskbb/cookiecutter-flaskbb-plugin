{{ cookiecutter.plugin_name }}
{{ '=' * cookiecutter.plugin_name|count }}

{{ cookiecutter.description }}


Installation
------------

.. code-block:: bash

    pip install flaskbb-plugin-{{ cookiecutter.plugin_module }}

Afterwards the plugin has to be installed from the management panel
(*Admin Panel -> Plugins -> Install*) so that its settings are added to
the database.


Settings
--------

============  =======  ================================
Setting       Default  Description
============  =======  ================================
``FOOBAR``    ``10``   The number of foo in bars.
============  =======  ================================

The settings are exposed prefixed with the plugin name, so ``FOOBAR`` is
available as ``flaskbb_config["{{ cookiecutter.plugin_module.upper() }}_FOOBAR"]``.


.. toctree::
    :maxdepth: 2

    api

{% if cookiecutter.repository %}

Links
-----

`source code <{{ cookiecutter.repository }}>`_ |
`issue tracker <{{ cookiecutter.repository }}/issues>`_
{%- endif %}
