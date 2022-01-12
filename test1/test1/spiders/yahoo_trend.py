import scrapy


class YahooTrendSpider(scrapy.Spider):
    name = 'yahoo_trend'
    allowed_domains = ['www.yahoo.co.jp']
    start_urls = ['https://www.yahoo.co.jp/']

    def parse(self, response):
        pass
