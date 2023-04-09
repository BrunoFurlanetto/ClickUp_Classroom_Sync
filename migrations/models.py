from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class ListsInClickUp(Base):
    __tablename__ = 'lists_in_clickup'

    list_id = Column(Integer, primary_key=True)
    list_name = Column(String, nullable=False)
    space_id = Column(Integer, nullable=False, unique=True)

    def __str__(self):
        return self.list_name


class CoursesInClassroom(Base):
    __tablename__ = 'courses_in_classroom'

    course_id = Column(Integer, primary_key=True)
    course_name = Column(String(50), nullable=False)
    clickup_list_id = Column(Integer, ForeignKey('lists_in_clickup.list_id'))

    def __str__(self):
        return self.course_name


class WorksInClickUp(Base):
    __tablename__ = 'works_in_clickup'

    work_id = Column(Integer, primary_key=True)
    task_clickup_id = Column(Integer, unique=True, nullable=False)
    work_title = Column(String(255), nullable=False)
    due_date = Column(DateTime, nullable=True)
    description = Column(Text, nullable=True)
    link_to_work = Column(Text, nullable=True)
    classrom_course_id = Column(Integer, ForeignKey('courses_in_classroom.course_id'))

    def __str__(self):
        return self.work_title
