import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()


class DBConnectionHandler:
    def __init__(self):
        self.__connection_string = os.getenv('url_db')
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)

        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        Session = sessionmaker(bind=self.__engine)
        self.session = Session()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
