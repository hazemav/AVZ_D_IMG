#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import scrapy
from scrapy.loader import XPathItemLoader
from scrapy.loader.processors import MapCompose, Join
from w3lib.html import replace_escape_chars
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from waseet.items import WaseetItem

class WaseetSpider(CrawlSpider):
    name = "waseet_spider.py"
    allowed_domains = ["eg.waseet.net"]
    start_urls = ["http://eg.waseet.net/ar/site/giza/real_estate/rent/listing/rent_apartments"
    ]
    rules = (
		Rule(LinkExtractor(allow=('giza/real_estate/'))),
        #Rule(LinkExtractor(allow=('listing/sale_apartments'))),
		Rule(LinkExtractor(allow=('sale*')),callback='parse_dir_contents'),
        Rule(LinkExtractor(allow=('rent*')),callback='parse_dir_contents'),

	)
#    def parse(self, response):
#        #xpath for tag that contains every adv //div[@class='col-sm-12 col-xs-12 listing-title']/a/@href
#        for href in response.xpath('//div[@class="col-sm-12 col-xs-12 listing-title"]/a/@href'):
#            url = response.urljoin(href.extract())
#            yield scrapy.Request(url, self.parse_dir_contents)
#        #xpath for tag that contains the next page button
#        next_page = response.xpath('//ul[@class="pagination pagination-sm"]/li/a[./span[contains(@class,"fa fa-angle-left flip")]]/@href')
#        if next_page:
#            url = response.urljoin(next_page[0].extract())
#            yield scrapy.Request(url, self.parse)


    def parse_dir_contents(self, response):
        item = WaseetItem()
        item['url'] = response.url
        item['W_phone_number'] = response.xpath('//a[@class="btn btn_shwphone "]/p/cite/text()').extract()
        item['W_title'] = response.xpath('//span[@class="hdline"]/span[@class="show_title"]/text()	').extract()
        item['W_posted_on'] = response.xpath('//p[@class="rght"]/span[@class="date"]/text()').extract()
        item['W_price'] = response.xpath('//big[@class="text-danger"]/span[@class="show_price"]/text()').extract()[0].strip()
        item['W_area'] = response.xpath('//p/span/i[@class="show_size"]/text()').extract()#[0].strip()
        item['W_neighbourhood'] = response.xpath('//span/i[@class="show_area"]/text()').extract()#[0].strip()
        item['W_bedroom'] = response.xpath('//span/i[@class="show_bedrooms"]/text()').extract()#[0].strip()
        item['W_bathroom'] = response.xpath('//span/i[@class="show_bathrooms"]/text()').extract()#[0].strip()
        #item['W_amenities'] = response.xpath('//dd[@class="u-ml__val"][7]/ul//li/text()').extract()
        item['W_desc'] = response.xpath('//p/i[@class="show_description"]/text()').extract()
        relative_img_urls=response.xpath('//a[@class="bigimg"]/img[@class="img-responsive iss"]/@src', encoding='utf-8').extract()
        item["image_urls"] = self.url_join(relative_img_urls, response)
        yield item

    def url_join(self, urls, response):
         joined_urls = []
         for url in urls:
             joined_urls.append(response.urljoin(url))
         return joined_urls
