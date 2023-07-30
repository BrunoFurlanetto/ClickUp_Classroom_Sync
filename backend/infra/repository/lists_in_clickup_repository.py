from ..models.lists_in_clickup import ListsInClickUp
from ..repository.base_repository import BaseRepository


class ListsInClickUpRepository(BaseRepository):
    def __init__(self):
        super().__init__(self)
        self.model = ListsInClickUp
