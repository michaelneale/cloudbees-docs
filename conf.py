# -*- coding: utf-8 -*-

import sys
import os

# eventlet/gevent should not monkey patch anything.
os.environ["GEVENT_NOPATCH"] = "yes"
os.environ["EVENTLET_NOPATCH"] = "yes"
os.environ["CELERY_LOADER"] = "default"

this = os.path.dirname(os.path.abspath(__file__))

# If your extensions are in another directory, add it here. If the directory
# is relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
sys.path.append(os.path.join(os.pardir, "tests"))
sys.path.append(os.path.join(this, "_ext"))


# General configuration
# ---------------------

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.coverage',
              'sphinx.ext.pngmath',
              'sphinx.ext.intersphinx']

html_show_sphinx = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'CloudBees'
copyright = u'2009-2012, CloudBees, Inc.'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0'
# The full version, including alpha/beta/rc tags.
release = '1.0'

exclude_trees = ['.build']

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'colorful'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_use_smartypants = True

# If false, no module index is generated.
html_use_modindex = True

# If false, no index is generated.
html_use_index = True

html_theme = "cloudbees"
html_theme_path = ["_theme"]
html_sidebars = {
    'index': ['sourcelink.html', 'searchbox.html'],
    '**': ['globaltoc.html', 'relations.html',
           'sourcelink.html', 'searchbox.html'],
}

# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = 'Cloudbees Manual, Version {0}'.format(version)
epub_author = 'CloudBees'
epub_publisher = 'CloudBees'
epub_copyright = '2010-2013'

# The language of the text. It defaults to the language option
# or en if the language is not set.
epub_language = 'en'

# The scheme of the identifier. Typical schemes are ISBN or URL.
epub_scheme = 'ISBN'

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
epub_identifier = 'cloudbees.com'

# A unique identification for the text.
epub_uid = 'CloudBees Manual, Version {0}'.format(version)

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# The depth of the table of contents in toc.ncx.
epub_tocdepth = 3

