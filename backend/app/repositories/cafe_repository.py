from sqlalchemy.orm import Session
from typing import Optional
from app.models.cafe import Cafe, NoiseLevel

class CafeRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 20, noise_level: Optional[NoiseLevel] = None):
        query = self.db.query(Cafe)
        if noise_level:
            query = query.filter(Cafe.noise_level == noise_level)
        return query.offset(skip).limit(limit).all()

    def get_by_id(self, cafe_id: int):
        return self.db.query(Cafe).filter(Cafe.id == cafe_id).first()