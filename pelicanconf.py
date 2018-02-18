#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Bill Tollett'
SITENAME = u'BillTollett.com'
SITEURL = ''
THEME = '/home/devbox/pelican-chameleon'
BS3_URL = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css'
BS3_JS  = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js'
BS3_THEME = 'https://maxcdn.bootstrapcdn.com/bootswatch/3.3.1/flatly/bootstrap.min.css'

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'Pacific/Honolulu'

DEFAULT_LANG = u'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
MENUITEMS = [
    ('Home', '/'),
    ('Archives', [
        ('Tags', '/tags.html'),
        ('Categories', '/categories.html'),
        ('Chronological', '/archives.html'),
        ]),
    ('Social', [
        ('Email', 'mailto: bill.tollett@gmail.com'),
        ('Github', 'https://github.com/wtollett'),
        ('Twitter', 'https://twitter.com/billt721'),
        ]),
    ]

# Social widget

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
