import logging

import scrapy

from imdb_crawler.items import ImdbCrawlerItem
from imdb_crawler.itemsloaders import ImdbCrawlerLoader


class ImdbSpiderSpider(scrapy.Spider):
    def __init__(self, *args, **kwargs):
        loggers = [
            logging.getLogger(name)
            for name in [
                "scrapy.spidermiddlewares.httperror",
                "scrapy.addons",
                "scrapy.extensions.telnet",
                "scrapy.crawler",
                "scrapy.middleware",
                "scrapy.statscollectors",
            ]
        ]

        for logger in loggers:
            logger.setLevel(logging.WARNING)

        super().__init__(*args, **kwargs)

    name = "imdb_spider"
    allowed_domains = ["imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top/?ref_=nv_mv_250"]

    def parse(self, response):
        self.logger.info("Starting data parsing")
        DIV_MOVIE_SELECTOR = "div.ipc-metadata-list-summary-item__c"
        TITLE_SELECTOR = ".ipc-title__text::text"
        SUMARY_SELECTOR = "span.cli-title-metadata-item"
        STARS_SELECTOR = "span.ipc-rating-star--imdb::text"

        divs_movies = response.css(DIV_MOVIE_SELECTOR)

        for div_movie in divs_movies:
            movie_loader = ImdbCrawlerLoader(item=ImdbCrawlerItem(), selector=div_movie)
            title_text = div_movie.css(TITLE_SELECTOR).get()
            rank, title = title_text.split(".", 1)
            movie_loader.add_value("rank", rank)
            movie_loader.add_value("title", title)
            movie_loader.add_css("stars", STARS_SELECTOR)
            movie_loader.add_css("year", f"{SUMARY_SELECTOR}:nth-child(1)::text")
            movie_loader.add_css("duration", f"{SUMARY_SELECTOR}:nth-child(2)::text")
            movie_loader.add_value("url", response.url)

            yield movie_loader.load_item()

        self.logger.info("Parsing finished")

        # next page
        next_page_url = response.css("li.next > a::attr(href)").extract_first()

        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)
