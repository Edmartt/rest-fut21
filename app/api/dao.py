import logging
from .db import DatabaseManager


class QueryGenerator:

    def __init__(self, connector: DatabaseManager):
        self.connector = connector

    def select(self, query, *args) -> list:
        _, cursor = self.connector.get_db()
        try:
            cursor.execute(query, *args)
            result = cursor.fetchall()
            if result:
                return result
        except Exception as ex:
            logging.exception(ex)
            return [ex]
        finally:
            self.connector.close_db()
