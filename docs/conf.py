

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


# -- Project information -----------------------------------------------------

project = 'StationXML'

# The full version, including alpha/beta/rc tags
release = '0.0.1'

version = '1.1.0'

author = ''

date= 'Jul 29, 2020'

def setup(app):
    app.add_css_file('css/custom.css')
    app.add_js_file('js/custom.js')

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinxcontrib.contentui',
              'linuxdoc.rstFlatTable',      # Implementation of the 'flat-table' reST-directive
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
    {\itshape\large '''+release+r''' \releaseinfo}\par
    \vspace{25pt}
    {\Large
      \begin{tabular}[t]{c}
        '''+author+r'''
      \end{tabular}\kern-\tabcolsep}\par
    \vspace{25pt}
    '''+date+r''' \par
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
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store','example_1.rst','examples','level-preamble.rst','level-network.rst','level-channel.rst','level-response.rst','level-station.rst', 'response-practical.rst']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
#
html_theme_options = {
    'navigation_depth': 0,
    'sticky_navigation': False,
}
html_logo='_images/fdsn-logo.png'

navigation_depth = -2

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',  # MTH: this was already added above
    'css/theme_overrides.css',
]

html_js_files = [
    'js/custom.js',
]
