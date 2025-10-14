# Configuration file for the Sphinx documentation builder.
# ELSA Integrated Spatial Planning Tool Documentation
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# =============================================================================
# PROJECT INFORMATION
# =============================================================================

project = 'ELSA Integrated Spatial Planning Tool'
copyright = '2025, UNDP & UNEP-WCMC'
author = 'UN Biodiversity Lab Team'
version = '1.0'
release = '1.0.1'

# =============================================================================
# GENERAL CONFIGURATION
# =============================================================================

# Add any Sphinx extension module names here
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
    'sphinx_design',           # For dropdowns and advanced layouts
    'sphinx_copybutton',       # Copy button for code blocks
]

# Add any paths that contain templates here, relative to this directory
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files
exclude_patterns = [
    '_build',
    'Thumbs.db', 
    '.DS_Store',
    '**.ipynb_checkpoints',
    'README.md'
]

# The master toctree document
master_doc = 'index'

# Source file suffixes
source_suffix = {
    '.rst': None,
    '.md': 'myst-parser',
}

# Build information
today_fmt = '%B %d, %Y'

# =============================================================================
# INTERNATIONALIZATION
# =============================================================================

language = 'en'
locale_dirs = ['locales/']
gettext_compact = False

# Language-specific settings for multi-language support
locale_docs = {
    'es': 'Spanish',
    'fr': 'French', 
    'ru': 'Russian',
    'pt': 'Portuguese'
}

# =============================================================================
# HTML OUTPUT OPTIONS
# =============================================================================

# The theme to use for HTML and HTML Help pages
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel
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

# Add any paths that contain custom static files (such as style sheets)
html_static_path = ['_static']

# Custom CSS files
html_css_files = [
    'elsa-custom.css',
]

# Page titles
html_title = "ELSA Integrated Spatial Planning Tool - User's Guide"
html_short_title = "ELSA User Guide"

# Logo and favicon (uncomment and customize as needed)
# html_logo = '_static/unbl_logo.png'
# html_favicon = '_static/favicon.ico'

# Search configuration
html_search_language = 'en'
html_search_options = {'type': 'default'}

# External search integration
html_use_opensearch = 'https://docs.unbiodiversitylab.org'

# Version control links
html_context = {
    "display_github": True,
    "github_user": "UNDP-UNBL",
    "github_repo": "elsa-documentation",
    "github_version": "main",
    "conf_py_path": "/docs/",
}

# =============================================================================
# FIGURE AND TABLE NUMBERING
# =============================================================================

# Automatically number figures, tables and code-blocks
numfig = True
numfig_secnum_depth = 2
numfig_format = {
    'figure': 'Figure %s',
    'table': 'Table %s',
    'code-block': 'Listing %s',
    'section': 'Section %s',
}

# =============================================================================
# LATEX/PDF OUTPUT OPTIONS
# =============================================================================

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
    'preamble': r'''
        \usepackage{charter}
        \usepackage[defaultsans]{lato}
        \usepackage{inconsolata}
    ''',
}

# Grouping the document tree into LaTeX files
latex_documents = [
    ('index', 'ELSA-UserGuide.tex', 
     'ELSA Integrated Spatial Planning Tool User\'s Guide',
     'UN Biodiversity Lab Team', 'manual'),
]

# =============================================================================
# EPUB OUTPUT OPTIONS
# =============================================================================

epub_title = project
epub_author = author
epub_publisher = 'UN Biodiversity Lab'
epub_copyright = copyright

# =============================================================================
# EXTENSION CONFIGURATION
# =============================================================================

# Intersphinx mapping for cross-documentation links
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

# Napoleon settings for Google/NumPy style docstrings
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

# Copy button configuration
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True

# =============================================================================
# COMMON EXTERNAL LINKS
# =============================================================================

# Define common links used throughout the documentation
rst_epilog = """
.. _UN Biodiversity Lab: https://www.unbiodiversitylab.org
.. _KMGBF: https://www.cbd.int/conferences/2021-2022/cop-15/documents
.. _prioritizr: https://prioritizr.net/
.. _UNEP-WCMC: https://www.unep-wcmc.org/
.. _UNDP: https://www.undp.org/
"""

# =============================================================================
# CUSTOM SETUP FUNCTION
# =============================================================================

def setup(app):
    """Custom setup for ELSA documentation."""
    
    # Add custom CSS for ELSA content
    app.add_css_file('elsa-custom.css')
    
    # Add custom directives if needed in the future
    # app.add_directive('elsa-example', ELSAExampleDirective)
    
    return {
        'version': version,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }