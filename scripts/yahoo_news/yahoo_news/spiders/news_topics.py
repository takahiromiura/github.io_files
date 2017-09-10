from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from yahoo_news.items import YahooNewsItem

class NewCrawlSpider(CrawlSpider):
    name = 'news_topics'
    allowed_domains = ['news.yahoo.co.jp']
    start_urls = ['http://news.yahoo.co.jp/']
    rules = (
        Rule(LinkExtractor(allow=r'/pickup/\d+$'), callback='parse_topics'),
    )

    def parse_topics(self, response):
        """
        トピックスのページからタイトルと本文を抜き出す
        """
        item = YahooNewsItem()
        item['title'] = response.css('.newsTitle ::text').extract_first()
        item['contents'] = response.css('.hbody ::text').extract_first()
        yield item
