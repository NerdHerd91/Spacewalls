import scrapy
import urlparse

from os.path import splitext, basename
from space_scrape.items import SpaceScrapeItem

class NasaIodSpider(scrapy.Spider):
    name = "nasa-iod"
    allows_domains = ["nasa"]
    start_urls = [
            "http://www.nasa.gov/multimedia/imagegallery/iotd.html#lowerAccordion-set1-slide1"
    ]

    base_domain = "http://www.nasa.gov"

    # This is the intermediate path to the Nasa ImageOfDay images, it would be preferred
    # to simply re-scrape but have yet to figure out how to scrape a second
    # interval of new start_urls.
    intermediate_path = "/sites/default/files/thumbnails/image/"


    def parse(self, response):
        print response.body
        for sel in response.xpath('//li[re:test(@class, "slide")]/div/div'):
            thumbnail = sel.xpath('img/@src').extract()[0]
            thumbnail_path = urlparse.urlsplit(thumbnail).path
            thumbnail_filename, thumbnail_fileext = splitext(basename(thumbnail_path))

            item = SpaceScrapeItem()
            item['title'] = thumbnail_filename
            item['link'] = self.base_domain + self.intermediate_path + thumbnail_filename
            item['desc'] = thumbnail_filename
            yield item
