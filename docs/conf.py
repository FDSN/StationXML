

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import re
import os
import subprocess
import sphinx_rtd_theme

def get_context():
    """Return the current RTD version or git branch name"""
    try:
        git_context = subprocess.check_output(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"]
        ).strip().decode("utf-8")

        # Check for RTD version, default to git_version if not on RTD
        context = os.getenv("READTHEDOCS_VERSION", git_context)

        return context
    except Exception:
        return ""

# -- Project information -----------------------------------------------------

project = 'StationXML'
copyright = '2022, International FDSN'
author = 'International FDSN'

# The full version, including alpha/beta/rc tags
version = '1.2'

# Documentation version, schema + date
# ALSO UPDATE the release documentation version in overview.rst
doc_version = version + ' (2022-02-25)'

# Allow |doc_version| to be used in RST
rst_epilog = '.. |doc_version| replace:: %s' % doc_version

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinxcontrib.contentui',
              'linuxdoc.rstFlatTable',      # Implementation of the 'flat-table' reST-directive
              #'sphinxcontrib.spelling',
             ]

spelling_word_list_filename=['spelling/text_words.txt',
                             'spelling/schema_words.txt',
                             ]

latex_maketitle = r'''
  \noindent\rule{\textwidth}{1pt}\par
    \begingroup % for PDF information dictionary
       \def\endgraf{ }\def\and{\& }%
       \pdfstringdefDisableCommands{\def\\{, }}% overwrite hyperref setup
       \hypersetup{pdfauthor={'''+author+r'''}, pdftitle={'''+project+r'''}}%
    \endgroup
  \begin{flushright}
    \sphinxlogo
    \sffamily\bfseries
    {\Huge '''+project+r''' }\par
    {\itshape\large '''+doc_version+r''' \releaseinfo}\par
    \vspace{25pt}
    {\Large
      \begin{tabular}[t]{c}
        '''+author+r'''
      \end{tabular}\kern-\tabcolsep}\par
    \vspace{25pt}
    \par
  \end{flushright}
  \setcounter{footnote}{0}
  \let\thanks\relax\let\maketitle\relax
'''

latex_elements = {
    'preamble': r'''
\input{mystyle.tex.txt}
\setlength{\tymin}{70pt}
    ''', #adds some macros and sets min width of most tables
    'classoptions': ',openany,oneside', #removes extra pages
    'maxlistdepth':'10',
    'maketitle': latex_maketitle
}

latex_additional_files = ["mystyle.tex.txt"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
# Note, some of these, like level-*, are included from other .rst files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store','examples',
                    'level-preamble.rst','level-network.rst','level-channel.rst',
                    'level-response.rst','level-station.rst','response-practical.rst']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 0,
    'sticky_navigation': False,
}
html_logo='_static/FDSN-logo.png'
html_favicon = '_static/favicon.ico'
html_title = 'FDSN StationXML'
html_show_sphinx = False
html_search_language = 'en'

navigation_depth = -2

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
  'css/custom.css',
  'css/theme_overrides.css',
]

html_js_files = [
  'js/sidebar_context.js'
]

# Enable sphinxmark for draft documentation
if get_context() == "draft":
    extensions.append("sphinxmark")
    sphinxmark_enable = True
    sphinxmark_div = "document"
