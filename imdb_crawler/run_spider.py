import time
from multiprocessing.context import Process

from loguru import logger
from pandas_dataframe import query_db_and_create_dataframe
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from imdb_crawler.spiders.imdb_spider import ImdbSpiderSpider


def get_dataframe():
    df_database = query_db_and_create_dataframe()
    if df_database.empty:
        logger.info("No data")
    else:
        logger.info(f"\n Database data: \n {df_database}")


def run_spider():
    crawler = CrawlerProcess(get_project_settings())
    crawler.crawl(ImdbSpiderSpider)
    crawler.start()


def execute_spider():
    process = Process(target=run_spider)
    process.start()
    process.join()
    get_dataframe()
