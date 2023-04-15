from sqlalchemy import and_

from infra.configs.connections import DBConnectionHandler
from infra.models.works_in_clickup import WorksInClickUp
from infra.repository.base_repository import BaseRepository


class WorksInClickUpRepository(BaseRepository):
    def __init__(self):
        super().__init__(self)
        self.model = WorksInClickUp
