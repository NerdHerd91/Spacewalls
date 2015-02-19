import scrapy
import urlparse

from os.path import splitext, basename
from space_scrape.items import SpaceScrapeItem

class SpaceXSpider(scrapy.Spider):
    name = "spacex"
    allows_domains = ["spacex"]
    start_urls = [
            "http://www.spacex.com/media"
    ]

    base_domain = "http://www.spacex.com"

    def parse(self, response):
        for sel in response.xpath('//div[re:test(@class, "views-row")]/div/div/span'):
            thumbnail = sel.xpath('a/img/@src').extract()[0]
            thumbnail_path = urlparse.urlsplit(thumbnail).path
            thumbnail_filename, thumbnail_fileext = splitext(basename(thumbnail_path))

            item = SpaceScrapeItem()
            item['title'] = thumbnail_filename
            item['link'] = self.base_domain + sel.xpath('a/@href').extract()[0]
            item['desc'] = thumbnail_filename
            yield item
