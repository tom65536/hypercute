"""Sphinx config file.

The actual configuration is in this projects `pyproject.toml``.
Look for the section ``[tool.sphinx-pyproject]``.
"""
from sphinx_pyproject import SphinxConfig


config = SphinxConfig('../../pyproject.toml', globalns=globals())
