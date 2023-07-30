from sqlalchemy import Column, String, DateTime, Text, ForeignKey, BigInteger
from sqlalchemy.orm import relationship

from ..configs.base import Base


class WorksInClickUp(Base):
    __tablename__ = 'works_in_clickup'

    work_id = Column(BigInteger, primary_key=True)
    task_clickup_id = Column(String(255), unique=True, nullable=False)
    work_title = Column(String(255), nullable=False)
    due_date = Column(DateTime, nullable=True)
    description = Column(Text, nullable=True)
    link_to_work = Column(Text, nullable=True)
    classrom_course_id = Column(BigInteger, ForeignKey('courses_in_classroom.course_id'))
    classroom_course = relationship('CoursesInClassroom', backref='course', lazy=True)

    def __str__(self):
        return self.work_title

    def __repr__(self):
        return self.work_title
