from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger
from sqlalchemy.orm import declarative_base, relationship

from infra.configs.base import Base
from infra.models.lists_in_clickup import ListsInClickUp


class CoursesInClassroom(Base):
    __tablename__ = 'courses_in_classroom'
    clickup_list = relationship('ListsInClickUp', backref='list', lazy=True)

    course_id = Column(BigInteger, primary_key=True, autoincrement=False)
    course_name = Column(String(50), nullable=False)
    clickup_list_id = Column(BigInteger, ForeignKey('lists_in_clickup.list_id'))

    def __str__(self):
        return self.course_name
