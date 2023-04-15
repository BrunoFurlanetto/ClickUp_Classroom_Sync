from infra.models.lists_in_clickup import ListsInClickUp
from infra.repository.base_repository import BaseRepository


class ListsInClickUpRepository(BaseRepository):
    def __init__(self):
        super().__init__(self)
        self.model = ListsInClickUp
