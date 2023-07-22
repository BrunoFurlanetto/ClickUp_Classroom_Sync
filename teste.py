from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from random import randint, choice

from infra.models.courses_in_classroom import CoursesInClassroom
from infra.models.lists_in_clickup import ListsInClickUp
from infra.repository.courses_in_classroom_repository import CoursesInClassroomRepository
from infra.repository.lists_in_clickup_repository import ListsInClickUpRepository

# populate table with 100 different data
print(CoursesInClassroomRepository().select_all())
