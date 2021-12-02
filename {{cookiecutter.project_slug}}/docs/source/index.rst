.. include:: ../README.rst
   :end-before: github-only

.. _Contributor Guide: contributing.html

Documentation
-------------

This part of the documentation guides you through all of the library's
usage patterns.

.. toctree::
   :maxdepth: 2



Examples
--------

.. toctree::
   :glob:

   examples/*

API Reference
-------------

If you are looking for information on a specific function, class, or
method, this part of the documentation is for you.

.. autosummary::
   :toctree: _autosummary
   :template: custom-module-template.rst
   :recursive:

   {{cookiecutter.package_name}}


Miscellaneous Pages
-------------------

.. toctree::
   :maxdepth: 2

   license
   changes

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. bibliography::
