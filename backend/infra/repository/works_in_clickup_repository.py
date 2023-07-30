from ..models.works_in_clickup import WorksInClickUp
from ..repository.base_repository import BaseRepository


class WorksInClickUpRepository(BaseRepository):
    def __init__(self):
        super().__init__(self)
        self.model = WorksInClickUp
