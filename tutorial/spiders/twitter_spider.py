"""
This file is referenced from 
https://realpython.com/blog/python/web-scraping-with-scrapy-and-mongodb/
"""

import scrapy
from scrapy.selector import Selector

from tutorial.items import TwitterItem

class TwitterSpider(scrapy.Spider):
    name = "twitter"
    allowed_domains = ["twitter.com"]
    search = "UB"
    start_urls = [
            "https://twitter.com/search?q=%23"+search+"%20lang%3Aen&src=typd"
            ]

    def parse(self, response):
        messages = Selector(response).xpath('//p[@class="js-tweet-text tweet-text"]//text()[normalize-space()]')
        
        for msg in messages:
            item = TwitterItem() 
            tmp = msg.extract()
            if tmp != "#" and tmp != self.search and tmp != "@":
                item['text'] = tmp
                print item['text']
            yield item
