# Configuration file for the Sphinx documentation builder.
# Read https://www.sphinx-doc.org/en/master/usage/configuration.html for more options available

# import sphinx_pdj_theme

# -- Project information

project = 'IP2Location'
copyright = '2023, IP2Location'
author = 'IP2Location'

release = '8.10.0'
version = '8.10.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    # 'sphinx.ext.autodoc',
    # 'sphinx.ext.autosummary',
    # 'sphinx.ext.intersphinx',
    'myst_parser',
    'sphinx_copybutton',
    # "sphinxext.opengraph",
]

# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html

myst_enable_extensions = [
    # "amsmath",
    # "attrs_inline",
    "colon_fence",
    "deflist",
    # "dollarmath",
    "fieldlist",
    # "html_admonition",
    # "html_image",
    # "linkify",
    # "replacements",
    # "smartquotes",
    # "strikethrough",
    # "substitution",
    # "tasklist",
]

# https://myst-parser.readthedocs.io/en/latest/configuration.html#setting-html-metadata
# language = "en"
myst_html_meta = {
    # "description lang=en": "metadata description",
    # "description lang=fr": "description des métadonnées",
    "description": "IP2Location Python library enables user to query the geolocation information for an IP address.",
    "keywords": "IP2Location, Geolocation, IP location",
    "google-site-verification": "DeW6mXDyMnMt4i61ZJBNuoADPimo5266DKob7Z7d6i4",
    # "property=og:locale":  "en_US"
}

# OpenGraph metadata
ogp_site_url = "https://ip2location-python.readthedocs.io/en/latest"

# ogp_custom_meta_tags = [
    # '<meta name="description" content="IP2Location Python library enables user to query the geolocation information for an IP address.">',
# ]

# intersphinx_mapping = {
    # 'python': ('https://docs.python.org/3/', None),
    # 'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
# }
# intersphinx_disabled_domains = ['std']

# templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_book_theme'

# PDJ theme options, see the list of available options here: https://github.com/jucacrispim/sphinx_pdj_theme/blob/master/sphinx_pdj_theme/theme.conf
html_theme_options = {
    "use_edit_page_button": False,
    "use_source_button": False,
    "use_issues_button": False,
    "use_download_button": False,
    "use_sidenotes": False,
}

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'images/ipl-logo-square-1200.png'

# Favicon
html_favicon = 'images/favicon.ico'

html_title = "IP2Location Python"

# html_extra_path = ["googlead5f0f82eb100b8b.html"]

html_baseurl = "https://ip2location-python.readthedocs.io/en/latest/"