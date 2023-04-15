from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import declarative_base

from infra.models.courses_in_classroom import CoursesInClassroom

ModelBaseWorksInClickUp = declarative_base()


class WorksInClickUp(ModelBaseWorksInClickUp):
    __tablename__ = 'works_in_clickup'

    work_id = Column(Integer, primary_key=True)
    task_clickup_id = Column(Integer, unique=True, nullable=False)
    work_title = Column(String(255), nullable=False)
    due_date = Column(DateTime, nullable=True)
    description = Column(Text, nullable=True)
    link_to_work = Column(Text, nullable=True)
    classrom_course_id = Column(Integer, ForeignKey(CoursesInClassroom.course_name))

    def __str__(self):
        return self.work_title

    def __repr__(self):
        return self.work_title
