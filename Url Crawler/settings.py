# -*- coding: utf-8 -*-

# Scrapy settings for dirbot project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
from scrapy.settings.default_settings import DEPTH_LIMIT, DOWNLOAD_DELAY

BOT_NAME = 'dirbot'

SPIDER_MODULES = ['dirbot.spiders']
NEWSPIDER_MODULE = 'dirbot.spiders'
DOWNLOAD_DELAY = 10

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'dirbot (+http://www.yourdomain.com)'
