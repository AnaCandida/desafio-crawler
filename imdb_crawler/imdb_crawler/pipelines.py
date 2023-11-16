import logging
import os

import psycopg2
from itemadapter import ItemAdapter


class ImdbCrawlerPipeline:
    def process_item(self, item, spider):
        return item
