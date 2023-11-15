# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbCrawlerItem(scrapy.Item):
    rank = scrapy.Field()
    title = scrapy.Field()
    stars = scrapy.Field()
    year = scrapy.Field()
    duration = scrapy.Field()
