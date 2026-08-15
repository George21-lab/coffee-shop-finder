from typing import Optional
from app.repositories.cafe_repository import CafeRepository
from app.models.cafe import NoiseLevel

class CafeService:
    def __init__(self, repository: CafeRepository):
        self.repository = repository

    def list_cafes(self, skip: int = 0, limit: int = 20, noise_level: Optional[NoiseLevel] = None):
        return self.repository.get_all(skip=skip, limit=limit, noise_level=noise_level)

    def get_cafe(self, cafe_id: int):
        return self.repository.get_by_id(cafe_id)