# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiadetailItem(scrapy.Item):
    house_code = scrapy.Field()
    price_content = scrapy.Field()
    price = scrapy.Field()
    tags = scrapy.Field()
    house_type = scrapy.Field()
    sub_way = scrapy.Field()
    house_comment = scrapy.Field()
    upload_date = scrapy.Field()
    square = scrapy.Field()
    direct = scrapy.Field()
    base_info_str = scrapy.Field()
    community_code = scrapy.Field()
    community = scrapy.Field()
    community_link = scrapy.Field()

