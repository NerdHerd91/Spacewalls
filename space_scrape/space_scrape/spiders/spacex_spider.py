import scrapy

class SpaceXSpider(scrapy.Spider):
    name = "spacex"
    allows_domains = ["spacex"]
    start_urls = [
            "http://www.spacex.com/media"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
