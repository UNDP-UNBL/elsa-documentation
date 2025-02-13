# Configuration file for the Sphinx documentation builder.
#
# See full documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sphinx_bootstrap_theme
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "ELSA Online Documentation"
copyright = "2025, UN Biodiversity Lab - UNDP"
author = "ELSA Core Team"


# -- General configuration ---------------------------------------------------

language = 'en'  # Default language is English

# Define locale directory where translations will be stored
locale_dirs = ['locales/']
gettext_compact = False  # Ensures separate .po files per source file

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton"
]

intersphinx_mapping = {
    "rtd": ("https://docs.readthedocs.io/en/stable/", None),
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for EPUB output
# epub_show_urls = "footnote"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
pygments_style = "friendly"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]

# (Optional) Logo. Should be small enough to fit the navbar (ideally 24x24).
# Path should be relative to the ``_static`` files directory.
# html_logo = "my_logo.png"

# # Theme options are theme-specific and customize the look and feel of a
# # theme further.
# html_theme_options = {
#     # Navigation bar title. (Default: ``project`` value)
#     'navbar_title': project,

#     # Tab name for entire site. (Default: "Site")
#     'navbar_site_name': "Home",

#     # A list of tuples containing pages or urls to link to.
#     # Valid tuples should be in the following forms:
#     #    (name, page)                 # a link to a page
#     #    (name, "/aa/bb", 1)          # a link to an arbitrary relative url
#     #    (name, "http://example.com", True) # arbitrary absolute url
#     # Note the "1" or "True" value above as the third argument to indicate
#     # an arbitrary url.
#     'navbar_links': [
#         ("UNBL", "https://unbiodiversitylab.org", True),
#         ("Link", "http://example.com", True),
#     ],

#     # Render the next and previous page links in navbar. (Default: true)
#     'navbar_sidebarrel': True,

#     # Render the current pages TOC in the navbar. (Default: true)
#     'navbar_pagenav': True,

#     # Tab name for the current pages TOC. (Default: "Page")
#     'navbar_pagenav_name': "Page",

#     # Global TOC depth for "site" navbar tab. (Default: 1)
#     # Switching to -1 shows all levels.
#     'globaltoc_depth': 2,

#     # Include hidden TOCs in Site navbar?
#     #
#     # Note: If this is "false", you cannot have mixed ``:hidden:`` and
#     # non-hidden ``toctree`` directives in the same page, or else the build
#     # will break.
#     #
#     # Values: "true" (default) or "false"
#     'globaltoc_includehidden': "true",

#     # HTML navbar class (Default: "navbar") to attach to <div> element.
#     # For black navbar, do "navbar navbar-inverse"
#     'navbar_class': "navbar navbar-inverse",

#     # Fix navigation bar to top of page?
#     # Values: "true" (default) or "false"
#     'navbar_fixed_top': "true",

#     # Location of link to source.
#     # Options are "nav" (default), "footer" or anything else to exclude.
#     'source_link_position': "nav",

#     # Bootswatch (http://bootswatch.com/) theme.
#     #
#     # Options are nothing (default) or the name of a valid theme
#     # such as "cosmo" or "sandstone".
#     'bootswatch_theme': "united",

#     # Choose Bootstrap version.
#     # Values: "3" (default) or "2" (in quotes)
#     'bootstrap_version': "3",
# }