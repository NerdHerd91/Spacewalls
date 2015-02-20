import urlparse
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from os.path import splitext, basename
from space_scrape.items import SpaceScrapeItem

class SpaceXSpider(CrawlSpider):
    name = "spacex"
    allows_domains = ["spacex"]
    start_urls = [
            "http://www.spacex.com/media"
    ]

    rules = (Rule (SgmlLinkExtractor(allow=("/media-gallery/detail/.", ),
        restrict_xpaths=('//div[re:test(@class, "views-row")]/div/div/span',)),
        callback="parse_items", follow=True),)

    def parse_items(self, response):
        hxs = HtmlXPathSelector(response)
        link = hxs.select('//div[re:test(@id, "asset-image")]/img/@src').extract()[0]
        link_path = urlparse.urlsplit(link).path
        link_filename, link_fileext = splitext(basename(link_path))

        item = SpaceScrapeItem()
        item['title'] = basename(link_path)
        item['link'] = link
        item['desc'] = link_filename
        yield item
