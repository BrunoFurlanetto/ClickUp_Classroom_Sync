from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

ModelBaseListsInClickUp = declarative_base()


class ListsInClickUp(ModelBaseListsInClickUp):
    __tablename__ = 'lists_in_clickup'

    list_id = Column(Integer, primary_key=True)
    list_name = Column(String, nullable=False)
    space_id = Column(Integer, nullable=False, unique=True)

    def __str__(self):
        return self.list_name
