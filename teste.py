from infra.configs.connections import DBConnectionHandler
from infra.models.works_in_clickup import WorksInClickUp
from infra.repository.lists_in_clickup_repository import ListsInClickUpRepository
from infra.repository.works_in_clickup_repository import WorksInClickUpRepository

print(ListsInClickUpRepository().select_all())
