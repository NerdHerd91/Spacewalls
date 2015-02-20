import scrapy
import urlparse

from os.path import splitext, basename
from space_scrape.items import SpaceScrapeItem

class SpaceXSpider(scrapy.Spider):
    name = "hubble"
    allows_domains = ["hubble"]
    start_urls = [
            "http://www.spacex.com/media"
    ]

    base_domain = "http://www.spacex.com"

    # This is the intermediate path to the SpaceX images, it would be preferred
    # to simply re-scrape but have yet to figure out how to scrape a second
    # interval of new start_urls.
    intermediate_path = "/sites/spacex/files/styles/media_gallery_large/public/"


    def parse(self, response):
        for sel in response.xpath('//div[re:test(@class, "views-row")]/div/div/span'):
            thumbnail = sel.xpath('a/img/@src').extract()[0]
            thumbnail_path = urlparse.urlsplit(thumbnail).path
            thumbnail_filename, thumbnail_fileext = splitext(basename(thumbnail_path))

            item = SpaceScrapeItem()
            item['title'] = thumbnail_filename
            #item['link'] = self.base_domain + sel.xpath('a/@href').extract()[0]
            item['link'] = self.base_domain + self.intermediate_path + thumbnail_filename
            item['desc'] = thumbnail_filename
            yield item
