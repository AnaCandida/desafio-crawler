import scrapy


class ImdbSpiderSpider(scrapy.Spider):
    name = "imdb_spider"
    allowed_domains = ["imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top/?ref_=nv_mv_250"]

    def parse(self, response):
        print("teste")
        # titles = response.css('h3.ipc-title__text::text').extract()
        titles = response.css(".ipc-title__text::text").getall()
        for title in titles:
            print(title.strip())
