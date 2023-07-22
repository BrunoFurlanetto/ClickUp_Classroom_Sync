from sqlalchemy import Column, Integer, String, BigInteger

from infra.configs.base import Base


class Spaces(Base):
    __tablename__ = 'spaces'

    space_id = Column(BigInteger, primary_key=True, autoincrement=False)
    name_space = Column(String(255), nullable=False)

    def __str__(self):
        return self.name_space

    def __repr__(self):
        return self.name_space
