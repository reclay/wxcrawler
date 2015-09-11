# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class WxSpiderItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    mid=Field()
    title =Field()
    des=Field()
    url=Field()
    content=Field()
    time=Field()
    author=Field()
    editor=Field()
    html=Field() 