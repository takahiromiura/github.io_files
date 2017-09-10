# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YahooNewsItem(scrapy.Item):
    """
    ニュースのタイトルと内容の要約を表す Item
    """
    title = scrapy.Field()
    contents = scrapy.Field()
