"""
Author :- Mandar Sawant
Email :- mandar.sawant95@gmail.com

"""
"""
Crawler :- To fetch all the required Urls. These urls will be used by selenium spider to crawl manually.

"""
from scrapy import *
from ..import items

class LocalbanyaUrlsSpider(Spider):

    # Name of the spider
    # Same name will be used in command line to start crawling
    # Command to run the spider "scrapy crawl localbanyaUrls"
    name = "localbanyaUrls"

    # Giving bound to spider i.e crawling is allowed to below specified domain only
    # Spider is restricted to visit other domains
    allowed_domains = ["http://www.localbanya.com"]

    # Crawler will start crawling from this url.
    start_urls = ["http://www.localbanya.com"]

    # Call back function provided by the scrapy to parse the visited url
    def parse(self, response):
        # Retrive response
        sel = Selector(response)

        # Fetch all urls
        urls = sel.xpath('//a[@id = "url"]/@href').extract()

        # Iterate over each url and save it using yield
        for url in urls:
            urlItem = items.Url()
            urlItem['navigation_url'] = url
            yield urlItem

