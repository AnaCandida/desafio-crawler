import logging

import scrapy
from scrapy_playwright.page import PageMethod

from imdb_crawler.items import ImdbCrawlerItem
from imdb_crawler.itemsloaders import ImdbCrawlerLoader


def should_abort_request(request):
    if request.resource_type in [
        "image"
    ]:  # Se incluir "script", "stylesheet", "font" aumentaria a performance, mas impacta na exibição dos elementos pro screenshot
        return True

    if request.method.lower() == "post":
        return True

    return False


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

    custom_settings = {
        "CONCURRENT_REQUESTS": 8,
        "PLAYWRIGHT_ABORT_REQUEST": should_abort_request,
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                meta={
                    "playwright": True,
                    "playwright_include_page": True,
                    "playwright_page_methods": [
                        PageMethod(
                            "wait_for_selector", "div.ipc-metadata-list-summary-item__c"
                        )
                    ],
                },
            )

    async def capture_screenshot(self, page, filename):
        await page.screenshot(path=filename, type="jpeg", quality=30)

    async def parse(self, response):
        self.logger.info("Starting data parsing")
        MOVIE_SELECTOR = "div.ipc-metadata-list-summary-item__c"
        TITLE_SELECTOR = ".ipc-title__text::text"
        SUMMARY_SELECTOR = "span.cli-title-metadata-item"
        STARS_SELECTOR = "span.ipc-rating-star--imdb::text"

        movies = response.css(MOVIE_SELECTOR)
        for movie in movies:
            title_text = movie.css(TITLE_SELECTOR).get()
            rank, title = title_text.split(".", 1)
            stars = movie.css(STARS_SELECTOR).get()
            summary_info = movie.css(SUMMARY_SELECTOR)
            year = summary_info.css(":nth-child(1)::text").get()
            duration = summary_info.css(":nth-child(2)::text").get()

            movie_loader = ImdbCrawlerLoader(item=ImdbCrawlerItem(), selector=movie)
            movie_loader.add_value("rank", rank)
            movie_loader.add_value("title", title)
            movie_loader.add_value("stars", stars)
            movie_loader.add_value("year", year)
            movie_loader.add_value("duration", duration)

            yield movie_loader.load_item()

        await self.capture_screenshot(
            page=response.meta["playwright_page"],
            filename="execution_proof/execution_proof.jpeg",
        )

        self.logger.info("Parsing finished")

        # next page
        next_page_url = response.css("li.next > a::attr(href)").extract_first()

        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)
