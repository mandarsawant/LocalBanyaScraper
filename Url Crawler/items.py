"""
Author :- Mandar Sawant
Email :- mandar.sawant95@gmail.com

"""

import scrapy

# Scrapy items are like Models which provides data structure to store scraped data.
class DirbotItem(scrapy.Item):
    # define the fields for your item here like:
    product_name = scrapy.Field()
    product_MRP_price = scrapy.Field()
    product_price = scrapy.Field()
    product_quantity = scrapy.Field()
    product_discount = scrapy.Field()

class Url(scrapy.Item):
    navigation_url = scrapy.Field()
