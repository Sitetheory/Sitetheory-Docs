# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from datetime import datetime

# import os
# import sys

# import sphinx_rtd_theme

# sys.path.insert(0, os.path.abspath('..'))
# sys.path.append(os.path.dirname(__file__))
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "readthedocs.settings.dev")

# from django.utils import timezone
#
# import django
#
# django.setup()
#
# sys.path.append(os.path.abspath('_ext'))
# extensions = [
#     'sphinx.ext.autosectionlabel',
#     'sphinx.ext.autodoc',
#     'sphinx.ext.intersphinx',
#     'sphinxcontrib.httpdomain',
#     'djangodocs',
#     'doc_extensions',
#     'sphinx_tabs.tabs',
#     'sphinx-prompt',
#     'recommonmark',
#     'notfound.extension',
#     'sphinx_search.extension',
# ]
# templates_path = ['_templates']

source_suffix = ['.rst']

master_doc = 'index'
project = u'Sitetheory'
copyright = '2015-{}, Sitetheory'.format(
    datetime.now().year
)
version = '1.0'
release = version
# exclude_patterns = ['_build']
# default_role = 'obj'
language = 'en'

# locale_dirs = [
#     'locale/',
# ]
# gettext_compact = False

# html_theme = 'sphinx_rtd_theme'
# html_static_path = ['_static']
# html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
# html_logo = 'img/logo.svg'
# html_theme_options = {
#     'logo_only': False,
#     'display_version': True,
# }
