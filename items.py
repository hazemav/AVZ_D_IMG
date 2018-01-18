# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WaseetItem(scrapy.Item):
    #W_tablecount = scrapy.Field()
    W_posted_on = scrapy.Field()
    W_title=scrapy.Field()
    W_neighbourhood = scrapy.Field()
    W_area = scrapy.Field()
    W_price = scrapy.Field()
    W_phone_number = scrapy.Field()
    title = scrapy.Field()
    pubDate = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
    images = scrapy.Field()
    image_urls = scrapy.Field()
    W_bedroom=scrapy.Field()
    W_bathroom=scrapy.Field()
    #W_amenities=scrapy.Field()
    W_desc=scrapy.Field()
    url=scrapy.Field()