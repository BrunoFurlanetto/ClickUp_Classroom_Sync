from sqlalchemy import Column, Integer, String, BigInteger
from sqlalchemy.orm import declarative_base, relationship

from infra.configs.base import Base


class ListsInClickUp(Base):
    __tablename__ = 'lists_in_clickup'

    list_id = Column(BigInteger, primary_key=True, autoincrement=False)
    list_name = Column(String(255), nullable=False)
    space_id = Column(String(50), nullable=False)

    def __str__(self):
        return self.list_name
