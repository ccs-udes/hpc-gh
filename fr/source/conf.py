# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Grappe GH'
copyright = '2026, CCS'
author = 'CCS'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = []

# templates_path = ['_templates']
# exclude_patterns = []

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_title = project

html_css_files = [
    'https://fonts.googleapis.com/css?family=Lato',
]

html_theme_options = {
    "light_css_variables": {
        "font-stack": "Lato, sans-serif",
        "font-stack--headings": "Lato, sans-serif",
    },
}

# html_static_path = ['_static']
