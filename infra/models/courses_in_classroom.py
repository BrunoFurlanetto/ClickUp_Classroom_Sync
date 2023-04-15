from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

from infra.models.lists_in_clickup import ListsInClickUp

ModelBaseCoursesInClassroom = declarative_base()


class CoursesInClassroom(ModelBaseCoursesInClassroom):
    __tablename__ = 'courses_in_classroom'

    course_id = Column(Integer, primary_key=True)
    course_name = Column(String(50), nullable=False)
    clickup_list_id = Column(Integer, ForeignKey(ListsInClickUp.list_id))

    def __str__(self):
        return self.course_name
