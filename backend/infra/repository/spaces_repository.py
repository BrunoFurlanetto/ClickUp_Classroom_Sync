from backend.infra.models.spaces import Spaces
from backend.infra.repository.base_repository import BaseRepository


class SpacesRepository(BaseRepository):
    def __init__(self):
        super().__init__(self)
        self.model = Spaces
