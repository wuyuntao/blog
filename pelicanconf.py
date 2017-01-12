#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

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

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
