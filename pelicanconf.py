#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import datetime

AUTHOR = 'yscman'
SITENAME = 'Epic Gurps'
SITEURL = 'rpg-gurps.github.io'
SITETITLE = "JG Dungeon"
SITESUBTITLE = "Bloody Adventures"
SITEDESCRIPTION = "A place where luck and wits speak volumes"
SITELOGO = 'images/logo_heros_rpg.jpeg'
FAVICON = '/images/favicon.ico'
# BROWSER_COLOR = "#333333"
# PYGMENTS_STYLE = "monokai"
DEFAULT_LANG = 'en'

PATH = 'content'
OUTPUT_PATH = "output"

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

THEME = "notmyidea-cms"

# ROBOTS = "index, follow"

#PLUGIN_PATHS = ['./pelican-plugins']

#PLUGINS = ['i18n_subsites']

#JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

#I18N_TEMPLATES_LANG = "en"
#DEFAULT_LANG = "en"
#OG_LOCALE = "en_US"
#LOCALE = "en_US"

DATE_FORMATS = {
    "en": "%B %d, %Y",
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

SOCIAL = (
    ("github", "https://github.com/rpg-gurps"),
)

#MENUITEMS = (
#    ("Archives", "/archives.html"),
#    ("Categories", "/categories.html"),
#    ("Tags", "/tags.html"),
#)


DEFAULT_PAGINATION = 10

STATIC_PATHS = ["images", "extra"]

EXTRA_PATH_METADATA = {
    "extra/ads.txt": {"path": "ads.txt"},
    "extra/CNAME": {"path": "CNAME"},
    "extra/favicon.ico":{"path":"favicon.ico"}
}

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

