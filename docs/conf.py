# ELSA Tool Documentation Configuration
# This configuration is designed for integration into existing Sphinx documentation

# Only define ELSA-specific settings if this is a standalone build
# When integrated, the parent conf.py will handle most configuration

import os
import sys

# Check if this is being built as part of a larger documentation project
is_standalone = not hasattr(sys.modules.get('__main__', None), '_sphinx_project_name')

if is_standalone:
    # -- Standalone Project Information --
    project = 'ELSA Integrated Spatial Planning Tool'
    copyright = '2025, UNDP & UNEP-WCMC'
    author = 'UN Biodiversity Lab Team'
    release = '1.0'
    
    # -- General configuration for standalone --
    extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.viewcode',
        'sphinx.ext.napoleon',
        'sphinx.ext.intersphinx',
        'sphinx_rtd_theme',
    ]
    
    templates_path = ['_templates']
    exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
    
    # -- HTML output options for standalone --
    html_theme = 'sphinx_rtd_theme'
    html_static_path = ['_static']
    
    # Theme options
    html_theme_options = {
        'logo_only': False,
        'display_version': True,
        'prev_next_buttons_location': 'bottom',
        'style_external_links': False,
        'style_nav_header_background': '#2980B9',
        'collapse_navigation': True,
        'sticky_navigation': True,
        'navigation_depth': 4,
        'includehidden': True,
        'titles_only': False
    }

# -- ELSA-specific configuration (always applied) --

# Custom roles and directives for ELSA documentation
def setup(app):
    """Custom setup for ELSA documentation."""
    
    # Add custom CSS for ELSA content
    app.add_css_file('elsa-custom.css')
    
    # Add custom directives if needed
    # app.add_directive('elsa-example', ELSAExampleDirective)
    
    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

# -- ELSA-specific settings --

# Figure numbering for ELSA figures
numfig_secnum_depth = 2
numfig_format = {
    'figure': 'Figure %s',
    'table': 'Table %s',
    'code-block': 'Listing %s',
}

# ELSA-specific intersphinx mappings
elsa_intersphinx_mapping = {
    'unbl': ('https://www.unbiodiversitylab.org/docs/', None),
    'prioritizr': ('https://prioritizr.net/', None),
}

# Merge with existing intersphinx mapping if present
if 'intersphinx_mapping' in globals():
    intersphinx_mapping.update(elsa_intersphinx_mapping)
else:
    intersphinx_mapping = elsa_intersphinx_mapping

# -- LaTeX output options (for PDF generation) --
elsa_latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
    'preamble': r'''
        \usepackage{charter}
        \usepackage[defaultsans]{lato}
        \usepackage{inconsolata}
    ''',
}

elsa_latex_documents = [
    ('elsa/index', 'ELSA-UserGuide.tex', 
     'ELSA Integrated Spatial Planning Tool User\'s Guide',
     'UN Biodiversity Lab Team', 'manual'),
]

# Apply LaTeX settings if this is standalone
if is_standalone:
    latex_elements = elsa_latex_elements
    latex_documents = elsa_latex_documents

# -- Search and accessibility --

# Language-specific settings
language = 'en'
html_search_language = 'en'

# Accessibility improvements
html_use_opensearch = 'https://docs.unbiodiversitylab.org'

# -- External links and references --

# Common external links used in ELSA documentation
rst_epilog = """
.. _UN Biodiversity Lab: https://www.unbiodiversitylab.org
.. _KMGBF: https://www.cbd.int/conferences/2021-2022/cop-15/documents
.. _prioritizr: https://prioritizr.net/
.. _UNEP-WCMC: https://www.unep-wcmc.org/
.. _UNDP: https://www.undp.org/
"""

# -- Version and build information --
# These can be overridden by the parent configuration

version = '1.0'
release = '1.0.0'

# Build information
today_fmt = '%B %d, %Y'

# -- File patterns --
exclude_patterns = [
    '_build',
    'Thumbs.db', 
    '.DS_Store',
    '**.ipynb_checkpoints',
    'README.md'
]

# Source file suffixes
source_suffix = {
    '.rst': None,
    '.md': 'myst-parser',
}

# Master document
master_doc = 'index'

# -- Custom CSS for integration --
html_css_files = [
    'elsa-custom.css',
]

# -- Conditional configuration based on build context --
def configure_for_integration():
    """Apply settings when integrated into larger documentation."""
    global html_title, html_short_title
    
    # Use section-specific titles when integrated
    html_title = "ELSA Tool Documentation"
    html_short_title = "ELSA Tool"

def configure_for_standalone():
    """Apply settings when built as standalone documentation."""
    global html_title, html_short_title, html_logo
    
    # Use full project title for standalone
    html_title = "ELSA Integrated Spatial Planning Tool - User's Guide"
    html_short_title = "ELSA User Guide"
    
    # Add logo if available
    # html_logo = '_static/unbl_logo.png'

# Apply appropriate configuration
if is_standalone:
    configure_for_standalone()
else:
    configure_for_integration()# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ELSA Integrated Spatial Planning Tool'
copyright = '2025, UNDP & UNEP-WCMC'
author = 'UN Biodiversity Lab Team'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Theme options
html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': '#2980B9',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# Custom CSS (optional)
html_css_files = [
    'custom.css',
]

# Logo (optional - add if you have UNBL logo)
# html_logo = '_static/unbl_logo.png'

# Favicon (optional)
# html_favicon = '_static/favicon.ico'

# -- Options for LaTeX output -----------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'letterpaper',
    
    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '10pt',
    
    # Additional stuff for the LaTeX preamble.
    'preamble': r'''
        \usepackage{charter}
        \usepackage[defaultsans]{lato}
        \usepackage{inconsolata}
    ''',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', 'ELSA-UserGuide.tex', 'ELSA Integrated Spatial Planning Tool User\'s Guide',
     'UN Biodiversity Lab Team', 'manual'),
]

# -- Options for EPUB output ------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# -- Extension configuration -------------------------------------------------

# Intersphinx mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

# Napoleon settings (for Google/NumPy style docstrings)
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

# -- Custom settings ---------------------------------------------------------

# Number figures, tables and code-blocks automatically
numfig = True
numfig_format = {
    'figure': 'Figure %s',
    'table': 'Table %s',
    'code-block': 'Listing %s',
    'section': 'Section %s',
}

# Show "Edit on GitHub" links (customize as needed)
html_context = {
    "display_github": True,
    "github_user": "your-organization",
    "github_repo": "elsa-user-guide",
    "github_version": "main",
    "conf_py_path": "/docs/",
}

# -- Search and index options -----------------------------------------------

# Language for search index
html_search_language = 'en'

# Minimum word length for search
html_search_options = {'type': 'default'}

# # Enable search highlighting
# html_search_scorer = '_static/searchtools.js'