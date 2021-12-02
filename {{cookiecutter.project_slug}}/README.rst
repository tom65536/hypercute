{%- macro heading(text) -%}
{% for _ in text %}={% endfor %}
{{text}}
{% for _ in text %}={% endfor %}
{%- endmacro -%}
{{ heading(cookiecutter.project_slug) }}

.. todo::

   BADGES

Description
-----------

Installation
------------
You can install *{{cookiecutter.project_slug}}* via pip_ from PyPI_:

.. code:: console

   $ pip install {{cookiecutter.project_slug}}


Contributing
------------

Contributions are very welcome.
To learn more, see the `Contributor Guide`_.


License
-------

Distributed under the terms of the `{{cookiecutter.license.replace("-", " ")}} license`_,
*{{cookiecutter.project_slug}}* is free and open source software.

Issues
------

If you encounter any problems,
please `file an issue`_ along with a detailed description.


Credits
-------

This project was generated from the `hypercute Cookiecutter`_ template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _{{cookiecutter.license.replace("-", " ")}} license: https://opensource.org/licenses/{{cookiecutter.license}}
.. _PyPI: https://pypi.org/
.. _hypercute Cookiecutter: https://github.com/tom65536/hypercute
.. _file an issue: {{cookiecutter.issue_tracker_url}}
.. _pip: https://pip.pypa.io/

.. no-doc
.. _Contributor Guide: CONTRIBUTING.rst



