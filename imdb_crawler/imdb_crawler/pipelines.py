import logging
import os

import psycopg2
from itemadapter import ItemAdapter
from psycopg2 import DataError, IntegrityError, OperationalError


class ImdbCrawlerPipeline:
    def process_item(self, item, spider):
        return item


class SavingToPostgresPipeline(object):
    def __init__(self):
        self.items_to_store = []

    def create_connection(self):
        logging.info("Connecting to the database")

        self.connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        )

        self.curr = self.connection.cursor()

    def close_connection(self):
        if self.connection:
            self.connection.commit()
            self.connection.close()
            logging.info("Database connection finished")

    def process_item(self, item, spider):
        try:
            self.items_to_store.append(item)
        except Exception as e:
            spider.logger.error(f"Error processing item: {e}")

        return item

    def store_db(self, items, spider):
        try:
            self.create_connection()

            values = [
                (
                    ItemAdapter(item).get("rank"),
                    ItemAdapter(item).get("title"),
                    ItemAdapter(item).get("stars"),
                    ItemAdapter(item).get("year"),
                    ItemAdapter(item).get("duration"),
                )
                for item in items
            ]

            self.curr.executemany(
                """INSERT INTO movies (rank, title, stars, year, duration)
                   VALUES (%s, %s, %s, %s, %s)
                   ON CONFLICT (rank) DO UPDATE
                   SET title = EXCLUDED.title,
                       stars = EXCLUDED.stars,
                       year = EXCLUDED.year,
                       duration = EXCLUDED.duration""",
                values,
            )

        except IntegrityError as integrity_error:
            spider.logger.error(f"IntegrityError: {integrity_error}")
            self.connection.rollback()

        except DataError as data_error:
            spider.logger.error(f"DataError: {data_error}")
            self.connection.rollback()

        except OperationalError as operational_error:
            spider.logger.error(f"OperationalError: {operational_error}")
            self.connection.rollback()



    def close_spider(self, spider):
        try:
            self.store_db(self.items_to_store, spider)
        except Exception as e:
            spider.logger.error(f"Error closing spider: {e}")

        self.close_connection()
        return self.items_to_store
