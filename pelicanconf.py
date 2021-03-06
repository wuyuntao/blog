#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from os import path

AUTHOR = 'Wu Yuntao'
SITENAME = 'from error import optimal'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

LOCALE = ('en_US', 'zh_CN')

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
)

# Social widget
SOCIAL = (
    ('GitHub', 'https://github.com/wuyuntao'),
    ('Twitter', 'https://twitter.com/wuyuntao'),
)

DEFAULT_PAGINATION = 10

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins', './extra_plugins']
PLUGINS = ['ipynb.markup', 'i18n_subsites']

# https://github.com/danielfrg/pelican-ipynbk
# Prevents pelican from trying to parse notebook checkpoint files
IGNORE_FILES = ['.ipynb_checkpoints']

# Theme
# https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3
THEME = './themes/pelican-bootstrap3'

JINJA_EXTENSIONS = ['jinja2.ext.i18n']

CUSTOM_CSS = 'css/custom.css'

STATIC_PATHS = ['images', 'css']

DISPLAY_CATEGORY_IN_BREADCRUMBS = True

BOOTSTRAP_NAVBAR_INVERSE = True

# A workaround to not use any pysegment stylesheets and use styles of ipynb plugin
PYGMENTS_STYLE = 'none'

BANNER = 'images/banner-saber.jpg'
#BANNER_SUBTITLE = 'Life is a big training data set to learn from errors and search for optimal decisions'
BANNER_ALL_PAGES = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
