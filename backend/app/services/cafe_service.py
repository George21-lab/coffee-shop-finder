from app.repositories.cafe_repository import CafeRepository

class CafeService:
    def __init__(self, repository: CafeRepository):
        self.repository = repository

    def list_cafes(self, skip: int = 0, limit: int = 20):
        return self.repository.get_all(skip=skip, limit=limit)

    def get_cafe(self, cafe_id: int):
        return self.repository.get_by_id(cafe_id)