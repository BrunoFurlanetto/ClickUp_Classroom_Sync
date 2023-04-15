from infra.configs.connections import DBConnectionHandler
from infra.models.works_in_clickup import WorksInClickUp
from infra.repository.works_in_clickup_repository import WorksInClickUpRepository

WorksInClickUpRepository().update(
    fields_and_new_values={},
    work_title='Fazer uma apresentação',
    classrom_course_id=9
)
