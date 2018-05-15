# -*- coding: utf-8 -*- #

from __future__ import unicode_literals


AUTHOR = 'André Caron'
SITENAME = 'SaladHappy'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Montreal'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = (
    ('Powered by Pelican', 'http://getpelican.com/'),
)
SOCIAL = (
    ('Twitter', 'https://twitter.com/mister_caron'),
    ('GitHub', 'https://github.com/AndreLouisCaron'),
)
DEFAULT_PAGINATION = 10
DEFAULT_METADATA = {
    'status': 'draft',
}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
