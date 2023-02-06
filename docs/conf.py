# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Physics and Data Science'
copyright = '2023, Physics and Data Science group'
author = 'Alex, Fabienne, Simona, Josh, Jakub'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'myst_nb',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.imgmath',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

nbsphinx_execute = 'never'
nb_execution_mode = "off"
nb_execution_allow_errors = False