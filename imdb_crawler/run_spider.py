# run_spider.py
import sys
import time
from multiprocessing.context import Process

import pandas as pd
import schedule
from loguru import logger
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from imdb_crawler.spiders.imdb_spider import ImdbSpiderSpider





def run_spider():
    crawler = CrawlerProcess(get_project_settings())
    crawler.crawl(ImdbSpiderSpider)
    crawler.start()


def run_process():
    process = Process(target=run_spider)
    process.start()
    process.join()



if __name__ == "__main__":
    logger.info("Rodando spider isoladamente")
    run_process()
else:
    logger.info("Agendamento de spider realizado.")
    # schedule.every(SPIDER_FREQUENCY).minutes.do(run_process)
    schedule.every().day.at("10:50").do(run_process)
    # schedule.every().tuesday.at("14:00").do(run_process)

    # Manter o script em execução para que o agendamento funcione
    while True:
        schedule.run_pending()
        time.sleep(1)
