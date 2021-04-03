# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Dblp1Item(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    href = scrapy.Field()
    author_name = scrapy.Field()
    journal_list = scrapy.Field()
    publish_date = scrapy.Field()
    abstract = scrapy.Field()
    article_keywords = scrapy.Field()
    controlled_index_keywords = scrapy.Field()
    noncontrolled_index_keywords = scrapy.Field()
    author_keywords = scrapy.Field()

