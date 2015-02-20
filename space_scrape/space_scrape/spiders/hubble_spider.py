import urlparse
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from os.path import splitext, basename
from space_scrape.items import SpaceScrapeItem

class HubbleSpider(CrawlSpider):
    name = "hubble"
    allows_domains = ["hubble"]
    start_urls = [
            "http://hubblesite.org/gallery/wallpaper/"
    ]

    rules = (Rule (SgmlLinkExtractor(allow=("/gallery/wallpaper/.", ),
        restrict_xpaths=('//div[re:test(@id, "ListBlock")]/a',)),
        callback="", follow=True), 
        Rule (SgmlLinkExtractor(allow=("/gallery/wallpaper/.", ),
            restrict_xpaths=('//li[re:test(@id, "wallpaper-1920x1200")]',)),
            callback="parse_items", follow=True))

    def parse_items(self, response):
        hxs = HtmlXPathSelector(response)
        link = hxs.select('//div[re:test(@class, "subpage-body")]/img/@src').extract()[0]
        link_path = urlparse.urlsplit(link).path
        link_filename, link_fileext = splitext(basename(link_path))

        item = SpaceScrapeItem()
        item['title'] = basename(link_path)
        item['link'] = link
        item['desc'] = link_filename
        yield item
