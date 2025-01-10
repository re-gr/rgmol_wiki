# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0,os.path.abspath(os.path.join("..//..//rgmol//rgmol")))
sys.setrecursionlimit(1500)


project = 'rgmol'
copyright = '2025, re-gr'
author = 're-gr'
release = '0.1'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc","sphinx.ext.napoleon"]
napoleon_custom_sections = [('Returns', 'params_style'), ("Attributes","params_style")]

templates_path = ['_templates']
exclude_patterns = []




# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
# html_theme = "sphinxawesome_theme"
html_static_path = ['_static']

napoleon_use_rtype=True
napoleon_use_param=True