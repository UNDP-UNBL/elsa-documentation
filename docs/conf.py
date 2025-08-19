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
        'sphinx_design',
        'sphinx_copybutton'
    ]
    
    templates_path = ['_templates']
    exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
    
    # -- HTML output options for standalone --
    html_theme = 'sphinx_rtd_theme'
    
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

# Internationalization
language = 'en'  # Default language
html_search_language = 'en'

locale_dirs = ['locale/']
gettext_compact = False

# Language-specific settings
locale_docs = {
    'es': 'Spanish',
    'fr': 'French', 
    'ru': 'Russian',
    'pt': 'Portuguese'
}


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