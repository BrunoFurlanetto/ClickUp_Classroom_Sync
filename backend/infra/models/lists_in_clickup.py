from sqlalchemy import Column, String, BigInteger, ForeignKey
from sqlalchemy.orm import relationship

from backend.infra.configs.base import Base

from backend.infra.models.spaces import Spaces


class ListsInClickUp(Base):
    __tablename__ = 'lists_in_clickup'

    list_id = Column(BigInteger, primary_key=True, autoincrement=False)
    list_name = Column(String(255), nullable=False)
    clickup_space = Column(BigInteger, ForeignKey('spaces.space_id'), nullable=False)
    space = relationship('Spaces', backref='space', lazy=True)

    def __str__(self):
        return self.list_name
