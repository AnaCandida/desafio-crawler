#!/usr/bin/env python
import sys
import time
from multiprocessing.context import Process

import pandas as pd
import schedule
from loguru import logger
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from imdb_crawler.spiders.imdb_spider import ImdbSpiderSpider
from pandas_dataframe import query_db_and_create_dataframe


def get_dataframe():
    df_database = query_db_and_create_dataframe()
    if df_database.empty:
        logger.info("No data")
    else:
        logger.info(f"\n Dados do banco de dados: \n {df_database}")


def run_spider():
    crawler = CrawlerProcess(get_project_settings())
    crawler.crawl(ImdbSpiderSpider)
    crawler.start()


def run_process():
    process = Process(target=run_spider)
    process.start()
    process.join()

    get_dataframe()


if __name__ == "__main__":
    if len(sys.argv) > 0 and sys.argv[1] == "run_once":
        logger.info("Rodando spider isoladamente")
        run_process()
    else:
        logger.info("Agendamento de spider realizado.")
        # schedule.every(SPIDER_FREQUENCY).minutes.do(run_process)
        schedule.every().day.at("14:50").do(run_process)
        # schedule.every().tuesday.at("14:00").do(run_process)

        # Manter o script em execução para que o agendamento funcione
        while True:
            schedule.run_pending()
            time.sleep(1)
