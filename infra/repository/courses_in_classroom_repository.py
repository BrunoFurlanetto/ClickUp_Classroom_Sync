from infra.models.courses_in_classroom import CoursesInClassroom
from infra.repository.base_repository import BaseRepository


class CoursesInClassroomRepository(BaseRepository):
    def __init__(self):
        super().__init__(self)
        self.model = CoursesInClassroom
