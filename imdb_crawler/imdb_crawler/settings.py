# Scrapy settings for imdb_crawler project
import logging

BOT_NAME = "imdb_crawler"
SPIDER_MODULES = ["imdb_crawler.spiders"]
NEWSPIDER_MODULE = "imdb_crawler.spiders"

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
ROBOTSTXT_OBEY = True


LOG_LEVEL = "INFO"
LOG_SHORT_NAMES = False
LOG_STDOUT = True
LOG_FORMAT = "%(asctime)s [%(name)s] %(levelname)s: %(message)s"


COOKIES_ENABLED = False

TELNETCONSOLE_ENABLED = False

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
]


DOWNLOADER_MIDDLEWARES = {
    "imdb_crawler.middlewares.UARotatorMiddleware": 400,
    "scrapy.downloadermiddlewares.retry.RetryMiddleware": None,
}

DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

PLAYWRIGHT_BROWSER_TYPE = "chromium"
# PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT = 10000

FEEDS = {
    "outputs/movies.json": {
        "format": "json",
        "encoding": "utf8",
        "store_empty": False,
        "fields": None,
        "indent": 4,
        "item_export_kwargs": {
            "export_empty_fields": True,
        },
    },
}

DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "pt-br",
}

ITEM_PIPELINES = {
    "imdb_crawler.pipelines.ImdbCrawlerPipeline": 100,
    "imdb_crawler.pipelines.SavingToPostgresPipeline": 300,
}
